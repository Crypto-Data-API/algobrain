---
title: "Combination Strategy Matrix"
type: index
created: 2026-07-18
updated: 2026-07-19
status: good
tags: [index, meta, methodology]
aliases: ["Combo Matrix", "Strategy Combination Matrix", "Primitive × Overlay Matrix"]
related: ["[[strategies-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[combinations-overview]]", "[[funding-rate-arbitrage]]", "[[trend-following-cta]]", "[[pairs-trading]]", "[[grid-trading]]", "[[mev-strategies]]", "[[delta-neutral-yield-farming]]", "[[skew-trading]]", "[[prediction-market-strategies]]", "[[stablecoin-depeg-profit-capture]]", "[[copy-trading]]", "[[etf-flow-directional]]", "[[crypto-beta-rotation]]", "[[options-rv-event-calendar]]", "[[alt-season-momentum-gate]]", "[[liquidation-depth-cascade-sizing]]"]
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

| Primitive \ Overlay | Regime gate | Funding filter | OI filter | Trend gate | Tail-hedge overlay | Vol targeting | Cross-venue | Unlock/event calendar | Sentiment-extreme filter | Session/time filter | Dominance/alt-season gate | Liquidity-depth gate | ETF-flow gate | Vol-term-structure gate | Social-velocity gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Funding carry** | [[regime-adaptive-strategy]] | — ¹ | [[oi-confirmed-trend]] ² | [[trend-aware-carry]] | [[carry-with-tail-hedge]] | [[vol-scaled-carry-sizing]] ⁵⁷ | [[hl-vs-cex-funding-divergence]] | [[event-calendar-risk-gating]] ²³ | [[crowded-long-funding-fade]] | [[funding-window-timing]] ¹⁷ | — ¹¹⁶ | — ¹¹⁷ | — ¹¹⁸ | planned ¹¹⁹ | — ¹²⁰ |
| **Basis / cash-and-carry** | [[regime-adaptive-strategy]] | [[funding-vs-basis-rotation]] ¹¹ | — ²⁴ | — ²⁵ | [[carry-with-tail-hedge]] | [[vol-scaled-carry-sizing]] ⁵⁷ | [[hl-vs-cex-funding-divergence]] | [[event-calendar-risk-gating]] ²³ | — ²⁶ | — ²⁷ | — ¹²¹ | — ¹²² | — ¹²³ | — ¹²⁴ | — ¹²⁵ |
| **Momentum / trend** | [[regime-adaptive-strategy]] | [[funding-filtered-momentum]] | [[oi-confirmed-trend]] | — ³ | [[trend-plus-tail-hedge]] | [[vol-targeted-trend-following]] | [[spot-led-momentum-filter]] | [[unlock-aware-momentum]] | [[contrarian-extremes]] ⁴ | [[session-aware-mean-reversion]] ¹² | [[alt-season-momentum-gate]] | planned ¹²⁶ | [[etf-flow-directional]] ¹²⁷ | planned ¹²⁸ | planned ¹²⁹ |
| **Mean-reversion** | [[regime-adaptive-strategy]] | [[funding-flush-reversal]] | [[oi-flush-reversion]] | [[pullback-trading]] ²² | [[put-protected-dip-buying]] ¹⁴ | [[vol-gated-mean-reversion]] ⁵⁸ | — ⁵⁹ | — ²⁸ | [[contrarian-extremes]] | [[session-aware-mean-reversion]] | — ¹³⁰ | planned ¹³¹ | — ¹³² | — ¹³³ | — ¹³⁴ |
| **Liquidation plays** | [[regime-adaptive-strategy]] | [[crowded-long-funding-fade]] | [[oi-confirmed-trend]] | — ²⁹ | [[cascade-monetization-rotation]] ¹³ | — ³⁰ | [[cross-venue-cascade-dislocation]] ¹⁸ | [[unlock-cascade-watch]] ³¹ | — ³² | [[off-hours-liquidation-playbook]] | — ¹³⁵ | [[liquidation-depth-cascade-sizing]] | — ¹³⁶ | — ¹³⁷ | — ¹³⁸ |
| **Narrative / event** | [[regime-adaptive-strategy]] | [[narrative-crowding-exit]] ³³ | [[oi-confirmed-trend]] | [[narrative-with-trend-confirmation]] | — ⁶⁰ | [[narrative-position-vol-targeting]] | — ³⁴ | [[unlock-short-with-crowding-gate]] | [[contrarian-extremes]] | — ³⁵ | planned ¹³⁹ | — ¹⁴⁰ | planned ¹⁴¹ | — ¹⁴² | planned ¹⁴³ |
| **Vol selling** | [[regime-adaptive-strategy]] | [[funding-conditioned-vol-selling]] | [[low-leverage-vol-selling]] ¹⁵ | [[trend-aligned-premium-selling]] | — ⁵ | [[volatility-targeting]] | — ³⁶ | [[event-calendar-risk-gating]] ²³ | [[post-panic-vol-selling]] | — ³⁷ | — ¹⁴⁴ | — ¹⁴⁵ | — ¹⁴⁶ | planned ¹⁴⁷ | — ¹⁴⁸ |
| **Vol buying / tail hedge** | [[regime-adaptive-strategy]] | — ³⁸ | [[leverage-stress-tail-hedge]] | [[long-options-trend-expression]] ¹⁹ | — ⁶ | — ³⁹ | — ⁴⁰ | [[event-vol-buying]] | [[complacency-vol-buying]] ⁴¹ | — ⁴² | — ¹⁴⁹ | — ¹⁵⁰ | — ¹⁵¹ | — ¹⁵² | — ¹⁵³ |
| **Grid / market-making** | [[regime-gated-grid]] | [[funding-skewed-grid]] | [[oi-aware-grid]] | — ⁷ | [[grid-with-tail-hedge]] ²⁰ | [[atr-scaled-grid]] ⁶¹ | — ⁴³ | [[event-calendar-risk-gating]] ²³ | — ⁴⁴ | [[session-overlap-momentum]] ⁸ | — ¹⁵⁴ | — ¹⁵⁵ | — ¹⁵⁶ | planned ¹⁵⁷ | — ¹⁵⁸ |
| **Stat-arb / pairs** | [[correlation-regime-pairs]] | [[pairs-with-funding-differential]] | [[oi-gated-pairs]] ⁶² | — ⁴⁵ | — ⁶³ | [[vol-balanced-pairs]] ⁴⁶ | [[hl-vs-cex-funding-divergence]] | [[unlock-pair-hedge]] | — ⁴⁷ | — ⁴⁸ | — ¹⁵⁹ | planned ¹⁶⁰ | — ¹⁶¹ | — ¹⁶² | — ¹⁶³ |
| **On-chain flow** | [[regime-adaptive-strategy]] | [[smart-money-vs-crowd-divergence]] ¹⁶ | [[oi-confirmed-trend]] | [[smart-money-orderflow-combo]] ⁹ | — ⁶⁴ | — ⁴⁹ | — ⁵⁰ | [[unlock-short-with-crowding-gate]] | [[onchain-capitulation-confluence]] | — ⁵¹ | — ¹⁶⁴ | — ¹⁶⁵ | planned ¹⁶⁶ | — ¹⁶⁷ | planned ¹⁶⁸ |
| **Sentiment** | [[regime-adaptive-strategy]] | [[sentiment-positioning-divergence]] ²¹ | — ⁵² | [[crypto-beta-rotation]] | — ⁶⁵ | — ⁵³ | — ⁵⁴ | — ⁵⁵ | — ¹⁰ | — ⁵⁶ | — ¹⁶⁹ | — ¹⁷⁰ | — ¹⁷¹ | — ¹⁷² | — ¹⁷³ |
| **MEV / execution** | — ⁶⁶ | — ⁶⁷ | — ⁶⁸ | — ⁶⁹ | — ⁷⁰ | — ⁷¹ | [[mev-strategies]] ⁷² | [[mev-strategies]] ⁷³ | — ⁷⁴ | [[mev-session-density]] | — ¹⁷⁴ | — ¹⁷⁵ | — ¹⁷⁶ | — ¹⁷⁷ | — ¹⁷⁸ |
| **DeFi yield / LP** | [[defi-yield-regime-gate]] | — ⁷⁵ | — ⁷⁶ | — ⁷⁷ | — ⁷⁸ | [[delta-neutral-yield-farming]] ⁷⁹ | [[concentrated-liquidity]] ⁸⁰ | [[defi-yield-event-calendar]] | [[defi-yield-sentiment-entry]] | — ⁸¹ | — ¹⁷⁹ | — ¹⁸⁰ | — ¹⁸¹ | planned ¹⁸² | — ¹⁸³ |
| **Options RV (skew & term structure)** | [[skew-trading]] ⁸² | [[options-rv-funding-filter]] | — ⁸³ | — ⁸⁴ | — ⁸⁵ | — ⁸⁶ | [[calendar-spread-arbitrage]] ⁸⁷ | [[options-rv-event-calendar]] | — ⁸⁸ | — ⁸⁹ | — ¹⁸⁴ | — ¹⁸⁵ | — ¹⁸⁶ | [[options-rv-event-calendar]] ¹⁸⁷ | — ¹⁸⁸ |
| **Prediction markets** | — ⁹⁰ | — ⁹¹ | — ⁹² | — ⁹³ | — ⁹⁴ | — ⁹⁵ | [[polymarket-prediction-market-arbitrage]] ⁹⁶ | [[prediction-market-strategies]] ⁹⁷ | [[prediction-market-strategies]] ⁹⁷ | — ⁹⁸ | — ¹⁸⁹ | — ¹⁹⁰ | — ¹⁹¹ | — ¹⁹² | — ¹⁹³ |
| **Stablecoin / peg** | — ⁹⁹ | — ¹⁰⁰ | — ¹⁰¹ | — ¹⁰² | — ¹⁰³ | — ¹⁰⁴ | [[stablecoin-pair-arbitrage]] ¹⁰⁵ | [[stablecoin-depeg-profit-capture]] ¹⁰⁶ | [[stablecoin-sentiment-depeg-entry]] | — ¹⁰⁷ | — ¹⁹⁴ | — ¹⁹⁵ | — ¹⁹⁶ | — ¹⁹⁷ | — ¹⁹⁸ |
| **Whale / copy-flow** | [[regime-adaptive-strategy]] | [[whale-copy-flow-funding-filter]] | — ¹⁰⁸ | [[smart-money-orderflow-combo]] ¹⁰⁹ | — ¹¹⁰ | — ¹¹¹ | [[on-chain-smart-money-tracking]] ¹¹² | [[copy-trading]] ¹¹³ | [[smart-money-vs-crowd-divergence]] ¹¹⁴ | — ¹¹⁵ | — ¹⁹⁹ | — ²⁰⁰ | — ²⁰¹ | — ²⁰² | — ²⁰³ |

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

**²³ [[event-calendar-risk-gating]]** covers three matrix cells: **funding carry × unlock/event calendar**, **grid/market-making × unlock/event calendar**, and **vol selling × unlock/event calendar**. All three involve mechanical/passive strategies that must be paused or de-sized around scheduled binary events (major unlocks, protocol upgrades, macro data releases, regulatory decisions). One unified framework page with per-strategy parameter guidance was created rather than three thin separate pages. The page also covers the basis/cash-and-carry × unlock/event cell (see footnote ²³ applied to that row) because the carry book unwind described for the funding carry row is identical in structure for basis/C&C books. Differentiated from [[event-vol-buying]] (TRADES the event — buys vol; this page AVOIDS the event — pauses passive strategies), [[regime-gated-grid]] (regime-based grid halt, lagging indicator; this page is calendar-based, forward-looking), and [[trend-aware-carry]] (trend-based carry reduction; this page is event-calendar-based halt).

**²⁴ Basis × OI filter = non-viable.** The basis/cash-and-carry trade is market-direction-neutral (long spot, short perp). An OI filter on a market-neutral structure does not produce a distinct overlay: high OI is already handled by the regime gate and the vol-targeting layer. Not additive.

**²⁵ Basis × trend gate = non-viable.** The basis/C&C trade is delta-neutral by construction. A trend gate on a direction-neutral trade introduces ambiguity: in a bull trend, funding is high (already captured by [[trend-aware-carry]]); the combination does not constitute a distinct strategy. [[trend-aware-carry]] substantively covers carry-in-trend.

**²⁶ Basis × sentiment-extreme filter = non-viable.** Basis/C&C is market-neutral carry; a sentiment-extreme filter would gate a neutral trade on a directional signal. The sentiment signal adds no independent information to the carry spread, which is already captured by the funding filter in [[funding-vs-basis-rotation]].

**²⁷ Basis × session/time filter = non-viable.** Basis/C&C convergence is a multi-day to multi-week trade; session-timing overlays do not add meaningful selectivity to a trade whose DTE spans multiple session cycles. Settlement timing for the perp leg is covered by [[funding-window-timing]] (funding carry row).

**²⁸ Mean-reversion × unlock/event = non-viable.** During an unlock event window, the correct action for a mean-reversion book is to pause it — which is a general risk-management instruction, not a named combination. The regime gate ([[regime-adaptive-strategy]]) and OI gate ([[oi-aware-grid]] logic) already handle the structural risk that unlocks create; a separate mean-reversion × unlock page would merely instruct: "check the event calendar before entering a mean-reversion trade."

**²⁹ Liquidation plays × trend gate = non-viable.** Cascade-fade entries are contrarian — they fade the direction of the liquidation move. A trend gate that restricts entries to the trend direction is the opposite of the strategy's logic: the cascade direction IS the trend during a cascade. Not a distinct overlay.

**³⁰ Liquidation plays × vol targeting = non-viable.** Cascade-fade positions are sized based on cascade severity (real-time liquidation volume, spread magnitude) — not by realized vol. The two sizing approaches conflict and vol targeting does not add a meaningful independent dimension to cascade-fade execution.

**³¹ [[unlock-cascade-watch]]** is placed in the liquidation plays × unlock/event calendar cell because the strategy specifically monitors the LIQUIDATION STRUCTURE (OI, funding, stop/liquidation clusters) around large scheduled token unlocks — staging cascade-fade limit orders and de-risking existing longs ahead of the risk window. The defining P&L mechanism is the cascade-fade (liquidation plays family); the unlock/event calendar is the organizing anchor. Differentiated from [[unlock-short-with-crowding-gate]] (directional short into the unlock; different action), [[unlock-pair-hedge]] (beta-neutral pair structure; different instrument), and [[unlock-aware-momentum]] (momentum book pause; different primitive).

**³² Liquidation plays × sentiment-extreme filter = non-viable.** Cascade-fade entries are triggered by real-time liquidation volume and OI/funding data — millisecond-scale signals. Sentiment indicators (Fear & Greed) are daily metrics too slow and too indirect for cascade-fade execution. The sentiment context is already embedded in the OI/funding cascade-confirmation gate.

**³³ [[narrative-crowding-exit]]** is placed in the narrative/event × funding filter cell because the strategy uses the funding rate (and OI) as the PRIMARY EXIT GATE for narrative-driven long positions: elevated funding + elevated OI = the narrative has become the crowded consensus trade, triggering exit or trim. The funding filter is the crowding-detection mechanism; the narrative long is the primitive. Differentiated from [[narrative-with-trend-confirmation]] (entry gate — this is the exit gate), [[crowded-long-funding-fade]] (enters a directional short — this exits a long), and [[contrarian-extremes]] (whole-market sentiment fade — this targets token-specific narrative crowding).

**³⁴ Narrative × cross-venue = non-viable.** Narratives drive directional price moves; cross-venue price arb is about execution, not narrative selection. No meaningful combination: narrative entries are unidirectional (long); cross-venue arb is directionally neutral.

**³⁵ Narrative × session/time filter = non-viable.** Narrative catalysts are event-driven, not session-dependent; they occur at announcement time regardless of session. Session filters add no selectivity to narrative entry timing.

**³⁶ Vol selling × cross-venue = non-viable.** The crypto short-vol instrument set is concentrated on Deribit; cross-venue diversification of short-vol positions is an operational consideration, not a distinct combination strategy generating independent edge.

**³⁷ Vol selling × session/time filter = non-viable.** Short-vol entries are gated by IV level (DVOL percentile, VRP), not session timing. No meaningful session-timing edge exists for options premium selling in a 24/7 market with globally continuous IV pricing.

**³⁸ Vol buying × funding filter = non-viable.** The funding signal is already incorporated as a gate component in [[leverage-stress-tail-hedge]] (Gate 2: 7d avg funding ≥ +0.04%/8h) and [[complacency-vol-buying]] (Gate 3: funding ≥ +0.030%/8h). A standalone vol buying × funding filter page would be redundant with these existing pages; both funding-gated vol-buying setups are already covered.

**³⁹ Vol buying × vol targeting = non-viable.** Vol targeting (scaling position by current realized vol level) applied to a long-vol position is circular: long-vol positions already have built-in vega scaling through the options Greeks. A separate vol-targeting overlay does not add an independent dimension; the IV-cheap gate in [[complacency-vol-buying]] and [[long-options-trend-expression]] already encodes the "buy more when IV is cheap" logic.

**⁴⁰ Vol buying × cross-venue = non-viable.** The crypto long-vol instrument set is concentrated on Deribit; cross-venue diversification of long-vol positions is an operational consideration without a distinct strategy-level combination.

**⁴¹ [[complacency-vol-buying]]** is placed in the vol buying/tail hedge × sentiment-extreme filter cell because the strategy purchases cheap vol (OTM puts or ATM straddles on Deribit) specifically when the three-factor COMPLACENCY gate passes: Fear & Greed ≥ 75 for ≥ 3 days (sentiment extreme — greed) AND DVOL ≤ 35th percentile (IV cheap) AND 7d avg funding ≥ +0.030%/8h or OI ≥ 70th pct (leverage building). The sentiment-extreme filter (greed extreme) is the primary trigger; the DVOL-cheap and leverage-building conditions are confirmation gates. Differentiated from [[leverage-stress-tail-hedge]] (OI-GATED trigger — objective stress metrics, not stated sentiment), [[event-vol-buying]] (calendar-driven, direction-agnostic; not sentiment-driven), and [[long-options-trend-expression]] (buys calls in confirmed uptrends; directionally bullish vs this page's crash-insurance framing).

**⁴² Vol buying × session/time filter = non-viable.** Long-vol positions (options accumulation) are not session-dependent; options are purchased based on IV level, trend/sentiment gates, and event calendars — none of which have meaningful session-timing structure in 24/7 crypto markets.

**⁴³ Grid × cross-venue = non-viable.** Cross-venue grids are a venue-arbitrage execution approach, not a named combination strategy; the structural cross-venue edge in liquidation and funding contexts is already documented in [[cross-venue-cascade-dislocation]] and [[hl-vs-cex-funding-divergence]].

**⁴⁴ Grid × sentiment-extreme filter = non-viable.** Sentiment extremes that would kill a grid are already detected by the regime gate (ADX, Bollinger-bandwidth in [[regime-gated-grid]]) or the OI gate ([[oi-aware-grid]]); a separate sentiment gate adds no independent information given these existing guards.

**⁴⁵ Stat-arb × trend gate = non-viable.** Applying a trend gate to market-neutral pairs trading converts the stat-arb strategy into a directional trade; the combination destroys the market-neutral property that is the primitive's core structural feature.

**⁴⁶ [[vol-balanced-pairs]]** is placed in the stat-arb/pairs × vol targeting cell because the strategy applies per-leg realized-vol scaling to a cointegrated spread so each leg contributes equal daily risk — eliminating the most common implementation flaw in crypto pairs where the high-vol leg (ETH in a BTC/ETH pair) dominates P&L, making the "pairs trade" effectively a directional bet on the high-vol leg. The vol-targeting overlay applies at the INTRA-SPREAD level (sizing the two legs relative to each other) rather than the portfolio level. Differentiated from [[correlation-regime-pairs]] (regime gate — pair eligibility, not leg sizing), [[pairs-with-funding-differential]] (carry-alignment filter — which leg to be on, not how much of each), and [[vol-targeted-trend-following]] (portfolio-level vol targeting on a directional position — different primitive and different application scope).

**⁴⁷ Stat-arb × sentiment-extreme filter = non-viable.** Sentiment as an overlay for stat-arb entries has no clear mechanism; spread mean-reversion is driven by the cointegrating relationship (structural anchor), not by overall market sentiment. Sentiment extremes correlate with high-vol regimes that break cointegration — already handled by [[correlation-regime-pairs]]'s regime gate.

**⁴⁸ Stat-arb × session/time filter = non-viable.** Pairs trading entries are z-score-driven; the half-life of the spread (3–25 days per [[vol-balanced-pairs]] and [[correlation-regime-pairs]]) spans multiple session cycles. Session filters add no meaningful selectivity to spread mean-reversion timing.

**⁴⁹ On-chain × vol targeting = non-viable.** Vol targeting on on-chain flow positions is a sizing rule; it is a parameter of the position, not a distinct combination strategy. The [[vol-targeted-trend-following]] framework already covers vol-scaled sizing for the trend component; applying vol targeting to on-chain positions is handled as part of standard portfolio risk management, not as a named combination.

**⁵⁰ On-chain × cross-venue = non-viable.** On-chain signals inherently observe all-venue flows (exchange inflows/outflows, whale movements across CEXs); there is no additional "cross-venue overlay" to apply on top of on-chain data — the on-chain signal already aggregates cross-venue behavior.

**⁵¹ On-chain × session/time filter = non-viable.** On-chain accumulation and flow signals are not session-dependent; whale activity occurs 24/7 independent of geographic session overlaps. Session filters add no meaningful timing selectivity to on-chain signals.

**⁵² Sentiment × OI filter = non-viable.** An OI filter on sentiment entries would duplicate [[sentiment-positioning-divergence]]'s funding/positioning gate (which already validates/invalidates the sentiment signal with derivative positioning data). A standalone sentiment × OI page would be a weaker, less differentiated version of the existing page.

**⁵³ Sentiment × vol targeting = non-viable.** Vol-targeting applied to a sentiment-contrarian position is a sizing rule, not a distinct combination; [[vol-targeted-trend-following]] and [[narrative-position-vol-targeting]] already cover vol-scaled sizing for the relevant primitives. Applying it to a sentiment strategy adds a sizing parameter, not a strategy-level edge.

**⁵⁴ Sentiment × cross-venue = non-viable.** Sentiment is a market-aggregate signal; cross-venue price differences are not meaningfully driven by sentiment signals; no distinct combination edge exists.

**⁵⁵ Sentiment × unlock/event calendar = non-viable.** Combining an unlock event with a sentiment confirmation (e.g., "only fade the unlock short if sentiment is also at a greed extreme") produces very rare signals and adds marginal selectivity already provided by the funding/OI crowding gate in [[unlock-short-with-crowding-gate]]. The combination is too thin to constitute a named strategy.

**⁵⁶ Sentiment × session/time filter = non-viable.** Sentiment (Fear & Greed) is a daily metric; session-timing filters add no meaningful granularity to sentiment-extreme entries, which are inherently multi-day setups.

**⁵⁷ [[vol-scaled-carry-sizing]]** covers TWO matrix cells: **funding carry × vol targeting** AND **basis / cash-and-carry × vol targeting**. One sizing framework governs both carry structures — size the carry book (either structure) to a constant daily-risk budget using the realized volatility of the carry P&L stream itself (not spot price vol). The carry P&L stream's vol is the correct denominator for carry sizing: it captures funding-rate noise, basis blowouts, and settlement timing effects that spot price vol misses. The critical correction to naive fixed-notional carry: the book is at maximum notional precisely when P&L volatility (and blowout risk) is highest. Vol-scaling forces the book smaller during the highest-risk carry regimes and larger when carry is quiet. Composable with [[carry-with-tail-hedge]] (tail hedge on the vol-scaled base), [[trend-aware-carry]] (trend throttle on top of vol-scaled notional), and [[event-calendar-risk-gating]] (event pause overrides vol-scaling).

**⁵⁸ [[vol-gated-mean-reversion]]** is placed in the mean-reversion × vol targeting cell. The fundamental tension — mean-reversion edge is empirically largest at moments of highest volatility (panics, funding flushes, OI flushes), yet naive vol targeting de-sizes most aggressively at those moments — requires a conditional treatment rather than a simple scaling rule. The page distinguishes HIGH-VOL-GOOD (flush/overshoot with mechanical reversion catalyst confirmed by funding < −0.015%/8h, OI −8%/24h, L/S ≤ 0.85 → size at 1.25×) from HIGH-VOL-BAD (cascade continuation with funding ≥ +0.010%/8h AND OI +10%/24h → size at 0.30×). The vol-regime gate is additive over the existing mean-reversion entry pages ([[funding-flush-reversal]], [[oi-flush-reversion]]) which define WHEN to enter; this page defines HOW MUCH to size those entries.

**⁵⁹ Mean-reversion × cross-venue = non-viable.** Mean-reversion in crypto perps is driven by funding flush, OI flush, or price overshoot mechanics — all single-venue structural signals. Cross-venue mean-reversion (venue premium/discount fade) is already covered by [[cross-exchange-arbitrage]] (continuous price arb between venues in normal conditions) and [[cross-venue-cascade-dislocation]] (cascade-driven dislocation between HL and Binance). A "mean-reversion × cross-venue" page combining both would describe venue-premium fade in non-cascade conditions, which is the standard cross-exchange-arb trade — substantively covered by the existing cross-exchange-arbitrage page. Not additive.

**⁶⁰ Narrative × tail-hedge overlay = non-viable.** Narrative/event positions are directional (long a narrative momentum), and tail protection on a directional position requires either (a) listed put options on the specific token (illiquid or unavailable for most narrative tokens — Deribit lists BTC and ETH, not altcoin memecoins), or (b) a proxy tail hedge on BTC/ETH (which is beta exposure, not a token-specific tail hedge — a narrative token can crash −70% while BTC is flat). The absence of liquid token-specific options markets for most narrative trades makes this combination non-buildable in practice. The closest viable alternative is [[put-protected-dip-buying]] (for the mean-reversion primitive where BTC/ETH options ARE available) and [[carry-with-tail-hedge]] (for delta-neutral carry books where the tail hedge targets the same asset). For narrative positions specifically, the risk management is done via position sizing ([[narrative-position-vol-targeting]]) and the crowding exit ([[narrative-crowding-exit]]), not via tail hedges.

**⁶¹ [[atr-scaled-grid]]** is placed in the grid / market-making × vol targeting cell. The ATR-scaled grid continuously adapts grid spacing to a fixed multiple of the current ATR(14, 4h), so spacing expands in high-vol (preventing fee-burning churn where too-tight spacing produces taker-only sweeps at a net loss) and contracts in low-vol (improving fill rate). Per-level notional adjusts inversely to vol to maintain a constant maximum inventory-accumulation risk per vol unit. Recalibrates every 4 hours when ATR changes ≥ 15%. This is additive over [[regime-gated-grid]] (binary on/off based on regime; this adapts geometry while running), [[oi-aware-grid]] (pause on OI build; this does not address breakout prevention), and [[funding-skewed-grid]] (inventory bias; this adjusts overall grid scale). All four are composable.

**⁶² [[oi-gated-pairs]]** is placed in the stat-arb/pairs × OI filter cell. The strategy refuses or exits spread entries when the short leg shows squeeze preconditions: 7d OI change ≥ +15% on the short leg AND/OR funding ≤ −0.015%/8h on the short leg (shorts crowded and paying) AND/OR L/S ≤ 0.80. The short-leg squeeze is the classic pairs killer — a mechanical forced-covering cascade that temporarily drives the overvalued leg higher regardless of the cointegration anchor, triggering the pairs stop before the structural reversion can occur. Mid-trade OI monitoring (4h polling) provides an early-warning exit before the 3.5σ stop fires. Composable with [[correlation-regime-pairs]] (pre-filter for eligible pairs), [[vol-balanced-pairs]] (leg sizing), and [[pairs-with-funding-differential]] (carry alignment); all four together constitute the highest-quality pairs entry framework in this wiki. Note: stat-arb × tail-hedge overlay (calls on the shorted leg as squeeze insurance) is a refinement documented in the oi-gated-pairs page rather than a separate combination — see footnote ⁶³.

**⁶³ Stat-arb / pairs × tail-hedge overlay = non-viable as a standalone page.** The concept — purchasing OTM calls on the short leg as insurance against a short squeeze — is real desk practice, but is documented as a refinement within [[oi-gated-pairs]] rather than a separate page, for two reasons: (a) the call premium cost on the short leg must be funded from somewhere — typically the spread's carry income via [[pairs-with-funding-differential]], creating no net new economic unit; (b) for most crypto pairs (all but BTC and ETH), listed options on the short leg are unavailable on Deribit, making this approach inaccessible for the majority of actionable pairs. The OI gate from [[oi-gated-pairs]] is a superior and universally available substitute that directly prevents the squeeze entry rather than hedging it after the fact.

**⁶⁴ On-chain flow × tail-hedge overlay = non-viable.** The combination premise — using on-chain stress metrics to time tail-hedge purchases — is substantively covered by [[leverage-stress-tail-hedge]], which already uses OI/market-cap (directly observable on-chain) and funding data as its primary stress gates. Adding on-chain whale-flow or exchange-flow metrics on top of the OI/funding gate in [[leverage-stress-tail-hedge]] would produce marginally earlier signals but would not constitute a structurally distinct combination. The overlap is too complete: [[leverage-stress-tail-hedge]]'s OI/market-cap ratio IS the canonical on-chain leverage stress metric; [[smart-money-vs-crowd-divergence]] and [[onchain-capitulation-confluence]] cover the on-chain flow signals in other contexts. A separate on-chain × tail-hedge page would be a thin variant of [[leverage-stress-tail-hedge]] with different input ordering.

**⁶⁵ Sentiment × tail-hedge overlay = non-viable.** Tail hedges on sentiment-contrarian positions require options on the assets being traded; sentiment strategies typically trade BTC/ETH (where options exist) or the whole market (where BTC/ETH options serve as a proxy). The combination collapses into either [[carry-with-tail-hedge]] (protecting a delta-neutral carry book with options) or [[complacency-vol-buying]] (buying options when sentiment is at a greed extreme). A "sentiment × tail-hedge overlay" page distinct from those two would describe: buy BTC/ETH calls as a hedge on a bearish sentiment fade trade — but sentiment fade entries are typically scaled by [[narrative-position-vol-targeting]]-type sizing, not by purchased options. Not a distinct combination.

**⁶⁶ MEV × regime gate = non-viable.** MEV (sandwiching, backrunning, JIT, liquidation MEV) is purely opportunistic and atomic — a MEV bot must evaluate each block opportunity on its own microstructure merits. Macro regime state (trending/ranging/vol-compressed) has no actionable relevance to the per-block extractable value computation. The "regime gate" concept applies to multi-day/week primitives that need protection from bad macro environments; MEV operates entirely within a single block with no carry-through risk.

**⁶⁷ MEV × funding filter = non-viable.** Funding rates are a multi-hour to multi-day signal; MEV execution windows are sub-second to one-block. The funding state when a sandwich or backrun opportunity appears is causally unrelated to whether that opportunity is profitable. No cross-contamination between the funding carry signal and per-block extraction value.

**⁶⁸ MEV × OI filter = non-viable.** Same reasoning as funding filter: OI is a multi-hour aggregate metric. Per-block MEV opportunities arise from pending transaction sequencing, not from aggregate OI levels.

**⁶⁹ MEV × trend gate = non-viable.** Trend is a multi-day/week signal; MEV extraction is per-block opportunistic. The trend direction does not determine whether a DEX arb, liquidation, or sandwich opportunity exists in the current block.

**⁷⁰ MEV × tail-hedge overlay = non-viable.** MEV positions are atomic (entered and exited within the same block); there is no residual inventory to hedge. Flash-loan-funded MEV paths have zero principal at risk across blocks. Non-atomic MEV that carries inventory (e.g., JIT LP position) is hedged via the LP delta management, not via a separate tail-hedge structure.

**⁷¹ MEV × vol targeting = non-viable.** Vol targeting scales position size by realized volatility to maintain constant daily-risk budget. MEV positions are either atomic (zero carry-through risk) or extremely short-lived scalps; there is no carry-through P&L stream with a vol to target. Size is determined by gas economics and available extractable value, not by a vol-scaling rule.

**⁷² [[mev-strategies]] covers MEV × cross-venue.** The existing MEV strategies page documents cross-venue arbitrage (DEX-to-DEX, DEX-to-CEX) as a core MEV strategy type. A new `planned` page for "MEV × cross-venue" would substantially overlap with mev-strategies and jito-solana-mev-arbitrage. Cell marked COVERED by existing page.

**⁷³ [[mev-strategies]] covers MEV × unlock/event calendar.** Event-driven MEV — including large unlock events that create predictable liquidation cascades and DEX rebalances — is documented within mev-strategies as the "event-driven MEV" sub-category. The event calendar shapes which MEV opportunities appear; this is inherent to MEV strategy design, not a separable overlay requiring a new page.

**⁷⁴ MEV × sentiment-extreme filter = non-viable.** Sentiment extremes (Fear & Greed) are daily metrics with no actionable relationship to per-block MEV extraction opportunities. No mechanism connects daily sentiment readings to the probability of MEV being profitable in the next block.

**⁷⁵ DeFi yield / LP × funding filter = non-viable.** The most natural interpretation — gate LP deployment on funding levels — is non-viable because LP yield (fee income) is determined by trading volume and pool composition, not by perp funding rates. The cross-contamination between funding state and DEX fee income is weak and not a named strategy. The closest genuine combination is [[delta-neutral-yield-farming]] (which already hedges the delta using perps, implicitly incorporating funding as a cost factor) — a separate "LP × funding filter" page would be a thin variant of that page's hedging discussion.

**⁷⁶ DeFi yield / LP × OI filter = non-viable.** OI (open interest in perp markets) has no direct structural relationship to LP profitability. High OI creates cascade risk that can drain LP positions via LVR, but this is already handled by the regime gate ([[defi-yield-regime-gate]]). A standalone OI filter for LP deployment adds no independent edge beyond the regime gate's vol-and-cascade detection.

**⁷⁷ DeFi yield / LP × trend gate = non-viable.** LP positions are market-neutral (both sides of the pool); applying a directional trend gate to a market-neutral LP deployment creates ambiguity. The concentrated-liquidity strategy ([[concentrated-liquidity]]) adjusts range placement based on trend, which is the nearest viable analog — but that is an execution detail of the LP primitive, not a separable overlay. [[defi-yield-regime-gate]] covers the regime-conditional LP deployment framing.

**⁷⁸ DeFi yield / LP × tail-hedge overlay = non-viable.** LP impermanent loss is equivalent to being short gamma (short a straddle on the pool's assets). Purchasing options to hedge this short-gamma exposure is real desk practice, but the cost of that hedge typically exceeds the fee income except in the highest-fee tiers with lowest volatility. The hedged-LP strategy is substantively covered within [[delta-neutral-yield-farming]] (delta-neutral via perp short) and [[concentrated-liquidity]] (range management to reduce IL exposure). A pure "LP + put overlay" page would document an expensive and rare positive-EV setup without distinct mechanism.

**⁷⁹ [[delta-neutral-yield-farming]] covers DeFi yield / LP × vol targeting.** Vol targeting on an LP position is the practice of adjusting the LP range width (concentrated liquidity) or total deployed notional based on current realized volatility. This is a core technique documented in [[delta-neutral-yield-farming]] (which adjusts the perp hedge ratio as vol changes) and [[concentrated-liquidity]] (which discusses range width vs vol). No new standalone page needed.

**⁸⁰ [[concentrated-liquidity]] covers DeFi yield / LP × cross-venue.** Cross-venue LP deployment — deploying across multiple AMMs (Uniswap, Curve, Balancer) to diversify fee income and pool composition risk — is documented within [[concentrated-liquidity]] as a multi-venue LP management topic. The structural cross-venue considerations (which pool, which fee tier, which chain) are inherent to the LP strategy design.

**⁸¹ DeFi yield / LP × session/time filter = non-viable.** LP fee income accrues continuously (24/7 DeFi markets); session filters do not apply to a passive yield-accrual position. Concentration range rebalancing is triggered by price movement and vol, not by session timing.

**⁸² [[skew-trading]] implicitly incorporates a regime gate.** The skew-trading page conditions entries on dislocation of the 25-delta risk reversal from its historical mean — which is equivalent to a regime gate: only trade when the skew is meaningfully dislocated. A separate "Options RV × regime gate" page would be redundant with the existing skew-trading entry conditions. Cell marked COVERED by existing page.

**⁸³ Options RV × OI filter = non-viable.** Options relative value (skew and term structure) is priced on the Deribit options surface; OI in perp markets is not a direct driver of options surface dislocation. The relevant "OI" for options RV is options OI by strike/expiry — which is inherent to the skew-trading and calendar-spread entry conditions, not a separate overlay.

**⁸⁴ Options RV × trend gate = non-viable.** Options RV trades (skew, term structure) are structured to be directionally neutral (delta-hedged). A trend gate on a delta-neutral structure introduces directional bias that conflicts with the market-neutral structure of the trade. The nearest analog — selecting which wing to sell based on trend — is covered by [[trend-aligned-premium-selling]] (which is a vol-selling strategy, not an RV strategy).

**⁸⁵ Options RV × tail-hedge overlay = non-viable.** Options RV positions are already structured as multi-leg spreads (risk reversals, calendar spreads, dispersion trades) that inherently limit max loss via their spread construction. Adding a further tail-hedge overlay on an already-hedged options spread would reduce net vega/theta to near zero, destroying the strategy's P&L source.

**⁸⁶ Options RV × vol targeting = non-viable.** Options RV positions are sized primarily by vega and theta budgets, not by a portfolio-level realized-vol scaling rule. Vol targeting on an options book uses the options Greeks for sizing — which is inherent to options portfolio management, not a separate named combination overlay. [[narrative-position-vol-targeting]] and [[vol-targeted-trend-following]] apply vol targeting to directional positions, not to options spread books.

**⁸⁷ [[calendar-spread-arbitrage]] covers Options RV × cross-venue.** Cross-venue options RV — trading term-structure dislocations between Deribit and CME, or between BTC and ETH term structures — is documented within [[calendar-spread-arbitrage]] as a multi-venue/multi-expiry spread trade. A new "Options RV × cross-venue" page would be a thin variant of calendar-spread-arbitrage's cross-venue section.

**⁸⁸ Options RV × sentiment-extreme filter = non-viable.** Options RV trades (skew, term structure) are triggered by statistical dislocation of the vol surface from its fair value — not by directional sentiment extremes. Sentiment extremes do create vol surface dislocations (panic → rich puts; euphoria → rich calls), but this is already embedded in the skew-trading entry conditions (RR25 dislocation from mean).

**⁸⁹ Options RV × session/time filter = non-viable.** Options RV dislocations are structural and persist for days to weeks (skew persistence, term-structure premium convergence cycles). Session filters do not add meaningful selectivity to positions with multi-day DTE and slow-moving surface dynamics.

**⁹⁰ Prediction markets × regime gate = non-viable.** Prediction market prices are event-probability estimates anchored to a real-world outcome (election result, regulatory decision, price threshold). The macro/vol regime does not determine whether a Polymarket market is mispriced relative to true event probability. The regime affects the perp/spot leg in [[polymarket-as-crypto-leading-indicator]] (which uses prediction markets as a signal, not as the trading venue), but the prediction market itself is not gated by regime state.

**⁹¹ Prediction markets × funding filter = non-viable.** Prediction market odds on Polymarket are denominated in USDC and settle against binary event outcomes, not perp funding rates. Funding rates are not a relevant filter for prediction market entry; there is no mechanism connecting funding state to Polymarket mispricing.

**⁹² Prediction markets × OI filter = non-viable.** Open interest in perp markets has no causal relationship to whether a prediction market is mispriced. These are structurally unrelated instruments.

**⁹³ Prediction markets × trend gate = non-viable.** Prediction market entries are triggered by probability mispricings relative to the true likelihood of binary events. Perp/spot trend state has no mechanism for improving prediction market entry timing; the tail-asset trend does not determine whether the event probability is correctly priced on Polymarket.

**⁹⁴ Prediction markets × tail-hedge overlay = non-viable.** Prediction market positions already have bounded payoffs ($0 or $1 per share); the maximum loss is the capital deployed. There is no tail exposure beyond the position size; options-based tail hedges on prediction market positions would be redundant with the inherent loss limit and are not available as instruments on Polymarket/Kalshi.

**⁹⁵ Prediction markets × vol targeting = non-viable.** Vol targeting as a sizing overlay requires a continuous P&L stream with a measurable realized volatility. Prediction market positions accrue no continuous P&L (they sit at a price and settle binary); applying vol targeting to them would mean sizing each new position by historical Sharpe on prior resolved markets — which is standard position sizing, not a named combination strategy.

**⁹⁶ [[polymarket-prediction-market-arbitrage]] covers Prediction markets × cross-venue.** Cross-venue prediction market arbitrage (Polymarket vs Kalshi vs PredictIt, YES/NO complement arb, cross-market triangulation) is the primary content of the existing page. Cell marked COVERED by existing page.

**⁹⁷ [[prediction-market-strategies]] covers Prediction markets × unlock/event calendar AND sentiment-extreme filter.** The existing page documents event-calendar anchoring of prediction market trades (entering into scheduled binary catalysts) and behavioral bias fading (favorite-longshot bias, recency extremes). Both overlays are inherent to prediction market strategy design and are covered by the existing page. Two cells marked COVERED.

**⁹⁸ Prediction markets × session/time filter = non-viable.** Prediction markets on Polymarket operate continuously; event-driven binary outcomes do not have session-timing structure. Entry timing is driven by odds movement and information, not by geographic session overlaps.

**⁹⁹ Stablecoin / peg × regime gate = non-viable.** Stablecoin depeg arbitrage (buy below peg, sell at peg restoration) is mechanically uncorrelated with macro regime state. A depeg event creates its own local micro-regime regardless of whether the overall crypto market is trending, ranging, or crashing. The [[stablecoin-depeg-profit-capture]] page already conditions entries on redemption channel status and pool composition — the functional equivalent of a regime gate for this specific primitive.

**¹⁰⁰ Stablecoin / peg × funding filter = non-viable.** Perp funding rates are a signal for the leveraged crowd's directional positioning in BTC/ETH. This has no direct causal link to whether a stablecoin is trading at a peg discount or premium. The stablecoin peg mechanic is driven by redemption channel status, pool imbalance, and collateral risk — not by perpetual market funding.

**¹⁰¹ Stablecoin / peg × OI filter = non-viable.** Same reasoning as funding filter: perp OI aggregates directional leverage in BTC/ETH, which is not a meaningful driver of stablecoin peg distance. Stablecoin depeg risk is driven by collateral quality, redemption mechanism, and pool composition.

**¹⁰² Stablecoin / peg × trend gate = non-viable.** Stablecoin depeg opportunities are mean-reverting mechanical trades (buy below $1, profit when peg restores). A trend gate would attempt to condition the entry on a directional trend in stablecoin price — but stablecoins do not trend; they deviate briefly and revert. A "downtrend confirmed" gate on a $0.95 stablecoin would prevent entry at exactly the time the opportunity is largest.

**¹⁰³ Stablecoin / peg × tail-hedge overlay = non-viable.** The largest tail risk in stablecoin depeg trades is not a directional price move but a "zero-recovery" failure (full depegging, algorithmic death spiral, frozen redemptions). Options-based tail hedges against complete stablecoin failure are either unavailable (no liquid puts on USDC, USDT) or extremely expensive. The correct risk management is position sizing (concentration limits, tiered capital deployment) and redemption channel monitoring — both documented in [[stablecoin-depeg-profit-capture]].

**¹⁰⁴ Stablecoin / peg × vol targeting = non-viable.** Vol targeting applies a realized-vol scaling rule to a position's size. Stablecoin depeg trades are sized by the discount magnitude (buy at $0.95, target $1.00) and capital concentration limits — not by a realized-vol budget. The vol of a stablecoin position is not the right denominator for sizing a mean-reversion-to-peg trade.

**¹⁰⁵ [[stablecoin-pair-arbitrage]] covers Stablecoin / peg × cross-venue.** Trading stablecoin cross-venue price dislocations (USDC at $0.998 on one exchange, $1.001 on another) is the primary content of the stablecoin-pair-arbitrage page. Cell marked COVERED by existing page.

**¹⁰⁶ [[stablecoin-depeg-profit-capture]] covers Stablecoin / peg × unlock/event calendar.** Large scheduled events (protocol upgrades, reserve audits, regulatory announcements) that can trigger depeg events are discussed in the depeg-profit-capture page as context for pre-positioning redemption arb capacity. The event calendar is an inherent input to stablecoin depeg monitoring.

**¹⁰⁷ Stablecoin / peg × session/time filter = non-viable.** Stablecoin depeg events occur at any time (often triggered by protocol events, exchange runs, or market panic) independent of geographic session. Session timing adds no meaningful selectivity to depeg entry triggers.

**¹⁰⁸ Whale / copy-flow × OI filter = non-viable.** OI is a market-aggregate metric for the overall leveraged crowd. Whale/copy-flow strategies track specific large-wallet behavior. The combination — "copy whales only when aggregate OI is low" — produces signals that are too rare to be actionable (whale accumulation events with low OI are uncommon) and the OI condition adds no independent information to the whale signal itself. The relevant OI check is already a component of [[smart-money-vs-crowd-divergence]] (funding + L/S gate, which is equivalent to an OI-momentum check).

**¹⁰⁹ [[smart-money-orderflow-combo]] covers Whale / copy-flow × trend gate.** That page combines on-chain smart-money signals with real-time order-flow (trend) confirmation — which is structurally a whale-flow primitive gated by a short-term trend/order-flow overlay. Cell marked COVERED by existing page.

**¹¹⁰ Whale / copy-flow × tail-hedge overlay = non-viable.** Copy-flow positions (following whale trades) are directional perp/spot entries. Tail protection on these positions requires BTC/ETH options (available on Deribit) but the overlay does not add a distinct named combination; it is a position-sizing add-on already covered by general portfolio risk management frameworks ([[carry-with-tail-hedge]], [[put-protected-dip-buying]]) applied to the directional entry. Not a structurally new combination.

**¹¹¹ Whale / copy-flow × vol targeting = non-viable.** Vol targeting on whale-copy positions is a sizing rule (scale down the position when BTC/ETH realized vol is high). This is a standard risk management technique documented in [[vol-targeted-trend-following]] and applicable to any directional position. It does not constitute a distinct strategy-level combination for the whale/copy-flow primitive.

**¹¹² [[on-chain-smart-money-tracking]] covers Whale / copy-flow × cross-venue.** Cross-venue whale tracking (observing wallet flows across Binance, Coinbase, Hyperliquid, DeFi) is documented within on-chain-smart-money-tracking as a core technique. The cross-venue dimension is inherent to on-chain wallet monitoring rather than a separable overlay. Cell marked COVERED by existing page.

**¹¹³ [[copy-trading]] partially covers Whale / copy-flow × unlock/event calendar.** The copy-trading page discusses timing context including major events that affect signal quality. However, the event calendar as a gate — "copy whales only outside major unlock/event windows when their signals are cleanest" — is a meaningful refinement. This cell is marked COVERED (existing page) with note that a planned page could refine further; the existing page's coverage is sufficient to avoid duplication for Campaign 2.

**¹¹⁴ [[smart-money-vs-crowd-divergence]] covers Whale / copy-flow × sentiment-extreme filter.** That combination page (on-chain accumulation + bearish derivative crowd positioning) is structurally a whale-flow primitive gated by a sentiment/positioning extreme overlay. Cell marked COVERED by existing page.

**¹¹⁵ Whale / copy-flow × session/time filter = non-viable.** Whale on-chain activity occurs 24/7 independent of geographic session overlaps. Whale accumulation events are not session-timed; applying a session filter to copy-flow entries would eliminate many high-quality signals that happen to fire during off-hours sessions without any corresponding improvement in signal quality.

---

### Campaign 2 — Column Expansion Footnotes (¹¹⁶–²⁰³)

**¹¹⁶ Funding carry × dominance/alt-season gate = non-viable.** The funding carry trade is delta-neutral (short perp, long spot or funding harvest); BTC dominance is a portfolio-level allocation signal for the intra-crypto BTC vs alt split. The carry book is not directionally long or short alts, so the dominance regime does not selectively improve or harm carry outcomes. The regime gate ([[regime-adaptive-strategy]]) already captures the macro regime conditions that correlate with dominance; adding a separate dominance gate is redundant.

**¹¹⁷ Funding carry × liquidity-depth gate = non-viable.** Carry book sizing by order-book depth at entry is a standard execution parameter, not a strategy-level overlay. The carry trade is sized by the carry P&L volatility (per [[vol-scaled-carry-sizing]]), not by real-time book depth. Depth is a constraint on execution, not a signal for whether to run carry.

**¹¹⁸ Funding carry × ETF-flow gate = non-viable.** ETF flows are a directional demand signal (positive flow = institutional buying); the funding carry trade is direction-agnostic (harvests the funding rate regardless of whether price rises or falls). Conditioning a neutral carry harvest on a directional flow gate introduces directional bias into a market-neutral strategy without a clear mechanism for improving carry outcomes.

**¹¹⁹ Funding carry × vol-term-structure gate = planned.** When the vol term structure is in steep backwardation (near-dated IV significantly above back-dated IV), the market is pricing an imminent vol spike. This is forward-looking event risk that neither the event calendar ([[event-calendar-risk-gating]]) nor the trend gate ([[trend-aware-carry]]) fully captures — the vol surface is the market's real-time aggregation of all forward risk. Reducing carry book size when TS is in steep backwardation provides a market-priced early-warning layer on top of the calendar-based and trend-based carry reduction rules.

**¹²⁰ Funding carry × social-velocity gate = non-viable.** Social attention velocity (rate of change of social mentions) is a narrative/retail sentiment signal with no clear mechanism for predicting carry rate behaviour. Perp funding rates are set by derivative market supply and demand, not by social attention velocity.

**¹²¹ Basis / cash-and-carry × dominance/alt-season gate = non-viable.** Basis / C&C is market-neutral (long spot, short dated futures); the dominance regime signal is about intra-crypto capital flows between BTC and alts. A neutral basis trade is not affected by the BTC vs alt allocation dynamic.

**¹²² Basis / cash-and-carry × liquidity-depth gate = non-viable.** Basis / C&C entries are multi-week trades sized by carry spread magnitude, not by real-time book depth. Depth at entry is a standard execution consideration, not a strategy-level overlay.

**¹²³ Basis / cash-and-carry × ETF-flow gate = non-viable.** See footnote ¹¹⁸. Same reasoning applies: delta-neutral basis harvest is not improved by a directional ETF flow gate.

**¹²⁴ Basis / cash-and-carry × vol-term-structure gate = non-viable.** The basis/C&C trade involves the FUTURES term structure (basis = dated future premium over spot). The vol-term-structure gate references the OPTIONS implied vol term structure — a different instrument on the same underlying. While options vol TS can signal event risk that affects carry, this is already captured by [[event-calendar-risk-gating]]; adding a separate options vol TS gate on top of the calendar gate would be largely redundant for a multi-week basis trade. The overlap with [[options-rv-event-calendar]] is complete: when [[options-rv-event-calendar]] signals near-dated IV richness, the same event should already be on the [[event-calendar-risk-gating]] calendar. Not a distinct viable combination.

**¹²⁵ Basis / cash-and-carry × social-velocity gate = non-viable.** Same reasoning as footnote ¹²⁰. Social attention velocity has no direct mechanism for predicting futures basis dynamics.

**¹²⁶ Momentum / trend × liquidity-depth gate = planned.** Momentum entries gated or sized by order-book depth at the breakout price: entries only when depth above the breakout is sufficient to suggest that the momentum is supply-driven rather than thin-book noise. Distinct from [[spot-led-momentum-filter]] (which gates on Coinbase premium / spot-vs-OI origin of the move, not on bid/ask depth level) and from [[oi-confirmed-trend]] (which gates on OI direction). The depth gate checks whether the market structure at the entry price can support the momentum entry without creating excessive adverse price impact.

**¹²⁷ [[etf-flow-directional]] covers momentum / trend × ETF-flow gate.** That strategy IS the ETF flow as a momentum/directional signal — it goes long when the ETF net-flow z-score is positive and rising, short when it turns negative. The ETF flow is both the signal and the gate for the directional position. A separate "momentum × ETF-flow gate" page would be a thin variant of etf-flow-directional. Cell marked COVERED by existing page.

**¹²⁸ Momentum / trend × vol-term-structure gate = planned.** Momentum entries restricted when the vol term structure is in steep backwardation (near-dated IV significantly above back-dated IV): the market is pricing an imminent directional event that could override or reverse the current momentum signal. This is more forward-looking than the trend gate (which uses lagging indicators) and complementary to [[unlock-aware-momentum]] (which uses specific event dates). The vol TS gate uses the market's aggregate forward-risk pricing to avoid momentum entries ahead of unknown or unscheduled events not captured by the named event calendar.

**¹²⁹ Momentum / trend × social-velocity gate = planned.** Momentum entries gated or confirmed by accelerating social attention (rate-of-change of mentions, not level). Requires BOTH price momentum AND social velocity acceleration to be active simultaneously: the social velocity component identifies the inflection in retail attention that precedes the momentum continuation phase. Distinct from [[contrarian-extremes]] (which uses sentiment LEVEL to fade momentum at extremes) and [[narrative-with-trend-confirmation]] (which gates on price trend, not social velocity).

**¹³⁰ Mean-reversion × dominance/alt-season gate = non-viable.** Mean-reversion is a single-asset strategy (price overshoot fades back to fair value); the dominance/alt-season signal is a portfolio-level allocation between BTC and alts. The dominance regime does not predict which individual assets are most overshot on a given day; applying it to mean-reversion entry selection adds no independent signal.

**¹³¹ Mean-reversion × liquidity-depth gate = planned.** At illiquid panic lows (thin book), price can overshoot its fundamental support level because even small selling exhausts the order book; when depth begins recovering (buyers re-posting bids), the MR entry has structural support. Distinct from [[funding-flush-reversal]] (funding-based signal) and [[oi-flush-reversion]] (OI-based signal): those gates identify when the leveraged crowd has been flushed; the depth gate confirms that passive market liquidity is returning to support the recovery.

**¹³² Mean-reversion × ETF-flow gate = non-viable.** ETF flows are directional (sustained inflow = bull demand); gating mean-reversion entries on ETF flow direction would turn a contrarian strategy into a trend-following one (only MR on the long side when ETF flows are positive). This conflicts with MR's core logic: the best reversion entries often occur when ETF flows are negative (maximum fear, maximum discount from fair value) — exactly when an ETF-flow gate would prohibit entry.

**¹³³ Mean-reversion × vol-term-structure gate = non-viable.** Mean-reversion edge is strongest in high-vol environments (flush events, overshoots). Blocking MR entries when vol TS is in backwardation (high near-dated IV = high vol event likely) would prevent the highest-quality MR entries. The vol TS gate is directionally opposed to the MR strategy's optimal deployment conditions.

**¹³⁴ Mean-reversion × social-velocity gate = non-viable.** Social velocity is too slow for mean-reversion timescales (MR is intraday to 1–3 days; social attention momentum is measured over days to weeks). The two signals operate on incompatible timescales; applying a social velocity gate to a 4-hour MR trade adds noise without signal.

**¹³⁵ Liquidation plays × dominance/alt-season gate = non-viable.** Cascade events are triggered by mechanical liquidation thresholds (price levels, funding rates, OI build) that are independent of the BTC dominance regime. A cascade can occur in alt-season or BTC-dominance regimes; the cascade-fade primitive does not have a dominance-regime dependency.

**¹³⁶ Liquidation plays × ETF-flow gate = non-viable.** Cascade events (real-time, minutes-to-hours) are orthogonal to multi-day ETF flow regime states. The funding and OI confirmation already embedded in cascade-fade triggers are more timely and more directly relevant than the ETF flow state, which is a daily signal.

**¹³⁷ Liquidation plays × vol-term-structure gate = non-viable.** Cascade events are triggered and managed in real time (1-hour to 4-hour windows); the vol term structure is a daily options market signal with multi-day persistence. There is no mechanism for the vol TS shape to predict whether a specific cascade will be revertible; the depth gate ([[liquidation-depth-cascade-sizing]]) and the regime gate ([[regime-adaptive-strategy]]) are the correct cascade-quality filters.

**¹³⁸ Liquidation plays × social-velocity gate = non-viable.** Cascades are executed on sub-hour timescales; social attention velocity is measured over days. No actionable relationship between social mention acceleration and cascade fade entry quality.

**¹³⁹ Narrative / event × dominance/alt-season gate = planned.** Narrative/event trades on altcoins concentrate almost entirely during alt-season (falling BTC dominance) periods; deploying narrative longs into rising-dominance environments typically results in the narrative playing out but the token losing ground to BTC (alt-season-absent narrative). The dominance gate selectively deploys narrative trades when the structural tailwind (alt-season) is aligned with the narrative catalyst.

**¹⁴⁰ Narrative / event × liquidity-depth gate = non-viable.** Narrative trades are directional (long a narrative momentum); order-book depth at entry is a standard execution consideration for sizing, not a strategy-level overlay that changes the narrative thesis. Depth is already implicitly managed via position sizing ([[narrative-position-vol-targeting]]) and entry timing ([[narrative-with-trend-confirmation]]). Not a named combination.

**¹⁴¹ Narrative / event × ETF-flow gate = planned.** Narrative entries confirmed by ETF flow alignment — when a bullish crypto narrative (e.g., "institutional accumulation season") coincides with positive and rising ETF net flow, the institutional and narrative signals are mutually reinforcing. The ETF flow provides the macro-institutional confirmation that the narrative has genuine capital backing beyond retail sentiment. Distinct from [[narrative-with-trend-confirmation]] (price trend gate) and [[etf-flow-directional]] (ETF flow as standalone directional signal without narrative context).

**¹⁴² Narrative / event × vol-term-structure gate = non-viable.** The combination — deploy narrative only when vol TS is NOT in steep backwardation — is partially covered by [[event-calendar-risk-gating]] (pauses narrative entries around known events) and [[options-rv-event-calendar]] (trades the vol TS dimension of events). A separate "narrative × vol TS gate" page would be a thin variant of the event-calendar gating logic applied to narrative entries, without adding a distinct mechanism.

**¹⁴³ Narrative / event × social-velocity gate = planned.** The rate of change of social mentions (social velocity) is the most direct signal that a narrative is gaining retail traction and approaching the momentum phase. Entry when BOTH the narrative has a real catalyst AND social velocity is accelerating (not just at a high level) identifies the early acceleration phase of the retail attention cycle — before the crowd reaches the exit of [[narrative-crowding-exit]]. This is the complement of [[contrarian-extremes]] (which trades extremes of sentiment level, not velocity).

**¹⁴⁴ Vol selling × dominance/alt-season gate = non-viable.** Vol selling on Deribit is limited to BTC and ETH options; the dominance regime (BTC vs alt market share) does not directly affect BTC/ETH implied vol dynamics. DVOL and the VRP are driven by global crypto market vol and institutional option demand, not by the BTC dominance percentage.

**¹⁴⁵ Vol selling × liquidity-depth gate = non-viable.** Vol selling (short Deribit options) is gated by DVOL percentile, VRP, and funding conditions — not by underlying perp market order-book depth. Options market liquidity on Deribit is a separate consideration from CEX perp book depth; a "sell vol only when BTC perp book is deep" gate has no clear mechanism for improving vol-selling outcomes.

**¹⁴⁶ Vol selling × ETF-flow gate = non-viable.** Short-vol entries are gated by IV/RV premium (DVOL vs realized vol spread) and crowd positioning (funding) — not by directional institutional flow. ETF inflows may correlate with elevated IV (institutional hedging demand), but this relationship is already captured by the funding and DVOL gates. Adding an ETF-flow gate to vol selling creates directional bias (only sell vol when institutional is buying) that conflicts with the vol-selling primitive's direction-neutral structure.

**¹⁴⁷ Vol selling × vol-term-structure gate = planned.** Sell vol only when the term structure is in contango (back-dated IV ≥ near-dated IV): the carry from near-to-far convergence accrues to the short-vol position, AND the near-dated IV is not already pricing imminent event risk. When the term structure is in backwardation (near > far), selling near-dated options means selling into event premium that is likely to spike further before reverting — the worst timing for a short-vol entry. This is complementary to [[event-calendar-risk-gating]] (calendar-based halt) and provides the MARKET-PRICED early warning layer (the vol surface aggregates all known and anticipated risks into the TS shape).

**¹⁴⁸ Vol selling × social-velocity gate = non-viable.** Implied vol is set by options market participants (institutional hedgers, vol-arb desks); social attention velocity is a retail signal that does not directly drive Deribit DVOL. No clear mechanism for social velocity to improve vol-selling entry timing beyond what DVOL/VRP/funding already capture.

**¹⁴⁹ Vol buying / tail hedge × dominance/alt-season gate = non-viable.** Tail hedges (long options on Deribit) are purchased on BTC or ETH; the BTC dominance regime does not independently predict the probability of a tail event. Tail events can occur in any dominance regime; the stress gates in [[leverage-stress-tail-hedge]] and [[complacency-vol-buying]] already incorporate the relevant market structure signals.

**¹⁵⁰ Vol buying / tail hedge × liquidity-depth gate = non-viable.** Options purchases on Deribit are not conditioned on underlying perp market order-book depth; the purchase is based on IV level and stress conditions. Depth in the perp market is not a meaningful gate for options accumulation timing.

**¹⁵¹ Vol buying / tail hedge × ETF-flow gate = non-viable.** Tail hedge accumulation (buying puts/straddles) is triggered by stress conditions (elevated OI/funding per [[leverage-stress-tail-hedge]], greed extremes per [[complacency-vol-buying]]), not by ETF flow direction. ETF inflows indicate institutional buying — the opposite of the tail-risk environment when tail hedges are most needed.

**¹⁵² Vol buying / tail hedge × vol-term-structure gate = non-viable.** When the vol term structure is in steep backwardation (near > far IV), the market is already pricing the event risk that vol buying targets. Buying tail hedges at this point (high near-dated IV, event premium already built in) means purchasing expensive insurance at precisely the wrong time — the event premium makes the put purchase unattractive. [[options-rv-event-calendar]] trades this surface dynamic from the RV side (sell near, buy far); a vol buying × vol TS page would describe buying at peak event premium — the structural opposite of that page's thesis. The [[event-vol-buying]] page already covers the pre-event straddle buy (before the premium builds), and [[complacency-vol-buying]] covers buying vol when IV is cheap. Not a viable standalone combination.

**¹⁵³ Vol buying / tail hedge × social-velocity gate = non-viable.** Social velocity is a retail narrative signal; tail hedge accumulation is a structural stress response (OI, funding, leverage). These operate in completely different signal spaces.

**¹⁵⁴ Grid / market-making × dominance/alt-season gate = non-viable.** Grids operate on single assets (typically BTC perp); the dominance regime is a portfolio-level allocation signal. A grid's profitability is determined by the vol/range relationship of the underlying asset, not by whether BTC is gaining or losing market share to alts.

**¹⁵⁵ Grid / market-making × liquidity-depth gate = non-viable.** Grid profitability depends on the spread and depth of the underlying market — an operator would not run a grid in a thin-book market. However, this is a deployment prerequisite, not a named combination strategy: checking that the market is deep enough to run a grid efficiently is standard due diligence, already incorporated into [[regime-gated-grid]]'s deployment conditions. Not a named overlay that generates additional edge.

**¹⁵⁶ Grid / market-making × ETF-flow gate = non-viable.** Grids are range-bound strategies; ETF flows create directional bias that produces the trending regimes that break grids. The regime gate ([[regime-gated-grid]]) already handles the trend-detection logic that ETF flows are a component of. A separate ETF-flow gate on a grid would at best replicate a component of [[regime-gated-grid]]'s signal.

**¹⁵⁷ Grid / market-making × vol-term-structure gate = planned.** Pause the grid when the vol term structure shifts into steep backwardation (near-dated IV significantly above back-dated IV), which signals that the market is pricing an imminent vol spike. This is more forward-looking than [[event-calendar-risk-gating]] (which requires a specific event to be on the calendar) and earlier than [[regime-gated-grid]]'s ADX/BB-width gate (which detects vol expansion after it has begun). The vol TS gate is the market's aggregate forward-pricing of all anticipated risks — including unscheduled events not on the event calendar — providing an additional lead-time warning for grid operators.

**¹⁵⁸ Grid / market-making × social-velocity gate = non-viable.** Grids are mechanical, single-asset strategies; social velocity is a narrative/retail attention signal. No mechanism connects social mention acceleration to grid profitability or grid break risk.

**¹⁵⁹ Stat-arb / pairs × dominance/alt-season gate = non-viable.** Pairs trading is market-neutral within a universe (e.g., BTC/ETH spread, SOL/AVAX spread); the dominance regime affects the absolute level of alts vs BTC but does not predict whether specific asset pairs will converge or diverge in their cointegration relationship. Applying a dominance gate to stat-arb would suppress pairs entries in rising-dominance regimes without a clear mechanism for why the spread mean-reversion is less reliable then.

**¹⁶⁰ Stat-arb / pairs × liquidity-depth gate = planned.** Before entering a pairs trade, verify that both legs (long and short) have sufficient order-book depth to build the position without excessive adverse price impact. Distinct from [[oi-gated-pairs]] (which checks OI/funding for squeeze risk on the short leg — a strategy-level risk) and from [[vol-balanced-pairs]] (which sizes the legs by vol balance). The depth gate is an execution-quality check: do NOT initiate the spread when the short leg has insufficient depth (the position-building itself would move the market against the entry before the spread has time to mean-revert).

**¹⁶¹ Stat-arb / pairs × ETF-flow gate = non-viable.** Market-neutral pairs trading: ETF flow creates directional bias that destroys the neutral structure. Same reasoning as footnote ⁴⁵ (trend gate).

**¹⁶² Stat-arb / pairs × vol-term-structure gate = non-viable.** Vol TS shape (near vs far IV relationship) does not independently predict cointegration relationship stability or spread mean-reversion timing. The regime gate ([[correlation-regime-pairs]]) and OI gate ([[oi-gated-pairs]]) are the appropriate filters for pairs stability; vol TS adds no independent information.

**¹⁶³ Stat-arb / pairs × social-velocity gate = non-viable.** Social velocity is a narrative/retail attention signal. Pairs spreads mean-revert based on cointegrating relationships (fundamental valuation anchors), not based on social attention dynamics. No mechanism connects social velocity to spread mean-reversion timing.

**¹⁶⁴ On-chain flow × dominance/alt-season gate = non-viable.** On-chain flow signals (whale accumulation, exchange inflows/outflows) are per-asset; the dominance regime is a portfolio-level allocation signal. An on-chain whale accumulation signal in ETH is not improved by knowing whether BTC dominance is rising or falling — the whale is accumulating the asset regardless of the dominance regime.

**¹⁶⁵ On-chain flow × liquidity-depth gate = non-viable.** On-chain whale accumulation signals are multi-day to multi-week in horizon (the signal detects slow accumulation over days); order-book depth is an intraday execution signal. Applying a depth gate to a multi-day on-chain signal adds noise without information, as depth can change hourly while the on-chain accumulation thesis plays out over weeks.

**¹⁶⁶ On-chain flow × ETF-flow gate = planned.** Dual institutional demand confirmation: on-chain smart-money accumulation signal active AND ETF net flow positive simultaneously. When both the on-chain large-wallet cohort AND the institutional ETF channel are net buying, the combined demand signal is more durable and has a larger price impact than either signal alone. Distinct from [[smart-money-vs-crowd-divergence]] (which requires the derivative crowd to be bearish — a divergence signal) and from [[etf-flow-directional]] (which uses ETF flow alone without on-chain confirmation).

**¹⁶⁷ On-chain flow × vol-term-structure gate = non-viable.** On-chain accumulation signals are multi-day to multi-week; vol TS shape is a daily options market signal. The two signals operate on comparable timescales but the mechanism is indirect — options market event risk pricing is not meaningfully predictive of whether smart-money on-chain accumulation will succeed. The event gate ([[event-calendar-risk-gating]]) and regime gate ([[regime-adaptive-strategy]]) already incorporate the risk-off signals that vol TS backwardation would add.

**¹⁶⁸ On-chain flow × social-velocity gate = planned.** On-chain smart-money accumulation + social velocity acceleration: the smart money is buying BEFORE the retail attention inflection. Social velocity rising from low levels while on-chain accumulation is active identifies the timing where the whale buying is about to be followed by retail momentum — the most valuable entry window in the information propagation cycle (earlier than [[whale-copy-flow-funding-filter]] which waits for funding neutrality, and complementary to [[smart-money-vs-crowd-divergence]] which requires crowd-short divergence).

**¹⁶⁹ Sentiment × dominance/alt-season gate = non-viable.** Whole-market Fear & Greed sentiment is already directionally correlated with dominance (fear = dominance rises as capital flees to BTC; greed = dominance falls as capital rotates to alts). The two signals are partially redundant; using both would create a double-counting of the same macro cycle signal.

**¹⁷⁰ Sentiment × liquidity-depth gate = non-viable.** Sentiment-extreme strategies (Fear & Greed contrarian entries) are multi-day to multi-week positions; order-book depth is intraday. Same timescale mismatch as footnote ¹³⁴. The sentiment signal is not meaningfully improved by adding an execution-quality depth check.

**¹⁷¹ Sentiment × ETF-flow gate = non-viable.** ETF flows are partly sentiment-driven (inflows correlate with greed; outflows with fear); gating a sentiment-contrarian strategy on ETF flow alignment risks circular logic (greed + ETF inflow = both bearish for contrarian = wait until inflows turn negative before entering — but inflows turning negative is itself a sentiment shift, duplicating the signal). The sentiment pages ([[contrarian-extremes]], [[sentiment-positioning-divergence]]) already incorporate derivative-market positioning that partially subsumes ETF flow information.

**¹⁷² Sentiment × vol-term-structure gate = non-viable.** Sentiment-extreme entries already fire at peak greed or peak fear conditions; vol TS in those conditions is either in contango (greed, low fear) or steep backwardation (panic fear). Adding a vol TS condition would make sentiment entries conditional on the vol surface being in a particular shape — which is already a component of [[complacency-vol-buying]] (enters when sentiment is greedy AND IV is cheap = contango-like condition) and [[post-panic-vol-selling]] (enters when sentiment is fearful AND vol is spiked = backwardation). Not a distinct combination.

**¹⁷³ Sentiment × social-velocity gate = non-viable.** The Fear & Greed index is itself partly derived from social attention and volume signals; adding a separate social velocity overlay on top of sentiment creates redundancy. The distinctive use of social velocity (rate of change, not level) is better paired with the narrative primitive (footnote ¹⁴³) where the acceleration signal directly identifies the narrative momentum phase.

**¹⁷⁴–¹⁷⁸ MEV / execution × all five new columns = non-viable.** MEV strategies (sandwiching, backrunning, JIT, liquidation MEV, DEX arb) are per-block atomic operations. Dominance regime, order-book depth, ETF flows, vol term structure, and social velocity are all multi-hour to multi-week signals; none have actionable relationships to per-block MEV extraction opportunities. Same reasoning as footnotes ⁶⁶–⁷⁴.

**¹⁷⁹ DeFi yield / LP × dominance/alt-season gate = non-viable.** LP positions are pool-specific (deploy into an ETH/USDC pool or a SOL/USDC pool); the dominance regime is a BTC vs alts portfolio-level signal. While alt-season correlates with higher fee income on alt-pool AMMs (more speculative volume), the decision to deploy in an alt pool vs a BTC pool is inherent to pool selection (a deployment parameter), not a named strategy overlay. The vol-regime gate ([[defi-yield-regime-gate]]) already captures the vol condition that drives LP profitability.

**¹⁸⁰ DeFi yield / LP × liquidity-depth gate = non-viable.** Pool liquidity (TVL, pool depth) is inherent to pool selection in DeFi; a "liquidity-depth gate" for LP deployment describes checking that the pool has sufficient TVL before deploying — this is standard due diligence, not a named combination strategy. [[concentrated-liquidity]] and [[delta-neutral-yield-farming]] both incorporate TVL and pool depth as deployment prerequisites.

**¹⁸¹ DeFi yield / LP × ETF-flow gate = non-viable.** ETF flows are off-chain institutional flows; DeFi LP fee income is driven by on-chain DEX trading volume and pool TVL. There is no direct mechanism connecting ETF net flow state to AMM LP profitability. The sentiment filter ([[defi-yield-sentiment-entry]]) and regime gate ([[defi-yield-regime-gate]]) capture the market conditions that drive LP outcomes more directly than ETF flows.

**¹⁸² DeFi yield / LP × vol-term-structure gate = planned.** LP positions are structurally short gamma (LVR ≈ σ²/8 per unit time). When the vol term structure shifts into steep backwardation (near-dated IV significantly above back-dated IV), the options market is pricing an imminent vol spike that will dramatically increase LVR costs. The vol TS gate is more forward-looking than the DVOL-level gate in [[defi-yield-regime-gate]] (which detects vol expansion after DVOL has already risen) — the TS shape shifts into backwardation hours to days before the DVOL level itself reaches the withdrawal threshold. Composable with the regime gate as a lead-indicator layer.

**¹⁸³ DeFi yield / LP × social-velocity gate = non-viable.** LP fee income is driven by DEX trading volume and pool TVL mechanics. Social attention velocity is a narrative signal that may correlate with token trading volume (during meme seasons, narrative-driven pools see higher volume) but this relationship is indirect and is already captured by the sentiment gate ([[defi-yield-sentiment-entry]]) and meme regime signals.

**¹⁸⁴ Options RV (skew & term structure) × dominance/alt-season gate = non-viable.** Options RV trades are executed on BTC and ETH Deribit options; the BTC dominance regime does not directly affect the BTC/ETH vol surface dislocation that options RV trades exploit. Skew and term structure dislocations are driven by derivative market supply/demand and event risk, not by intra-crypto capital allocation between BTC and alts.

**¹⁸⁵ Options RV (skew & term structure) × liquidity-depth gate = non-viable.** Options RV trades are executed on Deribit options (a separate liquidity venue from CEX perp markets). CEX order-book depth is not a meaningful gate for Deribit options liquidity; Deribit bid-ask spread and options OI are the relevant liquidity metrics for RV trades, and these are already incorporated into the kill criteria and entry conditions of [[skew-trading]], [[calendar-spread-arbitrage]], and [[options-rv-funding-filter]].

**¹⁸⁶ Options RV (skew & term structure) × ETF-flow gate = non-viable.** Options RV (skew, term structure) is gated by statistical vol surface dislocation and derivative crowd positioning (funding, OI) — not by ETF flow direction. While ETF inflows correlate with institutional hedging demand (which affects skew), this relationship is already embedded in the DVOL and skew-level conditions of the existing RV pages.

**¹⁸⁷ [[options-rv-event-calendar]] covers Options RV × vol-term-structure gate.** That page IS the vol term structure trade in the context of scheduled events: it positions the IV term structure trade (long back-dated IV vs short near-dated IV) specifically around event catalysts that create near-dated IV richness. The options RV primitive's primary expression is the vol term structure itself; a separate "Options RV × vol TS gate" would be substantively identical to [[options-rv-event-calendar]]. Cell marked COVERED by existing page.

**¹⁸⁸ Options RV (skew & term structure) × social-velocity gate = non-viable.** Options vol surface dynamics are driven by professional vol traders and institutional hedgers; social velocity is a retail narrative signal. No direct mechanism connects social mention acceleration to vol surface dislocation or skew richness.

**¹⁸⁹–¹⁹³ Prediction markets × all five new columns = non-viable.** Prediction market prices are event-outcome probability estimates anchored to real-world binary outcomes. Dominance regime, order-book depth, ETF flows, vol term structure, and social velocity have no direct causal relationship to whether a Polymarket/Kalshi market is mispriced relative to the true probability of the underlying event. Same reasoning as footnotes ⁹⁰–⁹⁸.

**¹⁹⁴–¹⁹⁸ Stablecoin / peg × all five new columns = non-viable.** Stablecoin depeg arbitrage is driven by redemption channel status, pool imbalance, and collateral risk — mechanistic factors unrelated to BTC dominance, CEX order-book depth, ETF flows, vol term structure shape, or social attention velocity. The existing regime gate, sentiment filter, and event calendar pages ([[stablecoin-depeg-profit-capture]], [[stablecoin-sentiment-depeg-entry]], [[stablecoin-pair-arbitrage]]) cover the viable overlay dimensions. Same reasoning as footnotes ⁹⁹–¹⁰⁷.

**¹⁹⁹ Whale / copy-flow × dominance/alt-season gate = non-viable.** Whale on-chain accumulation signals are per-asset; the dominance regime is a portfolio-level allocation signal. A whale accumulating ETH is providing a per-asset signal regardless of the dominance regime. The funding filter ([[whale-copy-flow-funding-filter]]) and divergence signal ([[smart-money-vs-crowd-divergence]]) already incorporate the crowd positioning context that the dominance regime would add.

**²⁰⁰ Whale / copy-flow × liquidity-depth gate = non-viable.** Whale-copy-flow positions are multi-day to multi-week swing entries; order-book depth is an intraday execution signal. Depth at entry is managed via standard position sizing, not as a strategy-level overlay on multi-week whale-copy entries.

**²⁰¹ Whale / copy-flow × ETF-flow gate = non-viable.** Both whale on-chain accumulation and ETF net flow are directional demand signals for the same underlying asset (BTC/ETH). Conditioning whale-copy entries on ETF flow alignment would create an "institutional double-confirmation" signal that is partially redundant: both signals point in the same direction (buy) without adding independent information that the other does not provide. [[on-chain-smart-money-tracking]] (cross-venue whale tracking) and [[smart-money-orderflow-combo]] (order flow confirmation) are more direct and timely second-leg signals than ETF flow.

**²⁰² Whale / copy-flow × vol-term-structure gate = non-viable.** Whale accumulation signals are multi-day to multi-week; vol TS shape is a daily options market signal. While a steep vol-TS backwardation could warn that an imminent event will test the whale's accumulation thesis, the event calendar ([[event-calendar-risk-gating]]) is the more direct and actionable tool for pausing whale-copy positions around scheduled events. Not a distinct combination.

**²⁰³ Whale / copy-flow × social-velocity gate = non-viable.** Whale on-chain accumulation signals are more informed than social velocity (whales buy before retail notices; social velocity rises after the whale signal has fired). Using social velocity as a gate on whale-copy entries would delay entry to the point where the informational advantage of the whale signal has been substantially reduced — the opposite of the goal. The whale signal should PRECEDE social velocity acceleration, making social velocity a lagging confirmation rather than a useful gate.

---

## Matrix Cell Counts (as of 2026-07-19 — Post C2-1 Column Expansion)

| Status | Count |
|---|---|
| Linked to existing page | 94 |
| Planned (gap to fill) | **14** |
| Non-viable (`—`) | 162 |
| **Total** | **270** |

*C2-1 column expansion (Campaign 2, 2026-07-19): +90 cells (18 rows × 5 new overlay columns). Of those 90 new cells: 2 COVERED by existing pages (momentum × ETF-flow gate = [[etf-flow-directional]]; options RV × vol-TS gate = [[options-rv-event-calendar]]); 16 PLANNED (see per-column audit in Campaign 2 section below); 72 NON-VIABLE with reasoned footnotes (¹¹⁶–²⁰³). Two planned cells authored as new pages in C2-1 (alt-season-momentum-gate, liquidation-depth-cascade-sizing). Additionally, 3 leftover C1-1 planned cells authored in this batch (defi-yield-event-calendar, defi-yield-sentiment-entry, options-rv-funding-filter).*

*C1-1 row expansion (Campaign 2, 2026-07-19): +60 cells (6 new rows × 10 columns). Of those 60 new cells: 16 COVERED by existing pages (mev-strategies × 2, delta-neutral-yield-farming, concentrated-liquidity, skew-trading, calendar-spread-arbitrage, polymarket-prediction-market-arbitrage, prediction-market-strategies × 2, stablecoin-pair-arbitrage, stablecoin-depeg-profit-capture, regime-adaptive-strategy [whale/copy-flow × regime gate], smart-money-orderflow-combo, on-chain-smart-money-tracking, smart-money-vs-crowd-divergence, copy-trading); 8 initially PLANNED; 36 NON-VIABLE with reasoned footnotes (⁶⁶–¹¹⁵). All 8 planned cells now authored across C1-1 and C2-1.*

*B8b completion note: all 120 original-matrix cells (12 rows × 10 columns) remain either linked or non-viable.*

---

## Campaign 2 — Column Expansion (2026-07-19, Batch C2-1)

Campaign 2 Batch C2-1 expands the matrix from **10 to 15 overlay columns** by adding five new overlay types. The original 10 columns covered the core primitive-level overlay universe. The five new columns cover structural regime signals that condition deployment of alt-heavy strategies, execution-quality signals (book depth), institutional flow signals (ETF), options-market forward-risk signals (vol term structure), and retail attention dynamics (social velocity).

**New columns added:**

1. **Dominance / alt-season gate** — BTC dominance as a deployment gate for alt-heavy strategies: deploy cross-sectional alt momentum, narrative, and growth-oriented strategies only when dominance is falling (alt-season confirmed); shift to BTC-only or suppress when dominance is rising. Covers 18 rows; 2 planned, 16 non-viable.

2. **Liquidity-depth gate** — entries and sizing conditioned on real-time order-book depth thresholds. Deep books signal structural liquidity supporting the trade; thin books signal cascade continuation risk or execution uneconomics. CryptoDataAPI depth endpoints: `GET /api/v1/liquidity/depth` and `GET /api/v1/liquidity/depth/{coin}`. Covers 18 rows; 4 planned, 14 non-viable.

3. **ETF-flow gate** — deployment conditioned on spot BTC/ETH ETF net-flow state (sustained inflows/outflows as macro-flow regime). CryptoDataAPI: `GET /api/v1/market-intelligence/etf/{asset}/flows`. 1 covered by [[etf-flow-directional]], 2 planned, 15 non-viable.

4. **Vol-term-structure gate** — conditioned on the IV term structure shape (near vs back-dated DVOL/IV: contango / backwardation / event-hump). Backwardation = market pricing imminent event risk; contango = carry accrues safely. Deribit IV surface required; CryptoDataAPI does not provide options surface data. 1 covered by [[options-rv-event-calendar]], 5 planned, 12 non-viable.

5. **Social-velocity gate** — rate-of-change of social attention (mention momentum, not level) gating narrative/momentum entries. Social velocity identifies the inflection in retail attention that precedes momentum continuation. No CryptoDataAPI endpoint for social velocity; noted honestly (Santiment, LunarCrush, or self-built from social APIs). 3 planned, 15 non-viable.

**Per-column audit summary:**

| Column | Covered by existing | Authored new | Planned remaining | Non-viable |
|---|---|---|---|---|
| Dominance/alt-season gate | 0 | 1 ([[alt-season-momentum-gate]]) | 1 (narrative×dominance) | 16 |
| Liquidity-depth gate | 0 | 1 ([[liquidation-depth-cascade-sizing]]) | 3 (momentum, mean-reversion, stat-arb) | 14 |
| ETF-flow gate | 1 ([[etf-flow-directional]]) | 0 | 2 (narrative×ETF, on-chain×ETF) | 15 |
| Vol-term-structure gate | 1 ([[options-rv-event-calendar]]) | 0 | 5 (funding-carry, momentum, vol-selling, grid, DeFi-yield) | 12 |
| Social-velocity gate | 0 | 0 | 3 (momentum, narrative, on-chain) | 15 |

**Pages authored in C2-1 (5 total — 3 leftover C1-1 + 2 new-column strongest):**

- [[defi-yield-event-calendar]] — DeFi yield/LP × unlock/event calendar: withdraw LP and farming positions ahead of scheduled catalysts (token unlocks ≥ 2% supply, protocol upgrades, points-program endings); redeploy after vol stabilises. The forward-looking, calendar-based complement to the vol-regime gate in [[defi-yield-regime-gate]].
- [[defi-yield-sentiment-entry]] — DeFi yield/LP × sentiment-extreme filter: deploy LP capital after Fear & Greed ≤ 20 fear extremes (pool TVL thin → yields rich, entry price at lows) and de-risk at greed extremes ≥ 75 (TVL crowded → yields compressed, IL exposure maximal at cycle highs).
- [[options-rv-funding-filter]] — Options RV × funding filter: use perp funding rate as a leading indicator for skew richness. Positive funding → call skew bid (sell risk reversal); negative funding → put skew bid (buy risk reversal). The derivative crowd that causes the funding extreme also drives the skew dislocation via option demand.
- [[alt-season-momentum-gate]] — Momentum / trend × dominance/alt-season gate: deploy cross-sectional alt-momentum only in falling-dominance (alt-season) regimes; shift to BTC-only trend in rising-dominance regimes. Solves the most common crypto momentum failure mode: deploying alt-relative-strength during dominance-rising regimes where BTC-dominance headwind overwhelms any alt-relative-strength signal.
- [[liquidation-depth-cascade-sizing]] — Liquidation plays × liquidity-depth gate: size cascade-fade entries proportionally to real-time bid-side order-book depth (as a fraction of its 24-hour average). Depth < 20% of average = no entry; graduated sizing from 25% at 20–39% depth to 100% at ≥ 80% depth. Eliminates the most common cascade-fade failure mode: entering into a thin book that amplifies the next cascade leg.

**Social data note:** The social-velocity gate column references rate-of-change of social mentions. CryptoDataAPI does not currently expose social volume or mention endpoints. Implementations using this gate require external social data providers (Santiment API at `https://api.santiment.net`; LunarCrush at `https://lunarcrush.com/developers`). These are noted honestly in pages that reference the social-velocity gate; no CryptoDataAPI endpoint path is cited for this data.

**14 remaining planned cells (across all 5 new columns):**

| Row | Column | Status |
|---|---|---|
| Narrative | Dominance/alt-season gate | planned |
| Momentum | Liquidity-depth gate | planned |
| Mean-reversion | Liquidity-depth gate | planned |
| Stat-arb / pairs | Liquidity-depth gate | planned |
| Narrative | ETF-flow gate | planned |
| On-chain flow | ETF-flow gate | planned |
| Funding carry | Vol-term-structure gate | planned |
| Momentum | Vol-term-structure gate | planned |
| Vol selling | Vol-term-structure gate | planned |
| Grid | Vol-term-structure gate | planned |
| DeFi yield / LP | Vol-term-structure gate | planned |
| Momentum | Social-velocity gate | planned |
| Narrative | Social-velocity gate | planned |
| On-chain flow | Social-velocity gate | planned |

---

## Campaign 2 — Row Expansion (2026-07-19)

Campaign 2 (Batch C1-1) expands the matrix from 12 to **18 primitive rows** by adding six new primitive families. The original 12 rows covered the core CEX/perp strategy universe. The six new rows cover strategy families that were previously documented as standalone pages but had no systematic overlay analysis:

**New rows added:**

1. **MEV / execution** — Maximal Extractable Value strategies (sandwiching, backrunning, JIT liquidity, liquidation MEV, DEX arbitrage). Primitive pages: [[mev-strategies]], [[jito-solana-mev-arbitrage]], [[jit-liquidity]], [[mev-execution-guide]]. Overlay analysis: nearly all standard overlays are non-viable because MEV is per-block atomic and has no carry-through risk that overlays can gate or size. Only cross-venue (covered by mev-strategies) and session/time (new: [[mev-session-density]]) are viable.
2. **DeFi yield / LP** — Liquidity provider yield strategies on AMMs and yield protocols. Primitive pages: [[defi-yield-farming]], [[leveraged-yield-farming]], [[concentrated-liquidity]], [[delta-neutral-yield-farming]]. IL is structurally a short-vol position; vol-regime gating is the highest-value overlay. Regime gate ([[defi-yield-regime-gate]]), event calendar ([[defi-yield-event-calendar]]), and sentiment entry ([[defi-yield-sentiment-entry]]) are planned. Vol targeting and cross-venue are covered by existing pages; most others non-viable.
3. **Options relative-value (skew & term structure)** — Structurally distinct from the vol selling and vol buying rows: those rows cover directional vol exposure (net short or net long vega). This row covers *market-neutral vol surface mispricings* — 25-delta risk reversal dislocation ([[skew-trading]]), inter-expiry basis ([[calendar-spread-arbitrage]]), cross-asset dispersion ([[crypto-options-dispersion]]). Overlays are mostly non-viable because these are already multi-leg delta-neutral structures. Event calendar ([[options-rv-event-calendar]]) and funding filter ([[options-rv-funding-filter]]) are viable planned additions.
4. **Prediction markets** — Polymarket, Kalshi, and other event-outcome binary markets. Primitive pages: [[prediction-market-strategies]], [[polymarket-prediction-market-arbitrage]], [[polymarket-as-crypto-leading-indicator]]. Most overlays are non-viable by mechanism (bounded-payoff binary markets have no carry-through risk, no funding, no OI to filter on). Cross-venue, event calendar, and sentiment extremes are covered by existing pages.
5. **Stablecoin / peg** — Stablecoin depeg arbitrage and peg-restoration strategies. Primitive pages: [[stablecoin-depeg-profit-capture]], [[stablecoin-pair-arbitrage]], [[synthetic-stablecoin-depeg-arbitrage]]. Sentiment-extreme filter ([[stablecoin-sentiment-depeg-entry]]) is the highest-value planned combination: panic sentiment creates the optimal depeg entry. Cross-venue and event calendar covered by existing pages.
6. **Whale / copy-flow** — Following on-chain informed flow (large wallet accumulation) and systematic copy-trading of tracked whales. Primitive pages: [[copy-trading]], [[on-chain-smart-money-tracking]], [[smart-money-vs-crowd-divergence]], [[smart-money-orderflow-combo]]. Funding filter ([[whale-copy-flow-funding-filter]]) is the key new planned page: copy whales only when the derivative crowd is not yet aligned with the whale move (positive carry for the position, not yet squeezed by crowding).

**Pages authored in C1-1 (5 of 7 planned cells):**

- [[mev-session-density]] — MEV / execution × session/time filter: MEV opportunity density is demonstrably session-dependent (CEX-arbitrage MEV peaks at major session opens; liquidation MEV peaks during high-vol periods). A session-aware MEV scheduling algorithm that concentrates infrastructure costs on high-density windows while pausing during low-yield periods.
- [[defi-yield-regime-gate]] — DeFi yield / LP × regime gate: IL is a short-vol position — deploy LP capital only in low-vol (low-ADV, low-DVOL) regimes; reduce or pause in trending/high-vol regimes. The asymmetry: LP fee income is roughly proportional to vol (good) but LVR loss grows with vol² (bad), so a vol-regime gate that caps deployment above a vol threshold captures most of the fee income while avoiding the worst LVR regimes.
- [[options-rv-event-calendar]] — Options RV × unlock/event calendar: position term-structure trades ahead of scheduled high-vol events (halvings, ETF decisions, FOMC) to harvest the vol-of-vol premium that builds into near-dated expiries. The event calendar gate selects WHEN to enter (not whether the surface is dislocated), generating a forward-looking calendar overlay on top of the RV entry condition.
- [[stablecoin-sentiment-depeg-entry]] — Stablecoin / peg × sentiment-extreme filter: Fear & Greed ≤ 15 AND stablecoin discount ≥ 2% simultaneously signals a panic-driven depeg where the discount is not justified by redemption channel failure. The sentiment-extreme filter separates panic-induced depeg (mean-revert to peg) from structural depeg (avoid / short).
- [[whale-copy-flow-funding-filter]] — Whale / copy-flow × funding filter: copy/follow whale accumulation signals ONLY when funding is flat or negative — i.e., when the derivative crowd is not yet aligned with the whale move. When funding is elevated (crowd has already followed the whale), the edge has largely been captured and entering late carries squeeze risk.

**3 remaining planned cells** (authored in future batches): [[defi-yield-event-calendar]] (DeFi yield × unlock/event calendar), [[defi-yield-sentiment-entry]] (DeFi yield / LP × sentiment-extreme filter — LP deployment at fear extremes when low-vol conditions coincide with panic entry opportunity), and [[options-rv-funding-filter]] (Options RV × funding filter — gate options skew and term-structure entries on funding state as a positioning-crowding check).

---

## Batch B8b — Program Completion (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above. This is the **final batch**; the combination-strategy program is now complete. Every cell in the 12×10 matrix is either linked to a page or marked non-viable with a reasoned footnote.

**Pages written (4 pages covering 5 cells):**

- [[vol-scaled-carry-sizing]] — MULTI-CELL: funding carry × vol targeting AND basis / cash-and-carry × vol targeting. One framework sizes both carry structures to a constant daily-risk budget using the carry P&L stream's realized volatility (not spot price vol) as the denominator. The core correction: carry books accumulate maximum notional at peak carry yield — exactly when P&L volatility (basis blowouts, squeeze risk, funding spikes) is highest. Vol-scaling forces the book smaller in the highest-risk carry regimes and larger in the quietest. Cold-start proxy: carry vol ≈ 15% of spot vol (funding carry) or 8% (basis); recalibrate on 10+ days of actual carry P&L. Rebalance when target notional differs ≥ 15% from current. Composable with [[carry-with-tail-hedge]], [[trend-aware-carry]], and [[event-calendar-risk-gating]] as sequential overlays on the vol-scaled base.
- [[oi-gated-pairs]] — stat-arb/pairs × OI filter. Refuses or exits spread entries when the short leg shows squeeze preconditions: 7d OI change ≥ +15% OR 24h OI change ≥ +8% OR (funding ≤ −0.015%/8h AND L/S ≤ 0.80) OR funding ≤ −0.025%/8h (unconditional). Mid-trade OI monitor at 4h intervals: exit 50% on 4h OI spike ≥ +4%; exit full on funding crossing −0.010%/8h while OI is building, L/S dropping to ≤ 0.75, or 7d OI change since entry exceeding +20%. The short-leg squeeze is the canonical pairs killer — a mechanical forced-covering cascade that overwhelms the cointegration anchor before it can revert. Composable with [[correlation-regime-pairs]] (pre-filter), [[vol-balanced-pairs]] (sizing), and [[pairs-with-funding-differential]] (carry alignment). Note: stat-arb × tail-hedge overlay (calls on the shorted leg) is documented as a refinement here rather than a separate page — see footnote ⁶³.
- [[atr-scaled-grid]] — grid / market-making × vol targeting. Grid spacing = 0.25 × ATR(14, 4h); bounds = reference price ± 2.5 × ATR; per-level notional scales inversely to vol when ATR > 1.5× baseline. Recalibrates every 4h when ATR changes ≥ 15% or every 48h on schedule. Regime kill (ADX > 25 or BB bandwidth > 80th pct) overrides recalibration. The specific contribution over [[regime-gated-grid]] (binary on/off), [[oi-aware-grid]] (OI-build pause), and [[funding-skewed-grid]] (inventory bias): adapts grid geometry continuously to current vol rather than using fixed spacing calibrated at deployment. All four grid overlays are composable.
- [[vol-gated-mean-reversion]] — mean-reversion × vol targeting. Resolves the fundamental tension: mean-reversion edge is strongest at moments of highest vol (panics, flush events), yet naive vol targeting de-sizes exactly those entries. Conditional framework: HIGH-VOL-GOOD (funding ≤ −0.015%/8h + OI −8%/24h + L/S ≤ 0.85 = flush/overshoot → size at 1.25×); HIGH-VOL-BAD (funding ≥ +0.010%/8h AND OI +10%/24h = continuation risk → size at 0.30×); NORMAL-VOL → 1.00×; EXTREME-VOL (RV ≥ 100%) → 0.10×. The sizing wrapper is signal-agnostic: applies on top of [[funding-flush-reversal]], [[oi-flush-reversion]], [[session-aware-mean-reversion]], or any reversion entry signal.

**Cells reclassified non-viable (4 cells):**

- Mean-reversion × cross-venue (footnote ⁵⁹): covered by [[cross-exchange-arbitrage]] (routine venue premium/discount reversion) and [[cross-venue-cascade-dislocation]] (cascade-driven venue dislocations); a separate page would be a thin variant of the cross-exchange-arb framework applied to a reversion primitive.
- Narrative / event × tail-hedge overlay (footnote ⁶⁰): non-buildable — options on specific narrative/memecoin tokens are unavailable or illiquid on Deribit; proxy hedges via BTC/ETH options are beta exposure, not token-specific tail protection. Risk management for narrative positions is via sizing ([[narrative-position-vol-targeting]]) and crowding exit ([[narrative-crowding-exit]]).
- Stat-arb / pairs × tail-hedge overlay (footnote ⁶³): covered as a refinement in [[oi-gated-pairs]]; options on the shorted leg are unavailable for most crypto pairs (only BTC/ETH on Deribit), and the OI gate from [[oi-gated-pairs]] is a superior and universally accessible substitute.
- On-chain flow × tail-hedge overlay (footnote ⁶⁴): overlap with [[leverage-stress-tail-hedge]] is too complete — that page already uses OI/market-cap (the canonical on-chain leverage stress metric) as its primary gate; a separate page would be a thin variant with different input ordering.

**Program completion statement:** Every viable primitive × overlay combination has a dedicated page. Every non-viable cell has a reasoned footnote (footnotes ¹–⁶⁵). No `planned` cells remain. The 12×10 matrix is closed.

---

## Batch B8 New Pages (2026-07-19)

Five new combination pages created in this batch — matrix cells updated above:

- [[vol-balanced-pairs]] — stat-arb/pairs × vol targeting (per-leg vol scaling so both legs contribute equal daily risk: notional_low-vol = total × vol_high / (vol_high + vol_low); eliminates the most common crypto pairs flaw where the high-vol leg [ETH in BTC/ETH] dominates P&L and converts the market-neutral spread into an unintended directional bet; eligibility: 60d correlation ≥ 0.70, cointegration p ≤ 0.05, OU half-life 3–25 days; entry at z-score ≥ 2.0; exit at z-score ≤ 0.5 or 3.5 stop or regime break; weekly vol rebalance if either leg's vol changes ≥ 15%; composable with correlation-regime-pairs [regime pre-filter] and pairs-with-funding-differential [carry alignment filter]; explicitly differentiated from correlation-regime-pairs [regime gate, not leg sizing], pairs-with-funding-differential [carry filter, not vol balance], and vol-targeted-trend-following [portfolio-level sizing on a directional position])
- [[complacency-vol-buying]] — vol buying × sentiment-extreme filter (buy cheap vol/tails when three-factor complacency gate passes: Fear & Greed ≥ 75 for ≥ 3 days [sustained greed] AND DVOL ≤ 35th pct 52w AND ≤ 90% of 30d avg [IV cheap] AND 7d avg funding ≥ +0.030%/8h or OI ≥ 70th pct [leverage building]; primary instrument: OTM put 10–15% OTM DTE 28–45 [if funding ≥ 0.050%/8h] or ATM straddle DTE 21–35 [if funding 0.030–0.050%/8h]; budget 1.0–2.0% of portfolio; exits: 1.5× profit target, DVOL +20 vol pts spike, sentiment normalises to ≤ 50 without ≥ 5% price decline, DTE-7 time exit; the symmetric complement of post-panic-vol-selling; explicitly differentiated from leverage-stress-tail-hedge [OI-stress-gated, not sentiment-gated — fires earlier than OI threshold in sentiment cycle], event-vol-buying [calendar-driven straddles, not sentiment-driven], and long-options-trend-expression [bullish call buying in trend, not crash insurance at greed top])
- [[narrative-crowding-exit]] — narrative/event × funding filter (exit discipline for any narrative long: ride while positioning is clean, exit/trim when funding + OI confirm the narrative has become the consensus crowded trade; Gate 1: 8h funding ≥ +0.050%/8h AND 7d avg ≥ +0.030%/8h; Gate 2: OI ≥ 75th pct of 30d distribution OR 7d OI change ≥ +20%; Gate 3 optional: L/S ≥ 1.60 → triple-confirmation; actions: both-gates = full exit; Gate 1 only = 65% trim with 6% trailing stop on residual 35%; explicitly differentiated from narrative-with-trend-confirmation [entry gate — this is the exit gate], crowded-long-funding-fade [enters a short — this exits a long], and contrarian-extremes [whole-market sentiment fade — this targets token-specific narrative crowding]; entry-strategy-agnostic: works alongside any narrative entry source)
- [[unlock-cascade-watch]] — liquidation plays × unlock/event calendar (monitor liquidation structure around large cliff unlocks ≥ 3% of supply; risk classification: HIGH [OI ≥ 75th pct AND 7d funding ≥ +0.030%/8h], MODERATE [OI 50th–75th pct OR funding +0.015–0.030%/8h], LOW; de-risk existing longs to 25% [HIGH] or 50% [MODERATE] by T − 7; cascade-fade orders: GTC limit buys at −8% [30%], −14% [40%], −20% [30%] of T − 1 close when OI ≥ 70th pct AND funding ≥ +0.025%/8h AND price not already −8% pre-unlock; cascade confirmed when 1h liq volume ≥ 2× 7d avg; post-fill target 8–15% recovery, stop at −10% below lowest fill; explicitly differentiated from unlock-short-with-crowding-gate [directional short], unlock-aware-momentum [momentum book pause without cascade-fade component], unlock-pair-hedge [beta-neutral pairs], and liquidation-cascade-fade [event-calendar-agnostic])
- [[event-calendar-risk-gating]] — MULTI-CELL: grid × unlock/event + funding carry × unlock/event + vol selling × unlock/event (also covers basis × unlock/event); unified framework for pausing/de-sizing mechanical/passive strategies around scheduled binary events; Tier 1 [full halt ±3 days]: halvings, ETF/regulatory decisions, major hard forks, unlocks ≥ 10% supply; Tier 2 [50–75% reduction ±2 days]: 4–9% unlocks, FOMC when macro correlation active, major EIPs; per-strategy parameters: grid [60% reduction T2; resume at DVOL −15 pts from peak AND price in range], carry [50% T2; resume at funding within 30% of pre-event], short-vol [75% T2; CLOSE all short options for T1; resume at DVOL −20 pts from peak]; explicitly differentiated from event-vol-buying [TRADES the event — buys vol; this AVOIDS the event — pauses passive books], regime-gated-grid [lagging vol-regime trigger; this is forward-looking calendar-based], and trend-aware-carry [trend-based carry reduction; this is event-date-based halt])

Skips (0 of 5 primaries): all five primary candidates confirmed additive. Backup `vol-scaled-carry-sizing` (funding carry × vol targeting) and `oi-gated-pairs` (stat-arb × OI filter) remain planned — not written. (Both written in B8b.)

Part 2 reclassifications: 29 `planned` cells reclassified as non-viable (`—`) via honest assessment (see footnotes ²⁴–²⁷, ²⁸–³², ³⁴–³⁵, ³⁶–³⁷, ³⁸–⁴², ⁴³–⁴⁴, ⁴⁵, ⁴⁷–⁴⁸, ⁴⁹–⁵¹, ⁵²–⁵⁶). Categories reclassified: basis row (4 cells: OI filter, trend gate, sentiment, session); liquidation plays row (3: trend gate, vol targeting, sentiment); narrative row (2: cross-venue, session); vol selling row (2: cross-venue, session); vol buying row (4: funding filter, vol targeting, cross-venue, session); grid row (2: cross-venue, sentiment); stat-arb row (3: trend gate, sentiment, session); on-chain row (3: vol targeting, cross-venue, session); sentiment row (5: OI filter, vol targeting, cross-venue, unlock/event, session). No viable-but-unwritten combinations were force-reclassified. Remaining 9 planned cells are all genuine gaps awaiting future batches.

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
