from math import floor, ceil, log10
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import datetime
from common_config import set_localization
from country_or_region import country_region

conn = st.connection("postgresql", type="sql")


# @st.cache_data(show_spinner=True, ttl=21600)
def split_frame(input_df, rows):
    df = [input_df.loc[i : i + rows - 1, :] for i in range(0, len(input_df), rows)]
    return df


# @st.cache_data(show_spinner=True, ttl=21600)
def query_df_first_records():
    df_first_records = conn.query(
        """
        SELECT level_name, level_id, username, user_id, time, upload_time, rank_out_of
        FROM goober_dash_time_trials_records
        WHERE rank=1
        ORDER BY upload_time DESC;
    """
    )
    return df_first_records


def load_page(selected_language):
    _ = set_localization(selected_language)

    try:
        country_region_list = country_region(selected_language)
        with open("../storage/last_update.txt", "r") as f:
            last_update = float(f.readline())

        with open("../storage/level_counts.txt", "r") as f:
            level_counts = int(f.readline())

        st.image(
            "static/GooberDash/goober_dash_logo_text.png",
            width=280,
        )
        st.html(
            '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-flag-checkered" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
            + _("Time Trials")
            + " ("
            + _("Certified Levels")
            + ')<br><img style="display: inline; margin: 0 5px 8px 0; width: 25px" src="./app/static/GooberDash/medal_1st.png">'
            + _("World Records Statistics")
            + "<span>"
        )
        st.caption(
            _("Last Update")
            + f": {datetime.datetime.fromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S')} UTC ("
            + _("Updated Every 12 Hours")
            + ")"
        )
        tab1, tab2, tab3 = st.tabs(
            [
                "🏆 **" + _("Performance Points Leaderboard") + "**",
                "🥇 **" + _("World Records") + "**",
                "🥧 **" + _("WRs Distribution") + "**",
            ]
        )

        with tab1:
            df_leaderboard = conn.query(
                "SELECT * FROM goober_dash_time_trials_leaderboard"
            )
            df_leaderboard.rename(
                columns={
                    "user_id": "User ID",
                    "username": "Player",
                    "total_points": "Performance Points",
                    "count": "Completed Levels",
                    "rank": "Global Rank",
                    "top_percentile": "Global Top %",
                    "rank_local": "Local Rank",
                    "top_percentile_local": "Local Top %",
                    "first": "🥇",
                    "second": "🥈",
                    "third": "🥉",
                    "total_points_diff": "Performance Points diff",
                    "count_diff": "Completed Levels diff",
                    "rank_diff": "Global Rank diff",
                    "top_percentile_diff": "Global Top % diff",
                    "rank_local_diff": "Local Rank diff",
                    "top_percentile_local_diff": "Local Top % diff",
                    "first_diff": "🥇 diff",
                    "second_diff": "🥈 diff",
                    "third_diff": "🥉 diff",
                },
                inplace=True,
            )
            display_global_rank_value = True
            display_local_rank_value = False
            display_user_id_value = False
            display_changes = False

            new_column_order = [
                "Global Rank",
                "Global Rank diff",
                "Local Rank",
                "Local Rank diff",
                "Player",
                "User ID",
                "Performance Points",
                "Performance Points diff",
                "Global Top %",
                "Global Top % diff",
                "Local Top %",
                "Local Top % diff",
                "🥇",
                "🥇 diff",
                "🥈",
                "🥈 diff",
                "🥉",
                "🥉 diff",
                "Completed Levels",
                "Completed Levels diff",
            ]
            df_leaderboard = df_leaderboard[new_column_order]
            df_leaderboard["Player"] = df_leaderboard["Player"].str.replace(
                "-", "", regex=False
            )

            top_menu = st.columns(5)

            options_dict = {
                "Global Rank": _("Global Rank"),
                "Global Rank diff": _("Global Rank diff"),
                "Local Rank": _("Local Rank"),
                "Local Rank diff": _("Local Rank diff"),
                "Completed Levels": _("Completed Levels"),
                "Completed Levels diff": _("Completed Levels diff"),
                "Performance Points": _("Performance Points"),
                "Performance Points diff": _("Performance Points diff"),
                "Global Top %": _("Global Top %"),
                "Global Top % diff": _("Global Top % diff"),
                "Local Top %": _("Local Top %"),
                "Local Top % diff": _("Local Top % diff"),
                "🥇": "🥇",
                "🥇 diff": _("🥇 diff"),
                "🥈": "🥈",
                "🥈 diff": _("🥈 diff"),
                "🥉": "🥉",
                "🥉 diff": _("🥉 diff"),
                "Player": _("Player"),
                "User ID": _("User ID"),
            }

            with top_menu[0]:
                options = [option for option in options_dict]
                sort_field = st.selectbox(
                    _("Sort By"),
                    options,
                    format_func=lambda x: options_dict.get(x),
                )
            with top_menu[1]:
                sort_direction = st.radio(
                    _("Order"), options=["▲", "▼"], horizontal=True
                )
            with top_menu[2]:
                filter_country = st.selectbox(
                    _("Country/Region"),
                    options=country_region_list,
                )
                if filter_country != "🌐 " + _("Global"):
                    display_local_rank_value = True
                    display_global_rank_value = False
                else:
                    display_local_rank_value = False
                    display_global_rank_value = True
            with top_menu[3]:
                filter_user = st.text_input(
                    _("Search Player"), placeholder=_("Username or User ID")
                )
            with top_menu[4]:
                display_global_rank = st.checkbox(
                    _("Display Global Rank"), value=display_global_rank_value
                )
                display_local_rank = st.checkbox(
                    _("Display Local Rank"), value=display_local_rank_value
                )
                display_user_id = st.checkbox(
                    _("Display User ID"), value=display_user_id_value
                )
                display_changes = st.checkbox(
                    _("Display Changes"), value=display_changes
                )

            def search_dataframe(filter_country, filter_user):
                if filter_user != "":
                    player_match = df_leaderboard[
                        df_leaderboard["Player"].str.contains(
                            filter_user, case=False, na=False
                        )
                    ]
                    user_id_match = df_leaderboard[
                        df_leaderboard["User ID"].str.contains(
                            filter_user, case=False, na=False
                        )
                    ]
                    result = (
                        pd.concat([player_match, user_id_match])
                        .drop_duplicates()
                        .reset_index(drop=True)
                    )
                if filter_country != "🌐 " + _("Global"):
                    if filter_user == "":
                        result = df_leaderboard
                    result = result[
                        result["Player"].str.contains(
                            filter_country[:2], case=False, na=False
                        )
                    ]
                return result

            if filter_country != "🌐 " + _("Global") or filter_user:
                df_leaderboard = search_dataframe(filter_country, filter_user)

            if df_leaderboard.empty:
                st.error(_("No Records Found"), icon="❌")

            df_leaderboard = df_leaderboard.sort_values(
                by=sort_field,
                ascending=sort_direction == "▲",
                ignore_index=True,
            )
            pagination = st.container()

            bottom_menu = st.columns((5, 1, 1))
            with bottom_menu[2]:
                batch_size = st.selectbox(_("Page Size"), options=[25, 50, 100])
            with bottom_menu[1]:
                total_pages = (
                    int(len(df_leaderboard) / batch_size) + 1
                    if int(len(df_leaderboard) / batch_size) > 0
                    else 1
                )
                current_page = st.number_input(
                    _("Page"), min_value=1, max_value=total_pages, step=1
                )

            pages = split_frame(df_leaderboard, batch_size)
            data = pages[current_page - 1]
            min_global_rank = data["Global Rank"].min()
            max_global_rank = data["Global Rank"].max()
            min_local_rank = data["Local Rank"].min()
            max_local_rank = data["Local Rank"].max()
            with bottom_menu[0]:
                bottom_info = (
                    _("Page")
                    + f" **{current_page}** "
                    + _("of")
                    + f" **{total_pages}**{'&nbsp;'*5}"
                )
                if filter_country == "🌐 " + _("Global"):
                    bottom_info += (
                        f"{filter_country} "
                        + _("Rank")
                        + f"**{min_global_rank}** "
                        + _("to")
                        + f" **{max_global_rank}** "
                    )
                else:
                    bottom_info += (
                        f"{filter_country} "
                        + _("Rank")
                        + f" **{min_local_rank}** "
                        + _("to")
                        + f" **{max_local_rank}** "
                    )
                bottom_info += (
                    "(" + _("Total number of Players") + f": **{len(df_leaderboard)}**)"
                )
                st.markdown(bottom_info)

            column_order_config = [
                "Global Rank diff",
                "Global Rank",
                "Local Rank diff",
                "Local Rank",
                "Player",
                "User ID",
                "Performance Points",
                "Performance Points diff",
                "Global Top %",
                "Global Top % diff",
                "Local Top %",
                "Local Top % diff",
                "🥇",
                "🥇 diff",
                "🥈",
                "🥈 diff",
                "🥉",
                "🥉 diff",
                "Completed Levels",
                "Completed Levels diff",
            ]
            if not display_global_rank:
                try:
                    column_order_config.remove("Global Rank")
                    column_order_config.remove("Global Rank diff")
                    column_order_config.remove("Global Top %")
                    column_order_config.remove("Global Top % diff")
                except Exception:
                    pass
            if not display_local_rank:
                try:
                    column_order_config.remove("Local Rank")
                    column_order_config.remove("Local Rank diff")
                    column_order_config.remove("Local Top %")
                    column_order_config.remove("Local Top % diff")
                except Exception:
                    pass
            if not display_user_id:
                try:
                    column_order_config.remove("User ID")
                except Exception:
                    pass
            if not display_changes:
                try:
                    column_order_config = [
                        column
                        for column in column_order_config
                        if column
                        not in [
                            "Global Rank diff",
                            "Local Rank diff",
                            "Performance Points diff",
                            "Global Top % diff",
                            "Local Top % diff",
                            "🥇 diff",
                            "🥈 diff",
                            "🥉 diff",
                            "Completed Levels diff",
                        ]
                    ]
                except Exception:
                    pass

            def _format_arrow(val, column_name):
                if isinstance(val, (int, float)) and not np.isnan(val):
                    if column_name == "Performance Points diff":
                        symbol = "▲" if val > 0 else "▼"
                        formatted_value = f"{int(abs(val))}"
                        suffix = " pp"
                        return f"{symbol} {formatted_value}{suffix}"
                    elif column_name in [
                        "Global Rank diff",
                        "Local Rank diff",
                    ]:
                        symbol = "▲" if val < 0 else "▼"
                        formatted_value = f"{int(abs(val))}"
                        suffix = ""
                        return f"{symbol} {formatted_value}{suffix}"
                    elif column_name in [
                        "🥇 diff",
                        "🥈 diff",
                        "🥉 diff",
                        "Completed Levels diff",
                    ]:
                        symbol = "▲" if val > 0 else "▼"
                        formatted_value = f"{int(abs(val))}"
                        suffix = ""
                        return f"{symbol} {formatted_value}{suffix}"
                    elif column_name in ["Global Top % diff", "Local Top % diff"]:
                        symbol = "▲" if val > 0 else "▼"
                        formatted_value = f"{abs(val):.2f}"
                        suffix = " %"
                        return f"{symbol} {formatted_value}{suffix}"
                    elif column_name in ["Global Rank", "Local Rank"]:
                        return f"# {val}"
                    elif column_name == "Performance Points":
                        return f"{val} pp"
                    elif column_name in ["Global Top %", "Local Top %"]:
                        return f"{val:.2f}%"
                elif pd.isna(val):
                    return ""
                return val

            def _color_arrow(val, column_name):
                try:
                    if val is None:
                        return "color: transparent;"
                    elif column_name in [
                        "Performance Points diff",
                        "🥇 diff",
                        "🥈 diff",
                        "🥉 diff",
                        "Completed Levels diff",
                    ]:
                        if val > 0:
                            return "color: green;"
                        elif val < 0:
                            return "color: red;"
                        else:
                            return "color: transparent;"
                    elif column_name in [
                        "Global Rank diff",
                        "Local Rank diff",
                        "Global Top % diff",
                        "Local Top % diff",
                    ]:
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

            data = data.style
            data = data.map(
                lambda val: _color_arrow(val, "Global Rank diff"),
                subset=["Global Rank diff"],
            )
            data = data.map(
                lambda val: _color_arrow(val, "Local Rank diff"),
                subset=["Local Rank diff"],
            )
            data = data.map(
                lambda val: _color_arrow(val, "Performance Points diff"),
                subset=["Performance Points diff"],
            )
            data = data.map(
                lambda val: _color_arrow(val, "Global Top % diff"),
                subset=["Global Top % diff"],
            )
            data = data.map(
                lambda val: _color_arrow(val, "Local Top % diff"),
                subset=["Local Top % diff"],
            )
            data = data.map(
                lambda val: _color_arrow(val, "🥇 diff"), subset=["🥇 diff"]
            )
            data = data.map(
                lambda val: _color_arrow(val, "🥈 diff"), subset=["🥈 diff"]
            )
            data = data.map(
                lambda val: _color_arrow(val, "🥉 diff"), subset=["🥉 diff"]
            )
            data = data.map(
                lambda val: _color_arrow(val, "Completed Levels diff"),
                subset=["Completed Levels diff"],
            )

            data = data.format(
                {
                    "Global Rank": lambda x: _format_arrow(x, "Global Rank"),
                    "Local Rank": lambda x: _format_arrow(x, "Local Rank"),
                    "Performance Points": lambda x: _format_arrow(
                        x, "Performance Points"
                    ),
                    "Global Top %": lambda x: _format_arrow(x, "Global Top %"),
                    "Local Top %": lambda x: _format_arrow(x, "Local Top %"),
                    "Global Rank diff": lambda x: _format_arrow(x, "Global Rank diff"),
                    "Local Rank diff": lambda x: _format_arrow(x, "Local Rank diff"),
                    "Performance Points diff": lambda x: _format_arrow(
                        x, "Performance Points diff"
                    ),
                    "Global Top % diff": lambda x: _format_arrow(
                        x, "Global Top % diff"
                    ),
                    "Local Top % diff": lambda x: _format_arrow(x, "Local Top % diff"),
                    "🥇 diff": lambda x: _format_arrow(x, "🥇 diff"),
                    "🥈 diff": lambda x: _format_arrow(x, "🥈 diff"),
                    "🥉 diff": lambda x: _format_arrow(x, "🥉 diff"),
                    "Completed Levels diff": lambda x: _format_arrow(
                        x, "Completed Levels diff"
                    ),
                }
            )

            pagination.dataframe(
                data=data,
                use_container_width=True,
                column_order=tuple(column_order_config),
                column_config={
                    "Completed Levels": st.column_config.ProgressColumn(
                        _("Completed Levels"),
                        help=_("Total Number of Levels with Records"),
                        format=f"%f/{level_counts}",
                        min_value=0,
                        max_value=level_counts,
                    ),
                    "User ID": st.column_config.ListColumn(_("User ID")),
                    "Global Rank": st.column_config.TextColumn(_("Global Rank")),
                    "Local Rank": st.column_config.TextColumn(_("Local Rank")),
                    "Player": st.column_config.TextColumn(_("Player")),
                    "Performance Points": st.column_config.NumberColumn(
                        _("Performance Points"),
                        help=_("Total Performance Points (pp) in all levels combined"),
                    ),
                    "Global Top %": st.column_config.NumberColumn(_("Global Top %")),
                    "Local Top %": st.column_config.NumberColumn(_("Local Top %")),
                    "Global Rank diff": st.column_config.NumberColumn(
                        "", width="small"
                    ),
                    "Local Rank diff": st.column_config.NumberColumn("", width="small"),
                    "Performance Points diff": st.column_config.TextColumn(
                        "", width="small"
                    ),
                    "Global Top % diff": st.column_config.TextColumn("", width="small"),
                    "Local Top % diff": st.column_config.TextColumn("", width="small"),
                    "🥇 diff": st.column_config.TextColumn("", width="small"),
                    "🥈 diff": st.column_config.TextColumn("", width="small"),
                    "🥉 diff": st.column_config.TextColumn("", width="small"),
                    "Completed Levels diff": st.column_config.TextColumn(
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
                                f"{pp_formula(i)} " + _("pp") for i in range(1, 101)
                            ],
                        }
                    )
                    st.dataframe(
                        df.drop(columns=[_("Performance Points")]).rename(
                            columns={
                                _("Performance Points pp"): _("Performance Points")
                            }
                        ),
                        hide_index=True,
                        use_container_width=True,
                    )

                with split[2]:
                    fig = px.line(df, x=_("Rank"), y=_("Performance Points"))
                    st.plotly_chart(fig, use_container_width=True)

        with tab2:
            df_first_records = query_df_first_records()
            df_first_records.rename(
                columns={
                    "level_name": "Level",
                    "level_id": "Level ID",
                    "username": "Player",
                    "user_id": "User ID",
                    "time": "Time",
                    "upload_time": "Upload Time",
                    "rank_out_of": "Level Records Count",
                },
                inplace=True,
            )
            df_first_records["Player"] = df_first_records["Player"].str.replace(
                "-", "", regex=False
            )

            df_first_records["Upload Time"] = df_first_records["Upload Time"].astype(
                str
            )
            if not df_first_records["Upload Time"].str.endswith(" UTC").all():
                df_first_records["Upload Time"] = (
                    df_first_records["Upload Time"] + " UTC"
                )
            df_first_records["Watch Replay"] = (
                "https://gooberdash.winterpixel.io/?play="
                + df_first_records["Level ID"]
                + "&replay="
                + df_first_records["User ID"]
            )
            df_first_records["Race Ghost"] = (
                "https://gooberdash.winterpixel.io/?play="
                + df_first_records["Level ID"]
                + "&ghost="
                + df_first_records["User ID"]
            )

            display_level_id_value = False
            display_user_id_value = False
            display_records_count_value = False

            checkboxes = st.columns(3)
            with checkboxes[0]:
                display_level_id = st.checkbox(
                    _("Display Level ID"),
                    value=display_level_id_value,
                    key="first_display_level_id",
                )
            with checkboxes[1]:
                display_user_id = st.checkbox(
                    _("Display User ID"),
                    value=display_user_id_value,
                    key="first_display_user_id",
                )
            with checkboxes[2]:
                display_records_count = st.checkbox(
                    _("Display Records Count"),
                    value=display_records_count_value,
                    key="first_display_records_count",
                )

            column_order_config = [
                "Level",
                "Level ID",
                "Player",
                "User ID",
                "Time",
                "Upload Time",
                "Level Records Count",
                "Watch Replay",
                "Race Ghost",
            ]
            if not display_level_id:
                try:
                    column_order_config.remove("Level ID")
                except Exception:
                    pass
            if not display_user_id:
                try:
                    column_order_config.remove("User ID")
                except Exception:
                    pass
            if not display_records_count:
                try:
                    column_order_config.remove("Level Records Count")
                except Exception:
                    pass
            st.dataframe(
                data=df_first_records,
                use_container_width=True,
                column_order=tuple(column_order_config),
                column_config={
                    "Level": st.column_config.TextColumn(_("Level")),
                    "Level ID": st.column_config.ListColumn(_("Level ID")),
                    "Player": st.column_config.TextColumn(_("Player")),
                    "User ID": st.column_config.ListColumn(_("User ID")),
                    "Time": st.column_config.NumberColumn(
                        _("Time"), format="%f " + _("s")
                    ),
                    "Upload Time": st.column_config.TextColumn(_("Upload Time")),
                    "Level Records Count": st.column_config.NumberColumn(
                        _("Level Records Count")
                    ),
                    "Watch Replay": st.column_config.LinkColumn(
                        _("Watch Replay"), display_text="▶️", width="small"
                    ),
                    "Race Ghost": st.column_config.LinkColumn(
                        _("Race Ghost"), display_text="👻", width="small"
                    ),
                },
                hide_index=True,
            )

        with tab3:
            df_first_records_2 = (
                df_first_records.groupby(["Player"]).size().reset_index(name="Counts")
            )
            fig = px.pie(
                df_first_records_2,
                values=df_first_records_2["Counts"],
                names=df_first_records_2["Player"],
                labels=df_first_records_2["Player"],
                hole=0.4,
            )
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(
                annotations=[
                    {
                        "text": f"{level_counts} "
                        + _("Levels")
                        + f"<br>{len(df_first_records_2.index)} "
                        + _("WR Holders")
                        + f"<br>{df_first_records_2['Counts'].sum()} "
                        + _("WRs"),
                        "showarrow": False,
                    }
                ]
            )
            st.plotly_chart(fig, use_container_width=True)

    except Exception as e:
        print(e)
        time.sleep(3)
