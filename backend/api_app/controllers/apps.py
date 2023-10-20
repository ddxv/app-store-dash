import datetime
import os

from litestar import Controller, get

from api_app.models import AppDetail, AppsOverview, Section, AppGroup

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


def get_app_overview_dict() -> AppsOverview:
    new_apps = query_recent_apps(period="weekly")
    trending_apps = query_recent_apps(period="monthly")
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
    trending_title = "New Apps this Month"
    recent_title = "New Apps this Week"
    my_dict = AppsOverview(
        new=Section(
            title=recent_title,
            data=[
                AppGroup(title="Google", apps=new_google_dicts),
                AppGroup(title="iOS", apps=new_ios_dicts),
            ],
        ),
        trending=Section(
            title=trending_title,
            data=[
                AppGroup(title="Google", apps=trending_google_dicts),
                AppGroup(title="iOS", apps=trending_ios_dicts),
            ],
        ),
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
