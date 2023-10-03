import pandas as pd

from config import get_logger
from dbcon.connections import get_db_connection
from sqlalchemy import text

logger = get_logger(__name__)


def get_app_categories() -> pd.DataFrame:
    sel_query = """SELECT *
                    FROM mv_app_categories
                    ;
                    """
    df = pd.read_sql(sel_query, DBCON.engine)
    df["store"] = df["store"].replace({1: "android", 2: "ios"})
    df = pd.pivot_table(
        data=df, index="category", values="app_count", columns="store", fill_value=0
    ).reset_index()
    return df


def get_top_apps_by_installs(category_in : list[str]=None, limit: int = 10) -> pd.DataFrame:
    logger.info("Query top installs")

    where_str = "" if category_in is None else f"WHERE category IN ('{"','".join(category_in)}') "

    sel_query = f"""SELECT
                    *
                    FROM store_apps sa
                    {where_str}
                    ORDER BY installs DESC NULLS LAST
                    LIMIT {limit}
                    ;
                    """

    df = pd.read_sql(sel_query, DBCON.engine)
    df["store"] = df["store"].replace({1: "android", 2: "ios"})
    return df

def get_single_app(app_id : str) -> pd.DataFrame:
    logger.info("Query for single app")
    where_str = f"WHERE store_id = '{app_id}'"
    where_str = text(where_str)
    sel_query = f"""SELECT
                    *
                    FROM store_apps sa
                    {where_str}
                    ;
                    """
    print(sel_query)
    df = pd.read_sql(sel_query, DBCON.engine)
    df["store"] = df["store"].replace({1: "android", 2: "ios"})
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


try:
    logger.info("set db engine")
    DBCON = get_db_connection("my-database")
    DBCON.set_engine()
except Exception:
    logger.info("Database Connection failed")
