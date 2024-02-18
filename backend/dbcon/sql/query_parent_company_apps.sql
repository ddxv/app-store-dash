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
        LEFT JOIN adtech.companies AS pc
            ON
                sac.company_id = pc.parent_company_id
        WHERE
            c.name = :network_name OR pc.name = :network_name
    )
ORDER BY installs DESC
LIMIT :mylimit;
