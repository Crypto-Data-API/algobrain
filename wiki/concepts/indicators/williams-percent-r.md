---
title: "Williams %R"
type: concept
created: 2026-04-20
updated: 2026-07-19
status: excellent
tags: [indicators, technical-analysis, momentum, mean-reversion]
aliases: ["Williams Percent R", "Williams %R", "%R", "Williams R"]
domain: [indicators]
prerequisites: ["[[momentum]]", "[[oscillators]]"]
difficulty: beginner
related: ["[[larry-williams]]", "[[stochastic]]", "[[rsi]]", "[[momentum]]", "[[oscillator]]", "[[overbought]]", "[[oversold]]", "[[divergence]]", "[[technical-analysis]]", "[[mean-reversion]]", "[[trend]]", "[[confluence]]"]
---

Williams %R is a momentum oscillator created by [[larry-williams|Larry Williams]] in 1973. It measures where the current close sits relative to the highest high over a lookback period, producing values from 0 to −100. It is essentially an inverted mirror image of the [[stochastic|Stochastic Oscillator]]'s %K line — where %K reads 0-100, %R reads 0 to −100 over the same range, so the two carry the same information on different scales (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Overview

Williams %R answers a single question: where does today's close fall within the high-low trading range of the last *n* periods? A reading of 0 means the close is at the very top of the range (maximum bullish momentum); −100 means the close is at the very bottom (maximum bearish momentum). Because it is bounded and normalized to the recent range, it is a **mean-reversion** tool best suited to range-bound markets, and like all overbought/oversold oscillators it gives premature signals in strong [[trend|trends]] (it can sit pinned near 0 throughout a sustained rally). Traders frequently pair it with a trend filter (e.g. a longer [[moving-averages|moving average]]) to suppress counter-trend signals.

## How It Works

```
%R = (Highest High − Close) / (Highest High − Lowest Low) × −100
```

where Highest High and Lowest Low are the extremes over the lookback period (default **14**).

- **Overbought** ([[overbought]]): readings near 0 (typically above −20) — close sits near the top of the recent range.
- **Oversold** ([[oversold]]): readings near −100 (typically below −80) — close sits near the bottom of the recent range.
- **Scale**: bounded between **0** (strongest) and **−100** (weakest); it can never leave that band.

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

### Step-by-Step Worked Example

Suppose over the last 14 days a stock's **highest high = $120**, its **lowest low = $100**, and today's **close = $116**.

```
%R = (120 − 116) / (120 − 100) × −100
   = (4 / 20) × −100
   = 0.20 × −100
   = −20
```

A reading of **−20** sits right at the overbought threshold — the close is in the top 20% of the 14-day range, signalling strong upside momentum but a stretched, possibly mean-reverting condition.

Two contrasting closes on the same range:

| Close | Calculation | %R | Zone |
|-------|-------------|-----|------|
| $119 | (120−119)/20 × −100 | **−5** | Deep overbought (near 0) |
| $116 | (120−116)/20 × −100 | **−20** | Overbought threshold |
| $110 | (120−110)/20 × −100 | **−50** | Mid-range / neutral |
| $103 | (120−103)/20 × −100 | **−85** | Oversold |
| $100 | (120−100)/20 × −100 | **−100** | Maximum oversold (range low) |

### Relationship to the Stochastic Oscillator

%R is an inverted [[stochastic|Stochastic %K]] on the same lookback. The conversion is exact:

```
%R = %K − 100        (equivalently  %K = %R + 100)
```

So a %R of −20 is the same information as a Stochastic %K of 80 — identical signal, flipped sign and shifted scale.

## Key Signals

- Readings crossing above −80 from below suggest bullish momentum
- Readings crossing below −20 from above suggest bearish momentum
- Divergences between %R and price warn of potential reversals

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

| Signal | Pattern | Interpretation |
|--------|---------|----------------|
| Oversold reversal | %R was below −80, then crosses back **above** −80 | Bounce / long candidate in a range |
| Overbought reversal | %R was above −20, then crosses back **below** −20 | Pullback / short candidate in a range |
| Bullish [[divergence]] | Price lower low, %R higher low | Selling pressure fading — potential bottom |
| Bearish [[divergence]] | Price higher high, %R lower high | Buying pressure fading — potential top |
| Momentum / "failure swing" | %R holds above −20 (or below −80) for many bars | A *trending* market, not a reversal — see pitfalls |

## How Traders Use It

- **Mean-reversion in ranges.** The classic use: fade extremes inside a [[consolidation]] — buy when %R turns up from below −80, sell when it turns down from above −20, with a [[stop-loss|stop]] just beyond the recent range extreme.
- **Trend filter, not standalone trigger.** Because it pins at extremes during strong [[trend|trends]], pair it with a longer [[moving-averages|moving average]]: in an uptrend, only take *oversold* (long) signals and ignore overbought ones, and vice versa.
- **Pullback timing within a trend.** In an established uptrend, a dip into oversold (%R < −80) that then turns up flags a buy-the-dip entry aligned with the trend rather than a counter-trend fade.
- **Divergence for reversals.** A new price high unconfirmed by %R (bearish [[divergence]]) is an early warning, best used with [[confluence]] from [[support]]/[[resistance]] or volume.
- **Settings.** A 14-period default is most common; shorter (e.g. 5–10) makes it twitchier for active trading, longer (e.g. 28) smooths it for swing horizons.

## Backtesting Evidence

One illustrative backtesting study reported a 71.7% win rate for Williams %R — the fourth highest among all indicators tested, reflecting its effectiveness as a mean-reversion oscillator in range-bound markets (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## About the Creator

Larry Williams is a legendary futures trader who won the 1987 Robbins World Cup of Futures Trading with a reported 11,376% return using momentum and %R methods (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Common Pitfalls

- **Premature signals in trends.** %R can sit pinned near 0 throughout a sustained rally (or near −100 in a crash). Treating every overbought reading as a sell shorts a strong uptrend repeatedly — the #1 oscillator mistake. In a trend, an "overbought" %R is a sign of *strength*, not an exit.
- **Whipsaw from over-sensitivity.** With only a 14-bar lookback and a 0/−100 bound, %R flips between extremes quickly; a short lookback magnifies this. Require a *cross back* through the threshold, not merely touching it.
- **Redundant stacking.** %R, [[stochastic|Stochastic]], and [[rsi|RSI]] are all bounded momentum [[oscillator|oscillators]] computed from the same price series. Running all three is false [[confluence]], not independent confirmation — they will mostly agree by construction.
- **No volume or trend context.** %R says nothing about [[volume]] or the broader [[trend]]; used alone it ignores the regime that determines whether mean-reversion even applies.
- **Identical-information trap.** Because %R = [[stochastic|%K]] − 100, debating "%R vs Stochastic %K" is debating the same indicator twice.

## Sources

- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)
- Williams, L. — *How I Made One Million Dollars... Last Year... Trading Commodities* (1973), where %R was introduced
- Murphy, J. — *Technical Analysis of the Financial Markets* (oscillator section covering %R, Stochastics, and RSI as a family)

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200` — OHLC bars carrying the highest-high/lowest-low/close inputs %R needs
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — rolling 24h high/low/close context

**Historical data:**
- `GET /api/v1/backtesting/klines` — full kline archive for %R signal studies
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — perp-side OHLCV for Hyperliquid listings

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute** — %R = (highest high − close) / (highest high − lowest low) × −100 over the last N bars from `GET /api/v1/market-data/klines`; or derive it for free from a stochastic %K already computed (%R = %K − 100)
- **Backtest** — replay cross-back-through-threshold rules (not mere touches) against `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08)
- **Regime gate** — only trade %R fades when `GET /api/v1/quant/market` shows `range_low_vol`; in `strong_trend_*` states %R pins at an extreme and every fade is a premature counter-trend entry
- **Tip** — do not stack %R with [[stochastic]] or [[rsi]] as "confirmation" in an agent's signal ensemble — %R and %K are the same series on a shifted scale, so agreement is by construction

## Related

- [[larry-williams]] — creator of %R
- [[stochastic]] — the indicator %R inverts (%R = %K − 100)
- [[rsi]] — sibling bounded momentum oscillator
- [[oscillator]] — the broader family
- [[momentum]] — what %R measures
- [[overbought]] / [[oversold]] — the extreme zones
- [[divergence]] — the reversal-warning signal
- [[mean-reversion]] — the regime where %R works best
- [[trend]] — the regime where it gives premature signals
