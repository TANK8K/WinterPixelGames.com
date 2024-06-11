import psycopg
import time
import streamlit as st
import flag
import re
from datetime import datetime
from pages.GooberDash.Backend.fetch_full_time_trials_leaderboard import (
    fetch_leaderboard,
    list_levels,
)


def update_leaderboard():
    while True:
        try:
            connection = psycopg.connect(**st.secrets.sql_credentials)

            with connection as conn:
                # Replace previous version with current version
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        TRUNCATE TABLE goober_dash_time_trials_leaderboard_prev;
                    """
                    )
                    cur.execute(
                        """
                        INSERT INTO goober_dash_time_trials_leaderboard_prev
                        SELECT * FROM goober_dash_time_trials_leaderboard;
                    """
                    )
                conn.commit()

                # Replace previous version with current version
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        TRUNCATE TABLE goober_dash_time_trials_records_prev;
                    """
                    )
                    cur.execute(
                        """
                        INSERT INTO goober_dash_time_trials_records_prev
                        SELECT * FROM goober_dash_time_trials_records;
                    """
                    )
                conn.commit()

                count = 0
                global level_ids
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
                                f"{flag.flag(re.search(r'\"country\":\s*\"(.*?)\"', entry["metadata"]).group(1))} {entry["username"]["value"]}",  # flag and username
                                entry["rank"],
                                0,  # rank_out_of
                                0,  # percentile
                                0,  # point
                                round(entry["score"] / 100000, 3),  # time
                                datetime.fromtimestamp(
                                    entry["update_time"]["seconds"]
                                ).strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                ),  # upload_time
                            )
                        )

                    # Table 'goober_dash_time_trials_records'
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

                    time.sleep(3)

                with conn.cursor() as cur:
                    # Table 'goober_dash_time_trials_records'
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
                    cur.execute(
                        """UPDATE goober_dash_time_trials_records SET rank = rank_eq"""
                    )

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

                    # Change player to have the most recent username for all records of the player
                    cur.execute(
                        """
                            WITH latest_usernames AS (
                                SELECT DISTINCT ON (user_id) 
                                    user_id, 
                                    username 
                                FROM goober_dash_time_trials_records 
                                ORDER BY user_id, upload_time DESC
                            )
                            UPDATE goober_dash_time_trials_records AS r
                            SET username = lu.username
                            FROM latest_usernames AS lu
                            WHERE r.user_id = lu.user_id;
                            """
                    )
                    conn.commit()

                    # Table 'goober_dash_time_trials_leaderboard'
                    # Calculate and rank by points
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

                    # Calculate number of 1st, 2nd, 3rd
                    cur.execute(
                        """
                            UPDATE goober_dash_time_trials_leaderboard AS ldb
                            SET 
                                first = COALESCE(ranks.first_place_count, 0),
                                second = COALESCE(ranks.second_place_count, 0),
                                third = COALESCE(ranks.third_place_count, 0)
                            FROM (
                                SELECT
                                    user_id,
                                    COUNT(*) FILTER (WHERE rank = 1) AS first_place_count,
                                    COUNT(*) FILTER (WHERE rank = 2) AS second_place_count,
                                    COUNT(*) FILTER (WHERE rank = 3) AS third_place_count
                                FROM
                                    goober_dash_time_trials_records
                                GROUP BY
                                    user_id
                            ) AS ranks
                            WHERE
                                ldb.user_id = ranks.user_id;
                            """
                    )

                    # Calculate local_rank and local_top_%
                    cur.execute(
                        """
                    WITH ExtractedFlags AS (
                        SELECT
                            user_id,
                            username,
                            total_points,
                            count,
                            rank,
                            top_percentile,
                            first,
                            second,
                            third,
                            LEFT(username, 2) AS country_flag
                        FROM
                            goober_dash_time_trials_leaderboard
                    ),
                    RankedLocal AS (
                        SELECT
                            user_id,
                            username,
                            total_points,
                            count,
                            rank,
                            top_percentile,
                            first,
                            second,
                            third,
                            country_flag,
                            RANK() OVER (PARTITION BY country_flag ORDER BY total_points DESC) AS rank_local,
                            ROUND(CAST(PERCENT_RANK() OVER (PARTITION BY country_flag ORDER BY total_points DESC) * 100 AS numeric), 2) AS top_percentile_local
                        FROM
                            ExtractedFlags
                    )
                    UPDATE goober_dash_time_trials_leaderboard ldb
                    SET 
                        rank_local = rnk.rank_local,
                        top_percentile_local = rnk.top_percentile_local
                    FROM
                        RankedLocal rnk
                    WHERE
                        ldb.user_id = rnk.user_id;
                    """
                    )

                    conn.commit()

            with open("../storage/last_update.txt", "w") as f:
                f.write(str(time.time()))

            with open("../storage/level_counts.txt", "w") as f:
                f.write(str(len(level_ids)))

            time.sleep(43200)
        except psycopg.OperationalError as e:
            print("Error:", e)
            connection = psycopg.connect(**st.secrets.sql_credentials)
        finally:
            connection.close()
