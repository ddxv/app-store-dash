SELECT DISTINCT
    ar.store AS store_id,
    s.name AS store_name,
    ar.store_collection AS collection_id,
    scol.collection AS collection_name,
    ar.store_category AS category_id,
    scat.category AS category_name
FROM
    app_rankings AS ar
LEFT JOIN
    stores AS s
    ON ar.store = s.id
LEFT JOIN
    store_collections AS scol
    ON ar.store_collection = scol.id AND ar.store = scol.store
LEFT JOIN
    store_categories AS scat
    ON ar.store_category = scat.id AND ar.store = scat.store
WHERE
    ar.crawled_date = CURRENT_DATE - INTERVAL '1 day';
