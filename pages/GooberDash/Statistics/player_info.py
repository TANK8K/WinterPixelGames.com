import streamlit as st
import pandas as pd
import plotly.express as px
import time
import datetime
from math import floor, ceil, log10
from pages.GooberDash.Backend.get_user import user_info_2

conn = st.connection("postgresql", type="sql")


@st.cache_resource(show_spinner=True, ttl=21600)
def query_df_user(user):
    df_user_records = conn.query(
        f"""
        SELECT username, user_id
        FROM goober_dash_time_trials_leaderboard
        WHERE user_id='{user}' OR username ILIKE '%{user}%'
    """
    )
    return df_user_records


@st.cache_resource(show_spinner=True, ttl=21600)
def query_df_user_records(user_id):
    df_user_records = conn.query(
        f"""
        SELECT level_name, level_id, username, user_id, time, upload_time, point, rank, rank_out_of, percentile
        FROM goober_dash_time_trials_records
        WHERE user_id='{user_id}'
        ORDER BY rank, upload_time DESC;
    """
    )
    return df_user_records


@st.cache_resource(show_spinner=True, ttl=21600)
def query_df_user_leaderboard_curr_row(user_id):
    df_user_leaderboard_curr_row = conn.query(
        f"""
        SELECT *
        FROM goober_dash_time_trials_leaderboard
        WHERE user_id='{user_id}'
    """
    )
    return df_user_leaderboard_curr_row


@st.cache_resource(show_spinner=True, ttl=21600)
def query_df_user_leaderboard_prev_row(user_id):
    df_user_leaderboard_prev_row = conn.query(
        f"""
        SELECT *
        FROM goober_dash_time_trials_leaderboard_prev
        WHERE user_id='{user_id}'
    """
    )
    return df_user_leaderboard_prev_row


@st.cache_resource(show_spinner=True, ttl=21600)
def query_df_level_ids():
    df_level_ids = conn.query(
        """
        SELECT DISTINCT level_id, level_name, rank_out_of
        FROM goober_dash_time_trials_records;
        """
    )
    return df_level_ids


def load_page():
    try:
        with open("../storage/last_update.txt", "r") as f:
            last_update = float(f.readline())

        with open("../storage/level_counts.txt", "r") as f:
            level_counts = int(f.readline())

        st.image(
            "static/goober_dash_logo_text.png",
            width=280,
        )
        st.html(
            '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-user" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Player Info<span>'
        )

        user_columns = st.columns((5, 1, 5))

        with user_columns[0]:
            user = st.text_input(
                "Search Player",
                placeholder="Username or User ID",
                value=None,
            )

        if user not in [None, ""]:
            users_found_database = query_df_user(user)
            users_found_database.rename(
                columns={
                    "username": "Player",
                    "user_id": "User ID",
                },
                inplace=True,
            )

            try:
                users_found_api_res = user_info_2(user)["users"][0]
                users_found_api_name = users_found_api_res["display_name"]
                users_found_api_id = users_found_api_res["id"]
                search_player_not_in_database = (
                    users_found_api_id not in users_found_database["User ID"].tolist()
                )
                if search_player_not_in_database:
                    new_row = {
                        "Player": users_found_api_name,
                        "User ID": users_found_api_id,
                    }
                    users_found_combined = pd.concat(
                        [pd.DataFrame([new_row]), users_found_database],
                        ignore_index=True,
                    )
                else:
                    users_found_combined = users_found_database
            except KeyError:
                users_found_combined = users_found_database

            if len(users_found_combined) == 1:
                user_id = users_found_combined.iloc[0]["User ID"]

            elif len(users_found_combined) > 1:
                with user_columns[2]:
                    player_name = st.selectbox(
                        "Select Player",
                        users_found_combined["Player"],
                        index=None,
                        placeholder=f"{len(users_found_combined)} Players found",
                    )
                    if player_name is not None:
                        user_id = users_found_combined.loc[
                            users_found_combined["Player"] == player_name, "User ID"
                        ].iloc[0]
                    else:
                        user_id = None
            else:
                st.error("❌ No Players Found")
                user_id = None

        if user_id not in [None, ""]:
            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                [
                    "📓 General Info",
                    "📊 Season Records",
                    "🏅 Medals",
                    "🗒️ Stats",
                    "⏳ Time Trials Records",
                ]
            )

            ###################################################################################################
            # async def user_info(
            #    self,
            #    interaction: discord.Interaction,
            #    user_type: typing.Literal["User ID", "Username"],
            #    id_or_username: str,
            #    # section: typing.Literal[
            #    #     "📓 General Info only",
            #    #     "with 📊 Seasons Records",
            #    #     "with 🎖️ Medals",
            #    #     "with 🗒️ Stats",
            #    #     "All",
            #    # ],
            # ):
            #    """🔵 Return info about a specified Goober Dash user"""
            #    # """🔵 Return info about a specified Goober Dash user with optional section(s)"""

            #    await refresh_config()

            #    await interaction.response.defer(ephemeral=False, thinking=True)

            #    # Get User ID (if Username is provided), create time and online status
            #    try:
            #        if user_type == "User ID":
            #            response = await goober_dash_client.user_info_2(id_or_username)
            #        else:
            #            id_or_username = id_or_username.replace("&", " ")
            #            response = await goober_dash_client.user_info_2("", id_or_username)
            #        user_info_2 = response["users"][0]
            #        user_id = user_info_2["id"]
            #        username = user_info_2["username"]
            #        create_time = user_info_2["create_time"]
            #        try:
            #            is_online = user_info_2["online"]
            #        except Exception:
            #            is_online = False
            #    except Exception:
            #        # The code is wrong, send an error response
            #        await interaction.followup.send(
            #            embed=discord.Embed(color=0xFF0000, title="❌ Player not found ❌")
            #        )
            #        return

            #    # Get user data
            #    response = await goober_dash_client.user_info(user_id)
            #    user_data = json.loads(response)

            #    # Get medals config
            #    awards_config = goober_dash_server_config["awards"]["awards"]

            #    # Get cosmetics config
            #    cosmetics_config = goober_dash_server_config["cosmetics"]

            #    # Get general player info
            #    display_name = user_data["display_name"]
            #    level = user_data["level"]

            #    cosmetics_type_keys = ["body", "hat", "suit", "hand", "color"]
            #    cosmetics_dict = dict()
            #    for cosmetics_type in cosmetics_type_keys:
            #        try:
            #            cosmetics_type_all_info = ""
            #            cosmetics_type_all_info += f"{str(cosmetics_config.get(user_data['skin'][cosmetics_type])['name']):<20} "
            #            cosmetics_type_all_info += f"Level {str(cosmetics_config.get(user_data['skin'][cosmetics_type])['level']):<2} "
            #            try:
            #                rarity = str(
            #                    cosmetics_config.get(user_data["skin"][cosmetics_type])[
            #                        "rarity"
            #                    ]
            #                )
            #                if rarity == "common":
            #                    cosmetics_type_all_info += rarity.title()
            #                elif rarity == "rare":
            #                    cosmetics_type_all_info += (
            #                        f"\u001b[2;32m{rarity.title()}\u001b[0m"
            #                    )
            #                elif rarity == "epic":
            #                    cosmetics_type_all_info += (
            #                        f"\u001b[2;35m{rarity.title()}\u001b[0m"
            #                    )
            #                elif rarity == "legendary":
            #                    cosmetics_type_all_info += (
            #                        f"\u001b[2;33m{rarity.title()}\u001b[0m"
            #                    )
            #            except KeyError:  # Default
            #                cosmetics_type_all_info += "Common"
            #        except Exception:
            #            cosmetics_type_all_info = "N.A."
            #        cosmetics_dict[cosmetics_type] = cosmetics_type_all_info

            #    # Add general player info
            #    general_info = "```ansi\n"
            #    general_info += f"{'Username: ':>15}{username}\n"
            #    general_info += f"{'Display name: ':>15}{display_name}\n"
            #    dt_create_time = datetime.datetime.strptime(
            #        create_time.translate(":-"), "%Y-%m-%dT%H:%M:%SZ"
            #    )
            #    general_info += f"{'Create Time: ':>15}{dt_create_time} UTC ({timeago.format(dt_create_time, datetime.datetime.now())})\n"
            #    general_info += f"{'Level: ':>15}{level}\n"
            #    general_info += f"{'Current Body: ':>15}{cosmetics_dict['body']}\n"
            #    general_info += f"{'Current Hat: ':>15}{cosmetics_dict['hat']}\n"
            #    general_info += f"{'Current Suit: ':>15}{cosmetics_dict['suit']}\n"
            #    general_info += f"{'Current Hand: ':>15}{cosmetics_dict['hand']}\n"
            #    general_info += f"{'Current Color: ':>15}{cosmetics_dict['color']}\n"
            #    general_info += f"{'User ID: ':>15}{user_id}\n"
            #    general_info += (
            #        f"{'Online: ':>15}"
            #        + "\u001b[2;"
            #        + ("32" if is_online else "31")
            #        + f"m{is_online}\u001b[0m\n"
            #    )
            #    general_info += "```"

            #    # Add to embed
            #    message = ""
            #    message += f"📓 ***General Info***:\n{general_info}\n"
            #    # message1 = ""
            #    # message1 += f"📓 ***General Info***:\n{general_info}\n"

            #    # # Send
            #    # await interaction.followup.send(
            #    #     embed=discord.Embed(title="Goober Dash <:goober:1146508948325814402>\nDetailed Player Info:", description=message1, color=0x55D3FD)
            #    # )

            #    # if section in {"with 📊 Seasons Records", "All"}:
            #    # Create seasons records list
            #    seasons_records_list = "```ansi\n"

            #    crowns = f"{'Season:':<8}{'Days:':<9}{'Local:':<9}{'Global:':<9}{'Crowns:':<8}{'Games:':<7}{'C/G:'}\n{'─'*56}\n"
            #    crowns_record = False

            #    for season in range(
            #        1, goober_dash_current_season + 1
            #    ):  # From first season to current season
            #        response_global = await goober_dash_client.query_leaderboard(
            #            season,
            #            "global",
            #            1,
            #            "",
            #            user_id,
            #        )
            #        try:
            #            records_global = response_global["owner_records"]
            #        except KeyError:
            #            continue

            #        country_code = json.loads(records_global[0]["metadata"])["country"]
            #        response_local = await goober_dash_client.query_leaderboard(
            #            season,
            #            f"country.{country_code.upper()}",
            #            1,
            #            "",
            #            user_id,
            #        )
            #        try:
            #            records_local = response_local["owner_records"]
            #        except KeyError:
            #            continue

            #        rank = int(records_global[0]["rank"])

            #        rank_emoji = "  "
            #        if season != goober_dash_current_season:
            #            if rank == 1:
            #                rank_emoji = "🥇"
            #            elif rank == 2:
            #                rank_emoji = "🥈"
            #            elif rank == 3:
            #                rank_emoji = "🥉"

            #        required_season_info = goober_dash_season_info(season, "short")

            #        crowns_record = True
            #        crowns += (
            #            f"{'CURRENT SEASON'.center(56, '-')}\n"
            #            if season == goober_dash_current_season
            #            else ""
            #        )
            #        crowns += f"{season:^8}"  # Season
            #        crowns += f"{required_season_info[2].split(' ', 1)[0]:<6}"  # Days
            #        crowns += flag.flagize(f":{country_code}: ")  # Country Flag
            #        crowns += f"{rank_emoji:<1}{'{:,}'.format(int(records_local[0]['rank'])):<7}"  # Local Rank
            #        crowns += f"{rank_emoji:<1}{'{:,}'.format(int(records_global[0]['rank'])):<7}"  # Global Rank
            #        crowns += (
            #            f"{'👑 ' + '{:,}'.format(int(records_global[0]['score'])):<7}"  # Crowns
            #        )
            #        crowns += f"{records_global[0]['num_score']:<7}"  # Games
            #        crowns += f"{int(records_global[0]['score'])/int(records_global[0]['num_score']):.2f}\n"  # Crowns / Games

            #    if not crowns_record:
            #        seasons_records_list += "No records found"
            #    else:
            #        seasons_records_list += crowns
            #        country_name = pycountry.countries.get(
            #            alpha_2=f"{country_code.upper()}"
            #        ).name
            #        seasons_records_list += (
            #            f"† Country/Region: {country_name} ({country_code})\n"
            #        )
            #    seasons_records_list += "```"

            #    # Add to embed
            #    message += f"📊 ***Seasons Records***:\n{seasons_records_list}\n"
            #    # message2 = ""
            #    # message2 += f"📊 ***Seasons Records***:\n{seasons_records_list}\n"

            #    # # Send
            #    # await interaction.followup.send(
            #    #     embed=discord.Embed(description=message2, color=0x55D3FD)
            #    # )

            #    # if section in {"with 🎖️ Medals", "All"}:
            #    # Create medal list
            #    medal_list = "```\n"

            #    l1 = []  # medals_priority
            #    l2 = []  # medals_names
            #    l3 = []  # medals_count

            #    for medal in user_data["awards"]:
            #        l1.append(awards_config.get(medal)["priority"])
            #        l2.append(awards_config.get(medal)["name"])
            #        l3.append(user_data["awards"][medal]["count"])

            #    if len(l1) != 0:
            #        l1, l2, l3 = map(
            #            list, zip(*sorted(zip(l1, l2, l3)))
            #        )  # Sort l2 and l3 according to l1

            #        for i in range(len(l1)):
            #            medal_list += f"{l2[i]:<20} x{l3[i]}\n"
            #    else:
            #        medal_list += "No medals found\n"
            #    medal_list += "```"

            #    # Add to embed
            #    message += f"🎖️ ***Medals***:\n{medal_list}\n"
            #    # message3 = ""
            #    # message3 += f"🎖️ ***Medals***:\n{medal_list}\n"

            #    # # Send
            #    # await interaction.followup.send(
            #    #     embed=discord.Embed(description=message3, color=0x55D3FD)
            #    # )

            #    # if section in {"with 🗒️ Stats", "All"}:
            #    # Create stats
            #    stats_list = "```ansi\n"
            #    stats = user_data["stats"]

            #    try:
            #        games_played = stats["GamesPlayed"]
            #    except KeyError:
            #        games_played = 0
            #    try:
            #        games_won = stats["GamesWon"]
            #    except KeyError:
            #        games_won = 0
            #    try:
            #        deaths = stats["Deaths"]
            #    except KeyError:
            #        deaths = 0
            #    try:
            #        deaths_per_games_played = f"{stats['Deaths']/stats['GamesPlayed']:.2f}"
            #    except KeyError:
            #        deaths_per_games_played = 0
            #    try:
            #        longest_winstreak = stats["Winstreak"]
            #    except KeyError:
            #        longest_winstreak = 0
            #    try:
            #        current_winstreak = stats["CurrentWinstreak"]
            #    except KeyError:
            #        current_winstreak = 0
            #    try:
            #        winrate = f"{games_won/games_played*100:.2f}"
            #    except Exception:
            #        winrate = 0

            #    stats_dict = {
            #        "Games Played": games_played,
            #        "Winrate": f"{winrate}% - \u001b[2;32m{games_won}W\u001b[0m \u001b[2;31m{games_played-games_won}L\u001b[0m",
            #        "Deaths": deaths,
            #        "Deaths/Games Played": deaths_per_games_played,
            #        "Longest Winstreak": longest_winstreak,
            #        "Current Winstreak": current_winstreak,
            #    }

            #    for key in stats_dict:
            #        stats_list += f"{key:>19}: {stats_dict[key]}\n"
            #    stats_list += "```"

            #    # Add to embed
            #    message += f"🗒️ ***Stats***:\n{stats_list}\n"
            #    # message4 = ""
            #    # message4 += f"🗒️ ***Stats***:\n{stats_list}\n"

            #    # # Send
            #    # await interaction.followup.send(
            #    #     embed=discord.Embed(description=message4, color=0x55D3FD)
            #    # )

            #    # Send
            #    await interaction.followup.send(
            #        embed=discord.Embed(
            #            title="Goober Dash <:goober:1146508948325814402>\nDetailed Player Info:",
            #            description=message,
            #            color=0x55D3FD,
            #        )
            #    )
            ###################################################################################################
            with tab1:
                st.write("WIP")
            with tab2:
                st.write("WIP")
            with tab3:
                st.write("WIP")
            with tab4:
                st.write("WIP")
            with tab5:
                st.caption(
                    f"Last Update: {datetime.datetime.fromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S')} UTC (Updated Every 12 Hours)"
                )

                user_leaderboard_curr_row = query_df_user_leaderboard_curr_row(user_id)
                user_leaderboard_prev_row = query_df_user_leaderboard_prev_row(user_id)

                metric_cols = st.columns((4, 4, 1, 1, 1, 4))

                try:
                    curr_performance_points = user_leaderboard_curr_row.loc[
                        0, "total_points"
                    ]
                    curr_global_rank = int(user_leaderboard_curr_row.loc[0, "rank"])
                    curr_first = int(user_leaderboard_curr_row.loc[0, "first"])
                    curr_second = int(user_leaderboard_curr_row.loc[0, "second"])
                    curr_third = int(user_leaderboard_curr_row.loc[0, "third"])
                    curr_completed_levels = int(
                        user_leaderboard_curr_row.loc[0, "count"]
                    )
                    curr_top_percent = int(
                        user_leaderboard_curr_row.loc[0, "top_percentile"]
                    )

                    prev_performance_points = user_leaderboard_prev_row.loc[
                        0, "total_points"
                    ]
                    prev_global_rank = int(user_leaderboard_prev_row.loc[0, "rank"])
                    prev_first = int(user_leaderboard_prev_row.loc[0, "first"])
                    prev_second = int(user_leaderboard_prev_row.loc[0, "second"])
                    prev_third = int(user_leaderboard_prev_row.loc[0, "third"])
                    prev_completed_levels = int(
                        user_leaderboard_prev_row.loc[0, "count"]
                    )

                    delta_performance_points = (
                        curr_performance_points - prev_performance_points
                    )
                    delta_global_rank = curr_global_rank - prev_global_rank
                    delta_first = curr_first - prev_first
                    delta_second = curr_second - prev_second
                    delta_third = curr_third - prev_third
                    delta_completed_levels = (
                        curr_completed_levels - prev_completed_levels
                    )

                    if delta_performance_points != 0:
                        metric_cols[0].metric(
                            label="Total Performance Points",
                            value=f"{curr_performance_points} pp",
                            delta=f"{delta_performance_points} pp",
                        )
                    else:
                        metric_cols[0].metric(
                            label="Total Performance Points",
                            value=f"{curr_performance_points} pp",
                        )
                    if delta_global_rank != 0:
                        metric_cols[1].metric(
                            label="Global Rank",
                            value=f"#{curr_global_rank} (Top {curr_top_percent}%)",
                            delta=delta_global_rank,
                            delta_color="inverse",
                        )
                    else:
                        metric_cols[1].metric(
                            label="Global Rank",
                            value=f"#{curr_global_rank} (Top {0.01}%)",
                        )

                    if delta_first != 0:
                        metric_cols[2].metric(
                            label="🥇", value=f"{curr_first}", delta=delta_first
                        )
                    else:
                        metric_cols[2].metric(label="🥇", value=f"{curr_first}")

                    if delta_second != 0:
                        metric_cols[3].metric(
                            label="🥈", value=f"{curr_second}", delta=delta_second
                        )
                    else:
                        metric_cols[3].metric(label="🥈", value=f"{curr_second}")
                    if delta_third != 0:
                        metric_cols[4].metric(
                            label="🥉", value=f"{curr_third}", delta=delta_third
                        )
                    else:
                        metric_cols[4].metric(label="🥉", value=f"{curr_third}")
                    if delta_completed_levels != 0:
                        metric_cols[5].metric(
                            label="Completed Levels",
                            value=f"{curr_completed_levels}/{level_counts}",
                            delta=delta_completed_levels,
                        )
                    else:
                        metric_cols[5].metric(
                            label="Completed Levels",
                            value=f"{curr_completed_levels}/{129}",
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
                            "upload_time": "Upload Time",
                            "point": "Performance Points",
                            "rank": "Rank",
                            "rank_out_of": "Out of",
                            "percentile": "Percentile",
                        },
                        inplace=True,
                    )

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
                    missing_levels["Percentile"] = None
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

                    df_user_records["column_name"] = (
                        df_user_records["Performance Points"]
                        .astype(float, errors="ignore")
                        .astype(float, errors="ignore")
                    )

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
                        if rank == 1:
                            return "🥇"
                        elif rank == 2:
                            return "🥈"
                        elif rank == 3:
                            return "🥉"
                        else:
                            return f"# {rank:.0f}"

                    df_user_records["Rank"] = df_user_records["Rank"].apply(add_emojis)

                    display_level_id_value = False
                    display_incompleted_levels_value = False

                    checkboxes = st.columns(2)
                    with checkboxes[0]:
                        display_level_id = st.checkbox(
                            "Display Level ID",
                            value=display_level_id_value,
                            key="first_display_level_id",
                        )
                    with checkboxes[1]:
                        display_incompleted_levels = st.checkbox(
                            "Display Incompleted Levels",
                            value=display_incompleted_levels_value,
                        )

                    column_order_config = [
                        "Level",
                        "Level ID",
                        "Time",
                        "Performance Points",
                        "Rank",
                        "Out of",
                        "Percentile",
                        "Upload Time",
                        "Watch Replay",
                        "Race Ghost",
                    ]
                    if not display_level_id:
                        column_order_config.remove("Level ID")
                    if not display_incompleted_levels:
                        df_user_records = df_user_records[
                            df_user_records["Time"].notna()
                        ]

                    def _format_arrow(val):
                        if isinstance(val, int):
                            return (
                                f"{'▲' if val > 0 else '▼'} {abs(val):.0f}"
                                if val != 0
                                else f"{val:.0f}"
                            )
                        else:
                            return val

                    def _color_arrow(val):
                        try:
                            return (
                                "color: green"
                                if val > 0
                                else "color: red" if val < 0 else "color: transparent"
                            )
                        except Exception:
                            pass

                    # df_user_records = df_user_records.style.map(
                    #    _color_arrow, subset=["Out of"]
                    # ).format(_format_arrow)

                    st.dataframe(
                        data=df_user_records,
                        use_container_width=True,
                        column_order=tuple(column_order_config),
                        column_config={
                            "Level ID": st.column_config.ListColumn(),
                            "Time": st.column_config.NumberColumn(format="%f s"),
                            "Watch Replay": st.column_config.LinkColumn(
                                display_text="▶️", width="small"
                            ),
                            "Race Ghost": st.column_config.LinkColumn(
                                display_text="👻", width="small"
                            ),
                            "Performance Points": st.column_config.NumberColumn(
                                help="Total Performance Points (pp) in all levels combined",
                                format="%d pp",
                            ),
                            "Percentile": st.column_config.ProgressColumn(
                                format="%f", min_value=0, max_value=100
                            ),
                            # "Out of": st.column_config.TextColumn("", width="small"),
                        },
                        hide_index=True,
                    )

                    with st.expander(
                        "**❔ How Performance Points (pp) are calculated**"
                    ):
                        st.latex(
                            r"""
                            \textrm{Performance \ Points} = 
                            \left\{
                            \begin{array}{lr}
                            \lfloor \frac{10000}{\textrm{Rank}} \rfloor & \textrm{if \ } 1 \leq \textrm{Rank} \leq 10\\
                            \lfloor \frac{1000}{2^{\left \lceil log_{10}\textrm{Rank} \right \rceil - 1}} \times (\frac{10^{\left \lceil log_{10}\textrm{Rank} \right \rceil - 1}}{\textrm{Rank}}+0.9) \rfloor & \textrm{if \ Rank} \gt 10
                            \end{array}
                            \right.
                            """
                        )

                        st.markdown("Top 100 Rank to Performance Points conversion")

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
                                    "Rank": [i for i in range(1, 101)],
                                    "Performance Points": [
                                        pp_formula(i) for i in range(1, 101)
                                    ],
                                    "Performance Points pp": [
                                        f"{pp_formula(i)} pp" for i in range(1, 101)
                                    ],
                                }
                            )
                            st.dataframe(
                                df.drop(columns=["Performance Points"]).rename(
                                    columns={
                                        "Performance Points pp": "Performance Points"
                                    }
                                ),
                                hide_index=True,
                                use_container_width=True,
                            )

                        with split[2]:
                            fig = px.line(df, x="Rank", y="Performance Points")
                            st.plotly_chart(fig, use_container_width=True)

                except KeyError:
                    st.error("❌ No Records Found")

    except Exception as e:
        print(e)
        time.sleep(3)
