---
title: Volatility
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [volatility, indicators, risk-management, derivatives]
aliases: [vol, volatility-trading]
domain: [indicators, risk-management]
prerequisites: ["[[standard-deviation]]", "[[options]]"]
difficulty: beginner
related:
  - "[[atr]]"
  - "[[bollinger-bands]]"
  - "[[options]]"
  - "[[position-sizing]]"
  - "[[implied-volatility]]"
  - "[[realized-volatility]]"
  - "[[vix]]"
  - "[[vol-of-vol]]"
  - "[[volatility-risk-premium]]"
---

# Volatility

Volatility is a statistical measure of the dispersion of returns for an asset, indicating how much and how quickly its price fluctuates. It is conventionally quantified as the annualized standard deviation of an asset's returns and is the single most important input to options pricing, risk management, and position sizing.

## Overview

High volatility means large price swings; low volatility means relatively stable prices. Volatility is central to risk management, options pricing, and position sizing. It is neither inherently good nor bad -- it represents opportunity and risk in equal measure.

A key empirical property is that volatility **clusters**: large moves tend to follow large moves and calm follows calm (the foundation of the ARCH/GARCH model family). It is also **mean-reverting** over the medium term and tends to spike sharply but decay slowly — volatility "takes the stairs up and the elevator down" is inverted relative to price, since fear (rising vol) arrives suddenly while complacency (falling vol) returns gradually.

## How It Is Measured

**Annualized standard deviation.** The textbook definition. Compute the standard deviation of periodic (e.g., daily) log returns and scale by the square root of the number of periods in a year:

```
σ_daily = stdev( ln(P_t / P_{t-1}) )
σ_annual = σ_daily × √252        (252 trading days per year)
```

The √time scaling assumes returns are independent and identically distributed — an approximation that breaks down under volatility clustering and fat tails, but a serviceable first pass.

**Other estimators** improve on close-to-close stdev by using intraday range data: Parkinson (high-low), Garman-Klass (OHLC), and Yang-Zhang (handles overnight gaps). These are more efficient because they extract information thrown away by close-only methods.

## Key Details

### Historical vs Implied Volatility

- **Historical (realized) volatility**: Calculated from past price data, typically as the standard deviation of returns over a set period (e.g., 30 days).
- **Implied volatility (IV)**: Derived from [[options]] prices. Reflects the market's forward-looking expectation of future volatility. When IV is high, options are expensive.

### Key Volatility Measures

- **VIX**: The CBOE Volatility Index, derived from S&P 500 options. Often called the "fear gauge." Readings above 30 indicate elevated fear; below 15 indicates complacency.
- **[[atr]] (Average True Range)**: Measures the average range of price bars over a period. Used for [[stop-loss]] placement and [[position-sizing]].
- **[[bollinger-bands|Bollinger Bands]]**: Plots standard deviation bands around a [[moving-averages|moving average]], visually displaying volatility expansion and contraction.

## Trading Relevance

Volatility drives opportunity -- trending markets require volatility to produce profits. Traders use volatility to size positions (smaller in high vol, larger in low vol), set stop distances, and identify breakout conditions. The "volatility squeeze" pattern (contracting [[bollinger-bands]]) often precedes large moves.

## Volatility in Professional Portfolio Management

[[chris-quill]] of [[itpm]] teaches a systematic approach to calculating and applying volatility:

- **Realized vs implied volatility comparison**: When implied volatility is higher than realized, options are "expensive" (favors selling); when lower, options are "cheap" (favors buying)
- **Volatility as a timing signal**: The [[eighty-twenty-analysis|80/20 volatility rule]] suggests only ~20% of the time offers enough volatility for active directional trading; the other 80% is for portfolio management
- **VIX trading**: [[raj-malhotra]] specializes in trading volatility directly through VIX-linked products as part of [[long-short-equity]] portfolio construction

## Related

- [[atr]] -- core volatility measurement tool
- [[bollinger-bands]] -- visual volatility indicator
- [[options]] -- priced using implied volatility
- [[position-sizing]] -- scaled to volatility
- [[long-short-equity]] -- portfolio framework leveraging volatility through options
- [[eighty-twenty-analysis]] -- the 80/20 volatility rule
- [[implied-volatility]] -- forward-looking, options-derived volatility
- [[realized-volatility]] -- backward-looking, return-derived volatility
- [[vix]] -- the benchmark equity volatility index
- [[vol-of-vol]] -- the volatility of volatility itself
- [[volatility-risk-premium]] -- the structural gap between implied and realized vol

## Sources

- Hull, J. — *Options, Futures, and Other Derivatives* (standard treatment of volatility estimation and its role in option pricing)
- Natenberg, S. — *Option Volatility and Pricing* (realized vs implied volatility, volatility trading)
- Sinclair, E. — *Volatility Trading* (estimators, forecasting, and the volatility risk premium)
- Engle, R. — "Autoregressive Conditional Heteroskedasticity" (1982), the origin of volatility clustering models (Nobel 2003)
