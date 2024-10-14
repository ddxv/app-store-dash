WITH ranked_apps AS (
    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY store, tag_source
            ORDER BY
                GREATEST(
                    COALESCE(rating_count, 0), COALESCE(installs, 0)
                ) DESC
        ) AS rank
    FROM
        adtech.company_top_apps
    WHERE
        company_domain = :company_domain
        AND (:mapped_category IS NULL OR category = :mapped_category)
)

SELECT *
FROM ranked_apps
WHERE rank <= :mylimit
ORDER BY store, tag_source, rank;
