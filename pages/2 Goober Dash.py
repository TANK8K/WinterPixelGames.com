import streamlit as st
import webbrowser
from common_config import common_config

common_config()


def load_page1():
    from pages.GooberDash.time_trials import load_page as GooberDash_time_trials
    st.empty()
    GooberDash_time_trials()


def load_page2():
    from pages.GooberDash.page2 import main
    st.empty()
    main()

def goober_dash_main_page():
    st.write("<h3><i class='fa-solid fa-list'></i>&nbsp;About</h3>", unsafe_allow_html=True)
    st.markdown(
        'Goober Dash is a multiplayer battle royale game that you can play online. Dash your opponents into deadly spikes, gather precious coins, and unlock a plethora of unique costumes as you strive to outlast the competition. Invite your friends to engage in epic battles in custom private lobbies. Unleash your creativity with the level editor, crafting and conquering your very own battlegrounds. Climb the global and country-based seasonal leaderboards to prove your dominance in this thrilling contest.'
    )
    
    if st.button('Play on browser'):
        webbrowser.open_new_tab('https://gooberdash.winterpixel.io')
    
    st.divider()
    st.write("<h3><i class='fa-solid fa-screwdriver-wrench'></i>&nbsp;Tools</h3>", unsafe_allow_html=True)
    st.button('Flip Level', on_click=load_page2)
    st.divider()
    st.write("<h3><i class='fa-solid fa-chart-simple'></i>&nbsp;Statistics</h3>", unsafe_allow_html=True)
    st.button('Time Trials', on_click=load_page1)

goober_dash_main_page()