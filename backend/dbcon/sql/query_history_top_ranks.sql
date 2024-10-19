SELECT
    arr.crawled_date,
    arr.rank,
    sa.name,
    sa.store_id
FROM
    app_rankings AS arr
LEFT JOIN
    store_apps AS sa ON arr.store_app = sa.id
WHERE
    arr.store_app IN (
        SELECT ar.store_app
        FROM
            app_rankings AS ar
        WHERE
            ar.crawled_date
            = (
                SELECT max(arr.crawled_date)
                FROM app_rankings arr
                WHERE arr.store = :store
            )
            AND ar.store = :store
            AND ar.store_collection = :collection_id
            AND ar.store_category = :category_id
        LIMIT :mylimit
    )
    AND arr.crawled_date >= :start_date
    AND arr.store = :store
    AND arr.store_collection = :collection_id
    AND arr.store_category = :category_id;
