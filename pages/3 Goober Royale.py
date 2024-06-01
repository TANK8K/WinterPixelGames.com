import streamlit as st
from common_config import common_config, back_to_home, back_to_menu

common_config()

try:
    if st.session_state.game != "GooberRoyale":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "GooberRoyale"


def to_user_info_page():
    st.session_state.page = "user_info"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "GooberRoyale" and st.session_state.page == "menu":
    with ph.container():
        st.html(
            """<style>
                    div[data-testid="column"] {
                        width: fit-content !important;
                        flex: unset;
                    }
                    div[data-testid="column"] * {
                        width: fit-content !important;
                    }
                    div[data-testid="stVerticalBlock"] p::before {
                        display: inline-block;
                        vertical-align: middle;
                        font-weight: 900;
                        font-size: 20px;
                        color: white;
                        padding-right: 5px;
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(6) > div:nth-child(1) p::before {
                        font-family: "Font Awesome 5 Free" !important;
                        content: "\\f0ac";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(8) > div:nth-child(1) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f392";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(11) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f007";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(11) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f073";
                    }
                    </style>"""
        )
        st.markdown(
            """
            <div style="margin: auto; max-width: 350px; display: flex; padding-bottom: 15px; justify-content: center;">
                <img src="https://winterpixelgames.com/static/images/goober_royale_logo_text.png" style="max-height: 100%; max-width: 100%">
            </div>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            """**Goober Royale** is a multiplayer battle royale game in which each player controls a character (called a "goober") and must collect weapons, power-ups and other items to eliminate their opponents. The clashes bring together 16 players on a map and the objective will be to be the last survivor of the game. You can play alone or in a team of 4 players. Your Goober will have several weapons, a main missile that reloads at regular intervals and a secondary accessory such as mines, a tornado, a drill and many others. Also use your jetpack to move around the map more easily, reach high places and surprise your opponents. Completing games and missions will earn you gold coins that you can spend either to improve your Goober's skills or to buy cosmetics that will give your character a unique style. An online ranking will allow you to see the 100 best players in the world and in your region."""
        )
        st.warning(
            "**Goober Royale** is in **beta** currently. (Bugs are expected and Data may be reset in future)",
            icon="⚠️",
        )
        st.html("<h4>Platforms</h4>")
        col1, col2 = st.columns(2)
        col1.link_button("Browser", "https://gooberroyale.winterpixel.io")
        st.html("<h4>Communities</h4>")
        col1, col2 = st.columns(2)
        col1.link_button("Discord", "https://discord.com/invite/kdGuBhXz2r")
        "---"
        st.html("<h3><i class='fa-solid fa-chart-simple'></i>&nbsp;Statistics</h3>")
        col1, col2 = st.columns(2)
        col1.button("User Info (WIP)", on_click=to_user_info_page, type="primary")
        col2.button(
            "Season Leaderboard (WIP)",
            on_click=to_season_leaderboard_page,
            type="primary",
        )
        back_to_home()

elif st.session_state.game == "GooberRoyale" and st.session_state.page == "user_info":
    with ph.container():
        from pages.GooberRoyale.Statistics.user_info import (
            load_page as GooberRoyale_user_info,
        )

        GooberRoyale_user_info()
        back_to_menu()

elif (
    st.session_state.game == "GooberRoyale"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from pages.GooberRoyale.Statistics.season_leaderboard import (
            load_page as GooberRoyale_season_leaderboard,
        )

        GooberRoyale_season_leaderboard()
        back_to_menu()
