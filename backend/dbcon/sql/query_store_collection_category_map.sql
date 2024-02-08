SELECT
                DISTINCT 
                ar.store as store_id,
                s.name as store_name,
                store_collection as collection_id,
                collection as collection_name,
                store_category as category_id,
                category as category_name
            FROM
                app_rankings ar
            LEFT JOIN
                stores s
                    ON s.id = ar.store
            LEFT JOIN 
                store_collections scol
                    ON scol.id = ar.store_collection AND ar.store = scol.store
            LEFT JOIN
                store_categories scat
                    ON scat.id = ar.store_category AND ar.store = scat.store
            WHERE
                crawled_date = CURRENT_DATE - INTERVAL '1 day';
