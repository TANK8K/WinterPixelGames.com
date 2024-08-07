import streamlit as st
from common_config import back_to_home, set_localization

_ = set_localization(st.session_state.language)

st.html(
    """
    <style>
        div[data-testid="stAppViewBlockContainer"] div[data-testid="column"] {
            width: fit-content !important;
            flex: unset;
        }
        div[data-testid="stAppViewBlockContainer"] div[data-testid="column"] * {
            width: fit-content !important;
        }
        a[data-testid="baseLinkButton-secondary"] {
            border: 2px solid #2b3d58;
        }
        a[data-testid="baseLinkButton-secondary"]:hover {
            border: 2px solid #158fd8
        }
        div[data-testid="stLinkButton"] p {
            font-weight: 800;
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(7) p::before, div[data-testid="stVerticalBlock"] div[data-testid="stLinkButton"] p::before {
            display: inline-block;
            vertical-align: middle;
            content: "";
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
            right: 5px;
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(1) p::before {
            background-image: url("./app/static/RocketBotRoyale/rocket_bot_royale_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(2) p::before {
            background-image: url("./app/static/GooberRoyale/goober_royale_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(3) p::before {
            background-image: url("./app/static/GooberShot/goober_shot_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(4) p::before {
            background-image: url("./app/static/MoonrockMiners/moonrock_miners_favicon.png");
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stHorizontalBlock"]:nth-child(13) > div:nth-child(5) p::before {
            background-image: url("./app/static/Broski/broski_favicon.png");
        }
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stVerticalBlock"] div[data-testid="stLinkButton"] p::before {
            background-image: url("./app/static/GDLM_favicon.png");
        }
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
    </style>
    """
)

st.html(
    '<h4><i class="fa-solid fa-arrow-up-right-from-square" style="display: inline; margin: 0 10px 8px 0; width: 25px"></i>'
    + _("Useful Links")
    + '</h4><h3><span style="font-size: 25px;">'
    + _("Staging Servers")
    + "<span></h3>"
)

st.markdown(
    _(
        """**Staging Servers** are seperate servers which are used for testing new features before releasing. Usually updates are released on **Staging Servers** a few days before public release. Developers invite members to test out some upcoming features and ask for feedbacks in **Offcial Winterpixel Games Discord server** occasionally.
"""
    )
)

col1, col2, col3, col4, col5 = st.columns(5)
col1.link_button(
    _("Rocket Bot Royale"), "https://staging-rocketbotroyale.winterpixel.io/"
)
# col2.link_button("Goober Dash", "https://upguys-staging.winterpixel.io/")
col2.link_button(
    _("Goober Royale"),
    "https://gooberroyale-staging.winterpixel.io/",
)
col3.link_button(_("Goober Shot"), "https://gooberfall-staging.winterpixel.io/")
col4.link_button(_("Moonrock Miners"), "https://staging-asteroids.winterpixel.io/")
col5.link_button(_("Broski"), "https://skier-staging.winterpixel.io/")

st.error(
    _(
        "**Staging Servers** use seperate databases. **DO NOT** spend money on **Staging Server** as items cannot be transferred."
    ),
    icon="🚨",
)

"---"

st.html('<h3><span style="font-size: 25px;">' + _("Friendly Websites") + "<span></h3>")

st.markdown(
    _(
        """[**Goober Dash Level Modding**](https://twhlynch.me/goober-dash-level-modding/) is a website made by [**Tom Lynch (aka index)**](https://twhlynch.me/) which provides useful **scripts** to generate levels for **[Goober Dash](./Goober_Dash)**.
"""
    )
)

st.link_button(
    _("Goober Dash Level Modding"), "https://twhlynch.me/goober-dash-level-modding/"
)

back_to_home(st.session_state.language)
