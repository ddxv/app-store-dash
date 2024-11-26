WITH ranked_apps AS (
    SELECT *
    FROM
        adtech.company_top_apps
    WHERE
        company_domain = :company_domain
        AND category = :mapped_category
        AND app_company_category_rank <= :mylimit
)

SELECT
    ranked_apps.company_domain,
    ranked_apps.store,
    ranked_apps.tag_source,
    ranked_apps.name,
    ranked_apps.store_id,
    ranked_apps.app_company_category_rank AS rank,
    ranked_apps.rating_count,
    ranked_apps.installs
FROM ranked_apps
ORDER BY
    ranked_apps.store, ranked_apps.tag_source,
    ranked_apps.app_company_category_rank;
