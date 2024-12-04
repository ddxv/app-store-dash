"""Script to generate sitemaps for AppGoblin."""

import pathlib
from datetime import datetime
from xml.dom.minidom import parseString
from xml.etree.ElementTree import Element, SubElement, tostring

import pandas as pd

from config import MODULE_DIR
from dbcon.queries import get_sitemap_apps, get_sitemap_companies

SITEMAP_DIR = MODULE_DIR.parent / pathlib.Path("frontend/static")


def set_df_sitemap_columns(
    df: pd.DataFrame, priority: float, changefreq: str = "weekly"
) -> pd.DataFrame:
    """Set sitemap-specific columns in DataFrame.

    Args:
        df: Input DataFrame
        priority: URL priority (0.0-1.0)
        changefreq: Update frequency (default: weekly)

    Returns:
        DataFrame with sitemap columns added

    """
    df["priority"] = priority
    df["changefreq"] = changefreq
    df["lastmod"] = datetime.now().strftime("%Y-%m-%d")
    return df


def create_sitemap(df: pd.DataFrame, filename: str) -> None:
    """Create individual sitemap XML file from DataFrame.

    Args:
        df: DataFrame containing URL data
        filename: Output filename

    """
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    # Direct string formatting instead of XML DOM operations
    template = """  <url>
    <loc>{url}</loc>
    <priority>{priority}</priority>
    <changefreq>{changefreq}</changefreq>
    <lastmod>{lastmod}</lastmod>
  </url>"""

    # Bulk append using list comprehension
    xml_lines.extend(template.format(**row) for _, row in df.iterrows())

    xml_lines.append("</urlset>")

    # Single write operation
    with pathlib.Path(SITEMAP_DIR / filename).open("w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))


def create_main_sitemap(sitemaps: list[str], filename: str) -> None:
    """Create main sitemap index file.

    Args:
        sitemaps: List of sitemap URLs to include
        filename: Output filename

    """
    # List of static URLs to include
    static_urls = [
        "https://appgoblin.info",
        "https://appgoblin.info/about",
        "https://appgoblin.info/sdks",
        "https://appgoblin.info/companies",
        "https://appgoblin.info/rankings/store/1/collection/1/category/1",
        "https://appgoblin.info/rankings/store/2/collection/4/category/120",
        "https://appgoblin.info/collections/new_monthly",
        "https://appgoblin.info/collections/new_weekly",
        "https://appgoblin.info/collections/new_yearly",
    ]

    # Combine static URLs with sitemaps
    sitemaps = static_urls + sitemaps

    # Start creating the sitemap index
    sitemap_index = Element(
        "sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    for sitemap in sitemaps:
        sitemap_elem = SubElement(sitemap_index, "sitemap")
        SubElement(sitemap_elem, "loc").text = sitemap
        SubElement(sitemap_elem, "lastmod").text = datetime.now().strftime("%Y-%m-%d")

    # Convert to string and prettify
    raw_xml = tostring(sitemap_index, encoding="utf-8")
    dom = parseString(raw_xml)
    pretty_xml = dom.toprettyxml(indent="  ")

    # Write to file, excluding the first line with the XML declaration
    with pathlib.Path(SITEMAP_DIR / filename).open("w", encoding="utf-8") as f:
        f.write("\n".join(pretty_xml.splitlines()[1:]))


def create_paginated_sitemaps(
    df: pd.DataFrame, base_filename: str, chunk_size: int = 25000
) -> list[str]:
    """Create multiple sitemap files by paginating large DataFrame.

    Args:
        df: Input DataFrame
        base_filename: Base name for output files
        chunk_size: Number of URLs per sitemap file

    Returns:
        List of generated sitemap filenames

    """
    chunk_size = 25000  # Adjust based on your needs
    filenames = []
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i : i + chunk_size]
        filename = f"{base_filename}_{i // chunk_size + 1}.xml"
        create_sitemap(chunk, filename)
        print(f"Generated {filename}")
        filenames.append(filename)
    return filenames


apps = get_sitemap_apps()
cdf = get_sitemap_companies()

MIN_APP_COUNT = 10

# Companies with URL slugs are more likely to be relevant (ie not typos from app-ads.txt)
cdf = cdf[(cdf["app_count"] > MIN_APP_COUNT) | (cdf["type_url_slug"].notna())]


# about 6
company_types = (
    cdf.groupby("type_url_slug")["app_count"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
company_types["url"] = (
    "https://appgoblin.info/companies/types/" + company_types["type_url_slug"]
)
company_types = set_df_sitemap_columns(company_types, 0.9)

# about 50
company_categories = (
    cdf.groupby("app_category")["app_count"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
company_categories["url"] = (
    "https://appgoblin.info/companies/categories/" + company_categories["app_category"]
)
company_categories = set_df_sitemap_columns(company_categories, 0.8)

# about 5 * 50
company_type_categories = (
    cdf.groupby(["type_url_slug", "app_category"])["app_count"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
company_type_categories["url"] = (
    "https://appgoblin.info/companies/types/"
    + company_type_categories["type_url_slug"]
    + "/"
    + company_type_categories["app_category"]
)
company_type_categories = set_df_sitemap_columns(company_type_categories, 0.7)


# about 1700
companies = (
    cdf.groupby("company_domain")["app_count"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
companies["url"] = "https://appgoblin.info/companies/" + companies["company_domain"]
companies = set_df_sitemap_columns(companies, 0.8)


# about 40k
company_domain_categories = (
    cdf.groupby(["company_domain", "app_category"])["app_count"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
# about 28k
MIN_CD_APP_COUNT = 20
company_domain_categories = company_domain_categories[
    company_domain_categories["app_count"] > MIN_CD_APP_COUNT
]
company_domain_categories["url"] = (
    "https://appgoblin.info/companies/"
    + company_domain_categories["company_domain"]
    + "/"
    + company_domain_categories["app_category"]
)
company_domain_categories = set_df_sitemap_columns(company_domain_categories, 0.6)


# about 600k
apps["url"] = "https://appgoblin.info/apps/" + apps["store_id"]
apps = set_df_sitemap_columns(apps, 0.5)


create_sitemap(companies, "sitemap_companies.xml")
create_sitemap(company_types, "sitemap_company_types.xml")
create_sitemap(company_categories, "sitemap_company_categories.xml")
create_sitemap(company_type_categories, "sitemap_company_type_categories.xml")

# Larger
paginated_sitemaps = create_paginated_sitemaps(
    company_domain_categories,
    "sitemap_company_domain_categories",
)
paginated_sitemaps += create_paginated_sitemaps(
    apps,
    "sitemap_apps",
)

# List of sitemap files
default_sitemaps = [
    "https://appgoblin.info/sitemap_companies.xml",
    "https://appgoblin.info/sitemap_company_types.xml",
    "https://appgoblin.info/sitemap_company_categories.xml",
    "https://appgoblin.info/sitemap_company_type_categories.xml",
]

create_main_sitemap(default_sitemaps + paginated_sitemaps, "sitemap.xml")
