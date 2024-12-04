SELECT
    app_category,
    company_domain,
    type_url_slug,
    sum(app_count) AS app_count
FROM
    adtech.companies_categories_types_app_counts
GROUP BY
    app_category,
    company_domain,
    type_url_slug
ORDER BY
    sum(app_count) DESC;
