SELECT
    cac.ad_network,
    cac.store,
    cac.tag_source,
    sa.name,
    sa.store_id,
    cac.app_category AS category,
    sa.rating_count,
    sa.reviews,
    sa.app_installs
FROM
    adtech.companies_app_counts AS cac
LEFT JOIN store_apps AS sa ON cac.store_app = sa.id
WHERE
    ad_network = :ad_network
    AND cac.store = :store_id
ORDER BY app_count DESC;
