SELECT
    ad_network,
    store,
    tag_source,
    sum(app_count) AS app_count
FROM
    adtech.companies_app_counts
GROUP BY ad_network, store, tag_source
ORDER BY app_count DESC;
