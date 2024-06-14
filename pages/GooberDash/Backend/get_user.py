import streamlit as st
import websocket
import json
import requests
import re

# crushers
# 2 6 5 4 3 1

# pancake
# left 40 67 83
# right 33 62 95
email = st.secrets.goober_dash_credentials.email
password = st.secrets.goober_dash_credentials.password

with open("../storage/goober_dash_token.txt", "r") as f:
    token = f.readline()  # goober_dash_token

# async def refresh_config():
#    """Refresh Goober Dash game configuration"""
#
#    global goober_dash_server_config
#
#    response = await goober_dash_client.get_config()
#    goober_dash_server_config = response
#
#    global goober_dash_current_season
#
#    duration, start_number, start_time = ([] for i in range(3))
#    for key in goober_dash_server_config["metadata"]["seasons"]["season_templates"]:
#        duration.append(key["duration"])
#        start_number.append(key["start_number"])
#        start_time.append(key["start_time"])
#
#    def get_current_season(current_timestamp):
#        index = np.searchsorted(start_time, current_timestamp)
#        accumulate_start_time = start_time[index - 1]
#        count = 0
#        while accumulate_start_time <= current_timestamp:
#            accumulate_start_time += duration[index - 1]
#            count += 1
#        current_season = start_number[index - 1] + count - 1
#        return current_season
#
#    goober_dash_current_season = get_current_season(time.time())
#
#
# def goober_dash_season_info(season, mode):
#    duration, start_number, start_time = ([] for i in range(3))
#    for key in goober_dash_server_config["metadata"]["seasons"]["season_templates"]:
#        duration.append(key["duration"])
#        start_number.append(key["start_number"])
#        start_time.append(key["start_time"])
#
#    season_index = np.searchsorted(start_number, season + 1) - 1
#
#    season_start_timestamp = (
#        start_time[season_index]
#        + (season - start_number[season_index]) * duration[season_index]
#    )
#    season_start = f"{datetime.datetime.utcfromtimestamp(season_start_timestamp):%Y-%m-%d %H:%M:%S} UTC"
#
#    season_end_timestamp = season_start_timestamp + duration[season_index]
#    season_end = f"{datetime.datetime.utcfromtimestamp(season_end_timestamp):%Y-%m-%d %H:%M:%S} UTC"
#
#    season_duration = duration[season_index]
#
#    if mode == "long":
#        season_days = f"{season_duration // (24 * 3600)} days {season_duration % (24 * 3600) // 3600} hours"
#    elif mode == "short":
#        s = season_duration / (24 * 3600)
#        season_days = f"{'{:.2f}'.format(s) if s%1 != 0 else int(s)} days"
#
#    current_timestamp = time.time()
#    if current_timestamp > season_end_timestamp:
#        status = "\u001b[2;31mEnded\u001b[0m"
#    else:
#        status = f"\u001b[2;32mIn progress\u001b[0m ({((current_timestamp - season_start_timestamp)/season_duration)*100:.0f} %)"
#
#    if season == goober_dash_current_season:
#        season_difference = (
#            current_timestamp - season_start_timestamp
#        ) / season_duration
#        season_seconds_remaining = (
#            ceil(season_difference) - season_difference
#        ) * season_duration
#        day = season_seconds_remaining // (24 * 3600)
#        hour = season_seconds_remaining % (24 * 3600) // 3600
#        minute = season_seconds_remaining % (24 * 3600) % 3600 // 60
#        second = season_seconds_remaining % (24 * 3600) % 3600 % 60
#        time_remaining = f"{int(day)}d {int(hour)}h {int(minute)}m {int(second)}s"
#    else:
#        time_remaining = ""
#
#    goober_dash_all_season_info = [
#        season_start,
#        season_end,
#        season_days,
#        status,
#        time_remaining,
#    ]
#    return goober_dash_all_season_info
#
#
# def refresh_token():
#    data = {
#        "email": email,
#        "password": password,
#        "vars": {
#            "client_version": "99999",
#        },
#    }
#
#    headers = {"authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="}
#
#    try:
#        response = requests.post(
#            "https://gooberdash-api.winterpixel.io/v2/account/authenticate/email?create=false",
#            data=json.dumps(data),
#            headers=headers,
#        )
#        token = json.loads(response.content)["token"]
#        return token
#    except Exception:
#        print("Invalid credentials!")
#
#
# def get_user():
#    try:
#        token = str(refresh_token())
#        ws1 = websocket.create_connection(
#            "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token=" + token
#        )
#        levels_query = {
#            "cid": "6",
#            "rpc": {"id": "levels_query_curated", "payload": "{}"},
#        }
#        ws1.send(json.dumps(levels_query).encode())
#        ws1.recv()
#        msg1 = ws1.recv()
#        output = json.loads(msg1)
#        ws1.close()
#        output2 = json.loads(output["rpc"]["payload"])
#        race_dict = {}
#
#        for level in output2["levels"]:
#            if level["game_mode"] == "Race":
#                race_dict[level["id"]] = level["name"]
#        return race_dict
#    except Exception as e:
#        print(e)
#
#
# async def query_leaderboard(
#    self,
#    season: int,
#    leaderboard_id: str,
#    limit: int = 100,
#    cursor: str = "",
#    owner_ids: str = "",
# ):
#    await self.refresh_token()
#
#    headers = {"authorization": f"Bearer {self.token}"}
#
#    url = "https://gooberdash-api.winterpixel.io/v2/leaderboard/"
#    url += f"{leaderboard_id}.{season}"
#    url += f"?limit={limit}"
#    url += f"&cursor={cursor}" if cursor != "" else ""
#    url += f"&owner_ids={owner_ids}" if owner_ids != "" else ""
#
#    return json.loads(
#        await self.get(
#            url,
#            headers=headers,
#        )
#    )


def user_info(user_id: str):
    ws = websocket.create_connection(
        f"wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token={token}"
    )
    query_player_profile = {
        "rpc": {
            "id": "query_player_profile",
            "payload": '{"user_id": "' + user_id + '"}',
        }
    }

    ws.send(json.dumps(query_player_profile).encode())
    ws.recv()
    msg = ws.recv()
    try:
        player_info = json.loads(msg)["rpc"]["payload"]
    except KeyError:
        return "invalid_user_id"
    return player_info


def user_info_2(username_or_id):
    is_uuid = bool(
        re.compile(
            r"^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$",
            re.IGNORECASE,
        ).match(username_or_id)
    )

    headers = {"authorization": f"Bearer {token}"}

    query_url = "https://gooberdash-api.winterpixel.io/v2/user" + (
        f"?ids={username_or_id}" if is_uuid else f"?usernames={username_or_id}"
    )
    response = requests.get(
        query_url,
        headers=headers,
    )
    return json.loads(response.content)
