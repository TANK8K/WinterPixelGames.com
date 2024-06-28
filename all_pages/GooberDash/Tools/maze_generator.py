import streamlit as st
from common_config import set_localization


def load_page(selected_language):
    _ = set_localization(selected_language)
    st.image(
        "static/GooberDash/goober_dash_logo_text.png",
        width=280,
    )
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-puzzle-piece" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
        + _("Maze Generator")
        + "<span>"
    )
