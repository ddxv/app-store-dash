SELECT
    sa.*,
    d.developer_id,
    d.name AS developer_name,
    pd.url AS developer_url
FROM store_apps AS sa
LEFT JOIN developers AS d
    ON sa.developer = d.id
LEFT JOIN app_urls_map AS aum
    ON sa.id = aum.store_app
LEFT JOIN pub_domains AS pd
    ON aum.pub_domain = pd.id
WHERE sa.store_id = :store_id;
