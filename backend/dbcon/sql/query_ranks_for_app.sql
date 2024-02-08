SELECT
    ar.crawled_date,
    ar.country,
    ar.store,
    ar.rank,
    scol.collection,
    scat.category
FROM
    app_rankings AS ar
LEFT JOIN
    store_apps AS sa
    ON ar.store_app = sa.id
LEFT JOIN store_collections AS scol
    ON ar.store_collection = scol.id
LEFT JOIN store_categories AS scat
    ON ar.store_category = scat.id
WHERE
    sa.store_id = :store_id
    AND
    ar.crawled_date >= :start_date;
