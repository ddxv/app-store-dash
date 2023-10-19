import datetime
import os

from litestar import Controller, get

from api_app.models import AppDetail, AppsOverview

from dbcon.queries import get_appstore_categories, query_recent_apps, get_single_app

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


def get_app_overview_dict() -> AppsOverview:
    new_apps = query_recent_apps(days=7)
    trending_apps = query_recent_apps(days=30)
    trending_ios_apps = trending_apps[~trending_apps["store"].str.contains("oogl")]
    trending_google_apps = trending_apps[trending_apps["store"].str.contains("oogl")]
    new_ios_dicts = new_apps[~new_apps["store"].str.contains("oogl")].to_dict(
        orient="records"
    )
    new_google_dicts = new_apps[new_apps["store"].str.contains("oogl")].to_dict(
        orient="records"
    )
    trending_google_dicts = trending_google_apps.to_dict(orient="records")
    trending_ios_dicts = trending_ios_apps.to_dict(orient="records")
    trending_title = "Trending Apps this Month"
    recent_title = "New Apps this Month"
    trending_dicts: dict = {}
    trending_dicts[trending_title] = {}
    trending_dicts[recent_title] = {}
    trending_dicts["new_google"] = new_google_dicts
    trending_dicts["new_ios"] = new_ios_dicts
    trending_dicts["trending_google"] = trending_google_dicts
    trending_dicts["trending_ios"] = trending_ios_dicts
    my_dict = AppsOverview(
        new_google=new_google_dicts,
        new_ios=new_ios_dicts,
        trending_google=trending_google_dicts,
        trending_ios=trending_ios_dicts,
    )
    return my_dict


class AppController(Controller):
    path = "/api/apps"

    @get(path="/")
    async def get_apps_overview(self) -> AppsOverview:
        """
        Handles a GET request for a list of apps

        Args:

        Returns:
            A dictionary representation of the list of apps for homepasge
        """
        logger.info("inside a request")
        home_dict = get_app_overview_dict()

        return home_dict

    @get(path="/{store_id:str}", cache=3600)
    async def get_app_detail(self, store_id: str) -> AppDetail:
        """
        Handles a GET request for a specific app.

        Args:
            store_id (str): The id of the app to retrieve.

        Returns:
            json
        """

        app_df = get_single_app(store_id)
        app_dict = app_df.to_dict(orient="records")[0]

        return app_dict