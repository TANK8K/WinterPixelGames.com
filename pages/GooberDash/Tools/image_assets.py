import streamlit as st
import os
import glob
from math import floor, log, pow


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

    def get_images_of_type(type):
        directory = f"./static/GooberDash/goober_item/{type.lower()}"
        images = [os.path.join(directory, file) for file in os.listdir(directory)]
        return sorted(images, key=lambda x: ("default" not in x, x))

    zip_path = "./static/GooberDash/gooberdash_image_assets_20240615.zip"
    file_size = os.path.getsize(zip_path)

    def convert_size(size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB")
        i = int(floor(log(size_bytes, 1024)))
        p = pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_name[i]}"

    with open(zip_path, "rb") as file:
        st.download_button(
            label=f"**Download All Image Assets ({convert_size(file_size)})**",
            data=file,
            file_name="goober_dash_image_assets.zip",
            mime="application/zip",
            type="primary",
        )

    st.markdown("#")

    types = [
        "🏅 Badge",
        "🎨 Color",
        "👕 Suit",
        "🎩 Hat",
        "⛏️  Hand",
        "👀 Eyes",
        "❔ Other Stuff",
    ]

    tabs = st.tabs(types)

    with tabs[0]:
        badges_directory = "./static/GooberDash/awards"
        badges = sorted(
            [
                os.path.join(badges_directory, file)
                for file in os.listdir(badges_directory)
            ]
        )

        n_rows = 1 + len(badges) // int(10)
        rows = [st.container() for _ in range(n_rows)]
        cols_per_row = [r.columns(10) for r in rows]
        cols = [column for row in cols_per_row for column in row]

        for image_index, badge in enumerate(badges):
            cols[image_index].image(badge)

    for i in range(5):
        with tabs[i + 1]:
            test_images = get_images_of_type(types[i + 1].split()[1])

            n_rows = 1 + len(test_images) // int(5)
            rows = [st.container() for _ in range(n_rows)]
            cols_per_row = [r.columns(10) for r in rows]
            cols = [column for row in cols_per_row for column in row]

            for image_index, test_image in enumerate(test_images):
                cols[image_index].image(test_image)

    with tabs[6]:
        png_images = glob.glob(
            os.path.join("./static/GooberDash/png_decompile_20240615", "**", "*.png"),
            recursive=True,
        )
        n_rows = 1 + len(png_images) // int(10)
        rows = [st.container() for _ in range(n_rows)]
        cols_per_row = [r.columns(10) for r in rows]
        cols = [column for row in cols_per_row for column in row]

        for image_index, png_image in enumerate(png_images):
            cols[image_index].image(png_image)
