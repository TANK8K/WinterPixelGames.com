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
    if st.session_state.game != "Broski":
        st.session_state.page = "menu"
except Exception:
    st.session_state.page = "menu"
st.session_state.game = "Broski"


def to_image_assets_page():
    st.session_state.page = "image_assets"


ph = st.empty()

if st.session_state.game == "Broski" and st.session_state.page == "menu":
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
                    div[data-testid="stHorizontalBlock"]:nth-child(11) > div:nth-child(1) p::before {
                        font-family: "font awesome 5 Free" !important;
                        content: "\\f03e";
                    }
                    </style>"""
        )
        st.image("static/Broski/broski_logo_text.png", width=500)
        st.markdown(
            _(
                """**BROSKI** is an arcade pixel style skiing game, it is a fun and has a unique visual style that allows you to enjoy skiing even in summer. In the game, you will play as a skier who races down a snowy mountain. Your goal is to ski the furthest distance possible. As you slide down the hill faster and faster, you have to avoid more and more obstacles on the way, which makes the game challenging. To test how far you can go, take the challenge!"""
            )
        )
        st.info(
            _("**Broski** is a **prototype single-player game** currently"),
            icon="ℹ️",
        )
        st.html("<h4>" + _("Platform") + "</h4>")
        col1, col2 = st.columns(2)
        col1.link_button(_("Browser"), "https://skier-staging.winterpixel.io/")
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
        back_to_home(st.session_state.language)

elif st.session_state.game == "Broski" and st.session_state.page == "image_assets":
    with ph.container():
        from all_pages.Broski.Tools.image_assets import (
            load_page as Broski_image_assets,
        )

        Broski_image_assets(st.session_state.language)
        back_to_menu(st.session_state.language)
