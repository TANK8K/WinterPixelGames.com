import streamlit as st
from os import listdir
from math import ceil
import pandas as pd


def load_page():
    st.image(
        "static/GooberDash/goober_dash_logo_text.png",
        width=280,
    )
    st.html(
        '<span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-image" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>Image Assets<span>'
    )

    st.warning(
        """
        The image assets in this page are for **promotional purpose** and/or **content creation** only (e.g. video thumbnails, wikis)

        Using content in derogatory fashions or for commerical purposes are prohibited.
        """,
        icon="⚠️",
    )
    tab1, tab2 = st.tabs(["Goober Generator", "Gallery"])

    directory = "./static/GooberDash/goober/5_color"
    files = listdir(directory)

    def initialize():
        df = pd.DataFrame(
            {
                "file": files,
                "incorrect": [False] * len(files),
                "label": [""] * len(files),
            }
        )
        df.set_index("file", inplace=True)
        return df

    if "df" not in st.session_state:
        df = initialize()
        st.session_state.df = df
    else:
        df = st.session_state.df

    controls = st.columns(3)
    with controls[0]:
        batch_size = st.select_slider("Batch size:", range(10, 110, 10))
    with controls[1]:
        row_size = st.select_slider("Row size:", range(1, 10), value=5)
    num_batches = ceil(len(files) / batch_size)
    with controls[2]:
        page = st.selectbox("Page", range(1, num_batches + 1))

    def update(image, col):
        df.at[image, col] = st.session_state[f"{col}_{image}"]
        if st.session_state[f"incorrect_{image}"] == False:
            st.session_state[f"label_{image}"] = ""
            df.at[image, "label"] = ""

    batch = files[(page - 1) * batch_size : page * batch_size]

    grid = st.columns(row_size)
    col = 0
    for image in batch:
        with grid[col]:
            st.image(f"{directory}/{image}")  # , caption=f"{image}")
            st.checkbox(
                f"{image}",
                key=f"incorrect_{image}",
                value=df.at[image, "incorrect"],
                on_change=update,
                args=(image, "incorrect"),
            )
        col = (col + 1) % row_size

    st.write("## Selections")
    st.dataframe([df["incorrect"]])
