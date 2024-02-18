WITH
parent_counts AS (
    SELECT
        COALESCE(
            ccom.parent_company_id,
            sac.company_id
        ) AS parent_or_self_id,
        COUNT(DISTINCT sac.store_app) AS app_count
    FROM
        adtech.store_apps_companies sac
    LEFT JOIN adtech.company_categories cc
ON
        sac.company_id = cc.company_id
    LEFT JOIN adtech.categories cat ON
        cc.category_id = cat.id
    LEFT JOIN adtech.companies ccom
    ON
        sac.company_id = ccom.id
    WHERE
        cat.id IN :categories
    GROUP BY
        parent_or_self_id
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
    parent_counts AS tc
    LEFT JOIN adtech.companies AS c
    ON
    tc.parent_or_self_id = c.id
    INNER JOIN total_app_count
    ON
    TRUE
    ORDER BY
    tc.app_count DESC;
