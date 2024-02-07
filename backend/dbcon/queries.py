import datetime

import numpy as np
import pandas as pd
from sqlalchemy import TextClause, text

from config import get_logger
from dbcon.connections import get_db_connection

logger = get_logger(__name__)


def query_recent_apps(collection: str, limit: int = 20) -> pd.DataFrame:
    logger.info(f"Query app_store for recent apps {collection=}")
    if collection == "new_weekly":
        table_name = "apps_new_weekly"
    elif collection == "new_monthly":
        table_name = "apps_new_monthly"
    elif collection == "new_yearly":
        table_name = "apps_new_yearly"
    elif collection == "top":
        table_name = "top_categories"
    else:
        table_name = "apps_new_weekly"
    my_cols = ", ".join(
        [
            "name",
            "store",
            "mapped_category",
            "store_id",
            "installs",
            "review_count",
            "rating_count",
            "rating",
            "icon_url_512",
            "featured_image_url",
            "phone_image_url_1",
            "tablet_image_url_1",
        ],
    )
    sel_query = f"""
                (
                    SELECT 
                        {my_cols}
                    FROM {table_name}
                    WHERE store = 1
                    ORDER BY installs DESC NULLS LAST
                )
                UNION ALL
                (
                    SELECT
                        {my_cols}
                    FROM {table_name}
                    WHERE store = 2
                    ORDER BY rating_count DESC NULLS LAST
                );
                """
    sel_query = f"""WITH    NumberedRows AS (
                    SELECT 
                        {my_cols},
                        ROW_NUMBER() OVER (PARTITION BY store, mapped_category
                    ORDER BY 
                        CASE WHEN store = 1 THEN installs ELSE rating_count END DESC NULLS LAST
                ) AS rn
                FROM {table_name}
            )
            SELECT 
                {my_cols}
            FROM NumberedRows
            WHERE rn <= {limit}
            ;
            """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    groups = df.groupby("store")
    for _store, group in groups:
        overall = group.sort_values(["installs", "rating_count"], ascending=False).head(
            limit,
        )
        overall["mapped_category"] = "overall"
        df = pd.concat([df, overall], axis=0)
    df = clean_app_df(df)
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
    table_name: str,
    start_date: str = "2021-01-01",
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
    table_name: str,
    start_date: str = "2021-01-01",
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


def get_all_tables_in_schema(schema_name: str) -> list[str]:
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
        data=df,
        index="category",
        values="app_count",
        columns="store",
        fill_value=0,
    ).reset_index()
    df["total_apps"] = df["android"] + df["ios"]
    df = df.sort_values("total_apps", ascending=False)

    return df


def query_ranks_for_app(store_id: str, days: int = 30) -> pd.DataFrame:
    start_date = (
        datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    ).strftime("%Y-%m-%d")
    sel_query = f"""SELECT
                    ar.crawled_date,
                    ar.country,
                    ar.store,
                    ar.rank,
                    scol.collection,
                    scat.category
                FROM
                    app_rankings ar
                LEFT JOIN
                    store_apps sa
                    ON sa.id = ar.store_app
                LEFT JOIN store_collections scol
                    ON scol.id = ar.store_collection
                LEFT JOIN store_categories scat
                    ON scat.id = ar.store_category
                WHERE
                    sa.store_id = '{store_id}'
                    AND
                        crawled_date >= '{start_date}'
                ;
        """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    return df


def get_most_recent_top_ranks(
    store: int,
    collection_id: int,
    category_id: int,
    limit: int = 25,
) -> pd.DataFrame:
    sel_query = f"""SELECT
                ar.rank,
                sa.name,
                sa.store_id,
                sa.icon_url_512
            FROM
                app_rankings ar
            LEFT JOIN
                stores s
                    ON s.id = ar.store
            LEFT JOIN
                store_apps sa ON sa.id = ar.store_app
            WHERE
                crawled_date = (SELECT max(crawled_date) FROM app_rankings WHERE store={store})
                AND ar.store = {store}
                AND ar.store_collection = {collection_id}
                AND ar.store_category = {category_id}
            LIMIT {limit}
            ;
        """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    return df


def get_history_top_ranks(
    store: int,
    collection_id: int,
    category_id: int,
    limit: int = 25,
    days=30,
) -> pd.DataFrame:
    start_date = (
        datetime.datetime.now(datetime.UTC) - datetime.timedelta(days=days)
    ).strftime("%Y-%m-%d")
    sel_query = f"""SELECT
            arr.crawled_date,
            arr.rank,
            sa.name,
            sa.store_id
            FROM
                app_rankings arr
            LEFT JOIN
                store_apps sa ON sa.id = arr.store_app
            WHERE
                arr.store_app IN (
                    SELECT
                        ar.store_app
                    FROM
                        app_rankings ar
                    WHERE
                        ar.crawled_date = (SELECT max(crawled_date) FROM app_rankings WHERE store={store})
                        AND ar.store = {store}
                        AND ar.store_collection = {collection_id}
                        AND ar.store_category = {category_id}
                    LIMIT {limit}
                    )
            AND arr.crawled_date >= '{start_date}'
            AND arr.store = {store}
            AND arr.store_collection = {collection_id}
            AND arr.store_category = {category_id}
            ;
        """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    return df


def get_store_collection_category_map() -> pd.DataFrame:
    sel_query = """SELECT
                DISTINCT 
                ar.store as store_id,
                s.name as store_name,
                store_collection as collection_id,
                collection as collection_name,
                store_category as category_id,
                category as category_name
            FROM
                app_rankings ar
            LEFT JOIN
                stores s
                    ON s.id = ar.store
            LEFT JOIN 
                store_collections scol
                    ON scol.id = ar.store_collection AND ar.store = scol.store
            LEFT JOIN
                store_categories scat
                    ON scat.id = ar.store_category AND ar.store = scat.store
            WHERE
                crawled_date = CURRENT_DATE - INTERVAL '1 day'
            ;
        """
    df = pd.read_sql(sel_query, con=DBCON.engine)
    return df


def get_category_top_apps_by_installs(category: str, limit: int = 10) -> pd.DataFrame:
    logger.info(f"Query {category=} for top installs")
    sel_query = """SELECT * 
            FROM 
                top_categories
            WHERE 
                mapped_category = %s
            LIMIT %s
            ;
        """
    df = pd.read_sql(
        sel_query,
        DBCON.engine,
        params=(category, limit),
    )
    if not df.empty:
        df = clean_app_df(df)
    return df


def get_single_app(store_id: str) -> pd.DataFrame:
    """Get basic app details for a single store_id."""
    logger.info(f"Query for single app_id={store_id}")
    where_str = f"WHERE store_id = '{store_id}'"
    where_stmt: TextClause = text(where_str)
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
                    {where_stmt}
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    if not df.empty:
        df = clean_app_df(df)
    return df


def get_app_package_details(store_id: str) -> pd.DataFrame:
    """Get basic app details for a single store_id."""
    logger.info(f"Query for single app_id={store_id}")
    where_str = f"store_id = '{store_id}'"
    app_where_stmt: TextClause = text(where_str)
    sel_query = f"""WITH latest_version_codes AS (
                    SELECT
                        vc.store_app,
                        MAX(vc.version_code) AS max_version_code
                    FROM
                        version_codes AS vc
                    GROUP BY
                        vc.store_app
                )
                SELECT
                    vc.store_app,
                    sa.store_id,
                    vd.*
                FROM
                    version_details AS vd
                LEFT JOIN
                    version_codes AS vc ON
                    vd.version_code = vc.id
                INNER JOIN
                    latest_version_codes AS lvc ON
                        vc.store_app = lvc.store_app
                    AND vc.version_code = lvc.max_version_code
                LEFT JOIN store_apps sa ON
                    sa.id = vc.store_app
                WHERE
                    vd.android_name != ''
                    AND
                    {app_where_stmt}
                ORDER BY
                    store_app,
                    xml_path,
                    android_name
                ;
    """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def clean_app_df(df: pd.DataFrame) -> pd.DataFrame:
    """Apply generic cleaning for a DF with app data from store_apps table."""
    df["store"] = df["store"].replace({1: "Google Play", 2: "Apple App Store"})
    string_nums = ["installs", "review_count", "rating_count"]
    for col in string_nums:
        df[f"{col}_num"] = df[col]
        df[col] = df[col].apply(
            lambda x: "N/A" if (x is None or np.isnan(x)) else f"{x:,.0f}",
        )
    df["rating"] = df["rating"].apply(lambda x: round(x, 2) if x else 0)
    ios_link = "https://apps.apple.com/us/app/-/id"
    play_link = "https://play.google.com/store/apps/details?id="
    play_dev_link = "https://play.google.com/store/apps/dev?id="
    ios_dev_link = "https://apps.apple.com/us/developer/-/id"
    df["store_link"] = (
        np.where(df["store"].str.contains("Google"), play_link, ios_link)
        + df["store_id"]
    )
    if "developer_id" in df.columns:
        df["store_developer_link"] = np.where(
            df["store"].str.contains("Google"),
            play_dev_link,
            ios_dev_link,
        ) + df["developer_id"].astype(str)

    date_cols = ["created_at", "store_last_updated", "updated_at"]
    for x in date_cols:
        if x not in df.columns:
            continue
        df[x] = df[x].dt.strftime("%Y-%m-%d")
    return df


def query_app_history(store_app: int) -> pd.DataFrame:
    logger.info(f"Query for history single app_id={store_app}")
    where_str = f"WHERE store_app = '{store_app}'"
    where_stmt: TextClause = text(where_str)
    sel_query = f"""SELECT
                    *
                    FROM store_apps_country_history sah
                    {where_stmt}
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


def query_single_developer(developer_id: str) -> pd.DataFrame:
    logger.info(f"Developers: {developer_id=}")
    sel_query = """SELECT
                        d.name AS developer_name,
                        pd.url as developer_url,
                        d.store as developer_store,
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
                        d.developer_id = %s
                    ;
                    """
    df = pd.read_sql(
        sel_query,
        DBCON.engine,
        params=(developer_id,),
    )
    if not df.empty:
        df = clean_app_df(df)
    return df


def search_apps(search_input: str, limit: int = 100) -> pd.DataFrame:
    """Search apps by term in database."""
    logger.info(f"App search: {search_input=}")
    sel_query = """WITH devs AS (
                    SELECT
                        d.id AS developer_id
                    FROM
                        developers d
                    WHERE
                        to_tsvector(
                            'simple',
                            d.name
                        ) @@ to_tsquery(
                            'simple',
                            %s
                        )
                ),
                apps AS (
                    SELECT
                        ssa.id AS app_id
                    FROM
                        store_apps ssa
                    WHERE
                        to_tsvector(
                            'simple',
                            ssa.name
                        ) @@ to_tsquery(
                            'simple',
                            %s
                        )
                )
                SELECT
                    *
                FROM
                    store_apps sa
                FULL OUTER JOIN devs ON
                    sa.developer = devs.developer_id
                FULL OUTER JOIN apps ON
                    sa.id = apps.app_id
                WHERE
                    apps.app_id IS NOT NULL
                    OR devs.developer_id IS NOT NULL
                ORDER BY
                    installs DESC NULLS LAST,
                    rating_count DESC NULLS LAST
                LIMIT %s
                ;
                """
    df = pd.read_sql(
        sel_query,
        DBCON.engine,
        params=(search_input, search_input, limit),
    )
    if not df.empty:
        df = clean_app_df(df)
    return df


def get_manifest_names() -> pd.DataFrame:
    """Get manifest data.

    Data is pulled for some apks and extracted from the AndroidManifest.xml
    """
    sel_query = """WITH latest_version_codes AS (
                    SELECT
                        vc.store_app,
                        MAX(vc.version_code) AS max_version_code
                    FROM
                        version_codes AS vc
                    GROUP BY
                        vc.store_app
                )
                SELECT
                    vc.store_app,
                    sa.store_id,
                    vd.*
                FROM
                    version_details AS vd
                LEFT JOIN
                    version_codes AS vc ON
                    vd.version_code = vc.id
                INNER JOIN
                    latest_version_codes AS lvc ON
                        vc.store_app = lvc.store_app
                    AND vc.version_code = lvc.max_version_code
                LEFT JOIN store_apps sa ON
                    sa.id = vc.store_app
                WHERE
                    vd.android_name != ''
                ORDER BY
                    store_app,
                    xml_path,
                    android_name
                ;
    """
    df = pd.read_sql(sel_query, DBCON.engine)
    return df


logger.info("set db engine")
DBCON = get_db_connection("madrone")
DBCON.set_engine()
