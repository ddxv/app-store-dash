SELECT
	store,
	tag_source,
	company_domain,
	company_name,
    'all' AS app_category,
	type_url_slug,
	sum(app_count) AS app_count
FROM
	adtech.companies_categories_types_app_counts ccac
WHERE
    type_url_slug = :type_slug
GROUP BY
	store,
	tag_source,
	company_domain,
	company_name,
	type_url_slug;
;