from dataclasses import dataclass, field


@dataclass
class AppDetail:
    """TODO: Fill out all details."""

    store_id: str
    name: str


@dataclass
class AppGroup:
    title: str  # iOS or Google
    apps: list[AppDetail]


@dataclass
class Category:
    key: str  # mapped id like game_puzzle
    ios: AppGroup
    google: AppGroup


@dataclass
class DeveloperApps:
    developer_id: str  # mapped id like game_puzzle
    title: str  # mapped id like game_puzzle
    apps: list[AppDetail]


@dataclass
class Collection:
    title: str  # Title like "Weekly by Downloads"
    categories: list[Category]  # Dict of category_id to Category


@dataclass
class AppsOverview:
    new_weekly: Collection
    new_monthly: Collection
    new_yearly: Collection
    top: Collection


@dataclass
class CategoryDetail:
    id: str
    name: str
    android: int
    ios: int
    type: str


@dataclass
class CategoriesOverview:
    categories: list[CategoryDetail]


# @dataclass
# class StoreCategoryDetail:
#     category_id: int
#     category_name: str


# @dataclass
# class StoreCollections:
#     int: list[StoreCategoryDetail]


# @dataclass


@dataclass
class StoreCategoryDetail:
    category_id: int
    category_name: str


@dataclass
class StoreCollections:
    collection_id: int
    collection_name: str
    categories: list[StoreCategoryDetail] = field(default_factory=list)


@dataclass
class StoreRankings:
    store_id: int
    store_name: str
    collections: list[StoreCollections] = field(default_factory=list)


@dataclass
class RankingOverview:
    stores_rankings: list[StoreRankings] = field(default_factory=list)


@dataclass
class AppRank:
    latest: dict
    history: dict
