---
name: KFSuay Register — POS Concurrency Demo
description: A believable restaurant point-of-sale terminal with a clearly-labeled rush-simulation demo feature bolted onto it.
colors:
  bg: "#f2f4f7"
  surface: "#ffffff"
  text-primary: "#1c2430"
  text-muted: "#6b7280"
  border: "#e2e5eb"
  tile-bucket: "#ff8a3d"
  tile-zabb: "#2bb673"
  tile-box: "#6c5ce7"
  tile-suklon: "#ff5d73"
  status-success: "#22c55e"
  status-reject: "#ef4444"
  demo-panel-bg: "#1c2430"
typography:
  display:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.4rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "normal"
  tile-label:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 700
    lineHeight: 1.25
  body:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 500
    lineHeight: 1.4
rounded:
  tile: "18px"
  panel: "14px"
  pill: "999px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
components:
  tile:
    rounded: "{rounded.tile}"
    padding: "20px"
    textColor: "#ffffff"
  primary-action:
    backgroundColor: "{colors.status-success}"
    textColor: "#ffffff"
    rounded: "{rounded.pill}"
    padding: "14px 28px"
---

# Design System: KFSuay Register

## Overview

**Creative North Star: "KFSuay Register"**

Replaces two earlier abstract directions (an ATC radar scope, then a
kitchen expo-ticket wheel) that dramatized the concurrency mechanism but
never read as an actual point-of-sale product — the user showed a photo
of a real touchscreen restaurant register and said, plainly, this is
what a POS looks like. This world commits to that: a bright, modern
register screen with a colorful item-tile grid, a running receipt log,
and a prominent primary action, in the visual language of real POS
software (Square/Toast/Clover-class systems), not demo-tool or
engineering-dashboard chrome.

The concurrency-safety story — the actual point of the backend — still
lives here, but subordinate: a small, visually distinct "demo controls"
panel (dark, set apart from the bright register) holds the rush-fire and
reset actions. A real POS terminal would never ship a "simulate rush"
button; keeping it visually separate is what keeps the register part
honest.

**Key Characteristics:**
- Bright, light register surface (`#f2f4f7` ground, white cards) — a
  POS sits on a counter under normal lighting, not a moody scene.
- Four saturated, named tile colors, one per real menu item, in the
  register-software register (not a restrained single-accent system).
- One green primary-action color reused for "accepted" status
  throughout, one red reused for "sold out / rejected."
- A dark, visually distinct demo-controls panel — the one deliberate
  break from "this is a real product" framing, and it's meant to read
  as one.

## Colors

A bright, saturated register palette; demo controls sit in a
deliberately different dark register.

### Primary
- **Bucket Orange** (#ff8a3d): the `ALL IN ONE BUCKET` tile — the one
  stock-constrained, "hero" item the whole demo turns on.

### Secondary
- **Zabb Green** (#2bb673): `Chick N Share Zabb` tile.
- **Signature Indigo** (#6c5ce7): `The Box Signature` tile.
- **Suk Lon Pink** (#ff5d73): `Suk Lon Jai` tile.
- **Accepted Green** (#22c55e): order-accepted status tag; distinct
  value from Zabb Green even though both read as "green," so status
  meaning never depends on a specific tile's color.
- **Sold-Out Red** (#ef4444): order-rejected / sold-out status tag and
  badge.

### Neutral
- **Register Ground** (#f2f4f7): the page background.
- **Card Surface** (#ffffff): header, tiles' text layer, receipt panel.
- **Ink** (#1c2430): primary text.
- **Muted Ink** (#6b7280): secondary text (timestamps, prices in the
  receipt log).
- **Hairline** (#e2e5eb): card borders and dividers.
- **Demo Panel** (#1c2430): the demo-controls panel background — reuses
  Ink as a fill specifically so it reads as a different surface
  register, not another light card.

### Named Rules
**The Two-Register Rule.** The ordering surface (tiles, receipt, header)
stays in the bright register-software palette at all times. The
demo-controls panel is the only place the dark palette appears — if
dark styling starts leaking into ordering UI, or bright styling leaks
into demo controls, the "real POS vs. bolted-on demo" distinction this
world exists to make has failed.

## Typography

**Display Font:** -apple-system, 'Segoe UI', Roboto, Helvetica, Arial,
sans-serif (system stack only — no network font load; this runs locally
during a screen recording and must not depend on a live connection).
**Body Font:** same system stack.

**Character:** one confident system sans throughout, bold on tiles and
totals (touch-target legibility), regular weight in the receipt log —
no mono/technical register anywhere. This is consumer register
software, not an engineering tool.

### Hierarchy
- **Display** (700, 1.4rem, 1.2): header branding, current total.
- **Tile Label** (700, 1.05rem, 1.25): item name on each tile.
- **Body** (500, 0.9rem, 1.4): receipt log lines, prices, timestamps.

## Layout

Single fixed viewport, not a scrolling page — the register fills the
recording frame. Header bar top (branding + live clock). Below it, a
2×2 item-tile grid on the left/center and a receipt/order-log panel on
the right, mirroring a real POS's order-summary sidebar. The
demo-controls panel is a small, visually distinct dark card tucked in a
corner, not integrated into the main grid. No responsive breakpoints —
single-operator local tool, always viewed at desktop size for
recording.

## Elevation & Depth

Soft, ambient card elevation throughout the register surface — real POS
software uses lifted cards, not flat glass. The demo panel gets the
same soft elevation so it reads as "also a real panel," just a
differently-colored one.

### Shadow Vocabulary
- **card-lift** (`box-shadow: 0 4px 14px rgba(20, 24, 33, 0.08)`):
  applied to the header, tiles, and receipt panel at rest.
- **card-lift-active** (`box-shadow: 0 2px 6px rgba(20, 24, 33, 0.12)`):
  applied on tile press (order placed), a brief compressed shadow.

### Named Rules
**The Lifted-Card Rule.** Every surface (tile, panel, header) casts a
soft ambient shadow. Nothing on the ordering surface is flat-against-the
-page — this is the opposite invariant from the two retired worlds,
which were deliberately flat/glowing instead.

## Shapes

Generously rounded rectangles throughout (18px tile radius, 14px panel
radius) — soft, touch-friendly register hardware, not sharp instrument
panels. The primary action button is fully pill-shaped (999px radius).

## Components

### Item Tile
- **Shape:** rounded rectangle (18px), one of the four named tile
  colors as a solid fill, white text.
- **Content:** item name (bold), price in ฿, and — `ALL IN ONE BUCKET`
  only — a live stock badge (`N left` or `SOLD OUT`).
- **State:** default (solid fill), pressed (card-lift-active + brief
  scale-down), sold out (badge switches to Sold-Out Red, tile dims
  slightly but stays tappable-looking honest — it visibly still tries
  and gets rejected, it doesn't just disable itself, since disabling it
  client-side would hide the real 409 the backend returns).

### Menu Icon
- **Style:** original flat-illustration SVG per item (white on the
  tile's own color, simple geometric shapes — bucket, drumstick +
  chili, takeout box, whole roast chicken), not a stock photo or emoji.
  No real food photography exists for these dishes; this is honest
  original art at the same tile scale a photo would occupy.

### Current Order (Cart)
- **Style:** white card above the receipt panel, one line per distinct
  item with quantity, a small decrement control, and a per-line
  subtotal; a running total and the "CONFIRM ORDER" pill button
  (Accepted Green) beneath it, disabled when the cart is empty.
- **State:** adding a tile increments its cart line (or creates one);
  confirming fires one real order per line concurrently, then empties
  the cart regardless of outcome.

### Receipt / Order Log
- **Style:** white card, hairline border, card-lift shadow, scrollable
  list, most recent line on top.
- **Line:** item name, quantity, price, a status tag (Accepted Green /
  Sold-Out Red), timestamp in muted ink.

### QR Receipt Modal
- **Style:** native `<dialog>`, white card, the generated QR code
  centered above the same receipt text it encodes (items, quantities,
  total, order reference, timestamp) — text is always shown alongside
  the code, never QR-only, so the receipt is legible without a scanner.
  If any cart line was declined, a Sold-Out Red note lists it and
  states it was excluded from the total.
- **State:** only opens when at least one cart line was accepted; a
  fully-declined confirm shows an inline rejection message instead,
  no modal.

### Demo Controls Panel
- **Style:** dark (#1c2430) card, card-lift shadow, small label
  "DEMO CONTROLS" in muted uppercase, tucked in a corner — deliberately
  reads as a different piece of software than the register above it.
- **Buttons:** "SIMULATE RUSH ×30" and "RESET STOCK," white/orange text
  on the dark panel, no register-tile styling.

### Header
- **Style:** white card-lift bar, register name left-aligned, live clock
  right-aligned (real POS terminals always show the time).

## Do's and Don'ts

### Do:
- **Do** keep the ordering surface in the bright register palette at
  all times (The Two-Register Rule).
- **Do** show `ALL IN ONE BUCKET` visibly attempting and failing (409)
  once sold out, rather than disabling the tile — the rejection is the
  point.
- **Do** keep demo controls visually and physically separate from the
  ordering tiles.

### Don't:
- **Don't** let dark demo-panel styling bleed into the register surface,
  or vice versa.
- **Don't** treat the cart as atomic — each confirmed line is its own
  real API call and can independently fail; never show a QR/total that
  includes a declined line.
- **Don't** style the QR code as a payment prompt (no PromptPay-style
  framing, no "pay here" language) — it encodes a receipt, not a
  payment request, and nothing here processes payment.
- **Don't** use a real or stock food photo for menu icons — original
  illustration only, since no licensed photography exists for these
  dishes.
- **Don't** load an external font or image asset — this tool must run
  fully offline during a local screen recording.
