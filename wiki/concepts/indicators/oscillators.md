---
title: "Oscillators"
type: concept
created: 2026-04-15
updated: 2026-07-19
status: good
tags: [indicators, technical-analysis, momentum, mean-reversion]
aliases: ["Oscillators", "Oscillator", "oscillator", "Technical Oscillator", "Momentum Oscillator"]
related: ["[[rsi]]", "[[macd]]", "[[stochastic]]", "[[cci]]", "[[williams-percent-r]]", "[[momentum]]", "[[indicators]]", "[[moving-averages]]", "[[divergence]]", "[[mean-reversion]]"]
domain: [indicators]
prerequisites: ["[[indicators]]", "[[momentum]]"]
difficulty: beginner
---

An oscillator is a class of technical indicator that fluctuates within a bounded (or centered) range, designed to measure the *momentum* or *velocity* of price rather than its absolute level. Because their values move back and forth between fixed extremes, oscillators are primarily used to identify **overbought** and **oversold** conditions, to flag momentum **[[divergence]]** against price, and to time entries in ranging or [[mean-reversion|mean-reverting]] markets.

## Overview

Oscillators fall into two structural families:

- **Bounded (range-bound) oscillators** swing between hard limits — typically 0–100. Examples: [[rsi|RSI]] (0–100), [[stochastic|Stochastic]] (0–100), [[williams-percent-r|Williams %R]] (−100 to 0). These have natural overbought/oversold thresholds (e.g. RSI > 70 / < 30).
- **Centered (unbounded) oscillators** oscillate around a zero or neutral line with no fixed ceiling. Examples: [[macd|MACD]], the rate-of-change (ROC), and [[cci|CCI]]. Signals come from zero-line crossovers and the relative magnitude of swings rather than absolute thresholds.

The common thread is that all oscillators are *derived from price* (and sometimes volume), which means they inherently **lag** raw price action. They trade timeliness for noise reduction and a normalized, comparable scale.

## How They Work

Most oscillators normalize recent price behavior into a standardized scale so that readings are comparable across instruments and timeframes. Representative formulas:

- **RSI** = 100 − [100 / (1 + RS)], where RS = average gain / average loss over *n* periods (default 14). Bounded 0–100.
- **Stochastic %K** = 100 × (Close − Lowest Low_n) / (Highest High_n − Lowest Low_n). Measures where the close sits within its recent range.
- **MACD** = EMA(12) − EMA(26), with a signal line = EMA(9) of the MACD. A centered oscillator; histogram = MACD − signal.
- **ROC** = 100 × (Price_t − Price_{t−n}) / Price_{t−n}. Pure rate-of-change, centered on zero.

### Core signal types

1. **Overbought / oversold** — the indicator pushes past a threshold (RSI > 70, Stochastic > 80), suggesting the move is overextended and prone to reversion.
2. **[[divergence|Divergence]]** — price makes a higher high while the oscillator makes a lower high (bearish divergence), signalling weakening momentum. The inverse is bullish divergence. This is generally considered the most valuable oscillator signal.
3. **Centerline / signal-line crossovers** — MACD crossing zero or its signal line; Stochastic %K crossing %D.
4. **Failure swings** — the oscillator fails to confirm a new price extreme and then breaks its prior pivot.

## Trading Relevance

Oscillators are most reliable in **ranging, sideways markets**, where price reverts between support and resistance and overbought/oversold thresholds line up with the range boundaries. Their classic failure mode is the **trending market**: a strong uptrend will keep RSI pinned above 70 for weeks, generating a stream of premature "sell" signals. The practitioner's rule of thumb is therefore to use oscillators for *timing within a regime*, not for picking tops and bottoms against a trend — pair them with a trend filter (e.g. price relative to a [[moving-averages|moving average]]) so overbought signals are only acted on in a confirmed downtrend and oversold signals only in an uptrend.

Divergence is the one oscillator signal that retains value in trending conditions, because it can flag exhaustion before price confirms. Many traders combine a centered oscillator ([[macd|MACD]]) to read trend momentum with a bounded one ([[rsi|RSI]] or [[stochastic|Stochastic]]) to time the pullback entry. Because all oscillators are price-derived and correlated, stacking several of the same type adds little — the common mistake is "indicator soup," where three oscillators that say the same thing create a false sense of confirmation.

## Common Oscillators

| Oscillator | Type | Range | Primary use |
|---|---|---|---|
| [[rsi\|RSI]] | Bounded | 0–100 | Overbought/oversold, divergence |
| [[stochastic\|Stochastic]] | Bounded | 0–100 | Range entries, %K/%D crossovers |
| [[williams-percent-r\|Williams %R]] | Bounded | −100–0 | Overbought/oversold (fast) |
| [[macd\|MACD]] | Centered | Unbounded | Trend momentum, crossovers |
| [[cci\|CCI]] | Centered | Unbounded (±100 typical) | Cyclical turns, divergence |
| Rate of Change (ROC) | Centered | Unbounded | Raw momentum |

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/indicators/technical` — universe-wide price-structure state including the RSI component (Pro+), the pre-computed bounded-oscillator read
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200` — OHLCV for computing any oscillator in the table above (RSI, Stochastic, MACD, ROC, CCI)

**Historical data:**
- `GET /api/v1/indicators/technical/{symbol}` — per-asset state with a rolling 60-day history (Pro+)
- `GET /api/v1/backtesting/klines` — full kline archive (Binance spot 1h/4h/1d back to 2017-08) for threshold and divergence backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/technical"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-indicators]].

**Live dashboards:** [technical structure](https://cryptodataapi.com/technical-structure) · [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — `GET /api/v1/indicators/technical` (Pro+) screens the whole universe for stretched RSI states in one call; anything beyond RSI derives locally from `GET /api/v1/market-data/klines`
- **Regime pairing** — the page's core rule is executable: gate oscillator fades with `GET /api/v1/indicators/signum-rgg` (ADX/DMI RED/GREY/GREEN, Pro+) so overbought/oversold signals fire only in GREY chop, never against a GREEN/RED trend
- **Backtest** — replay thresholds and divergences over `GET /api/v1/backtesting/klines` (1h/4h/1d back to 2017-08); measure the pinned-oscillator failure mode explicitly by segmenting results by trend state
- **Tip** — avoid indicator soup: bounded oscillators computed from the same closes are highly correlated, so backtest one bounded plus one centered oscillator rather than stacking three near-duplicates

## Sources

- John J. Murphy, *Technical Analysis of the Financial Markets* (1999) — chapters on momentum oscillators and divergence.
- J. Welles Wilder, *New Concepts in Technical Trading Systems* (1978) — original definition of RSI and the oscillator-as-momentum framework.
- Martin Pring, *Technical Analysis Explained* — taxonomy of bounded vs. centered oscillators.

## Related

- [[rsi]]
- [[macd]]
- [[stochastic]]
- [[cci]]
- [[williams-percent-r]]
- [[momentum]]
- [[divergence]]
- [[mean-reversion]]
- [[moving-averages]]
- [[indicators]]
