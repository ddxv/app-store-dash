"""Return API endpoint for categories.

/categories/{category_id} a specific app
"""

from typing import Self

import numpy as np
from litestar import Controller, get
from litestar.config.response_cache import CACHE_FOREVER

from api_app.models import AppGroup, CategoriesOverview, Category
from config import get_logger
from dbcon.queries import get_appstore_categories, get_category_top_apps_by_installs

logger = get_logger(__name__)


def category_overview() -> CategoriesOverview:
    """Categories for apps."""
    cats = get_appstore_categories()
    cats = cats[cats["total_apps"] > 100]  # noqa: PLR2004 magic number ok

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
    """App Store Categories API."""

    path = "/api/categories"

    @get(path="/", cache=CACHE_FOREVER)
    async def get_categories_overview(self: Self) -> CategoriesOverview:
        """Handle GET request for a list of categories.

        Returns
        -------
            A dictionary representation of the list of categories
            each with an id, name, type and total of apps

        """
        logger.info(f"{self.path} start")
        overview = category_overview()
        logger.info(f"{self.path} return")

        return overview

    @get(path="/{category_id:str}", cache=86400)
    async def get_category(self: Self, category_id: str) -> Category:
        """Handle GET request for a single category.

        Returns
        -------
            A dictionary representation of a category
            with ios and google apps

        """
        logger.info(f"{self.path} start")
        df = get_category_top_apps_by_installs(category_id, limit=20)
        google = AppGroup(
            apps=(df[df["store"].str.contains("oogle")].to_dict(orient="records")),
            title="Google",
        )
        ios = AppGroup(
            apps=df[~df["store"].str.contains("oogle")].to_dict(orient="records"),
            title="iOS",
        )
        category = Category(key=category_id, ios=ios, google=google)
        return category
