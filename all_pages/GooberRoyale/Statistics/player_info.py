import streamlit as st
from common_config import set_localization


def load_page(selected_language):
    _ = set_localization(selected_language)
    st.image("static/GooberRoyale/goober_royale_logo_text.png", width=235)
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-user" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
        + _("Player Info")
        + "<span>"
    )
