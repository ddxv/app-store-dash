WITH
parent_counts AS (
    SELECT
        cm.mapped_category,
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
    LEFT JOIN adtech.companies ccom ON
        sac.company_id = ccom.id
    LEFT JOIN store_apps sa ON
        sac.store_app = sa.id
    LEFT JOIN category_mapping cm ON
        sa.category = cm.original_category
    WHERE
        cat.id IN :categories
    GROUP BY
        cm.mapped_category,
        parent_or_self_id
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
    parent_counts AS tc
LEFT JOIN adtech.companies AS c
    ON
    tc.parent_or_self_id = c.id
INNER JOIN total_app_count tac
    ON
    tc.mapped_category = tac.mapped_category
ORDER BY
    tc.app_count DESC;
