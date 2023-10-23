import datetime

from api_app.models import AppDetail, AppsOverview, Collection, StoreSection
from config import get_logger
from dbcon.queries import get_single_app, query_recent_apps
from litestar import Controller, get

logger = get_logger(__name__)

"""
/apps/{store_id} a specific app
"""


def get_string_date_from_days_ago(days: int) -> str:
    mydate = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    mydate_str = mydate.strftime("%Y-%m-%d")
    return mydate_str


def get_app_overview_dict() -> AppsOverview:
    new_weekly = query_recent_apps(period="weekly")
    new_monthly = query_recent_apps(period="monthly")
    monthly_ios_apps = new_monthly[~new_monthly["store"].str.contains("oogl")]
    monthly_google_apps = new_monthly[new_monthly["store"].str.contains("oogl")]
    weekly_ios_dicts = new_weekly[~new_weekly["store"].str.contains("oogl")].to_dict(
        orient="records"
    )
    weekly_google_dicts = new_weekly[new_weekly["store"].str.contains("oogl")].to_dict(
        orient="records"
    )
    monthly_google_dicts = monthly_google_apps.to_dict(orient="records")
    monthly_ios_dicts = monthly_ios_apps.to_dict(orient="records")
    monthly_title = "New Apps this Month"
    weekly_title = "New Apps this Week"
    my_dict = AppsOverview(
        new_weekly=Collection(
            title=weekly_title,
            google=StoreSection(title="Google", apps=weekly_google_dicts),
            ios=StoreSection(title="iOS", apps=weekly_ios_dicts),
        ),
        new_monthly=Collection(
            title=monthly_title,
            google=StoreSection(title="Google", apps=monthly_google_dicts),
            ios=StoreSection(title="iOS", apps=monthly_ios_dicts),
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
