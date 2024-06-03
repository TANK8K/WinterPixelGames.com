import streamlit as st
from threading import Thread
from pages.GooberDash.Backend.update_time_trails_leaderboard import (
    update_leaderboard as GooberDash_update_time_trails_leaderboard,
)

t2 = Thread(target=GooberDash_update_time_trails_leaderboard(email, password))

t2.start()
t2.join()
