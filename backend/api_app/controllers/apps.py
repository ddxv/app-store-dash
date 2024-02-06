import datetime
import urllib.parse

import numpy as np
import pandas as pd
from litestar import Controller, get
from litestar.exceptions import NotFoundException

from api_app.models import (
    AppDetail,
    AppGroup,
    AppRank,
    Category,
    Collection,
    DeveloperApps,
)
from config import get_logger
from dbcon.queries import (
    get_single_app,
    query_app_history,
    query_ranks_for_app,
    query_recent_apps,
    query_single_developer,
    search_apps,
)

logger = get_logger(__name__)

"""
/apps/{store_id} a specific app
"""


def get_search_results(search_term: str) -> AppGroup:
    """Parse search term and return resulting APpGroup."""
    decoded_input = urllib.parse.unquote(search_term)
    df = search_apps(search_input=decoded_input, limit=20)
    logger.info(f"{decoded_input=} returned rows: {df.shape[0]}")
    apps_dict = df.to_dict(orient="records")
    app_group = AppGroup(title=search_term, apps=apps_dict)
    return app_group


def get_app_history(app_dict: dict) -> dict:
    store_app = app_dict["id"]
    app_name = app_dict["name"]

    app_hist = query_app_history(store_app)
    app_dict["histogram"] = app_hist.sort_values(["id"]).tail(1)["histogram"].values[0]
    app_dict["history_table"] = app_hist.drop(["id", "store_app"], axis=1).to_dict(
        orient="records",
    )
    app_hist["group"] = app_name
    app_hist = app_hist[
        ~((app_hist["installs"].isnull()) & (app_hist["rating_count"].isnull()))
    ]
    metrics = ["installs", "rating", "review_count", "rating_count"]
    group_col = "group"
    xaxis_col = "crawled_date"
    app_hist = app_hist.sort_values(xaxis_col)
    app_hist["date_change"] = app_hist[xaxis_col] - app_hist[xaxis_col].shift(1)
    app_hist["days_changed"] = app_hist["date_change"].apply(
        lambda x: np.nan if pd.isnull(x) else x.days,
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
        app_hist[[group_col, xaxis_col] + change_metrics]
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
    # TODO: KEEP?
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
    for metric in final_metrics:
        meltdf = mymelt.loc[mymelt.group == metric]
        # meltdf = meltdf.rename(columns={"value": "percentage_value"})
        melteddicts = meltdf.to_dict(orient="records")
        if "Rate of Change" in metric:
            change_dicts += melteddicts
        else:
            number_dicts += melteddicts
    my_dicts = {"numbers": number_dicts, "changes": change_dicts}
    return my_dicts


def get_string_date_from_days_ago(days: int) -> str:
    mydate = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    mydate_str = mydate.strftime("%Y-%m-%d")
    return mydate_str


def get_app_overview_dict(collection: str) -> Collection:
    category_limit = 20
    df = query_recent_apps(collection=collection, limit=category_limit)
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
    path = "/api/apps"

    @get(path="/collections/{collection:str}", cache=3600)
    async def get_apps_overview(self, collection: str) -> Collection:
        """Handle GET request for a list of apps.

        Args:
        ----
            collection:collection

        Returns:
        -------
            A dictionary representation of the list of apps for homepasge

        """
        logger.info(f"{self.path} start {collection=}")
        # print(f"collection={collection}")
        home_dict = get_app_overview_dict(collection=collection)

        logger.info(f"{self.path} return")
        return home_dict

    @get(path="/{store_id:str}", cache=3600)
    async def get_app_detail(self, store_id: str) -> AppDetail:
        """Handle GET request for a specific app.

         store_id (str): The id of the app to retrieve.

        Returns
        -------
            json

        """
        logger.info(f"{self.path} start")
        app_df = get_single_app(store_id)
        if app_df.empty:
            raise NotFoundException(
                f"Store ID not found: {store_id!r}",
                status_code=404,
            )
        app_dict = app_df.to_dict(orient="records")[0]
        app_hist_dict = get_app_history(app_dict)
        app_dict["historyData"] = app_hist_dict
        return app_dict

    @get(path="/{store_id:str}/ranks", cache=3600)
    async def app_ranks(self, store_id: str) -> AppRank:
        """Handles a GET request for a specific app ranks.

        Args:
        ----
            store_id (str): The id of the store to retrieve.

        Returns:
        -------
            json

        """
        logger.info(f"{self.path} start")
        df = query_ranks_for_app(store_id=store_id)
        if df.empty:
            raise NotFoundException(
                f"Ranks not found for {store_id!r}",
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
            pdf.pivot(columns=["rank_group"], index=["crawled_date"], values="rank")
            .reset_index()
            .to_dict(orient="records")
        )
        rank_dict = AppRank(latest=latest_dict, history=hist_dict)
        return rank_dict

    @get(path="/developers/{developer_id:str}", cache=3600)
    async def get_developer_apps(self, developer_id: str) -> DeveloperApps:
        """Handles a GET request for a specific developer.

        Args:
        ----
            developer_id (str): The id of the developer to retrieve.

        Returns:
        -------
            json

        """
        logger.info(f"{self.path} start")
        apps_df = query_single_developer(developer_id)

        if apps_df.empty:
            raise NotFoundException(
                f"Store ID not found: {developer_id!r}",
                status_code=404,
            )
        developer_name = apps_df.to_dict(orient="records")[0]["developer_name"]
        apps_dict = apps_df.to_dict(orient="records")

        developer_apps = DeveloperApps(
            developer_id=developer_id,
            title=developer_name,
            apps=apps_dict,
        )
        return developer_apps

    @get(path="/search/{search_term:str}", cache=3600)
    async def search(self, search_term: str) -> AppGroup:
        logger.info(f"{self.path} term={search_term}")

        apps_dict = get_search_results(search_term)
        return apps_dict


COLLECTIONS = {
    "new_weekly": {"title": "New Apps this Week"},
    "new_monthly": {"title": "New Apps this Month"},
    "new_yearly": {"title": "New Apps this Year"},
    "top": {"title": "Alltime Top"},
}
