SELECT
    store,
    tag_source,
    'all' AS app_category,
    sum(app_count) AS app_count
FROM
    adtech.total_categories_app_counts
GROUP BY
    store, tag_source;
