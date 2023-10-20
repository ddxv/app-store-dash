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
    name: int
    total: int


@dataclass
class CategoriesOverview:
    apps: list[CategoryDetail]
    games: list[CategoryDetail]
