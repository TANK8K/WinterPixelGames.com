import streamlit as st

def common_config():
    st.set_page_config(page_title='WinterPixelGames » Tools and Stats',
                       page_icon='static/images/wpg_hex_logo_144.png',
                       layout='centered',
                       initial_sidebar_state='auto',
                        menu_items={
                            'About': '''
                            Provides useful **:blue-background[Tools & Statistics]** of games made by **[Winterpixel Games](https://winterpixel.com/)**!

                            This website is **NOT** affiliated with or endorsed by Winterpixel Games Inc.

                            [![Source Code](https://winterpixelgames.com/static/images/source_code_icon_v4_20.svg)](https://github.com/TANK8K/WinterPixelGames.com_streamlit_part)[:gray[Source Code]](https://github.com/TANK8K/WinterPixelGames.com_streamlit_part)

                            Developed with 💖 by **[:blue[TANK8K]](https://tank8k.com/)**
                            
                            [![Github](https://winterpixelgames.com/static/images/github_icon_20.svg)](https://github.com/TANK8K/)&nbsp;
                            [![YouTube](https://winterpixelgames.com/static/images/youtube_icon_20.svg)](https://youtube.com/@TANK8K/)&nbsp;
                            [![My Website](https://winterpixelgames.com/static/images/tank8k_favicon_20.svg)](https://tank8k.com/)

                            
                            '''
                        })

    st.logo("static/images/streamlit_banner.png",
            icon_image="static/images/wpg_hex_logo_144.png")

    insert_html = """
        <link href='https://fonts.googleapis.com/css?family=Baloo 2' rel='stylesheet'>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"> 
        <style>
        h1, h2, h3, h4, h5, h6, p, li {
            font-family: 'Baloo 2' !important;
        }
        div[data-testid="stSidebarNav"] > ul[data-testid="stSidebarNavItems"] > li > div > a > span {
            color: white !important;
            font-weight: 800;
            font-size: 18px;
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
            background-image: url("https://winterpixelgames.com/static/images/RocketBotRoyale_logo.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(3) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberDash_logo.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(4) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberRoyale_logo.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(5) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/GooberShot_logo.png");
            background-size: 100% 100%;
            display: inline-block;
            height: 25px;
            width: 25px;
            position: relative;
        }
        ul[data-testid="stSidebarNavItems"] > li:nth-child(6) > div > a::before{
            content: "";
            background-image: url("https://winterpixelgames.com/static/images/MoonrockMiners_logo.png");
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
            font-weight:900;
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
        }
        div[data-testid="stDecoration"] {
            background-image: linear-gradient(90deg, rgb(22, 142, 217), rgb(108, 195, 251));
        }
        </style>
    """

    st.markdown(insert_html, unsafe_allow_html=True)
