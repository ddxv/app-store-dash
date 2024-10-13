WITH ranked_apps AS (
    SELECT
        ad_network,
        tag_source,
        SUM(app_count) AS app_count,
        ROW_NUMBER() OVER (
            PARTITION BY tag_source
            ORDER BY SUM(app_count) DESC
        ) AS rank
    FROM
        adtech.companies_parent_app_counts
    WHERE
        app_category = :app_category OR :app_category IS NULL
    GROUP BY ad_network, tag_source
)

SELECT
    tag_source,
    ad_network,
    app_count
FROM ranked_apps
WHERE rank <= :mylimit
ORDER BY tag_source, rank;
