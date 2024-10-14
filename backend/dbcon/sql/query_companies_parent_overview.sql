SELECT
    company_domain,
    company_name,
    store,
    app_category,
    tag_source,
    sum(app_count) AS app_count
FROM
    adtech.companies_parent_app_counts
WHERE
    app_category = :app_category OR :app_category IS NULL
GROUP BY company_domain, company_name, store, app_category, tag_source
ORDER BY app_count DESC;
