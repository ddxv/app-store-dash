"""API for app data.

/apps/{store_id} a specific app
/apps/search/{search_term} search for apps
"""

import datetime
import time
import urllib.parse
from typing import Self

import numpy as np
import pandas as pd
from adscrawler import connection as write_conn
from adscrawler.app_stores import apple, google, scrape_stores
from litestar import Controller, Response, get
from litestar.background_tasks import BackgroundTask
from litestar.exceptions import NotFoundException

from api_app.models import (
    AdsTxtEntries,
    AppDetail,
    AppGroup,
    AppHistory,
    AppRank,
    Category,
    Collection,
    DeveloperApps,
    PackageDetails,
)
from config import get_logger
from dbcon.queries import (
    get_app_history,
    get_app_package_details,
    get_ranks_for_app,
    get_recent_apps,
    get_single_app,
    get_single_apps_adstxt,
    get_single_developer,
    get_total_counts,
    search_apps,
)

logger = get_logger(__name__)


def search_both_stores(search_term: str) -> None:
    """Search both stores and return resulting AppGroup."""
    google_full_results = google.search_play_store(search_term)
    if len(google_full_results) > 0:
        process_search_results(google_full_results)
    apple_ids = apple.search_app_store_for_ids(search_term)
    if len(apple_ids) > 0:
        apple_full_results = [
            {"store_id": store_id, "store": 2} for store_id in apple_ids
        ]
        process_search_results(apple_full_results)


def get_search_results(search_term: str) -> AppGroup:
    """Parse search term and return resulting APpGroup."""
    decoded_input = urllib.parse.unquote(search_term)
    df = search_apps(search_input=decoded_input, limit=20)
    logger.info(f"{decoded_input=} returned rows: {df.shape[0]}")
    apps_dict = df.to_dict(orient="records")
    app_group = AppGroup(title=search_term, apps=apps_dict)
    return app_group


def process_search_results(results: list[dict]) -> None:
    """After having queried an external app store send results to db."""
    logger.info("search results to try opening connection")
    db_conn = write_conn.get_db_connection(use_ssh_tunnel=True)
    db_conn.set_engine()
    logger.info("search results to be processed")
    scrape_stores.process_scraped(db_conn, results, "appgoblin_search")
    logger.info("search results done")


def get_playstore_results(search_term: str) -> AppGroup:
    """Parse search term and return resulting APpGroup."""
    decoded_input = urllib.parse.unquote(search_term)
    df = search_apps(search_input=decoded_input, limit=20)
    logger.info(f"{decoded_input=} returned rows: {df.shape[0]}")
    apps_dict = df.to_dict(orient="records")
    app_group = AppGroup(title=search_term, apps=apps_dict)
    return app_group


def app_history(store_app: int, app_name: str) -> AppHistory:
    """Get the history of app scraping."""
    app_hist = get_app_history(store_app)
    histogram = app_hist.sort_values(["id"]).tail(1)["histogram"].to_numpy()[0]
    history_table = (
        app_hist.sort_values("crawled_date", ascending=False)
        .drop(["id", "store_app"], axis=1)
        .to_dict(
            orient="records",
        )
    )
    app_hist["group"] = app_name
    app_hist = app_hist[
        ~((app_hist["installs"].isna()) & (app_hist["rating_count"].isna()))
    ]
    metrics = ["installs", "rating", "review_count", "rating_count"]
    group_col = "group"
    xaxis_col = "crawled_date"
    app_hist = app_hist.sort_values(xaxis_col)
    app_hist["date_change"] = app_hist[xaxis_col] - app_hist[xaxis_col].shift(1)
    app_hist["days_changed"] = app_hist["date_change"].apply(
        lambda x: np.nan if pd.isna(x) else x.days,
    )
    change_metrics = []
    for metric in metrics:
        app_hist[f"{metric}_change"] = app_hist[metric] - app_hist.shift(1)[metric]
        # Rate of Change
        app_hist[f"{metric}_rate_of_change"] = (
            app_hist[metric] - app_hist.shift(1)[metric]
        ) / app_hist.shift(1)[metric]
        # Treated as whole percentage by frontend
        app_hist[f"{metric}_rate_of_change"] = (
            app_hist[f"{metric}_rate_of_change"] * 100
        )
        # Avg Per Day
        app_hist[f"{metric}_avg_per_day"] = (
            app_hist[f"{metric}_change"] / app_hist["days_changed"]
        )
        change_metrics.append(metric + "_rate_of_change")
        change_metrics.append(metric + "_avg_per_day")
    app_hist = (
        app_hist[[group_col, xaxis_col, *change_metrics]]
        .drop(app_hist.index[0])
        .rename(
            columns={
                "installs_avg_per_day": "Installs Daily Average",
                "rating_count_avg_per_day": "Rating Count Daily Average",
                "review_count_avg_per_day": "Review Count Daily Average",
                "rating_rate_of_change": "Rating Rate of Change",
                "installs_rate_of_change": "Installs Rate of Change",
                "rating_count_rate_of_change": "Rating Count Rate of Change",
                "review_count_rate_of_change": "Review Count Rate of Change",
            },
        )
    )
    app_hist = app_hist.replace([np.inf, -np.inf], np.nan)
    app_hist = app_hist.dropna(axis="columns", how="all")
    if app_hist.empty:
        return app_hist.to_dict(orient="records")
    # Not useful column
    app_hist = app_hist.drop(["rating_avg_per_day"], axis=1, errors="ignore")
    # This is an odd step as it makes each group a metric
    # not for when more than 1 dimension
    mymelt = app_hist.melt(id_vars=xaxis_col).rename(columns={"variable": "group"})
    final_metrics = [x for x in app_hist.columns if x not in ["group", "crawled_date"]]
    number_dicts = []
    change_dicts = []
    ratings_dicts = []
    plot_dicts = {}
    for metric in final_metrics:
        meltdf = mymelt.loc[mymelt.group == metric]
        metric_dict = meltdf.to_dict(orient="records")
        if "Rate of Change" in metric:
            change_dicts += metric_dict
        else:
            number_dicts += metric_dict
        if metric == "Installs Daily Average":
            plot_dicts["installs"] = metric_dict
        if metric in ["Review Count Daily Average", "Rating Count Daily Average"]:
            ratings_dicts += metric_dict
    plot_dicts["numbers"] = number_dicts
    plot_dicts["ratings"] = ratings_dicts
    plot_dicts["changes"] = change_dicts
    hist = AppHistory(
        histogram=histogram,
        history_table=history_table,
        plot_data=plot_dicts,
    )
    return hist


def get_string_date_from_days_ago(days: int) -> str:
    """Get the stringified date from x days ago."""
    mydate = datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    mydate_str = mydate.strftime("%Y-%m-%d")
    return mydate_str


def get_app_overview_dict(collection: str) -> Collection:
    """Get collection overview."""
    category_limit = 20
    df = get_recent_apps(collection=collection, limit=category_limit)
    categories_dicts = []
    groups = df.groupby(["mapped_category"])
    for category_key, apps in groups:
        ios_dicts = (
            apps[~apps["store"].str.contains("oogl")]
            .head(category_limit)
            .to_dict(orient="records")
        )
        google_dicts = (
            apps[apps["store"].str.contains("oogl")]
            .head(category_limit)
            .to_dict(orient="records")
        )
        categories_dicts.append(
            Category(
                key=category_key,
                google=AppGroup(title="Google", apps=google_dicts),
                ios=AppGroup(title="iOS", apps=ios_dicts),
            ),
        )
    response_collection = Collection(
        title=COLLECTIONS[collection]["title"],
        categories=categories_dicts,
    )
    return response_collection


class AppController(Controller):
    """Controller holding all API endpoints for an app."""

    path = "/api/apps"

    @get(path="/overview", cache=86400)
    async def get_overview(self: Self) -> dict:
        """Handle GET request for a list of apps.

        Returns
        -------
            A dictionary representation of the total counts

        """
        start = time.perf_counter()
        overview_df = get_total_counts()
        overview_dict = overview_df.to_dict(orient="records")[0]
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return overview_dict

    @get(path="/collections/{collection:str}", cache=3600)
    async def get_apps_overview(self: Self, collection: str) -> Collection:
        """Handle GET request for a list of apps.

        Args:
        ----
            collection:collection

        Returns:
        -------
            A dictionary representation of the list of apps for homepage

        """
        start = time.perf_counter()
        home_dict = get_app_overview_dict(collection=collection)

        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return home_dict

    @get(path="/{store_id:str}", cache=3600)
    async def get_app_detail(self: Self, store_id: str) -> AppDetail:
        """Handle GET request for a specific app.

         store_id (str): The id of the app to retrieve.

        Returns
        -------
            json

        """
        start = time.perf_counter()
        app_df = get_single_app(store_id)
        if app_df.empty:
            msg = f"Store ID not found: {store_id!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        app_dict = app_df.to_dict(orient="records")[0]
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return app_dict

    @get(path="/{store_id:str}/history", cache=3600)
    async def get_app_history_details(self: Self, store_id: str) -> AppHistory:
        """Handle GET request for a specific app.

         store_id (str): The id of the app to retrieve.

        Returns
        -------
            json

        """
        start = time.perf_counter()
        app_df = get_single_app(store_id)
        if app_df.empty:
            msg = f"Store ID not found: {store_id!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        app_dict = app_df.to_dict(orient="records")[0]
        store_app = app_dict["id"]
        app_name = app_dict["name"]

        hist_dict = app_history(store_app=store_app, app_name=app_name)
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return hist_dict

    @get(path="/{store_id:str}/packageinfo", cache=3600)
    async def get_package_info(self: Self, store_id: str) -> PackageDetails:
        """Handle GET request for a specific app.

         store_id (str): The id of the app to retrieve.

        Returns
        -------
            json

        """
        start = time.perf_counter()

        df = get_app_package_details(store_id)

        if df.empty:
            msg = f"Package info for store ID not found: {store_id!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )

        cats = df.loc[df["category_slug"].notna(), "category_slug"].unique().tolist()
        company_cats = {}
        for cat in cats:
            company_cats[cat] = {
                k: f.groupby("xml_path")["value_name"].apply(list).to_dict()
                for k, f in df[df["category_slug"] == cat].groupby("company_domain")
            }

        is_permission = df["xml_path"] == "uses-permission"
        is_matching_packages = df["value_name"].str.startswith(
            ".".join(store_id.split(".")[:2]),
        )

        is_android_activity = df["value_name"].str.contains(
            r"^(com.android)|(android)",
        )

        permissions_df = df[is_permission]

        left_overs_df = df[
            ~is_permission
            & ~is_matching_packages
            & ~is_android_activity
            & df["company_name"].isna()
        ]
        permissions_list = permissions_df.value_name.tolist()
        permissions_list = [
            x.replace("android.permission.", "") for x in permissions_list
        ]

        trackers_dict = PackageDetails(
            company_categories=company_cats,
            permissions=permissions_list,
            leftovers=left_overs_df[["xml_path", "value_name"]]
            .groupby("xml_path")["value_name"]
            .apply(list)
            .to_dict(),
        )
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return trackers_dict

    @get(path="/{store_id:str}/ranks", cache=3600)
    async def app_ranks(self: Self, store_id: str) -> AppRank:
        """Handle GET requests for a specific app ranks.

        Args:
        ----
            store_id (str): The id of the store to retrieve.

        Returns:
        -------
            json

        """
        start = time.perf_counter()
        df = get_ranks_for_app(store_id=store_id)
        if df.empty:
            msg = f"Ranks not found for {store_id!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        df["rank_group"] = df["collection"] + ": " + df["category"]
        latest_dict = df[df["crawled_date"].max() == df["crawled_date"]][
            ["rank", "store", "crawled_date", "collection", "category"]
        ].to_dict(orient="records")
        df["crawled_date"] = pd.to_datetime(df["crawled_date"]).dt.strftime("%Y-%m-%d")
        pdf = df[["crawled_date", "rank", "rank_group"]].sort_values("crawled_date")
        # This format is for echarts, expects data series as columns
        hist_dict = (
            pdf.pivot_table(
                columns=["rank_group"],
                index=["crawled_date"],
                values="rank",
            )
            .reset_index()
            .to_dict(orient="records")
        )
        rank_dict = AppRank(latest=latest_dict, history=hist_dict)
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return rank_dict

    @get(path="/developers/{developer_id:str}", cache=3600)
    async def get_developer_apps(self: Self, developer_id: str) -> DeveloperApps:
        """Handle GET request for a specific developer.

        Args:
        ----
            developer_id (str): The id of the developer to retrieve.

        Returns:
        -------
            json

        """
        start = time.perf_counter()
        apps_df = get_single_developer(developer_id)

        if apps_df.empty:
            msg = f"Store ID not found: {developer_id!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        developer_name = apps_df.to_dict(orient="records")[0]["developer_name"]
        apps_dict = apps_df.to_dict(orient="records")

        developer_apps = DeveloperApps(
            developer_id=developer_id,
            title=developer_name,
            apps=apps_dict,
        )
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return developer_apps

    @get(path="/{store_id:str}/adstxt", cache=3600)
    async def get_developer_adstxt(self: Self, store_id: str) -> AdsTxtEntries:
        """Handle GET request for a store_id's related ads txt entries.

        Note these IDs are only connected to the app's developer's URL
        and thus are not app specific.

        Args:
        ----
            store_id (str): The url of the store_id's ads txt to retrieve

        Returns:
        -------
            json

        """
        start = time.perf_counter()
        adstxt_df = get_single_apps_adstxt(store_id)

        if adstxt_df.empty:
            msg = f"App's ads-txt entries not found: {store_id!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        direct_adstxt_dict = adstxt_df[
            adstxt_df["relationship"].str.upper() == "DIRECT"
        ].to_dict(orient="records")
        reseller_adstxt_dict = adstxt_df[
            adstxt_df["relationship"].str.upper() == "RESELLER"
        ].to_dict(orient="records")

        txts = AdsTxtEntries(
            direct_entries=direct_adstxt_dict,
            reseller_entries=reseller_adstxt_dict,
        )
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return txts

    @get(path="/search/{search_term:str}", cache=3600)
    async def search(self: Self, search_term: str) -> AppGroup:
        """Search apps and developers.

        Args:
        ----
            search_term: str the search term to search for.
                Can search packages, developers and app names.

        """
        start = time.perf_counter()
        apps_dict = get_search_results(search_term)
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        return Response(
            apps_dict,
            background=BackgroundTask(search_both_stores, search_term),
        )

    @get(path="/search/{search_term:str}/playstore", cache=3600)
    async def search_playstore(self: Self, search_term: str) -> AppGroup:
        """Search apps and developers.

        Args:
        ----
            search_term: str the search term to search for.
                Can search packages, developers and app names.

        """
        start = time.perf_counter()
        results = google.search_play_store(search_term)
        app_group = AppGroup(title="Google Playstore Results", apps=results)
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        if len(results) > 0:
            return Response(
                app_group,
                background=BackgroundTask(process_search_results, results),
            )
        return app_group

    @get(path="/search/{search_term:str}/applestore", cache=3600)
    async def search_applestore(self: Self, search_term: str) -> AppGroup:
        """Search apps and developers.

        Args:
        ----
            search_term: str the search term to search for.
                Can search packages, developers and app names.

        """
        logger.info(f"{self.path} term={search_term} for apple store")

        start = time.perf_counter()

        ids = apple.search_app_store_for_ids(search_term)
        full_results = [{"store_id": store_id, "store": 2} for store_id in ids]
        results = apple.app_details_for_ids(ids[:10])

        df = pd.DataFrame(results)
        df = apple.clean_ios_app_df(df)

        df["store_link"] = "https://apps.apple.com/us/app/-/id" + df["store_id"]

        results_dict = df.to_dict(orient="records")

        app_group = AppGroup(title="Apple App Store Results", apps=results_dict)
        duration = round((time.perf_counter() - start), 2)
        logger.info(f"{self.path} took {duration}ms")
        if len(results) > 0:
            return Response(
                app_group,
                background=BackgroundTask(process_search_results, full_results),
            )
        return app_group


COLLECTIONS = {
    "new_weekly": {"title": "New Apps this Week"},
    "new_monthly": {"title": "New Apps this Month"},
    "new_yearly": {"title": "New Apps this Year"},
    "top": {"title": "Alltime Top"},
}
