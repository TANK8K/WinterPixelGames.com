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
    if st.session_state.game != "RocketBotRoyale":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "RocketBotRoyale"


def to_optimize_crate_page():
    st.session_state.page = "optimize_crate"


def to_image_assets_page():
    st.session_state.page = "image_assets"


def to_player_info_page():
    st.session_state.page = "player_info"


def to_season_leaderboard_page():
    st.session_state.page = "season_leaderboard"


ph = st.empty()

if st.session_state.game == "RocketBotRoyale" and st.session_state.page == "menu":
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
                        content: "\\f466";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(10) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f03e";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f007";
                    }
                    div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(2) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f073";
                    }
                    </style>"""
        )
        st.image("static/RocketBotRoyale/rocket_bot_royale_banner_v2.png")
        st.markdown(
            _(
                """**ROCKET BOT ROYALE** is a fun new take on the online battle royale formula. Powerful, wall-climbing, rocket-jumping, artillery-pumping Robo-Tanks are the vehicle of choice in this fast-paced shootout, where the goal is to survive longer than the competition. Collect the loot to upgrade your arsenal, tunnel into the terrain to take cover and collect buried treasure, and avoid the rising water levels to be the blast one standing!"""
            )
        )

        st.html("<h4>" + _("Platforms") + "</h4>")
        col1, col2, col3, col4 = st.columns(4)
        col1.link_button(_("Browser"), "https://rocketbotroyale.winterpixel.io")
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

        st.html("<h4>" + _("Communities") + "</h4>")
        col1, col2, col3, col4 = st.columns(4)
        col1.link_button("Discord", "https://discord.com/invite/kdGuBhXz2r")
        col2.link_button("Steam", "https://steamcommunity.com/app/1748390/discussions")
        col3.link_button(
            "Fandom",
            "https://rocketbotroyale.fandom.com/wiki/Rocket_Bot_Royale_Wiki",
        )
        col4.link_button("Reddit", "https://www.reddit.com/r/RocketBotRoyale")
        "---"
        st.html(
            "<h3><i class='fa-solid fa-screwdriver-wrench'></i>&nbsp;"
            + _("Tools")
            + "</h3>"
        )
        col1, col2 = st.columns(2)
        col1.button(
            _("Optimize Crate") + " (" + _("WIP") + ")",
            on_click=to_optimize_crate_page,
            type="primary",
        )
        col2.button(
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


elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "optimize_crate"
):
    with ph.container():
        from all_pages.RocketBotRoyale.Tools.optimize_crate import (
            load_page as RocketBotRoyale_optimize_crate,
        )

        RocketBotRoyale_optimize_crate(st.session_state.language)
        back_to_menu(st.session_state.language)

elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "image_assets"
):
    with ph.container():
        from all_pages.RocketBotRoyale.Tools.image_assets import (
            load_page as RocketBotRoyale_image_assets,
        )

        RocketBotRoyale_image_assets(st.session_state.language)
        back_to_menu(st.session_state.language)

elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "player_info"
):
    with ph.container():
        from all_pages.RocketBotRoyale.Statistics.player_info import (
            load_page as RocketBotRoyale_player_info,
        )

        RocketBotRoyale_player_info(st.session_state.language)
        back_to_menu(st.session_state.language)

elif (
    st.session_state.game == "RocketBotRoyale"
    and st.session_state.page == "season_leaderboard"
):
    with ph.container():
        from all_pages.RocketBotRoyale.Statistics.season_leaderboard import (
            load_page as RocketBotRoyale_season_leaderboard,
        )

        RocketBotRoyale_season_leaderboard(st.session_state.language)
        back_to_menu(st.session_state.language)
