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
LEFT JOIN adtech.company_domain_mapping AS cdm
    ON
        c.id = cdm.company_id
LEFT JOIN adtech.company_domain_mapping AS pcdm
    ON
        cc.id = pcdm.company_id
LEFT JOIN ad_domains AS ad
    ON
        cdm.domain_id = ad.id
LEFT JOIN ad_domains AS parad
    ON
        pcdm.domain_id = parad.id
LEFT JOIN adtech.sdk_packages AS sp
    ON
        c.id = sp.company_id
        -- OR cc.id = sp.company_id
LEFT JOIN adtech.sdk_paths AS sp2
    ON
        c.id = sp2.company_id
        OR cc.id = sp2.company_id
WHERE
    ad.domain = :company_domain
    OR parad.domain = :company_domain
