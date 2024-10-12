SELECT
    ad_network,
    store,
    tag_source,
    sum(app_count) AS app_count
FROM
    adtech.companies_app_counts
WHERE
    app_category = :app_category
    AND (NULL IS NULL OR app_category IS NULL)
GROUP BY ad_network, store, tag_source
ORDER BY app_count DESC;
