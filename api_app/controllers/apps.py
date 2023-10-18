import datetime
import os

from litestar import Controller, get

from api_app.models import AppDetail, AppOverview
from config.config import IMAGES_DIR

"""
/apps/{store_id} a specific app
"""


def get_string_date_from_days_ago(days: int) -> str:
    mydate = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    mydate_str = mydate.strftime("%Y-%m-%d")
    return mydate_str


def get_most_recent_storm_dirs() -> tuple[str, list[str]]:
    storm_dirs: list = []
    i = 0
    while len(storm_dirs) == 0 and i <= 5:
        date_str = get_string_date_from_days_ago(i)
        if date_str in os.listdir(IMAGES_DIR):
            storm_dirs = os.listdir(f"{IMAGES_DIR}/{date_str}")
            print(f"{date_str=} found {len(storm_dirs)} directories")
        else:
            print(f"{date_str=} found no directories")
        i += 1
    return date_str, storm_dirs


class AppController(Controller):
    path = "/api/apps"

    @get(path="/")
    async def get_apps_overview(self) -> AppOverview:
        """
        Handles a GET request for a list of apps

        Args:

        Returns:
            Storms: A dictionary representation of the list of apps.
        """
        date_str, storm_dirs = get_most_recent_storm_dirs()

        mydict = Storms([Storm(id=mystorm, date=date_str) for mystorm in storm_dirs])

        return mydict

    @get(path="/{store_id:str}", cache=3600)
    async def get_storm_image(self, store_id: str) -> AppDetail:
        """
        Handles a GET request for a specific app.

        Args:
            store_id (str): The id of the app to retrieve.

        Returns:
            json
        """

        app_dict = {"store_id"}
        return app_dict
