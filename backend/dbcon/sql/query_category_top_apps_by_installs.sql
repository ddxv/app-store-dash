SELECT * 
            FROM 
                top_categories
            WHERE 
                mapped_category = :category
            LIMIT :limit
            ;
