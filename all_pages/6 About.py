import streamlit as st
from common_config import back_to_home

st.html(
    """
    <style>
        div[data-testid="stVerticalBlock"] div:nth-child(14) p:nth-child(2) {
            position: relative;
            top: -15px;
        }
        div[data-testid="stAppViewBlockContainer"] {
            padding: 50px 5vw 100px 5vw !important;
        }
        h4 {
            padding-bottom: 15px;
        }
        h3 {
            padding-bottom: 0;
        }
        table * {
            border: none !important;
        }
        table {
            font-size: 1.3rem;
            margin-top: 10px;
            position: relative;
            top: -20px;
        }
        table thead {
            display: none;
        }
        table td {
            padding: 0 5vw 0 0 !important;
        }
        table a {
            color: rgb(46, 154, 255) !important;
        }
        table td:first-child {
            padding-right: 5vw;
            display: inline-block;
        }
        table td img {
            margin-right: 5px;
            width: 25px;
        }
    </style>
    """
)

st.html(
    """
    <h4><i class="fa-solid fa-circle-info" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>About</h4><h3><span style="font-size: 25px;">What is WinterPixelGames?<span></h3>
    """
)

st.markdown(
    """**:blue-background[WinterPixelGames]** (WPG) is a community-driven site made by [**TANK8K**](https://tank8k.com/) which provides useful **Tools & Statistics** of games made by **[Winterpixel Games](https://www.winterpixel.com/)**, including **[Rocket Bot Royale](./Rocket_Bot_Royale)**, **[Goober Dash](./Goober_Dash)**, **[Goober Royale](./Goober_Royale)**, **[Goober Shot](./Goober_Shot)**, and **[Moonrock Miners](./Moonrock_Miners)**.

---"""
)

st.html(
    """
    <h3><span style="font-size: 25px;">Affiliation<span></h3>
    """
)

st.markdown(
    """This website is **NOT** affiliated with or endorsed by **Winterpixel Games Inc.**

---"""
)

st.html(
    """
    <h3><span style="font-size: 25px;">Copyright Notice<span></h3>
    """
)

st.markdown(
    """Rocket Bot Royale, Goober Dash, Goober Royale, Goober Shot, Moonrock Miners, Websites and Media **@ Winterpixel Games Inc.**

---"""
)

st.html(
    """
    <h3><span style="font-size: 25px;">License<span></h3>
    """
)

st.markdown(
    """The source code is licensed under **MIT license**. 

---"""
)

st.html(
    """
    <h3><span style="font-size: 25px;">Technology<span></h3>
    """
)

st.markdown(
    """
    |||
    |---|---|
    |**Framework**|![Streamlit](https://winterpixelgames.com/static/images/streamlit.svg)[Streamlit](https://streamlit.io)|
    |**Language**|![Python](https://winterpixelgames.com/static/images/python.svg)[Python](https://www.python.org/)|
    |**Database**|![PostgreSQL](https://winterpixelgames.com/static/images/postgresql.svg)[PostgreSQL](https://www.postgresql.org/)|
    |**Cloud Vendor**|![Digital Ocean](https://winterpixelgames.com/static/images/digital_ocean.svg)[Digital Ocean](https://www.digitalocean.com/)|
    |**Web Server**|![Nginx](https://winterpixelgames.com/static/images/nginx.svg)[Nginx](https://nginx.org/)|
    |**Source Code**|![GitHub Repo](https://winterpixelgames.com/static/images/source_code.svg)[GitHub Repo](https://github.com/TANK8K/WinterPixelGames.com)|
    """
)

"---"

st.html(
    """
    <h3><span style="font-size: 25px;">Developer<span></h3>
    """
)

st.markdown(
    """
    |||
    |---|---|
    |**GitHub**|![GitHub](https://winterpixelgames.com/static/images/github.svg)[TANK8K](https://github.com/TANK8K/)|
    |**Replit**|![Replit](https://winterpixelgames.com/static/images/replit.svg)[TANK8K](https://replit.com/@TANK8K/)|
    |**Discord**|![Discord](https://winterpixelgames.com/static/images/discord.svg)[TANK8K](https://discord.com/invite/9q2Nnt4wnd)|
    |**YouTube**|![YouTube](https://winterpixelgames.com/static/images/youtube.svg)[TANK8K](https://youtube.com/@TANK8K/)|
    |**Personal Website**|![Personal Website](https://winterpixelgames.com/static/images/tank8k.svg)[TANK8K](https://tank8k.com/)|
    """
)

st.markdown(" Developed with 💖 by **[:blue[TANK8K]](https://tank8k.com/)**")
back_to_home()
