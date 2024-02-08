SELECT
            arr.crawled_date,
            arr.rank,
            sa.name,
            sa.store_id
            FROM
                app_rankings arr
            LEFT JOIN
                store_apps sa ON sa.id = arr.store_app
            WHERE
                arr.store_app IN (
                    SELECT
                        ar.store_app
                    FROM
                        app_rankings ar
                    WHERE
                        ar.crawled_date = (SELECT max(crawled_date) FROM app_rankings WHERE store=:store)
                        AND ar.store = :store
                        AND ar.store_collection = :collection_id
                        AND ar.store_category = :category_id
                    LIMIT :limit
                    )
            AND arr.crawled_date >= :start_date
            AND arr.store = :store
            AND arr.store_collection = :collection_id
            AND arr.store_category = :category_id
            ;
