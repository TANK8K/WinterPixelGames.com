import streamlit as st


def load_page():
    st.image("static/GooberRoyale/goober_royale_logo_text.png", width=235)
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-calendar-days" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Season Leaderboard<span>'
    )
