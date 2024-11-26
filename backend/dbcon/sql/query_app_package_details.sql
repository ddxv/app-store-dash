SELECT
    cavd.xml_path,
    cavd.tag,
    cavd.value_name,
    cavd.company_name,
    cavd.company_domain,
    cavd.category_slug
FROM
    companies_apps_version_details AS cavd
WHERE
    cavd.store_id = :store_id
ORDER BY cavd.xml_path, cavd.value_name;
