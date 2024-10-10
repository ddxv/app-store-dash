SELECT
    c.name AS company_name,
    sp.package_pattern,
    sp2.path_pattern,
    COALESCE(
        cc.name,
        c.name
    ) AS parent_company_name
FROM
    adtech.companies AS c
LEFT JOIN adtech.companies AS cc
    ON
        c.parent_company_id = cc.id
LEFT JOIN adtech.sdk_packages AS sp
    ON
        c.id = sp.company_id
        OR cc.id = sp.company_id
LEFT JOIN adtech.sdk_paths AS sp2
    ON
        c.id = sp2.company_id
        OR cc.id = sp2.company_id
WHERE
    c.name = :company
    OR cc.name = :company;
