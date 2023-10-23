from dataclasses import dataclass


@dataclass
class AppDetail:
    store_id: str
    name: str


@dataclass
class StoreSection:
    title: str  # iOS or Google
    apps: list[AppDetail]


@dataclass
class Category:
    key: str  # mapped id like game_puzzle
    ios: StoreSection
    google: StoreSection


@dataclass
class Collection:
    title: str  # Title like "Weekly by Downloads"
    categories: dict[str, Category]  # Dict of category_id to Category


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
