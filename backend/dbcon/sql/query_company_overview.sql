SELECT
    company_domain,
    company_name,
    store,
    tag_source,
    app_category,
    sum(app_count) AS app_count
FROM
    adtech.companies_app_counts
WHERE company_domain = :company_domain
GROUP BY company_domain, company_name, store, tag_source, app_category
ORDER BY app_count DESC;
