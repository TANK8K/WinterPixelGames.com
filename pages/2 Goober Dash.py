import streamlit as st
from common_config import common_config
from pages.GooberDash.time_trials import load_page as GooberDash_time_trials

common_config()

def load_page2():
    from pages.GooberDash.page2 import main
    main()

st.sidebar.button('Time Trials', on_click=GooberDash_time_trials)
st.sidebar.button('Page 2', on_click=load_page2)
