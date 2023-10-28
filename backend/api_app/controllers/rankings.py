from api_app.models import (
    RankingOverview,
    StoreCollections,
    StoreCategoryDetail,
)
from config import get_logger

from dbcon.queries import (
    get_ranks,
    get_store_collection_category_map,
)
from litestar import Controller, get

logger = get_logger(__name__)

"""
/categories/{category_id} a specific app
"""


def ranking_map() -> RankingOverview:
    df = get_store_collection_category_map()
    overview = RankingOverview()

    groups = df.groupby("store_id")
    for store, group in groups:
        store_collections = StoreCollections()
        cgroups = group.groupby("collection_id")
        for col_id, cgroup in cgroups:
            category_details = [
                StoreCategoryDetail(row["category_id"], row["category_name"])
                for _, row in cgroup.iterrows()
            ]
            store_collections.categories.extend(category_details)
        overview.store_collections[store] = store_collections

    return overview


# def ranking_map() -> RankingOverview:
#     df = get_store_collection_category_map()
#     my_dict: RankingOverview = {}
#     groups = df.groupby("store_id")
#     for store, group in groups:
#         my_dict[store] = {}
#         cgroups = group.groupby("collection_id")
#         for col_id, cgroup in cgroups:
#             my_dict[store][col_id] = {}
#             my_dict[store][col_id]["categories"] = cgroup[
#                 ["category_id", "category_name"]
#             ].to_dict(orient="records")
#     return my_dict


class RankingsController(Controller):
    path = "/api/rankings/"

    @get(path="/", cache=True)
    async def get_ranking_overview(self) -> RankingOverview:
        """
        Handles a GET request for a list of ranking collecitons and categories

        Returns:
            A dictionary representation of the list of categories
            each with an id, name, type and total of apps
        """
        logger.info(f"{self.path} start")
        overview = ranking_map()

        return overview

    @get(path="/{store:int}/{collection_id:int}/{category_id:int}", cache=3600)
    async def get_ranking(
        self, store: int, collection_id: int, category_id: int, category: int
    ) -> dict:
        """
        Handles a GET request for a collection+category rank

        Returns:
            A dictionary representation of a category
            with ios and google apps
        """
        logger.info(f"{self.path} start")
        df = get_ranks(
            store=store, collection_id=collection_id, category_id=category_id, limit=50
        )
        ranks_dict = df.to_dict(orient="records")

        return ranks_dict
