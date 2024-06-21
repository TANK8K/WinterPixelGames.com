import streamlit as st
import pandas as pd
import os
from math import ceil
from streamlit_image_select import image_select
from pages.GooberDash.Backend.get_config import get_config
from pages.GooberDash.Backend.goober_generator import generate_goober


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
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-image" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Image Assets<span>',
        unsafe_allow_html=True,
    )

    st.warning(
        """
        The image assets in this page are for **promotional purpose** and/or **content creation** only (e.g. video thumbnails, wikis)

        Using content in derogatory fashions or for commercial purposes is prohibited.
        """,
        icon="⚠️",
    )
    tab1, tab2 = st.tabs(["🏭 **Goober Generator**", "🖼️ **Gallery**"])

    gd_config = get_config()

    def get_cosmetics_name(filename):
        cosmetics_name = gd_config["cosmetics"][filename]["name"]
        return cosmetics_name

    with tab1:
        # directories = [
        #    "./static/GooberDash/goober_item/color",
        #    "./static/GooberDash/goober_item/hand",
        #    "./static/GooberDash/goober_item/hat",
        #    "./static/GooberDash/goober_item/suit",
        # ]

        # all_files = []

        # for directory in directories:
        #    try:
        #        files = os.listdir(directory)
        #        all_files.extend([os.path.join(directory, file) for file in files])
        #    except FileNotFoundError:
        #        st.error(f"Directory not found: {directory}")

        # def process_file_path(file_path):
        #    filename_with_extension = os.path.basename(file_path)
        #    filename_without_extension = os.path.splitext(filename_with_extension)[0]
        #    return filename_without_extension

        # def initialize():
        #    df = pd.DataFrame(
        #        {
        #            "file": all_files,
        #            "cosmetics_name": all_files,
        #            "select": [False] * len(all_files),
        #            "label": [""] * len(all_files),
        #        }
        #    )
        #    df.set_index("file", inplace=True)
        #    df["cosmetics_name"] = df["cosmetics_name"].apply(process_file_path)
        #    return df

        # if "df" not in st.session_state:
        #    df = initialize()
        #    st.session_state.df = df
        # else:
        #    df = st.session_state.df

        # controls = st.columns(3)
        # with controls[0]:
        #    batch_size = st.select_slider("Batch size:", range(10, 110, 10))
        # with controls[1]:
        #    row_size = st.select_slider("Row size:", range(1, 10), value=5)
        # num_batches = ceil(len(all_files) / batch_size)
        # with controls[2]:
        #    page = st.selectbox("Page", range(1, num_batches + 1))

        # def update(image, col):
        #    if image in df.index:
        #        df.at[image, col] = st.session_state[f"{col}_{image}"]
        #        if not st.session_state[f"select_{image}"]:
        #            st.session_state[f"label_{image}"] = ""
        #            df.at[image, "label"] = ""

        # batch = all_files[(page - 1) * batch_size : page * batch_size]

        # grid = st.columns(row_size)
        # col = 0
        # for image in batch:
        #    with grid[col]:
        #        st.image(image)  # , caption=f"{image}")
        #        st.checkbox(
        #            # f"{os.path.basename(image)}",
        #            f"{get_cosmetics_name(os.path.splitext(os.path.basename(image))[0])}",
        #            key=f"select_{image}",
        #            value=df.at[image, "select"] if image in df.index else False,
        #            on_change=update,
        #            args=(image, "select"),
        #        )
        #    col = (col + 1) % row_size

        # st.write("## Selections")
        # st.dataframe(df[["cosmetics_name", "select"]])

        def get_images_of_type(type):
            directory = f"./static/GooberDash/goober_item/{type.lower()}"
            images = [os.path.join(directory, file) for file in os.listdir(directory)]
            return sorted(images, key=lambda x: ("default" not in x, x))

        types = ["Color", "Suit", "Hat", "Hand"]

        cosmetics_dict = {}

        tabs = st.tabs(types)
        for i in range(4):
            with tabs[i]:
                img = image_select(
                    label="",
                    images=get_images_of_type(types[i]),
                    use_container_width=False,
                )
                cosmetics_dict[types[i].lower()] = (
                    f"{os.path.splitext(os.path.basename(img))[0]}"
                )

        st.divider()

        goober_file_path = generate_goober(
            cosmetics_dict["hat"],
            cosmetics_dict["suit"],
            cosmetics_dict["hand"],
            cosmetics_dict["color"],
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

        st.markdown("######")
