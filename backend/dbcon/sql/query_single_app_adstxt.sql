SELECT
    company_name,
    ad_domain_url,
    publisher_id,
    relationship,
    developer_domain_crawled_at
FROM adstxt_entries_store_apps
WHERE store_id = :store_id;
