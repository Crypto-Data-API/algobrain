---
title: "Combination Strategy Matrix"
type: index
created: 2026-07-18
updated: 2026-07-19
status: good
tags: [index, meta, methodology]
aliases: ["Combo Matrix", "Strategy Combination Matrix", "Primitive × Overlay Matrix"]
related: ["[[strategies-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[combinations-overview]]", "[[funding-rate-arbitrage]]", "[[trend-following-cta]]", "[[pairs-trading]]", "[[grid-trading]]"]
---

# Combination Strategy Matrix

A **combination strategy** is a [[edge-taxonomy|primitive edge]] paired with an **overlay or filter** that improves at least one of: selectivity (only taking the subset of signals with the highest expected value), sizing accuracy (scaling risk proportional to signal quality), or survivability (avoiding the regime that kills the primitive). The primitive provides the core P&L mechanism; the overlay does not generate a separate edge — it restricts or modulates deployment of the primitive to reduce the drag of bad-regime losses.

## How to Read This Matrix

- **Rows** = primitive strategy families (what generates the edge)
- **Columns** = overlay/filter types (what gates or sizes the primitive)
- **`[[page]]`** = an existing wiki page covers this exact combination (click to read)
- **`planned`** = the combination is viable and gap-filling; no page exists yet
- **`—`** = non-sensical or redundant combination (see footnotes below the table)

A single cell can hold multiple page references if more than one page exists for a primitive × overlay combination. The matrix is deliberately sparse: most cells are either `planned` (gap to fill) or `—` (non-viable). The goal is to capture the specific combinations that are genuinely additive relative to running the primitive alone.

---

## Matrix

| Primitive \ Overlay | Regime gate | Funding filter | OI filter | Trend gate | Tail-hedge overlay | Vol targeting | Cross-venue | Unlock/event calendar | Sentiment-extreme filter | Session/time filter |
|---|---|---|---|---|---|---|---|---|---|---|
| **Funding carry** | [[regime-adaptive-strategy]] | — ¹ | [[oi-confirmed-trend]] ² | planned | [[carry-with-tail-hedge]] | planned | [[hl-vs-cex-funding-divergence]] | planned | [[crowded-long-funding-fade]] | planned |
| **Basis / cash-and-carry** | [[regime-adaptive-strategy]] | planned | planned | planned | [[carry-with-tail-hedge]] | planned | [[hl-vs-cex-funding-divergence]] | planned | planned | planned |
| **Momentum / trend** | [[regime-adaptive-strategy]] | [[funding-filtered-momentum]] | [[oi-confirmed-trend]] | — ³ | [[trend-plus-tail-hedge]] | [[vol-targeted-trend-following]] | planned | [[unlock-aware-momentum]] | [[contrarian-extremes]] ⁴ | planned |
| **Mean-reversion** | [[regime-adaptive-strategy]] | [[funding-flush-reversal]] | [[oi-flush-reversion]] | planned | planned | planned | planned | planned | [[contrarian-extremes]] | planned |
| **Liquidation plays** | [[regime-adaptive-strategy]] | [[crowded-long-funding-fade]] | [[oi-confirmed-trend]] | planned | planned | planned | planned | planned | planned | planned |
| **Narrative / event** | [[regime-adaptive-strategy]] | planned | [[oi-confirmed-trend]] | planned | planned | planned | planned | [[unlock-short-with-crowding-gate]] | [[contrarian-extremes]] | planned |
| **Vol selling** | [[regime-adaptive-strategy]] | planned | planned | planned | — ⁵ | [[volatility-targeting]] | planned | planned | planned | planned |
| **Vol buying / tail hedge** | [[regime-adaptive-strategy]] | planned | planned | planned | — ⁶ | planned | planned | planned | planned | planned |
| **Grid / market-making** | [[regime-gated-grid]] | [[funding-skewed-grid]] | planned | — ⁷ | planned | planned | planned | planned | planned | [[session-overlap-momentum]] ⁸ |
| **Stat-arb / pairs** | [[regime-adaptive-strategy]] | [[pairs-with-funding-differential]] | planned | planned | planned | planned | [[hl-vs-cex-funding-divergence]] | planned | planned | planned |
| **On-chain flow** | [[regime-adaptive-strategy]] | planned | [[oi-confirmed-trend]] | [[smart-money-orderflow-combo]] ⁹ | planned | planned | planned | [[unlock-short-with-crowding-gate]] | planned | planned |
| **Sentiment** | [[regime-adaptive-strategy]] | planned | planned | [[crypto-beta-rotation]] | planned | planned | planned | planned | — ¹⁰ | planned |

---

### Footnotes

**¹ Funding carry × funding filter = self-referential.** The primitive *is* the funding signal. Adding a "funding filter" would mean gating the carry trade on its own entry signal, which is already baked into the primitive's rules. Not a separate overlay.

**² OI-confirmed-trend** is listed under funding carry because the [[oi-confirmed-trend]] basket uses OI confirmation on Hyperliquid perp trends, which are directly linked to the funding-carry regime; the OI filter acts on top of carry.

**³ Momentum × trend gate = tautology.** Momentum is the trend. Gating a trend strategy on "trend confirmed" replicates the trend signal itself, not a separate overlay.

**⁴ [[contrarian-extremes]]** inverts momentum at sentiment extremes — this is a sentiment-filter on momentum, making it a combination; the page covers both components.

**⁵ Vol selling × tail-hedge overlay = partial cancellation.** A tail-hedge overlay on a vol-selling book reduces net short-vol exposure. This is just a smaller vol-selling position with higher costs, not a genuinely new combination. The right framing is position sizing, not a named combination.

**⁶ Vol buying × tail-hedge overlay = double-counting.** Long vol is itself the tail hedge; overlaying another tail hedge adds only a second long-vol position.

**⁷ Grid × trend gate = exit rule, not overlay.** The regime kill on a grid trade is a stop, not a separate overlay that generates edge. [[regime-gated-grid]] captures this framing.

**⁸ [[session-overlap-momentum]]** is listed under grid/market-making × session filter because session-overlap momentum exploits the liquidity structure that also drives grid profitability.

**⁹ [[smart-money-orderflow-combo]]** combines on-chain smart-money with order-flow confirmation — structurally this is an on-chain-flow primitive gated by a short-term trend/order-flow signal.

**¹⁰ Sentiment × sentiment-extreme filter = self-referential.** The sentiment *primitive* already acts on sentiment signals; gating it on another sentiment extreme is not a separate overlay.

---

## Matrix Cell Counts (as of 2026-07-19)

| Status | Count |
|---|---|
| Linked to existing page | 27 |
| Planned (gap to fill) | 64 |
| Non-viable (`—`) | 9 |

---

## Batch B2 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[pairs-with-funding-differential]] — stat-arb/pairs × funding filter
- [[funding-flush-reversal]] — mean-reversion × funding filter
- [[unlock-aware-momentum]] — momentum × unlock/event calendar
- [[funding-skewed-grid]] — grid/market-making × funding filter
- [[oi-flush-reversion]] — mean-reversion × OI filter

---

## Batch B1 New Pages (2026-07-18)

Five new combination pages created in this batch — matrix cells updated above:

- [[funding-filtered-momentum]] — momentum × funding filter
- [[regime-gated-grid]] — grid × regime gate
- [[carry-with-tail-hedge]] — funding carry + basis × tail-hedge overlay
- [[unlock-short-with-crowding-gate]] — narrative/event × funding filter (unlock context)
- [[vol-targeted-trend-following]] — momentum × vol targeting

---

## Related

- [[strategies-overview]] — the full strategy catalog hub
- [[combinations-overview]] — the combinations subcategory overview
- [[edge-taxonomy]] — the six edge sources that primitives harvest
- [[regime-matrix]] — which strategies work in which regimes
- [[regime-strategy-playbook]] — operational playbook for regime-matched deployment
- [[failure-modes]] — why combinations fail (the overlay does not fix a broken primitive)
- [[funding-rate-arbitrage]] — the canonical funding carry primitive
- [[trend-following-cta]] — the canonical momentum/trend primitive
- [[pairs-trading]] — the canonical stat-arb primitive
- [[grid-trading]] — the canonical grid/market-making primitive
