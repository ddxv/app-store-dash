from dataclasses import dataclass


@dataclass
class AppDetail:
    store_id: str
    name: str


@dataclass
class AppsOverview:
    new_ios: list[AppDetail]
    new_google: list[AppDetail]
    trending_google: list[AppDetail]
    trending_ios: list[AppDetail]
