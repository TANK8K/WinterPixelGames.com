import psycopg
import streamlit as st
from datetime import datetime
from pages.GooberDash.Backend.fetch_full_time_trials_leaderboard import (
    fetch_leaderboard,
    list_levels,
)

connection = psycopg.connect(**st.secrets.sql_credentials)

with connection as conn:
    count = 0
    # level_ids = list_levels()
    level_ids = {"01194f86-c8e3-4d8f-af7b-9f16cc08531d": "dummy level name"}

    for count, level_id in enumerate(level_ids):
        print(count, level_id)

        data = fetch_leaderboard(level_id)

        data_to_insert = []
        for entry in data:
            data_to_insert.append(
                (
                    entry["leaderboard_id"].split(".")[-1],  # level_id
                    level_ids[level_id],  # level_name
                    entry["owner_id"],  # user_id
                    entry["username"]["value"],  # username
                    entry["rank"],
                    0,  # rank_out_of
                    0,  # percentile
                    0,  # point
                    round(entry["score"] / 100000, 3),  # time
                    datetime.fromtimestamp(entry["update_time"]["seconds"]).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),  # upload_time
                )
            )

        # Fetch records from each level
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO goober_dash_time_trials_records (
                    level_id, level_name, user_id, username, rank, rank_out_of, percentile, point, time, upload_time
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (level_id, user_id) DO UPDATE SET
                    level_name = EXCLUDED.level_name,
                    username = EXCLUDED.username,
                    rank = EXCLUDED.rank,
                    rank_out_of = EXCLUDED.rank_out_of,
                    percentile = EXCLUDED.percentile,
                    point = EXCLUDED.point,
                    time = EXCLUDED.time,
                    upload_time = EXCLUDED.upload_time
                """,
                data_to_insert,
            )

        conn.commit()

    with conn.cursor() as cur:
        # Add 'rank_eq' temporarily
        cur.execute(
            """ALTER TABLE goober_dash_time_trials_records ADD COLUMN rank_eq INTEGER"""
        )

        # Caclulate the 'rank_eq'
        cur.execute(
            """
            WITH ranked AS (
            SELECT level_id, user_id, time,
                   RANK() OVER (PARTITION BY level_id ORDER BY time) as rank
            FROM goober_dash_time_trials_records
            )
            UPDATE goober_dash_time_trials_records
            SET rank_eq = ranked.rank
            FROM ranked
            WHERE goober_dash_time_trials_records.level_id = ranked.level_id
            AND goober_dash_time_trials_records.user_id = ranked.user_id
            AND goober_dash_time_trials_records.time = ranked.time 
        """
        )

        # Replace 'rank' with 'rank_eq'
        cur.execute("""UPDATE goober_dash_time_trials_records SET rank = rank_eq""")

        # Remove 'rank_eq'
        cur.execute(
            """ALTER TABLE goober_dash_time_trials_records DROP COLUMN rank_eq"""
        )

        # Calculate 'points' based on 'rank_eq'
        cur.execute(
            """
            UPDATE goober_dash_time_trials_records
            SET point = CASE
                WHEN rank BETWEEN 1 AND 10 THEN FLOOR(10000 / rank)
                ELSE FLOOR((1000 / POWER(2, CEIL(LOG(10, rank) - 1)))
                    * (POWER(10, CEIL(LOG(10, rank)) - 1) / rank + 0.9))
                END
        """
        )

        # Caculate 'rank_out_of'
        cur.execute(
            """
            WITH user_counts AS (
                SELECT level_id, COUNT(user_id) AS user_count
                FROM goober_dash_time_trials_records
                GROUP BY level_id
            )
            UPDATE goober_dash_time_trials_records l
            SET rank_out_of = uc.user_count
            FROM user_counts uc
            WHERE l.level_id = uc.level_id;
            """
        )

        # Calculate 'percentile'
        cur.execute(
            """
            UPDATE goober_dash_time_trials_records
            SET percentile = ROUND(100 * (1 - (rank - 1)::float / rank_out_of)::numeric, 2)
            WHERE rank_out_of > 0;
        """
        )

        # Calculate and Update table 'goober_dash_time_trials_leaderboard'
        cur.execute(
            """
            INSERT INTO goober_dash_time_trials_leaderboard (user_id, username, total_points, count, rank, top_percentile)
            SELECT
                user_id,
                username,
                SUM(point) AS total_points,
                COUNT(*) AS count,
                RANK() OVER (ORDER BY SUM(point) DESC) AS rank,
                ROUND((CAST(PERCENT_RANK() OVER (ORDER BY SUM(point) DESC) * 100 AS numeric)), 2) AS top_percentile
            FROM
                goober_dash_time_trials_records
            GROUP BY
                user_id, username
            ORDER BY
                total_points DESC
            ON CONFLICT (user_id) DO UPDATE
            SET
                username = EXCLUDED.username,
                total_points = EXCLUDED.total_points,
                count = EXCLUDED.count,
                rank = EXCLUDED.rank,
                top_percentile = EXCLUDED.top_percentile;
        """
        )

        conn.commit()
