import datetime

from api_app.models import CategoriesOverview
from config import get_logger


from dbcon.queries import get_appstore_categories
from litestar import Controller, get

logger = get_logger(__name__)

"""
/categories/{category_id} a specific app
"""


def get_string_date_from_days_ago(days: int) -> str:
    mydate = datetime.datetime.utcnow() - datetime.timedelta(days=days)
    mydate_str = mydate.strftime("%Y-%m-%d")
    return mydate_str


def category_overview() -> dict:
    cats = get_appstore_categories()
    cats = cats[cats["total_apps"] > 100]
    categories = cats["category"].unique().tolist()

    game_categories = [x for x in categories if "game_" in x]
    app_categories = [x for x in categories if x not in game_categories]

    apps = [{"id": x, "name": x.replace("_", " ").title()} for x in app_categories]

    games = [
        {"id": x, "name": x.replace("game_", "").replace("_", " ").title()}
        for x in game_categories
    ]

    category_dicts = CategoriesOverview(apps=apps, games=games)

    return category_dicts


class AppController(Controller):
    path = "/api/categories"

    @get(path="/")
    async def get_categories_overview(self) -> CategoriesOverview:
        """
        Handles a GET request for a list of categories

        Returns:
            A dictionary representation of the list of categories
            each with an id, name and total of installs
        """
        logger.info("inside a request")
        my_dict = category_overview()

        return my_dict
