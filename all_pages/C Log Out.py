import streamlit as st
import time
from ruamel.yaml import YAML
from common_config import (
    back_to_home,
    get_manager,
    set_localization,
)

_ = set_localization(st.session_state.language)

if st.session_state["logged_in"] == False:
    st.markdown(_("You are now logged out"))
    back_to_home(_)

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

_ = set_localization(st.session_state.language)
cookie_manager = get_manager("log_out")
logged_in_user_username = cookie_manager.get(cookie="username")

with open("config.yaml", "r") as file:
    config = yaml.load(file)
config["credentials"]["usernames"][logged_in_user_username]["logged_in"] = False
with open("config.yaml", "w") as file:
    yaml.dump(config, file)

st.session_state["logged_in"] = True
try:
    cookie_manager_2 = get_manager("delete_account_cookie")
    cookie_manager_2.delete(cookie="account", key="delete_cookie_account")
except Exception:
    pass
try:
    cookie_manager_3 = get_manager("delete_name_cookie")
    cookie_manager_3.delete(cookie="name", key="delete_cookie_name")
except Exception:
    pass
try:
    cookie_manager_4 = get_manager("delete_username_cookie")
    cookie_manager_4.delete(cookie="username", key="delete_cookie_username")
except Exception:
    pass
time.sleep(1)
st.switch_page("all_pages/0 Home.py")
