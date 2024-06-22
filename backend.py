import streamlit as st
import time
import requests
import json
import threading
from all_pages.GooberDash.Backend.time_trials_sql import (
    update_leaderboard as GooberDash_update_time_trials_leaderboard,
)

email = st.secrets.goober_dash_credentials.email
password = st.secrets.goober_dash_credentials.password


def run_threaded_functions(functions):
    threads = []

    for func in functions:
        thread = threading.Thread(target=func_wrapper, args=(func,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def func_wrapper(func):
    try:
        func()
    except Exception as e:
        print(f"Error in function {func.__name__}: {e}")


def clear_cache():
    while True:
        try:
            st.cache_resource.clear()
            time.sleep(10800)
        except Exception as e:
            print(f"Failed to clear cache: {e}")
            time.sleep(5)


def refresh_goober_dash_token():
    while True:
        try:
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

            response = requests.post(
                "https://gooberdash-api.winterpixel.io/v2/account/authenticate/email?create=false",
                data=json.dumps(data),
                headers=headers,
            )
            token = json.loads(response.content)["token"]

            with open("../storage/goober_dash_token.txt", "w") as f:
                f.write(token)

            time.sleep(540)
        except Exception as e:
            print(f"Failed to refresh token: {e}")
            time.sleep(5)


if __name__ == "__main__":
    run_threaded_functions(
        [
            GooberDash_update_time_trials_leaderboard,
            refresh_goober_dash_token,
            clear_cache,
        ]
    )
