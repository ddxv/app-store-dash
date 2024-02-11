SELECT *
FROM
    store_apps
WHERE
    id IN
    (
        SELECT sat.store_app
        FROM
            store_apps_networks AS sat
        LEFT JOIN networks AS t
            ON
                sat.network = t.id
        WHERE
            t.name = :network_name
    )
ORDER BY installs DESC
LIMIT :mylimit;
