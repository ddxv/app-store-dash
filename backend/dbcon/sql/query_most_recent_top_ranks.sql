SELECT
                ar.rank,
                sa.name,
                sa.store_id,
                sa.icon_url_512
            FROM
                app_rankings ar
            LEFT JOIN
                stores s
                    ON s.id = ar.store
            LEFT JOIN
                store_apps sa ON sa.id = ar.store_app
            WHERE
                crawled_date = (SELECT max(crawled_date) FROM app_rankings WHERE store=:store)
                AND ar.store = :store
                AND ar.store_collection = :collection_id
                AND ar.store_category = :category_id
            LIMIT :limit
            ;
