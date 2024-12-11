"""API endoipoints for companies.

/companies/ returns list of top companies overall.

"""

import time
import urllib
from typing import Self

import numpy as np
import pandas as pd
from litestar import Controller, get
from litestar.config.response_cache import CACHE_FOREVER

from api_app.models import (
    AppGroup,
    CompaniesCategoryOverview,
    CompaniesOverview,
    CompanyAppsOverview,
    CompanyCategoryOverview,
    CompanyDetail,
    CompanyPatterns,
    CompanyPatternsDict,
    CompanyPlatformOverview,
    CompanyTypes,
    ParentCompanyTree,
    TopCompanies,
    TopCompaniesOverviewShort,
    TopCompaniesShort,
)
from config import get_logger
from dbcon.queries import (
    get_adtech_categories,
    get_adtech_category_type,
    get_companies_parent_overview,
    get_companies_top,
    get_company_overview,
    get_company_parent_categories,
    get_company_sdks,
    get_company_tree,
    get_tag_source_category_totals,
    get_tag_source_totals,
    get_top_companies,
    new_get_top_apps_for_company,
    search_companies,
)

logger = get_logger(__name__)


def get_search_results(search_term: str) -> pd.DataFrame:
    """Parse search term and return resulting AppGroup."""
    decoded_input = urllib.parse.unquote(search_term)
    df = search_companies(search_input=decoded_input, limit=20)
    logger.info(f"{decoded_input=} returned rows: {df.shape[0]}")
    return df


def get_company_apps_new(
    company_domain: str,
    category: str | None = None,
) -> CompanyAppsOverview:
    """Get the overview data from the database."""
    df = new_get_top_apps_for_company(
        company_domain=company_domain,
        mapped_category=category,
    )

    android_adstxt_reseller = df[
        (df["tag_source"] == "app_ads_reseller")
        & (df["store"].str.startswith("Google"))
    ]
    ios_adstxt_reseller = df[
        (df["tag_source"] == "app_ads_reseller")
        & (~df["store"].str.startswith("Google"))
    ]

    android_adstxt_direct = df[
        (df["tag_source"] == "app_ads_direct") & (df["store"].str.startswith("Google"))
    ]
    ios_adstxt_direct = df[
        (df["tag_source"] == "app_ads_direct") & (~df["store"].str.startswith("Google"))
    ]

    android_sdk = df[
        (df["tag_source"] == "sdk") & (df["store"].str.startswith("Google"))
    ]
    ios_sdk = df[(df["tag_source"] == "sdk") & (~df["store"].str.startswith("Google"))]

    results = CompanyAppsOverview(
        adstxt_reseller=CompanyPlatformOverview(
            android=AppGroup(
                apps=android_adstxt_reseller.to_dict(orient="records"),
                title=company_domain,
            ),
            ios=AppGroup(
                apps=ios_adstxt_reseller.to_dict(orient="records"),
                title=company_domain,
            ),
        ),
        adstxt_direct=CompanyPlatformOverview(
            android=AppGroup(
                apps=android_adstxt_direct.to_dict(orient="records"),
                title=company_domain,
            ),
            ios=AppGroup(
                apps=ios_adstxt_direct.to_dict(orient="records"),
                title=company_domain,
            ),
        ),
        sdk=CompanyPlatformOverview(
            android=AppGroup(
                apps=android_sdk.to_dict(orient="records"),
                title=company_domain,
            ),
            ios=AppGroup(apps=ios_sdk.to_dict(orient="records"), title=company_domain),
        ),
    )
    return results


def make_top_companies(top_df: pd.DataFrame) -> TopCompaniesShort:
    """Make top companies short."""
    top_sdk_df = top_df[top_df["tag_source"] == "sdk"].copy()
    top_adstxt_direct_df = top_df[top_df["tag_source"] == "app_ads_direct"].copy()
    top_adstxt_reseller_df = top_df[top_df["tag_source"] == "app_ads_reseller"].copy()

    top_sdk_df["company_title"] = np.where(
        top_sdk_df["company_name"].isna(),
        top_sdk_df["company_domain"],
        top_sdk_df["company_name"],
    )
    top_adstxt_direct_df["company_title"] = np.where(
        top_adstxt_direct_df["company_name"].isna(),
        top_adstxt_direct_df["company_domain"],
        top_adstxt_direct_df["company_name"],
    )
    top_adstxt_reseller_df["company_title"] = np.where(
        top_adstxt_reseller_df["company_name"].isna(),
        top_adstxt_reseller_df["company_domain"],
        top_adstxt_reseller_df["company_name"],
    )

    top_sdk_df = top_sdk_df.rename(
        columns={"company_title": "group", "app_count": "value"},
    ).sort_values(by=["value"], ascending=True)
    top_adstxt_direct_df = top_adstxt_direct_df.rename(
        columns={"company_title": "group", "app_count": "value"},
    ).sort_values(by=["value"], ascending=True)
    top_adstxt_reseller_df = top_adstxt_reseller_df.rename(
        columns={"company_title": "group", "app_count": "value"},
    ).sort_values(by=["value"], ascending=True)

    top_companies_short = TopCompaniesShort(
        sdk=top_sdk_df.to_dict(orient="records"),
        adstxt_direct=top_adstxt_direct_df.to_dict(orient="records"),
        adstxt_reseller=top_adstxt_reseller_df.to_dict(orient="records"),
    )
    return top_companies_short


def prep_companies_overview_df(
    overview_df: pd.DataFrame,
) -> tuple[pd.DataFrame, CompaniesCategoryOverview]:
    """Prep companies overview dataframe."""
    overview_df = (
        overview_df.groupby(
            ["company_name", "company_domain", "store", "tag_source"],
            dropna=False,
        )[["app_count", "total_app_count"]]
        .sum()
        .reset_index()
    )

    overview_df["percentage"] = (
        overview_df["app_count"] / overview_df["total_app_count"]
    )
    overview_df["store_tag"] = np.where(
        overview_df["store"].str.contains("Google"),
        "google",
        "apple",
    )
    overview_df["store_tag_source"] = (
        overview_df["store_tag"] + "_" + overview_df["tag_source"]
    )

    # NOTE: This is crucial for SDK to be first
    # since it has more than just advertising data
    store_tag_source_values = overview_df["store_tag_source"].unique().tolist()
    sdk_values = [x for x in store_tag_source_values if "sdk" in x]
    store_tag_source_values = sdk_values + [
        x for x in store_tag_source_values if x not in sdk_values
    ]

    overview_df = overview_df.pivot(
        index=["company_name", "company_domain"],
        columns=["store_tag_source"],
        values="percentage",
    ).reset_index()
    overview_df = overview_df.sort_values(
        by=store_tag_source_values,
        ascending=False,
    ).head(1000)
    return overview_df


def get_overviews(
    category: str | None = None,
    type_slug: str | None = None,
) -> CompaniesOverview:
    """Get the overview data from the database."""
    # Get Top 5 Companies for Plots
    top_df = get_companies_top(type_slug=type_slug, app_category=category, limit=5)
    top_companies_short = make_top_companies(top_df)

    if type_slug:
        logger.info("Getting adtech category type")
        overview_df = get_adtech_category_type(type_slug, app_category=category)
    else:
        logger.info("Getting companies parent overview")
        overview_df = get_companies_parent_overview(app_category=category)

    if category:
        logger.info("Getting category totals")
        tag_source_category_app_counts = get_tag_source_category_totals()
    else:
        logger.info("Getting category totals")
        tag_source_category_app_counts = get_tag_source_totals()

    overview_df = overview_df.merge(
        tag_source_category_app_counts,
        on=["app_category", "store", "tag_source"],
        validate="m:1",
    )

    category_overview = make_category_uniques(df=overview_df.copy())

    overview_df = prep_companies_overview_df(overview_df)

    results = CompaniesOverview(
        companies_overview=overview_df.to_dict(orient="records"),
        top=top_companies_short,
        categories=category_overview,
    )

    return results


def append_overall_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Add single row for overall category."""
    metrics = ["installs", "app_count", "ratings"]
    total_cols = ["total_ratings", "total_installs", "category_total_apps"]
    overall_totals = (
        df.groupby(["store", "mapped_category"])[total_cols]
        .first()
        .reset_index()
        .groupby(["store"])[total_cols]
        .sum()
    )
    overall_company_df = df.groupby(["store", "name"])[metrics].sum().reset_index()
    overall_df = overall_company_df.merge(
        overall_totals,
        how="left",
        on="store",
        validate="m:1",
    )
    overall_df["mapped_category"] = "overall"
    df = pd.concat([df, overall_df])
    """Append a consolidated games category.
    note this wouldn't work for Apple as not needed.
    """
    games_cat_df = (
        df.loc[(df["mapped_category"].str.contains(r"^game"))]
        .groupby(["store", "name"])[metrics + total_cols]
        .sum()
        .reset_index()
    )
    games_cat_df["mapped_category"] = "games"
    df = pd.concat([df, games_cat_df])
    return df


def old_companies_overview(categories: list[int]) -> TopCompanies:
    """Process networks and return TopCompanies class."""
    df = get_top_companies(categories=categories)
    df_parents = get_top_companies(
        categories=categories,
        group_by_parent=True,
    )

    df = df[~df["company_name"].isna()].rename(columns={"company_name": "name"})
    df_parents = df_parents.rename(columns={"company_name": "name"})

    # Append combined columns like "overall" and "games"
    df = append_overall_categories(df)
    df_parents = append_overall_categories(df_parents)

    # Since new columns added, recalculate percentages
    df["app_count_percent"] = df["app_count"] / df["category_total_apps"]
    df["installs_percent"] = df["installs"] / df["total_installs"]
    df["ratings_percent"] = df["ratings"] / df["total_ratings"]
    df_parents["app_count_percent"] = (
        df_parents["app_count"] / df_parents["category_total_apps"]
    )
    df_parents["installs_percent"] = (
        df_parents["installs"] / df_parents["total_installs"]
    )
    df_parents["ratings_percent"] = df_parents["ratings"] / df_parents["total_ratings"]

    df = df.sort_values(
        ["app_count_percent", "installs", "ratings"],
        ascending=False,
        na_position="first",
    )
    df_parents = df_parents.sort_values(
        ["app_count_percent", "installs", "ratings"],
        ascending=False,
        na_position="first",
    )

    required_columns = [
        "store",
        "mapped_category",
        "name",
        "installs",
        "ratings",
        "app_count",
        "installs_percent",
        "ratings_percent",
        "app_count_percent",
    ]

    df = df[[*required_columns, "parent_company_name"]]
    df_parents = df_parents[required_columns]

    def transform_group(group: pd.DataFrame) -> dict:
        return group.drop(columns=["store", "mapped_category"]).to_dict(
            orient="records",
        )

    top = TopCompanies(
        all_companies=df.groupby(["store", "mapped_category"])
        .apply(transform_group)
        .unstack(level=1)
        .to_dict(orient="index"),
        parent_companies=df_parents.groupby(["store", "mapped_category"])
        .apply(transform_group)
        .unstack(level=1)
        .to_dict(orient="index"),
    )
    return top


def make_category_uniques(df: pd.DataFrame) -> CompaniesCategoryOverview:
    """Make category sums for overview."""
    overview = CompaniesCategoryOverview()

    # Precompute boolean masks
    is_apple = df["store"].str.contains("Apple")
    is_google = df["store"].str.contains("Google")
    is_sdk = df["tag_source"] == "sdk"
    is_app_ads_reseller = df["tag_source"] == "app_ads_reseller"
    is_app_ads_direct = df["tag_source"] == "app_ads_direct"

    # Function to calculate unique counts
    def get_unique_company_counts(mask: pd.Series) -> int:
        return df.loc[mask, "company_domain"].nunique()

    def get_app_sums(mask: pd.Series) -> int:
        return df.loc[mask, "app_count"].sum()

    # Calculate overall stats
    overall_stats = {
        "total_companies": df["company_domain"].nunique(),
        "total_apps": int(df["app_count"].sum()),
        "sdk_ios_total_companies": get_unique_company_counts(is_apple & is_sdk),
        "sdk_ios_total_apps": int(get_app_sums(is_apple & is_sdk)),
        "sdk_android_total_companies": get_unique_company_counts(is_google & is_sdk),
        "sdk_android_total_apps": int(get_app_sums(is_google & is_sdk)),
        "adstxt_direct_ios_total_companies": get_unique_company_counts(
            is_apple & is_app_ads_direct
        ),
        "adstxt_direct_android_total_companies": get_unique_company_counts(
            is_google & is_app_ads_direct,
        ),
        "adstxt_reseller_ios_total_companies": get_unique_company_counts(
            is_apple & is_app_ads_reseller,
        ),
        "adstxt_reseller_android_total_companies": get_unique_company_counts(
            is_google & is_app_ads_reseller,
        ),
    }
    overview.update_stats("all", **overall_stats)

    return overview


def make_company_category_sums(df: pd.DataFrame) -> CompanyCategoryOverview:
    """Make category sums for overview."""
    overview = CompanyCategoryOverview()
    conditions = {
        "sdk_ios": (df["store"].str.contains("Apple")) & (df["tag_source"] == "sdk"),
        "sdk_android": (df["store"].str.contains("Google"))
        & (df["tag_source"] == "sdk"),
        "adstxt_direct_ios": (df["store"].str.contains("Apple"))
        & (df["tag_source"] == "app_ads_direct"),
        "adstxt_direct_android": (df["store"].str.contains("Google"))
        & (df["tag_source"] == "app_ads_direct"),
        "adstxt_reseller_ios": (df["store"].str.contains("Apple"))
        & (df["tag_source"] == "app_ads_reseller"),
        "adstxt_reseller_android": (df["store"].str.contains("Google"))
        & (df["tag_source"] == "app_ads_reseller"),
    }

    # Calculate sums for all conditions in one go
    results = {
        key: df.loc[condition, "app_count"].sum()
        for key, condition in conditions.items()
    }

    # Unpack results
    (
        sdk_ios_total_apps,
        sdk_android_total_apps,
        adstxt_direct_ios_total_apps,
        adstxt_direct_android_total_apps,
        adstxt_reseller_ios_total_apps,
        adstxt_reseller_android_total_apps,
    ) = (
        results["sdk_ios"],
        results["sdk_android"],
        results["adstxt_direct_ios"],
        results["adstxt_direct_android"],
        results["adstxt_reseller_ios"],
        results["adstxt_reseller_android"],
    )

    total_apps = (
        sdk_ios_total_apps
        + sdk_android_total_apps
        + adstxt_direct_ios_total_apps
        + adstxt_direct_android_total_apps
        + adstxt_reseller_ios_total_apps
        + adstxt_reseller_android_total_apps
    )

    overview.update_stats(
        "all",
        total_apps=total_apps,
        adstxt_direct_ios_total_apps=adstxt_direct_ios_total_apps,
        adstxt_direct_android_total_apps=adstxt_direct_android_total_apps,
        adstxt_reseller_ios_total_apps=adstxt_reseller_ios_total_apps,
        adstxt_reseller_android_total_apps=adstxt_reseller_android_total_apps,
        sdk_ios_total_apps=sdk_ios_total_apps,
        sdk_android_total_apps=sdk_android_total_apps,
    )
    cats = df.app_category.unique().tolist()
    for cat in cats:
        conditions = {
            "sdk_ios": (df["store"].str.contains("Apple"))
            & (df["tag_source"] == "sdk")
            & (df["app_category"] == cat),
            "sdk_android": (df["store"].str.contains("Google"))
            & (df["tag_source"] == "sdk")
            & (df["app_category"] == cat),
            "adstxt_direct_ios": (df["store"].str.contains("Apple"))
            & (df["tag_source"] == "app_ads_direct")
            & (df["app_category"] == cat),
            "adstxt_direct_android": (df["store"].str.contains("Google"))
            & (df["tag_source"] == "app_ads_direct")
            & (df["app_category"] == cat),
            "adstxt_reseller_ios": (df["store"].str.contains("Apple"))
            & (df["tag_source"] == "app_ads_reseller")
            & (df["app_category"] == cat),
            "adstxt_reseller_android": (df["store"].str.contains("Google"))
            & (df["tag_source"] == "app_ads_reseller")
            & (df["app_category"] == cat),
        }

        # Calculate sums for all conditions in one go
        results = {
            key: df.loc[condition, "app_count"].sum()
            for key, condition in conditions.items()
        }

        # Unpack results
        (
            sdk_ios_total_apps,
            sdk_android_total_apps,
            adstxt_direct_ios_total_apps,
            adstxt_direct_android_total_apps,
            adstxt_reseller_ios_total_apps,
            adstxt_reseller_android_total_apps,
        ) = (
            results["sdk_ios"],
            results["sdk_android"],
            results["adstxt_direct_ios"],
            results["adstxt_direct_android"],
            results["adstxt_reseller_ios"],
            results["adstxt_reseller_android"],
        )

        total_apps = (
            sdk_ios_total_apps
            + sdk_android_total_apps
            + adstxt_direct_ios_total_apps
            + adstxt_direct_android_total_apps
            + adstxt_reseller_ios_total_apps
            + adstxt_reseller_android_total_apps
        )

        overview.update_stats(
            cat,
            total_apps=total_apps,
            adstxt_direct_ios_total_apps=adstxt_direct_ios_total_apps,
            adstxt_direct_android_total_apps=adstxt_direct_android_total_apps,
            adstxt_reseller_ios_total_apps=adstxt_reseller_ios_total_apps,
            adstxt_reseller_android_total_apps=adstxt_reseller_android_total_apps,
            sdk_ios_total_apps=sdk_ios_total_apps,
            sdk_android_total_apps=sdk_android_total_apps,
        )
    return overview


class CompaniesController(Controller):
    """API EndPoint return for all ad tech companies."""

    path = "/api/"

    @get(path="/companies", cache=86400)
    async def companies(self: Self) -> CompaniesOverview:
        """Handle GET request for all companies.

        Returns
        -------
        CompaniesOverview
            An overview of companies across different platforms and sources.

        """
        start = time.perf_counter() * 1000

        overview = get_overviews()

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"GET /api/companies took {duration}ms")

        return overview

    @get(path="/companies/categories/{category:str}", cache=86400)
    async def companies_categories(self: Self, category: str) -> CompaniesOverview:
        """Handle GET request for all companies in a category.

        Returns
        -------
        CompaniesOverview
            An overview of companies across different platforms and sources.

        """
        logger.info(f"GET /api/companies/categories/{category} start")

        overview = get_overviews(category=category)

        return overview

    @get(
        path="/companies/{company_domain:str}",
        cache=86400,
    )
    async def company_overview(
        self: Self,
        company_domain: str,
    ) -> CompanyCategoryOverview:
        """Handle GET request for a specific company.

        Args:
        ----
        company_domain : str
            The domain of the company to retrieve apps for.

        Returns:
        -------
        CategoryOverview
            An overview of companies, filtered for the specified company and category.

        """
        start = time.perf_counter() * 1000
        df = get_company_overview(company_domain=company_domain)

        overview = make_company_category_sums(df=df)

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"GET /api/companies/{company_domain} took {duration}ms")
        return overview

    @get(
        path="/companies/{company_domain:str}/topapps",
        cache=86400,
    )
    async def company_apps(
        self: Self,
        company_domain: str,
        category: str | None = None,
    ) -> CompanyAppsOverview:
        """Handle GET request for a specific company top apps.

        Args:
        ----
        company_domain : str
            The domain of the company to retrieve apps for.
        category : str | None
            The category to retrieve apps for.

        Returns:
        -------
        CompanyAppsOverview
            An overview of companies, filtered for the specified company and category.

        """
        start = time.perf_counter() * 1000
        results = get_company_apps_new(company_domain=company_domain, category=category)

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(
            f"GET /api/companies/{company_domain}/topapps {category=} took {duration}ms"
        )
        return results

    @get(
        path="/companies/{company_domain:str}/parentcategories",
        cache=86400,
    )
    async def company_parent_categories(
        self: Self,
        company_domain: str,
    ) -> dict:
        """Handle GET request for a specific company parent categories.

        Args:
        ----
        company_domain : str
            The domain of the company to retrieve apps for.

        Returns:
        -------
        dict
            A dictionary of parent categories for the specified company.

        """
        start = time.perf_counter() * 1000

        df = get_company_parent_categories(company_domain=company_domain)

        num_categories = 9

        top_cats = (
            df.sort_values(by="app_count", ascending=False)
            .head(num_categories)
            .app_category.tolist()
        )

        df.loc[~df["app_category"].isin(top_cats), "app_category"] = "others"

        df = df.groupby(["app_category"])["app_count"].sum().reset_index()

        df["name"] = df["app_category"]

        df["name"] = (
            df["name"]
            .str.replace("game_", "Games: ")
            .str.replace("_and_", " & ")
            .str.replace("_", " ")
            .str.title()
        )

        df = df.rename(columns={"name": "group", "app_count": "value"})

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(
            f"GET /api/companies/{company_domain}/parentcategories took {duration}ms"
        )
        return df.to_dict(orient="records")

    @get(
        path="/companies/{queried_domain:str}/tree",
        cache=86400,
    )
    async def company_tree(
        self: Self,
        queried_domain: str,
    ) -> ParentCompanyTree:
        """Handle GET request for company tree.

        Args:
        ----
        queried_domain : str
            The name of the company to retrieve apps for.

        Returns:
        -------
        ParentCompanyTree
            An overview of companies, filtered for the specified company and category.

        """
        start = time.perf_counter() * 1000

        df = get_company_tree(company_domain=queried_domain)

        parent_company = df["parent_company_name"].tolist()[0]
        parent_company_domain = df["parent_company_domain"].tolist()[0]

        queried_company_name = df[(queried_domain == df["company_domain"])][
            "company_name"
        ].tolist()[0]

        if parent_company == queried_domain:
            parent_company = None

        domains = (
            df[
                ~(parent_company == df["company_name"])
                # & (queried_domain == df["company_name"])
                & (queried_domain == df["company_domain"])
            ]["company_domain"]
            .unique()
            .tolist()
        )

        children_companies = (
            df[
                ~(parent_company == df["company_name"])
                & (queried_domain != df["company_domain"])
            ]
            .rename(columns={"company_domain": "domains"})
            .groupby(["company_name"])["domains"]
            .apply(lambda x: list(x))
            .reset_index()
            .to_dict(orient="records")
        )

        tree = ParentCompanyTree(
            parent_company_name=parent_company,
            parent_company_domain=parent_company_domain,
            queried_company_domain=queried_domain,
            queried_company_name=queried_company_name,
            domains=domains,
            children_companies=children_companies,
        )

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"GET /api/companies/{queried_domain}/tree took {duration}ms")

        return tree

    @get(
        path="/companies/{company_domain:str}/sdks",
        cache=3600,
    )
    async def company_sdks(
        self: Self,
        company_domain: str,
    ) -> CompanyPatternsDict:
        """Handle GET request for company sdks.

        Args:
        ----
        company_domain : str
            The domain of the company to retrieve apps for.

        Returns:
        -------
        ParentCompanySDKs
            An overview of companies, filtered for the specified company and category.

        """
        start = time.perf_counter() * 1000

        df = get_company_sdks(company_domain=company_domain)

        mydict = CompanyPatternsDict(
            companies={
                company_name[0]: CompanyPatterns(
                    package_patterns=mylist["package_pattern"].unique().tolist(),
                    paths=mylist["path_pattern"].unique().tolist(),
                )
                for company_name, mylist in df.groupby(["company_name"])
            },
        )

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"GET /api/companies/{company_domain}/sdks took {duration}ms")

        return mydict

    @get(path="/companies/types/", cache=CACHE_FOREVER)
    async def all_adtech_types(self: Self) -> CompanyTypes:
        """Handle GET request for a list of adtech company categories.

        Returns
        -------
            A dictionary representation of the list of categories
            each with an id, name, type and total of apps

        """
        start = time.perf_counter() * 1000
        company_types_df = get_adtech_categories()

        company_types = CompanyTypes(types=company_types_df.to_dict(orient="records"))

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"{self.path} took {duration}ms")

        return company_types

    @get(path="/companies/types/{type_slug:str}", cache=86400)
    async def adtech_type(
        self: Self,
        type_slug: str,
        category: str | None = None,
    ) -> CompaniesOverview:
        """Handle GET request for a list of adtech company categories.

        Returns
        -------
            A dictionary representation of the list of categories
            each with an id, name, type and total of apps

        """
        start = time.perf_counter() * 1000
        overview = get_overviews(category=category, type_slug=type_slug)

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"/companies/types/{type_slug}?{category=} took {duration}ms")

        return overview

    @get(path="/companies/topshort/", cache=CACHE_FOREVER)
    async def get_companies_shortlist_top(self: Self) -> TopCompaniesOverviewShort:
        """Handle GET request for a list of adtech company categories.

        Returns
        -------
            A dictionary representation of the list of categories
            each with an id, name, type and total of apps

        """
        start = time.perf_counter() * 1000
        adnetworks = get_companies_top(
            type_slug="ad-networks", app_category=None, limit=5
        )
        mmps = get_companies_top(type_slug="ad-attribution", app_category=None, limit=5)
        analytics = get_companies_top(
            type_slug="product-analytics", app_category=None, limit=5
        )
        top_ad_networks = make_top_companies(adnetworks)
        top_mmps = make_top_companies(mmps)
        top_analytics = make_top_companies(analytics)

        top_companies = TopCompaniesOverviewShort(
            adnetworks=top_ad_networks,
            attribution=top_mmps,
            analytics=top_analytics,
        )

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"{self.path} took {duration}ms")

        return top_companies

    @get(path="/companies/search/{search_term:str}", cache=86400)
    async def get_companies_search(self: Self, search_term: str) -> list[CompanyDetail]:
        """Handle GET request for a list of adtech company categories.

        Returns
        -------
            A list of CompanyDetail objects

        """
        start = time.perf_counter() * 1000
        results = get_search_results(search_term=search_term)

        results["app_category"] = "all"

        category_totals_df = get_tag_source_totals()

        overview_df = results.merge(
            category_totals_df,
            on=["app_category", "store", "tag_source"],
            validate="m:1",
        )

        overview_df = prep_companies_overview_df(overview_df)

        duration = round((time.perf_counter() * 1000 - start), 2)
        logger.info(f"{self.path}/{search_term} took {duration}ms")

        return overview_df.to_dict(orient="records")
