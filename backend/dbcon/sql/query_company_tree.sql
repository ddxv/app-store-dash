SELECT
    c.name AS company_name,
    ad."domain",
    COALESCE(
        cc.name,
        c.name,
        ad."domain"
    ) AS parent_company_name
FROM
    adtech.companies AS c
LEFT JOIN adtech.companies AS cc
    ON
        c.parent_company_id = cc.id
LEFT JOIN adtech.company_domain_mapping AS cdm
    ON
        c.id = cdm.company_id
FULL OUTER JOIN ad_domains AS ad
    ON
        cdm.domain_id = ad.id
WHERE
    c.name = :company
    OR cc.name = :company
    OR ad.domain ILIKE :company || '%';
