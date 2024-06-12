import streamlit as st
from common_config import common_config, back_to_home, back_to_menu


common_config()

try:
    if st.session_state.game != "GooberDash":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "GooberDash"


def to_flip_level_page():
    st.session_state.page = "flip_level"


def to_maze_generator_page():
    st.session_state.page = "maze_generator"


def to_time_trials_certified_levels_page():
    st.session_state.page = "time_trials_certified_levels"


def to_player_info_page():
    st.session_state.page = "player_info"


def to_level_info_page():
    st.session_state.page = "level_info"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "GooberDash" and st.session_state.page == "menu":
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
                        content: "\\f07e";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(10) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f12e";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f11e";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f007";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(3) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f279";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(4) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f073";
                    }
                    </style>"""
        )
        st.image("static/goober_dash_banner_v2.png")
        st.markdown(
            "**GOOBER DASH** is a multiplayer battle royale game that you can play online. Dash your opponents into deadly spikes, gather precious coins, and unlock a plethora of unique costumes as you strive to outlast the competition. Invite your friends to engage in epic battles in custom private lobbies. Unleash your creativity with the level editor, crafting and conquering your very own battlegrounds. Climb the global and country-based seasonal leaderboards to prove your dominance in this thrilling contest."
        )

        st.html("<h4>Platforms</h4>")
        col1, col2, col3, col4 = st.columns(4)
        col1.link_button("Browser", "https://gooberdash.winterpixel.io")
        col2.link_button(
            "Steam", "https://store.steampowered.com/app/2661160/Goober_Dash"
        )
        col3.link_button(
            "Play Store",
            "https://play.google.com/store/apps/details?id=com.winterpixel.gooberdash",
        )
        col4.link_button(
            "App Store", "https://apps.apple.com/us/app/goober-dash/id6470684038"
        )

        st.html("<h4>Communities</h4>")
        col1, col2, col3, col4 = st.columns(4)
        col1.link_button("Discord", "https://discord.com/invite/kdGuBhXz2r")
        col2.link_button("Steam", "https://steamcommunity.com/app/2661160/discussions")
        col3.link_button(
            "Fandom", "https://goober-dash.fandom.com/wiki/Goober_Dash_Wiki"
        )
        col4.link_button("Reddit", "https://www.reddit.com/r/gooberdash")
        "---"
        st.html("<h3><i class='fa-solid fa-screwdriver-wrench'></i>&nbsp;Tools</h3>")
        col1, col2 = st.columns(2)
        col1.button("Flip Level", on_click=to_flip_level_page, type="primary")
        col2.button(
            "Maze Generator (WIP)", on_click=to_maze_generator_page, type="primary"
        )
        "---"
        st.html("<h3><i class='fa-solid fa-chart-simple'></i>&nbsp;Statistics</h3>")
        col1, col2, col3, col4 = st.columns(4)
        col1.button(
            "Time Trials (Certified Levels)",
            on_click=to_time_trials_certified_levels_page,
            type="primary",
        )
        col2.button("Player Info (WIP)", on_click=to_player_info_page, type="primary")
        col3.button("Level Info (WIP)", on_click=to_level_info_page, type="primary")
        col4.button(
            "Season Leaderboard (WIP)",
            on_click=to_season_leaderboard_page,
            type="primary",
        )
        back_to_home()

elif st.session_state.game == "GooberDash" and st.session_state.page == "flip_level":
    with ph.container():
        from pages.GooberDash.Tools.flip_level import load_page as GooberDash_flip_level

        GooberDash_flip_level()
        back_to_menu()

elif (
    st.session_state.game == "GooberDash" and st.session_state.page == "maze_generator"
):
    with ph.container():
        from pages.GooberDash.Tools.maze_generator import (
            load_page as GooberDash_maze_generator,
        )

        GooberDash_maze_generator()
        back_to_menu()

elif (
    st.session_state.game == "GooberDash"
    and st.session_state.page == "time_trials_certified_levels"
):
    with ph.container():
        from pages.GooberDash.Statistics.time_trials_certified_levels import (
            load_page as GooberDash_time_trials_certified_levels,
        )

        GooberDash_time_trials_certified_levels()
        back_to_menu()

elif st.session_state.game == "GooberDash" and st.session_state.page == "player_info":
    with ph.container():
        from pages.GooberDash.Statistics.player_info import (
            load_page as GooberDash_player_info,
        )

        GooberDash_player_info()
        back_to_menu()

elif st.session_state.game == "GooberDash" and st.session_state.page == "level_info":
    with ph.container():
        from pages.GooberDash.Statistics.level_info import (
            load_page as GooberDash_level_info,
        )

        GooberDash_level_info()
        back_to_menu()

elif (
    st.session_state.game == "GooberDash"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from pages.GooberDash.Statistics.season_leaderboard import (
            load_page as GooberDash_season_leaderboard,
        )

        GooberDash_season_leaderboard()
        back_to_menu()
