import streamlit as st

def common_config():
    st.set_page_config(page_title='WinterPixelGames » Tools and Stats',
                       page_icon='static/images/wpg_hex_logo_144.png',
                       layout='wide',
                       initial_sidebar_state='auto',
                       menu_items={
                            'About': '''
                            Provides useful **:blue-background[Tools & Statistics]** of games made by **[Winterpixel Games](https://winterpixel.com/)**!

                            This website is **NOT** affiliated with or endorsed by Winterpixel Games Inc. 

                            All relevant trademarks belong to their respective owners.

                            ​

                            Developed with 💖 by **[:blue[TANK8K]](https://tank8k.com/)**
                            
                            [![Source Code](https://winterpixelgames.com/static/images/source_code_icon_25.svg)](https://github.com/TANK8K/WinterPixelGames.com_streamlit_part)&nbsp;
                            [![Github](https://winterpixelgames.com/static/images/github_icon_20.svg)](https://github.com/TANK8K/)&nbsp;&nbsp;
                            [![YouTube](https://winterpixelgames.com/static/images/youtube_icon_20.svg)](https://youtube.com/@TANK8K/)&nbsp;&nbsp;
                            [![My Website](https://winterpixelgames.com/static/images/tank8k_favicon_20.svg)](https://tank8k.com/)
                            '''
                        })

    st.logo("static/images/streamlit_banner.png",
            icon_image="static/images/wpg_hex_logo_144.png")

    st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400..800&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"> 
        <div class="footer">
            <p><span style="display:inline-block;">This website is NOT affiliated with or endorsed by Winterpixel Games Inc.</span><span style="display:inline-block;">&nbsp;All relevant trademarks belong to their respective owners.</span><br>Developed with 💖 by <a style="text-decoration:none" href="https://tank8k.com/" target="_blank">TANK8K</a></p>
        </div>
        <style>
        *:hover {
            cursor: url('https://winterpixelgames.com/static/images/cursor_v5.png'), auto !important;
        }
        *:focus {
            cursor: url('https://winterpixelgames.com/static/images/cursor_v5.png'), auto !important;
        }
        h1, h2, h3, h4, h5, h6, p, li {
            font-family: 'Baloo 2' !important;
        }
        h3 {
            font-weight: 800;
            color: #32bafa;
            font-size: 25px;
        }
        h3, h4 {
            padding: 0;
        }
        section[data-testid="stSidebar"] {
            width: 336px !important;
        }
        div[data-testid="stSidebarNav"] > ul[data-testid="stSidebarNavItems"] > li > div > a > span {
            color: white !important;
            font-weight: 700;
            font-size: 25px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(1) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f015";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 8px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(2) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/RocketBotRoyale_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(3) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberDash_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(4) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberRoyale_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(5) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberShot_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(6) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/MoonrockMiners_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 35px;
            width: 35px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(7) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f129";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 14px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(8) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f08e";
            display: inline-block;
            vertical-align: middle;
            font-weight: 800;
            font-size: 20px;
            color: white;
            min-width: 35px;
            padding-left: 7px;
        }
        header {
            background: transparent !important;
        }
        button[data-baseweb="tab"] {
            color: #ffffff !important; 
        }
        div[data-baseweb="tab-list"] > div[data-baseweb="tab-highlight"] {
            background-color: #3097e6 !important;
        }
        div[data-testid="stSidebarHeader"] img[data-testid="stLogo"] {
            width: 100%;
            height: 2.5em;
            left: 12px;
            position: relative;
            transform: scale(1.2, 1.2);
            top: 15px;
        }
        div[data-testid="stDecoration"] {
            background-image: linear-gradient(90deg, rgb(0, 108, 176), rgb(0, 43, 71));
        }
        div[role="dialog"] > div > div > div[data-testid="stMarkdownContainer"] > p:nth-last-child(1) {
            display: none;
        }
        div[role="dialog"] > div:nth-child(2) > div > div:not([data-testid="stMarkdownContainer"]):nth-last-child(1) {
            display: none;
        }
        div[role="dialog"] > div:nth-child(2) > div > div:not([data-testid="stMarkdownContainer"]):nth-child(1) {
            display: none;
        }
        ul[data-testid="main-menu-list"] > ul:nth-child(4) {
            display: none;
        }
        ul[data-testid="main-menu-list"] > div[data-testid="main-menu-divider"] {
            display: none;
        } 
        body {
            overscroll-behavior-x: none !important;
            overscroll-behavior-y: none !important;
        }
        div[data-testid="collapsedControl"] {
            left: 0.5rem;
        }
        div[data-testid="collapsedControl"] > div {
            padding-top: 8px;
            left: -3px;
            position: relative;
        }
        div[data-testid="stSidebarCollapseButton"] {
            position: relative;
            top: 25px;
            left: 22px;
        }
        div[data-testid="stSidebarCollapseButton"] > button[data-testid="baseButton-header"], button[data-testid="baseButton-headerNoPadding"] {
            border-radius: 50px;
        }
        div[data-testid="collapsedControl"] > button[data-testid="baseButton-headerNoPadding"] > svg {
            font-size: 1rem;
            position: relative;
        }
        * {
            cursor: url('https://winterpixelgames.com/static/images/cursor_v5.png'), auto !important;
        }
        @supports not selector(::-webkit-scrollbar) {
            html {
                scrollbar-color: rgb(108, 195, 251) transparent !important;
            }
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar {
            width: 6px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-track {
            background-color: rgba(255, 255, 255, 0.1) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3) !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 0.8), rgba(50, 144, 212, 0.8)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb:hover {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 0.9), rgba(50, 144, 212, 0.9)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        div[data-testid="stAppViewContainer"] ::-webkit-scrollbar-thumb:active {
            background-image: linear-gradient(45deg, rgba(22, 79, 122, 1), rgba(50, 144, 212, 1)) !important;
            border-radius: 6px !important;
            -webkit-box-shadow: rgba(0,0,0,.12) 0 3px 13px 1px !important;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            height: 33px;
            color: white;
            text-align: center;
            background-color: #081427;
            z-index: 99999;
            border-top: 0.5px inset #666666;
        }
        .footer > p {
            font-size: 11px !important;
            line-height: 15px;
            margin-top: 1px;
        }
        div[data-testid="collapsedControl"] > div > button {
            margin: 0;
            position: relative;
            top: -2px;
        }
        div[data-testid="collapsedControl"] {
            background: #192841;
            margin-left: -50px;
            left: 30px;
            padding: 3px 0 3px 30px;
            border-radius: 50px;
            outline: none;
            border-color: #158fd8;
            box-shadow: 0 0 12px #158fd8;
            top: 35px;
        }
        div[data-testid="collapsedControl"] img {
            transform: scale(1.6,1.6);
            top: 6px;
            position: relative;
            left: -1px;
        }
        div[data-testid="stAppViewBlockContainer"] p {
            font-size: 20px;
        }
        hr:not([size]) {
            height: 1px;
            margin: 15px 0px;
        }
        a[data-testid="baseLinkButton-primary"]:hover, a[data-testid="baseLinkButton-secondary"]:hover, div[data-testid="stVerticalBlock"] div:not([data-baseweb]) button:hover {
            color: white;
            outline: none;
            border: 1.5px solid #158fd8;
            box-shadow: 0 0 10px #158fd8;
        }
        a[data-testid="baseLinkButton-primary"]:focus, a[data-testid="baseLinkButton-secondary"]:focus, button:focus {
            color: white !important;
        }
        a[kind="primary"]:hover, button[kind="primary"]:hover {
            background: #192841;
        }
        div[data-baseweb="tab-list"] button:hover {
            color: #158fd8 !important;    
            border: none !important;
            box-shadow: none !important;
        }
        section[data-testid="stSidebar"] > div:nth-child(2) > div > div {
            display: none;
        }
        div[data-testid="stAppViewBlockContainer"] {
            padding: 0px 30px 50px 30px;
        }
        </style>
    """, unsafe_allow_html=True)