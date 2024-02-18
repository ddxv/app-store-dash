WITH
counts AS (
    SELECT
        sac.company_id,
        COUNT(DISTINCT sac.store_app) AS app_count
    FROM
        adtech.store_apps_companies sac
    LEFT JOIN adtech.company_categories cc
ON
        sac.company_id = cc.company_id
    LEFT JOIN adtech.categories cat ON
        cc.category_id = cat.id
    WHERE
        cat.id IN :categories
    GROUP BY
        sac.company_id
),
total_app_count AS (
    SELECT
        COUNT(DISTINCT store_app)
    FROM
        adtech.store_apps_companies
)
SELECT
    c.name AS name,
    tc.app_count,
    total_app_count.count AS total_app_count,
    (
        tc.app_count / total_app_count.count::decimal
    ) AS PERCENT
    FROM
    counts AS tc
    LEFT JOIN adtech.companies AS c
    ON
        tc.company_id = c.id
    INNER JOIN total_app_count
    ON TRUE
    ORDER BY
    tc.app_count DESC;
