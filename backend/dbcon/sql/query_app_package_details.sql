WITH my_app AS (
    SELECT id
    FROM
        store_apps
    WHERE
        store_id = :store_id
),

latest_version_code AS (
    SELECT
        vc.store_app,
        MAX(vc.version_code) AS max_version_code
    FROM
        version_codes AS vc
    INNER JOIN my_app AS app
        ON
            vc.store_app = app.id
    GROUP BY
        vc.store_app
),

company_categories AS (
    SELECT
        c.id AS company_id,
        STRING_AGG(
            cat.name,
            ', '
        ) AS category_names
    FROM
        adtech.companies AS c
    LEFT JOIN adtech.company_categories AS ccat
        ON
            c.id = ccat.company_id
    LEFT JOIN adtech.categories AS cat
        ON
            ccat.category_id = cat.id
    GROUP BY
        c.id
)

SELECT
    vc.store_app,
    vd.xml_path,
    vd.tag,
    vd.android_name,
    c.name AS company_name,
    cc.category_names
FROM
    version_details AS vd
LEFT JOIN version_codes AS vc
    ON
        vd.version_code = vc.id
INNER JOIN latest_version_code AS lvc
    ON
        vc.version_code = lvc.max_version_code
        AND vc.store_app = lvc.store_app
LEFT JOIN adtech.sdk_packages AS tm
    ON
        vd.android_name ILIKE tm.package_pattern || '%'
LEFT JOIN adtech.companies AS c
    ON
        tm.company_id = c.id
LEFT JOIN company_categories AS cc
    ON
        c.id = cc.company_id
ORDER BY
    vc.store_app,
    vd.xml_path,
    vd.android_name;
