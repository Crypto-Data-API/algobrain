---
title: Momentum
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [momentum, indicators, technical-analysis, behavioral-finance]
aliases: ["momentum-investing", "price momentum"]
domain: [indicators, behavioral-finance]
prerequisites: ["[[moving-averages]]", "[[trend]]"]
difficulty: beginner
related:
  - "[[rsi]]"
  - "[[macd]]"
  - "[[moving-averages]]"
  - "[[volume]]"
  - "[[momentum-anomaly]]"
  - "[[momentum-factor]]"
  - "[[momentum-investing]]"
  - "[[time-series-momentum]]"
  - "[[trend-following]]"
---

# Momentum

Momentum is the empirical tendency of an asset's price to continue moving in the same direction over intermediate horizons — assets that have been rising tend to keep rising, and those falling tend to keep falling. It is both a measurable property of price (captured by oscillators like [[rsi]] and [[macd]]) and one of the most robust return factors in finance (the [[momentum-anomaly|momentum anomaly]]).

## Overview

Momentum operates across two distinct but related domains:

1. **As an indicator** — the rate and direction of recent price change. Momentum oscillators measure how fast price is moving and whether that speed is increasing or decreasing, helping traders gauge trend strength and spot exhaustion via [[divergence]].
2. **As a factor** — a cross-sectional and time-series return premium. Buying recent winners and selling recent losers has produced positive risk-adjusted returns across asset classes and across more than a century of data (see [[momentum-anomaly]], [[momentum-factor]]).

The factor was formalized academically by Jegadeesh and Titman (1993), who showed that ranking US stocks on trailing 3-12 month returns and going long the winners / short the losers earned roughly 1% per month. The effect has since been confirmed in equities globally, currencies, commodities, bonds, and crypto (Asness, Moskowitz, Pedersen 2013).

## How It Works

### Two forms of the factor

- **Time-series (absolute) momentum**: An asset's *own* past returns predict its future returns. If an asset rose over the past 6-12 months, it is statistically more likely to keep rising. This is the basis of [[trend-following|trend-following]] CTAs (Moskowitz, Ooi, Pedersen 2012). See [[time-series-momentum]].
- **Cross-sectional (relative) momentum**: *Relative* performance matters. Assets that outperformed their peers tend to continue outperforming. This is the classic Jegadeesh-Titman long-short construction.

### The lookback structure

The canonical academic specification is **"12-1" momentum**: rank on the trailing 12-month return while *skipping the most recent month*. The skip avoids short-term reversal — over a 1-month horizon, prices mean-revert rather than trend, so including the most recent month contaminates the signal. Beyond ~18 months, returns reverse (long-term reversal / the value effect).

### Momentum indicators

Traders quantify momentum with several tools:

- **[[rsi]] (Relative Strength Index)**: speed and magnitude of recent gains vs. losses on a 0-100 scale; flags overbought/oversold.
- **[[macd]]**: tracks the relationship between two [[moving-averages]], signaling momentum shifts via crossovers and histogram.
- **Rate of Change (ROC)**: simple percentage change over a fixed lookback — the most direct momentum measure.
- **Stochastic oscillator**: position of close within the recent high-low range.
- **[[volume]]**: rising price on rising volume confirms momentum; rising price on falling volume warns of weakening conviction.

## Why It Exists

The dominant explanation is **behavioral** (see [[behavioral-finance]]): investors underreact to news, anchor on past prices, and exhibit the disposition effect (selling winners too early, holding losers too long). Information diffuses slowly, so prices drift toward fair value over weeks-to-months rather than instantly. A secondary explanation is **risk-bearing** — momentum carries severe crash risk (the negatively skewed "momentum crash" tail), and part of the premium compensates holders for bearing it. See [[momentum-anomaly]] for the full mechanism discussion.

## Trading Relevance

Momentum strategies range from simple trend-following (buy above the 200-day [[moving-averages|MA]], sell below) to sophisticated quantitative factor models like the MTUM ETF. The single defining risk is the **momentum crash** — sudden, violent reversals where crowded momentum trades unwind, typically when a beaten-down market rebounds sharply (1932, August 2009, the November 2020 vaccine rotation, the August 2024 mega-cap unwind). Practitioners mitigate this by scaling exposure inversely to realized volatility (Barroso-Santa-Clara 2015) and de-risking in bear-market-plus-high-vol regimes (Daniel-Moskowitz 2016). Combining momentum signals with [[volume]] confirmation and risk controls like [[stop-loss]] orders helps manage the tail.

## Sources

- Jegadeesh, N. and Titman, S. (1993). "Returns to Buying Winners and Selling Losers." *Journal of Finance* 48 (1).
- Asness, C., Moskowitz, T., Pedersen, L. H. (2013). "Value and Momentum Everywhere." *Journal of Finance* 68 (3).
- Moskowitz, T., Ooi, Y. H., Pedersen, L. H. (2012). "Time Series Momentum." *Journal of Financial Economics* 104 (2).
- Daniel, K. and Moskowitz, T. (2016). "Momentum Crashes." *Journal of Financial Economics* 122 (2).

## Related

- [[rsi]] -- primary momentum oscillator
- [[macd]] -- momentum crossover indicator
- [[moving-averages]] -- foundation of trend-following momentum
- [[volume]] -- confirms or contradicts momentum signals
- [[momentum-anomaly]] -- the cross-sectional factor and its mechanism
- [[momentum-factor]] -- factor-investing treatment
- [[momentum-investing]] -- the systematic trading strategy
- [[time-series-momentum]] -- own-asset momentum / trend-following cousin
