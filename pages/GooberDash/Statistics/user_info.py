from math import floor, ceil, log10
import streamlit as st
import pandas as pd
import plotly.express as px
import time
import datetime

conn = st.connection("postgresql", type="sql")


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
            '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-user" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>User Info<span>'
        )

        user_id = st.text_input(
            "Search Player",
            placeholder="Exact User ID",
            value=None,
            # "Search Player", placeholder="Exact Username or User ID", value=None
        )

        if user_id != None:
            tab1, tab2, tab3, tab4, tab5 = st.tabs(
                [
                    "📓 General Info",
                    "📊 Season Records",
                    "🏅 Medals",
                    "🗒️ Stats",
                    "⏳ Time Trials Records",
                ]
            )

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

                curr_performance_points = user_leaderboard_curr_row.loc[
                    0, "total_points"
                ]
                curr_global_rank = int(user_leaderboard_curr_row.loc[0, "rank"])
                curr_first = int(user_leaderboard_curr_row.loc[0, "first"])
                curr_second = int(user_leaderboard_curr_row.loc[0, "second"])
                curr_third = int(user_leaderboard_curr_row.loc[0, "third"])
                curr_completed_levels = int(user_leaderboard_curr_row.loc[0, "count"])
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
                prev_completed_levels = int(user_leaderboard_prev_row.loc[0, "count"])

                delta_performance_points = (
                    curr_performance_points - prev_performance_points
                )
                delta_global_rank = curr_global_rank - prev_global_rank
                delta_first = curr_first - prev_first
                delta_second = curr_second - prev_second
                delta_third = curr_third - prev_third
                delta_completed_levels = curr_completed_levels - prev_completed_levels

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
                        label="Completed Levels", value=f"{curr_completed_levels}/{129}"
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

                df_user_records["Upload Time"] = df_user_records["Upload Time"].astype(
                    str
                )
                if not df_user_records["Upload Time"].str.endswith(" UTC").all():
                    df_user_records["Upload Time"] = (
                        df_user_records["Upload Time"] + " UTC"
                    )

                df_user_records["Upload Time"] = df_user_records["Upload Time"].replace(
                    "NaT UTC", None
                )

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
                    df_user_records = df_user_records[df_user_records["Time"].notna()]

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

                with st.expander("**❔ How Performance Points (pp) are calculated**"):
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
                                columns={"Performance Points pp": "Performance Points"}
                            ),
                            hide_index=True,
                            use_container_width=True,
                        )

                    with split[2]:
                        fig = px.line(df, x="Rank", y="Performance Points")
                        st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        print(e)
        time.sleep(3)
