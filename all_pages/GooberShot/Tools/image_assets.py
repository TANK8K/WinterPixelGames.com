import streamlit as st
from common_config import set_localization

_ = set_localization(st.session_state.language)


def load_page():
    st.image(
        "static/GooberShot/goober_shot_logo_text.png",
        width=280,
    )
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-image" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
        + _("Image Assets")
        + "<span>"
    )

    st.warning(
        _(
            """
        The image assets in this page are for **promotional purpose** and/or **content creation** only (e.g. video thumbnails, wikis)

        Using content in derogatory fashions or for commerical purposes are prohibited.
        """
        ),
        icon="⚠️",
    )
    tab1 = st.tabs(["🖼️ **" + _("Gallery") + "**"])
