SELECT
    sar.crawled_date,
    sar.country,
    sar.store,
    sar.rank,
    sar.collection,
    sar.category
FROM
    store_apps_rankings AS sar
WHERE
    sar.store_id = :store_id
    AND
    sar.crawled_date >= :start_date;
