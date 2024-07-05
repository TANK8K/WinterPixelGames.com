import streamlit as st
import time
from ruamel.yaml import YAML
from streamlit_js_eval import streamlit_js_eval
from common_config import (
    get_manager,
    set_localization,
    back_to_home,
)

yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

_ = set_localization(st.session_state.language)

st.html(
    '<h4><i class="fa-solid fa-language" style="display: inline; margin: 0 10px 8px 0; width: 25px"></i>'
    + _("Language")
    + "</h4>"
)

st.html(
    """
    <style>
    div[data-testid="stAppViewContainer"] section:nth-child(2) div[data-testid="stAppViewBlockContainer"], div[data-testid="stAppViewContainer"] section:nth-child(3) div[data-testid="stAppViewBlockContainer"] {
        position: relative !important;
        bottom: 0px !important;
    }
    div[data-testid="stLinkButton"] > a[kind="primary"]::before{
        font-family: "Font Awesome 5 Free" !important;
        content: "\\f2b5";
        display: inline-block;
        vertical-align: middle;
        font-weight: 800;
        font-size: 18px;
        color: white;
        min-width: 35px;
        padding-left: 7px;
    }
    div[data-testid="stLinkButton"] button p, div[role="dialog"] div[data-testid="stLinkButton"] a p  {
        font-family: 'Baloo 2';
        font-weight: 700;
        font-size: 18px;
    }
    div[data-testid="stExpander"] a {
        border: none;
        box-shadow: none;
        background: transparent;
        color: white;
        padding: 0;
        margin: 0;
    }
    div[data-testid="stExpander"] p {
        font-family: 'Baloo 2' !impotant;
        font-weight: 700 !important;
        font-size: 18px !important;
    }
    div[data-testid="stExpander"] .row-widget.stLinkButton p::after {
        font-family: "Font Awesome 5 Free" !important;
        content: "\\f0c1";
        display: inline-block;
        vertical-align: middle;
        font-weight: 800;
        font-size: 15px;
        color: white;
        min-width: 35px;
        padding-left: 7px;
    }
    div[data-testid="stExpander"] a:hover {
        border: none;
        box-shadow: none;
        background: transparent;
        color: rgb(48, 151, 230);
        text-decoration: underline !important;
    }
    div[data-testid="stExpander"] .row-widget.stLinkButton {
        height: 18px;
    }
    button[data-testid="baseButton-secondary"]::before {
        font-family: "Font Awesome 5 Free" !important;
        content: "\\f058";
        display: inline-block;
        vertical-align: middle;
        font-weight: 800;
        font-size: 18px;
        color: white;
        padding-right: 7px;
    }
    div[data-testid="stExpanderDetails"] .row-widget.stLinkButton::before {
        content: "- ";
    }
    div[data-testid="stExpanderDetails"] div[data-testid="element-container"]:nth-child(3) {
        display: contents !important;
    }
    </style>"""
)

languages_dict = {
    "english": "🇺🇸 English ✅",
    "zh-TW": "🇹🇼 繁體中文 ✅",
    "zh-CN": "🇨🇳 簡体中文 ✅",
    "fr": "🇫🇷 Français 🚧",
    "es-ES": "🇪🇸 Español 🚧",
    "it": "🇮🇹 Italiano 🚧",
    "de": "🇩🇪 Deutsch 🚧",
    "nl": "🇳🇱 Nederlands 🚧",
    "pt-PT": "🇵🇹 Português 🚧",
    "pt-BR": "🇧🇷 Português brasileir 🚧",
    "da": "🇩🇰 Dansk 🚧",
    "nb": "🇳🇴 Norsk bokmål 🚧",
    "no": "🇳🇴 Norsk 🚧",
    "sv-SE": "🇸🇪 Svenska 🚧",
    "fi": "🇫🇮 Suomi 🚧",
    "pl": "🇵🇱 Polski 🚧",
    "uk": "🇺🇦 Українська 🚧",
    "ru": "🇷🇺 Русский 🚧",
    "sk": "🇸🇰 Slovenský 🚧",
    "sl": "🇸🇮 Slovenščina 🚧",
    "bg": "🇧🇬 Български 🚧",
    "cs": "🇨🇿 Čeština 🚧",
    "ro": "🇷🇴 Română 🚧",
    "et": "🇪🇪 Eesti 🚧",
    "el": "🇬🇷 Ελληνική 🚧",
    "hu": "🇭🇺 Magyar 🚧",
    "lv": "🇱🇻 Latviešu 🚧",
    "lt": "🇱🇹 Lietuvių 🚧",
    "tr": "🇹🇷 Türkçe 🚧",
    "id": "🇮🇩 Bahasa Indonesia 🚧",
    "ar": "🇸🇦 العربية 🚧",
    "ko": "🇰🇷 한국어 🚧",
    "ja": "🇯🇵 日本語 🚧",
}

languages = [language for language in languages_dict]
languages.insert(0, languages.pop(languages.index(st.session_state.language)))

st.session_state.language = st.selectbox(
    " ",
    languages,
    format_func=lambda x: languages_dict.get(x),
    label_visibility="collapsed",
)

cookie_manager = get_manager("pop_choose_language")
cookie_manager.set("locale", st.session_state.language)

if st.button("**" + _("Apply") + "**"):
    time.sleep(1)
    st.switch_page("all_pages/0 Home.py")

st.markdown("####")

with st.expander(_("Contributors") + """ (""" + _("In no particular order") + ")"):
    st.link_button(
        "Stickman A",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    )
    st.link_button(
        "shimobri",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    )
    st.link_button(
        "TANK8K",
        "https://github.com/TANK8K/",
    )

st.link_button(
    "**" + _("Contribute") + "**",
    "https://translate.winterpixelgames.com/",
    type="primary",
)

back_to_home(st.session_state.language)
