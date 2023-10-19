import datetime
import os

from litestar import Controller, get

from api_app.models import CategoriesOverview

from dbcon.queries import get_appstore_categories

from config import get_logger

logger = get_logger(__name__)

"""
/apps/{store_id} a specific app
"""


def get_string_date_from_days_ago(days: int) -> str:
    mydate = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    mydate_str = mydate.strftime("%Y-%m-%d")
    return mydate_str


def category_overview() -> dict:
    cats = get_appstore_categories()
    # Make app count strings
    cats["android"] = cats["android"].apply(
        lambda x: "{:,.0f}".format(x) if x else "N/A"
    )
    cats["ios"] = cats["ios"].apply(lambda x: "{:,.0f}".format(x) if x else "N/A")
    category_dicts = cats.to_dict(orient="records")
    return category_dicts


class AppController(Controller):
    path = "/api/categories"

    @get(path="/")
    async def get_apps_overview(self) -> CategoriesOverview:
        """
        Handles a GET request for a list of categories

        Args:

        Returns:
            A dictionary representation of the list of apps for homepasge
        """
        logger.info("inside a request")
        home_dict = get_appstore_categories()

        return home_dict
