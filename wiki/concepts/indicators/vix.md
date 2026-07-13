---
title: "VIX (CBOE Volatility Index)"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [volatility, indicators, options, risk-management]
aliases: ["VIX", "CBOE Volatility Index", "Fear Index"]
related: ["[[implied-volatility]]", "[[volatility-trading]]", "[[options-greeks]]", "[[realized-volatility]]", "[[volatility-risk-premium]]", "[[sp500]]"]
domain: [volatility, risk-management]
difficulty: intermediate
---

The **VIX** (CBOE Volatility Index) is a real-time index that measures the market's expectation of 30-day forward-looking [[implied-volatility|volatility]] on the [[sp500|S&P 500 Index]]. Often called the "Fear Index," it is derived from the prices of S&P 500 index options and serves as the most widely followed barometer of investor sentiment and market risk in global finance.

## Overview

The VIX was introduced by the Chicago Board Options Exchange (CBOE) in 1993, originally based on S&P 100 options. In 2003, the methodology was updated to use S&P 500 options and a wider strike range, making it more representative of market-wide expectations. The index is calculated continuously during trading hours and quoted in annualized percentage points.

The VIX does not measure past volatility -- it measures *expected* volatility over the next 30 calendar days, as implied by [[options-pricing|options prices]]. When traders are willing to pay more for options (particularly [[put-options|puts]] for downside protection), the VIX rises. When demand for protection falls, the VIX declines.

## How It Works

The VIX is calculated using a model-free methodology that aggregates the weighted prices of out-of-the-money S&P 500 puts and calls across a wide range of strike prices. The key inputs are:

- **Near-term and next-term SPX options** expiring in approximately 23-37 days
- **Out-of-the-money puts and calls** across all available strikes
- **Weighted average** that emphasizes options closest to at-the-money

The formula produces a single number representing annualized expected volatility. A VIX of 20 implies the market expects the S&P 500 to move roughly 20% / sqrt(12) = ~5.8% over the next 30 days (one standard deviation).

**Interpreting VIX Levels:**

| VIX Range | Interpretation | Market Condition |
|-----------|---------------|------------------|
| Below 15 | Low volatility / complacency | Bull market, steady grind higher |
| 15-25 | Normal range | Typical market conditions |
| 25-35 | Elevated fear | Corrections, uncertainty |
| Above 40 | Crisis / panic | Crashes, systemic events |

Historical extremes include the 2008 financial crisis (VIX peaked near 80) and the March 2020 COVID crash (VIX hit 82.69). The long-run average sits around 19-20.

A critical property of the VIX is that it is **mean-reverting** -- spikes tend to be short-lived, and the index gravitates back toward its long-term average. This mean-reversion is the foundation of many [[volatility-trading]] strategies.

## Trading Applications

**Direct VIX Trading:** The VIX itself is not directly tradable, but several derivative products track it:

- **VIX Futures** -- trade on CBOE Futures Exchange; typically in [[contango]] (futures > spot), creating a persistent roll cost for long holders
- **VIX ETPs** -- products like VXX (short-term futures), UVXY (2x leveraged), and SVXY (inverse) provide access but suffer from contango decay over time
- **VIX Options** -- European-style options on the VIX index, popular for tail hedging

**Portfolio Hedging:** The VIX has a strong negative correlation with the S&P 500 (approximately -0.7 to -0.8). This makes VIX calls or VIX futures useful as portfolio hedges during [[market-crashes|market drawdowns]]. However, the persistent cost of carry from contango makes permanent VIX hedges expensive.

**Volatility Risk Premium Harvesting:** Because [[implied-volatility]] (as measured by the VIX) tends to exceed [[realized-volatility]] on average, systematic sellers of VIX-linked products or SPX options can harvest the [[volatility-risk-premium]]. This is the basis of many institutional options strategies.

**Regime Identification:** Traders use VIX levels and term structure (comparing near-term vs. longer-term VIX futures) to identify market regimes. A VIX term structure in [[backwardation]] (near-term > far-term) signals acute fear and often marks short-term bottoms.

## Related

- [[implied-volatility]] -- the broader concept the VIX measures
- [[realized-volatility]] -- actual observed vol, compared against VIX to gauge risk premium
- [[volatility-risk-premium]] -- the spread between IV and RV that the VIX helps quantify
- [[volatility-trading]] -- strategies built around trading volatility directly
- [[options-greeks]] -- sensitivity measures for options, especially [[vega]]
- [[contango]] -- the typical VIX futures term structure that erodes long positions

## Sources

- (Source: [[book-option-volatility-and-pricing]]) -- comprehensive treatment of volatility measures and VIX
- (Source: [[book-the-black-swan]]) -- Nassim Taleb's discussion of fat tails and the limitations of standard volatility measures
