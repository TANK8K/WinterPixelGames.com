import streamlit as st
import time
from threading import Thread
from pages.GooberDash.Backend.time_trials_sql import (
    update_leaderboard as GooberDash_update_time_trials_leaderboard,
)


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
    run_threaded_functions([GooberDash_update_time_trials_leaderboard, clear_cache])
