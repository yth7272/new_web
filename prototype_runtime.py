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


def render_placeholder(page_key: str, page_title: str, intent: str, *, height: int = 900) -> None:
    css = read_asset("assets/tokens.css")
    html = f"""
    <!doctype html>
    <html lang="ko">
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=1440, initial-scale=1" />
      <style>{css}</style>
    </head>
    <body>
      <div class="cp-app">
        <header class="cp-topbar">
          <div class="cp-promo">CuraPulse Prototype v0.1 · Desktop meeting build</div>
          <nav class="cp-nav">
            <div class="cp-logo">curapulse<span>+</span></div>
            <div class="cp-navlinks">
              <a>DEVICE</a><a>BOOSTER</a><a>INNER</a><a>CALM</a>
              <a>SCIENCE</a><a>COMMUNITY</a><a>BRAND</a><a>SUPPORT</a>
            </div>
            <div class="cp-actions"><span>LOGIN</span><span>CART</span><span>SEARCH</span></div>
          </nav>
        </header>
        <main class="cp-shell">
          <section class="cp-page-hero">
            <p class="cp-kicker">{page_key}</p>
            <h1>{page_title}</h1>
            <p>{intent}</p>
            <div class="cp-button-row">
              <button class="cp-btn cp-btn-primary">GO / MODIFY 판단</button>
              <button class="cp-btn cp-btn-ghost">회의 메모</button>
            </div>
          </section>
          <section class="cp-placeholder-grid">
            <article class="cp-panel">
              <p class="cp-kicker">Prototype Scope</p>
              <h2>이 화면에서 검증할 것</h2>
              <p>실제 결제, 검색, 회원 기능은 구현하지 않고 동선과 정보 배치만 검증합니다. 카페24 이관 시 살아남는 것은 코드가 아니라 구조, 카피, 디자인 규칙입니다.</p>
            </article>
            <article class="cp-panel">
              <p class="cp-kicker">Next Design Pass</p>
              <h2>다음 작업</h2>
              <p>디자인 시스템 승인 후 이 화면의 실제 섹션, 카드, 폼, CTA를 Claude Design 산출물 기준으로 채웁니다.</p>
            </article>
          </section>
        </main>
      </div>
    </body>
    </html>
    """
    st.html(html, width="stretch")
