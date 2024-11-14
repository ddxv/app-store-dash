SELECT
    c.name AS company_name,
    ad.domain AS company_domain
FROM
    adtech.sdk_packages AS sp
LEFT JOIN adtech.companies AS c
    ON
        sp.company_id = c.id
LEFT JOIN adtech.company_domain_mapping AS cdm
    ON
        c.id = cdm.company_id
LEFT JOIN ad_domains AS ad
    ON
        cdm.domain_id = ad.id
WHERE
    sp.package_pattern LIKE :value_pattern || '%';
