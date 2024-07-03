import streamlit as st
from common_config import (
    back_to_home,
    back_to_menu,
    set_localization,
    footer_account_language,
)

_ = set_localization(st.session_state.language)
footer_account_language(st.session_state.language)

try:
    if st.session_state.game != "GooberShot":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "GooberShot"


def to_image_assets_page():
    st.session_state.page = "image_assets"


def to_player_info_page():
    st.session_state.page = "player_info"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "GooberShot" and st.session_state.page == "menu":
    with ph.container():
        st.html(
            """<style>
                    div[data-testid="stAppViewBlockContainer"] div[data-testid="column"] {
                        width: fit-content !important;
                        flex: unset;
                    }
                    div[data-testid="stAppViewBlockContainer"] div[data-testid="column"] * {
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
                        content: "\\f03e";
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
        st.image("static/GooberShot/goober_shot_logo_text.png", width=330)
        st.markdown(
            _(
                """**GOOBER SHOT** throws you into thrilling online archery battles against three other players! Prepare your bow, sharpen your arrows, enter the arena, and unleash your skills as a master archer. Remember, every arrow counts! Show off your precision and reflexes as you aim, shoot, and dodge with finesse. Rise through the ranks, climb the global leaderboards, and prove yourself as the ultimate archery champion. Will you emerge as the greatest archer in the realm?"""
            )
        )
        st.info(
            _(
                "**Goober Shot** is in **beta** currently (Bugs are expected and Data may be reset in future)"
            ),
            icon="ℹ️",
        )
        st.html("<h4>" + _("Platform") + "</h4>")
        col1, col2 = st.columns(2)
        col1.link_button(_("Browser"), "https://goobershot.winterpixel.io")
        st.html("<h4>" + _("Community") + "</h4>")
        col1, col2 = st.columns(2)
        col1.link_button("Discord", "https://discord.com/invite/kdGuBhXz2r")
        "---"
        st.html(
            "<h3><i class='fa-solid fa-screwdriver-wrench'></i>&nbsp;"
            + _("Tools")
            + "</h3>"
        )
        col1, col2 = st.columns(2)
        col1.button(
            _("Image Assets") + " (" + _("WIP") + ")",
            on_click=to_image_assets_page,
            type="primary",
        )
        "---"
        st.html(
            "<h3><i class='fa-solid fa-chart-simple'></i>&nbsp;"
            + _("Statistics")
            + "</h3>"
        )
        col1, col2 = st.columns(2)
        col1.button(
            _("Player Info") + " (" + _("WIP") + ")",
            on_click=to_player_info_page,
            type="primary",
        )
        col2.button(
            _("Season Leaderboard") + " (" + _("WIP") + ")",
            on_click=to_season_leaderboard_page,
            type="primary",
        )
        back_to_home(st.session_state.language)

elif st.session_state.game == "GooberShot" and st.session_state.page == "image_assets":
    with ph.container():
        from all_pages.GooberShot.Tools.image_assets import (
            load_page as GooberShot_image_assets,
        )

        GooberShot_image_assets(st.session_state.language)
        back_to_menu(st.session_state.language)

elif st.session_state.game == "GooberShot" and st.session_state.page == "player_info":
    with ph.container():
        from all_pages.GooberShot.Statistics.player_info import (
            load_page as GooberShot_player_info,
        )

        GooberShot_player_info(st.session_state.language)
        back_to_menu(st.session_state.language)

elif (
    st.session_state.game == "GooberShot"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from all_pages.GooberShot.Statistics.season_leaderboard import (
            load_page as GooberShot_season_leaderboard,
        )

        GooberShot_season_leaderboard(st.session_state.language)
        back_to_menu(st.session_state.language)
