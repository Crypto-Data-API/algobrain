---
title: MACD (Moving Average Convergence Divergence)
type: concept
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [macd, indicators, technical-analysis]
aliases: [MACD, "MACD Histogram", "Macd Histogram"]
domain: [indicators]
prerequisites: ["[[moving-averages]]", "[[momentum]]"]
difficulty: beginner
related:
  - "[[cryptodataapi]]"
  - "[[moving-averages]]"
  - "[[momentum]]"
  - "[[rsi]]"
  - "[[volume]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
  - "[[john-murphy]]"
  - "[[gerald-appel]]"
  - "[[commodities]]"
  - "[[crude-oil]]"
  - "[[gold]]"
  - "[[intermarket-analysis]]"
  - "[[technical-analysis-of-the-financial-markets]]"
  - "[[trend-following-cta]]"
  - "[[vwap]]"
---

# MACD (Moving Average Convergence Divergence)

MACD is a trend-following momentum indicator that shows the relationship between two exponential [[moving-averages]] of an asset's price.

## Overview

Developed by Gerald Appel in the late 1970s, MACD is one of the most widely used technical indicators (Source: [[book-technical-analysis-of-the-financial-markets]]). It captures both trend direction and momentum in a single tool, making it valuable for identifying trend changes and gauging the strength of moves.

## How It Works

- **MACD line**: 12-period EMA minus 26-period EMA. When positive, the short-term trend is above the long-term trend (bullish); when negative, it is below (bearish).
- **Signal line**: 9-period EMA of the MACD line. Acts as a trigger for buy/sell signals.
- **Histogram**: MACD line minus signal line. Visualizes the distance between the two lines -- expanding histogram bars indicate accelerating momentum, contracting bars indicate decelerating momentum.

## Key Signals

- **Bullish crossover**: MACD line crosses above the signal line. Suggests upward momentum is building.
- **Bearish crossover**: MACD line crosses below the signal line. Suggests downward momentum is building.
- **Zero-line crossover**: MACD crossing above zero confirms the short-term trend has overtaken the long-term trend (bullish); crossing below confirms bearish dominance.
- **Divergence**: Price makes a new high/low but MACD does not -- a warning of potential trend reversal, similar to [[rsi]] divergence.

## Trading Relevance

MACD works best in trending markets and generates whipsaws during ranging conditions. Many traders combine MACD with [[rsi]] for confirmation -- for instance, entering when MACD gives a bullish crossover and RSI is rising from oversold. The histogram is particularly useful for spotting momentum shifts before the actual crossover occurs. Adjusting the default 12/26/9 parameters to faster or slower settings can tailor the indicator to different trading styles.

## MACD Histogram

The MACD histogram, popularized by Thomas Aspray in 1986, represents the difference between the MACD line and its signal line. While MACD crossovers are the most commonly cited signals, the histogram often provides earlier warnings of momentum shifts (Source: [[book-technical-analysis-of-the-financial-markets]]).

Key histogram principles:

- **Histogram turning down from a high level** is often the earliest signal of a momentum shift, occurring before the actual MACD/signal line crossover. This gives traders an advance warning to tighten stops or reduce position size.
- **Histogram crossing the zero line** is equivalent to the MACD/signal line crossover -- but the histogram's visual representation makes it easier to spot the rate of change.
- **Histogram divergence** -- when price makes a new high but the histogram makes a lower high -- is one of the most reliable signals in technical analysis. It indicates that while price is still advancing, the rate of momentum gain is slowing.
- **Successive histogram peaks of diminishing height** during an uptrend are a warning that the trend is losing steam, even if MACD itself remains positive and above its signal line.

## Commodity Applications

MACD works well across energy and metals markets, where trends tend to be persistent and driven by fundamental supply/demand imbalances (Source: [[book-technical-analysis-of-the-financial-markets]]). The weekly MACD on [[crude-oil]] and [[gold]] is one of the most-watched signals among CTAs and commodity fund managers. Because these markets trend more reliably than equities, MACD's trend-following nature is particularly well-suited to them.

MACD histogram divergence is particularly effective in [[commodities|commodity markets]] because:

- Commodity trends are often driven by identifiable fundamental catalysts (supply disruptions, weather, policy changes), so momentum exhaustion visible in the histogram frequently precedes actual fundamental shifts in market perception.
- Weekly MACD crossovers on [[gold]], [[crude-oil]], [[copper]], and [[natural-gas]] are tracked by [[trend-following-cta|CTA funds]] as systematic entry/exit triggers.
- The MACD zero-line crossover on monthly charts of commodity indices serves as a regime filter -- above zero favors long-only commodity exposure, below zero favors reduced allocation or outright shorts.

## Best-Practice Combinations

**[[vwap|VWAP]] + MACD** is a popular intraday stack: VWAP provides institutional bias (price above VWAP = bullish context), while MACD confirms momentum direction. This combination is particularly effective in equities and crypto day trading (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study across US equities reported MACD with a 40.1% win rate. While this appears low, MACD is a trend-following indicator — it generates most of its P&L from a few large winners, not frequent small gains. The low win rate is offset by a favourable payoff ratio when used in trending markets (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## About the Creator

[[gerald-appel|Gerald Appel]] developed MACD in the late 1970s. It remains a staple in TradingView's built-in toolkit and virtually every charting platform (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Sources

- Gerald Appel, *Technical Analysis: Power Tools for Active Investors* (FT Prentice Hall, 2005) — Appel's own treatment of the MACD he created.
- Thomas Aspray, "Fine-Tuning the MACD" (*Technical Analysis of Stocks & Commodities*, 1988) — introduced the MACD histogram and divergence techniques.
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — covers MACD construction, signal interpretation, and divergence.
- [[book-technical-analysis-of-the-financial-markets]] -- Murphy covers MACD construction, signal interpretation, histogram analysis, and divergence techniques in detail
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Win-rate data, VWAP+MACD combination, cross-market applicability

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/indicators/technical` — price-structure state (SMA/BB/RSI) across assets
- `GET /api/v1/indicators/signum-rgg` — ADX(14)+DMI RED/GREY/GREEN state

**Historical data:**
- `GET /api/v1/indicators/technical/{symbol}` — per-asset detail + 60d history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — raw OHLCV for computing your own

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/indicators/technical"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-indicators]].

**Live dashboards:** [technical structure](https://cryptodataapi.com/technical-structure) · [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — MACD is not pre-computed server-side; derive EMA(12) − EMA(26), the 9-period signal line, and the histogram from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` (or `GET /api/v1/hyperliquid/candles` for perps). Seed the EMAs with well over 26 warm-up bars so early values are stable
- **Trend gate** — `GET /api/v1/indicators/signum-rgg` (ADX/DMI RED/GREY/GREEN, Pro+) filters out the ranging conditions where MACD whipsaws; take crossovers only when the colour agrees with the signal direction
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) supports multi-cycle crossover, zero-line, and histogram-divergence studies; expect trend-following economics (≈40% win rates carried by payoff ratio)
- **Tip** — histogram peaks of diminishing height are the earliest momentum-exhaustion tell; encode this as "n-th histogram peak lower than (n−1)-th while MACD > 0" rather than eyeballing divergence

## Related

- [[moving-averages]] -- MACD is derived from EMAs
- [[momentum]] -- MACD measures momentum shifts
- [[rsi]] -- commonly paired with MACD for confirmation
- [[macd-vs-rsi]] -- comparison of MACD and RSI for signal confirmation
- [[commodities]] -- MACD widely used across commodity futures
- [[crude-oil]] -- weekly MACD is a key CTA signal for oil
- [[gold]] -- weekly MACD crossovers are widely watched
- [[trend-following-cta]] -- CTAs use MACD as a core systematic signal
- [[intermarket-analysis]] -- MACD applied across related markets in Murphy's framework
- [[john-murphy]] -- covers MACD as a central indicator in his analytical toolkit
