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
| **Funding carry** | [[regime-adaptive-strategy]] | — ¹ | [[oi-confirmed-trend]] ² | [[trend-aware-carry]] | [[carry-with-tail-hedge]] | [[vol-scaled-carry-sizing]] ⁵⁷ | [[hl-vs-cex-funding-divergence]] | [[event-calendar-risk-gating]] ²³ | [[crowded-long-funding-fade]] | [[funding-window-timing]] ¹⁷ |
| **Basis / cash-and-carry** | [[regime-adaptive-strategy]] | [[funding-vs-basis-rotation]] ¹¹ | — ²⁴ | — ²⁵ | [[carry-with-tail-hedge]] | [[vol-scaled-carry-sizing]] ⁵⁷ | [[hl-vs-cex-funding-divergence]] | [[event-calendar-risk-gating]] ²³ | — ²⁶ | — ²⁷ |
| **Momentum / trend** | [[regime-adaptive-strategy]] | [[funding-filtered-momentum]] | [[oi-confirmed-trend]] | — ³ | [[trend-plus-tail-hedge]] | [[vol-targeted-trend-following]] | [[spot-led-momentum-filter]] | [[unlock-aware-momentum]] | [[contrarian-extremes]] ⁴ | [[session-aware-mean-reversion]] ¹² |
| **Mean-reversion** | [[regime-adaptive-strategy]] | [[funding-flush-reversal]] | [[oi-flush-reversion]] | [[pullback-trading]] ²² | [[put-protected-dip-buying]] ¹⁴ | [[vol-gated-mean-reversion]] ⁵⁸ | — ⁵⁹ | — ²⁸ | [[contrarian-extremes]] | [[session-aware-mean-reversion]] |
| **Liquidation plays** | [[regime-adaptive-strategy]] | [[crowded-long-funding-fade]] | [[oi-confirmed-trend]] | — ²⁹ | [[cascade-monetization-rotation]] ¹³ | — ³⁰ | [[cross-venue-cascade-dislocation]] ¹⁸ | [[unlock-cascade-watch]] ³¹ | — ³² | [[off-hours-liquidation-playbook]] |
| **Narrative / event** | [[regime-adaptive-strategy]] | [[narrative-crowding-exit]] ³³ | [[oi-confirmed-trend]] | [[narrative-with-trend-confirmation]] | — ⁶⁰ | [[narrative-position-vol-targeting]] | — ³⁴ | [[unlock-short-with-crowding-gate]] | [[contrarian-extremes]] | — ³⁵ |
| **Vol selling** | [[regime-adaptive-strategy]] | [[funding-conditioned-vol-selling]] | [[low-leverage-vol-selling]] ¹⁵ | [[trend-aligned-premium-selling]] | — ⁵ | [[volatility-targeting]] | — ³⁶ | [[event-calendar-risk-gating]] ²³ | [[post-panic-vol-selling]] | — ³⁷ |
| **Vol buying / tail hedge** | [[regime-adaptive-strategy]] | — ³⁸ | [[leverage-stress-tail-hedge]] | [[long-options-trend-expression]] ¹⁹ | — ⁶ | — ³⁹ | — ⁴⁰ | [[event-vol-buying]] | [[complacency-vol-buying]] ⁴¹ | — ⁴² |
| **Grid / market-making** | [[regime-gated-grid]] | [[funding-skewed-grid]] | [[oi-aware-grid]] | — ⁷ | [[grid-with-tail-hedge]] ²⁰ | [[atr-scaled-grid]] ⁶¹ | — ⁴³ | [[event-calendar-risk-gating]] ²³ | — ⁴⁴ | [[session-overlap-momentum]] ⁸ |
| **Stat-arb / pairs** | [[correlation-regime-pairs]] | [[pairs-with-funding-differential]] | [[oi-gated-pairs]] ⁶² | — ⁴⁵ | — ⁶³ | [[vol-balanced-pairs]] ⁴⁶ | [[hl-vs-cex-funding-divergence]] | [[unlock-pair-hedge]] | — ⁴⁷ | — ⁴⁸ |
| **On-chain flow** | [[regime-adaptive-strategy]] | [[smart-money-vs-crowd-divergence]] ¹⁶ | [[oi-confirmed-trend]] | [[smart-money-orderflow-combo]] ⁹ | — ⁶⁴ | — ⁴⁹ | — ⁵⁰ | [[unlock-short-with-crowding-gate]] | [[onchain-capitulation-confluence]] | — ⁵¹ |
| **Sentiment** | [[regime-adaptive-strategy]] | [[sentiment-positioning-divergence]] ²¹ | — ⁵² | [[crypto-beta-rotation]] | — ⁶⁵ | — ⁵³ | — ⁵⁴ | — ⁵⁵ | — ¹⁰ | — ⁵⁶ |

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

---

## Matrix Cell Counts (as of 2026-07-19 — Program Complete)

| Status | Count |
|---|---|
| Linked to existing page | 66 |
| Planned (gap to fill) | **0** |
| Non-viable (`—`) | 54 |

*B8b changes: +5 linked (vol-scaled-carry-sizing covers 2 cells — funding carry × vol targeting AND basis × vol targeting; oi-gated-pairs covers stat-arb × OI filter; atr-scaled-grid covers grid × vol targeting; vol-gated-mean-reversion covers mean-reversion × vol targeting); −5 planned (5 to linked); +4 non-viable (mean-reversion × cross-venue, narrative × tail-hedge overlay, stat-arb × tail-hedge overlay, on-chain × tail-hedge overlay all reclassified with reasons in footnotes ⁵⁹–⁶⁵).*

*Program completion: all 120 matrix cells are now either linked to a page or marked non-viable with a reasoned footnote. No `planned` cells remain.*

*B8 (prior batch) changes for reference: +8 linked (7 new page cells + basis/unlock covered by event-calendar-risk-gating); −37 planned (8 to linked, 29 to non-viable via Part 2 reclassification); +41 non-viable (29 new reclassifications + 12 existing from footnotes ¹–¹⁰ + new ones added in B8 footnotes ²³–⁵⁶).*

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
