SELECT *
FROM
    public.store_apps
WHERE
    id IN
    (
        SELECT sac.store_app
        FROM
            adtech.store_apps_companies AS sac
        LEFT JOIN adtech.companies AS c
            ON
                sac.company_id = c.id
        WHERE
            c.name = :network_name
    )
ORDER BY installs DESC
LIMIT :mylimit;
