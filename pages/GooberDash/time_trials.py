import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import websocket
import json
import requests
import time
import os
from replit import db
from pathlib import Path

email = os.environ['email']
password = os.environ['password']


def refresh_token(email, password):
    data = {
        "email": email,
        "password": password,
        "vars": {
            "client_version": "99999",
        },
    }

    headers = {
        "authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="
    }

    try:
        response = requests.post(
            "https://gooberdash-api.winterpixel.io/v2/account/authenticate/email?create=false",
            data=json.dumps(data),
            headers=headers,
        )
        token = json.loads(response.content)["token"]
        return token
    except Exception:
        print("Invalid credentials!")


def list_levels():
    try:
        token = str(refresh_token(email, password))
        ws1 = websocket.create_connection(
            "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="
            + token)
        levels_query = {
            "cid": "6",
            "rpc": {
                "id": "levels_query_curated",
                "payload": "{}"
            }
        }
        ws1.send(json.dumps(levels_query).encode())
        ws1.recv()
        msg1 = ws1.recv()
        output = json.loads(msg1)
        ws1.close()

        output2 = json.loads(output["rpc"]["payload"])

        race_dict = dict()

        for level in output2["levels"]:
            if level["game_mode"] == "Race":
                race_dict[level["id"]] = level["name"]

        return race_dict
    except Exception as e:
        print(e)


def load_page():
    try:
        race_dict = list_levels()
        time.sleep(2)
        
        df = pd.DataFrame(
            np.asarray(json.loads(db["df"])),
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

        st.markdown("## :blue[Goober] :red[Dash]")
        st.markdown(
            '<img style="display: inline; margin: 0 5px 8px 0; width: 25px" src="https://winterpixelgames.com/static/images/medal_1st.png"><span style="font-size: 25px">World Records Statistics</span>',
            unsafe_allow_html=True)
        st.caption("Update every 6 hours")
        tab1, tab2, tab3 = st.tabs([
            "🥇 All Records (WR Holders)",
            "🌟 Hall of Fame (Top 3)",
            "🗒️ Distribution (Pie Chart)",
        ])

        with tab1:
            st.dataframe(df2.set_index(df2.columns[0]))

        with tab2:
            df3 = df.groupby(["Rank",
                              "Player"]).size().reset_index(name="Counts")
            df3 = df3.pivot(index="Player", columns="Rank", values="Counts")
            df3 = df3.fillna(0)
            df3 = df3.rename(columns={
                "Player": "Player",
                "1": "🥇",
                "2": "🥈",
                "3": "🥉"
            })
            df3["Rank"] = df3[["🥇", "🥈", "🥉"]].apply(tuple, axis=1).rank(
                method='min', ascending=False).astype(int)
            df3 = df3.reset_index()
            df3.set_index("Rank", inplace=True)
            df3 = df3.sort_values("Rank")
            df3.loc[:, "Total"] = df3.sum(numeric_only=True, axis=1)
            st.dataframe(df3)

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
            fig.update_layout(annotations=[
                dict(
                    text=
                    f"{len(race_dict)} Levels<br>{len(df2.index)} WR Holders<br>{df2['Counts'].sum()} WRs",
                    showarrow=False,
                )
            ])
            st.plotly_chart(fig, use_container_width=True)
        st.text(
            "WinterPixelGames.com is not affiliated with or endorsed by WinterpixelGames Inc."
        )
        st.text("All relevant trademarks belong to their respective owners.")
    except Exception as e:
        print(e)
        time.sleep(3)
