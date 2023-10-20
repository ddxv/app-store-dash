from dataclasses import dataclass


@dataclass
class AppDetail:
    store_id: str
    name: str


@dataclass
class AppGroup:
    title: str
    apps: list[AppDetail]


@dataclass
class Section:
    title: str
    data: list[AppGroup]


@dataclass
class AppsOverview:
    new: Section
    trending: Section


@dataclass
class CategoryDetail:
    category: str
    installs: int
    reviews: int


@dataclass
class CategoriesOverview:
    data: list[CategoryDetail]
