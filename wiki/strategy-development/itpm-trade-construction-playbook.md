---
title: "ITPM Trade Construction Playbook"
type: concept
created: 2026-04-10
updated: 2026-06-20
status: excellent
tags: [strategy-development, itpm, options, trade-construction, playbook]
aliases: ["ITPM Playbook", "Kreil Trade Construction", "Professional Trader Workflow"]
domain: [strategy-development, options]
difficulty: intermediate
related: ["[[anton-kreil]]", "[[strategy-development-overview]]", "[[research-checklist]]", "[[options-greeks]]", "[[itpm-five-principles]]"]
---

# ITPM Trade Construction Playbook

A workflow for *producing* trades from a market view, in the style taught by the Institute of Trading and Portfolio Management and [[anton-kreil|Anton Kreil]]. Most of this wiki catalogs strategies as static objects ("here is a covered call"); this page is about the *process* a discretionary professional trader uses to convert a market view into an actual portfolio of positions. Distinct from systematic strategy development because the inputs are qualitative (top-down macro view, sector relative strength, fundamental story) and the outputs are constructed trades (specific options structures sized to a thesis).

## The Process at a High Level

```
Macro View
   ↓
Geographic / Asset Class Allocation
   ↓
Sector Selection (Long / Short)
   ↓
Stock Selection Within Sectors
   ↓
Catalyst Identification
   ↓
Risk/Reward Geometry
   ↓
Options Structuring
   ↓
Position Sizing
   ↓
Hedging
   ↓
Trade Management
   ↓
Exit
```

The process is *top-down*: you start with the broad picture and work down to individual positions. This is the opposite of bottom-up screening, where you find a stock first and then justify it. Top-down forces you to have a *reason* for being in any given position before you take it.

### Stage Index

Each stage answers one question and produces one output that feeds the next stage. Skipping a stage is the most common source of the [Common Mistakes](#common-mistakes) below.

| Stage | Question it answers | Output | Skipping it causes |
|---|---|---|---|
| 1. [Macro View](#stage-1-macro-view) | What is the world doing? | A defensible top-down picture | Trading setups in isolation |
| 2. [Geographic / Asset Class](#stage-2-geographic-and-asset-class-allocation) | Where do I want exposure? | Thematic positions | No parent theme for trades |
| 3. [Sector Selection](#stage-3-sector-selection) | Which sectors win/lose? | Long-sector & short-sector lists | Fighting sector leadership |
| 4. [Stock Selection](#stage-4-stock-selection-within-sectors) | Best stock in each sector? | Long & short short-lists | Weak names in right sectors |
| 5. [Catalyst](#stage-5-catalyst-identification) | What moves it, and when? | Time horizon + invalidation | A hope, not a trade |
| 6. [Risk/Reward Geometry](#stage-6-riskreward-geometry) | Entry / target / stop? | R/R ratio (min 3:1) | Sizing then hoping |
| 7. [Options Structuring](#stage-7-options-structuring) | Which structure fits the view? | A defined-risk structure | Paying full risk on stock |
| 8. [Position Sizing](#stage-8-position-sizing) | How much? | 1-2% capital at risk | Blow-up risk |
| 9. [Hedging](#stage-9-hedging) | What unwanted risk remains? | A hedged book | Carrying market beta you didn't want |
| 10. [Trade Management](#stage-10-trade-management) | Is the thesis still alive? | Monitoring + roll plan | Letting options expire in your face |
| 11. [Exit](#stage-11-exit) | Why am I getting out? | A clean exit | Holding past invalidation |

The discipline that separates ITPM-style construction from retail trading is that **every output is produced before the trade is placed.** You do not discover your stop after you are in the position; you draw the [Stage 6](#stage-6-riskreward-geometry) geometry first and let it gate everything downstream.

## Stage 1: Macro View

Before opening any position, you need a view on:

1. **Global growth** — accelerating, decelerating, in recession
2. **Inflation regime** — rising, falling, stable
3. **Central bank trajectory** — hiking, cutting, on hold
4. **Liquidity conditions** — expanding, contracting
5. **Risk appetite** — risk-on or risk-off
6. **Currency dynamics** — strong dollar / weak dollar trend

These six form the "macro picture." Each translates into rough preferences for asset classes:

- Risk-on + accelerating growth → favor equities, especially cyclicals; underweight bonds
- Rising inflation + hiking cycle → favor commodities, underweight long-duration bonds, careful on growth stocks
- Risk-off + slowing growth → favor bonds, defensive sectors, gold; underweight cyclicals
- Strong dollar → underweight emerging markets, underweight commodities

The macro view doesn't have to be precise. It just has to be *defensible* and *consistent*. ITPM emphasizes that most retail traders don't form a macro view at all; they trade individual setups in isolation. The first source of edge is just *having* a top-down framework.

## Stage 2: Geographic and Asset Class Allocation

Given the macro view, allocate across:

- **Geographies** — US, Europe, Asia, EM
- **Asset classes** — equities, bonds, FX, commodities
- **Long vs. short bias** — net long or net short the market

The output is a set of *thematic positions* — "long US tech because the Fed is dovish and growth is accelerating," "short European banks because the ECB is behind the curve."

These themes are the *parents* of all individual stock positions. Every stock you trade should be a *child* of a thematic position.

## Stage 3: Sector Selection

Within your favored geographies, identify which sectors should *win* and which should *lose* in the macro regime you've defined.

The ITPM approach uses **sector relative strength**: rank sectors by their performance vs. the broad market over multiple lookback windows (1, 3, 6, 12 months). Sectors with persistent positive relative strength are *leadership sectors*; sectors with persistent negative relative strength are *laggards*.

For each macro regime, leadership sectors are usually:
- **Risk-on / accelerating growth:** Tech, Discretionary, Industrials, Materials, Financials
- **Risk-off / slowing growth:** Staples, Utilities, Healthcare, Real Estate (defensives)
- **Inflationary:** Energy, Materials, Financials (banks benefit from rising rates)
- **Disinflationary:** Tech, Discretionary, growth in general

The output of this stage is a *list of sectors* you want to be long and a *list of sectors* you want to be short.

## Stage 4: Stock Selection Within Sectors

Within each long-sector, identify the *strongest* stocks. Within each short-sector, identify the *weakest* stocks. The selection criteria:

### Top-down filters
- Inside an in-favor sector? (long candidates)
- Inside an out-of-favor sector? (short candidates)
- Inside an in-favor geography?

### Fundamental filters
- Strong revenue and earnings growth? (long)
- Declining or flat fundamentals? (short)
- High quality (low debt, high margins)? (long)
- Deteriorating quality? (short)
- Reasonable valuation? (long; overvalued = caution)
- Stretched valuation? (short candidate)

### Technical filters
- Strong relative strength vs. sector and broad market? (long)
- Weak relative strength? (short)
- In a clear technical uptrend / downtrend?
- Positioned near a logical support / resistance level?

### Sentiment filters
- Bullish analyst consensus + rising estimates? (long)
- Bearish consensus + falling estimates? (short)
- High short interest in a strong stock? (squeeze potential, long)
- Crowded long with declining momentum? (short)

The intersection of these filters produces a *short list* of long candidates and short candidates within each sector.

## Stage 5: Catalyst Identification

A position without a catalyst is a position with no reason to move. Before placing the trade, identify:

1. **What is the catalyst that will move the stock?** (earnings, product launch, FDA decision, sector rotation, macro event)
2. **When does the catalyst hit?** (specific date, range of dates, ongoing)
3. **What is the expected reaction?** (positive surprise, negative surprise, in-line)
4. **What is the *consensus* expectation?** (so you know what's already priced in)
5. **What would a *positive surprise* look like, and how would the stock react?**
6. **What would a *negative surprise* look like, and how would the stock react?**

Without a clear catalyst and a clear theory of how the stock will react, the trade is a hope. With them, the trade has a defined *time horizon* and a defined *invalidation*.

## Stage 6: Risk/Reward Geometry

Before placing the trade, define:

- **Entry price** (or range)
- **Target price** (the catalyst-driven move)
- **Stop price** (the level at which the thesis is invalidated)
- **Risk/reward ratio** (target − entry) / (entry − stop)

ITPM teaches that *minimum acceptable R/R is 3:1*. A trade that risks $1 to make $1 is a coin flip even if you have skill; the win rate has to be high to compensate. A 3:1 trade only needs to be right 25% of the time to break even, and is profitable on small skill edges.

The geometry is *prior to* the size and structure decisions. If you can't draw a clean R/R chart, you don't have a tradeable view.

## Stage 7: Options Structuring

This is where ITPM diverges most sharply from retail trading. Instead of buying or selling stock outright, professional traders use options structures designed to:

1. **Match the time horizon** to the catalyst
2. **Match the directional view** (bullish, bearish, neutral)
3. **Match the volatility view** (vol expanding, vol contracting)
4. **Limit the maximum loss** to a defined dollar amount
5. **Optimize the cost** by using spreads instead of outright options

Common ITPM structures:

### Bull View, High Conviction, Defined Risk
- **Long call** at the strike near current price, expiration ~2 weeks past the catalyst
- Or: **Bull call spread** (long lower-strike call, short higher-strike call) — caps the upside but reduces cost
- Or: **Risk reversal** (long call, short put) — synthetic long with no premium, full upside

### Bull View, Lower Conviction
- **Bull put spread** (short higher-strike put, long lower-strike put) — collect premium, profit if stock stays above the higher strike
- Or: **Cash-secured put** at a level you'd happily own — get paid to wait

### Bear View, High Conviction, Defined Risk
- **Long put** or **bear put spread**
- **Risk reversal short** (short call, long put)

### Bear View, Lower Conviction
- **Bear call spread** — collect premium

### Neutral / Range-Bound View
- **Iron condor** — collect premium if stock stays in range
- **Iron butterfly** — same idea, narrower range, higher premium

The structure is chosen *after* the directional and timing view, not before. The view determines the structure; not the other way around.

### Structure Selection Matrix

Cross the directional view (rows) against the volatility view and conviction (columns) to pick a structure. This is the table the page exists to provide — the bridge from view to instrument:

| View ↓ / Conviction → | High conviction, defined risk | Lower conviction (income) | Vol view modifier |
|---|---|---|---|
| **Bullish** | [[bull-call-spread\|Long call]] or [[bull-call-spread]] | [[bull-put-spread\|Bull put spread]] or [[cash-secured-put\|cash-secured put]] | If vol cheap → long call; if vol rich → spread/sell put |
| **Bearish** | [[bear-put-spread\|Long put]] or bear put spread; [[risk-reversal\|short risk reversal]] | [[bear-call-spread\|Bear call spread]] | If vol cheap → long put; if vol rich → bear call spread |
| **Neutral / range** | — | [[iron-condor]] / [[iron-butterfly]] | Sell vol only when [[implied-volatility\|IV]] is elevated |
| **Synthetic long, no premium** | [[risk-reversal\|Risk reversal]] (long call + short put) | — | Best when skew makes puts rich |

Reading the table: a **bullish, high-conviction view in a low-IV environment** points to a long call (cheap vol, full upside, defined risk = premium). The **same directional view in a high-IV environment** points to a [[bull-call-spread]] or a [[bull-put-spread]] — you do not want to pay rich premium, so you cap upside or collect premium instead. The volatility view is the modifier that decides *long premium vs. short premium* once direction and conviction are set. See [[options-greeks]] for the Greeks each structure expresses (delta for direction, vega for the vol view, theta for time decay).

## Stage 8: Position Sizing

ITPM uses a strict per-trade risk budget, typically 1-2% of capital at risk per trade. The position is sized so that:

```
position_size × max_loss_per_share = 1-2% of capital
```

For options, the max loss is the entire premium paid (for long options) or the difference in strikes minus credit received (for spreads).

This is *risk-defined* sizing — the trader controls the maximum loss, regardless of whether the stop is hit, by structuring the position so that even total loss doesn't exceed the risk budget.

For options strategies, this is much cleaner than for outright stock trades. You know exactly what you can lose; the position size follows mechanically.

## Stage 9: Hedging

Individual trades are risky in isolation. The professional approach is to *combine* trades into a portfolio that hedges out unwanted risks:

- **Delta hedge** — combine long and short positions so net delta exposure is small
- **Sector hedge** — long the strong stock + short the weak stock in the same sector → market-neutral sector trade
- **Beta hedge** — short the index against the long book → market-neutral
- **Pair hedge** — long winner + short loser in same industry → idiosyncratic-only exposure
- **Vol hedge** — sell vol on positions where you have a directional view, reducing total premium cost

The hedging is *intentional*. It allows you to express a relative-value view ("Apple will outperform Samsung") without taking on the unrelated risk that the entire tech sector might collapse.

## Stage 10: Trade Management

Once the trade is on:

1. **Monitor the catalyst calendar** — make sure the catalyst is still scheduled
2. **Watch for thesis-invalidating news** — if the macro picture changes, exit
3. **Track relative strength** — if the long stock loses leadership, exit even before the catalyst
4. **Roll or close before expiration** — never let options expire in your face
5. **Take profits at targets** — pre-define profit-taking levels

The trade has an *exit plan* before it's entered. If the catalyst hits and the stock moves to target, take profit. If it hits and the stock fails to move (thesis wrong), exit. If it doesn't hit by expiration (timing wrong), exit.

## Stage 11: Exit

Three exit conditions:

1. **Profit target hit** — exit, no questions
2. **Stop hit** — exit, no questions
3. **Thesis invalidated** — exit even if stop not yet hit

The hardest of the three is #3. It requires the discipline to recognize that the *reason* for the trade is gone, even if the price hasn't yet moved enough to trigger the stop. ITPM emphasizes that the best traders exit on thesis invalidation, not on price.

## Common Mistakes

ITPM curriculum repeatedly emphasizes the most common retail mistakes:

1. **Trading without a top-down view** — picking individual setups in isolation
2. **No catalyst identification** — buying because "it looks cheap"
3. **Wrong timeframe options** — using weekly options for multi-week catalysts
4. **No defined R/R before entry** — sizing then hoping
5. **Outright stock instead of options** — paying full risk when defined-risk options achieve the same view
6. **No portfolio construction** — running individual trades instead of a hedged book
7. **Overtrading** — too many trades, too little research per trade
8. **No journaling** — repeating the same mistake without recognizing the pattern

## Worked Example: From Macro View to Sized Position

A single thesis traced through all eleven stages, to show how each output feeds the next. (Illustrative — generic numbers, not a recommendation.)

| Stage | Decision in this example |
|---|---|
| 1. Macro | Growth accelerating, central bank on hold, risk-on. Favor cyclicals/tech. |
| 2. Geo / asset class | Overweight US equities, long bias. Theme: "long US tech on dovish-hold + AI capex." |
| 3. Sector | Tech shows persistent positive relative strength → long-sector. Utilities lagging → short-sector. |
| 4. Stock | Within tech, pick the *strongest* RS name with rising estimates as the long; within utilities, the *weakest* deteriorating name as the short. |
| 5. Catalyst | Long name reports earnings in 3 weeks; consensus modest; whisper suggests upside surprise. Defined date + defined invalidation (a miss). |
| 6. R/R geometry | Entry at current price; target = catalyst-driven move (+12%); stop = thesis-invalidation level (−4%). R/R = 3:1, meets the minimum. |
| 7. Structure | Bullish, high conviction, IV not elevated → **long call** ~2 weeks past earnings. (Had IV been rich → [[bull-call-spread]].) |
| 8. Sizing | Max loss = premium paid. Size so premium = 1-2% of capital. Total loss is bounded and pre-budgeted. |
| 9. Hedging | Short the weak utility name (or short index beta) to neutralize market risk → expresses the *relative* tech-over-utilities view, not raw market exposure. |
| 10. Management | Confirm earnings date holds; watch for thesis-breaking macro news; track RS leadership; plan to roll/close before expiry. |
| 11. Exit | Earnings beat → take profit at target. Miss → exit on thesis invalidation, not on the stop alone. No move by expiry → close (timing wrong). |

The chain is unbroken: the macro view *created* the theme, the theme *created* the sector pair, the sector pair *created* the stock pair, the catalyst *created* the time horizon, the geometry *created* the R/R, the view *created* the structure, the structure *created* the clean max-loss, and the max-loss *created* the size. Remove any link and the trade degrades into a retail setup.

## Quick-Reference Pre-Trade Checklist

Run this before every entry. If any answer is "no," the trade is not ready.

- [ ] Do I have a defensible **macro view** this position is a child of?
- [ ] Is the stock in an **in-favor sector** (long) / out-of-favor sector (short)?
- [ ] Is this the **strongest** (long) / **weakest** (short) name in that sector?
- [ ] Is there a **dated catalyst** and a clear theory of the reaction?
- [ ] Have I drawn entry, target, stop, and is **R/R ≥ 3:1**?
- [ ] Does the **structure** match my directional *and* volatility view?
- [ ] Is max loss sized to **1-2% of capital**?
- [ ] Is unwanted **market/sector beta hedged** out?
- [ ] Do I have a written **exit plan** (target / stop / invalidation) before entry?

This checklist is the discretionary counterpart to the systematic [[research-checklist]]; both exist to force the same discipline — a reason before a position.

## How This Differs From Systematic Strategies

Systematic strategies (the rest of this wiki) start with a numerical signal and execute mechanically. ITPM-style discretionary trading starts with a *view* and constructs trades to express it. Both can be profitable; they require very different research processes.

A useful integration: use systematic methods to *generate candidates* (sector relative strength scans, fundamental screens, options unusual activity), then apply the discretionary trade-construction workflow to convert candidates into actual positions.

## What ITPM Adds to the Wiki

The wiki has many pages on individual options strategies — [[bull-call-spread]], [[iron-condor]], [[risk-reversal]], etc. — but no page on *how to choose between them*. This page is that bridge: it answers the question "given my view, which structure should I use, and how should I size it?"

## Sources

- [[anton-kreil]] — founder
- [[itpm-five-principles]] — Kreil's underlying framework
- [[itpm-ten-secrets]] — companion source
- [[itpm-education-methodology-overview]] — broader methodology context
- [[itpm-professional-traders-amazing-advice]]

## Related

- [[strategy-development-overview]]
- [[research-checklist]] — systematic counterpart to the pre-trade checklist
- [[edge-taxonomy]] — where the discretionary edge sits (analytical + informational)
- [[risk-management-overview]]
- [[options-greeks]]
- [[implied-volatility]] — the vol-view input to the structure matrix
- [[bull-call-spread]]
- [[bull-put-spread]]
- [[bear-put-spread]]
- [[bear-call-spread]]
- [[iron-condor]]
- [[iron-butterfly]]
- [[risk-reversal]]
- [[cash-secured-put]]
- [[covered-call]]
- [[wheel-strategy]]
- [[sector-rotation]]
- [[arbitrage-opportunity-map]] — cross-wiki view of where mispricings cluster
- [[asterdex-perp-trading-map]] · [[low-cap-crypto-trading-map]] — venue-specific companion maps
