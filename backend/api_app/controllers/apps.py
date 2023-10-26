import datetime

from api_app.models import (
    AppDetail,
    Collection,
    AppGroup,
    Category,
)
from config import get_logger
from dbcon.queries import (
    get_single_app,
    query_recent_apps,
    get_app_history,
    search_apps,
)
from litestar import Controller, get
from litestar.exceptions import NotFoundException

logger = get_logger(__name__)

"""
/apps/{store_id} a specific app
"""


def get_search_results(search_term: str) -> AppGroup:
    df = search_apps(search_input=search_term, limit=20)
    apps_dict = df.to_dict(orient="records")
    app_group = AppGroup(title=search_term, apps=apps_dict)
    return app_group


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
            )
        )
    response_collection = Collection(
        title=COLLECTIONS[collection]["title"], categories=categories_dicts
    )
    return response_collection


class AppController(Controller):
    path = "/api/apps"

    @get(path="/collections/{collection:str}", cache=3600)
    async def get_apps_overview(self, collection: str) -> Collection:
        """
        Handles a GET request for a list of apps

        Args:
            collection:collection

        Returns:
            A dictionary representation of the list of apps for homepasge
        """
        logger.info(f"{self.path} start")
        print(f"collection={collection}")
        home_dict = get_app_overview_dict(collection=collection)

        logger.info(f"{self.path} return")
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
        logger.info(f"{self.path} start")

        app_df = get_single_app(store_id)
        if app_df.empty:
            raise NotFoundException(
                f"Store ID not found: {store_id!r}", status_code=404
            )
        app_dict = app_df.to_dict(orient="records")[0]
        store_app = app_dict["id"]
        app_hist = get_app_history(store_app)
        app_dict["histogram"] = (
            app_hist.sort_values(["id"]).tail(1)["histogram"].values[0]
        )
        app_dict["history_table"] = (
            app_hist.drop(["id", "store_app"], axis=1)
            .style.format(precision=0, thousands=",", decimal=".")
            .to_html(index=None, classes="pretty-table")
        )

        return app_dict

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
