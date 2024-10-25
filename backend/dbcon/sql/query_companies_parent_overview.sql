SELECT
    company_domain,
    company_name,
    store,
    'all' AS app_category,
    tag_source,
    sum(app_count) AS app_count
FROM
    adtech.companies_parent_app_counts
GROUP BY company_domain, company_name, store, tag_source;
