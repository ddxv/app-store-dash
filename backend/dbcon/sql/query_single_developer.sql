SELECT
                        d.name AS developer_name,
                        pd.url as developer_url,
                        d.store as developer_store,
                        sa.*
                    FROM
                        app_urls_map aum
                    LEFT JOIN pub_domains pd ON
                        pd.id = aum.pub_domain
                    LEFT JOIN store_apps sa ON
                        sa.id = aum.store_app
                    LEFT JOIN developers d ON
                        d.id = sa.developer
                    WHERE
                        d.developer_id = :developer_id;
