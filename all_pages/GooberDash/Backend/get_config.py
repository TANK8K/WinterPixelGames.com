import streamlit as st
import json
import websocket

email = st.secrets.goober_dash_credentials.email
password = st.secrets.goober_dash_credentials.password


def get_config():
    try:
        with open("../storage/goober_dash_token.txt", "r") as f:
            token = f.readline()  # goober_dash_token
        ws = websocket.create_connection(
            f"wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token={token}"
        )
        player_fetch_data = {"rpc": {"id": "player_fetch_data", "payload": "{}"}}
        ws.send(json.dumps(player_fetch_data).encode())
        ws.recv()
        msg = ws.recv()
        msg_json_loads = json.loads(msg)["rpc"]["payload"]
        server_config = json.loads(msg_json_loads)["data"]
        return server_config
    except Exception as e:
        print(e)
