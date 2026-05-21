# 05. KPI 이벤트 정의서

> 출처: `00-goals.md` Sub-goal S1~S5 KPI
> 목적: 각 KPI를 실제로 측정하기 위해 어떤 이벤트를 어디서 어떤 파라미터로 발화시킬지 정의
> 적용 task: `02-tasks-phase1.md` 운영/검수 섹션의 KPI 측정 가능성 확인(T-OP06)
> 작성일: 2026-05-19
>
> **표기 규칙**
> - 이벤트명: GA4 표준 이벤트는 그대로, 자체 커스텀은 `snake_case`
> - 측정 위치: 페이지 또는 액션
> - 발화 책임: 해당 task ID

---

## 1. 이벤트 아키텍처 한눈에

```
사용자 액션
   ↓
브라우저 GA4 (dataLayer + gtag)
   ↓
   ├─→ GA4 대시보드 (S1·S2·S4·S5 분석)
   └─→ Cafe24 주문 데이터 + 자체 CRM 이벤트 hook (S2·S3 측정)
              ↓
        BigQuery / 자체 DB (LTV·후속 구매율 분석)
```

3개 채널을 합쳐서 봐야 S1~S5 모두 측정 가능합니다.
- **GA4**: 페이지뷰, 클릭, 스크롤, 체류 (S1·S4 핵심)
- **Cafe24 주문**: AOV, 카트 구성 (S2 핵심)
- **자체 CRM 이벤트**: 정품등록, 후속 구매, 디바이스↔부스터 크로스셀 (S3·S5 핵심)

---

## 2. S1. 신규 의사결정 가속

| KPI | 이벤트명 | 발화 위치 | 핵심 파라미터 | 대시보드 | 발화 책임 task |
|---|---|---|---|---|---|
| **방문→PDP 도달율** | `view_item` (GA4 표준) | 모든 PDP 진입 시 | `item_id`, `item_name`, `item_category` (=라인), `item_list_name` (=진입 출처) | GA4 탐색 — Funnel | T-DV01, T-DV02, T-DV03, T-BO11 |
| **PDP→장바구니율** | `add_to_cart` (GA4 표준) | 카트 담기 클릭 시 | `item_id`, `value`, `quantity`, `entry_source` (custom) | GA4 Funnel | T-DV01~03, T-BO 라인 PDP |
| **평균 클릭 수** | `click_path_step` (custom) | 메인 → 진입 바 → 4라인 카드 → PDP 각 클릭 | `step_n`, `from_page`, `to_page` | GA4 탐색 + Looker | T-C02, T-C03, T-C04, T-ME01~04 |
| **추천 진입 바 클릭율** | `select_promotion` (GA4 표준) | 추천 빠른 진입 바 6개 카드 클릭 | `promotion_id`, `promotion_name`, `slot_position` | GA4 — 프로모션 | T-C03 |
| **다중 진입로 탭 사용율** | `entry_path_tab` (custom) | 라인/고민/유형/선물 탭 전환 | `tab` (=line/concern/type/gift), `category` (=BOOSTER/INNER/CALM) | GA4 + Looker | T-ME01 |

> **S1 핵심 funnel**: `page_view(메인)` → `select_promotion or click_path_step` → `view_item` → `add_to_cart`

---

## 3. S2. 객단가 상승

| KPI | 이벤트명 | 발화 위치 | 핵심 파라미터 | 대시보드 | 발화 책임 task |
|---|---|---|---|---|---|
| **평균 객단가(AOV)** | `purchase` (GA4 표준) + Cafe24 주문 | 결제 완료 | `transaction_id`, `value`, `items[]`, `tax`, `shipping` | GA4 + Cafe24 + Looker | 결제 흐름 (Cafe24 기본) |
| **카트 내 상품 수** | `purchase` (GA4) `items[]` 길이 | 결제 완료 | `items[]` (count 추출) | GA4 — 전자상거래 | (위 동일) |
| **PULSE PICK 묶음 구매율** | `purchase` + `bundle_type` 파라미터 | 결제 완료 | `bundle_type` (=`pulse_pick` / `routine_pack` / `gift` / `none`) | Looker | T-BO10 (PULSE PICK), T-BO09 (루틴팩), T-ME04 (선물하기) |
| **루틴팩 카트 비중** | (위 동일, `bundle_type=routine_pack` 필터) | — | — | Looker | T-BO09 |
| **선물하기 객단가** | (위 동일, `bundle_type=gift` 필터) + `gift_options` | 결제 완료 | `gift_options[]` (=`wrap`, `card`, `anonymous`, `receipt_split`) | Looker | T-ME04, T-ME05 |

> **bundle_type 분류 룰**: 카트에 PULSE PICK SKU 1개 이상 = `pulse_pick`, 루틴팩 SKU = `routine_pack`, 선물하기 페이지 진입 후 구매 = `gift`. 우선순위: gift > pulse_pick > routine_pack.

---

## 4. S3. 재구매 CRM 자동화

| KPI | 이벤트명 | 발화 위치 | 핵심 파라미터 | 대시보드 | 발화 책임 task |
|---|---|---|---|---|---|
| **정품등록 전환율** | `device_registration_complete` (custom) | 정품등록 완료 시 | `device_sku`, `serial_id`, `purchase_date`, `is_member`, `registered_within_days` | 자체 CRM + Looker | **T-DV15** (등록 후 CRM 이벤트 발행) |
| **정품등록 시작율** | `device_registration_start` (custom) | 정품등록 페이지 진입 + 시리얼 입력 시작 | `entry_point` (=Hero/SUPPORT/마이페이지) | GA4 + Looker | T-DV10 |
| **디바이스 구매자 후속 부스터 구매율** | `subsequent_purchase_after_device` (custom) | 디바이스 구매 후 N일 내 부스터 구매 발생 시 | `device_purchase_date`, `subsequent_sku`, `days_between` | 자체 CRM (Cafe24 주문 + 회원 ID 조인) | T-DV15 + Cafe24 데이터 |
| **정품등록 리워드 사용율** | `reward_redeemed` (custom) | 리워드 사용(샘플 키트 수령 or 쿠폰 사용) 시 | `reward_type`, `device_purchase_date` | 자체 CRM | T-DV14 (리워드 적립 로직) |
| **마이페이지 정품등록 현황 조회** | `view_my_devices` (custom) | 마이페이지 정품등록 섹션 진입 시 | `device_count`, `as_pending_count` | GA4 | T-AC03 |

> **회원 ID 매핑이 핵심**: S3는 회원 ID로 GA4·Cafe24·자체 CRM을 조인할 수 있어야 측정 가능. T-AC01(회원 시스템 매핑)이 완료되어야 S3 KPI 측정 가능.

---

## 5. S4. 신뢰 → 전환

| KPI | 이벤트명 | 발화 위치 | 핵심 파라미터 | 대시보드 | 발화 책임 task |
|---|---|---|---|---|---|
| **PDP 체류시간** | GA4 자동 (engagement_time) | 모든 PDP | (자동) `engagement_time_msec` | GA4 — 페이지 분석 | (자동, 추가 작업 없음) |
| **PDP CTA 클릭율** | `add_to_cart` + `view_item_to_cart_ratio` | PDP에서 카트 담기 | (S1과 동일) | GA4 Funnel | T-DV01~03, T-BO11 |
| **SCIENCE 6요소 영역 도달율** | `scroll_to_science_section` (custom) | PDP 내 SCIENCE 6요소 영역(메커니즘/임상/인증) 70% 노출 시 | `pdp_id`, `section_name` | GA4 + Looker | T-SC01 (PDP 표준 모듈) |
| **임상 출처 클릭율** | `clinical_source_click` (custom) | 임상 카드에서 출처 링크 클릭 | `source_url`, `pdp_id` | GA4 | T-SC01, T-SC04 |
| **리뷰 노출 클릭율** | `select_content` (GA4 표준, `content_type=review`) | PDP 리뷰 섹션 클릭 시 | `content_id`, `content_type=review`, `has_photo` | GA4 | T-CM02 (리뷰 통합 설계) |

> **S4 측정의 전제**: T-SC01(PDP 6요소 표준 모듈)이 모든 신규 PDP에 적용되어 있어야 함. 그렇지 않으면 비교 불가.

---

## 6. S5. 라인 자산화

| KPI | 이벤트명 | 발화 위치 | 핵심 파라미터 | 대시보드 | 발화 책임 task |
|---|---|---|---|---|---|
| **라인별 검색 유입 점유** | GA4 자동 (`source/medium`, `landing_page`) | 외부 검색 유입 시 | `landing_page` (=라인 페이지 URL), `keyword` (가능 시) | GA4 — Acquisition | T-BO03~08 (부스터 6라인 페이지 SEO 메타) |
| **라인 평균 GMV** | `purchase` (GA4) + `items[].item_category` | 결제 완료 | `item_category` (=라인명) | Looker | T-C09 (상품명 공식), Cafe24 SKU 카테고리 매핑 |
| **광고 라인 단가 효율** | `purchase` + `utm_*` 파라미터 | 결제 완료 | `utm_campaign`, `utm_content` (=라인명) + 광고비 외부 입력 | Looker | 마케팅 운영 |
| **라인 페이지 → PDP 진입율** | `select_item` (GA4) + `item_list_name` | 라인 페이지에서 SKU 클릭 | `item_list_name` (=라인명+`_line_page`), `item_id` | GA4 | T-BO03~08 |
| **라인 SCIENCE 진입율** | `science_page_view` (custom) | 라인 페이지에서 SCIENCE 진입 CTA 클릭 | `line_name`, `science_section` | GA4 | T-BO03~08 + T-SC03 |

> **S5 측정의 전제**: T-BO01(부스터 라인 슬로건 6개 확정)과 T-C09(상품명 공식 적용)가 완료되어 SKU의 `item_category`가 라인명으로 일관 매핑되어야 함.

---

## 7. 데이터 모델 — 최소 공통 파라미터

모든 이벤트는 가능한 한 다음 공통 파라미터를 함께 보냅니다. 회원 ID 매핑은 S3 측정의 전제.

| 파라미터 | 값 예시 | 필요 시점 |
|---|---|---|
| `user_id` | 회원 ID (Cafe24) | 모든 로그인 사용자 (T-AC01 완료 후) |
| `client_id` | GA4 자동 | 모든 이벤트 |
| `session_id` | GA4 자동 | 모든 이벤트 |
| `device_type` | `mobile` / `tablet` / `desktop` | 모든 이벤트 |
| `is_member` | `true` / `false` | 모든 이벤트 |
| `entry_path_origin` | 직전 진입 페이지 카테고리 (=`home` / `recommend_bar` / `gnb` / `search`) | view_item, add_to_cart |

---

## 8. 대시보드 구성 권고

운영자가 매주/매월 확인할 화면.

| 대시보드 | 도구 | 위젯 | 새로고침 주기 |
|---|---|---|---|
| **주간 매출/전환 요약** | GA4 + Looker | AOV, 카트 상품 수, S1 funnel | 주 1회 자동 |
| **정품등록 모니터** | 자체 CRM | 일별 등록 수, 등록 전환율, 리워드 사용율, 후속 부스터 구매 | 일 1회 |
| **라인 자산 효율** | Looker | 라인별 GMV, 검색 유입, 광고 단가 | 주 1회 |
| **PDP 신뢰 지표** | GA4 | PDP 체류·SCIENCE 영역 도달율·CTA 클릭율 | 주 1회 |
| **리뷰/루틴 행동** | GA4 | 리뷰 클릭율, 루틴랩 진입 후 구매 | 주 1회 |

---

## 9. 02-tasks-phase1.md에 추가해야 할 task (KPI 측정 가능성 보강)

현 02 task에는 GA4·이벤트 태깅 task가 없습니다. T-OP06(배포 전 최종 검토)의 AC가 "S1~S5 KPI 측정 가능 상태"이므로 다음 task가 추가되어야 합니다.

| 신규 task ID 후보 | 제목 | 산출물 | 의존성 | MVP 컷 |
|---|---|---|---|---|
| T-AN01 | GA4·Looker 계정/속성 셋업 + 기본 페이지뷰 검증 | GA4 속성, 측정 ID, 기본 페이지뷰 작동 확인 | T-D03 (Cafe24 GTM 가능 여부) | must-open |
| T-AN02 | GA4 표준 이벤트 태깅 (view_item / add_to_cart / purchase) | 모든 PDP/카트/결제에 표준 이벤트 발화 | T-AN01, T-DV01~03, T-BO11 | must-open |
| T-AN03 | 커스텀 이벤트 태깅 (S1·S3·S4·S5 본 문서 정의) | 커스텀 이벤트 발화 + 파라미터 검증 | T-AN02, T-DV15, T-SC01 | must-open |
| T-AN04 | 주간 매출/전환 + 정품등록 모니터 대시보드 | Looker 대시보드 2개 | T-AN02, T-AN03 | post-open |
| T-AN05 | 라인 자산 효율 + PDP 신뢰 대시보드 | Looker 대시보드 2개 | T-AN02, T-AN03 | post-open |

> **다음 작업**: 02-tasks-phase1.md에 위 5개 task를 "9.5 분석/추적" 섹션으로 추가하고, T-OP06의 AC에 "T-AN01~05 모두 must-open 완료"를 의존성으로 명시.
