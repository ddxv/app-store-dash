SELECT
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
WHERE sa.store_id = :store_id;
