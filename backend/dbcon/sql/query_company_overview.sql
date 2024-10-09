SELECT
    ad_network,
    store,
    tag_source,
    app_category,
    sum(app_count) AS app_count
FROM
    adtech.companies_app_counts
WHERE ad_network = :company
GROUP BY ad_network, store, tag_source, app_category
ORDER BY app_count DESC;
