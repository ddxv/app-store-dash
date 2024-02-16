WITH latest_version_codes AS (
    SELECT
        vc.store_app,
        MAX(vc.version_code) AS max_version_code
    FROM
        version_codes AS vc
    GROUP BY
        vc.store_app
)

SELECT
    vd.*,
    vc.store_app,
    sa.store_id,
    t.name AS tracker_name,
    n.name AS network_name
FROM
    version_details AS vd
LEFT JOIN
    version_codes AS vc
    ON
        vd.version_code = vc.id
LEFT JOIN network_package_map AS tm
    ON
        vd.android_name ~* tm.package_pattern::TEXT
LEFT JOIN tracker_package_map AS tr
    ON
        vd.android_name ~* tr.package_pattern::TEXT
LEFT JOIN trackers AS t
    ON
        tr.tracker = t.id
LEFT JOIN networks AS n
    ON
        tm.network = n.id
INNER JOIN
    latest_version_codes AS lvc
    ON
        vc.store_app = lvc.store_app
        AND vc.version_code = lvc.max_version_code
LEFT JOIN store_apps AS sa
    ON
        vc.store_app = sa.id
WHERE
    vd.android_name != ''
    AND
    sa.store_id = :store_id
ORDER BY
    vc.store_app,
    vd.xml_path,
    vd.android_name
