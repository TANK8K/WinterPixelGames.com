import streamlit as st
import os
import random
from all_pages.GooberDash.Backend.goober_generator import generate_goober
from common_config import set_localization


def load_page(selected_language):
    _ = set_localization(selected_language)
    st.image(
        "static/GooberDash/goober_dash_logo_text.png",
        width=280,
    )
    st.markdown(
        """
        <style> 
        div[data-testid="stDownloadButton"] p {
            font-size: 20px !important;
        }
        div[data-testid="stDownloadButton"] p::before {
            font-family: "Font Awesome 5 Free" !important;
            font-weight: 600 !important;
            content: "\\f019";
            display: inline-block;
            vertical-align: middle;
            font-size: 20px !important;
            color: white;
            padding-right: 8px;
        }
        div[data-testid="stAppViewBlockContainer"] button[data-testid="baseButton-primary"] { 
            position: absolute;
            right: 50%;
            transform: translateX(50%);
        }
        }
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stVerticalBlock"]  div[data-testid="stButton"] button[data-testid="baseButton-primary"]:nth-last-child(1) p { 
            font-size: 20px !important;
        }
        div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div[data-testid="element-container"]:not(:last-child) div[data-testid="stButton"] button[data-testid="baseButton-secondary"]:nth-last-child(1) p::before { 
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f00c" !important;
            font-weight: 600 !important;
            display: inline-block;
            vertical-align: middle;
            font-size: 20px !important;
            color: white;
            padding-right: 8px;
        }
        div[data-testid="element-container"]:nth-child(11) div[data-testid="stButton"] button[data-testid="baseButton-primary"] div[data-testid="stMarkdownContainer"] p::before { 
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f522";
            font-weight: 600 !important;
            display: inline-block;
            vertical-align: middle;
            font-size: 18px;
            color: white;
            padding-right: 8px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-robot" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>'
        + _("Goober Generator")
        + "<span>",
        unsafe_allow_html=True,
    )

    def get_images_of_type(type):
        directory = f"./static/GooberDash/goober_item/{type.lower()}"
        images = [os.path.join(directory, file) for file in os.listdir(directory)]
        return sorted(images, key=lambda x: ("default" not in x, x))

    def extract_image_name(image_path):
        return os.path.splitext(os.path.basename(image_path))[0]

    types = ["Color", "Suit", "Hat", "Hand", "Eyes"]

    if "cosmetics_dict" not in st.session_state:
        st.session_state.cosmetics_dict = {t.lower(): None for t in types}

    tabs = st.tabs(
        [
            "🎨 " + _("Color"),
            "👕 " + _("Suit"),
            "🎩 " + _("Hat"),
            "⛏️  " + _("Hand"),
            "👀 " + _("Eyes"),
        ]
    )

    for i in range(5):
        with tabs[i]:
            images = get_images_of_type(types[i])

            # Pre-select the first item if not already selected
            if st.session_state.cosmetics_dict[types[i].lower()] is None:
                st.session_state.cosmetics_dict[types[i].lower()] = extract_image_name(
                    images[0]
                )

            # Display images in a grid layout
            cols = st.columns(6)
            for idx, img_path in enumerate(images):
                with cols[idx % 6]:
                    st.image(img_path)
                    if st.button(_("Select"), key=f"{types[i]}_{idx}"):
                        st.session_state.cosmetics_dict[types[i].lower()] = (
                            extract_image_name(img_path)
                        )
                    st.markdown("###")

    st.markdown("#")
    st.divider()

    def overlay_goober():
        global goober_file_path
        goober_file_path = generate_goober(
            st.session_state.cosmetics_dict["hat"],
            st.session_state.cosmetics_dict["suit"],
            st.session_state.cosmetics_dict["hand"],
            st.session_state.cosmetics_dict["color"],
            st.session_state.cosmetics_dict["eyes"],
        )
        st.image(goober_file_path)
        st.write("")

    overlay_goober()

    with open(goober_file_path, "rb") as file:
        st.download_button(
            label="**" + _("Download") + "**",
            data=file,
            file_name="generated_goober.png",
            mime="image/png",
            type="primary",
        )
    st.markdown("###")
    if st.button(_("Random"), type="primary"):
        for type in types:
            random_stuff = extract_image_name(
                random.choice(get_images_of_type(type.lower()))
            )
            st.session_state.cosmetics_dict[type.lower()] = random_stuff

    os.remove(goober_file_path)

    st.markdown("###")
