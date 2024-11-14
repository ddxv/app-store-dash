SELECT *
FROM (
    SELECT
        *,
        ROW_NUMBER()
            OVER (PARTITION BY store ORDER BY app_count DESC)
        AS row_num
    FROM companies_version_details_count
) AS ranked
WHERE row_num <= 100
ORDER BY store ASC, app_count DESC;
