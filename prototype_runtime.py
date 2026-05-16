from pathlib import Path

import streamlit as st


ROOT = Path(__file__).resolve().parent


MENU_HTML = """
<div class="cp-navlinks" aria-label="Primary navigation">
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/DEVICE">DEVICE</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>DEVICE</strong><span>미용 디바이스 라인업과 정품 등록 진입</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>기기 라인업</p>
          <a href="/Product_Detail">듀얼테트라 <span class="cp-menu-status">P1</span></a>
          <a href="/Product_Detail">듀얼테트라 프로 <span class="cp-menu-status">P1</span></a>
          <a href="/Product_Detail">듀얼테트라 헤일로 <span class="cp-menu-status">P1</span></a>
          <a href="/DEVICE">액세서리 / 정품 부품</a>
        </div>
        <div class="cp-menu-col">
          <p>구매 전후 지원</p>
          <a href="/DEVICE">디바이스 비교하기</a>
          <a href="/DEVICE">디바이스 사용법</a>
          <a href="/Device_Auth">정품 인증번호 등록 <span class="cp-menu-status is-hot">CRM</span></a>
          <a href="/PHILOSOPHY">셀러브리티 / 앰버서더</a>
          <a href="/ROUTINE_LAB">디바이스 체험단</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/BOOSTER">BOOSTER</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>BOOSTER</strong><span>바르는 부스터 제품과 루틴 조합</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>라인 / 카테고리</p>
          <a href="/BOOSTER">부스터 루틴팩 <span class="cp-menu-status">P1</span></a>
          <a href="/GIFT">선물하기 큐레이션 <span class="cp-menu-status">P1</span></a>
          <a href="/BOOSTER">데일리 글로우 라인</a>
          <a href="/BOOSTER">Fomular 모드</a>
          <a href="/BOOSTER">라이트 라인</a>
          <a href="/BOOSTER">베어 라인</a>
          <a href="/BOOSTER">클리어 라인</a>
          <a href="/BOOSTER">컴포트 라인</a>
        </div>
        <div class="cp-menu-col">
          <p>추천 / 개인화</p>
          <a href="/PULSE_PICK">PULSE PICK <span class="cp-menu-status is-hot">핵심</span></a>
          <a href="/PULSE_PICK">MY BOOSTER ROUTINE</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/INNER">INNER</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>INNER</strong><span>이너뷰티 제품과 섭취 루틴 구조</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>라인 / 카테고리</p>
          <a href="/INNER">이너 루틴팩</a>
          <a href="/INNER">콜라겐 라인</a>
          <a href="/INNER">글로우 라인</a>
          <a href="/INNER">디톡스 라인</a>
          <a href="/INNER">안티에이징 라인</a>
          <a href="/INNER">슬립 라인</a>
        </div>
        <div class="cp-menu-col">
          <p>추천 / 개인화</p>
          <a href="/INNER">INNER PICK</a>
          <a href="/INNER">MY INNER ROUTINE</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/CALM">CALM</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>CALM</strong><span>수면, 무드, 아로마 중심의 마음 루틴</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>라인 / 카테고리</p>
          <a href="/CALM">캄 루틴팩</a>
          <a href="/CALM">슬립 라인</a>
          <a href="/CALM">무드 라인</a>
          <a href="/CALM">데이 라인</a>
          <a href="/CALM">텐션 라인</a>
          <a href="/CALM">아로마 라인</a>
        </div>
        <div class="cp-menu-col">
          <p>추천 / 개인화</p>
          <a href="/CALM">CALM PICK</a>
          <a href="/CALM">MY CALM ROUTINE</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/SCIENCE">SCIENCE</a>
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
    <a class="cp-nav-trigger" href="/ROUTINE_LAB">COMMUNITY</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>COMMUNITY</strong><span>루틴 공유, 리뷰, 멤버십 참여 영역</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>참여 콘텐츠</p>
          <a href="/ROUTINE_LAB">ROUTINE LAB <span class="cp-menu-status is-hot">MVP</span></a>
          <a href="/ROUTINE_LAB">리뷰</a>
          <a href="/POLICY_MOCKUPS">라이브 방송 <span class="cp-menu-status is-muted">P2</span></a>
          <a href="/POLICY_MOCKUPS">멤버십</a>
        </div>
        <div class="cp-menu-col">
          <p>체험단</p>
          <a href="/ROUTINE_LAB">일반 체험단</a>
          <a href="/ROUTINE_LAB">디바이스 체험단</a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/PHILOSOPHY">BRAND</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>BRAND</strong><span>브랜드 철학과 신뢰 자산</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>브랜드 스토리</p>
          <a href="/PHILOSOPHY">PHILOSOPHY <span class="cp-menu-status">P1</span></a>
          <a href="/PHILOSOPHY">앰버서더 / 셀러브리티</a>
          <a href="/PHILOSOPHY">EWG / 지속가능성</a>
          <a href="/PHILOSOPHY">비앙글로</a>
        </div>
        <div class="cp-menu-col">
          <p>회사 정보</p>
          <a href="/PHILOSOPHY">회사 소개 / 뉴스</a>
          <a href="/SUPPORT">매장 안내 <span class="cp-menu-status is-muted">HIDE</span></a>
          <a href="/SUPPORT">채용 <span class="cp-menu-status is-muted">HIDE</span></a>
        </div>
      </div>
    </div>
  </div>
  <div class="cp-nav-item">
    <a class="cp-nav-trigger" href="/SUPPORT">SUPPORT</a>
    <div class="cp-mega" role="menu">
      <div class="cp-mega-head"><strong>SUPPORT</strong><span>구매, 사용, A/S 지원 동선</span></div>
      <div class="cp-mega-grid">
        <div class="cp-menu-col">
          <p>고객 지원</p>
          <a href="/SUPPORT">공지</a>
          <a href="/SUPPORT">FAQ</a>
          <a href="/SUPPORT">1:1 문의</a>
          <a href="/SUPPORT">배송 / 반품</a>
        </div>
        <div class="cp-menu-col">
          <p>사용 / A/S</p>
          <a href="/SUPPORT">스킨케어 사용법</a>
          <a href="/SUPPORT">A/S 안내</a>
          <a href="/Device_Auth">A/S 접수 <span class="cp-menu-status is-hot">정품등록 연동</span></a>
        </div>
      </div>
    </div>
  </div>
</div>
"""


FOOTER_HTML = """
<footer class="cp-footer">
  <div class="cp-footer-grid">
    <div>
      <strong>curapulse+</strong>
      <p>회의용 프로토타입 v0.2 · 실제 Cafe24 운영 코드가 아닌 의사결정용 시각 명세입니다.</p>
    </div>
    <div>
      <p class="cp-footer-title">SHOP</p>
      <a href="/DEVICE">DEVICE</a>
      <a href="/BOOSTER">BOOSTER</a>
      <a href="/INNER">INNER</a>
      <a href="/CALM">CALM</a>
    </div>
    <div>
      <p class="cp-footer-title">DECISION</p>
      <a href="/DECISION_BACKLOG">Decision Backlog</a>
      <a href="/CAFE24_DEV_CHECK">Cafe24 DEV CHECK</a>
      <a href="/POLICY_MOCKUPS">Policy Mockups</a>
    </div>
    <div>
      <p class="cp-footer-title">SUPPORT</p>
      <a href="/Device_Auth">정품등록</a>
      <a href="/SUPPORT">FAQ / A/S</a>
      <a href="/CART_CHECKOUT">Cart Mock</a>
    </div>
  </div>
</footer>
"""


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
    html = (
        read_asset(template_path)
        .replace("{{TOKENS_CSS}}", css)
        .replace("{{NAV_MENU}}", MENU_HTML)
        .replace("{{FOOTER}}", FOOTER_HTML)
    )
    if "cp-footer" not in html:
        html = html.replace("</main>", f"{FOOTER_HTML}</main>")
    st.html(html, width="stretch")
