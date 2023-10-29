from api_app.models import (
    RankingOverview,
    StoreCollections,
    StoreCategoryDetail,
    StoreRankings,
)
from config import get_logger

from dbcon.queries import (
    get_ranks,
    get_store_collection_category_map,
    get_ranks_for_app,
)
from litestar import Controller, get

logger = get_logger(__name__)

"""
/rankings/ of all apps as pulled from stores 
"""


def ranking_map() -> RankingOverview:
    df = get_store_collection_category_map()
    overview = RankingOverview()
    groups = df.groupby(["store_id", "store_name"])
    for store_idx, group in groups:
        store_id = int(store_idx[0])
        store_name = store_idx[1]
        cgroups = group.groupby(["collection_id", "collection_name"])
        rankings = StoreRankings(store_id=store_id, store_name=store_name)
        for col_idx, cgroup in cgroups:
            collection_id = int(col_idx[0])
            collection_name = col_idx[1]
            category_details = [
                StoreCategoryDetail(
                    category_id=int(row["category_id"]),
                    category_name=row["category_name"],
                )
                for _, row in cgroup.iterrows()
                if row["category_id"]
            ]
            rankings.collections.append(
                StoreCollections(
                    collection_id=collection_id,
                    collection_name=collection_name,
                    categories=category_details,
                )
            )
        overview.stores_rankings.append(rankings)
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

    # @get(path="/{store:int}/{collection_id:int}/{category_id:int}", cache=3600)
    # async def get_ranking(
    #     self, store: int, collection_id: int, category_id: int, category: int
    # ) -> dict:
    #     """
    #     Handles a GET request for a collection+category rank

    #     Returns:
    #         A dictionary representation of a category
    #         with ios and google apps
    #     """
    #     logger.info(f"{self.path} start")
    #     df = get_ranks(
    #         store=store, collection_id=collection_id, category_id=category_id, limit=50
    #     )
    #     ranks_dict = df.to_dict(orient="records")

    #     return ranks_dict

    @get(path="/{store:int}/{store_app:int}", cache=3600)
    async def get_ranking(self, store: int, store_app: int) -> dict:
        """
        Handles a GET request for a collection+category rank

        Returns:
            A dictionary representation of a category
            with ios and google apps
        """
        logger.info(f"{self.path} start")
        df = get_ranks_for_app(store=store, store_app=store_app)
        ranks_dict = df.to_dict(orient="records")

        return ranks_dict
