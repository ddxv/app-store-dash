SELECT *
FROM
    store_apps
WHERE
    id IN
    (
        SELECT sat.store_app
        FROM
            store_apps_trackers AS sat
        LEFT JOIN trackers AS t
            ON
                sat.tracker = t.id
        WHERE
            t.name = :tracker_name
    )
ORDER BY installs DESC
LIMIT :mylimit;
