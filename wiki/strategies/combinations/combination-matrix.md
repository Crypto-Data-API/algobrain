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
| **Funding carry** | [[regime-adaptive-strategy]] | — ¹ | [[oi-confirmed-trend]] ² | [[trend-aware-carry]] | [[carry-with-tail-hedge]] | planned | [[hl-vs-cex-funding-divergence]] | planned | [[crowded-long-funding-fade]] | [[funding-window-timing]] ¹⁷ |
| **Basis / cash-and-carry** | [[regime-adaptive-strategy]] | [[funding-vs-basis-rotation]] ¹¹ | planned | planned | [[carry-with-tail-hedge]] | planned | [[hl-vs-cex-funding-divergence]] | planned | planned | planned |
| **Momentum / trend** | [[regime-adaptive-strategy]] | [[funding-filtered-momentum]] | [[oi-confirmed-trend]] | — ³ | [[trend-plus-tail-hedge]] | [[vol-targeted-trend-following]] | [[spot-led-momentum-filter]] | [[unlock-aware-momentum]] | [[contrarian-extremes]] ⁴ | [[session-aware-mean-reversion]] ¹² |
| **Mean-reversion** | [[regime-adaptive-strategy]] | [[funding-flush-reversal]] | [[oi-flush-reversion]] | [[pullback-trading]] ²² | [[put-protected-dip-buying]] ¹⁴ | planned | planned | planned | [[contrarian-extremes]] | [[session-aware-mean-reversion]] |
| **Liquidation plays** | [[regime-adaptive-strategy]] | [[crowded-long-funding-fade]] | [[oi-confirmed-trend]] | planned | [[cascade-monetization-rotation]] ¹³ | planned | [[cross-venue-cascade-dislocation]] ¹⁸ | planned | planned | [[off-hours-liquidation-playbook]] |
| **Narrative / event** | [[regime-adaptive-strategy]] | planned | [[oi-confirmed-trend]] | [[narrative-with-trend-confirmation]] | planned | [[narrative-position-vol-targeting]] | planned | [[unlock-short-with-crowding-gate]] | [[contrarian-extremes]] | planned |
| **Vol selling** | [[regime-adaptive-strategy]] | [[funding-conditioned-vol-selling]] | [[low-leverage-vol-selling]] ¹⁵ | [[trend-aligned-premium-selling]] | — ⁵ | [[volatility-targeting]] | planned | planned | [[post-panic-vol-selling]] | planned |
| **Vol buying / tail hedge** | [[regime-adaptive-strategy]] | planned | [[leverage-stress-tail-hedge]] | [[long-options-trend-expression]] ¹⁹ | — ⁶ | planned | planned | [[event-vol-buying]] | planned | planned |
| **Grid / market-making** | [[regime-gated-grid]] | [[funding-skewed-grid]] | [[oi-aware-grid]] | — ⁷ | [[grid-with-tail-hedge]] ²⁰ | planned | planned | planned | planned | [[session-overlap-momentum]] ⁸ |
| **Stat-arb / pairs** | [[correlation-regime-pairs]] | [[pairs-with-funding-differential]] | planned | planned | planned | planned | [[hl-vs-cex-funding-divergence]] | [[unlock-pair-hedge]] | planned | planned |
| **On-chain flow** | [[regime-adaptive-strategy]] | [[smart-money-vs-crowd-divergence]] ¹⁶ | [[oi-confirmed-trend]] | [[smart-money-orderflow-combo]] ⁹ | planned | planned | planned | [[unlock-short-with-crowding-gate]] | [[onchain-capitulation-confluence]] | planned |
| **Sentiment** | [[regime-adaptive-strategy]] | [[sentiment-positioning-divergence]] ²¹ | planned | [[crypto-beta-rotation]] | planned | planned | planned | planned | — ¹⁰ | planned |

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

**¹⁴ [[put-protected-dip-buying]]** is placed in the mean-reversion × tail-hedge overlay cell because the strategy's defining feature is a post-capitulation mean-reversion entry (the primitive) paired with a simultaneously-purchased OTM put (the tail-hedge overlay that converts the infinite downside into a hard floor). The three capitulation entry triggers ([[funding-flush-reversal]], [[oi-flush-reversion]], [[onchain-capitulation-confluence]]) define WHEN to enter; the put overlay defines the RISK STRUCTURE of the entry. Differentiated from [[leverage-stress-tail-hedge]] (pre-crash put accumulation without a simultaneous long entry) and from [[cascade-monetization-rotation]] (lifecycle rotation structure).

**¹⁵ [[low-leverage-vol-selling]]** is placed in the vol selling × OI filter cell because the primary structural gate is OI/market-cap below a threshold — the same OI metric as [[leverage-stress-tail-hedge]]'s stress gate, but inverted: this page enters short-vol only when OI/MC is LOW (structural cascade fuel absent). It is explicitly differentiated from all three other vol-selling combos: [[funding-conditioned-vol-selling]] (enters when funding is HIGH), [[post-panic-vol-selling]] (enters post-event when fear is extreme), and [[trend-aligned-premium-selling]] (enters based on trend direction to select which wing to sell). This page is the fourth distinct entry regime for vol-selling: the structural-leverage-absence gate.

**¹⁶ [[smart-money-vs-crowd-divergence]]** is placed in the on-chain flow × funding filter cell because the strategy's second leg is a derivative-crowd positioning filter (flat/negative funding, short-biased long/short ratio) applied on top of the on-chain smart-money accumulation signal. The funding filter is the crowd-positioning gate; the on-chain accumulation is the primary informed-flow signal. Explicitly differentiated from [[smart-money-orderflow-combo]] (order-flow-based second leg, intraday) and [[crowded-short-funding-fade]] (funding filter alone without on-chain confirmation).

**¹⁷ [[funding-window-timing]]** is placed in the funding carry × session/time filter cell because the strategy is a peri-settlement timing overlay on the funding carry primitive: it exploits the 30–60 minute pre-settlement repositioning drift around the 8-hourly CEX (00:00/08:00/16:00 UTC) and hourly Hyperliquid funding settlement timestamps. The session/time filter is the predictable discrete settlement schedule. Differentiated from [[hl-vs-cex-funding-divergence]] (rate spread, not settlement timing), [[funding-skewed-grid]] (continuous intraday centre adjustment), and [[funding-rate-harvest]] (multi-period carry, not peri-settlement scalp).

**¹⁸ [[cross-venue-cascade-dislocation]]** is placed in the liquidation plays × cross-venue cell because the strategy exploits the transient price dislocation between Hyperliquid and Binance perp markets that arises specifically during concentrated liquidation cascades — the liquidation play is the primary P&L mechanism (forced non-economic flow on the dislocated venue); the cross-venue hedge (long dislocated HL, short calm Binance) is the structural risk-neutralisation that converts a directional fade into a near-market-neutral spread trade. Differentiated from [[liquidation-cascade-arbitrage]] (DeFi MEV on-chain liquidation bonus — entirely different mechanism), [[hl-vs-cex-funding-divergence]] (steady-state funding spread, not cascade price gap), and [[cross-exchange-arbitrage]] (continuous price arb in normal conditions, not cascade-triggered).

**¹⁹ [[long-options-trend-expression]]** is placed in the vol buying/tail hedge × trend gate cell because the strategy uses a confirmed trend gate to select direction and an IV/RV filter to select the instrument (long call or call spread instead of futures/perp when IV is cheap relative to realized vol). The vol-buying/options instrument is how the trend is expressed; the trend gate is the direction-selection overlay. Differentiated from [[event-vol-buying]] (calendar-triggered, direction-agnostic straddles) and [[trend-plus-tail-hedge]] (long trend position + tail hedge, not trend expression via long options).

**²⁰ [[grid-with-tail-hedge]]** is placed in the grid/market-making × tail-hedge overlay cell because the strategy overlays a budgeted OTM put position — financed entirely from grid income — on top of a standard grid, capping the maximum loss from gap-through-the-ladder events. The tail-hedge overlay converts the grid from infinite-downside to bounded-maximum-loss per cycle. The income-financing pattern is adapted from [[carry-with-tail-hedge]]. Differentiated from [[regime-gated-grid]], [[oi-aware-grid]], and [[funding-skewed-grid]] (all gate WHEN/HOW the grid runs; this page caps the loss WHEN those gates fail).

**²¹ [[sentiment-positioning-divergence]]** is placed in the sentiment × funding filter cell because the strategy trades the gap between STATED sentiment (Fear & Greed index extreme) and ACTUAL positioning (funding rate and long/short ratio): extreme fear + negative funding = washout complete (long); extreme fear + positive funding = capitulation incomplete (avoid or short modestly). The funding filter is the positioning-reality check that validates or invalidates the stated sentiment signal. Differentiated from [[contrarian-extremes]] (stated sentiment alone, no positioning confirmation), [[crowded-short-funding-fade]] (positioning alone, no sentiment gate), and [[smart-money-vs-crowd-divergence]] (on-chain accumulation vs positioning, not stated sentiment vs positioning).

**²² [[pullback-trading]]** is listed in the mean-reversion × trend gate cell as the existing page that substantively covers higher-timeframe-trend-gated mean-reversion entries. [[pullback-trading]] documents the retracement entry framework (buying weakness in intact uptrends after leveraged weak hands are flushed; entry conditioned on the higher-timeframe trend remaining intact). [[trend-pullback-rally-fade]] (Hyperliquid basket, piloted) covers the same framework in a more systematic basket form. The B7 backup candidate `higher-timeframe-reversion-gate` was assessed and found covered by these two pages; no new page was written.

---

## Matrix Cell Counts (as of 2026-07-19)

| Status | Count |
|---|---|
| Linked to existing page | 53 |
| Planned (gap to fill) | 38 |
| Non-viable (`—`) | 9 |

---

## Batch B7 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[funding-window-timing]] — funding carry × session/time filter (peri-settlement timing overlay: enters 40–50 min before 8h CEX settlement timestamps (00:00/08:00/16:00 UTC) or 10–15 min before Hyperliquid's hourly settlement when |funding| ≥ 0.015%/8h, OI ≥ 60th percentile, and no cascade active; exploits the discrete repositioning drift as large leveraged participants position on the receiving side before the snapshot fires; explicitly differentiated from hl-vs-cex-funding-divergence (rate spread), funding-skewed-grid (continuous centre adjustment), funding-rate-harvest (multi-period carry), and session-overlap-momentum (geographic session overlap, not settlement timestamp))
- [[grid-with-tail-hedge]] — grid/market-making × tail-hedge overlay (OTM put overlay financed from grid income: budget = 15–25% of trailing 14d net grid P&L, capped at 0.8% of notional; buys 10–15% OTM put at DTE 21–35 only when DVOL ≤ 70th percentile; grid halt fires if ADX > 25 or 12h OI change > +3%; put payoff caps gap-through-the-ladder loss; converts grid from infinite-downside to bounded-maximum-loss per cycle; explicitly differentiated from regime-gated-grid, oi-aware-grid, funding-skewed-grid (all gate WHEN/HOW the grid runs — this caps the loss WHEN those gates fail); income-financing pattern adapted from carry-with-tail-hedge)
- [[sentiment-positioning-divergence]] — sentiment × funding filter ("talk vs money": two setups: (1) washout long: Fear & Greed ≤ 20 for ≥ 2 days AND funding ≤ −0.005%/8h AND L/S ≤ 0.90 AND higher low on daily → enter long; (2) incomplete-cap: Fear & Greed ≤ 20 AND funding ≥ +0.010%/8h AND L/S ≥ 1.10 → avoid long / short modestly; explicitly differentiated from contrarian-extremes (sentiment alone, no positioning gate), crowded-short-funding-fade (positioning alone, no sentiment gate), and smart-money-vs-crowd-divergence (on-chain vs positioning, not stated sentiment vs positioning))
- [[long-options-trend-expression]] — vol buying/tail hedge × trend gate (express confirmed trends via long calls or call spreads on Deribit when IV is cheap relative to realized vol: trend gate = daily close ≥ 12% above EMA50, 4h RSI ≥ 58, 7d avg funding ≥ 0.015%/8h; IV-cheap gate = DVOL ≤ 90% of 30d avg OR 20d RV ≥ DVOL + 5 vol pts OR DVOL ≤ 40th pct; strike 10–15% OTM, DTE 35–55 days; eliminates stop-wicking failure mode — option cannot be stopped out, only expired; explicitly differentiated from trend-following-cta (futures + stop), vol-targeted-trend-following (size scaling not instrument switch), event-vol-buying (calendar-driven straddles), and trend-aligned-premium-selling (sells options when IV elevated — structural complement))
- [[cross-venue-cascade-dislocation]] — liquidation plays × cross-venue (during cascades HL-Binance BTC perp spread ≥ 0.5% [liq volume ≥ 3× 7d avg trigger]: go long HL (dislocated) + short Binance (reference), equal notional, 1:1 hedge; exit when spread reconverges to ≤ 0.1% or 15-minute time limit; stop at spread ≥ 1.5%; explicitly differentiated from liquidation-cascade-arbitrage (DeFi MEV on-chain liquidation bonus — different mechanism entirely), hl-vs-cex-funding-divergence (steady-state funding spread, not cascade price dislocation), and cross-exchange-arbitrage (continuous arb in normal conditions, not cascade-triggered))

Skips (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.

Backup evaluation: `higher-timeframe-reversion-gate` — mean-reversion × trend gate — is already substantively covered by [[pullback-trading]] (retracement entry in uptrend; swing/position) and [[trend-pullback-rally-fade]] (counter-trend entry with the primary trend; HL basket, piloted). Both pages document taking mean-reversion entries WITH the higher-timeframe trend. Matrix cell (mean-reversion × trend gate) marked [[pullback-trading]] ²² as the existing page reference. Backup `vol-balanced-pairs` (stat-arb × vol targeting) remains `planned` — not yet covered.

Note: [[long-options-trend-expression]] (vol buying/tail hedge × trend gate) is placed in the vol buying row rather than momentum/trend row because the defining P&L mechanism is the long options instrument (vol buying/tail hedge family) and the trend gate is the overlay. The momentum/trend row's trend gate cell is a tautology (see footnote ³); the vol-buying row's trend gate cell was vacant and is the correct placement.

---

## Batch B6 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[put-protected-dip-buying]] — mean-reversion × tail-hedge overlay (post-capitulation dip-buy with a simultaneously-purchased OTM put as a contractual disaster floor; cannot gap through; entry-trigger-agnostic: uses any of funding-flush-reversal, oi-flush-reversion, or onchain-capitulation-confluence to define WHEN; the put defines the RISK STRUCTURE; differentiated from leverage-stress-tail-hedge which accumulates puts pre-crash without a simultaneous long, and from cascade-monetization-rotation's lifecycle rotation)
- [[oi-aware-grid]] — grid/market-making × OI filter (pause or de-size the grid when 12h OI change ≥ +5% — rapid OI build signals directional leverage entering the market and creating breakout fuel; resume after OI stabilises below +3%/12h for 6 consecutive hours; explicitly differentiated from regime-gated-grid which uses lagging vol-regime indicators: OI build fires 4–24 hours before the breakout, earlier than ADX/Bollinger-bandwidth)
- [[narrative-position-vol-targeting]] — narrative/event × vol targeting (vol-scale each narrative/memecoin position to a fixed 1%-of-portfolio daily-risk budget so hot high-vol names cannot dominate portfolio risk; portfolio heat cap limits total concurrent narrative notional to 25% of portfolio; explicitly differentiated from vol-targeted-trend-following which applies vol targeting to the large-cap BTC/ETH trend book — this page targets the high-vol-dispersion narrative sub-book where 20-day RV ranges from 80% to 500%+ annualised)
- [[smart-money-vs-crowd-divergence]] — on-chain flow × funding filter (long entry when whale accumulation score ≥ 65 AND exchange outflows top-quartile AND 8h funding ≤ 0.00%/8h AND long/short ≤ 0.95 AND at least one higher low on daily — informed on-chain accumulation while the derivative crowd is bearishly positioned; explicitly differentiated from smart-money-orderflow-combo which uses real-time order-flow as the second leg, and from crowded-short-funding-fade which requires no on-chain confirmation)
- [[low-leverage-vol-selling]] — vol selling × OI filter (sell vol ONLY when structural cascade fuel is absent: OI/MC ≤ 2.0%, funding flat [−0.01%, +0.02%/8h], long/short balanced [0.9–1.2]; the structural inverse of leverage-stress-tail-hedge; differentiated from all three prior vol-selling combos: funding-conditioned-vol-selling [enters when funding is HIGH], post-panic-vol-selling [post-event fear extreme], trend-aligned-premium-selling [trend-selected wing] — this is the fourth vol-selling regime: structural leverage ABSENCE gate)

Skips (0 of 5 primaries): all five primary candidates confirmed additive. No backups used.

Note: [[low-leverage-vol-selling]] fills the vol selling × OI filter cell with an inverted OI gate (OI LOW = safe to sell vol) vs [[leverage-stress-tail-hedge]] which uses the OI HIGH gate (OI HIGH = buy puts). These are structurally complementary pages covering opposite ends of the same OI metric.

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
