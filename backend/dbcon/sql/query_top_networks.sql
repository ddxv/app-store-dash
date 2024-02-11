WITH
network_counts AS (
    SELECT
        network,
        count(DISTINCT store_app) AS app_count
    FROM
        store_apps_networks
    GROUP BY
        network
),

total_app_count AS (
    SELECT count(DISTINCT store_app)
    FROM
        store_apps_networks
)

SELECT
    t.name AS network_name,
    tc.app_count,
    total_app_count.count AS total_app_count,
    (
        tc.app_count / total_app_count.count::decimal
    ) AS percent
FROM
    network_counts AS tc
LEFT JOIN networks AS t
    ON
        tc.network = t.id
INNER JOIN total_app_count ON
    TRUE;
