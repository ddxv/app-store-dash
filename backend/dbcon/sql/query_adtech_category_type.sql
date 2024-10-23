SELECT
	*
FROM
	adtech.companies_categories_types_app_counts cctac
WHERE
	type_url_slug = :type_slug
ORDER BY
	app_count DESC;
