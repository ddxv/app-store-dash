SELECT
                        sa.*,
                        d.developer_id,
                        d.name as developer_name,
                        pd.url as developer_url
                    FROM store_apps sa
                    LEFT JOIN developers d
                        ON d.id = sa.developer
                    LEFT JOIN app_urls_map aum
                        ON aum.store_app = sa.id
                    LEFT JOIN pub_domains pd
                        ON pd.id = aum.pub_domain
		WHERE store_id = :store_id
                    ;
