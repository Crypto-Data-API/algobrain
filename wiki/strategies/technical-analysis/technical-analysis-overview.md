---
title: "Technical Analysis Strategies"
type: overview
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [technical-analysis, indicators, options, breakout]
aliases: ["TA Strategies"]
related: ["[[strategies-overview]]", "[[fundamental-analysis-overview]]", "[[swing-trading-overview]]", "[[day-trading-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[indicators-overview]]", "[[triple-screen-system]]"]
---

# Technical Analysis

Strategies based on chart patterns, technical indicators, and price-action analysis. Technical analysis assumes that all relevant information is reflected in price and volume, and that historical patterns tend to repeat because human psychology does not change. Whether or not one believes in pure TA, understanding support/resistance, trend structure, and indicator signals improves entries, exits, and risk management for any trading style.

## What Distinguishes This Family

- **Edge sources** — almost entirely *behavioral*: chart patterns persist because crowds anchor to round numbers and prior highs, chase trends late, and capitulate at extremes. A secondary *structural* component exists where self-fulfilling order flow clusters at widely watched levels (e.g. breakout points, moving averages). See [[edge-taxonomy]].
- **Typical timeframes** — the most flexible family in the catalog: the same setups apply from intraday charts ([[opening-range-breakout]]) through daily swing charts to weekly trend systems ([[turtle-trading]]).
- **Capital and data requirements** — the lowest barrier to entry of any family: OHLCV data and free charting tools suffice for the indicator and pattern strategies; the options structures additionally need an options chain and approval for spreads. Minimal capital is required, which is also why these edges are the most crowded and most decayed — cost discipline and selectivity matter more than the signal itself.
- **Who it suits** — discretionary traders who read charts well and apply strict risk control; also systematic traders who codify the rule-based subset (crossovers, channel breakouts). The options sub-catalog suits income-oriented traders who want defined-risk structures around technical levels.
- **Regime sensitivity** — trend tools fail in ranges, oscillators fail in trends. Classifying the regime first (see [[regime-matrix]] and [[regime-detection]]) is the single biggest performance lever for everything on this page.

This folder contains two sub-families: **chart/indicator strategies** (classical TA) and **options structures** that are typically deployed around technical levels and views.

> **See also:** the indicator *concepts* (how each tool is calculated and what it measures) live in the [[indicators-overview]] hub. This page catalogs the *strategies* built from those tools. For the methodology of combining tools across timeframes, see the flagship [[triple-screen-system|Triple Screen system]] and [[multi-timeframe-confluence]].

## How to Navigate This Hub

| If you want to... | Go to | Key pages |
|---|---|---|
| Ride a trend | Trend-Following & Crossover Systems | [[moving-average-crossover]], [[supertrend]], [[turtle-trading]] |
| Trade escapes from consolidation | Breakout Strategies | [[breakout-trading]], [[donchian-channel-breakout]], [[opening-range-breakout]] |
| Read structure / patterns | Classical Charting Theories | [[elliott-wave]], [[wyckoff-method]], [[fibonacci-trading]] |
| Follow institutional order flow | Order-Flow & Institutional | [[ict-methodology]], [[smart-money-concepts]] |
| Take a directional view with defined risk | Directional Spreads | [[vertical-spread]], [[bull-call-spread]], [[risk-reversal]] |
| Generate income / sell premium | Income & Premium Selling | [[wheel-strategy]], [[iron-condor]], [[covered-call]] |
| Trade volatility itself | Volatility & Multi-Leg | [[gamma-scalping]], [[volatility-arbitrage]], [[calendar-spread]] |
| Hedge an existing position | Hedging & Repair | [[protective-put]], [[collar]], stock-repair |
| Understand the *indicators* themselves | Concept hub | [[indicators-overview]], [[rsi]], [[macd]] |

## Match the Tool to the Regime

The single biggest performance lever (see [[regime-matrix]] and [[regime-detection]]) is using trend tools in trends and oscillator/mean-reversion tools in ranges. Mismatching is the most common way TA loses money.

| Regime | What works | What fails | Representative strategies |
|---|---|---|---|
| **Trending (strong)** | Trend-following, breakout, momentum | Oscillators (chronic overbought/oversold) | [[turtle-trading]], [[moving-average-crossover]], [[donchian-channel-breakout]] |
| **Range-bound / choppy** | Mean-reversion, support/resistance fades, premium selling | Breakouts (false), trend crossovers (whipsaw) | [[rsi-divergence]], [[iron-condor]], [[short-strangle]] |
| **High volatility / stress** | Defined-risk structures, long convexity, wider stops | Naked premium selling, tight stops | [[protective-put]], [[backspread]], [[vertical-spreads]] |
| **Low volatility / drift** | Premium selling, calendar spreads, theta harvest | Long premium (theta bleed) | [[calendar-spread]], [[wheel-strategy]], [[covered-call]] |

## Chart & Indicator Strategies

### Trend-Following & Crossover Systems

- [[moving-average-crossover]] — Simple, effective trend-following with SMA or EMA crossovers; the canonical starting point.
- [[macd-crossover]] — Trading momentum shifts when the MACD line crosses its signal line.
- [[supertrend]] — ATR-based trailing indicator that flips long/short with the trend.
- [[parabolic-sar]] — Time/price stop-and-reverse system for riding trends.
- [[ichimoku-cloud]] — A self-contained system giving trend, momentum, and support/resistance in one indicator.
- [[turtle-trading]] — The famous rules-based trend system taught by Dennis and Eckhardt.
- [[heikin-ashi]] — Smoothed candlesticks that filter noise to hold trends longer.
- [[renko-trading]] — Price-only brick charts that strip out time and noise.
- [[point-and-figure]] — Classical column-based charting for objective breakout targets.
- [[rate-of-change]] — Pure momentum oscillator strategies based on N-period price change.
- [[triple-screen-system]] — Elder's three-timeframe filter: trade with the higher-TF trend, enter on a pullback. (Lives in `wiki/strategies/`, not this folder.)

### Breakout Strategies

- [[breakout-trading]] — Core playbook for entering when price escapes consolidation.
- [[breakout-strategies]] — Survey of breakout variants, filters, and failure handling.
- [[support-resistance-breakout]] — Trading the break of well-tested horizontal levels.
- [[channel-breakout]] — Entries on escapes from trend channels.
- [[donchian-channel-breakout]] — Rule-based N-day high/low breakouts.
- [[volatility-breakout]] — Entering when range expansion exceeds a volatility threshold.
- [[opening-range-breakout]] — Trading the break of the first N minutes' range.
- [[london-breakout]] — FX session strategy trading the break of the pre-London range.
- [[darvas-box]] — Nicolas Darvas's box method for riding momentum stocks.

### Classical Charting Theories & Patterns

- [[elliott-wave]] — Wave-count framework for impulse and corrective market structure.
- [[fibonacci-trading]] — Retracement and extension levels for entries and targets.
- [[gann-theory]] — W.D. Gann's geometric price-time methods.
- [[harmonic-patterns]] — Fibonacci-ratio patterns (Gartley, Bat, Crab) for reversal zones.
- [[wyckoff-method]] — Accumulation/distribution phase analysis of institutional campaigns.
- [[supply-demand-zones]] — Trading fresh imbalance zones where institutions transacted.
- [[rsi-divergence]] — Spotting reversals where price and momentum disagree.

### Order-Flow & Institutional Concepts

- [[ict-methodology]] — Inner Circle Trader framework: liquidity pools, fair-value gaps, killzones.
- [[smart-money-concepts]] — Retail adaptation of institutional order-flow ideas (BOS, CHoCH, order blocks).

## Options Structures

### Directional Spreads

- [[vertical-spread]] — The building block: defined-risk directional spread across two strikes.
- [[vertical-spreads]] — Companion survey of the four vertical spread variants.
- [[bull-call-spread]] — Debit spread for a moderately bullish view.
- [[bull-put-spread]] — Credit spread profiting if price stays above the short put.
- [[bear-call-spread]] — Credit spread profiting if price stays below the short call.
- [[bear-put-spread]] — Debit spread for a moderately bearish view.
- [[ratio-spread]] — Unbalanced spread selling more options than bought for cheap directional exposure.
- [[backspread]] — Reverse ratio: long extra options for convex payoff on a big move.
- [[risk-reversal]] — Selling a put to finance a call (or vice versa) for synthetic direction.
- [[synthetic-long]] — Long call plus short put replicating stock exposure.

### Income & Premium Selling

- [[covered-call]] — Selling calls against stock holdings to generate income.
- [[cash-secured-put]] — Selling puts backed by cash, to earn premium or acquire stock cheaper.
- [[wheel-strategy]] — Cycling cash-secured puts into covered calls for continuous income.
- [[options-selling]] — General premium-selling playbook and its risk profile.
- [[short-straddle]] — Selling call and put at the same strike for maximum premium, undefined risk.
- [[short-strangle]] — Selling OTM call and put for a wider profit zone than the straddle.
- [[strangle]] — The long/short strangle structure across OTM strikes.
- [[straddle-strangle]] — Comparison of straddle vs strangle structures and when to use each.
- [[iron-condor]] — Defined-risk range-bound income from a put spread plus call spread.
- [[iron-butterfly]] — At-the-money short straddle with protective wings.
- [[iron-fly]] — Companion page on the iron butterfly's mechanics and management.
- [[jade-lizard]] — Short put plus short call spread with no upside risk.
- [[gut-spread]] — In-the-money strangle variant with intrinsic-value cushioning.

### Volatility & Multi-Leg Structures

- [[butterfly-spread]] — Three-strike structure for pinpoint price targets at low cost.
- [[broken-wing-butterfly]] — Skewed butterfly that removes risk on one side for a credit.
- [[christmas-tree-spread]] — Multi-strike ladder for directional moves with reduced cost.
- [[calendar-spread]] — Selling near-dated, buying far-dated options to harvest time decay.
- [[diagonal-spread]] — Calendar with different strikes for direction plus theta.
- [[double-diagonal]] — Two diagonals combined into a wide income tent.
- [[box-spread]] — Four-leg structure locking in a riskless interest-rate payoff.
- [[reverse-iron-condor]] — Buying the condor to profit from a large move either way.
- [[strip-strap]] — Skewed straddle variants biased bearish (strip) or bullish (strap).
- [[seagull-option]] — Three-leg FX-style structure financing protection with a sold wing.
- [[gamma-scalping]] — Dynamically hedging a long-gamma position to monetize realized volatility.
- [[volatility-arbitrage]] — Trading implied vs realized volatility mispricings.
- [[0dte-trading]] — Trading zero-days-to-expiry options on expiration day.
- [[options-strategies]] — Master index of option structures and when to deploy them.

### Hedging & Repair

- [[protective-put]] — Buying puts to insure a stock position.
- [[married-put]] — Buying stock and put together as a packaged insured position.
- [[collar]] — Financing put protection by selling a covered call.
- [[collar-strategy]] — Companion page on collar construction and management.

## All Pages (auto)

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/technical-analysis"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Comparisons

- [[technical-vs-fundamental-analysis]] — side-by-side comparison of technical and fundamental approaches.

## Coverage Gaps

Topics still lacking dedicated pages in this folder: classical chart patterns (head & shoulders, triangles, flags), candlestick patterns, trend lines and channels as a standalone topic, and volume analysis. Indicator fundamentals live in `wiki/concepts/indicators/` (e.g. [[rsi]], [[macd]]).

## Related

- [[strategies-overview]] — top-level strategy catalog
- [[fundamental-analysis-overview]] — the opposing analytical school
- [[swing-trading-overview]] — the timeframe where most TA setups are traded
- [[day-trading-overview]] — intraday application of TA tools
- [[quantitative-overview]] — systematic formalization of TA signals
- [[edge-taxonomy]] — why behavioral chart edges exist and decay
- [[regime-matrix]] — matching trend vs oscillator tools to market regime
- [[indicators-overview]] — the concept hub for the indicators these strategies use
- [[triple-screen-system]] — flagship multi-timeframe method combining trend + oscillator + trigger
- [[multi-timeframe-confluence]] — the general principle behind aligning timeframes
- [[volatility-trading]] — broader volatility strategy context for the options structures
