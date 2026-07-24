---
name: The 86 Board — KFSuay POS Concurrency Demo
description: A diner expo ticket wheel that turns a Postgres row-lock race into a watchable kitchen rush.
colors:
  board-bg: "#170f0a"
  rail-metal: "#4a3c2e"
  ticket-paper: "#f2e6c9"
  ticket-ink: "#2b2117"
  stamp-fired: "#ff8c1a"
  stamp-86: "#ff3b30"
  board-panel: "#12241a"
  chalk: "#f4efe3"
typography:
  readout:
    fontFamily: "ui-monospace, 'JetBrains Mono', 'SF Mono', Consolas, monospace"
    fontSize: "clamp(1.1rem, 2.4vw, 1.6rem)"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "0.04em"
  label:
    fontFamily: "ui-monospace, 'JetBrains Mono', 'SF Mono', Consolas, monospace"
    fontSize: "0.7rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.18em"
rounded:
  ticket: "2px"
  panel: "4px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
components:
  toggle-fire:
    backgroundColor: "{colors.board-panel}"
    textColor: "{colors.stamp-fired}"
    rounded: "{rounded.ticket}"
    padding: "12px 20px"
  toggle-reset:
    backgroundColor: "{colors.board-panel}"
    textColor: "{colors.chalk}"
    rounded: "{rounded.ticket}"
    padding: "12px 20px"
---

# Design System: The 86 Board

## Overview

**Creative North Star: "The 86 Board"**

Replaces an earlier radar-scope direction that dramatized the concurrency
race well but read as generic engineering tooling — nothing on screen
said "restaurant." This world is a diner expo ticket wheel: the real
piece of kitchen hardware cooks clip paper order tickets to, rotating
them past the pass window. Each concurrent order request is a ticket
clipped to the wheel; it resolves live as either stamped **FIRED**
(orange ink, order accepted) or **86'D** (red ink, kitchen's out — a
real, universally-understood restaurant term for "sold out," not an
invented label).

The old world's restraint carries over unchanged: two accent inks only
(orange for fired, red for 86'd), everything else warm neutral kitchen
material (dark backdrop, kraft ticket paper, chalkboard panel). The
readout uses the same two-word kitchen vocabulary as the tickets
themselves (FIRED / 86'D / STOCK), not engineering counters.

**Key Characteristics:**
- Circular expo wheel, rim clipped with ticket stubs, dark warm kitchen
  backdrop instead of a cold CRT ground.
- Two-ink stamp system: orange FIRED, red 86'D — nothing else colored.
- Chalkboard-style readout panel (dark green-black, chalk-white digits)
  instead of an LED data block.
- Ticket-rail hardware switches (FIRE / RESET), same panel-mounted
  register as before, restyled in kitchen materials.

## Colors

Warm, dim kitchen-at-night backdrop; two hot inks do all the signaling.

### Primary
- **Fired Orange** (#ff8c1a): the FIRED stamp ink, and the RESET switch
  isn't this color — reserved entirely for "order accepted."

### Secondary
- **86'd Red** (#ff3b30): the 86'D stamp ink, the STOCK readout once it
  hits zero, and the FIRE switch's tip — firing the burst is what risks
  triggering it.

### Neutral
- **Board Backdrop** (#170f0a): the kitchen-at-night ground the wheel
  sits against.
- **Rail Metal** (#4a3c2e): the wheel's rim and spokes — warm dark
  steel, not chrome.
- **Ticket Paper** (#f2e6c9): unresolved ticket stubs, kraft/cream
  paper color, before either stamp lands.
- **Ticket Ink** (#2b2117): printed ticket text (dot-matrix register).
- **Board Panel** (#12241a): the chalkboard readout and switch-panel
  background — dark green-black, distinct from the warmer backdrop.
- **Chalk** (#f4efe3): readout digits and static labels on the board
  panel.

### Named Rules
**The Two-Ink Rule.** Nothing on this surface is any color but fired
orange, 86'd red, or the warm neutral kitchen materials (backdrop,
metal, paper, chalkboard). A third accent hue anywhere breaks the
kitchen-hardware illusion — carried over unchanged from the previous
world.

## Typography

**Display/Readout Font:** ui-monospace, 'JetBrains Mono', 'SF Mono',
Consolas, monospace (system stack only — no network font load; this
runs locally during a screen recording and must not depend on a live
connection).
**Label Font:** the same mono stack, uppercase, wide-tracked — doubles
as both "dot-matrix ticket printer" register and chalkboard-stencil
register, so no second face is needed.

**Character:** one monospace family carries two readings at once: small
tracked caps read as ticket-printer text on the wheel, larger tracked
digits read as chalk numerals on the board panel.

### Hierarchy
- **Readout** (600, clamp(1.1rem, 2.4vw, 1.6rem), 1.1): the live FIRED /
  86'D / STOCK counters on the chalkboard panel.
- **Label** (600, 0.7rem, 1.2, 0.18em tracking, uppercase): static
  captions under each readout value.

### Named Rules
**The No-Prose Rule.** No sentence-case text appears anywhere — labels
are short, uppercase, tracked, like a printed ticket or chalk stencil.
Carried over from the previous world.

## Layout

Single fixed viewport, not a scrolling page — the wheel fills the
recording frame. A centered circular wheel dominates; the chalkboard
readout panel docks bottom-right, the FIRE/RESET switch panel docks
bottom-left. No responsive breakpoints — single-operator local tool,
always viewed at desktop size for recording.

## Elevation & Depth

Mostly flat, kitchen-hardware flat — no soft UI drop shadows. Ticket
stubs get a small hard-edged offset shadow (paper sitting slightly proud
of the wheel, like a real clipped ticket), not a blurred glow; the wheel
rim and chalkboard panel are flat matte materials.

### Shadow Vocabulary
- **ticket-lift** (`box-shadow: 2px 2px 0 rgba(0,0,0,0.4)`): a small hard
  offset under every ticket stub, paper sitting proud of the wheel.
- **stamp-glow** (`text-shadow: 0 0 6px currentColor`): a faint ink glow
  on a stamp the instant it lands (fired or 86'd), settling to flat once
  resolved.

### Named Rules
**The Hard-Shadow Rule.** Where the previous world used soft CRT bloom,
this world uses one small hard offset shadow for paper sitting on metal
— never a blurred ambient glow except the brief stamp-landing flash.

## Shapes

The wheel is a true circle (rim + spokes). Ticket stubs are small
rounded rectangles (2px radius) with a jagged torn top edge
(`clip-path` notches) — paper torn from a ticket printer, not a UI chip.
The chalkboard panel and switches are rectangular with a minimal radius,
read as mounted hardware.

## Components

### Toggle Switches (FIRE / RESET)
- **Shape:** rectangular, 2px radius, thin rail-metal bezel border.
- **FIRE:** 86'd-red tipped indicator, board-panel background; snaps
  down with a short mechanical throw on press, disabled mid-burst.
- **RESET:** chalk-white tipped indicator, same panel background; calls
  the reseed endpoint and replays the wheel "back in service."
- **Hover/Focus:** tip glow brightens slightly; no border color shift —
  panel hardware doesn't repaint itself.

### Chalkboard Readout
- **Style:** chalk-white digits on the board-panel background,
  tabular-nums so digits don't jitter width as they tick.
- **State:** three live values (FIRED, 86'D, STOCK) update as each
  ticket resolves; STOCK hitting 0 turns the STOCK value 86'd-red and
  the wheel's hub shows "86'D — SOLD OUT."

### Ticket Stub
- **Style:** small rounded rectangle, kraft-paper fill, jagged torn top
  edge, ticket-lift hard shadow.
- **State:** unresolved (pulsing kraft paper, unstamped, in flight),
  fired (stamped orange, clips onto the wheel rim and settles), 86'd
  (stamped red, slides off the wheel edge and stays dimly visible — a
  fired ticket disappearing from view would hide the very outcome this
  demo exists to show).

## Do's and Don'ts

### Do:
- **Do** keep every color decision inside fired-orange, 86'd-red, or the
  warm neutral kitchen materials (The Two-Ink Rule).
- **Do** use real kitchen vocabulary (FIRED, 86'D) on every label —
  never rename these to engineering terms (cleared/rejected/etc.).
- **Do** keep 86'd tickets visible after resolving, never fading to
  fully transparent.

### Don't:
- **Don't** add a third accent hue, even a muted one, anywhere on this
  surface.
- **Don't** soften the switches into rounded pill buttons — they are
  panel hardware, not web-app controls.
- **Don't** load an external font or image asset — this tool must run
  fully offline during a local screen recording.
