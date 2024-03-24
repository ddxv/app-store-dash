WITH
counts AS (
    SELECT
        cm.mapped_category,
        sac.company_id,
        COUNT(DISTINCT sac.store_app) AS app_count
    FROM
        adtech.store_apps_companies sac
    LEFT JOIN adtech.company_categories cc ON
            sac.company_id = cc.company_id
    LEFT JOIN adtech.categories cat ON
        cc.category_id = cat.id
    LEFT JOIN store_apps sa ON
        sac.store_app = sa.id
    LEFT JOIN category_mapping cm ON
        sa.category = cm.original_category
    WHERE
        cat.id IN :categories
    GROUP BY
        cm.mapped_category,
        sac.company_id
),
total_app_count AS (
    SELECT
        cm.mapped_category,
        COUNT(DISTINCT store_app)
    FROM
        adtech.store_apps_companies sac
    LEFT JOIN store_apps sa ON
        sac.store_app = sa.id
    LEFT JOIN category_mapping cm ON
        sa.category = cm.original_category
    GROUP BY
        cm.mapped_category
)
SELECT
    tc.mapped_category,
    c.name AS name,
    tc.app_count,
    tac.count AS total_app_count,
    (
        tc.app_count / tac.count::decimal
    ) AS PERCENT
FROM
    counts AS tc
LEFT JOIN adtech.companies AS c ON
    tc.company_id = c.id
INNER JOIN total_app_count tac ON
    tc.mapped_category = tac.mapped_category
ORDER BY
    tc.app_count DESC
;
