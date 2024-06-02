import streamlit as st
from common_config import common_config, back_to_home, back_to_menu

common_config()

try:
    if st.session_state.game != "RocketBotRoyale":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "RocketBotRoyale"


def to_username_changer_page():
    st.session_state.page = "username_changer"


def to_optimize_crate_page():
    st.session_state.page = "optimize_crate"


def to_user_info_page():
    st.session_state.page = "user_info"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "RocketBotRoyale" and st.session_state.page == "menu":
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
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"] p::before {
                        display: inline-block;
                        vertical-align: middle;
                        font-weight: 900;
                        font-size: 20px;
                        color: white;
                        padding-right: 5px;
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(1) p::before {
                        font-family: "Font Awesome 5 Free" !important;
                        content: "\\f0ac";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(2) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f1b6";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(3) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f3ab";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(5) > div:nth-child(4) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f36f";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(7) > div:nth-child(1) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f392";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(7) > div:nth-child(2) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f1b6";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(7) > div:nth-child(3) p::before {
                        font-family: "Font Awesome 5 Free" !important;
                        content: "\\f06d";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(7) > div:nth-child(4) p::before {
                        font-family: "Font Awesome 5 Brands" !important;
                        content: "\\f281";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(10) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f2f9";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(10) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f466";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(14) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f007";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(14) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f073";
                    }
                    </style>"""
        )
        st.image("static/rocket_bot_royale_banner_v2.png")
        st.markdown(
            """**ROCKET BOT ROYALE** is a fun new take on the online battle royale formula. Powerful, wall-climbing, rocket-jumping, artillery-pumping Robo-Tanks are the vehicle of choice in this fast-paced shootout, where the goal is to survive longer than the competition. Collect the loot to upgrade your arsenal, tunnel into the terrain to take cover and collect buried treasure, and avoid the rising water levels to be the blast one standing!"""
        )

        st.html("<h4>Platforms</h4>")
        col1, col2, col3, col4 = st.columns(4)
        col1.link_button("Browser", "https://rocketbotroyale.winterpixel.io")
        col2.link_button(
            "Steam", "https://store.steampowered.com/app/1748390/Rocket_Bot_Royale"
        )
        col3.link_button(
            "Play Store",
            "https://play.google.com/store/apps/details?id=com.winterpixel.rocketbotroyale",
        )
        col4.link_button(
            "App Store",
            "https://apps.apple.com/us/app/rocket-bot-royale/id1585995080",
        )

        st.html("<h4>Communities</h4>")
        col1, col2, col3, col4 = st.columns(4)
        col1.link_button("Discord", "https://discord.com/invite/kdGuBhXz2r")
        col2.link_button("Steam", "https://steamcommunity.com/app/1748390/discussions")
        col3.link_button(
            "Fandom",
            "https://rocketbotroyale.fandom.com/wiki/Rocket_Bot_Royale_Wiki",
        )
        col4.link_button("Reddit", "https://www.reddit.com/r/RocketBotRoyale")
        "---"
        st.html("<h3><i class='fa-solid fa-screwdriver-wrench'></i>&nbsp;Tools</h3>")
        col1, col2 = st.columns(2)
        col1.button(
            "Username Changer", on_click=to_username_changer_page, type="primary"
        )
        col2.button(
            "Optimize Crate (WIP)", on_click=to_optimize_crate_page, type="primary"
        )
        st.warning(
            "Discussions about the **Username Changer** is **NOT** allowed in the **Official Winterpixel Games Discord server** as Moderators **DO NOT APPROVE** it.",
            icon="⚠️",
        )
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

elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "username_changer"
):
    with ph.container():
        from pages.RocketBotRoyale.Tools.username_changer import (
            load_page as RocketBotRoyale_username_changer,
        )

        RocketBotRoyale_username_changer()
        back_to_menu()

elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "optimize_crate"
):
    with ph.container():
        from pages.RocketBotRoyale.Tools.optimize_crate import (
            load_page as RocketBotRoyale_optimize_crate,
        )

        RocketBotRoyale_optimize_crate()
        back_to_menu()

elif (
    st.session_state.game == "RocketBotRoyale" and st.session_state.page == "user_info"
):
    with ph.container():
        from pages.RocketBotRoyale.Statistics.user_info import (
            load_page as RocketBotRoyale_user_info,
        )

        RocketBotRoyale_user_info()
        back_to_menu()

elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from pages.RocketBotRoyale.Statistics.season_leaderboard import (
            load_page as RocketBotRoyale_season_leaderboard,
        )

        RocketBotRoyale_season_leaderboard()
        back_to_menu()
