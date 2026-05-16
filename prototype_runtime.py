from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent


def setup_page(title: str) -> None:
    st.set_page_config(
        page_title=f"{title} | CuraPulse Prototype",
        page_icon="CP",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    st.markdown(
        """
        <style>
        .block-container { padding: 0; max-width: none; }
        header[data-testid="stHeader"] { display: none; }
        section[data-testid="stSidebar"] { display: none; }
        button[data-testid="stBaseButton-headerNoPadding"] { display: none; }
        div[data-testid="stToolbar"] { display: none; }
        div[data-testid="stDecoration"] { display: none; }
        div[data-testid="stStatusWidget"] { display: none; }
        div[data-testid="stAppDeployButton"] { display: none; }
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def read_asset(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def render_template(template_path: str, *, height: int = 1200) -> None:
    css = read_asset("assets/tokens.css")
    html = read_asset(template_path).replace("{{TOKENS_CSS}}", css)
    st.html(html, width="stretch")
