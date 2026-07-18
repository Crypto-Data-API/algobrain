---
title: "Combination Strategies"
type: overview
created: 2026-07-18
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, methodology, portfolio-theory]
aliases: ["Combinations Overview", "Strategy Combinations", "Combo Strategies"]
related: ["[[strategies-overview]]", "[[combination-matrix]]", "[[multi-strategy-portfolio]]", "[[regime-adaptive-strategy]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[kelly-for-strategies]]"]
---

# Combination Strategies

Combination strategies pair a **primitive edge** — a core P&L mechanism from one of the fundamental strategy families — with an **overlay or filter** that improves its selectivity, sizing, or survivability. The primitive is where the edge lives; the overlay restricts or modulates deployment so the strategy only runs in conditions where its edge is most reliable and avoids the regime that kills it.

This is different from a multi-strategy portfolio (see [[multi-strategy-portfolio]]), where the goal is diversification across uncorrelated edges. A combination strategy has **one primary edge** — the primitive — and the overlay is a risk-management or signal-quality tool, not a second independent source of alpha.

For a structured view of which overlays work with which primitives, see the **[[combination-matrix]]**.

---

## What Makes a Good Combination

A combination earns its existence when:

1. **The overlay is independently measurable.** A funding-rate filter on momentum requires real-time funding data — not the momentum signal itself. An overlay that is derived from the same data as the primitive adds noise, not information.
2. **The overlay targets the primitive's known failure mode.** Grid trading fails in trends → regime gate. Carry fails in funding inversions → tail hedge. Unlock shorts fail when crowded → crowding gate. The overlay must address a *specific, identified* failure mode, not a generic risk.
3. **The combination survives cost.** Adding an overlay always adds cost (data requirements, monitoring complexity, trade frequency changes). The improvement in risk-adjusted returns must exceed that cost.
4. **The overlay does not eliminate the primitive's edge.** An OTM put overlay on vol selling (the [[failure-modes|Failure Mode #5]] hedge attempt) just reduces vol-selling exposure — it does not produce a new edge. Not every pair of strategies is a viable combination.

---

## Pages in This Category

```dataview
TABLE strategy_type, timeframe, edge_source, backtest_status, expected_sharpe, status
FROM "wiki/strategies/combinations"
WHERE type = "strategy"
SORT status DESC, updated DESC
```

---

## Primitive × Overlay Coverage

The [[combination-matrix]] maps the full space of crypto strategy primitives against overlays/filters. **Program complete as of 2026-07-19: all 120 matrix cells are either linked to a dedicated page or marked non-viable with a reasoned footnote (0 planned cells remain). The wiki now contains 66 combination strategy pages.**

| Status | Count |
|---|---|
| Existing pages | 66 matrix cells covered |
| Planned | 0 |
| Non-viable (`—`) | 54 cells (explained in the matrix with footnotes ¹–⁶⁵) |

---

## Combination Families

### Carry + Overlays
The [[funding-rate-arbitrage|funding carry]] primitive extended by:
- **[[carry-with-tail-hedge]]** — budgeted OTM put overlay financed from carry income
- **[[delta-neutral-yield-farming]]** — staking yield stacked on top of the carry book
- **[[hl-vs-cex-funding-divergence]]** — cross-venue carry spread (Hyperliquid vs CEX)

### Momentum + Overlays
The [[trend-following-cta|trend/momentum]] primitive extended by:
- **[[funding-filtered-momentum]]** — momentum entries gated by non-consensus funding
- **[[vol-targeted-trend-following]]** — vol-scaled position sizing on momentum signals
- **[[oi-confirmed-trend]]** — OI confirmation filter on Hyperliquid trend entries
- **[[trend-plus-tail-hedge]]** — trend book plus explicit tail-hedge overlay

### Grid / Market-Making + Overlays
- **[[regime-gated-grid]]** — grid deployed only inside confirmed range regimes, hard-killed on regime flip

### Event-Driven + Overlays
- **[[unlock-short-with-crowding-gate]]** — token unlock shorts filtered for non-crowded entry conditions
- **[[contrarian-extremes]]** — sentiment-extreme filter on mean-reversion entries

### Multi-Strategy Meta-Combinations
- **[[regime-adaptive-strategy]]** — regime-switching across multiple sub-strategies
- **[[multi-strategy-portfolio]]** — correlation-adjusted allocation across uncorrelated strategy families
- **[[volatility-targeting]]** — portfolio-level vol-targeting as a sizing overlay
- **[[asymmetric-barbell]]** — barbell construction (safe core + speculative tail)
- **[[delta-neutral-yield-farming]]** — yield stacking with delta hedge
- **[[crypto-yield-stack]]** — DeFi layer stacking (directional)

### Information + Overlays
- **[[smart-money-orderflow-combo]]** — on-chain smart-money signal confirmed by live order flow
- **[[alternative-data-alpha]]** — alternative data overlaid on price signals
- **[[dca-technical-hybrid]]** — DCA timing improved by technical entry signals

---

## Key Concepts for Building Combinations

- **[[edge-taxonomy]]** — the six edge sources; combination overlays must address a *different* dimension from the primitive or the same dimension more precisely
- **[[failure-modes]]** — the catalog of how strategies die; the best overlays target specific failure modes
- **[[regime-matrix]]** — which primitives work in which regimes; the regime gate is a direct read from this
- **[[when-to-retire-a-strategy]]** — the framework for deciding when a combination is no longer viable (and whether to retire or just pause)
- **[[kelly-for-strategies]]** — sizing the combination's capital allocation within a book

---

## Related

- [[strategies-overview]] — the full strategy hub
- [[combination-matrix]] — the structured primitive × overlay matrix
- [[multi-strategy-portfolio]] — portfolio-level combination (diversification across edges)
- [[regime-adaptive-strategy]] — regime-switching meta-strategy
- [[edge-taxonomy]] — edge classification
- [[failure-modes]] — why strategies and combinations fail
