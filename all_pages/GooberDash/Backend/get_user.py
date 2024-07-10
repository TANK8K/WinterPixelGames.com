import websocket
import json
import requests
import re


def user_info(user_id: str):
    with open("../storage/goober_dash_token.txt", "r") as f:
        token = f.readline()  # goober_dash_token

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
    return json.loads(player_info)


def user_info_2(username_or_id):
    with open("../storage/goober_dash_token.txt", "r") as f:
        token = f.readline()  # goober_dash_token

    is_uuid = bool(
        re.compile(
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
            re.IGNORECASE,
        ).match(username_or_id)
    )
    print(is_uuid)

    headers = {"authorization": f"Bearer {token}"}

    query_url = "https://gooberdash-api.winterpixel.io/v2/user" + (
        f"?ids={username_or_id}" if is_uuid else f"?usernames={username_or_id}"
    )
    response = requests.get(
        query_url,
        headers=headers,
    )
    return json.loads(response.content)
