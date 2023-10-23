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
class Collection:
    title: str  # Title like "Weekly by Downloads"
    ios: StoreSection
    google: StoreSection


@dataclass
class AppsOverview:
    new_weekly: Collection
    new_monthly: Collection


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
