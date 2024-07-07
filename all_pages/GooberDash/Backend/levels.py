import json
import requests
import datetime
import re


def download_level(level_id):
    try:
        with open("../storage/goober_dash_token.txt", "r") as f:
            token = f.readline()  # goober_dash_token

        headers = {"authorization": f"Bearer {token}"}

        response = requests.post(
            "https://gooberdash-api.winterpixel.io/v2/rpc/levels_editor_get",
            data='"{\\"id\\":\\"' + level_id + '\\"}"',
            headers=headers,
        )
        payload = json.loads(response.content)["payload"]
        response = json.loads(payload)
        return response

    except Exception as e:
        print(e)


def upload_level(response, output):
    try:
        with open("../storage/goober_dash_token.txt", "r") as f:
            token = f.readline()  # goober_dash_token

        headers = {"authorization": f"Bearer {token}"}
        current_time = str(int(datetime.datetime.now().timestamp()))
        level_name = response["name"]
        game_mode = response["game_mode"]
        level_name = response["name"]
        player_count = str(response["player_count"])
        theme = response["theme"]
        nodes = (
            str(json.loads(output)["nodes"])
            .replace("'", '\\\\\\"')
            .replace(" ", "")
            .replace("True", "true")
            .replace("False", "false")[1:-1]
        )

        data = (
            '"{\\"engine_version\\":2,\\"game_mode\\":\\"'
            + game_mode
            + '\\",\\"level_data\\":\\"{\\\\\\"metadata\\\\\\":{\\\\\\"author_id\\\\\\":\\\\\\"e3552f30-35cc-4cee-a70e-bc0607016cad\\\\\\",\\\\\\"author_name\\\\\\":\\\\\\"ToeBiter\\\\\\",\\\\\\"game_mode\\\\\\":\\\\\\"'
            + game_mode
            + '\\\\\\",\\\\\\"id\\\\\\":\\\\\\"\\\\\\",\\\\\\"name\\\\\\":\\\\\\"'
            + level_name
            + " flipped "
            + current_time
            + '\\\\\\",\\\\\\"player_count\\\\\\":'
            + player_count
            + ',\\\\\\"published\\\\\\":\\\\\\"Private\\\\\\",\\\\\\"rating\\\\\\":0,\\\\\\"rating_count\\\\\\":0,\\\\\\"theme\\\\\\":\\\\\\"'
            + theme
            + '\\\\\\",\\\\\\"type\\\\\\":0},\\\\\\"nodes\\\\\\":['
            + nodes
            + ']}\\",\\"level_name\\":\\"'
            + level_name
            + " flipped "
            + current_time
            + '\\",\\"level_theme\\":\\"'
            + theme
            + '\\",\\"player_count\\":'
            + player_count
            + ',\\"pub_state\\":\\"Private\\",\\"world_idx\\":0}"'.replace(" ", "")
        )
        data = re.sub(r"[^\x00-\x7F]+", "", data)
        response2 = requests.post(
            "https://gooberdash-api.winterpixel.io/v2/rpc/levels_editor_create",
            data=data,
            headers=headers,
        )
        payload = json.loads(response2.content)["payload"]
        uuid = json.loads(payload)["uuid"]
        return uuid

    except Exception as e:
        print(e)
