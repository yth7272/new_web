# 001. 2026-05-16 변경 요구 사항

## 요청 요약

- 현재 new web 프로토타입에서 암호 입력 화면을 제거한다.
- 기존 `FM 모드`, `Firm Up`, `펌업` 계열 명칭은 더 이상 사용하지 않는다.
- 해당 명칭을 `Fomular 모드`로 변경하고, 의미 설명은 `유효성분 침투 모드`로 통일한다.
- 변경 요구 사항은 `docs/requirement` 하위에 번호와 날짜를 포함해 기록한다.

## 반영 범위

- Streamlit 메인 진입 화면의 암호 입력 및 `APP_PASSWORD` 의존 로직 제거.
- 디자인 시스템 샘플, 메인 페이지, BOOSTER, PULSE PICK, ROUTINE LAB, SCIENCE, CART/CHECKOUT, 제품 상세 템플릿의 노출 문구 변경.
- mock data의 대표 루틴명 변경.
- 내비게이션 메가 메뉴와 정적 preview/master board/카테고리 가이드 문서의 관련 명칭 변경.

## 검증 시나리오

- 앱 진입 시 암호 입력 필드 없이 메인 페이지가 바로 렌더링되는지 확인한다.
- 저장소 전체에서 `APP_PASSWORD`, `Password`, `비밀번호`, `require_auth`, `Firm Up`, `FIRM`, `펌업` 잔여 문구가 없는지 검색한다.
- Python 파일이 문법 오류 없이 컴파일되는지 확인한다.
- Streamlit 서버가 정상 기동되고 HTTP 응답을 반환하는지 확인한다.

## 운영 리스크 메모

- 이번 변경은 인증 게이트를 제거하므로 회의용 공개 범위가 넓어진다. 외부에 노출되는 배포 환경이라면 별도 접근 제어가 필요한지 배포 전에 확인해야 한다.
- 주기 실행 또는 백그라운드 작업은 포함되지 않아 Retry, Dead man's switch, Health Check 추가 대상은 없다.
