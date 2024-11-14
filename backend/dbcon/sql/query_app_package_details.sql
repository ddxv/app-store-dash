SELECT
    cavd.xml_path,
    cavd.tag,
    cavd.value_name,
    cavd.company_name,
    cavd.company_domain,
    cavd.category_name
FROM
    companies_apps_version_details AS cavd
LEFT JOIN store_apps AS sa
    ON
        cavd.store_app = sa.id
WHERE
    sa.store_id = :store_id
ORDER BY cavd.xml_path, cavd.value_name;
