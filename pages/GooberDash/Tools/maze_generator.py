import streamlit as st


def load_page():
    st.image(
        "https://winterpixelgames.com/static/images/goober_dash_logo_text.png",
        width=280,
    )
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-puzzle-piece" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Maze Generator<span>'
    )
