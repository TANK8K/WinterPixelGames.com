import streamlit as st
import streamlit_authenticator as stauth
import uuid
from ruamel.yaml import YAML
from common_config import (
    back_to_home,
    get_manager,
    set_localization,
)

_ = set_localization(st.session_state.language)

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

cookie_manager = get_manager("account")
logged_in_user_username = cookie_manager.get(cookie="username")
saved_account = cookie_manager.get(cookie="account")


def validate_user_id(uuid_str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str
    except ValueError:
        return False


if saved_account is not None:
    st.html(
        '<h4><i class="fa-solid fa-address-card" style="display: inline; margin: 0 10px 8px 0; width: 25px"></i>'
        + _("Account")
        + "</h4>"
    )

    st.html(
        """
        <style>
        div[data-testid="stForm"] {
            border: none;
            padding: 0;
        }
        div[data-testid="stAppViewContainer"] section:nth-child(2) div[data-testid="stAppViewBlockContainer"], div[data-testid="stAppViewContainer"] section:nth-child(3) div[data-testid="stAppViewBlockContainer"] {
            position: relative !important;
            bottom: 0px !important;
        }
        </style>"""
    )

    with open("config.yaml", "r") as file:
        config = yaml.load(file)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["pre-authorized"],
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "**" + _("Linked Game Accounts") + "**",
            "**" + _("Change Nickname/Email") + "**",
            "**" + _("Change Password") + "**",
        ]
    )

    with tab1:
        with st.form("Linked Game Accounts"):
            st.markdown("### " + _("Linked Game Accounts"))
            st.info(
                _(
                    "Statistics of Linked Accounts will be tracked daily and displayed in Player Info"
                )
                + " ("
                + _("WIP")
                + ")",
                icon="ℹ️",
            )
            try:
                user_id_RBR_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_RBR"]
            except KeyError:
                user_id_RBR_record = ""
            try:
                user_id_GD_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_GD"]
            except KeyError:
                user_id_GD_record = ""
            try:
                user_id_GR_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_GR"]
            except KeyError:
                user_id_GR_record = ""
            try:
                user_id_GS_record = config["credentials"]["usernames"][
                    logged_in_user_username
                ]["user_id_GS"]
            except KeyError:
                user_id_GS_record = ""

            user_id_RBR = st.text_input(
                "**" + _("Rocket Bot Royale") + "**",
                value=user_id_RBR_record,
                placeholder=_("No User ID Found") if user_id_RBR_record == "" else None,
                max_chars=36,
            )
            user_id_GD = st.text_input(
                "**" + _("Goober Dash") + "**",
                value=user_id_GD_record,
                placeholder=_("No User ID Found") if user_id_GD_record == "" else None,
                max_chars=36,
            )
            user_id_GR = st.text_input(
                "**" + _("Goober Royale") + "**",
                value=user_id_GR_record,
                placeholder=_("No User ID Found") if user_id_GR_record == "" else None,
                max_chars=36,
            )
            user_id_GS = st.text_input(
                "**" + _("Goober Shot") + "**",
                value=user_id_GS_record,
                placeholder=_("No User ID Found") if user_id_GS_record == "" else None,
                max_chars=36,
            )
            user_id_dict = {
                "user_id_RBR": user_id_RBR,
                "user_id_GD": user_id_GD,
                "user_id_GR": user_id_GR,
                "user_id_GS": user_id_GS,
            }
            convert_to_game_name_dict = {
                "user_id_RBR": _("Rocket Bot Royale"),
                "user_id_GD": _("Goober Dash"),
                "user_id_GR": _("Goober Royale"),
                "user_id_GS": _("Goober Shot"),
            }
            Update_button = st.form_submit_button(_("Update"))
            if Update_button:
                correct_format_all = True
                for key in user_id_dict:
                    if user_id_dict[key] != "":
                        if not validate_user_id(user_id_dict[key]):
                            st.error(
                                _("Wrong User ID format of ")
                                + convert_to_game_name_dict[key]
                            )
                            correct_format_all = False
                            break
                        else:
                            config["credentials"]["usernames"][logged_in_user_username][
                                key
                            ] = user_id_dict[key]
                if correct_format_all:
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("User IDs are updated successfully"))
    with tab2:
        if saved_account is not None:
            try:
                if authenticator.update_user_details(
                    logged_in_user_username,
                    fields={
                        "Form name": _("Change Name/Email"),
                        "Field": _("Field"),
                        "Name": _("Nickname"),
                        "Email": _("Email"),
                        "New value": _("New value"),
                        "Update": _("Update"),
                    },
                ):
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("Entries updated successfully"))
            except Exception as e:
                st.error(e)

    with tab3:
        if saved_account is not None:
            try:
                if authenticator.reset_password(
                    logged_in_user_username,
                    fields={
                        "Form name": _("Change Password"),
                        "Current password": _("Current Password"),
                        "New password": _("New Password"),
                        "Repeat password": _("Repeat Password"),
                        "Reset": _("Reset"),
                    },
                ):
                    with open("config.yaml", "w") as file:
                        yaml.dump(config, file)
                    st.success(_("Password modified successfully"))
            except Exception as e:
                st.error(e)
    back_to_home(st.session_state.language)
