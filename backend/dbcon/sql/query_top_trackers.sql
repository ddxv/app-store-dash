WITH
tracker_counts AS (
    SELECT
        tracker,
        count(DISTINCT store_app) AS app_count
    FROM
        store_apps_trackers
    GROUP BY
        tracker
),

total_app_count AS (
    SELECT count(DISTINCT store_app)
    FROM
        store_apps_trackers
)

SELECT
    t.name AS tracker_name,
    tc.app_count,
    total_app_count.count AS total_app_count,
    (
        tc.app_count / total_app_count.count::decimal
    ) AS percent
FROM
    tracker_counts AS tc
LEFT JOIN trackers AS t
    ON
        tc.tracker = t.id
INNER JOIN total_app_count ON
    TRUE;
