import streamlit as st
import os
from streamlit_image_select import image_select
from all_pages.GooberDash.Backend.goober_generator import generate_goober


def load_page():
    st.image(
        "static/GooberDash/goober_dash_logo_text.png",
        width=280,
    )
    st.html(
        """
        <style> 
        div[data-testid="stDownloadButton"] p::before {
            display: inline-block;
            vertical-align: middle;
            font-weight: 900;
            font-size: 20px;
            color: white;
            padding-right: 5px;
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f019";
        }
        div[data-testid="stAppViewBlockContainer"] button[data-testid="baseButton-primary"] { 
            position: absolute;
            right: 50%;
            transform: translateX(50%);
        }
        </style>
        """
    )
    st.markdown(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-robot" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Goober Generator<span>',
        unsafe_allow_html=True,
    )

    def get_images_of_type(type):
        directory = f"./static/GooberDash/goober_item/{type.lower()}"
        images = [os.path.join(directory, file) for file in os.listdir(directory)]
        return sorted(images, key=lambda x: ("default" not in x, x))

    types = ["🎨 Color", "👕 Suit", "🎩 Hat", "⛏️  Hand", "👀 Eyes"]

    cosmetics_dict = {}

    tabs = st.tabs(types)
    for i in range(5):
        with tabs[i]:
            img = image_select(
                label="",
                images=get_images_of_type(types[i].split()[1]),
                use_container_width=False,
            )
            cosmetics_dict[types[i].split()[1].lower()] = (
                f"{os.path.splitext(os.path.basename(img))[0]}"
            )

    st.divider()

    goober_file_path = generate_goober(
        cosmetics_dict["hat"],
        cosmetics_dict["suit"],
        cosmetics_dict["hand"],
        cosmetics_dict["color"],
        cosmetics_dict["eyes"],
    )
    st.image(goober_file_path)
    st.write("")

    with open(goober_file_path, "rb") as file:
        st.download_button(
            label="**Download**",
            data=file,
            file_name="generated_goober.png",
            mime="image/png",
            type="primary",
        )

    os.remove(goober_file_path)

    st.markdown("###")
