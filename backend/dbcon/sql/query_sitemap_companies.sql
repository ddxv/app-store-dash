SELECT
    sum(app_count) AS app_count ,
    app_category,
    company_domain,
    type_url_slug
FROM
    adtech.companies_categories_types_app_counts cctac
GROUP BY
    app_category,
    company_domain,
    type_url_slug
ORDER BY
    sum(app_count) DESC
;