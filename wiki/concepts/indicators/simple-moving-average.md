---
title: "Simple Moving Average"
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [technical-analysis, indicators, trend-following]
aliases: ["SMA"]
related: ["[[exponential-moving-average]]", "[[moving-averages]]", "[[trend-following]]", "[[macd]]", "[[bollinger-bands]]", "[[support-and-resistance]]"]
domain: [technical-analysis]
difficulty: beginner
---

The Simple Moving Average (SMA) is the arithmetic mean of closing prices over a specified number of periods. It assigns equal weight to every price in the lookback window and is the most fundamental [[indicators|indicator]] in [[technical-analysis]]. By smoothing out short-term price fluctuations, the SMA reveals the underlying [[trend]] direction and provides dynamic [[support-and-resistance]] levels.

## Overview

The SMA is calculated as:

**SMA(N) = (P1 + P2 + ... + PN) / N**

Where P1 through PN are the closing prices of the last N periods and N is the lookback length. Each new period, the oldest price drops off and the newest price is added, causing the average to "move" with the market.

Common SMA periods and their uses:
- **20-period SMA** -- short-term trend; often the centerline of [[bollinger-bands]]
- **50-period SMA** -- medium-term trend; widely watched by institutional traders
- **100-period SMA** -- intermediate-term trend filter
- **200-period SMA** -- long-term trend; the most watched moving average on Wall Street. Stocks above their 200-SMA are generally considered in an uptrend; below, in a downtrend.

The SMA's strength is its simplicity and wide adoption. Because so many traders watch the same levels (especially the 50 and 200 SMAs), these averages often become self-fulfilling [[support-and-resistance]] zones -- price tends to react at these levels because participants expect it to.

## How It Works

### Trend Identification

The most basic use of the SMA is determining trend direction:
- **Price above SMA** -- bullish bias; the trend is up
- **Price below SMA** -- bearish bias; the trend is down
- **SMA slope** -- rising SMA confirms uptrend; falling SMA confirms downtrend; flat SMA indicates consolidation

Using multiple SMAs of different periods provides a layered view. In a healthy uptrend, shorter SMAs are above longer SMAs (e.g., 20 > 50 > 200), and the price is above all of them.

### Crossover Signals

When a shorter-period SMA crosses above a longer-period SMA, it generates a bullish signal (and vice versa):

- **Golden Cross** -- 50-SMA crosses above the 200-SMA. Widely regarded as a major long-term bullish signal. Historically, it has preceded significant rallies in equity indices.
- **Death Cross** -- 50-SMA crosses below the 200-SMA. The bearish counterpart. Signals potential long-term downtrend.

Crossover strategies are inherently lagging -- by the time the cross occurs, a meaningful portion of the move has already happened. This is the tradeoff for reliability: fewer false signals but later entries.

### Dynamic Support and Resistance

In trending markets, the SMA often acts as a moving floor (support in uptrends) or ceiling (resistance in downtrends). Traders use pullbacks to the SMA as entry opportunities:
- In an uptrend, buy when price pulls back to the 20 or 50 SMA and bounces
- In a downtrend, sell/short when price rallies up to the 20 or 50 SMA and reverses

### SMA vs. EMA

Compared to the [[exponential-moving-average|EMA]], the SMA:
- **Lags more** -- equal weighting means old prices have the same influence as recent ones
- **Is smoother** -- less reactive to price spikes, which reduces whipsaws
- **Gives equal importance to all periods** -- can be an advantage (stability) or disadvantage (slow to react)
- Is preferred for longer-term analysis (200-period), while the EMA is often preferred for shorter-term and momentum-based strategies

See [[moving-averages]] for a comprehensive comparison of moving average types.

## Trading Applications

### Trend Filter
Use the 200-SMA as a binary filter: only take long trades when price is above the 200-SMA, and only short trades when below. This single rule eliminates a large number of losing trades in trend-following systems.

### Moving Average Envelope
Plot bands at a fixed percentage above and below the SMA (e.g., +/- 3%). Price reaching the upper band in an uptrend may indicate overextension; touching the lower band may signal a buying opportunity. A simpler precursor to [[bollinger-bands]].

### Multiple Moving Average Systems
- **Dual MA crossover** -- trade when a fast SMA crosses a slow SMA (e.g., 10/50)
- **Triple MA** -- use three SMAs (e.g., 4/9/18) for entry, confirmation, and exit signals
- **Ribbon** -- plot many SMAs close together (e.g., 10 through 50 in steps of 5) to visualize trend strength; when the ribbon is fanned out, the trend is strong

### Limitations
- **Lagging indicator** -- by definition, the SMA reacts after the fact
- **Whipsaws in ranging markets** -- crossover signals produce frequent false signals when price moves sideways
- **Equal weighting** -- a sharp price change N periods ago affects the SMA just as much as today's price, which can produce counterintuitive jumps when the old price drops out of the window

## Related

- [[exponential-moving-average]] -- variant that weights recent prices more heavily
- [[moving-averages]] -- overview of all moving average types
- [[bollinger-bands]] -- volatility bands built around a 20-SMA
- [[macd]] -- indicator derived from the difference between two EMAs
- [[trend-following]] -- strategy category that relies heavily on moving averages
- [[support-and-resistance]] -- dynamic S/R provided by moving averages
- [[sma-vs-ema]] -- detailed comparison of the SMA and EMA

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- comprehensive treatment of moving averages and their applications
