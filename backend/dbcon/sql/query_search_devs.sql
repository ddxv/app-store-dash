-- noqa: disable=LT02
-- noqa: disable=LT08
-- noqa: disable=RF02
-- noqa: disable=PRS
-- SQLFluff currently unable to parse the double @ below
-- https://github.com/sqlfluff/sqlfluff/issues/4837
WITH devs AS (
    SELECT sa.* FROM store_apps AS sa
    LEFT JOIN developers AS d ON sa.developer = d.id
    WHERE
       d.textsearchable_index_col @@ to_tsquery(
            'simple',
            :searchinput
        )
    )
SELECT * FROM devs
ORDER BY
    installs DESC NULLS LAST,
    rating_count DESC NULLS LAST
LIMIT :mylimit;
