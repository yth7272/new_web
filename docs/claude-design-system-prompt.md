# Claude Design Prompt: CuraPulse Design System v0.1

Use the uploaded project context files and the live reference site below to create a desktop-only CuraPulse ecommerce prototype design system.

Reference site:
https://themedicube.co.kr/

Important: use the reference site only for commerce structure and rhythm. Do not copy Medicube brand assets, images, exact layout, or exact visual identity.

## Goal

Create one polished desktop design system page for a meeting prototype. This is not production Cafe24 code. It is a visual decision tool for CuraPulse D2C renewal.

## Design Direction

Borrow these patterns from Medicube:

- black promo strip at the top
- clean white navigation bar
- strong black Korean typography
- large visual commerce hero cards
- compact category shortcuts
- product cards where image, badge, price, membership price, and cart CTA are clear
- visible device/service flows such as device usage, comparison, and authentic product registration

Translate them into CuraPulse:

- brand tone: clinical, commercial, premium but not cold
- colors: white, black, Pulse Coral, light clinical mint, small blue signal accents
- structure: DEVICE / BOOSTER / INNER / CALM / SCIENCE / COMMUNITY / BRAND / SUPPORT
- product logic: DEVICE + BOOSTER + PULSE PICK + SCIENCE evidence
- avoid a discount-only mall feeling; make SCIENCE and routine logic central

## Required Components

Create a single HTML design system sheet containing:

1. Top promo bar
2. Global navigation
3. Hero section for DEVICE + BOOSTER
4. Category rail with the 8 GNB items
5. Product card variants
6. Badge system
7. CTA buttons
8. SCIENCE module with six parts: headline, mechanism, ingredient card, clinical chart, certification badge, CTA
9. ROUTINE LAB card
10. Device authentic registration form
11. Color tokens and typography scale

## Constraints

- Desktop only. Do not optimize for mobile in this version.
- No real payment, login, search, membership, or AI behavior.
- No copied Medicube photos or logos.
- Use realistic placeholders that feel ecommerce-ready.
- Keep cards at 8px radius or less unless the element is a pill CTA.
- Make the first viewport feel like a real ecommerce site, not a planning document.

## Output

Return a single self-contained HTML/CSS design system page. Use semantic class names that can later map to `assets/tokens.css`.
