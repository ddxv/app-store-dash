"""Data models for APIs."""

from dataclasses import dataclass, field


@dataclass
class AppDetail:

    """All app details, mostly from store_app table.

    NOTE: not all details are listed in the class.
    """

    store_id: str
    name: str
    store_url: str


@dataclass
class AppHistory:

    """All app history details.

    NOTE: not all details are listed in the class.
    """

    histogram: dict
    history_table: dict
    plot_data: dict


@dataclass
class AdsTxtEntries:

    """App ads txt entries."""

    direct_entries: dict
    reseller_entries: dict


@dataclass
class PackageDetails:

    """Lists of Package permissions, trackers etc from Manifest."""

    permissions: list[str]
    trackers: dict[str, dict[str, list[str]]]
    networks: dict[str, dict[str, list[str]]]
    leftovers: dict[str, list[str]]
    android: list[str]


@dataclass
class AppGroup:

    """A Group of Apps by Platform."""

    title: str  # iOS or Google
    apps: list[AppDetail]


@dataclass
class Category:

    """A Category for apps with ios and google separated."""

    key: str  # mapped id like game_puzzle
    ios: AppGroup
    google: AppGroup


@dataclass
class DeveloperApps:

    """A developer's list of apps.

    Note: This is platform specific.
    """

    developer_id: str
    title: str
    apps: list[AppDetail]


@dataclass
class CompanyApps:

    """A company's list of apps."""

    title: str
    apps: list[AppDetail]


@dataclass
class Collection:

    """A single Collection as defined by us to combine ios and Google collections."""

    title: str  # Title like "Weekly by Downloads"
    categories: list[Category]  # Dict of category_id to Category


@dataclass
class AppsOverview:

    """All collections together for the frontend."""

    new_weekly: Collection
    new_monthly: Collection
    new_yearly: Collection
    top: Collection


@dataclass
class CategoryDetail:

    """Represents detailed information about a category.

    Includes its identifier, name, and app counts for both Android and iOS platforms, along with its type.
    """

    id: str
    name: str
    android: int
    ios: int
    type: str


@dataclass
class CategoriesOverview:

    """Holds a list of CategoryDetail objects providing an overview of all categories."""

    categories: list[CategoryDetail]


@dataclass
class CompanyPatterns:

    """Holds a list of package patterns and paths for a company."""

    package_patterns: list[str]
    paths: list[str]


@dataclass
class CompanyPatternsDict:

    """Holds a list of package patterns and paths for a company."""

    companies: dict[str, CompanyPatterns]


@dataclass
class ChildrenCompanyTree:

    """A company tree with parent companies and domains."""

    company_name: str
    domains: list[str]


@dataclass
class ParentCompanyTree:

    """A company tree with parent companies and domains."""

    parent_company_name: str | None
    parent_company_domain: str | None
    company_name: str
    domains: list[str]
    children_companies: list[ChildrenCompanyTree]


@dataclass
class CompanyDetail:

    """Describes details of a tracker.

    Includes its db identifier, name, and the count of its occurrences.
    """

    company_id: int
    name: str
    count: int


@dataclass
class PlatformCompanies:

    """Represents companies for a specific platform."""

    top: list[dict]


@dataclass
class CategoryAppStats:

    """Contains a list of CompanyDetail objects representing the top networks identified."""

    total_apps: int = 0
    adstxt_direct_ios_total_apps: int = 0
    adstxt_direct_android_total_apps: int = 0
    adstxt_reseller_ios_total_apps: int = 0
    adstxt_reseller_android_total_apps: int = 0
    sdk_ios_total_apps: int = 0
    sdk_android_total_apps: int = 0


@dataclass
class CategoryOverview:

    """Contains a dictionary of categories, each with their associated statistics."""

    categories: dict[str, CategoryAppStats] = field(default_factory=dict)

    def add_category(self, category: str) -> None:
        """Add a category to the overview."""
        if category not in self.categories:
            self.categories[category] = CategoryAppStats()

    def update_stats(self, category: str, **kwargs: int) -> None:
        """Update the stats for a category."""
        if category not in self.categories:
            self.add_category(category)
        for key, value in kwargs.items():
            if hasattr(self.categories[category], key):
                setattr(self.categories[category], key, value)


@dataclass
class CompaniesOverview:

    """Contains a list of CompanyDetail objects representing the top networks identified."""

    companies_overview: list[CompanyDetail]
    sdk: PlatformCompanies
    adstxt_direct: PlatformCompanies
    adstxt_reseller: PlatformCompanies
    categories: CategoryOverview


@dataclass
class CompanyPlatformOverview:

    """Represents companies for a specific platform."""

    ios: AppGroup
    android: AppGroup


@dataclass
class CompanyAppsOverview:

    """Overview of a company's apps on different platforms."""

    sdk: CompanyPlatformOverview
    adstxt_direct: CompanyPlatformOverview
    adstxt_reseller: CompanyPlatformOverview


@dataclass
class TopCompanies:

    """Contains a list of CompanyDetail objects representing the top networks identified."""

    all_companies: list[CompanyDetail]
    parent_companies: list[CompanyDetail]


@dataclass
class StoreCategoryDetail:

    """Describes details of a store category, including its identifier and name."""

    category_id: int
    category_name: str


@dataclass
class StoreCollections:

    """Represents a collection within a store.

    Including its identifier, name, and the categories it contains.
    Categories are optional and can be added as a list.
    """

    collection_id: int
    collection_name: str
    categories: list[StoreCategoryDetail] = field(default_factory=list)


@dataclass
class StoreRankings:

    """Holds information about a store's rankings.

    Including its identifier, name, and the collections it contains. Collections are optional and can be added as a list.
    """

    store_id: int
    store_name: str
    collections: list[StoreCollections] = field(default_factory=list)


@dataclass
class RankingOverview:

    """Provides an overview of rankings across different stores, containing a list of StoreRankings objects."""

    stores_rankings: list[StoreRankings] = field(default_factory=list)


@dataclass
class AppRank:

    """Represents the ranking details of an app, including its latest rankings and historical rankings data as dictionaries."""

    latest: dict
    history: dict
