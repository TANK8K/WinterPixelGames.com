import json
import re
import streamlit as st
import numpy as np
from io import StringIO
from all_pages.GooberDash.Backend.levels import upload_level, download_level
from common_config import set_localization


def flip_json(file_name, data):
    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return super(NpEncoder, self).default(obj)

    new_json = {
        "metadata": {
            "author_id": "",
            "author_name": "",
            "game_mode": "Race",
            "id": "",
            "name": f"{file_name} flipped",
            "player_count": 1,
            "published": "Private",
            "rating": 0,
            "theme": "castle",
            "type": 0,
        },
        "nodes": [],
    }
    keys = ["game_mode", "player_count", "theme"]
    for key in keys:
        new_json["metadata"][key] = data["metadata"][key]

    nodes = []

    shape_rotation_0_3_swap_1_2_swap_dict = {0: 3, 1: 2, 2: 1, 3: 0}
    shape_rotation_1_3_swap_dict = {0: 0, 1: 3, 2: 2, 3: 1}
    shape_rotation_0_2_swap_dict = {0: 2, 1: 1, 2: 0, 3: 3}

    for i in data["nodes"]:
        if "animation" in i:
            if "position" in i["animation"]["tween_sequences"]:
                for j in i["animation"]["tween_sequences"]["position"]["tweens"]:
                    if j["value_type"] == 5:
                        j["value_x"] = -j["value_x"]
            if "rotation_degrees" in i["animation"]["tween_sequences"]:
                for j in i["animation"]["tween_sequences"]["rotation_degrees"][
                    "tweens"
                ]:
                    if j["value_type"] == 3:
                        new = -j["value"]
                        j["value"] = new

        if not (i["pivot_x"] == 0.5 and i["pivot_y"] == 0.5):
            new_pivot_x = 1 - i["pivot_x"]
            i["pivot_x"] = new_pivot_x
            if "properties" in i:
                i["properties"]["pivot"] = re.sub(
                    "\([^]]*\,", f"({new_pivot_x},", i["properties"]["pivot"]
                )

        i["x"] = -(i["x"] + i["width"])
        i["rotation"] = -i["rotation"]
        if i["type"] in [
            "ramp",
            "background_ramp",
            "background_ramp2",
            "background_ramp3",
        ]:
            i["shape_rotation"] = shape_rotation_0_3_swap_1_2_swap_dict[
                i["shape_rotation"]
            ]
        elif i["type"] in [
            "arrow",
            "alert",
            "pit",
            "gravity_field",
            "checkpoint",
            "finish_line",
            "floor",
        ]:
            i["shape_rotation"] = shape_rotation_1_3_swap_dict[i["shape_rotation"]]
        elif i["type"] in ["laser"]:
            i["shape_rotation"] = shape_rotation_0_2_swap_dict[i["shape_rotation"]]
        nodes.append(i)

    new_json["nodes"] = nodes[::-1]

    res = json.dumps(new_json, cls=NpEncoder)
    return res


def load_page(selected_language):
    _ = set_localization(selected_language)
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
        div[data-testid="stAppViewBlockContainer"] div[data-testid="stLinkButton"] p::before {
            display: inline-block;
            vertical-align: middle;
            font-weight: 900;
            font-size: 20px;
            color: white;
            padding-right: 5px;
            font-family: "Font Awesome 5 Free" !important;
            content: "\\f11b";
        }
        </style>
        <span style="font-size: 25px; font-weight: bold;"><i class="fa-solid fa-left-right" style="display: inline; margin: 0 5px 8px 0; width: 25px"></i>"""
        + _("Flip Level")
        + "<span>"
    )
    data = None

    method = st.selectbox(_("Upload and Download Level by"), (_("Level ID"), "JSON"))

    with st.form("input_form"):
        if method == _("Level ID"):
            level_id = (
                st.text_input(
                    "**" + _("Level ID") + "(" + _("Full URL supported") + ")**"
                )
                .replace("https://gooberdash.winterpixel.io/?play=", "")
                .split("&ghost")[0]
            )
        elif method == "JSON":
            uploaded_file = st.file_uploader(
                "**" + _("Upload the JSON File") + "**",
                accept_multiple_files=False,
                type="json",
            )
        submit = st.form_submit_button("**" + _("Submit") + "**")

    if submit:
        try:
            if method == _("Level ID"):
                response = download_level(level_id)
                level_name = response["name"]
                data = json.loads(response["data"])
            elif method == "JSON":
                level_name = uploaded_file.name
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                data = json.loads(stringio.read())

            output = flip_json(level_name, data)

            if method == _("Level ID"):
                uuid = upload_level(response, output)
                url = f"https://gooberdash.winterpixel.io?play={uuid}"
                st.write(_("The Level ID of the output Level is") + f" {uuid}")
                st.link_button(
                    "**" + _("Play Level on Browser") + "**", url, type="primary"
                )
            elif method == "JSON":
                st.download_button(
                    label=_("Download Output"),
                    data=output,
                    file_name=f"{level_name.replace('.json','')} "
                    + _("flipped")
                    + ".json",
                    mime="text/json",
                    type="primary",
                )

        except Exception as e:
            if method == _("Level ID"):
                st.error("Level not found")
                print(e)
            elif method == "JSON":
                st.error("Wrong JSON content")
                print(e)
