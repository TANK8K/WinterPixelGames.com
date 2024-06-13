import streamlit as st
import time
import requests
import json
from threading import Thread
from pages.GooberDash.Backend.time_trials_sql import (
    update_leaderboard as GooberDash_update_time_trials_leaderboard,
)

email = st.secrets.goober_dash_credentials.email
password = st.secrets.goober_dash_credentials.password


def refresh_goober_dash_token():
    while True:
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

            with open("../storage/goober_dash_token.txt", "w") as f:
                f.write(token)
        except Exception:
            print("Invalid credentials!")

        time.sleep(540)


def clear_cache():
    while True:
        st.cache_data.clear()
        st.cache_resource.clear()
        time.sleep(21600)


def run_threaded_functions(functions):
    threads = []
    for func in functions:
        thread = Thread(target=func)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    run_threaded_functions(
        [
            GooberDash_update_time_trials_leaderboard,
            refresh_goober_dash_token,
            clear_cache,
        ]
    )
    # run_threaded_functions(
    #    [GooberDash_update_time_trials_leaderboard, refresh_goober_dash_token]
    # )
