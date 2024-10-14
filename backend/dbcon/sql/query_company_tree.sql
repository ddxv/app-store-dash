WITH mytree AS (
    SELECT
        c.name AS company_name,
        ad.domain AS company_domain,
        COALESCE(
            parad.domain,
            ad.domain
        ) AS parent_company_domain,
        COALESCE(
            cc.name,
            c.name,
            ad.domain
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
    FULL OUTER JOIN ad_domains AS ad
        ON
            cdm.domain_id = ad.id
    LEFT JOIN ad_domains AS parad
        ON
            pcdm.domain_id = parad.id
)

SELECT *
FROM
    mytree
WHERE
    company_domain = :company_domain
    OR parent_company_domain = :company_domain;
