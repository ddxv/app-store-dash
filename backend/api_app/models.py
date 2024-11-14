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
    company_categories: dict
    leftovers: dict[str, list[str]]


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
class Collection:
    """A single Collection to combine ios and Google collections."""

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

    Includes its identifier, name, and app counts for
    both Android and iOS platforms, along with its type.
    """

    id: str
    name: str
    android: int
    ios: int
    type: str


@dataclass
class CategoriesOverview:
    """Holds a list of CategoryDetail objects.

    Providing an overview of all categories.
    """

    categories: list[CategoryDetail]


@dataclass
class CompanyTypes:
    """Holds a list of CategoryDetail objects.

    Providing an overview of all categories.
    """

    types: list[dict]


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
    queried_company_domain: str
    queried_company_name: str
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
    """Companies data for a specific platform (iOS/Android)."""

    ios: list[dict]
    android: list[dict]


@dataclass
class TopCompaniesShort:
    """Represents top companies across different categories."""

    sdk: PlatformCompanies
    adstxt_direct: PlatformCompanies
    adstxt_reseller: PlatformCompanies


@dataclass
class TopCompaniesOverviewShort:
    """Represents top companies across different categories."""

    adnetworks: TopCompaniesShort
    attribution: TopCompaniesShort
    analytics: TopCompaniesShort


@dataclass
class CategoryCompaniesStats:
    """Contains a list of CompanyDetail objects.

    Representing the top networks identified.
    """

    total_companies: int = 0
    adstxt_direct_ios_total_companies: int = 0
    adstxt_direct_android_total_companies: int = 0
    adstxt_reseller_ios_total_companies: int = 0
    adstxt_reseller_android_total_companies: int = 0
    sdk_ios_total_companies: int = 0
    sdk_android_total_companies: int = 0


@dataclass
class CategoryCompanyStats:
    """Contains a list of CompanyDetail objects.

    Representing the top networks identified.
    """

    total_apps: int = 0
    adstxt_direct_ios_total_apps: int = 0
    adstxt_direct_android_total_apps: int = 0
    adstxt_reseller_ios_total_apps: int = 0
    adstxt_reseller_android_total_apps: int = 0
    sdk_ios_total_apps: int = 0
    sdk_android_total_apps: int = 0


@dataclass
class CompaniesCategoryOverview:
    """Contains a dictionary of categories, each with their associated statistics."""

    categories: dict[str, CategoryCompaniesStats] = field(default_factory=dict)

    def add_category(self, category: str) -> None:
        """Add a category to the overview."""
        if category not in self.categories:
            self.categories[category] = CategoryCompaniesStats()

    def update_stats(self, category: str, **kwargs: int) -> None:
        """Update the stats for a category."""
        if category not in self.categories:
            self.add_category(category)
        for key, value in kwargs.items():
            if hasattr(self.categories[category], key):
                setattr(self.categories[category], key, value)


@dataclass
class CompanyCategoryOverview:
    """Contains a dictionary of categories, each with their associated statistics."""

    categories: dict[str, CategoryCompanyStats] = field(default_factory=dict)

    def add_category(self, category: str) -> None:
        """Add a category to the overview."""
        if category not in self.categories:
            self.categories[category] = CategoryCompanyStats()

    def update_stats(self, category: str, **kwargs: int) -> None:
        """Update the stats for a category."""
        if category not in self.categories:
            self.add_category(category)
        for key, value in kwargs.items():
            if hasattr(self.categories[category], key):
                setattr(self.categories[category], key, value)


@dataclass
class CompaniesOverview:
    """Contains a list of CompanyDetail objects.

    Representing the top networks identified.
    """

    companies_overview: list[CompanyDetail]
    top: TopCompaniesShort
    categories: CompaniesCategoryOverview


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
    """Contains a list of CompanyDetail objects.

    Representing the top networks identified.
    """

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

    Including its identifier, name, and the collections it contains.
    Collections are optional and can be added as a list.
    """

    store_id: int
    store_name: str
    collections: list[StoreCollections] = field(default_factory=list)


@dataclass
class RankingOverview:
    """Provides an overview of rankings across different stores.

    Containing a list of StoreRankings objects.
    """

    stores_rankings: list[StoreRankings] = field(default_factory=list)


@dataclass
class AppRank:
    """Represents the ranking details of an app.

    Including its latest rankings and historical rankings data as dictionaries.
    """

    latest: dict
    history: dict


@dataclass
class SdksOverview:
    """Contains a list of SDK objects.

    Representing the top sdks identified.
    """

    ios_overview: list[dict]
    android_overview: list[dict]


@dataclass
class SdkOverview:
    """Contains a list of sdk overview objects."""

    ios_overview: list[dict]
    android_overview: list[dict]


@dataclass
class SdkCompanies:
    """Contains a list of sdk companies objects."""

    companies: list[dict]
