import datetime

import numpy as np
import pandas as pd
from sqlalchemy import text

from config import get_logger
from dbcon.connections import get_db_connection

logger = get_logger(__name__)


def get_dash_users() -> dict:
    sel_query = """SELECT *
                    FROM dash.users
                    ;"""
    df = pd.read_sql(sel_query, DBCON.engine)
    users_dict = df.set_index("username").to_dict(orient="index")
    return users_dict


def get_app_categories() -> list[str]:
    sel_query = """SELECT DISTINCT category
                    FROM networks_with_app_metrics
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    category_list = df["category"].tolist()
    category_list.sort()
    return category_list


def query_networks_with_app_metrics() -> pd.DataFrame:
    table_name = "networks_with_app_metrics"
    sel_query = f"""SELECT
                    *
                    FROM 
                    {table_name}
                    ;
                """
    df = pd.read_sql(sel_query, DBCON.engine)
    df = df.rename(
        columns={
            "publisher_urls": "publishers_count",
            "total_publisher_urls": "publishers_total",
        }
    )
    return df


def query_networks_count(top_only: bool = False) -> pd.DataFrame:
    if top_only:
        table_name = "network_counts_top"
    else:
        table_name = "network_counts"
    sel_query = f"""SELECT
                    *
                    FROM 
                    {table_name}
                    ;
                """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def query_network_uniqueness(limit=100):
    sel_query = f"""
        SELECT
        ad_domain_url,
        count(DISTINCT publisher_id) AS publisher_count,
        sum(is_unique) AS unique_count
    FROM
        publisher_url_developer_ids_uniques
    GROUP BY
        ad_domain_url
    ORDER BY publisher_count DESC
    LIMIT {limit}
    ;
    """
    df = pd.read_sql(sel_query, DBCON.engine)
    df["percent"] = df["unique_count"] / df["publisher_count"]
    return df


def get_app_txt_view(developer_url: str, direct_only=True) -> pd.DataFrame:
    if direct_only:
        direct_only_str = "AND av.relationship = 'DIRECT'"
    else:
        direct_only_str = ""
    sel_query = f"""WITH cte1 AS (
            SELECT
                av.developer_domain_url,
                av.ad_domain AS ad_domain_id,
                av.ad_domain_url,
                av.publisher_id
            FROM
                app_ads_view av
            WHERE
                av.developer_domain_url LIKE '{developer_url}'
                {direct_only_str}
                )
            SELECT
                c1.developer_domain_url AS my_domain_url,
                av2.developer_domain_url AS their_domain_url,
                CASE
                  WHEN av2.developer_domain_url != c1.developer_domain_url
                    THEN 'FAIL'
                    ELSE 'PASS'
                  END AS is_my_id,
                av2.publisher_id,
                av2.ad_domain_url,
                av2.ad_domain AS ad_domain_id,
                av2.relationship AS relationship,
                av2.txt_entry_crawled_at
            FROM
                cte1 c1
            LEFT JOIN app_ads_view av2 ON
                av2.ad_domain_url = c1.ad_domain_url
                AND av2.publisher_id = c1.publisher_id
                    ;
                """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def query_store_apps_overview(start_date: str):
    logger.info("Query logging.store_apps_snapshot")
    sel_query = f"""SELECT
                        sas.*,
                        s.name AS store_name,
                        coalesce(cr.outcome, 'not_crawled') AS outcome
                    FROM
                    logging.store_apps_snapshot sas
                    LEFT JOIN crawl_results cr
                        ON cr.id = sas.crawl_result
                    LEFT JOIN stores s
                        ON s.id = sas.store
                    where updated_at >= '{start_date}'
                    ;
                """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df = df.drop(["store", "crawl_result"], axis=1)
    return df


def query_pub_domains_overview(start_date: str):
    logger.info("Query logging.pub_domains_snapshot")
    sel_query = f"""SELECT
                        ss.*,
                        coalesce(cr.outcome, 'not_crawled') AS outcome
                    FROM
                    logging.snapshot_pub_domains ss
                    LEFT JOIN crawl_results cr
                        ON cr.id = ss.crawl_result
                    where updated_at >= '{start_date}'
                    ;
                """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df = df.drop(["crawl_result"], axis=1)
    return df


def query_recent_apps(days: int = 7):
    logger.info("Query app_store for recent apps")
    limit = 10
    my_date = (
        datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
    ).strftime("%Y-%m-%d")
    sel_query = f"""WITH RankedApps AS (
                    SELECT
                        *,
                        ROW_NUMBER() OVER(PARTITION BY store 
                        ORDER BY 
                            installs DESC NULLS LAST, 
                            review_count DESC NULLS LAST
                    ) AS rn
                    FROM store_apps sa
                    WHERE
                        sa.release_date >= '{my_date}'
                        AND crawl_result = 1
                )
                SELECT *
                FROM RankedApps
                WHERE rn <= {limit}
                ;
                """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df = clean_app_df(df)
    return df


def query_app_store_sources(start_date: str = "2021-01-01") -> pd.DataFrame:
    logger.info(f"Query app_store sources: table_name=app_store_sources {start_date=}")
    sel_query = f"""SELECT 
                        created_at::date AS date,
                        sa.store,
                        COALESCE(crawl_source, 'unknown') AS crawl_source,
                        count(*) as app_count
                    FROM store_apps sa
                        LEFT JOIN logging.store_app_sources sas
                        ON sas.store_app = sa.id
                    WHERE sa.created_at >= '{start_date}'
                    GROUP BY 
                        created_at::date, 
                        sa.store,
                        COALESCE(crawl_source, 'unknown')
                    ;
                    """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
    df["store"] = df["store"].replace({1: "Google Play", 2: "Apple App Store"})
    return df


def query_developer_updated_timestamps(start_date: str = "2021-01-01") -> pd.DataFrame:
    logger.info(f"Query updated times: table_name=developers {start_date=}")
    sel_query = f"""WITH my_dates AS (
                    SELECT
                        store,
                        generate_series('{start_date}', 
                            CURRENT_DATE, '1 day'::INTERVAL)::date AS date
                    FROM generate_series(1, 2, 1) AS num_series(store)
                    ),
                    updated_dates AS (
                    SELECT
                        store,
                        dca.apps_crawled_at::date AS crawled_date,
                        count(1) AS devs_crawled_count
                    FROM
                        developers d
                    LEFT JOIN logging.developers_crawled_at dca
                        ON dca.developer = d.id
                    WHERE
                        dca.apps_crawled_at >= '{start_date}'
                    GROUP BY
                        store,
                        dca.apps_crawled_at::date
                    ),
                    created_dates AS (
                    SELECT
                        store,
                        created_at::date AS created_date,
                        count(1) AS created_count
                    FROM
                        developers
                    WHERE
                        created_at >= '{start_date}'
                    GROUP BY
                        store,
                        created_at::date
                        )
                    SELECT
                        my_dates.store AS store,
                        my_dates.date AS date,
                        updated_dates.devs_crawled_count,
                        created_dates.created_count
                    FROM
                        my_dates
                    LEFT JOIN updated_dates ON
                        my_dates.date = updated_dates.crawled_date 
                            AND my_dates.store = updated_dates.store
                    LEFT JOIN created_dates ON
                        my_dates.date = created_dates.created_date
                            AND my_dates.store = created_dates.store
                    ORDER BY
                        my_dates.date DESC
                    ;
                """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df = df.fillna(0)
    df["store"] = df["store"].replace({1: "Google Play", 2: "Apple App Store"})
    return df


def query_app_updated_timestamps(
    table_name: str, start_date: str = "2021-01-01"
) -> pd.DataFrame:
    logger.info(f"Query updated times: {table_name=} {start_date=}")
    audit_join, audit_select = "", ""
    if table_name == "store_apps":
        audit_select = " audit_dates.updated_count, "
        audit_join = """LEFT JOIN audit_dates ON
                        my_dates.date = audit_dates.updated_date
                        """
    sel_query = f"""WITH my_dates AS (
                    SELECT
                        store,
                        generate_series('{start_date}', 
                            CURRENT_DATE, '1 day'::INTERVAL)::date AS date
                    FROM generate_series(1, 2, 1) AS num_series(store)
                    ),
                    updated_dates AS (
                    SELECT
                        store,
                        updated_at::date AS last_updated_date,
                        count(1) AS last_updated_count
                    FROM
                        {table_name}
                    WHERE
                        updated_at >= '{start_date}'
                    GROUP BY
                        store,
                        updated_at::date
                    ),
                    created_dates AS (
                    SELECT
                        store,
                        created_at::date AS created_date,
                        count(1) AS created_count
                    FROM
                        {table_name}
                    WHERE
                        created_at >= '{start_date}'
                    GROUP BY
                        store,
                        created_at::date
                        )
                    SELECT
                        my_dates.store AS store,
                        my_dates.date AS date,
                        updated_dates.last_updated_count,
                        {audit_select}
                        created_dates.created_count
                    FROM
                        my_dates
                    LEFT JOIN updated_dates ON
                        my_dates.date = updated_dates.last_updated_date 
                            AND my_dates.store = updated_dates.store
                    {audit_join}
                    LEFT JOIN created_dates ON
                        my_dates.date = created_dates.created_date
                            AND my_dates.store = created_dates.store
                    ORDER BY
                        my_dates.date DESC
                    ;
                """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df = df.fillna(0)
    df["store"] = df["store"].replace({1: "Google Play", 2: "Apple App Store"})
    return df


def query_updated_timestamps(
    table_name: str, start_date: str = "2021-01-01"
) -> pd.DataFrame:
    logger.info(f"Query updated times: {table_name=}")
    sel_query = f"""WITH my_dates AS (
                    SELECT
                        generate_series('{start_date}', 
                            CURRENT_DATE, '1 day'::INTERVAL)::date AS date),
                    updated_dates AS (
                    SELECT
                        updated_at::date AS last_updated_date,
                        count(1) AS last_updated_count
                    FROM
                        {table_name}
                    WHERE
                        updated_at >= '{start_date}'
                    GROUP BY
                        updated_at::date),
                    created_dates AS (
                    SELECT
                        created_at::date AS created_date,
                        count(1) AS created_count
                    FROM
                        {table_name}
                    WHERE
                        created_at >= '{start_date}'
                    GROUP BY
                        created_at::date)
                    SELECT
                        my_dates.date AS date,
                        updated_dates.last_updated_count,
                        created_dates.created_count
                    FROM
                        my_dates
                    LEFT JOIN updated_dates ON
                        my_dates.date = updated_dates.last_updated_date
                    LEFT JOIN created_dates ON
                        my_dates.date = created_dates.created_date
                    ORDER BY
                        my_dates.date DESC
                    ;
                """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    df = df.fillna(0)
    return df


def query_search_developers(search_input: str, limit: int = 1000):
    logger.info(f"Developer search: {search_input=}")
    search_input = f"%%{search_input}%%"
    sel_query = f"""SELECT
                        d.*,
                        pd.*,
                        sa.*
                    FROM
                        app_urls_map aum
                    LEFT JOIN pub_domains pd ON
                        pd.id = aum.pub_domain
                    LEFT JOIN store_apps sa ON
                        sa.id = aum.store_app
                    LEFT JOIN developers d ON
                        d.id = sa.developer
                    WHERE
                        d.name ILIKE '{search_input}'
                        OR d.developer_id ILIKE '{search_input}'
                        OR pd.url ILIKE '{search_input}'
                    LIMIT {limit}
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def get_all_tables_in_schema(schema_name: str):
    logger.info("Get checks tables")
    sel_schema = f"""SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = '{schema_name}'
    ;"""
    tables = pd.read_sql(sel_schema, DBCON.engine)
    tables = tables["table_name"].values.tolist()
    return tables


def get_schema_overview(schema_name: str = "public") -> pd.DataFrame:
    sel_query = f"""SELECT
                        table_schema,
                        table_name,
                        column_name
                    FROM
                        information_schema.columns
                    WHERE
                        table_schema ='{schema_name}'
                    ORDER BY
                        table_schema,
                        table_name
                ;
                """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def get_appstore_categories() -> pd.DataFrame:
    sel_query = """SELECT *
                    FROM mv_app_categories
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    df["store"] = df["store"].replace({1: "android", 2: "ios"})
    df = pd.pivot_table(
        data=df, index="category", values="app_count", columns="store", fill_value=0
    ).reset_index()
    df["total_apps"] = df["android"] + df["ios"]
    df = df.sort_values("total_apps", ascending=False)

    return df


def get_top_apps_by_installs(
    category_in: list[str] | None = None, limit: int = 10
) -> pd.DataFrame:
    logger.info("Query top installs")
    if category_in is not None:
        my_list_str = "('" + "','".join(category_in) + "')"
        where_str = f""" JOIN category_mapping cm 
                    ON sa.category = cm.original_category
                    WHERE cm.mapped_category IN {my_list_str}
                    """
    else:
        where_str = ""

    sel_query = f"""
                WITH RankedApps AS (
                    SELECT
                        *,
                        ROW_NUMBER() OVER(PARTITION BY store 
                        ORDER BY installs DESC NULLS LAST, review_count DESC NULLS LAST
                    ) AS rn
                    FROM store_apps sa
                    {where_str}
                )
                SELECT *
                FROM RankedApps
                WHERE rn <= {limit}
                ;
                """

    df = pd.read_sql(sel_query, DBCON.engine)
    # df["store"] = df["store"].replace({1: "android", 2: "ios"})
    df["store"] = df["store"].replace({1: "Google Play", 2: "Apple App Store"})
    df["installs"] = df["installs"].apply(lambda x: "{:,.0f}".format(x) if x else "N/A")
    df["review_count"] = df["review_count"].apply(
        lambda x: "{:,.0f}".format(x) if x else "N/A"
    )
    df["rating"] = df["rating"].apply(lambda x: "{:.2f}".format(x) if x else "N/A")
    ios_link = "https://apps.apple.com/us/app/-/id"
    play_link = "https://play.google.com/store/apps/details?id="
    df["store_link"] = (
        np.where(df["store"].str.contains("Google"), play_link, ios_link)
        + df["store_id"]
    )
    return df


def get_single_app(app_id: str) -> pd.DataFrame:
    logger.info(f"Query for single app_id={app_id}")
    where_str = f"WHERE store_id = '{app_id}'"
    where_str = text(where_str)
    sel_query = f"""SELECT
                        sa.*,
                        d.developer_id,
                        d.name as developer_name,
                        pd.url as developer_url
                    FROM store_apps sa
                    LEFT JOIN developers d
                        ON d.id = sa.developer
                    LEFT JOIN app_urls_map aum
                        ON aum.store_app = sa.id
                    LEFT JOIN pub_domains pd
                        ON pd.id = aum.pub_domain
                    {where_str}
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    df = clean_app_df(df)
    return df


def clean_app_df(df: pd.DataFrame) -> pd.DataFrame:
    df["store"] = df["store"].replace({1: "Google Play", 2: "Apple App Store"})
    df["installs"] = df["installs"].apply(lambda x: "{:,.0f}".format(x) if x else "N/A")
    df["review_count"] = df["review_count"].apply(
        lambda x: "{:,.0f}".format(x) if x else "N/A"
    )
    df["rating"] = df["rating"].apply(lambda x: round(x, 2) if x else 0)
    ios_link = "https://apps.apple.com/us/app/-/id"
    play_link = "https://play.google.com/store/apps/details?id="
    df["store_link"] = (
        np.where(df["store"].str.contains("Google"), play_link, ios_link)
        + df["store_id"]
    )
    df["rating_percent"] = (1 - (df["rating"] / 5)) * 100
    return df


def get_app_history(store_app: int) -> pd.DataFrame:
    logger.info(f"Query for history single app_id={store_app}")
    where_str = f"WHERE store_app = '{store_app}'"
    where_str = text(where_str)
    sel_query = f"""SELECT
                    *
                    FROM store_apps_country_history sah
                    {where_str}
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def get_apps_by_name(search_input: str, limit: int = 100):
    logger.info(f"App search: {search_input=}")
    search_input = f"%%{search_input}%%"
    sel_query = f"""SELECT
                    sa.*,
                    d.name as developer_name
                    FROM
                        store_apps sa
                    LEFT JOIN developers d ON
                        d.id = sa.developer
                    WHERE
                        sa.name ILIKE '{search_input}'
                        OR sa.store_id ILIKE '{search_input}'
                    LIMIT {limit}
                    ;
                    """

    df = pd.read_sql(sel_query, DBCON.engine)
    df["store"] = df["store"].replace({1: "android", 2: "ios"})
    return df


try:
    logger.info("set db engine")
    DBCON = get_db_connection("madrone")
    DBCON.set_engine()
    APP_CATEGORIES = get_app_categories()
except Exception:
    logger.info("Database Connection failed")
    APP_CATEGORIES = ["cat1", "cat2"]
