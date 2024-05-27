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

    insert_html = """
        <link href='https://fonts.googleapis.com/css?family=Baloo 2' rel='stylesheet'>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"> 
        <div class="footer">
            <p>Developed with 💖 by <a style="text-decoration:none" href="https://tank8k.com/" target="_blank">TANK8K</a></p>
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
        section[data-testid="stSidebar"] {
            width: 336px !important;
        }
        div[data-testid="stSidebarNav"] > ul[data-testid="stSidebarNavItems"] > li > div > a > span {
            color: white !important;
            font-weight: 800;
            font-size: 25px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(1) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f015";
            display: inline-block;
            vertical-align: middle;
            font-weight:900;
            color: white;
            min-width: 25px;
            padding-left: 5px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(2) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/RocketBotRoyale_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(3) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberDash_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(4) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberRoyale_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(5) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberShot_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(6) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/MoonrockMiners_logo_180.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(7) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f129";
            display: inline-block;
            vertical-align: middle;
            font-weight:900;
            color: white;
            min-width: 25px;
            padding-left: 10px;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(8) > div > a::before{
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f08e";
            display: inline-block;
            vertical-align: middle;
            font-weight: 900;
            color: white;
            min-width: 25px;
            padding-left: 5px;
        }
        header {
            background: transparent !important;
        }
        button > div[data-testid="stMarkdownContainer"]:hover {
            color: #3097e6 !important; 
        }
        button[data-baseweb="tab"] {
            color: #ffffff !important; 
        }
        div[data-baseweb="tab-list"] > div[data-baseweb="tab-highlight"] {
            background-color: #3097e6 !important;
        }
        img[data-testid="stLogo"] {
            width: 100%;
            height: 2.5em;
            left: 8px;
            position: relative;
        }
        div[data-testid="stDecoration"] {
            background-image: linear-gradient(90deg, rgb(0, 108, 176), rgb(0, 43, 71));
        }
        div[role="dialog"] > div > div > div[data-testid="stMarkdownContainer"] > p:nth-last-child(1) {
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
            bottom: 2px;
            width: 100%;
            height: 25px;
            color: white;
            text-align: center;
            background-color: #081427;
            z-index: 99999;
        }
        .footer > p {
            font-size: 18px !important;
        }
        div[data-testid="collapsedControl"] > div > button {
            margin: 0;
        }
        div[data-testid="collapsedControl"] {
            background: #192841;
            margin-left: -50px;
            left: 10px;
            padding-left: 30px;
            border-radius: 50px;
            outline: none;
            border-color: #158fd8;
            box-shadow: 0 0 12px #158fd8;
        }
        div[data-testid="stAppViewBlockContainer"] p {
            font-size: 25px;
        }
        </style>
    """
    # background: #041827;
    #   opacity: .5;
    #   border: 2px solid #1590d8;
    #   margin-left: -50px;
    #   left: 20px;
    #   padding-left: 30px;
    #   border-radius: 50px;

    st.markdown(insert_html, unsafe_allow_html=True)
