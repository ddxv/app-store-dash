"""API endoipoints for companies.

/networks/ returns list of top networks.
/trackers/ returns list of top trackers.
"""

from typing import Self

import pandas as pd
from litestar import Controller, get
from litestar.exceptions import NotFoundException

from api_app.models import CompanyApps, TopCompanies
from config import get_logger
from dbcon.queries import get_apps_for_company, get_top_companies

logger = get_logger(__name__)


def append_overall_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Add single row for overall category."""
    metrics = ["installs", "app_count", "ratings"]
    total_cols = ["total_ratings", "total_installs", "category_total_apps"]
    overall_totals = (
        df.groupby(["store", "mapped_category"])[total_cols]
        .first()
        .reset_index()
        .groupby(["store"])[total_cols]
        .sum()
    )
    overall_company_df = df.groupby(["store", "name"])[metrics].sum().reset_index()
    overall_df = overall_company_df.merge(
        overall_totals,
        how="left",
        on="store",
        validate="m:1",
    )
    overall_df["mapped_category"] = "overall"
    df = pd.concat([df, overall_df])
    """Append a consolidated games category.
    note this wouldn't work for Apple as not needed.
    """
    games_cat_df = (
        df.loc[(df["mapped_category"].str.contains(r"^game"))]
        .groupby(["store", "name"])[metrics + total_cols]
        .sum()
        .reset_index()
    )
    games_cat_df["mapped_category"] = "games"
    df = pd.concat([df, games_cat_df])
    return df


def companies_overview(categories: list[int]) -> TopCompanies:
    """Process networks and return TopCompanies class."""
    df = get_top_companies(categories=categories)
    df_parents = get_top_companies(
        categories=categories,
        group_by_parent=True,
    )

    df = df[~df["company_name"].isna()].rename(columns={"company_name": "name"})
    df_parents = df_parents.rename(columns={"company_name": "name"})

    # Append combined columns like "overall" and "games"
    df = append_overall_categories(df)
    df_parents = append_overall_categories(df_parents)

    # Since new columns added, recalculate percentages
    df["app_count_percent"] = df["app_count"] / df["category_total_apps"]
    df["installs_percent"] = df["installs"] / df["total_installs"]
    df["ratings_percent"] = df["ratings"] / df["total_ratings"]
    df_parents["app_count_percent"] = (
        df_parents["app_count"] / df_parents["category_total_apps"]
    )
    df_parents["installs_percent"] = (
        df_parents["installs"] / df_parents["total_installs"]
    )
    df_parents["ratings_percent"] = df_parents["ratings"] / df_parents["total_ratings"]

    df = df.sort_values(
        ["app_count_percent", "installs", "ratings"],
        ascending=False,
        na_position="first",
    )
    df_parents = df_parents.sort_values(
        ["app_count_percent", "installs", "ratings"],
        ascending=False,
        na_position="first",
    )

    required_columns = [
        "store",
        "mapped_category",
        "name",
        "installs",
        "ratings",
        "app_count",
        "installs_percent",
        "ratings_percent",
        "app_count_percent",
    ]

    df = df[[*required_columns, "parent_company_name"]]
    df_parents = df_parents[required_columns]

    def transform_group(group: pd.DataFrame) -> dict:
        return group.drop(columns=["store", "mapped_category"]).to_dict(
            orient="records",
        )

    top = TopCompanies(
        all_companies=df.groupby(["store", "mapped_category"])
        .apply(transform_group)
        .unstack(level=1)
        .to_dict(orient="index"),
        parent_companies=df_parents.groupby(["store", "mapped_category"])
        .apply(transform_group)
        .unstack(level=1)
        .to_dict(orient="index"),
    )
    return top


class CompaniesController(Controller):

    """API EndPoint return for all ad tech companies."""

    path = "/api/"

    @get(path="/networks", cache=3600)
    async def top_networks(self: Self) -> TopCompanies:
        """Handle GET request for a list of top networks.

        Returns
        -------
            A dictionary representation of the list of networks
            each with an id, name, type and total of apps.

        """
        logger.info(f"{self.path}/networks start")
        overview = companies_overview(categories=[1])

        return overview

    @get(path="/trackers", cache=3600)
    async def top_trackers(self: Self) -> TopCompanies:
        """Handle GET request for a list of top trackers.

        Returns
        -------
            A dictionary representation of the list of trackers
            each with an id, name, type and total of apps.

        """
        logger.info(f"{self.path}/trackers start")
        overview = companies_overview(categories=[2, 3])

        return overview

    @get(
        path="/companies/{company_name:str}/{store_name:str}/{category_name:str}",
        cache=3600,
    )
    async def get_company_apps(
        self: Self,
        company_name: str,
        store_name: str,
        category_name: str,
    ) -> CompanyApps:
        """Handle GET request for a specific company.

        Args:
        ----
            company_name: The name of the company to retrieve apps for.
            store_name: The name of the store to retrieve apps for.
            category_name: The name of the category to retrieve apps for.

        Returns:
        -------
            CompanyApps.

        """
        logger.info(f"{self.path}/companies start")

        if store_name == "Google":
            store_id = 1
        elif store_name == "Apple":
            store_id = 2
        else:
            msg = f"Store Name not found: {store_name!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )

        apps_df = get_apps_for_company(
            company_name=company_name,
            store_id=store_id,
            mapped_category=category_name,
            include_parents=True,
        )

        if apps_df.empty:
            msg = f"Network Name not found: {company_name!r}"
            raise NotFoundException(
                msg,
                status_code=404,
            )
        apps_dict = apps_df.to_dict(orient="records")

        apps = CompanyApps(
            title=company_name,
            apps=apps_dict,
        )
        return apps
