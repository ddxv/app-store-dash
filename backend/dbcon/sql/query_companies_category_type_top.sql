WITH ranked_apps AS (
    SELECT
        company_domain,
        company_name,
        tag_source,
        SUM(app_count) AS app_count,
        ROW_NUMBER() OVER (
            PARTITION BY tag_source
            ORDER BY SUM(app_count) DESC
        ) AS rank
    FROM
        adtech.companies_categories_types_app_counts
    WHERE
        type_url_slug = :type_slug
        AND (app_category = :app_category OR :app_category IS NULL)
    GROUP BY company_domain, company_name, tag_source
)

SELECT
    tag_source,
    company_domain,
    company_name,
    app_count
FROM ranked_apps
WHERE rank <= :mylimit
ORDER BY tag_source, rank;
