from pathlib import Path
import hmac
import os

import streamlit as st


ROOT = Path(__file__).resolve().parent
DEFAULT_PROTOTYPE_PASSWORD = "curapulse2026"


def expected_password() -> str:
    try:
        return st.secrets.get("APP_PASSWORD", DEFAULT_PROTOTYPE_PASSWORD)
    except Exception:
        return os.environ.get("APP_PASSWORD", DEFAULT_PROTOTYPE_PASSWORD)


def require_password() -> None:
    if st.session_state.get("prototype_unlocked"):
        return

    st.markdown(
        """
        <style>
        .block-container { max-width: 520px; padding-top: 18vh; }
        header[data-testid="stHeader"] { display: none; }
        section[data-testid="stSidebar"] { display: none; }
        button[data-testid="stBaseButton-headerNoPadding"] { display: none; }
        div[data-testid="stToolbar"] { display: none; }
        div[data-testid="stDecoration"] { display: none; }
        div[data-testid="stStatusWidget"] { display: none; }
        div[data-testid="stAppDeployButton"] { display: none; }
        #MainMenu, footer { visibility: hidden; }
        .cp-login-title { font-size: 34px; font-weight: 900; letter-spacing: -0.04em; margin-bottom: 8px; }
        .cp-login-copy { color: #4f565f; line-height: 1.6; margin-bottom: 24px; }
        </style>
        <div class="cp-login-title">CuraPulse Prototype</div>
        <div class="cp-login-copy">회의용 프로토타입입니다. 비밀번호를 입력하면 페이지를 볼 수 있습니다.</div>
        """,
        unsafe_allow_html=True,
    )
    password = st.text_input("Password", type="password", label_visibility="collapsed")
    if st.button("Enter", type="primary", use_container_width=True):
        if hmac.compare_digest(password, expected_password()):
            st.session_state["prototype_unlocked"] = True
            st.rerun()
        st.error("비밀번호가 맞지 않습니다.")
    st.stop()


def setup_page(title: str) -> None:
    st.set_page_config(
        page_title=f"{title} | CuraPulse Prototype",
        page_icon="CP",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    require_password()
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
