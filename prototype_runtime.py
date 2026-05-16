from pathlib import Path
import hmac
import os
import tomllib

import streamlit as st


ROOT = Path(__file__).resolve().parent


MENU_HTML = """
<div class="cp-navlinks" aria-label="Primary navigation">
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">DEVICE</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>DEVICE</strong><span>미용 디바이스 라인업과 정품 등록 진입</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>기기 라인업</p>
          <a href="/Product_Detail">듀얼테트라 <span class="cp-menu-status">P1</span></a>
          <a href="/Product_Detail">듀얼테트라 프로 <span class="cp-menu-status">P1</span></a>
          <a href="/Product_Detail">듀얼테트라 헤일로 <span class="cp-menu-status">P1</span></a>
          <a href="#">액세서리 / 정품 부품</a>
        </div>
        <div class="cp-menu-col">
          <p>구매 전후 지원</p>
          <a href="#">디바이스 비교하기</a>
          <a href="#">디바이스 사용법</a>
          <a href="/Device_Auth">정품 인증번호 등록 <span class="cp-menu-status is-hot">CRM</span></a>
          <a href="#">셀러브리티 / 앰버서더</a>
          <a href="#">디바이스 체험단</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">BOOSTER</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>BOOSTER</strong><span>바르는 부스터 제품과 루틴 조합</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>라인 / 카테고리</p>
          <a href="/BOOSTER">부스터 루틴팩 <span class="cp-menu-status">P1</span></a>
          <a href="/BOOSTER">데일리 글로우 라인</a>
          <a href="/BOOSTER">펌업 라인</a>
          <a href="/BOOSTER">라이트 라인</a>
          <a href="/BOOSTER">베어 라인</a>
          <a href="/BOOSTER">클리어 라인</a>
          <a href="/BOOSTER">컴포트 라인</a>
        </div>
        <div class="cp-menu-col">
          <p>추천 / 개인화</p>
          <a href="/PULSE_PICK">PULSE PICK <span class="cp-menu-status is-hot">핵심</span></a>
          <a href="#">MY BOOSTER ROUTINE</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">INNER</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>INNER</strong><span>이너뷰티 제품과 섭취 루틴 구조</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>라인 / 카테고리</p>
          <a href="#">이너 루틴팩</a>
          <a href="#">콜라겐 라인</a>
          <a href="#">글로우 라인</a>
          <a href="#">디톡스 라인</a>
          <a href="#">안티에이징 라인</a>
          <a href="#">슬립 라인</a>
        </div>
        <div class="cp-menu-col">
          <p>추천 / 개인화</p>
          <a href="#">INNER PICK</a>
          <a href="#">MY INNER ROUTINE</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">CALM</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>CALM</strong><span>수면, 무드, 아로마 중심의 마음 루틴</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>라인 / 카테고리</p>
          <a href="#">캄 루틴팩</a>
          <a href="#">슬립 라인</a>
          <a href="#">무드 라인</a>
          <a href="#">데이 라인</a>
          <a href="#">텐션 라인</a>
          <a href="#">아로마 라인</a>
        </div>
        <div class="cp-menu-col">
          <p>추천 / 개인화</p>
          <a href="#">CALM PICK</a>
          <a href="#">MY CALM ROUTINE</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">SCIENCE</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>SCIENCE</strong><span>기술 원리, 임상 데이터, 인증 신뢰 구조</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>근거 카테고리</p>
          <a href="/SCIENCE">DEVICE SCIENCE</a>
          <a href="/SCIENCE">BOOSTER SCIENCE</a>
          <a href="/SCIENCE">INNER SCIENCE</a>
          <a href="/SCIENCE">CALM SCIENCE</a>
        </div>
        <div class="cp-menu-col">
          <p>라이브러리</p>
          <a href="/SCIENCE">임상 데이터 라이브러리 <span class="cp-menu-status">P1</span></a>
          <a href="/SCIENCE">R&amp;D / 인증 / 파트너십</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">COMMUNITY</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>COMMUNITY</strong><span>루틴 공유, 리뷰, 멤버십 참여 영역</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>참여 콘텐츠</p>
          <a href="/ROUTINE_LAB">ROUTINE LAB <span class="cp-menu-status is-hot">MVP</span></a>
          <a href="#">리뷰</a>
          <a href="#">라이브 방송 <span class="cp-menu-status is-muted">P2</span></a>
          <a href="#">멤버십</a>
        </div>
        <div class="cp-menu-col">
          <p>체험단</p>
          <a href="#">일반 체험단</a>
          <a href="#">디바이스 체험단</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">BRAND</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>BRAND</strong><span>브랜드 철학과 신뢰 자산</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>브랜드 스토리</p>
          <a href="/PHILOSOPHY">PHILOSOPHY <span class="cp-menu-status">P1</span></a>
          <a href="#">앰버서더 / 셀러브리티</a>
          <a href="#">EWG / 지속가능성</a>
          <a href="#">비앙글로</a>
        </div>
        <div class="cp-menu-col">
          <p>회사 정보</p>
          <a href="#">회사 소개 / 뉴스</a>
          <a href="#">매장 안내 <span class="cp-menu-status is-muted">HIDE</span></a>
          <a href="#">채용 <span class="cp-menu-status is-muted">HIDE</span></a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <button class="cp-nav-trigger" type="button">SUPPORT</button>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>SUPPORT</strong><span>구매, 사용, A/S 지원 동선</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>고객 지원</p>
          <a href="#">공지</a>
          <a href="#">FAQ</a>
          <a href="#">1:1 문의</a>
          <a href="#">배송 / 반품</a>
        </div>
        <div class="cp-menu-col">
          <p>사용 / A/S</p>
          <a href="#">스킨케어 사용법</a>
          <a href="#">A/S 안내</a>
          <a href="/Device_Auth">A/S 접수 <span class="cp-menu-status is-hot">정품등록 연동</span></a>
        </div>
      </div>
    </div>
  </div>
</div>
"""


def expected_password() -> str | None:
    try:
        password = st.secrets.get("APP_PASSWORD")
        if password:
            return str(password)
    except Exception:
        pass

    password = os.environ.get("APP_PASSWORD")
    if password:
        return password

    local_secrets = ROOT / ".streamlit" / "secrets.toml"
    if local_secrets.exists():
        return tomllib.loads(local_secrets.read_text(encoding="utf-8-sig")).get("APP_PASSWORD")
    return None


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
    configured_password = expected_password()
    if not configured_password:
        st.error("APP_PASSWORD가 설정되지 않았습니다.")
        st.stop()

    password = st.text_input("Password", type="password", label_visibility="collapsed")
    if st.button("Enter", type="primary", use_container_width=True):
        if hmac.compare_digest(password, configured_password):
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
    html = (
        read_asset(template_path)
        .replace("{{TOKENS_CSS}}", css)
        .replace("{{NAV_MENU}}", MENU_HTML)
    )
    st.html(html, width="stretch")
