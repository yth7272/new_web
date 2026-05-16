# CuraPulse D2C Prototype

Desktop-only Streamlit prototype for CuraPulse 자사몰 개편 회의.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Structure

- `streamlit_app.py`: design system landing page
- `pages/`: Streamlit multipage routes for the v0.1 meeting scope
- `templates/`: embedded HTML templates
- `assets/tokens.css`: shared design tokens and components
- `assets/mock-data.json`: mock product/member/routine data
- `docs/prototype-definition-v0.1.md`: one-page prototype definition

## Prototype pages

- `/`: Design System
- `/Main_Page`: Main page flow
- `/BOOSTER`: BOOSTER category
- `/Product_Detail`: Product detail with SCIENCE module
- `/PULSE_PICK`: Device x booster recommendation
- `/Device_Auth`: Authentic product registration
- `/ROUTINE_LAB`: Community MVP
- `/SCIENCE`: Clinical library
- `/PHILOSOPHY`: Brand philosophy

## Streamlit Cloud

Deploy from `yth7272/new_web`, branch `main`, main file path `streamlit_app.py`.

## Scope note

This prototype is not production Cafe24 code. It is a visual decision tool for structure, flow, copy, and design direction.
