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
    id: str
    name: str
    android: int
    ios: int
    type: str


@dataclass
class CategoriesOverview:
    categories: list[CategoryDetail]
