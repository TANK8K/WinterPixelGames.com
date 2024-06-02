import streamlit as st
from common_config import common_config, back_to_home

common_config()

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
        table {
            font-size: 1.3rem;
            margin-top: 10px;
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
    <table>
        <tr>
            <td><b>Framework</b></td>
            <td><img src="https://winterpixelgames.com/static/images/streamlit.svg" width="25"><a href="https://streamlit.io" target="_blank">Streamlit</a></td>
        </tr>
        <tr>
            <td><b>Language</b></td>
            <td><img src="https://winterpixelgames.com/static/images/python.svg" width="25"><a href="https://www.python.org/" target="_blank">Python</a></td>
        </tr>
        <tr>
            <td><b>Database (WIP)</b></td>
            <td><img src="https://winterpixelgames.com/static/images/postgresql.svg" width="25"><a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a></td>
        </tr>
        <tr>
            <td><b>Cloud Vendor</b></td>
            <td><img src="https://winterpixelgames.com/static/images/digital_ocean.svg" width="25"><a href="https://www.digitalocean.com/" target="_blank">Digital Ocean</a></td>
        </tr>
        <tr>
            <td><b>Web Server</b></td>
            <td><img src="https://winterpixelgames.com/static/images/nginx.svg" width="25"><a href="https://nginx.org/" target="_blank">Nginx</a></td>
        </tr>
        <tr>
            <td><b>Source Code</b></td>
            <td><img src="https://winterpixelgames.com/static/images/source_code.svg" width="25"><a href="https://github.com/TANK8K/WinterPixelGames.com" target="_blank">GitHub Repo</a></td>
        </tr>
    </table>
    """
)

"---"

st.html(
    """
    <h3><span style="font-size: 25px;">Developer<span></h3>
    <table>
        <tr>
            <td><b>GitHub</b></td>
            <td><img src="https://winterpixelgames.com/static/images/github.svg" width="25"><a href="https://github.com/TANK8K/" target="_blank">TANK8K</a></td>
        </tr>
        <tr>
            <td><b>Replit</b></td>
            <td><img src="https://winterpixelgames.com/static/images/replit.svg" width="25"><a href="https://replit.com/@TANK8K" target="_blank">TANK8K</a></td>
        </tr>
        <tr>
            <td><b>Discord</b></td>
            <td><img src="https://winterpixelgames.com/static/images/discord.svg" width="25"><a href="https://discord.com/invite/9q2Nnt4wnd" target="_blank">TANK8K</a></td>
        </tr>
        <tr>
            <td><b>YouTube</b></td>
            <td><img src="https://winterpixelgames.com/static/images/youtube.svg" width="25"><a href="https://youtube.com/@TANK8K/" target="_blank">TANK8K</a></td>
        </tr>
        <tr>
            <td><b>Personal Website</b></td>
            <td><img src="https://winterpixelgames.com/static/images/tank8k.svg" width="25"><a href="https://tank8k.com/" target="_blank">TANK8K</a></td>
        </tr>
    </table> 
    """
)

st.markdown(" Developed with 💖 by **[:blue[TANK8K]](https://tank8k.com/)**")
back_to_home()
