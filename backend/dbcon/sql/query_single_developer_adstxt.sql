WITH parent_companies AS (
    SELECT
        c.id AS company_id,
        c.name AS company_name,
        COALESCE(c.parent_company_id, c.id) AS parent_company_id,
        COALESCE(pc.name, c.name) AS parent_company_name
    FROM adtech.companies AS c
    LEFT JOIN adtech.companies AS pc ON c.parent_company_id = pc.id
)

SELECT DISTINCT
    myc.parent_company_name AS company_name,
    aav.ad_domain,
    aav.ad_domain_url,
    aav.publisher_id,
    aav.relationship,
    aav.crawl_result,
    aav.developer_domain_crawled_at
FROM app_ads_view AS aav
LEFT JOIN pub_domains AS pd
    ON aav.developer_domain_url = pd.url
LEFT JOIN app_urls_map AS aum
    ON pd.id = aum.pub_domain
LEFT JOIN store_apps AS sa
    ON aum.store_app = sa.id
LEFT JOIN developers AS d
    ON sa.developer = d.id
LEFT JOIN adtech.company_domain_mapping AS cdm ON aav.ad_domain = cdm.domain_id
LEFT JOIN parent_companies AS myc
    ON cdm.company_id = myc.company_id
WHERE sa.store_id = :store_id;
