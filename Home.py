import streamlit as st
import time
from threading import Thread
from common_config import common_config

# from pages.GooberDash.Backend.update_time_trails_leaderboard import update_leaderboard as GooberDash_update_time_trails_leaderboard

common_config()


def load_website():
    st.markdown(
        '<div class="container" style="margin: auto; max-width: 550px; display: flex; padding: 1.5rem 0; justify-content: center;"><img src="https://winterpixelgames.com/static/images/streamlit_banner_v2.png" style="max-height: 100%; max-width: 100%"></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span id="welcome" style="font-weight: 800; text-align: center; display: inline-block; width: 100%; padding: .8rem 0 0 0;"><span style="display: inline-block;">Welcome to :blue-background[WinterPixelGames]&nbsp;!</span><span style="display: inline-block;">A website which provides useful Tools & Statistics of games made by [Winterpixel Games](https://www.winterpixel.com/)</span></span>',
        unsafe_allow_html=True,
    )
    st.html(
        """
    <style>
        #welcome a {
            text-decoration: none;
        }
        .row-widget.stButton {
            display: flex;
            justify-content: center;
        }
        div[data-testid="column"] {
            display: inline-block !important;
        }
        div[data-testid="stHorizontalBlock"] div button { 
            border: none;
            background: transparent;
            padding: 2vh;
            margin: 8px;
        }
        div[data-testid="stHorizontalBlock"] div button:hover { 
            border: none !important;
            box-shadow: 0 0 0px transparent !important;
        }
        div[data-testid="stHorizontalBlock"] div button:active { 
            background: transparent;
        }
        div[data-testid="stHorizontalBlock"] div button p:hover:before { 
            box-shadow: 0 0 30px #158fd8;
        }
        @media screen and (min-width: 1100px) and (orientation: landscape) {
            #welcome {
                padding-top: 4rem !important;
                font-size: 2vw !important;
            } 
            div[data-testid="stHorizontalBlock"] { 
                padding-top: 4rem !important;
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:after { 
                content: "Rocket Bot Royale" !important;
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:after { 
                content: "Goober Dash" !important;
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(3) button:after { 
                content: "Goober Royale" !important;
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(4) button:after { 
                content: "Goober Shot" !important;
            }
            div[data-testid="stHorizontalBlock"] > div:nth-child(5) button:after { 
                content: "Moonrock Miners" !important;
            }
        }
        div[data-testid="stHorizontalBlock"] div button:hover:after { 
            position: relative;
            top: 15rem;
            font-family: 'Baloo 2';
            font-weight: 700;
            font-size: 2rem;
        }
        div[data-testid="stHorizontalBlock"] div button p:before { 
            border: 5px solid #0196ee;
            max-width: 25vw;
            border-radius: 2.8rem;
            background-size: 100%;
            display: flex;
            justify-content: center;
            overflow: hidden;
            content: "";
            position: absolute;
            width: 80%;
            bottom: auto;
            left: 50%;
            top: 10%;
            transform: translateX(-50%) scale(0.9);
            aspect-ratio: 1/1;
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
    """
    )
    col1, col2, col3, col4, col5 = st.columns(5)
    if col1.button("​", key="RBR"):
        st.switch_page("pages/1 Rocket Bot Royale.py")

    if col2.button("​", key="GD"):
        st.switch_page("pages/2 Goober Dash.py")

    if col3.button("​", key="GR"):
        st.switch_page("pages/3 Goober Royale.py")

    if col4.button("​", key="GS"):
        st.switch_page("pages/4 Goober Shot.py")

    if col5.button("​", key="MM"):
        st.switch_page("pages/5 Moonrock Miners.py")


t1 = Thread(target=load_website())
# t2 = Thread(target=GooberDash_update_time_trails_leaderboard())

t1.start()
t1.join()

# t2.start()
# t2.join()
