# CuraPulse Prototype Definition v0.1

## Purpose

This prototype is a visual decision tool for the first CuraPulse D2C renewal meeting. It exists to test information architecture, page flow, product presentation, SCIENCE notation, and key module placement before the real Cafe24 implementation begins.

## Non-purpose

This is not production Cafe24 code. The Streamlit app, embedded HTML, CSS, and mock data are not expected to migrate into the final store. What should survive are design tokens, page structure, copy direction, product taxonomy, and clinical data presentation rules.

## Scope

The v0.1 meeting build is desktop only. It includes the design system and eight prototype pages: Main Page, BOOSTER, Product Detail, PULSE PICK, Device Auth, ROUTINE LAB, SCIENCE, and PHILOSOPHY.

Real payment, real login, real search, automatic membership upgrades, AI routine coaching, live commerce, store locator, and recruiting are excluded from v0.1.

## Technology

The prototype uses Streamlit for hosting, routing, and simple mock state. Page designs are embedded as standalone HTML through `st.components.v1.html()`. Shared visual decisions live in `assets/tokens.css`.

## Meeting Exit Criteria

Each included page should receive one of three decisions: GO, MODIFY, or HIDE. The decision result should be reflected back into the IA Master Board after the meeting.
