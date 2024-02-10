-- noqa: disable=LT02
-- noqa: disable=LT08
-- noqa: disable=RF02
-- noqa: disable=PRS
-- SQLFluff currently unable to parse the double @ below
-- https://github.com/sqlfluff/sqlfluff/issues/4837
WITH devs AS (
    SELECT d.id AS developer_id
    FROM
        developers AS d
    WHERE
        to_tsvector(
            'simple',
            d.name
        ) @@ to_tsquery(
            'simple',
            :searchinput
        )
    ),
apps AS (
    SELECT ssa.id AS app_id
    FROM
        store_apps AS ssa
    WHERE
        to_tsvector(
            'simple',
            ssa.name
        ) @@ to_tsquery(
            'simple',
            :searchinput
        )
)
SELECT *
FROM
    store_apps AS sa
FULL OUTER JOIN devs ON
    sa.developer = devs.developer_id
FULL OUTER JOIN apps ON
    sa.id = apps.app_id
WHERE
    apps.app_id IS NOT NULL
OR devs.developer_id IS NOT NULL
ORDER BY
    sa.installs DESC NULLS LAST,
    sa.rating_count DESC NULLS LAST
LIMIT :mylimit;
