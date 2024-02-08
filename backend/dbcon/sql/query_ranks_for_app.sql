SELECT
                    ar.crawled_date,
                    ar.country,
                    ar.store,
                    ar.rank,
                    scol.collection,
                    scat.category
                FROM
                    app_rankings ar
                LEFT JOIN
                    store_apps sa
                    ON sa.id = ar.store_app
                LEFT JOIN store_collections scol
                    ON scol.id = ar.store_collection
                LEFT JOIN store_categories scat
                    ON scat.id = ar.store_category
                WHERE
                    sa.store_id = :store_id
                    AND
                        crawled_date >= :start_date
                ;
