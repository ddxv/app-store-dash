WITH devs AS (
                    SELECT
                        d.id AS developer_id
                    FROM
                        developers d
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
                    SELECT
                        ssa.id AS app_id
                    FROM
                        store_apps ssa
                    WHERE
                        to_tsvector(
                            'simple',
                            ssa.name
                        ) @@ to_tsquery(
                            'simple',
                            :searchinput
                        )
                )
                SELECT
                    *
                FROM
                    store_apps sa
                FULL OUTER JOIN devs ON
                    sa.developer = devs.developer_id
                FULL OUTER JOIN apps ON
                    sa.id = apps.app_id
                WHERE
                    apps.app_id IS NOT NULL
                    OR devs.developer_id IS NOT NULL
                ORDER BY
                    installs DESC NULLS LAST,
                    rating_count DESC NULLS LAST
                LIMIT :limit
                ;

