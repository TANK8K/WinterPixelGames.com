import numpy as np
import websocket
import json
import requests
import time
import datetime
import flag
import re
import os
import threading
from replit import db

email = "mevavis921@jzexport.com"
password = "b7YPADMh"

if "df" not in db.keys():
    db["df"] = None

if "df_last_update" not in db.keys():
    db["df_last_update"] = None


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

    headers = {"authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="}

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
            "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token=" + token
        )
        levels_query = {
            "cid": "6",
            "rpc": {"id": "levels_query_curated", "payload": "{}"},
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


lock = threading.Lock()


def update_leaderboard():
    with lock:
        while True:
            time.sleep(21601)
            # time.sleep(5)

            try:
                global data, data_tied, race_dict

                race_dict = list_levels()
                time.sleep(10)
                data = np.empty([len(race_dict), 5], dtype="<U100")
                data_tied = np.empty([0, 5], dtype="<U100")

                token = str(refresh_token(email, password))
                index = 0
                for level_id in race_dict:
                    level_name = race_dict[level_id]
                    ws2 = websocket.create_connection(
                        "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="
                        + token
                    )

                    payload = '{"level_id":"' + str(level_id) + '","limit":50}'
                    query_leaderboard = {
                        "cid": "11",
                        "rpc": {
                            "id": "time_trial_query_leaderboard",
                            "payload": f"{payload}",
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
                    print(level_name, "1")
                    data[index] = [
                        level_name,
                        "1",
                        f"{flag.flag(json.loads(msg2_json_loads_row['records'][0]['metadata'])['country'])}   {re.sub(r'[^A-Za-z0-9 ]+','',msg2_json_loads_row['records'][0]['username']['value'])}",
                        (
                            f"   {record_time:.3f}"
                            if int(record_time) < 10
                            else f"{record_time:.3f}"
                        ),
                        str(
                            datetime.datetime.fromtimestamp(
                                msg2_json_loads_row["records"][0]["update_time"][
                                    "seconds"
                                ]
                            )
                        ),
                    ]

                    rank_eq = 1
                    prev_rank_counter = 0
                    rank_index = 1
                    while rank_eq <= 3:
                        next_record_time = float(
                            f"{msg2_json_loads_row['records'][rank_index]['score'] / 100000:.3f}"
                        )
                        if next_record_time != record_time:
                            rank_eq += prev_rank_counter + 1
                            prev_rank_counter = 0
                        else:
                            prev_rank_counter += 1
                        if rank_eq <= 3:
                            print(level_name, rank_eq)
                            append_row = [
                                level_name,
                                rank_eq,
                                f"{flag.flag(json.loads(msg2_json_loads_row['records'][rank_index]['metadata'])['country'])}   {re.sub(r'[^A-Za-z0-9 ]+','',msg2_json_loads_row['records'][rank_index]['username']['value'])}",
                                (
                                    f"   {next_record_time:.3f}"
                                    if int(next_record_time) < 10
                                    else f"{next_record_time:.3f}"
                                ),
                                str(
                                    datetime.datetime.fromtimestamp(
                                        msg2_json_loads_row["records"][rank_index][
                                            "update_time"
                                        ]["seconds"]
                                    )
                                ),
                            ]

                            data_tied = np.vstack([data_tied, [append_row]])
                        rank_index += 1

                    index += 1
                    ws2.close()
                    # time.sleep(1)
                    time.sleep(2)

                db["df"] = json.dumps(np.vstack([data, data_tied]), cls=NumpyEncoder)
                db["df_last_update"] = time.time()

            except Exception as e:
                print(e)
                pass
