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
    level_ids = list_levels()
    # level_ids = {"01194f86-c8e3-4d8f-af7b-9f16cc08531d": "dummy level name"}

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
                    0,  # point
                    round(entry["score"] / 100000, 3),  # time
                    datetime.fromtimestamp(entry["update_time"]["seconds"]).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),  # upload_time
                )
            )

        # Fetch records
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO leaderboard (
                    level_id, level_name, user_id, username, rank, point, time, upload_time
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (level_id, user_id) DO UPDATE SET
                    level_name = EXCLUDED.level_name,
                    username = EXCLUDED.username,
                    rank = EXCLUDED.rank,
                    point = EXCLUDED.point,
                    time = EXCLUDED.time,
                    upload_time = EXCLUDED.upload_time
                """,
                data_to_insert,
            )

        conn.commit()

    with conn.cursor() as cur:
        # Add rank_eq column temporarily
        cur.execute("""ALTER TABLE leaderboard ADD COLUMN rank_eq INTEGER""")

        # Caclulate the rank_eq column
        cur.execute(
            """
            WITH ranked AS (
            SELECT level_id, user_id, time,
                   RANK() OVER (PARTITION BY level_id ORDER BY time) as rank
            FROM leaderboard
            )
            UPDATE leaderboard
            SET rank_eq = ranked.rank
            FROM ranked
            WHERE leaderboard.level_id = ranked.level_id
            AND leaderboard.user_id = ranked.user_id
            AND leaderboard.time = ranked.time 
        """
        )

        # Replace rank column with rank_eq column
        cur.execute("""UPDATE leaderboard SET rank = rank_eq""")

        # Remove rank_eq column
        cur.execute("""ALTER TABLE leaderboard DROP COLUMN rank_eq""")

        # Calculate points based on rank_eq
        cur.execute(
            """
            UPDATE leaderboard
            SET point = CASE
                WHEN rank BETWEEN 1 AND 10 THEN FLOOR(10000 / rank)
                ELSE FLOOR((1000 / POWER(2, CEIL(LOG(10, rank) - 1)))
                    * (POWER(10, CEIL(LOG(10, rank)) - 1) / rank + 0.9))
                END
        """
        )

        conn.commit()

    conn.close()
