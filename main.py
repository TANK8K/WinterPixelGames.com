import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import websocket
import json
import requests
import time
import datetime
import flag
import re
import os
from replit import db
from threading import Thread

email = os.environ['email']
password = os.environ['password']

if "df" not in db.keys():
    db["df"] = None


class NumpyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


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


def update_leaderboard():
    while True:
        time.sleep(21601)

        try:
            global data, data_tied, race_dict

            race_dict = list_levels()
            time.sleep(2)
            data = np.empty([len(race_dict), 5], dtype="<U100")
            data_tied = np.empty([0, 5], dtype="<U100")

            token = str(refresh_token(email, password))
            index = 0
            for level_id in race_dict:
                level_name = race_dict[level_id]
                # print(level_name)
                ws2 = websocket.create_connection(
                    "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="
                    + token)

                payload = '{"level_id":"' + str(level_id) + '","limit":50}'
                query_leaderboard = {
                    "cid": "11",
                    "rpc": {
                        "id": "time_trial_query_leaderboard",
                        "payload": f"{payload}"
                    },
                }
                ws2.send(json.dumps(query_leaderboard).encode())
                ws2.recv()
                msg2 = ws2.recv()
                msg2_json_loads = json.loads(msg2)["rpc"]["payload"]
                msg2_json_loads_row = json.loads(msg2_json_loads)

                record_time = float(
                    f"{msg2_json_loads_row['records'][0]['score'] / 100000:.3f}"
                )
                data[index] = [
                    level_name,
                    "1",
                    f"{flag.flag(json.loads(msg2_json_loads_row['records'][0]['metadata'])['country'])}   {re.sub(r'[^A-Za-z0-9 ]+','',msg2_json_loads_row['records'][0]['username']['value'])}",
                    f"   {record_time:.3f}"
                    if int(record_time) < 10 else f"{record_time:.3f}",
                    str(
                        datetime.datetime.fromtimestamp(
                            msg2_json_loads_row["records"][0]["update_time"]
                            ["seconds"])),
                ]

                rank_eq = 1
                rank_index = 1
                while rank_eq == 1 or (rank_index <= 3 and rank_eq <= 3):
                    next_record_time = float(
                        f"{msg2_json_loads_row['records'][rank_index]['score'] / 100000:.3f}"
                    )
                    if next_record_time != record_time:
                        rank_eq += 1
                    if rank_eq == 1 or (rank_index <= 3 and rank_eq <= 3):
                        append_row = [
                            level_name,
                            rank_eq,
                            f"{flag.flag(json.loads(msg2_json_loads_row['records'][rank_index]['metadata'])['country'])}   {re.sub(r'[^A-Za-z0-9 ]+','',msg2_json_loads_row['records'][rank_index]['username']['value'])}",
                            (f"   {next_record_time:.3f}"
                             if int(next_record_time) < 10 else
                             f"{next_record_time:.3f}"),
                            str(
                                datetime.datetime.fromtimestamp(
                                    msg2_json_loads_row["records"][rank_index]
                                    ["update_time"]["seconds"])),
                        ]

                        data_tied = np.vstack([data_tied, [append_row]])
                    rank_index += 1
                    #time.sleep(1)
                    time.sleep(3)

                index += 1
                ws2.close()
                #time.sleep(1)
                time.sleep(5)

            db["df"] = json.dumps(np.vstack([data, data_tied]),
                                  cls=NumpyEncoder)

        except Exception as e:
            print(e)
            pass


def load_website():
    while True:
        try:
            st.set_page_config(
                layout="wide",
                initial_sidebar_state="collapsed",
            )

            insert_html = """
                <link href='https://fonts.googleapis.com/css?family=Baloo 2' rel='stylesheet'>
                <style>
                h1, h2, h3, h4, h5, h6, p {
                    font-family: 'Baloo 2' !important;
                    font-weight: bolder;
                    text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
                }
                header {
                    background: transparent !important;
                }
                [data-testid="stAppViewContainer"] > .main {
                    background-image: url("https://winterpixelgames.com/static/images/background_gd.png");
                    height: 100%; 
                    background-position: center;
                    background-repeat: no-repeat;
                    background-size: cover;
                }
                #stDecoration {
                    display: none;
                }
                .main-svg {
                  border-radius: 10px;
                }
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
            """
            st.markdown(insert_html, unsafe_allow_html=True)

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
                df3 = df3.pivot(index="Player",
                                columns="Rank",
                                values="Counts")
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
                fig.update_traces(textposition="inside",
                                  textinfo="percent+label")

                race_dict = list_levels()

                time.sleep(1)

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
            st.text(
                "All relevant trademarks belong to their respective owners.")
        except Exception as e:
            print(e)
            time.sleep(900)


t1 = Thread(target=load_website())
t2 = Thread(target=update_leaderboard())

t1.start()
t2.start()

t1.join()
t2.join()
