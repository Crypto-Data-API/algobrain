---
title: "Volume Nodes (HVN, LVN, Single Prints)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [market-microstructure, technical-analysis, indicators, volume, support-and-resistance, breakout]
aliases: ["HVN", "LVN", "High Volume Node", "Low Volume Node", "Volume Nodes", "Single Prints", "Volume Gap", "Naked POC zone"]
related: ["[[volume-profile]]", "[[point-of-control]]", "[[value-area]]", "[[value-area-high-and-low]]", "[[support-and-resistance]]", "[[market-profile]]", "[[liquidity-pools]]", "[[volume-profile-trading-strategy]]"]
domain: [market-microstructure, technical-analysis]
prerequisites: ["[[volume-profile]]"]
difficulty: intermediate
---

**Volume nodes** are the peaks and valleys of the [[volume-profile]] histogram. A **High-Volume Node (HVN)** is a price (or zone) where the profile bulges outward — a lot of volume traded there. A **Low-Volume Node (LVN)** is a narrow "valley" where the profile pinches in — little volume traded, meaning price passed through quickly. **Single prints** are the extreme case: a price touched only once or twice, leaving a thin sliver in the profile. Reading nodes is how traders translate raw volume distribution into a map of acceptance (HVNs) and rejection (LVNs).

## Overview

If the [[point-of-control]] is the single tallest bar, HVNs are the other thick bars, and LVNs are the thin gaps between them. The profile is therefore a sequence of trade zones (HVNs) separated by transition zones (LVNs). Price behaves very differently in each:

- **HVN = acceptance.** Both sides transacted heavily, so there is resting two-sided interest and "memory." Price slows, chops, and often reverses on entering an HVN. HVNs act like magnets and as strong [[support-and-resistance]].
- **LVN = rejection / fast-move.** Little traded there, so there is nothing to absorb an order. When price re-enters an LVN it accelerates through — these are the profile's "gaps." LVNs act as barriers between HVNs and as breakout zones once crossed.

This single insight — *price oscillates within accepted zones and travels quickly through rejected ones* — underpins much of the [[volume-profile-trading-strategy]].

## High-Volume Nodes (HVN)

An HVN marks a price the market was repeatedly willing to trade at. Practically:

- **Support / resistance.** Approached from outside, an HVN slows and often turns price. The thicker and more multi-session the node, the stronger.
- **Magnet.** Price drifts toward nearby HVNs in the absence of a strong trend.
- **Absorption zone.** Aggressive flow into an HVN can be soaked up by resting limit orders ([[absorption]]); a fade against trend is most reliable at a thick composite HVN with absorption visible on the [[footprint-chart]].
- **Consolidation.** Markets spend most of their time inside HVNs, so they are where ranges form.

HVNs from **composite profiles** (many sessions aggregated) are the structural levels swing traders care about; intraday HVNs matter to day traders.

## Low-Volume Nodes (LVN) and single prints

An LVN marks a price the market rejected — it left quickly without building volume. Practically:

- **Fast-move zone.** Re-entry into an LVN tends to produce a quick, low-resistance move to the next HVN; LVNs make good *targets* (price will get there fast) and poor *places to sit* (no support).
- **Breakout boundary.** The LVN separating two value areas is the line a breakout must cross; acceptance through it confirms the move into the next zone.
- **Binary rejection.** Single prints and very thin LVNs often act as sharp inflection points — price either rejects hard or rips straight through.
- **Unfinished auctions.** Single-print runs in [[market-profile]] mark prices the auction skipped; they frequently get revisited and "repaired" later.

## How traders use volume nodes

| Node | Reads as | Typical play |
|------|----------|--------------|
| HVN | Acceptance, support/resistance, magnet | Fade approaches; expect chop/reversal; manage trades around it |
| LVN | Rejection, fast-move gap, barrier | Use as a *target* (fast travel) or breakout trigger; don't expect support inside |
| Single print | Extreme rejection / skipped auction | Sharp inflection; expect a binary reaction or a later "repair" revisit |
| POC | The single highest node | See [[point-of-control]] — fairest price, magnet |

A common composite workflow: build a multi-session profile, mark the major HVNs and the LVNs between them, then trade rotations *between* adjacent HVNs and momentum *through* the LVNs, with the next HVN as the target.

## Worked Example

The following is a qualitative, hypothetical illustration — no real prices are implied.

A swing trader builds a [[composite-profile|composite profile]] over several weeks and the histogram shows a clear two-zone structure: a **lower HVN** where the market consolidated for days, an **upper HVN** from an earlier base, and a pronounced **LVN** (volume gap) separating them — a price band the market sped through once without building business.

The trader treats the structure as a map:

1. **Rotation inside the lower HVN.** While price trades within the lower HVN, the trader expects chop and two-sided rotation, fading approaches to the HVN's upper and lower extremes back toward its centre. The HVN is acceptance, so it behaves as a range, not a launchpad.

2. **Momentum through the LVN.** When price finally pushes out of the lower HVN and *accepts* into the LVN above (builds volume where there was none, confirmed by [[cumulative-volume-delta|CVD]] expanding with price), the trader expects a **fast, low-resistance move** — there is little prior business to absorb orders. The LVN is therefore a poor place to sit but an excellent *target to travel through*; the trader holds for the **upper HVN** as the objective, since price tends to "fall up" or "fall down" through a gap to the next thick node.

3. **Reaction at the upper HVN.** On reaching the upper HVN, acceptance memory reasserts and price slows and chops again. The trader scales out or fades, since the next zone of heavy two-sided interest has been reached.

If the LVN break *fails* — price pokes in but cannot build volume and snaps back into the lower HVN — the trader reads **rejection** and reverts to the rotation playbook. The nodes define *where* price will accelerate or stall; CVD and price action confirm *whether* the break is real.

## Relationship to other levels

- HVNs frequently coincide with the [[point-of-control]] and with classic [[support-and-resistance]] (prior highs/lows), which strengthens them.
- LVNs often align with [[fair-value-gaps]] and with [[liquidity-pools]] just beyond obvious levels, since thin prices are where stops and breakout orders rest.
- The [[value-area-high-and-low|value-area edges]] may sit at or near a node boundary, making the distinction between "edge of value" and "edge of node" blurry but mutually reinforcing.

## Limitations and risks

- **Parameter sensitivity** — what counts as "high" or "low" volume depends on the row size and the profile range; nodes are relative, not absolute.
- **Lookback dependence** — composite HVNs shift with the chosen window; cherry-picking a window that explains current price is curve-fitting.
- **Not directional** — a node tells you *where* price may react, not *which way*; pair with [[order-flow]] / [[cumulative-volume-delta|CVD]] for direction.
- **Illiquid distortion** — on thin or [[wash-trading|wash-traded]] instruments the histogram reflects noise, so "nodes" are spurious.

## Related

- [[volume-profile]] — the histogram nodes are read from
- [[point-of-control]] — the single highest-volume node
- [[value-area]] / [[value-area-high-and-low]] — the acceptance band and its edges
- [[composite-profile]] — multi-session nodes are the structural levels
- [[support-and-resistance]] — HVNs are volume-based S/R
- [[market-profile]] — TPO single prints and skipped auctions
- [[order-flow]] / [[cumulative-volume-delta]] — direction/confirmation at a node
- [[liquidity]] / [[liquidity-pools]] — thin LVN prices are where stops/orders rest
- [[vwap]] — dynamic fair-value reference often near a node
- [[volume-profile-trading-strategy]] — rotation between HVNs, fast-moves through LVNs

## Sources

- Gap-finder Perplexity deep research, "Volume profile indicator as a trading strategy" (2026-06-19).
- Reference video: https://www.youtube.com/watch?v=YmygDgtoxO8
- General market knowledge.
