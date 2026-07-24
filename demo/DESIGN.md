---
name: KFSuay Register — POS Concurrency Demo
description: A red-and-white, KFC-coded restaurant register with a discreetly-hidden concurrency demo behind it.
colors:
  bg: "#faf5ec"
  surface: "#ffffff"
  ink: "#1a1a1a"
  muted: "#6b6b6b"
  border: "#ecdfc9"
  brand-red: "#d81f26"
  brand-red-deep: "#a5161b"
  status-success: "#1f9d55"
  status-declined: "#1a1a1a"
  demo-panel-bg: "#1c2430"
typography:
  display:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  tile-label:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 800
    lineHeight: 1.2
  body:
    fontFamily: "-apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 500
    lineHeight: 1.4
rounded:
  tile: "14px"
  panel: "14px"
  pill: "999px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "24px"
components:
  tile:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.tile}"
    padding: "20px"
    textColor: "{colors.ink}"
  primary-action:
    backgroundColor: "{colors.brand-red}"
    textColor: "#ffffff"
    rounded: "{rounded.pill}"
    padding: "14px 28px"
---

# Design System: KFSuay Register

## Overview

**Creative North Star: "KFSuay Register"**

Third pass on this world. First two builds (an ATC radar scope, a
kitchen expo-ticket wheel) proved the mechanism but didn't read as a
POS; the next build fixed that with a generic bright register-software
look (Square/Toast/Clover-class, full rainbow tile palette). The user
then explained the actual brand: **KFSuay** is a pun — KFC + Thai
"suay" (ซวย, unlucky) — and asked for the register to genuinely feel
like KFC. This pass replaces the rainbow-tile palette with a red/white,
bucket-and-bold-type identity that evokes the category by color,
weight, and motif — never by reproducing KFC's actual logo, wordmark,
or the Colonel's likeness, which stay strictly out of scope as real
trademarked assets.

The concurrency-safety story — the actual engineering point of the
whole project — moves fully offstage in this pass: no standing panel at
all. A small discreet icon in the corner opens the same dark,
deliberately non-register-styled demo panel from the previous world.
Hiding it (rather than removing it) was a deliberate call after the
user confirmed they still want it reachable — it's the real proof this
portfolio piece exists to make.

**Key Characteristics:**
- Near-white, warm register ground (`#faf5ec`) with white cards — no
  more per-item rainbow tiles; one brand red carries the identity.
- Heavy-weight (900) display type on branding and totals — bold,
  confident, fast-food-poster energy instead of the previous world's
  restrained 700 weight.
- Status colors decoupled from brand red on purpose: green stays
  "accepted," but "declined/sold out" moves to near-black (a stamped,
  crossed-out register-tape feel) so it never competes visually with
  brand-red CTAs.
- Demo controls are fully hidden by default — a first for this project;
  every earlier world kept them standing and merely visually distinct.

## Colors

A red-and-white QSR-register palette; demo controls stay in their own
separate dark register, now hidden behind an icon rather than always
visible.

### Primary
- **KFSuay Red** (#d81f26): header band, primary action (CONFIRM
  ORDER), tile accent stripes, price badges — the one color that
  carries the brand.

### Secondary
- **Deep Red** (#a5161b): pressed/active states on red elements, the
  bucket-tile's featured stripe pattern's darker band.
- **Accepted Green** (#1f9d55): order-accepted status tag — kept from
  the previous world since "green means success" doesn't need
  reinventing.
- **Declined Ink** (#1a1a1a): order-declined/sold-out status tag and
  badge — moved off red specifically so a "SOLD OUT" stamp never reads
  as another red brand element.

### Neutral
- **Register Ground** (#faf5ec): page background — warm near-white,
  not the previous world's cool gray, closer to a paper bucket-liner
  tone.
- **Card Surface** (#ffffff): tiles, cart, receipt panel, header.
- **Ink** (#1a1a1a): primary text.
- **Muted Ink** (#6b6b6b): secondary text (timestamps, prices in the
  receipt log).
- **Hairline** (#ecdfc9): card borders and dividers, warm-toned to
  match the register ground rather than a cool gray.
- **Demo Panel** (#1c2430): unchanged from the previous world — still
  the one deliberately different, non-register surface.

### Named Rules
**The One-Red Rule.** Exactly one saturated color carries this brand.
No second or third accent hue anywhere on the register surface — where
the previous world used four named tile colors, this world spends its
entire color budget on red, white, and near-black.
**The Decoupled-Status Rule.** "Declined" is never rendered in brand
red — it's near-black. This keeps the one loud brand color reserved for
identity and action, never accidentally reading as an error state.

## Typography

**Display Font:** -apple-system, 'Segoe UI', Roboto, Helvetica, Arial,
sans-serif (system stack only — no network font load; this runs locally
during a screen recording and must not depend on a live connection).
**Body Font:** same system stack.

**Character:** heavy (900) weight on branding, tile names, and totals —
posterish, confident, fast-food-menu-board energy — regular weight in
the receipt log and fine print. The jump from body to display weight is
the register's whole typographic personality; there is no second
typeface or mono register anywhere.

### Hierarchy
- **Display** (900, 1.5rem, 1.1, -0.01em): header wordmark, order
  totals, the receipt modal's "Order Confirmed" headline.
- **Tile Label** (800, 1.05rem, 1.2): item name on each tile.
- **Body** (500, 0.9rem, 1.4): receipt log lines, prices, timestamps,
  cart lines.

## Layout

Unchanged composition from the previous world: single fixed viewport,
header top, 2×2 item-tile grid left/center, cart + receipt panel right.
What's gone is the standing demo-controls panel — replaced by a small
icon-only toggle, bottom corner, that opens the same panel as an
overlay rather than a permanent fixture. No responsive breakpoints —
single-operator local tool, always viewed at desktop size for
recording.

## Elevation & Depth

Unchanged from the previous world: soft ambient card elevation on every
surface (header, tiles, cart, receipt). Flat-against-the-page is still
never the answer here.

### Shadow Vocabulary
- **card-lift** (`box-shadow: 0 4px 14px rgba(26, 26, 26, 0.08)`):
  applied to the header, tiles, cart, and receipt panel at rest.
- **card-lift-active** (`box-shadow: 0 2px 6px rgba(26, 26, 26, 0.12)`):
  applied on tile press.

## Shapes

Rounded rectangles throughout (14px tile/panel radius — slightly
tighter than the previous world's 18px, closer to real packaging/menu-
board corner rounding). The primary action button stays fully
pill-shaped.

## Components

### Item Tile
- **Shape:** white card (14px radius), a brand-red top accent stripe,
  a red price badge.
- **Content:** icon (red/black duotone, was white-on-color before),
  item name (heavy black), price badge in red, and — `ALL IN ONE
  BUCKET` only — a live stock badge (`N left` in red, or `SOLD OUT` in
  declined-ink).
- **State:** default (white card + red stripe), pressed
  (card-lift-active + brief scale-down), sold out (badge switches to
  Declined Ink, tile visibly still tappable and still tries/fails —
  never client-side disabled, since that would hide the real 409).
- **Featured treatment:** `ALL IN ONE BUCKET` — the flagship, the one
  stock-constrained item — gets a subtle diagonal red/white stripe
  texture behind its icon, the one deliberate nod to bucket-meal
  packaging.

### Menu Icon
- **Style:** the same original flat-illustration SVGs as before, fills
  changed from white to brand red (with black accent details where the
  original used opacity), since tiles are now white cards instead of
  solid color fills.

### Current Order (Cart) / Receipt / QR Modal
- **Unchanged in structure and behavior** from the previous world (see
  git history for the full prior spec) — cart lines, CONFIRM ORDER,
  the QR receipt modal, and the order log all keep their exact
  mechanics. Only their color/type tokens shift to this world's red/
  white/black palette; CONFIRM ORDER moves from Accepted Green to
  KFSuay Red (still distinguishable from status green/declined-ink).

### Demo Controls (now hidden)
- **Trigger:** a small circular icon button (⚙ or similar), muted gray,
  bottom-right corner — deliberately unbranded, not red, not part of
  the register's visual language, so it reads as a settings affordance
  rather than a feature.
- **Panel:** unchanged dark (#1c2430) card, opens as an overlay/popover
  from the icon rather than standing permanently. Same "SIMULATE RUSH
  ×30" / "RESET STOCK" buttons.

### Header
- **Style:** solid KFSuay Red band (not white/card-lift like the rest),
  white heavy-weight wordmark, live clock in white at reduced opacity.

## Do's and Don'ts

### Do:
- **Do** keep the entire ordering surface to red, white, and near-black
  (The One-Red Rule).
- **Do** keep "declined" status in near-black, never red (The
  Decoupled-Status Rule).
- **Do** show `ALL IN ONE BUCKET` visibly attempting and failing (409)
  once sold out, rather than disabling the tile.
- **Do** keep the demo-controls icon visually unbranded/neutral so it
  never looks like a register feature.

### Don't:
- **Don't** reproduce KFC's actual logo, wordmark, or the Colonel's
  likeness — evoke the category through color/weight/motif only.
- **Don't** show the demo-controls panel by default — it must be one
  deliberate click away, never standing.
- **Don't** treat the cart as atomic — each confirmed line is its own
  real API call and can independently fail; never show a QR/total that
  includes a declined line.
- **Don't** style the QR code as a payment prompt — it encodes a
  receipt, not a payment request.
- **Don't** use a real or stock food photo for menu icons — original
  illustration only.
- **Don't** load an external font or image asset — this tool must run
  fully offline during a local screen recording.
