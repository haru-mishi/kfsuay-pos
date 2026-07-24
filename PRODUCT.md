# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: the project's author, running this locally to screen-record the
concurrency-safety demo for a portfolio project card. Secondary: anyone
later watching that recorded clip (not the live tool itself — it is never
deployed or shared as a running link).

## Product Purpose

A visual, repeatable restatement of what `demo_concurrency.py` already
proves via terminal output: that the order endpoint's `SELECT ... FOR
UPDATE` row lock prevents overselling under concurrent requests. Exists so
the mechanism can be *watched* (requests racing, a live succeeded/rejected
tally, stock landing at exactly 0) instead of read as a script's final
assertion — better raw material for a portfolio demo video than a
terminal pass/fail line.

## Positioning

Every other project on the portfolio shows a finished UI. This one shows
the failure mode being prevented, live: fire a burst of concurrent orders
against limited stock and watch the lock resolve the race in real time,
ending exactly at zero, never negative.

## Operating Context

Run locally via the existing `docker compose up` (Postgres + FastAPI app,
already working). Opened in a browser on the same machine, used once or a
few times back-to-back while screen-recording. Never deployed publicly —
consistent with DESIGN.md's existing decision that this API has no auth
and isn't meant to be exposed.

## Capabilities and Constraints

- Talks to the real, already-built endpoint: `POST
  /branches/{branch_id}/orders` (branch_id, item_id, quantity). No new
  backend endpoints planned beyond one addition: a reset/reseed action
  (see below), since the demo drains seeded stock to 0 on each run.
- Must fire many concurrent requests from the browser and visualize, live:
  requests in flight, running succeeded (200) vs rejected (409) counts,
  and final stock.
- Reset action re-seeds the target branch/item's stock so the demo can be
  re-run without restarting containers.
- No auth, no cart, no multi-item orders — same locked scope as the
  backend slice itself (see DESIGN.md).
- Single-machine, single-operator use. No multi-user/session concerns.

## Brand Commitments

User wants red/orange in the palette. Not otherwise tied to the portfolio
site's existing navy/accent-blue system — this is a standalone tool, not
a portfolio page.

## Evidence on Hand

`DESIGN.md` and `demo_concurrency.py` already document and prove the
underlying mechanism (30 concurrent single-unit requests against 10
seeded units → exactly 10 succeed, 20 rejected, final stock 0). This
frontend is a visual front-end for the same real behavior, not a
simulation — no fabricated data or fake results.

## Product Principles

1. **Mechanism visible, not decorative.** The visualization must show
   *which* requests won and lost in real time, not just a spinner
   followed by a final count.
2. **Real calls only.** Every request shown must hit the actual FastAPI
   endpoint against the actual Postgres row lock — no mocked/simulated
   race.
3. **Repeatable without infra restarts.** Reset must actually reseed DB
   state via a real call, not a page reload.
4. **Built for capture, not production.** Optimize for how it reads in a
   screen recording (pacing, legibility of the tally) over
   responsive/cross-browser completeness — single operator, single
   session, never deployed.
