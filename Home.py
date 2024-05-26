import streamlit as st
from threading import Thread
from common_config import common_config
from backend.GooberDash.update_time_trails_leaderboard import update_leaderboard as GooberDash_update_time_trails_leaderboard

def load_website():
    common_config()
    st.write('This is the index_page')


t1 = Thread(target=load_website())
t2 = Thread(target=GooberDash_update_time_trails_leaderboard())

t1.start()
t2.start()

t1.join()
t2.join()
