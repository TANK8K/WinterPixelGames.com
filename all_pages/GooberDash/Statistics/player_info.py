import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import time
import datetime
import timeago
import os
import re
import flag
import json
from math import floor, ceil, log10, isnan
from all_pages.GooberDash.Backend.get_user import user_info, user_info_2
from all_pages.GooberDash.Backend.season import (
    current_season,
    season_info,
    season_leaderboard,
)
from all_pages.GooberDash.Backend.get_config import get_config
from all_pages.GooberDash.Backend.goober_generator import generate_goober
from common_config import set_localization
from country_or_region import country_region

conn = st.connection("postgresql", type="sql")

goober_dash_config = get_config()


# @st.cache_data(show_spinner=True, ttl=21600)
def query_df_user(user):
    df_user_records = conn.query(
        f"""
        SELECT username, user_id
        FROM goober_dash_time_trials_leaderboard
        WHERE user_id='{user}' OR username ILIKE '%{user}%'
    """
    )
    return df_user_records


# @st.cache_data(show_spinner=True, ttl=21600)
def query_df_user_records(user_id):
    df_user_records = conn.query(
        f"""
        SELECT *
        FROM goober_dash_time_trials_records
        WHERE user_id='{user_id}'
        ORDER BY rank, upload_time DESC;
    """
    )
    return df_user_records


# @st.cache_data(show_spinner=True, ttl=21600)
def query_df_user_leaderboard(user_id):
    df_user_leaderboard = conn.query(
        f"""
        SELECT *
        FROM goober_dash_time_trials_leaderboard
        WHERE user_id='{user_id}'
    """
    )
    return df_user_leaderboard


# @st.cache_data(show_spinner=True, ttl=21600)
def query_df_level_ids():
    df_level_ids = conn.query(
        """
        SELECT DISTINCT level_id, level_name, rank_out_of
        FROM goober_dash_time_trials_records;
        """
    )
    return df_level_ids


def load_page(selected_language):
    _ = set_localization(selected_language)
    try:
        with open("../storage/last_update.txt", "r") as f:
            last_update = float(f.readline())

        with open("../storage/level_counts.txt", "r") as f:
            level_counts = int(f.readline())

        st.image(
            "static/GooberDash/goober_dash_logo_text.png",
            width=280,
        )
        st.html(
            '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-user" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
            + _("Player Info")
            + "<span>"
        )
        st.html(
            """
            <style>
            table * {
                border: none !important;
            }
            table {
                font-size: 1.3rem;
                margin-top: 10px;
                position: relative;
                top: -20px;
            }
            table td {
                padding: 0 5vw 0 0 !important;
            }
            table a {
                color: rgb(46, 154, 255) !important;
            }
            table td:first-child {
                padding-right: 5vw;
                display: inline-block;
            }
            table td img {
                width: 80px !important;
            }
            </style>
        """
        )
        user_columns = st.columns((5, 1, 5))

        with user_columns[0]:
            user = st.text_input(
                "**" + _("Search Player") + "**",
                placeholder=_("Username or User ID"),
                value=None,
            )

        if user in [None, ""]:
            user_id = None
        else:
            users_found_database = query_df_user(user)
            try:
                username_of_users_found_database = users_found_database.loc[
                    0, "username"
                ][3:]
            except KeyError:
                st.error("❌ " + _("No Players Found"))
                user_id = None
            users_found_database.rename(
                columns={
                    "username": "Player",
                    "user_id": "User ID",
                },
                inplace=True,
            )

            try:
                try:
                    user_info_2_res = user_info_2(user)["users"][0]
                except KeyError:
                    user_info_2_res = user_info_2(username_of_users_found_database)[
                        "users"
                    ][0]
                user_info_2_res_user_id = user_info_2_res["id"]
                user_info_2_res_username = user_info_2_res["username"]
                search_player_not_in_database = (
                    user_info_2_res_user_id
                    not in users_found_database["User ID"].tolist()
                )
                if search_player_not_in_database:
                    new_row = {
                        "Player": user_info_2_res_username,
                        "User ID": user_info_2_res_user_id,
                    }
                    users_found_combined = pd.concat(
                        [pd.DataFrame([new_row]), users_found_database],
                        ignore_index=True,
                    )
                else:
                    row_index = users_found_database.index[
                        users_found_database["User ID"] == user_info_2_res_user_id
                    ][0]
                    row_to_move = users_found_database.loc[[row_index]]
                    remaining_df = users_found_database.drop(index=row_index)
                    result_df = pd.concat(
                        [row_to_move, remaining_df], ignore_index=True
                    )
                    users_found_combined = result_df
            except KeyError:
                users_found_combined = users_found_database

            if len(users_found_combined) == 1:
                user_id = users_found_combined.iloc[0]["User ID"]
                player_name = users_found_combined.iloc[0]["Player"]

            elif len(users_found_combined) > 1:
                with user_columns[2]:
                    player_name = st.selectbox(
                        "**" + _("Select Player") + "**",
                        users_found_combined["Player"],
                        index=None,
                        placeholder=f"{len(users_found_combined)} "
                        + _("Players found"),
                    )
                    if player_name is not None:
                        user_id = users_found_combined.loc[
                            users_found_combined["Player"] == player_name, "User ID"
                        ].iloc[0]
                    else:
                        user_id = None
            else:
                st.error("❌ " + _("No Players Found"))
                user_id = None

        if user_id not in [None, ""]:
            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                [
                    "📓 **" + _("General Info") + "**",
                    "📊 **" + _("Season Records") + "**",
                    "🏅 **" + _("Awards") + "**",
                    "🗒️ **" + _("Stats") + "**",
                    "⏳ **" + _("Time Trials Records") + "**",
                ]
            )

            def remove_non_alphanumeric_keep_spaces(s):
                return re.sub(r"[^a-zA-Z0-9 ]", "", s)

            def contains_flag_emoji(s):
                flag_emoji_pattern = re.compile(r"[\U0001F1E6-\U0001F1FF]{2}")
                return bool(flag_emoji_pattern.search(s))

            with tab1:
                user_info_res = user_info(user_id)
                user_info_2_res = user_info_2(user_id)["users"][0]
                cosmetics_dict = user_info_res["skin"]
                user_username = user_info_2_res["username"]
                user_display_name = user_info_2_res["display_name"]
                user_create_time = datetime.datetime.strptime(
                    user_info_2_res["create_time"].translate(":-"), "%Y-%m-%dT%H:%M:%SZ"
                )
                user_level = user_info_res["level"]
                try:
                    user_online = user_info_2_res["online"]
                except KeyError:
                    user_online = False

                col1, col2 = st.columns((2, 1))
                with col1:
                    st.markdown(
                        """
                        |||
                        |---|---|
                        |**"""
                        + _("Username")
                        + f"""**|{user_username}|"""
                        + """|
                        |**"""
                        + _("Display Name")
                        + f"""**|{remove_non_alphanumeric_keep_spaces(user_display_name)}|"""
                        + """|
                        |**"""
                        + _("User ID")
                        + f"""**|`{user_id}`|"""
                        + """|
                        |**"""
                        + (
                            _("Country/Region")
                            + """**|"""
                            + country_region(selected_language, player_name.split()[0])
                            + """|
                        |**"""
                            if contains_flag_emoji(player_name)
                            else ""
                        )
                        + _("Create Time")
                        + f"""**|{user_create_time} UTC ({timeago.format(user_create_time, datetime.datetime.now())})|"""
                        + """|
                        |**"""
                        + _("Player Level")
                        + f"""**|{user_level}|"""
                        + """|
                        |**"""
                        + _("Online")
                        + """**|:"""
                        + ("green" if user_online else "red")
                        + f"""[{user_online}]|"""
                    )
                with col2:
                    goober_file_path = generate_goober(
                        cosmetics_dict["hat"],
                        cosmetics_dict["suit"],
                        cosmetics_dict["hand"],
                        cosmetics_dict["color"],
                    )
                    st.image(goober_file_path)
                    os.remove(goober_file_path)
            with tab2:
                season_cols = st.columns(6, vertical_alignment="center")
                current_season_get = current_season(time.time())
                with season_cols[0]:
                    target_season = st.number_input(
                        "**" + _("Season") + "**",
                        min_value=19,
                        max_value=current_season_get,
                        value=current_season_get,
                    )
                try:
                    target_player_season_global_record = season_leaderboard(
                        target_season,
                        "global",
                        1,
                        "",
                        user_id,
                    )["owner_records"][0]
                    player_country = json.loads(
                        target_player_season_global_record["metadata"]
                    )["country"]
                    target_player_season_local_record = season_leaderboard(
                        target_season,
                        f"country.{player_country}",
                        1,
                        "",
                        user_id,
                    )["owner_records"][0]

                    season_cols[1].metric(
                        "**" + _("Global Rank") + "**",
                        f"🌐 {target_player_season_global_record['rank']}",
                    )
                    season_cols[2].metric(
                        "**" + _("Local Rank") + "**",
                        f"{flag.flag(player_country)} {target_player_season_local_record['rank']}",
                    )
                    season_cols[3].metric(
                        "**" + _("Crowns") + "**",
                        f"👑 {target_player_season_global_record['score']}",
                    )
                    season_cols[4].metric(
                        "**" + _("Crown Rounds") + "**",
                        f"🏁 {target_player_season_global_record['num_score']}",
                    )
                    season_cols[5].metric(
                        "**" + _("Crowns/Crown Round") + "**",
                        f"✨ {int(target_player_season_global_record['score'])/int(target_player_season_global_record['num_score']):.2f}",
                    )
                except KeyError:
                    with season_cols[1]:
                        st.error("❌ " + _("No Records Found"))

                target_season_info = season_info(current_season_get, "long")
                st.markdown(
                    """
                    |||
                    |---|---|
                    |**"""
                    + _("Start")
                    + f"""**|{target_season_info[0]}|"""
                    + """|
                    |**"""
                    + _("End")
                    + f"""**|{target_season_info[1]}|"""
                    + """|
                    |**"""
                    + _("Duration")
                    + f"""**|{target_season_info[2]}|"""
                    + """|
                    |**"""
                    + _("Status")
                    + f"""**|{target_season_info[3]}|"""
                    + """|
                    |**"""
                    + _("Ends In")
                    + f"""**|{target_season_info[4]}|"""
                )

            with tab3:
                awards_config = goober_dash_config["awards"]["awards"]

                sorted_awards = sorted(
                    awards_config.items(), key=lambda item: item[1]["priority"]
                )
                sorted_award_names = [award[0] for award in sorted_awards]

                player_awards = user_info_res["awards"]

                awards_markdown = "|Award|Count|Name|Description|\n|---|---|---|---|"
                for award in sorted_award_names:
                    if award in player_awards:
                        awards_markdown += f"\n|![{award}](./app/static/GooberDash/awards/{awards_config[award]['icon']})|**x{player_awards[award]['count']}**|{awards_config[award]['name']}|{awards_config[award]['desc'].replace('.','')}|"
                st.write(awards_markdown)
            with tab4:
                stats = user_info_res["stats"]

                try:
                    games_played = stats["GamesPlayed"]
                except KeyError:
                    games_played = 0
                try:
                    games_won = stats["GamesWon"]
                except KeyError:
                    games_won = 0
                try:
                    deaths = stats["Deaths"]
                except KeyError:
                    deaths = 0
                try:
                    deaths_per_games_played = (
                        f"{stats['Deaths']/stats['GamesPlayed']:.2f}"
                    )
                except KeyError:
                    deaths_per_games_played = 0
                try:
                    longest_winstreak = stats["Winstreak"]
                except KeyError:
                    longest_winstreak = 0
                try:
                    current_winstreak = stats["CurrentWinstreak"]
                except KeyError:
                    current_winstreak = 0
                try:
                    winrate = f"{games_won/games_played*100:.2f}"
                except Exception:
                    winrate = 0

                first_cols = st.columns(4)
                first_cols[0].metric(
                    "**" + _("Games Played") + "**", f"🏁 {games_played}"
                )
                first_cols[1].metric("**" + _("Games Won") + "**", f"🥇 {games_won}")
                first_cols[2].metric(
                    "**" + _("Games Lost") + "**", f"😢 {games_played - games_won}"
                )
                first_cols[3].metric("**" + _("Winrate") + "**", f"✨ {winrate}%")

                second_cols = st.columns(4)
                second_cols[0].metric("**" + _("Deaths") + "**", f"💀 {deaths}")
                second_cols[1].metric(
                    "**" + _("Deaths/Games Played") + "**",
                    f"💀 {deaths_per_games_played}",
                )
                second_cols[2].metric(
                    "**" + _("Longest Winstreak") + "**", f"🔥 {longest_winstreak}"
                )
                second_cols[3].metric(
                    "**" + _("Current Winstreak") + "**", f"🔥 {current_winstreak}"
                )

                if games_played != 0:
                    pie_chart_init = {
                        "counts": [games_won, games_played - games_won],
                        "type": ["Won", "Lost"],
                    }
                    fig = px.pie(
                        pie_chart_init,
                        values=pie_chart_init["counts"],
                        names=pie_chart_init["type"],
                        hole=0.4,
                        color="type",
                        color_discrete_sequence=[
                            "#769655",
                            "#b43431",
                        ],
                    )
                    fig.update_traces(
                        textposition="inside",
                        textinfo="percent+label",
                        insidetextfont_color="white",
                        sort=False,
                    )
                    fig.update_layout(
                        annotations=[
                            {
                                "text": f"<span style='font-size: 16px; font-weight: bold; line-height: 1.5 !important;'>{games_played} "
                                + _("Games")
                                + f"<br><span style='color: #769655;'>{games_won} "
                                + _("Won")
                                + f"</span><br><span style='color: #b43431;'>{games_played-games_won} "
                                + _("Lost")
                                + "</span></span>",
                                "showarrow": False,
                            }
                        ],
                        uniformtext_minsize=16,
                        uniformtext_mode="hide",
                        showlegend=False,
                    )
                    st.plotly_chart(fig, use_container_width=True, on_select="ignore")
            with tab5:
                st.caption(
                    _("Last Update")
                    + f": {datetime.datetime.fromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S')} UTC ("
                    + _("Updated Every 12 Hours")
                    + ")"
                )

                user_leaderboard = query_df_user_leaderboard(user_id)

                metric_cols = st.columns((3, 3, 1, 1, 1, 1, 2, 2))

                try:
                    performance_points = user_leaderboard.loc[0, "total_points"]
                    global_rank = user_leaderboard.loc[0, "rank"]
                    top_percent = user_leaderboard.loc[0, "top_percentile"]
                    first = user_leaderboard.loc[0, "first"]
                    second = user_leaderboard.loc[0, "second"]
                    third = user_leaderboard.loc[0, "third"]
                    completed_levels = user_leaderboard.loc[0, "count"]
                    average_percentile = user_leaderboard.loc[0, "average_percentile"]

                    delta_performance_points = int(
                        user_leaderboard.loc[0, "total_points_diff"]
                    )
                    delta_global_rank = int(user_leaderboard.loc[0, "rank_diff"])
                    delta_first = int(user_leaderboard.loc[0, "first_diff"])
                    delta_second = int(user_leaderboard.loc[0, "second_diff"])
                    delta_third = int(user_leaderboard.loc[0, "third_diff"])
                    delta_completed_levels = int(user_leaderboard.loc[0, "count_diff"])
                    delta_average_percentile = float(
                        user_leaderboard.loc[0, "average_percentile_diff"]
                    )

                    if delta_performance_points != 0:
                        metric_cols[0].metric(
                            label="**" + _("Total Performance Points") + "**",
                            value=f"{performance_points} pp",
                            delta=f"{delta_performance_points} pp",
                        )
                    else:
                        metric_cols[0].metric(
                            label="**" + _("Total Performance Points") + "**",
                            value=f"{performance_points} pp",
                        )
                    if delta_global_rank != 0:
                        metric_cols[1].metric(
                            label="**" + _("Global Rank") + "**",
                            value=(
                                f"#{global_rank} "
                                + (
                                    "(" + _("Top ") + f"{top_percent:.2f}%)"
                                    if global_rank != 1
                                    else "(" + _("First") + ")"
                                )
                            ),
                            delta=delta_global_rank,
                            delta_color="inverse",
                        )
                    else:
                        metric_cols[1].metric(
                            label="**" + _("Global Rank") + "**",
                            value=(
                                f"#{global_rank} "
                                + (
                                    "(" + _("Top ") + f"{top_percent:.2f}%)"
                                    if global_rank != 1
                                    else "(" + _("First") + ")"
                                )
                            ),
                        )

                    if delta_first != 0:
                        metric_cols[3].metric(
                            label="🥇", value=f"{first}", delta=delta_first
                        )
                    else:
                        metric_cols[3].metric(label="🥇", value=f"{first}")

                    if delta_second != 0:
                        metric_cols[4].metric(
                            label="🥈", value=f"{second}", delta=delta_second
                        )
                    else:
                        metric_cols[4].metric(label="🥈", value=f"{second}")
                    if delta_third != 0:
                        metric_cols[5].metric(
                            label="🥉", value=f"{third}", delta=delta_third
                        )
                    else:
                        metric_cols[5].metric(label="🥉", value=f"{third}")
                    if delta_completed_levels != 0:
                        metric_cols[6].metric(
                            label="**" + _("Completed Levels") + "**",
                            value=f"{completed_levels}/{level_counts}",
                            delta=delta_completed_levels,
                        )
                    else:
                        metric_cols[6].metric(
                            label="**" + _("Completed Levels") + "**",
                            value=f"{completed_levels}/{level_counts}",
                        )
                    if delta_average_percentile != 0:
                        metric_cols[7].metric(
                            label="**" + _("Average Percentile") + "**",
                            value=f"{average_percentile}",
                            delta=delta_average_percentile,
                        )
                    else:
                        metric_cols[7].metric(
                            label="**" + _("Average Percentile") + "**",
                            value=f"{average_percentile}",
                        )

                    st.divider()

                    df_level_ids = query_df_level_ids()
                    df_user_records = query_df_user_records(user_id)
                    df_user_records.rename(
                        columns={
                            "level_name": "Level",
                            "level_id": "Level ID",
                            "username": "Player",
                            "user_id": "User ID",
                            "time": "Time",
                            "time_diff": "Time diff",
                            "upload_time": "Upload Time",
                            "point": "Performance Points",
                            "point_diff": "Performance Points diff",
                            "rank": "Rank",
                            "rank_diff": "Rank diff",
                            "rank_out_of": "Out of",
                            "rank_out_of_diff": "Out of diff",
                            "percentile": "Percentile",
                            "percentile_diff": "Percentile diff",
                        },
                        inplace=True,
                    )

                    if completed_levels != level_counts:
                        merged_df = pd.merge(
                            df_level_ids,
                            df_user_records,
                            left_on="level_id",
                            right_on="Level ID",
                            how="left",
                        )

                        missing_levels = merged_df[merged_df["Level ID"].isna()]
                        missing_levels = missing_levels[
                            ["level_name", "level_id", "rank_out_of"]
                        ].rename(
                            columns={
                                "level_name": "Level",
                                "level_id": "Level ID",
                                "rank_out_of": "Out of",
                            }
                        )
                        missing_levels["Time"] = None
                        missing_levels["Performance Points"] = None
                        missing_levels["Rank"] = None
                        missing_levels["Percentile"] = 0
                        missing_levels["Upload Time"] = None
                        missing_levels["Watch Replay"] = None
                        missing_levels["Race Ghost"] = None

                        missing_levels = missing_levels.dropna(how="all", axis=1)
                        if not missing_levels.empty:
                            df_user_records = pd.concat(
                                [df_user_records, missing_levels], ignore_index=True
                            )

                    df_user_records["Player"] = df_user_records["Player"].str.replace(
                        "-", "", regex=False
                    )

                    def format_time(x):
                        if pd.isnull(x):
                            return None
                        if isinstance(x, str) and x.endswith(" " + _("s")):
                            return x
                        if isinstance(x, float) and x.is_integer():
                            x = int(x)
                        return f"{x} " + _("s")

                    df_user_records["Time"] = df_user_records["Time"].apply(format_time)

                    def format_performance_points(x):
                        if pd.isnull(x):
                            return None
                        if isinstance(x, str) and x.endswith(" " + _("pp")):
                            return x
                        if isinstance(x, float) and x.is_integer():
                            x = int(x)
                        return f"{x} " + _("pp")

                    df_user_records["Performance Points"] = df_user_records[
                        "Performance Points"
                    ].apply(format_performance_points)

                    df_user_records["Upload Time"] = df_user_records[
                        "Upload Time"
                    ].astype(str)
                    if not df_user_records["Upload Time"].str.endswith(" UTC").all():
                        df_user_records["Upload Time"] = (
                            df_user_records["Upload Time"] + " UTC"
                        )

                    df_user_records["Upload Time"] = df_user_records[
                        "Upload Time"
                    ].replace("NaT UTC", None)

                    df_user_records["Watch Replay"] = (
                        "https://gooberdash.winterpixel.io/?play="
                        + df_user_records["Level ID"]
                        + "&replay="
                        + df_user_records["User ID"]
                    )
                    df_user_records["Race Ghost"] = (
                        "https://gooberdash.winterpixel.io/?play="
                        + df_user_records["Level ID"]
                        + "&ghost="
                        + df_user_records["User ID"]
                    )

                    def add_emojis(rank):
                        if pd.isna(rank):
                            return None
                        if isinstance(rank, str) and (
                            rank.startswith("🥇")
                            or rank.startswith("🥈")
                            or rank.startswith("🥉")
                            or rank.startswith("#")
                        ):
                            return rank
                        elif rank == 1:
                            return "🥇"
                        elif rank == 2:
                            return "🥈"
                        elif rank == 3:
                            return "🥉"
                        else:
                            return f"# {int(rank)}"

                    df_user_records["Rank"] = df_user_records["Rank"].apply(add_emojis)

                    checkboxes = st.columns(3)
                    with checkboxes[0]:
                        display_level_id = st.checkbox(
                            _("Display Level ID"),
                            value=False,
                            key="first_display_level_id",
                        )
                    with checkboxes[1]:
                        display_incompleted_levels = st.checkbox(
                            _("Display Incompleted Levels"),
                            value=False,
                        )
                    with checkboxes[2]:
                        display_changes = st.checkbox(
                            _("Display Changes"),
                            value=False,
                        )

                    column_order_config = [
                        "Level",
                        "Level ID",
                        "Time",
                        "Time diff",
                        "Performance Points",
                        "Performance Points diff",
                        "Rank",
                        "Rank diff",
                        "Out of",
                        "Out of diff",
                        "Percentile",
                        "Percentile diff",
                        "Upload Time",
                        "Watch Replay",
                        "Race Ghost",
                    ]
                    if not display_level_id:
                        column_order_config.remove("Level ID")
                    if completed_levels != level_counts:
                        if not display_incompleted_levels:
                            df_user_records = df_user_records[
                                df_user_records["Time"].notna()
                            ]
                    if not display_changes:
                        column_order_config = [
                            column
                            for column in column_order_config
                            if column
                            not in [
                                "Time diff",
                                "Performance Points diff",
                                "Rank diff",
                                "Out of diff",
                                "Percentile diff",
                            ]
                        ]

                    def _format_arrow(val, column_name):
                        if isinstance(val, (int, float)) and not np.isnan(val):
                            if column_name == "Time diff":
                                symbol = "▲" if val > 0 else "▼"
                                formatted_value = f"{abs(val):.2f}"
                                suffix = " " + _("s")
                                return f"{symbol} {formatted_value}{suffix}"
                            elif column_name == "Performance Points diff":
                                symbol = "▲" if val > 0 else "▼"
                                formatted_value = f"{int(abs(val))}"
                                suffix = " pp"
                                return f"{symbol} {formatted_value}{suffix}"
                            elif column_name == "Rank diff":
                                symbol = "▲" if val < 0 else "▼"
                                formatted_value = f"{int(abs(val))}"
                                suffix = ""
                                return f"{symbol} {formatted_value}{suffix}"
                            elif column_name == "Out of diff":
                                if val > 0:
                                    return f"(+ {int(val)})"
                                elif val < 0:
                                    return f"(- {abs(int(val))})"
                                else:
                                    return ""
                            elif column_name == "Percentile diff":
                                symbol = "▲" if val > 0 else "▼"
                                formatted_value = f"{abs(val):.2f}"
                                return f"{symbol} {formatted_value}"
                        elif pd.isna(val):
                            return ""
                        return val

                    def _color_arrow(val, column_name):
                        try:
                            if val is None:
                                return "color: transparent;"
                            elif column_name in [
                                "Performance Points diff",
                                "Percentile diff",
                            ]:
                                if val > 0:
                                    return "color: green;"
                                elif val < 0:
                                    return "color: red;"
                                else:
                                    return "color: transparent;"
                            elif column_name == "Out of diff":
                                if val > 0:
                                    return "color: white;"
                                else:
                                    return "color: transparent;"
                            elif column_name in ["Time diff", "Rank diff"]:
                                if val > 0:
                                    return "color: red;"
                                elif val < 0:
                                    return "color: green;"
                                else:
                                    return "color: transparent;"
                            else:
                                return None
                        except Exception:
                            return None

                    df_user_records = df_user_records.style
                    df_user_records = df_user_records.map(
                        lambda val: _color_arrow(val, "Time diff"), subset=["Time diff"]
                    )
                    df_user_records = df_user_records.map(
                        lambda val: _color_arrow(val, "Performance Points diff"),
                        subset=["Performance Points diff"],
                    )
                    df_user_records = df_user_records.map(
                        lambda val: _color_arrow(val, "Rank diff"), subset=["Rank diff"]
                    )
                    df_user_records = df_user_records.map(
                        lambda val: _color_arrow(val, "Out of diff"),
                        subset=["Out of diff"],
                    )
                    df_user_records = df_user_records.map(
                        lambda val: _color_arrow(val, "Percentile diff"),
                        subset=["Percentile diff"],
                    )

                    df_user_records = df_user_records.format(
                        {
                            "Time diff": lambda x: _format_arrow(x, "Time diff"),
                            "Performance Points diff": lambda x: _format_arrow(
                                x, "Performance Points diff"
                            ),
                            "Rank diff": lambda x: _format_arrow(x, "Rank diff"),
                            "Out of diff": lambda x: _format_arrow(x, "Out of diff"),
                            "Percentile diff": lambda x: _format_arrow(
                                x, "Percentile diff"
                            ),
                        }
                    )

                    st.dataframe(
                        data=df_user_records,
                        use_container_width=True,
                        column_order=tuple(column_order_config),
                        column_config={
                            "Level": st.column_config.TextColumn(_("Level")),
                            "Level ID": st.column_config.ListColumn(_("Level ID")),
                            "Time": st.column_config.TextColumn(_("Time")),
                            "Performance Points": st.column_config.TextColumn(
                                _("Performance Points"),
                                help=_(
                                    "Total Performance Points (pp) in all levels combined"
                                ),
                            ),
                            "Rank": st.column_config.TextColumn(_("Rank")),
                            "Out of": st.column_config.NumberColumn(_("Out of")),
                            "Percentile": st.column_config.ProgressColumn(
                                _("Percentile"), format="%f", min_value=0, max_value=100
                            ),
                            "Upload Time": st.column_config.TextColumn(
                                _("Upload Time")
                            ),
                            "Watch Replay": st.column_config.LinkColumn(
                                _("Watch Replay"), width="small"
                            ),
                            "Race Ghost": st.column_config.LinkColumn(
                                _("Race Ghost"), width="small"
                            ),
                            "Out of diff": st.column_config.TextColumn(
                                "", width="small"
                            ),
                            "Time diff": st.column_config.TextColumn("", width="small"),
                            "Performance Points diff": st.column_config.TextColumn(
                                "", width="small"
                            ),
                            "Rank diff": st.column_config.TextColumn("", width="small"),
                            "Percentile diff": st.column_config.TextColumn(
                                "", width="small"
                            ),
                        },
                        hide_index=True,
                    )

                    with st.expander(
                        "**❔ " + _("How Performance Points (pp) are calculated") + "**"
                    ):
                        st.latex(
                            r"""
                           \textrm{"""
                            + _("Performance Points")
                            + r"""} =
                           \left\{
                           \begin{array}{lr}
                           \lfloor \frac{10000}{\textrm{"""
                            + _("Rank")
                            + r"""}} \rfloor & \textrm{"""
                            + _("if")
                            + r""" \ } 1 \leq \textrm{"""
                            + _("Rank")
                            + r"""} \leq 10\\
                           \lfloor \frac{1000}{2^{\left \lceil log_{10}\textrm{"""
                            + _("Rank")
                            + r"""} \right \rceil - 1}} \times (\frac{10^{\left \lceil log_{10}\textrm{"""
                            + _("Rank")
                            + r"""} \right \rceil - 1}}{\textrm{"""
                            + _("Rank")
                            + r"""}}+0.9) \rfloor & \textrm{"""
                            + _("if")
                            + r""" \ """
                            + _("Rank")
                            + r"""} \gt 10
                           \end{array}
                           \right.
                           """
                        )

                        st.markdown(_("Top 100 Rank to Performance Points conversion"))

                        def pp_formula(i):
                            if i <= 10:
                                return floor(10000 / i)
                            else:
                                return floor(
                                    1000
                                    / (2 ** (ceil(log10(i) - 1)))
                                    * (10 ** (ceil(log10(i)) - 1) / i + 0.9)
                                )

                        split = st.columns((2, 1, 8))
                        with split[0]:
                            df = pd.DataFrame(
                                {
                                    _("Rank"): [i for i in range(1, 101)],
                                    _("Performance Points"): [
                                        pp_formula(i) for i in range(1, 101)
                                    ],
                                    _("Performance Points pp"): [
                                        f"{pp_formula(i)} " + _("pp")
                                        for i in range(1, 101)
                                    ],
                                }
                            )
                            st.dataframe(
                                df.drop(columns=[_("Performance Points")]).rename(
                                    columns={
                                        _("Performance Points pp"): _(
                                            "Performance Points"
                                        )
                                    }
                                ),
                                hide_index=True,
                                use_container_width=True,
                            )

                        with split[2]:
                            fig = px.line(df, x=_("Rank"), y=_("Performance Points"))
                            st.plotly_chart(fig, use_container_width=True)

                except KeyError:
                    st.error("❌ " + _("No Records Found"))

    except Exception as e:
        print(e)
        time.sleep(3)
