import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import datetime

conn = st.connection("postgresql", type="sql")


def load_page():
    try:
        dataframe = np.load("../storage/dataframe.npy")

        with open("../storage/last_update.txt", "r") as f:
            last_update = float(f.readline())

        with open("../storage/level_counts.txt", "r") as f:
            level_counts = int(f.readline())

        df = pd.DataFrame(
            np.asarray(dataframe),
            columns=[
                "Level",
                "Rank",
                "Player",
                "Record (in seconds)",
                "Upload time (in UTC)",
            ],
        )
        df2 = df[df["Rank"] == "1"]
        df2 = df2.drop("Rank", axis=1)
        df2 = df2.sort_values(by=["Upload time (in UTC)"], ascending=False)

        st.image(
            "static/goober_dash_logo_text.png",
            width=280,
        )
        st.html(
            '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-flag-checkered" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Time Trials<br><img style="display: inline; margin: 0 5px 8px 0; width: 25px" src="./app/static/medal_1st.png">World Records Statistics<span>'
        )
        st.caption(
            f"Last Update: {datetime.datetime.fromtimestamp(last_update).strftime('%Y-%m-%d %H:%M:%S')} UTC (Update every 6 hours)"
        )
        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🥇 All Records (WR Holders)",
                "🌟 Hall of Fame (Top 3)",
                "🥧 Distribution (Pie Chart)",
                "🏆 Time Trials Points Leaderboard",
            ]
        )

        with tab1:
            st.dataframe(df2, use_container_width=True, height=500, hide_index=True)

        with tab2:
            df3 = df.groupby(["Rank", "Player"]).size().reset_index(name="Counts")
            df3 = df3.pivot(index="Player", columns="Rank", values="Counts")
            df3 = df3.fillna(0)
            df3 = df3.rename(
                columns={"Player": "Player", "1": "🥇", "2": "🥈", "3": "🥉"}
            )
            df3["Rank"] = (
                df3[["🥇", "🥈", "🥉"]]
                .apply(tuple, axis=1)
                .rank(method="min", ascending=False)
                .astype(int)
            )
            df3 = df3.reset_index()
            df3.set_index("Rank", inplace=True)
            df3 = df3.sort_values("Rank")
            df3.loc[:, "Total"] = df3.sum(numeric_only=True, axis=1)
            st.dataframe(df3, height=500)

        with tab3:
            df2 = df2.groupby(["Player"]).size().reset_index(name="Counts")
            fig = px.pie(
                df2,
                values=df2["Counts"],
                names=df2["Player"],
                labels=df2["Player"],
                hole=0.4,
            )
            fig.update_traces(textposition="inside", textinfo="percent+label")
            fig.update_layout(
                annotations=[
                    {
                        "text": f"{level_counts} Levels<br>{len(df2.index)} WR Holders<br>{df2['Counts'].sum()} WRs",
                        "showarrow": False,
                    }
                ]
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab4:
            df_leaderboard = conn.query(
                "SELECT * FROM goober_dash_time_trials_leaderboard"
            )

            top_menu = st.columns(3)
            with top_menu[0]:
                sort = st.radio(
                    "Sort Data", options=["Yes", "No"], horizontal=1, index=1
                )
            if sort == "Yes":
                with top_menu[1]:
                    sort_field = st.selectbox("Sort By", options=df_leaderboard.columns)
                with top_menu[2]:
                    sort_direction = st.radio(
                        "Direction", options=["⬆️", "⬇️"], horizontal=True
                    )
                df_leaderboard = df_leaderboard.sort_values(
                    by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True
                )
            pagination = st.container()

            bottom_menu = st.columns((4, 1, 1))
            with bottom_menu[2]:
                batch_size = st.selectbox("Page Size", options=[25, 50, 100])
            with bottom_menu[1]:
                total_pages = (
                    int(len(df_leaderboard) / batch_size)
                    if int(len(df_leaderboard) / batch_size) > 0
                    else 1
                )
                current_page = st.number_input(
                    "Page", min_value=1, max_value=total_pages, step=1
                )
            with bottom_menu[0]:
                st.markdown(f"Page **{current_page}** of **{total_pages}** ")

    except Exception as e:
        print(e)
        time.sleep(3)
