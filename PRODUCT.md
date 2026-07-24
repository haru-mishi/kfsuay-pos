# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: the project's author, running this locally to screen-record a
portfolio demo. Secondary: anyone later watching that recorded clip (not
the live tool itself — it is never deployed or shared as a running
link).

## Product Purpose

A believable restaurant point-of-sale register (menu tile grid, tap to
order, running receipt log) for the single Bangkok branch — not an
abstract visualization. It exists to look and behave like real POS
software first; the concurrency-safety story rides inside it as a
clearly-labeled secondary "simulate rush" action that fires a burst of
concurrent taps at the one contended item and lets the row-lock race
resolve live in the same receipt log a normal single order would use.

**Revision note:** an earlier version of this file described a fully
abstract, non-POS-shaped visualization as the whole product (first an
ATC radar scope, then a kitchen expo-ticket wheel). The user clarified
that read as "some fancy [art piece]," not a POS, and supplied a
reference photo of a real touchscreen restaurant register (tablet
screen, colorful item-tile grid, card reader) as binding visual
authority. This revision supersedes that positioning; the abstract
directions and their DESIGN.md are retired.

## Positioning

Every other project on the portfolio shows a finished UI already — this
one should too, immediately recognizable as a restaurant register, not
a demo-tool aesthetic. What makes it different from a normal POS mockup
is that tapping items and firing the rush both hit the same real
FastAPI + Postgres backend with a real row lock behind it.

## Operating Context

Run locally via the existing `docker compose up` (Postgres + FastAPI
app, already working). Opened in a browser on the same machine, used
once or a few times back-to-back while screen-recording. Never deployed
publicly — consistent with DESIGN.md's existing decision that this API
has no auth and isn't meant to be exposed. Single branch only (Bangkok)
— a real POS terminal belongs to one physical location, so no
branch-switcher is needed or realistic.

## Capabilities and Constraints

- Talks to the real, already-built endpoints: `POST
  /branches/{branch_id}/orders` (single item + quantity per call — the
  endpoint already accepts a quantity, so one real call per distinct
  cart line covers checkout without needing a new multi-item backend
  endpoint), `GET /branches/{branch_id}/items/{item_id}/stock`, `POST
  /admin/reset`.
- Menu tiles show the real seeded menu (`ALL IN ONE BUCKET` ฿199,
  `Chick N Share Zabb` ฿89, `The Box Signature` ฿159, `Suk Lon Jai`
  ฿619) at the real prices from `init.sql`, each with a flat-illustration
  icon (no real food photography exists for these dishes, and none
  should be fabricated/hotlinked — see Evidence on Hand).
- Ordering flow: tapping a tile adds/increments it in a client-side
  cart (not yet submitted); "CONFIRM ORDER" submits one real API call
  per distinct cart line (with its quantity) concurrently. This is a
  UI convenience over the same single-item endpoint, not a fake atomic
  multi-item order — every line is a real, independent transaction, and
  a line can fail (e.g. insufficient stock) independently of the
  others.
- On confirm: lines that succeed generate a real receipt (items,
  quantities, total, timestamp, a short order reference) rendered as
  both text and a scannable QR code encoding that same receipt text —
  not a payment QR; scanning it just surfaces the real order data, no
  payment is implied or processed. Lines that fail are shown as
  declined in the receipt log and excluded from the total/QR; if every
  line fails, no QR is shown at all.
- Only `ALL IN ONE BUCKET` at Bangkok is stock-constrained (seeded at
  10); the other three items are seeded at 100 and effectively never
  run out, so only that one tile carries a live stock badge.
- The rush-simulation and reset controls must be visually set apart
  from the ordering surface and hidden from the default view — a real
  register would never ship a "simulate rush" button. Reachable via a
  small discreet icon (not styled like a normal POS action) that opens
  the same dark, deliberately non-register-styled panel. Rush fires
  directly against the bucket item, bypassing the cart (it's a stress
  test, not a customer order).
- No auth, no multi-item atomic backend order, no branch switching.
  Single-machine, single-operator use.

## Brand Commitments

Binding visual reference #1: the user-supplied photo of a real
touchscreen restaurant POS terminal — governs the *form factor*
(register-software composition: header, item-tile grid, cart, receipt
panel), not the color story.

Binding visual reference #2 (supersedes the multi-color tile palette):
"KFSuay" is a pun — KFC + Thai "suay" (ซวย, unlucky) — and the register
should feel like KFC: red/white, bucket-meal iconography, bold
confident branding. Not a literal trademark copy (no reproduction of
KFC's actual logo, wordmark, or the Colonel's likeness) — the palette,
type weight, and bucket/stripe motifs evoke the category without
copying protected assets. The earlier full-palette tile strategy
(orange/green/purple/pink) is retired in favor of a red-led, near-white
register.

Demo controls (rush/reset) are hidden behind a small discreet icon
rather than shown as a standing panel — the user confirmed they still
want it reachable (it's the actual concurrency-safety proof, the real
point of this project) but not visually part of the register.

## Evidence on Hand

`DESIGN.md` and `demo_concurrency.py` already document and prove the
underlying mechanism (30 concurrent single-unit requests against 10
seeded units → exactly 10 succeed, 20 rejected, final stock 0). The
rush-simulation feature is a real front-end for the same real behavior,
not a simulation — no fabricated data or fake results. Menu names and
prices are the real seeded values, not placeholders. No real food
photography exists for these dishes; menu icons are original flat
illustrations built for this project, not sourced/hotlinked stock
photos — the user confirmed this explicitly rather than have real-looking
but uncredited/unlicensed photos stand in for the menu.

## Product Principles

1. **Register first, demo feature second.** The screen must read as a
   real POS terminal on its own; the rush/reset controls are visually
   subordinate and clearly labeled as a demo aid.
2. **Real calls only.** Every order shown — single tap or rush burst —
   must hit the actual FastAPI endpoint against the actual Postgres row
   lock. No mocked/simulated results.
3. **Repeatable without infra restarts.** Reset must actually reseed DB
   state via a real call, not a page reload.
4. **Built for capture, not production.** Optimize for how it reads in
   a screen recording over responsive/cross-browser completeness —
   single operator, single session, never deployed.
