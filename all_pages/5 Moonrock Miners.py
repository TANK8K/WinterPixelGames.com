import streamlit as st
from common_config import (
    back_to_home,
    back_to_menu,
    set_localization,
    footer_and_language,
)

_ = set_localization(st.session_state.language)
footer_and_language(st.session_state.language)

try:
    if st.session_state.game != "MoonrockMiners":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "MoonrockMiners"


def to_image_assets_page():
    st.session_state.page = "image_assets"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "MoonrockMiners" and st.session_state.page == "menu":
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
                        content: "\\f03e";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(14) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f073";
                    }
                    </style>"""
        )
        st.image("static/MoonrockMiners/moonrock_miners_banner.png", width=500)
        st.markdown(
            _(
                """**MOONROCK MINERS** is a gravity-defying multiplayer space battle game set in an asteroid field. Blast other players, collect powerups and crystals, and avoid the asteroids. Try to survive until the end to win the match. Compete against players around the world in real-time to rank in every season. You can also create your own custom lobbies to play private games online with your friends!"""
            )
        )
        st.info(
            _("**Moonrock Miners** is **no longer in development**"),
            icon="ℹ️",
        )
        st.html("<h4>" + _("Platform") + "</h4>")
        col1, col2 = st.columns(2)
        col1.link_button(_("Browser"), "https://moonrockminers.com")
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
            _("Season Leaderboard") + " (" + _("WIP") + ")",
            on_click=to_season_leaderboard_page,
            type="primary",
        )
        st.info(
            _("**Leaderboard** is **disabled** currently"),
            icon="ℹ️",
        )
        back_to_home(st.session_state.language)

elif (
    st.session_state.game == "MoonrockMiners"
    and st.session_state.page == "image_assets"
):
    with ph.container():
        from all_pages.MoonrockMiners.Tools.image_assets import (
            load_page as MoonrockMiners_image_assets,
        )

        MoonrockMiners_image_assets(st.session_state.language)
        back_to_menu(st.session_state.language)

elif (
    st.session_state.game == "MoonrockMiners"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from all_pages.MoonrockMiners.Statistics.season_leaderboard import (
            load_page as MoonrockMiners_season_leaderboard,
        )

        MoonrockMiners_season_leaderboard(st.session_state.language)
        back_to_menu(st.session_state.language)
