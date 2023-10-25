import numpy as np

from api_app.models import CategoriesOverview, Category
from config import get_logger


from dbcon.queries import get_appstore_categories, get_category_top_apps_by_installs
from litestar import Controller, get

logger = get_logger(__name__)

"""
/categories/{category_id} a specific app
"""


def category_overview() -> CategoriesOverview:
    cats = get_appstore_categories()
    cats = cats[cats["total_apps"] > 100]

    cats["name"] = cats["category"]
    cats["name"] = (
        cats["name"]
        .str.replace("game_", "")
        .str.replace("_and_", " & ")
        .str.replace("_", " ")
        .str.title()
    )
    cats = cats.rename(columns={"category": "id"})

    summary = cats[["android", "ios", "total_apps"]].sum()
    summary["name"] = "Overall"
    summary["id"] = "overall"
    cats.loc["Overall"] = summary

    cats[["android", "ios", "total_apps"]] = cats[
        ["android", "ios", "total_apps"]
    ].astype(int)

    cats = cats.sort_values("total_apps", ascending=False)

    cats["type"] = np.where(cats.id.str.contains("_game|games"), "game", "app")

    category_dicts = cats.to_dict(orient="records")

    overview = CategoriesOverview(categories=category_dicts)

    return overview


class CategoryController(Controller):
    path = "/api/categories"

    @get(path="/", cache=True)
    async def get_categories_overview(self) -> CategoriesOverview:
        """
        Handles a GET request for a list of categories

        Returns:
            A dictionary representation of the list of categories
            each with an id, name, type and total of apps
        """
        logger.info(f"{self.path} start")
        overview = category_overview()

        return overview

    @get(path="/{category_id:str}", cache=3600)
    async def get_category(self, category_id: str) -> Category:
        """
        Handles a GET request for a single category

        Returns:
            A dictionary representation of a category
            with ios and google apps
        """
        logger.info(f"{self.path} start")
        df = get_category_top_apps_by_installs(category_id, limit=20)
        google = df[df["store"].str.contains("oogle")].to_dict(orient="records")
        ios = df[~df["store"].str.contains("oogle")].to_dict(orient="records")
        category = Category(key=category_id, ios=ios, google=google)
        return category
