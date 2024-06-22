import streamlit as st
from common_config import common_config

common_config()

pg = st.navigation(
    {
        "": [
            st.Page("all_pages/0 Home.py", title="Home", default=True, url_path=""),
            st.Page(
                "all_pages/1 Rocket Bot Royale.py",
                title="Rocket Bot Royale",
                url_path="Rocket_Bot_Royale",
            ),
            st.Page(
                "all_pages/2 Goober Dash.py",
                title="Goober Dash",
                url_path="Goober_Dash",
            ),
            st.Page(
                "all_pages/3 Goober Royale.py",
                title="Goober Royale",
                url_path="Goober_Royale",
            ),
            st.Page(
                "all_pages/4 Goober Shot.py",
                title="Goober Shot",
                url_path="Goober_Shot",
            ),
            st.Page(
                "all_pages/5 Moonrock Miners.py",
                title="Moonrock Miners",
                url_path="Moonrock_Miners",
            ),
            st.Page(
                "all_pages/6 About.py",
                title="About",
                url_path="About",
            ),
            st.Page(
                "all_pages/7 Useful Links.py",
                title="Useful Links",
                url_path="Userful_Links",
            ),
        ],
    }
)


try:
    pg.run()
except Exception as e:
    print(e)
