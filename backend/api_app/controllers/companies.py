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
    metric = "installs" if "installs" in df.columns else "app_count"
    overall_cat_df = df.groupby("name")[[metric, f"total_{metric}"]].sum().reset_index()
    overall_cat_df["mapped_category"] = "overall"
    overall_cat_df["percent"] = (
        overall_cat_df[metric] / overall_cat_df[f"total_{metric}"]
    )
    df = pd.concat([df, overall_cat_df])
    df = append_games_category(df, metric)
    return df


def append_games_category(df: pd.DataFrame, metric: str) -> pd.DataFrame:
    """Append a consolidated games category.

    note this wouldn't work for Apple as not needed.
    """
    overall_cat_df = (
        df[df["mapped_category"].str.contains(r"^game")]
        .groupby("name")[[metric, f"total_{metric}"]]
        .sum()
        .reset_index()
    )
    overall_cat_df["mapped_category"] = "games"
    overall_cat_df["percent"] = (
        overall_cat_df[metric] / overall_cat_df[f"total_{metric}"]
    )
    df = pd.concat([df, overall_cat_df])
    return df


def companies_overview(categories: list[int]) -> TopCompanies:
    """Process networks and return TopCompanies class."""
    df = get_top_companies(categories=categories, group_by_parent=False)
    mdf = get_top_companies(categories=categories, monthly=True)
    monthly_parents = get_top_companies(
        categories=categories,
        monthly=True,
        group_by_parent=True,
    )

    mdf = mdf[~mdf["company_name"].isna()].rename(columns={"company_name": "name"})
    monthly_all = (
        mdf.groupby(["mapped_category", "name"])[["installs", "total_installs"]]
        .agg(
            {"installs": "sum", "total_installs": "first"},
        )
        .reset_index()
    )

    monthly_parents = monthly_parents.rename(columns={"company_name": "name"})

    monthly_all["percent"] = monthly_all["installs"] / monthly_all["total_installs"]
    monthly_parents["percent"] = (
        monthly_parents["installs"] / monthly_all["total_installs"]
    )

    pdf = get_top_companies(categories=categories, group_by_parent=True)
    df = df[~df["name"].isna()]
    pdf = pdf[~pdf["name"].isna()]

    df = append_overall_categories(df)
    pdf = append_overall_categories(pdf)

    monthly_all = append_overall_categories(monthly_all)
    monthly_parents = append_overall_categories(monthly_parents)

    # Function to transform each group into a list of dictionaries
    def transform_group(group: pd.Grouper) -> dict:
        return group.drop(columns="mapped_category").to_dict(orient="records")

    df = df.sort_values("app_count", ascending=False)
    pdf = pdf.sort_values("app_count", ascending=False)
    monthly_all = monthly_all.sort_values("installs", ascending=False)
    monthly_parents = monthly_parents.sort_values("installs", ascending=False)
    top = TopCompanies(
        all_companies=df.groupby("mapped_category").apply(transform_group).to_dict(),
        parent_companies=pdf.groupby("mapped_category")
        .apply(transform_group)
        .to_dict(),
        monthly_all_companies=monthly_all.groupby("mapped_category")
        .apply(transform_group)
        .to_dict(),
        monthly_parent_companies=monthly_parents.groupby("mapped_category")
        .apply(transform_group)
        .to_dict(),
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

    @get(path="/companies/{company_name:str}", cache=3600)
    async def get_company_apps(self: Self, company_name: str) -> CompanyApps:
        """Handle GET request for a specific company.

        Args:
        ----
            company_name: The name of the company to retrieve apps for.

        Returns:
        -------
            CompanyApps.

        """
        logger.info(f"{self.path}/companies start")
        apps_df = get_apps_for_company(company_name, include_parents=True)

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
