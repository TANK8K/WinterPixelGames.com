import streamlit as st
from common_config import set_localization

_ = set_localization(st.session_state.language)


def load_page():
    st.image(
        "static/GooberDash/goober_dash_logo_text.png",
        width=280,
    )
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-calendar-days" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
        + _("Season Leaderboard")
        + "<span>"
    )
