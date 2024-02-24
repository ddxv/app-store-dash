"""API endoipoints for companies.

/networks/ returns list of top networks.
/trackers/ returns list of top trackers.
"""

from typing import Self

from litestar import Controller, get
from litestar.exceptions import NotFoundException

from api_app.models import CompanyApps, TopCompanies
from config import get_logger
from dbcon.queries import get_apps_for_company, get_top_companies

logger = get_logger(__name__)


def companies_overview(categories: list[int]) -> TopCompanies:
    """Process networks and return TopCompanies class."""
    df = get_top_companies(categories=categories, group_by_parent=False)
    mdf = get_top_companies(categories=categories, monthly=True)
    monthly_parents = get_top_companies(
        categories=categories,
        monthly=True,
        group_by_parent=True,
    )

    total_installs = mdf["total_installs"].to_numpy()[0]

    mdf = mdf[~mdf["company_name"].isna()].rename(columns={"company_name": "name"})
    monthly_all = (
        mdf.groupby("name")[["installs", "total_installs"]]
        .agg(
            {"installs": "sum", "total_installs": "first"},
        )
        .reset_index()
    )

    monthly_parents = monthly_parents.rename(columns={"company_name": "name"})

    monthly_all["percent"] = monthly_all["installs"] / total_installs
    monthly_parents["percent"] = monthly_parents["installs"] / total_installs

    pdf = get_top_companies(categories=categories, group_by_parent=True)
    df = df[~df["name"].isna()]
    pdf = pdf[~pdf["name"].isna()]
    df = df.sort_values("app_count", ascending=False)
    pdf = pdf.sort_values("app_count", ascending=False)
    monthly_all = monthly_all.sort_values("installs", ascending=False)
    monthly_parents = monthly_parents.sort_values("installs", ascending=False)
    top = TopCompanies(
        all_companies=df.to_dict(orient="records"),
        parent_companies=pdf.to_dict(orient="records"),
        monthly_all_companies=monthly_all.to_dict(orient="records"),
        monthly_parent_companies=monthly_parents.to_dict(orient="records"),
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
