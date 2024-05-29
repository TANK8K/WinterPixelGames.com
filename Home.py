import streamlit as st
import time
from threading import Thread
from common_config import common_config
from pages.GooberDash.Backend.update_time_trails_leaderboard import update_leaderboard as GooberDash_update_time_trails_leaderboard

common_config()

def load_website():
    st.markdown('<div class="container" style="margin: auto; max-width: 550px; display: flex; padding: 1.5rem 0; justify-content: center;"><img src="https://winterpixelgames.com/static/images/streamlit_banner_v2.png" style="max-height: 100%; max-width: 100%"></div>', unsafe_allow_html=True)
    st.markdown(
        '<span style="text-align: center; font-size: 1.6rem; display: inline-block; width: 100%; padding: .8rem 0;">Welcome to **:blue-background[WinterPixelGames]**, a website which provides useful **Tools & Statistics** of games made by **[Winterpixel Games](https://www.winterpixel.com/)**!</span>', unsafe_allow_html=True
    )
    st.html("""
    <style>
        .row-widget.stButton {
          display: flex;
          justify-content: center;
        }
        div[data-testid="stHorizontalBlock"] button:hover {
            background-color: #183d65;
            transition: .2s ease-in-out;
            -wenkit-transition: .2s ease-in-out;
        }
        div[data-testid="stHorizontalBlock"] button {
            border: 2px solid #0196ee !important;
            border-radius: 10px !important;
            width: 95% !important;
            min-height: 30vh !important;
            box-shadow: 0 0 10px #158fd8;
        }
        div[data-testid="stHorizontalBlock"] button p {
            font-weight: 700 !important;
            font-size: 1.5em !important;
            top: 7rem;
        }
        div[data-testid="stHorizontalBlock"] button p::before { 
            content: "";
            background-size: 100% 100%;
            display: block;
            margin: auto;
            justify-content: center;
            height: 5em;
            width: 5em;
            overflow: hidden;
            position: relative;
            margin-top: 10px;
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) button p::before { 
            background-image: url("https://winterpixelgames.com/static/images/rocket_bot_royale_favicon.png");
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) button p::before { 
            background-image: url("https://winterpixelgames.com/static/images/goober_dash_favicon.png");
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(3) button p::before { 
            background-image: url("https://winterpixelgames.com/static/images/goober_royale_favicon.png");
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(4) button p::before { 
            background-image: url("https://winterpixelgames.com/static/images/goober_shot_favicon.png");
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(5) button p::before { 
            background-image: url("https://winterpixelgames.com/static/images/moonrock_miners_favicon.png");
        }
    </style>
    """)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("Rocket Bot Royale"):
            st.switch_page("pages/1 Rocket Bot Royale.py")

    with col2:
        if st.button("Goober Dash"):
            st.switch_page("pages/2 Goober Dash.py")

    with col3:
        if st.button("Goober Royale"):
            st.switch_page("pages/3 Goober Royale.py")

    with col4:
        if st.button("Goober Shot"):
            st.switch_page("pages/4 Goober Shot.py")

    with col5:
        if st.button("Moonrock Miners"):
            st.switch_page("pages/5 Moonrock Miners.py")
        
t1 = Thread(target=load_website())
t2 = Thread(target=GooberDash_update_time_trails_leaderboard())

t1.start()
t1.join()

t2.start()
t2.join()