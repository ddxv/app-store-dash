SELECT *
FROM
    adtech.companies_categories_types_app_counts
WHERE
    type_url_slug = :type_slug
    AND (app_category = :app_category OR :app_category IS NULL)
ORDER BY
    app_count DESC;
