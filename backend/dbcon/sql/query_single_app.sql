SELECT
    id,
    name,
    store_id,
    store,
    category,
    rating,
    rating_count,
    review_count,
    installs,
    store_last_updated,
    created_at,
    updated_at,
    crawl_result,
    icon_url_512,
    release_date,
    featured_image_url,
    phone_image_url_1,
    phone_image_url_2,
    phone_image_url_3,
    tablet_image_url_1,
    tablet_image_url_2,
    tablet_image_url_3,
    developer_id,
    developer_name,
    developer_url,
    adstxt_last_crawled,
    adstxt_crawl_result,
    version_code,
    sdk_last_crawled,
    sdk_crawl_result
FROM
    store_apps_overview
WHERE
    store_id = :store_id;
