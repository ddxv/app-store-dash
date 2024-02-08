SELECT
    sa.*,
    d.name AS developer_name,
    pd.url AS developer_url,
    d.store AS developer_store
FROM
    app_urls_map AS aum
LEFT JOIN pub_domains AS pd
    ON
        aum.pub_domain = pd.id
LEFT JOIN store_apps AS sa
    ON
        aum.store_app = sa.id
LEFT JOIN developers AS d
    ON
        sa.developer = d.id
WHERE
    d.developer_id = :developer_id;
