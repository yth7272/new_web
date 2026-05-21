# 03. ClickUp 임포트 설계

> 출처: `02-tasks-phase1.md`
> 임포트 파일: `clickup-import-tasks.csv`
> 기준 task 수: 87개
> 작성일: 2026-05-19

---

## 1. 권장 ClickUp 구조

ClickUp에는 **폴더 1개 + 섹션별 리스트**로 넣는 방식을 권장합니다. `MVP 컷`은 리스트를 나누는 기준이 아니라 커스텀 필드로 둡니다. 이렇게 해야 DEVICE, BOOSTER, SUPPORT처럼 실제 담당 흐름은 유지하면서도 `must-open`만 필터링해 오픈 전 범위를 볼 수 있습니다.

| 레벨 | 이름 | 설명 |
|---|---|---|
| Space | 기존 운영 Space 또는 신규 Space | 이미 자사몰/개발 운영 Space가 있으면 그 안에 둠 |
| Folder | CuraPulse v4 자사몰 개편 | 이번 개편 task 전체 묶음 |
| List | 0. 의사결정 회의 | D1~D11 선행 결정 |
| List | 1. 공통 / 메인 / GNB | GNB, 메인, 인벤토리, SKU 마스터 |
| List | 2. DEVICE | DEVICE 허브, PDP, 정품등록 |
| List | 3. BOOSTER | 부스터 라인, PULSE PICK, 루틴팩 |
| List | 4. 다중 진입로 | 고민별/유형별/선물하기 |
| List | 5. SCIENCE | SCIENCE 허브, PDP 표준 모듈, 근거 라이브러리 |
| List | 6. COMMUNITY | ROUTINE LAB, 리뷰 통합 |
| List | 7. BRAND | PHILOSOPHY, 회사/뉴스/매거진 |
| List | 8. SUPPORT | FAQ, 문의, 배송/반품, A/S |
| List | 8.5 회원 / 로그인 / 마이페이지 | 회원, 정품등록 hook, 마이페이지 |
| List | 8.7 분석 / 추적 | GA4, 이벤트 태깅, Looker 대시보드 |
| List | 9. 운영 / 검수 / 배포 전 | 법무 검수, UX 점검, 배포 판정 |

---

## 2. 상태값

| 상태 | 의미 |
|---|---|
| `to do` | 아직 시작하지 않음 |
| `in progress` | 작업 중 |
| `blocked` | 결정/자료/의존성 때문에 막힘 |
| `review` | 산출물 작성 후 검토 중 |
| `done` | 수용기준(AC) 충족 |

---

## 3. 커스텀 필드

| 필드명 | 타입 | 값 |
|---|---|---|
| `Task ID` | Text | T-D01, T-C01 등 |
| `MVP Cut` | Dropdown | `must-open`, `post-open`, `phase-2` |
| `Critical Path` | Checkbox 또는 Dropdown | `yes`, `no` |
| `Owner Group` | Text 또는 People | PM, 개발, 디자인, 콘텐츠 등 |
| `Dependencies` | Text | 선행 task ID |
| `Deliverable` | Long text | 산출물 |
| `Acceptance Criteria` | Long text | 수용기준(AC) |
| `Tags` | Label | P0/P1/P2, MVP 컷, 섹션명 |

담당자를 실제 ClickUp 사용자로 배정하기 전까지는 `Owner Group`을 부서명 텍스트로 둡니다. 실제 담당자가 확정되면 People 필드 또는 assignee로 옮깁니다.

---

## 4. CSV 필드 매핑

`clickup-import-tasks.csv`는 아래 컬럼으로 생성되어 있습니다.

| CSV 컬럼 | ClickUp 매핑 |
|---|---|
| `Task Name` | Task name |
| `Description` | Description |
| `List` | List 또는 커스텀 필드 |
| `Status` | Status |
| `Priority` | Priority 또는 custom dropdown |
| `MVP Cut` | Custom field |
| `Critical Path` | Custom field |
| `Owner Group` | Custom field |
| `Dependencies` | Custom field |
| `Deliverable` | Custom field |
| `Acceptance Criteria` | Custom field |
| `Tags` | Tags |
| `Task ID` | Custom field |

ClickUp CSV 임포트가 여러 리스트 자동 생성을 지원하지 않는 경우, 먼저 하나의 리스트에 전체 CSV를 넣고 `List` 컬럼으로 필터링한 뒤 섹션별 리스트로 이동합니다.

---

## 5. 의존성 처리

CSV에는 의존성을 텍스트로 넣었습니다. ClickUp의 dependency 기능은 임포트 후 다음 순서로 수동 또는 자동화 처리합니다.

1. `Critical Path = yes` task 7개를 먼저 확인합니다.
2. `Dependencies` 필드에서 `T-` ID를 읽어 선행 task를 연결합니다.
3. `T-D02`, `T-D03`, `T-D04`, `T-AC01`, `T-BO01`, `T-SC01`, `T-DV10`은 별도 Gantt/Timeline에서 추적합니다.
4. `T-AN01~03`은 P0은 아니지만 `T-OP06` 배포 판정의 선행 조건으로 별도 필터를 만듭니다.

---

## 6. 권장 뷰

| View | 필터/그룹 기준 | 용도 |
|---|---|---|
| `Must Open Board` | `MVP Cut = must-open` | 1차 오픈 전 필수 범위 |
| `Critical Path` | `Critical Path = yes` | PM 매일 점검 |
| `Post Open Backlog` | `MVP Cut = post-open` | 오픈 후 1~4주 보강 |
| `Phase 2 Backlog` | `MVP Cut = phase-2` | 2차 이관 |
| `By Owner Group` | `Owner Group` 그룹핑 | 부서별 배정 |
| `By Section` | `List` 또는 섹션 그룹핑 | 문서 구조와 동일하게 보기 |

---

## 7. 임포트 전 확인

- `clickup-import-tasks.csv`가 87행인지 확인합니다.
- `P0` task가 7개인지 확인합니다.
- `must-open` task가 62개인지 확인합니다.
- `post-open` task가 23개인지 확인합니다.
- `phase-2` task가 2개인지 확인합니다.
- 담당자 실명 배정 전에는 `Owner Group`만 사용합니다.
- 의존성은 CSV 임포트 후 ClickUp 안에서 연결합니다.

---

## 8. 현재 기준 요약

| 구분 | 수 |
|---|---:|
| 전체 task | 87 |
| P0 | 7 |
| P1 | 74 |
| P2 | 6 |
| must-open | 62 |
| post-open | 23 |
| phase-2 | 2 |

임포트 후 가장 먼저 확인할 것은 `Critical Path` 뷰입니다. 이 7개 task가 늦으면 나머지 task를 병렬로 배정해도 전체 오픈 일정이 밀립니다.
