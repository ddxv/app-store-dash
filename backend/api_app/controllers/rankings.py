from api_app.models import (
    RankingOverview,
    StoreCollections,
    StoreCategoryDetail,
    StoreRankings,
)
from config import get_logger
import pandas as pd
import datetime

from dbcon.queries import (
    get_store_collection_category_map,
    get_most_recent_top_ranks,
    get_history_top_ranks,
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

    @get(path="/{store:int}/{collection:int}/{category:int}/short", cache=40000)
    async def get_short_ranks_for_category(
        self, store: int, collection: int, category: int
    ) -> dict:
        """
        Handles a GET request for a store/collection/category rank

        Returns:
            A dictionary representation of a category
            with ios and google apps
        """
        logger.info(f"{self.path} start for store/collection/category")
        df = get_most_recent_top_ranks(
            store=store,
            collection_id=collection,
            category_id=category,
            limit=5,
        )
        ranks_dict = df.to_dict(orient="records")
        return {"ranks": ranks_dict}

    @get(path="/{store:int}/{collection:int}/{category:int}", cache=3600)
    async def get_ranks_for_category(
        self, store: int, collection: int, category: int
    ) -> dict:
        """
        Handles a GET request for a store/collection/category rank

        Returns:
            A dictionary representation of a category
            with ios and google apps
        """
        logger.info(f"{self.path} start for store/collection/category")
        df = get_most_recent_top_ranks(
            store=store,
            collection_id=collection,
            category_id=category,
            limit=20,
        )
        ranks_dict = df.to_dict(orient="records")
        return {"ranks": ranks_dict}

    @get(path="/{store:int}/{collection:int}/{category:int}/history", cache=3600)
    async def get_ranks_history_for_category(
        self, store: int, collection: int, category: int
    ) -> dict:
        """
        Handles a GET request for a store/collection/category rank

        Returns:
            A list of dictionary representation of a category history
            with ios or google apps
        """
        logger.info(f"{self.path} start for store/collection/category")
        df = get_history_top_ranks(
            store=store,
            collection_id=collection,
            category_id=category,
            limit=10,
            days=30,
        )
        df["crawled_date"] = pd.to_datetime(df["crawled_date"])
        last_crawled_date = df["crawled_date"].max()
        # Sort by 'crawled_date' to make sure the latest dates are last
        df = df.sort_values("crawled_date", ascending=True)
        # NOTE: don't include 'rank' in group by as table is already unique by that
        # Need to get each apps location on that time
        df = (
            df.groupby([pd.Grouper(key="crawled_date", freq="1W")] + ["name"])
            .last()
            .reset_index()
        )
        df.loc[
            df["crawled_date"].dt.date
            >= datetime.datetime.now(datetime.timezone.utc).date(),
            "crawled_date",
        ] = last_crawled_date
        df["crawled_date"] = pd.to_datetime(df["crawled_date"]).dt.strftime("%Y-%m-%d")
        hist_dict = (
            df.pivot(columns=["name"], index=["crawled_date"], values="rank")
            .reset_index()
            .to_dict(orient="records")
        )
        return {"history": hist_dict}
