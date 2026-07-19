---
title: "Volatility Spike"
type: concept
created: 2026-05-07
updated: 2026-07-19
status: excellent
tags: [volatility, indicators, options, risk-management, vix]
aliases: ["Vol Spike", "Volatility Spike", "VIX Spike", "Vol Shock"]
related: ["[[vix]]", "[[vix-futures]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[volatility-regime]]", "[[volatility-regime-classification]]", "[[volatility-regime-switching]]", "[[vol-regime-detection]]", "[[vol-of-vol]]", "[[vvix]]", "[[volatility-term-structure]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[covid-crash]]", "[[options-risk-budgeting]]", "[[vega-budgeting]]", "[[long-vol-vs-short-vol]]", "[[gamma-explosion]]", "[[second-order-greeks]]", "[[vanna]]", "[[vega]]", "[[gamma]]", "[[leaps]]"]
domain: [volatility, indicators, options]
prerequisites: ["[[implied-volatility]]", "[[vix]]"]
difficulty: intermediate
---

A **volatility spike** is a sudden, large rise in [[implied-volatility|implied volatility]] (and typically in realised volatility a few days later) over a very short window — most commonly a single trading session. Empirically the [[vix|VIX]] frequently leaps from sub-15 to 30+ on shock days, and historic episodes have seen VIX more than triple intraday from prior-session close. A vol spike is *not* the same thing as a [[volatility-regime|vol regime shift]]: a spike can fully mean-revert within days, while a regime shift sticks for weeks-to-months. The mechanics that drive a spike (dealer hedging, gamma squeezes, [[volatility-targeting|vol-target]] flows, ETP rebalancing) are largely independent of whether the spike *resolves* into a sustained stressed regime.

## Mechanism

A vol spike is the joint output of several reinforcing flows that activate at roughly the same time. Identifying the contributing flows is what determines whether the spike will mean-revert or cement into a regime change.

Before the mechanism, a rough severity scale helps calibrate response. The thresholds below are conventional reference points, not hard rules:

| Severity | Single-session VIX move | Typical character | Base-rate (post-1990, illustrative) |
|----------|--------------------------|--------------------|--------------------------------------|
| Minor | +15–25% | Flow/technical wobble; usually retraces same week | several per year |
| Moderate | +25–60% | News-driven; backwardation appears briefly | a few per year |
| Major | +60–120% | Structural/forced flows; ETP and short-vol stress | roughly once a year |
| Extreme | >2x intraday | Systemic or terminal-clause events (Volmageddon, COVID) | once every few years |

The severity scale is about *the move*, not the level. As §"Common Mistakes" notes, a VIX 15→20 move is more disruptive to a short-vol book than VIX 25→28 despite being a smaller absolute change, because vega risk scales non-linearly with level (see [[vol-of-vol]]).

### 1. Dealer hedging unwind

Options dealers run inventory positions whose Greeks must be hedged in the underlying. In normal conditions, market makers are net short [[gamma|gamma]] to the customer (customers buy puts and calls, dealers sell). When spot moves sharply, short-gamma dealers must buy (or sell) the underlying to stay flat — buying into rallies and selling into drops. This *hedging activity itself* increases realised volatility, which raises [[implied-volatility|IV]] (because option pricing models scale with realised), which forces re-hedging at the new IV. The feedback loop is the canonical *gamma scramble*. See [[gamma-explosion]] for the full mechanism.

A distinct but reinforcing channel is the **vanna flow** ([[second-order-greeks|second-order Greek]] [[vanna]]): when IV jumps, the delta of dealers' short OTM puts becomes more negative even with spot flat, forcing them to *sell* the underlying. This vanna-driven selling adds to the gamma scramble during a spike, which is why equity selloffs and VIX spikes feed each other. See [[second-order-greeks#Worked Example — Vanna Surprise on a Delta-Neutral Book]] for the mechanics.

### 2. Gamma squeeze on short-vol books

Short-volatility positions (short strangles, [[iron-condor|iron condors]], leveraged inverse-VIX ETPs) hold negative vega *and* negative gamma. When IV rises, the books take both a vega loss (mark-to-market) and a gamma loss (the underlying has moved more than the position's hedge can compensate). Margin calls force the funds to *buy back the very options they were short* — bidding up IV further. This is the precise mechanism that destroyed [[xiv-velocity-shares|XIV]] in [[volmageddon|February 2018]]: the daily rebalancing flow of short-vol ETPs near the close mechanically purchased VIX futures at any price, lifting them and triggering the ETP termination clause.

### 3. ETP rebalancing flows

Volatility ETPs ([[xiv-velocity-shares|XIV]], SVXY, UVXY, VIXY, etc.) rebalance daily to maintain target leverage. The rebalance trade is *always in the direction of the move* — leveraged long-vol products buy more VIX futures into a rally; inverse products buy VIX futures into a rally as part of their delta-neutralizing hedge. On a quiet day this rebalance flow is small. On a sharp move day, the flow scales non-linearly with the size of the move and frequently dominates marginal price discovery in the last hour of trading. Volmageddon's terminal hour was almost entirely ETP rebalance flow.

### 4. Broad de-risking

Risk-budget-driven funds ([[risk-parity]], [[volatility-targeting]], CTA, risk-control products) automatically de-leverage when realised vol breaches their budgets. They sell *across all positions* simultaneously. The cross-asset selling pushes more securities into the hedger's gamma scramble and accelerates the spike.

### 5. Liquidity contraction

Market makers reduce quoted size in fast markets. The same flow that produces a 1-vol-point IV move under normal liquidity produces 5+ vol-point moves under thin liquidity. Liquidity contraction is itself a feedback term: as IV rises, dealer balance-sheet usage rises, dealers reduce inventory, liquidity worsens, IV rises further.

## Distinguishing Spike from Regime Shift

A spike that mean-reverts within a week is operationally very different from a spike that initiates a sustained stressed regime. The market generates many of the former; the latter are rare. The structural test is whether the *underlying conditions* that drive volatility have changed.

| Indicator | Spike (mean-reverting) | Regime shift (persistent) |
|-----------|------------------------|---------------------------|
| Catalyst | Technical / flow-driven | Fundamental / macro change |
| Term structure response | Front-month spikes; back-month muted | Entire curve shifts up |
| Backwardation | Brief (1–3 sessions) | Sustained (5+ sessions) |
| Credit spreads | Modest widening | Large, sustained widening |
| RV/IV ratio | RV trails; IV overshoots | RV catches and exceeds IV |
| Cross-asset confirmation | Limited | Broad (FX, rates, gold, credit all confirm) |
| [[vvix|VVIX]] | Spikes more than VIX | Spikes alongside VIX |
| Resolution | Days | Weeks-to-months |

Operational rule: **wait for sustained backwardation (3+ sessions) and credit confirmation before treating a vol spike as a regime change.** See [[volatility-regime-classification]] for the full classification framework and [[vol-regime-detection]] for real-time detection methods.

## Empirical Cases

### August 24, 2015 — "Flash crash" Monday

VIX opened at ~28 (vs ~13 the prior week) and traded as high as ~53 intraday before closing at 40.74. The prior Friday's close was 28.03; intraday the index showed a >2x spike from prior settlement. Triggered by the China devaluation panic two sessions earlier, the spike mean-reverted within 3 weeks to sub-20. Classic example of a *spike that did not become a regime change*.

### February 5, 2018 — [[volmageddon|Volmageddon]]

The defining short-vol blowup of the modern era. On February 5, 2018, VIX rose from 17.31 (Feb 2 close) to 37.32 (Feb 5 close), a +115% single-day move. After-hours, [[xiv-velocity-shares|XIV]] saw its rebalance flow drive VIX futures to print an additional ~30% rise overnight, triggering the ETP's termination clause and destroying $1.9B+ of investor capital. VIX spent the next three weeks elevated and then mean-reverted, but the *short-vol ecosystem* was permanently changed. The spike *was* a regime change in a structural sense — the short-vol ETP complex never recovered to its pre-Feb-2018 size — even though spot VIX itself mean-reverted.

### March 2020 — [[covid-crash|COVID Crash]]

VIX rose from 14.38 on Feb 19, 2020 to a closing high of 82.69 on March 16, 2020, an intra-period peak of 85.47. This was both a spike *and* a regime change: VIX stayed above 30 for ~2 months. Realised vol caught and exceeded implied. Term structure stayed in backwardation for weeks. Credit spreads blew out; the dollar funding stress was systemic. The fact that the spike was accompanied by macro deterioration and cross-asset confirmation distinguished it from the Aug 2015 type-pattern.

### August 5, 2024 — [[vix-august-2024-spike|JPY carry unwind]]

On August 5, 2024, VIX printed an intraday high of 65.73, briefly pushing into territory only seen in March 2020 and March 2008. The trigger was the unwinding of the JPY carry trade after the Bank of Japan rate hike on July 31, combined with a weak July US payrolls print on August 2. By August 9 the VIX had retraced to ~20. The spike was severe but mean-reverted quickly because the *structural drivers* (dollar funding, macro shock, credit dislocation) were absent. Typical example of a *flow-driven spike that did not become a regime change*.

### Single-session spike cases (smaller magnitude)

- **August 2007** — quant equity unwind. VIX +30% over two sessions.
- **May 6, 2010** — [[flash-crash|Flash Crash]]. VIX briefly +30% intraday, mostly retraced same session.
- **August 2011** — US debt downgrade. VIX +50% over two sessions, sustained for ~3 weeks before partial mean reversion.
- **January 27, 2021** — meme-stock short squeeze. VIX +60% in a single session before retracing within days.

## Implications for Strategy

### 1. Short-vol books need spike-survivable sizing

The base rate of a "VIX doubles in a session" event is roughly once every 2–3 years in S&P 500 over the post-1990 sample. Any short-vol position must survive that scenario *with size left over* to take advantage of post-spike opportunities. Sizing using 95% historical VaR — which is calibrated to *normal* days — leaves the book under-protected against the spike day. See [[options-risk-budgeting]] §"Tail-Risk / Scenario Budget".

### 2. Long convexity is most valuable around spikes

The P&L profile of a long-[[vega|vega]]/long-[[gamma|gamma]] tail hedge is dominated by a small number of vol-spike days. A position that bleeds 1% per month for 18 months and then prints 30% on a single spike day has a high *time-average* return even if the average daily P&L looks negative. This is the structural argument for a persistent small allocation to long convexity even in calm regimes — see [[long-vol-vs-short-vol]] and [[volatility-regime-classification]] §"Convexity Allocation".

Common instruments for capturing or hedging a spike, and what each is exposed to:

| Instrument | Primary exposure | Spike payoff | Main drawback |
|------------|------------------|--------------|----------------|
| Long [[vix]] calls | VIX + [[vega]] convexity | very high (convex) | severe theta/roll bleed in calm |
| Long index puts (incl. [[leaps]] puts) | [[delta]] + [[vega]] | high on selloff | path-dependent; vega crush after |
| Long VIX futures | front-month VIX | linear, no convexity | roll cost in contango |
| Long [[long-dated-options]] straddles | [[gamma]] + vega | moderate, durable | expensive carry; long-dated [[vega]] |
| Tail funds / put spreads | defined convexity | capped but cheaper | cap limits the big-spike payoff |

The choice is a trade-off between **carry cost in calm** and **convexity in the spike** — VIX calls maximise convexity but bleed hardest; put spreads minimise bleed but cap the payoff exactly when an extreme spike would pay most.

### 3. VVIX as a meta-signal

[[vvix|VVIX]] (the VIX-of-VIX) measures the volatility of VIX options. VVIX tends to rise *before* VIX in many spike events because options dealers hedge their VIX option books before retail flow shows up in spot VIX. A sharp VVIX rise without commensurate VIX rise can be a leading indicator of an impending spike.

### 4. Selling into a spike vs after a spike

Selling premium *into* a fresh spike is selling at the precise moment the [[vega|vega]] markup is happening — your short-vega position takes the worst of the markup. Selling premium *after* a spike has stabilized (3–5 sessions of consolidation) lets the volatility risk premium compress in your favour. The latter is consistently more profitable empirically; the former is where most short-vol blowups concentrate.

### 5. Spike-day liquidity is the binding constraint

Bid-ask spreads on options widen 3–10x on spike days. A "stop loss at -$5,000" set under normal liquidity becomes a "stop loss at -$15,000" when executed on a spike day. Position sizing must assume *spike-day execution liquidity*, not normal-day liquidity.

## Common Mistakes

1. **Assuming all spikes mean-revert.** Most do; the ones that don't (2008, 2020, 2022) destroy short-vol books that fade them. The base rate is overstated by survivorship — books that faded a regime-change spike no longer exist to publish their results.
2. **Confusing VIX level with VIX *change***. A move from VIX 15 to VIX 20 (5 points / +33%) is much more disruptive to a short-vol book than a move from VIX 25 to VIX 28 (3 points / +12%). Vol-of-vol scales non-linearly with level — see [[vol-of-vol]].
3. **Selling premium "because IV is high."** IV is high *because* something is happening. The premium-to-realised gap may be *narrower* during a spike than during calm — sellers receive bigger premium per contract but are exposed to a much wider distribution of outcomes.
4. **Treating VIX as the only vol benchmark.** Single-name IVs can spike for stock-specific reasons that don't move VIX. A short strangle on a single name during an earnings spike is not protected by a calm VIX.
5. **Ignoring the term structure.** Front-month VIX futures spike harder than back-month. A short-front-leg / long-back-leg position (calendar spread) flips P&L sign as the curve inverts.
6. **Re-shorting too early after a spike.** Vol-of-vol stays elevated for days after a spike even when spot VIX retraces. Selling into the immediate post-spike rally typically drops you straight into the next leg of the spike.

## Detection in Real Time

A simple operational checklist for *during* a spike:

- VIX up >20% intraday from prior close → spike threshold breached.
- VIX/VIX3M ratio crossing 1.00 → backwardation onset; structural concern.
- VVIX up >25% same day → vol-of-vol confirmation.
- HY OAS up >25 bps same day → cross-asset confirmation.
- Realised 5-day vol catching up to implied → not yet, but watch.

If any 3 of the above hit simultaneously, treat the move as potentially regime-shifting and de-risk before waiting for confirmation. The asymmetry (cheap to de-risk and be wrong; expensive to ride it through and be wrong) favours acting on incomplete signals. See [[vol-regime-detection]] for the structured detection framework.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/volatility/regime` — per-asset vol states; the `vol_shock` label is the crypto spike flag
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/market` — HMM probabilities including the `vol_spike` state (15-min refresh)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility, the amplifier in the mechanism above

**Historical data:**
- `GET /api/v1/backtesting/klines` — kline archive for measuring historical realized-vol jumps
- `GET /api/v1/backtesting/liquidations` — liquidation records (Hyperliquid, since 2026-03-30), the crypto counterpart of forced-flow unwinds

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/quant/market"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [short-term regimes](https://cryptodataapi.com/market-regimes) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — poll `GET /api/v1/quant/market` for the `vol_spike` probability and `GET /api/v1/volatility/regime/score` for the market-wide stress read; in crypto the forced-flow leg of the checklist is liquidations, visible via `GET /api/v1/quant/gex` liquidation profiles (Pro+)
- **Detect** — an agent's crypto version of this page's checklist: `vol_spike` probability jumping + liquidity fragility score rising + realized 24h vol from klines outrunning its 30d mean — treat any 2-of-3 as de-risk-now
- **Backtest** — spike-vs-regime-shift classification replays against `GET /api/v1/quant/regimes/history` (hourly HMM since 2020, Pro Plus) joined to `GET /api/v1/backtesting/klines`; liquidation-driven spikes are only replayable since 2026-03-30
- **Tip** — mirror the asymmetry rule mechanically: cheap to de-gross on a false spike signal, ruinous to ride a true one — so wire the detector to sizing before the spike, not to an alert a human reads after it

## Related

- [[vix]] — the volatility index that spikes
- [[vix-futures]] — the term structure that signals regime
- [[vvix]] — vol of vol; spike leading indicator
- [[implied-volatility]] / [[realized-volatility]] — the two vols whose gap behaves differently in spikes vs regime shifts
- [[volatility-regime]] — the broader concept
- [[volatility-regime-classification]] — the operational regime framework
- [[volatility-regime-switching]] — formal regime models
- [[vol-regime-detection]] — real-time detection methods
- [[vol-of-vol]] — why vega risk scales non-linearly with level
- [[volatility-term-structure]] — the curve that inverts in regime change
- [[gamma-explosion]] — the dealer-hedging mechanism
- [[volmageddon]] — case study: spike that destroyed a structural product
- [[vix-august-2024-spike]] — case study: severe spike that mean-reverted
- [[covid-crash]] — case study: spike that became a regime change
- [[options-risk-budgeting]] — sizing options books to survive spikes
- [[vega-budgeting]] — vega exposure limits in vol-spike scenarios
- [[long-vol-vs-short-vol]] — the posture spectrum
- [[second-order-greeks]] — vanna/vomma dominate P&L during spikes
- [[vanna]] — the delta-vs-vol flow that reinforces the spike
- [[leaps]] — long-dated puts as a slow-bleed spike hedge

## Sources

- Whaley, R. (2000). *The Investor Fear Gauge*. Journal of Portfolio Management. Foundational reference for VIX behaviour and spike dynamics.
- CBOE — VIX, VIX9D, VIX3M, VVIX methodology white papers.
- Bollen, N. and Whaley, R. (2004). *Does Net Buying Pressure Affect the Shape of Implied Volatility Functions?* Journal of Finance 59(2). Documents the dealer-hedging contribution to IV moves.
- Reports on the February 2018 short-vol blowup — *Financial Times*, *Risk.net*, CFTC and SEC post-event analyses; Credit Suisse XIV documentation.
- BIS Quarterly Reviews (March 2020, December 2020) — analysis of the COVID dollar funding stress and the cross-asset vol response.
- Bank of Japan and IMF post-event commentary on the August 2024 carry-trade unwind.
- Engle, R. and Ng, V. (1993). *Measuring and Testing the Impact of News on Volatility*. Journal of Finance 48(5). Asymmetric response of vol to news, foundational for spike mechanics.
