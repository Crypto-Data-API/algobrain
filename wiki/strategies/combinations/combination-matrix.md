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
| **Funding carry** | [[regime-adaptive-strategy]] | — ¹ | [[oi-confirmed-trend]] ² | [[trend-aware-carry]] | [[carry-with-tail-hedge]] | planned | [[hl-vs-cex-funding-divergence]] | planned | [[crowded-long-funding-fade]] | planned |
| **Basis / cash-and-carry** | [[regime-adaptive-strategy]] | [[funding-vs-basis-rotation]] ¹¹ | planned | planned | [[carry-with-tail-hedge]] | planned | [[hl-vs-cex-funding-divergence]] | planned | planned | planned |
| **Momentum / trend** | [[regime-adaptive-strategy]] | [[funding-filtered-momentum]] | [[oi-confirmed-trend]] | — ³ | [[trend-plus-tail-hedge]] | [[vol-targeted-trend-following]] | [[spot-led-momentum-filter]] | [[unlock-aware-momentum]] | [[contrarian-extremes]] ⁴ | [[session-aware-mean-reversion]] ¹² |
| **Mean-reversion** | [[regime-adaptive-strategy]] | [[funding-flush-reversal]] | [[oi-flush-reversion]] | planned | planned | planned | planned | planned | [[contrarian-extremes]] | [[session-aware-mean-reversion]] |
| **Liquidation plays** | [[regime-adaptive-strategy]] | [[crowded-long-funding-fade]] | [[oi-confirmed-trend]] | planned | [[cascade-monetization-rotation]] ¹³ | planned | planned | planned | planned | [[off-hours-liquidation-playbook]] |
| **Narrative / event** | [[regime-adaptive-strategy]] | planned | [[oi-confirmed-trend]] | [[narrative-with-trend-confirmation]] | planned | planned | planned | [[unlock-short-with-crowding-gate]] | [[contrarian-extremes]] | planned |
| **Vol selling** | [[regime-adaptive-strategy]] | [[funding-conditioned-vol-selling]] | planned | [[trend-aligned-premium-selling]] | — ⁵ | [[volatility-targeting]] | planned | planned | [[post-panic-vol-selling]] | planned |
| **Vol buying / tail hedge** | [[regime-adaptive-strategy]] | planned | [[leverage-stress-tail-hedge]] | planned | — ⁶ | planned | planned | [[event-vol-buying]] | planned | planned |
| **Grid / market-making** | [[regime-gated-grid]] | [[funding-skewed-grid]] | planned | — ⁷ | planned | planned | planned | planned | planned | [[session-overlap-momentum]] ⁸ |
| **Stat-arb / pairs** | [[correlation-regime-pairs]] | [[pairs-with-funding-differential]] | planned | planned | planned | planned | [[hl-vs-cex-funding-divergence]] | [[unlock-pair-hedge]] | planned | planned |
| **On-chain flow** | [[regime-adaptive-strategy]] | planned | [[oi-confirmed-trend]] | [[smart-money-orderflow-combo]] ⁹ | planned | planned | planned | [[unlock-short-with-crowding-gate]] | [[onchain-capitulation-confluence]] | planned |
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

**¹¹ [[funding-vs-basis-rotation]]** is listed under basis/cash-and-carry × funding filter because it is the *allocation-layer* strategy that switches the carry book between perp-funding carry and dated-futures basis carry depending on which pays more — the funding filter is the rotation decision rule that gates which instrument is active.

**¹² [[session-aware-mean-reversion]]** appears in both momentum × session/time filter and mean-reversion × session/time filter cells because the strategy covers session-conditional parameter adjustment for both RSI/VWAP-based mean-reversion and the fading of off-hours momentum overshoots at major-session opens. The primary primitive is mean-reversion (session conditioning amplifies the reversion); the momentum row cell reflects the "fade the off-hours drift at session open" use case.

**¹³ [[cascade-monetization-rotation]]** is placed in the liquidation plays × tail-hedge cell rather than vol buying × tail-hedge because the defining P&L mechanism is the capital rotation from the tail-hedge payoff into a cascade-fade entry — the liquidation-plays (cascade fade) leg is the completion of the lifecycle. The tail hedge is the entry leg (referenced to [[leverage-stress-tail-hedge]]); the liquidation-fade redeployment is the exit and redeployment logic. This page would be redundant with [[leverage-stress-tail-hedge]] in the vol buying row.

---

## Matrix Cell Counts (as of 2026-07-19)

| Status | Count |
|---|---|
| Linked to existing page | 42 |
| Planned (gap to fill) | 49 |
| Non-viable (`—`) | 9 |

---

## Batch B5 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[trend-aware-carry]] — funding carry × trend gate (carry book that scales down or exits the short-perp leg when a strong directional trend is running against the structure; uptrends at SMA20+15% + RSI ≥ 70 + funding ≥ 0.05%/8h trigger 60% → 30% deployment reduction; different from carry-with-tail-hedge which maintains full deployment with a permanent hedge overlay)
- [[post-panic-vol-selling]] — vol selling × sentiment-extreme filter (sell BTC/ETH options after a panic spike once five stabilisation gates are simultaneously confirmed: Fear & Greed ≤ 20 for 2 days, DVOL ≥ 85th percentile AND +20 vol-pt spike, 24h RV rolling over from ≥ 80 vol-pt peak, no fresh cascade in 12h, no new 7-day low in 4h; explicitly differentiated from funding-conditioned-vol-selling which fires on bullish crowding, not post-crash fear)
- [[cascade-monetization-rotation]] — liquidation plays × tail-hedge overlay (lifecycle strategy: accumulate OTM puts during stress buildup per leverage-stress-tail-hedge entry rules, monetise when cascade fires ≥12% drop or DVOL +25pts+$500M liq, rotate 60% of gross payoff into cascade-fade perp long within 4 hours; the combination is the capital rotation, not a novel approach to either leg)
- [[unlock-pair-hedge]] — stat-arb/pairs × unlock/event calendar (express cliff unlock shorts as a long-short pair: short the unlocking token perp, long a beta-matched sector peer in a 1/beta ratio; strips BTC/sector beta to isolate idiosyncratic supply shock; explicitly differentiated from unlock-short-with-crowding-gate which is an outright short filtered for crowding, not a beta-hedged pairs structure)
- [[trend-aligned-premium-selling]] — vol selling × trend gate (sell puts in confirmed uptrends, calls in confirmed downtrends; trend selects which wing to sell rather than whether to sell; DVOL ≥ 50th percentile + trend confirmation = sell the under-bid wing; explicitly differentiated from funding-conditioned-vol-selling which fires on funding crowding in any regime, and from post-panic-vol-selling which fires on post-crash fear)

Skips (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.

Note: [[post-panic-vol-selling]] fills the vol selling × sentiment-extreme filter cell; [[trend-aligned-premium-selling]] fills the vol selling × trend gate cell. The two vol-selling combos are in different cells and their leads explicitly differentiate them from each other and from funding-conditioned-vol-selling.

---

## Batch B4 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[correlation-regime-pairs]] — stat-arb/pairs × regime gate (cointegration-regime gate: rolling correlation floor + cointegration test significance + OU half-life within bounds; flatten on correlation breakdown instead of averaging into a structurally broken spread)
- [[event-vol-buying]] — vol buying × unlock/event calendar (buy ATM straddles or OTM strangles on Deribit ahead of scheduled binary-outcome catalysts — halvings, ETF/regulatory decisions, major Ethereum upgrades, large unlocks — when IV has not yet priced the event; exit into IV spike or within 48h post-event)
- [[session-aware-mean-reversion]] — mean-reversion × session/time filter (session-conditional parameter table for RSI/VWAP/Bollinger-based reversion: lower thresholds and higher targets in thin off-hours and weekend sessions; session-open transition windows as highest-conviction entry timing; explicitly differentiated from off-hours-liquidation-playbook which requires a cascade trigger)
- [[leverage-stress-tail-hedge]] — vol buying/tail hedge × OI filter (accumulate OTM puts when all three stress gates are simultaneously elevated: OI/market-cap ≥ 3%, 7d-average funding ≥ 0.04%/8h, long/short ratio ≥ 1.8; exit on crash payoff, IV expansion, or stress deactivation; explicitly standalone — not a carry-book hedge)
- [[spot-led-momentum-filter]] — momentum × cross-venue (momentum entries only when the move is spot-led: positive Coinbase premium sustained ≥ 2h, funding flat/≤ 0.03%, and spot volume growing faster than OI; differentiated from funding-filtered-momentum which gates on funding LEVEL; this page gates on flow ORIGIN/cross-venue structure)

Skips (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.

Note: [[session-aware-mean-reversion]] is placed in both the mean-reversion × session/time and momentum × session/time cells (see footnote ¹²). Both planned cells are now covered by a single page; net reduction in planned count = 5 pages × varying planned-cell coverage.

---

## Batch B3 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[funding-vs-basis-rotation]] — basis/cash-and-carry × funding filter (allocation layer between perp-funding carry and dated-futures basis carry)
- [[funding-conditioned-vol-selling]] — vol selling × funding filter (enter short-vol only when elevated funding confirms leverage-crowd VRP richness)
- [[off-hours-liquidation-playbook]] — liquidation plays × session/time filter (session-conditional cascade-fade with adjusted triggers, sizing, and slippage per liquidity window)
- [[narrative-with-trend-confirmation]] — narrative/event × trend gate (require breakout / higher-low above MA before entering narrative trade)
- [[onchain-capitulation-confluence]] — on-chain flow × sentiment-extreme filter (bottom entry requires BOTH on-chain capitulation signal AND Fear & Greed extreme simultaneously)

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
