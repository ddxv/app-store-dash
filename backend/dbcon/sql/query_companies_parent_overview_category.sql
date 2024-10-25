SELECT
    company_domain,
    company_name,
    store,
    app_category,
    tag_source,
    SUM(app_count) AS app_count
FROM
    adtech.companies_parent_app_counts
WHERE
    app_category = :app_category
GROUP BY company_domain, company_name, store, app_category, tag_source;
