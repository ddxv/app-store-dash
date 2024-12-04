SELECT
    store_id, store_last_updated
FROM
    store_apps sa
WHERE
    crawl_result = 1
    AND installs > 1000
    OR rating_count > 100
ORDER BY
    GREATEST(
    COALESCE(
            installs,
            0
        ),
    COALESCE(
            CAST(
                rating_count AS bigint
            ),
            0
        )* 50
    ) DESC;
