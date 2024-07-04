import streamlit as st
import extra_streamlit_components as stx
from common_config import (
    main_config,
    available_languages,
    set_localization,
    account_system,
)

st.set_page_config(
    page_title="WinterPixelGames » Tools and Stats",
    page_icon="static/wpg_hex_logo_144.png",
    layout="wide",
    initial_sidebar_state="auto",
)

main_config()
available_languages()

try:
    _ = set_localization(st.session_state.language)
except Exception:
    _ = set_localization("english")

account_system(_)

pg = st.navigation(
    {
        "": [
            st.Page("all_pages/0 Home.py", title=_("Home"), default=True, url_path=""),
            st.Page(
                "all_pages/1 Rocket Bot Royale.py",
                title=_("Rocket Bot Royale"),
                url_path="Rocket_Bot_Royale",
            ),
            st.Page(
                "all_pages/2 Goober Dash.py",
                title=_("Goober Dash"),
                url_path="Goober_Dash",
            ),
            st.Page(
                "all_pages/3 Goober Royale.py",
                title=_("Goober Royale"),
                url_path="Goober_Royale",
            ),
            st.Page(
                "all_pages/4 Goober Shot.py",
                title=_("Goober Shot"),
                url_path="Goober_Shot",
            ),
            st.Page(
                "all_pages/5 Moonrock Miners.py",
                title=_("Moonrock Miners"),
                url_path="Moonrock_Miners",
            ),
            st.Page(
                "all_pages/6 Broski.py",
                title=_("Broski"),
                url_path="Broski",
            ),
            st.Page(
                "all_pages/7 About.py",
                title=_("About"),
                url_path="About",
            ),
            st.Page(
                "all_pages/8 Useful Links.py",
                title=_("Useful Links"),
                url_path="Userful_Links",
            ),
        ],
    }
)


try:
    pg.run()
except Exception as e:
    print(e)
