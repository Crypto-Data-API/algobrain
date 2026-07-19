---
title: Relative Strength Index (RSI)
type: concept
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [rsi, indicators, technical-analysis]
aliases: [RSI, relative-strength-index]
domain: [indicators]
difficulty: beginner
related:
  - "[[cryptodataapi]]"
  - "[[momentum]]"
  - "[[stochastic]]"
  - "[[macd]]"
  - "[[moving-averages]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
  - "[[john-murphy]]"
  - "[[j-welles-wilder]]"
  - "[[adx]]"
  - "[[atr]]"
  - "[[commodities]]"
  - "[[intermarket-analysis]]"
  - "[[technical-analysis-of-the-financial-markets]]"
  - "[[williams-percent-r]]"
---

# RSI (Relative Strength Index)

The RSI is a momentum oscillator that measures the speed and magnitude of recent price changes on a scale of 0 to 100, identifying overbought and oversold conditions.

## Overview

Developed by J. Welles Wilder in 1978, RSI is one of the most popular technical indicators (Source: [[book-technical-analysis-of-the-financial-markets]]). It compares the average gain to the average loss over a lookback period (default 14 periods) to produce a single value indicating whether recent price action has been predominantly bullish or bearish.

## How It Works

- **RSI formula**: RSI = 100 - (100 / (1 + RS)), where RS = average gain / average loss over N periods.
- **Overbought (>70)**: Price has risen aggressively and may be due for a pullback or consolidation.
- **Oversold (<30)**: Price has fallen sharply and may be due for a bounce or relief rally.
- **Midline (50)**: Acts as a trend filter. RSI holding above 50 suggests bullish momentum; below 50 suggests bearish.

## Key Signals

- **Divergence**: Price makes a new high but RSI makes a lower high (bearish divergence), or price makes a new low but RSI makes a higher low (bullish divergence). Divergence warns of potential trend exhaustion.
- **Failure swings**: RSI breaks above 70, pulls back, then fails to reach 70 again before dropping -- a bearish failure swing. The inverse applies for bullish swings.
- **Range shifts**: In strong uptrends, RSI oscillates between 40-80. In downtrends, it oscillates between 20-60. The boundaries shift with trend strength.

## Trading Relevance

RSI is best used as a confirmation tool rather than a standalone signal. Overbought/oversold readings alone are not reliable entry triggers -- in strong trends, RSI can remain overbought or oversold for extended periods. Divergence signals combined with [[support-and-resistance]] or [[volume]] confirmation are more robust. Many traders adjust the default 14-period to suit their timeframe (shorter for day trading, longer for swing).

## Commodity Applications

RSI is particularly useful for mean-reverting [[commodities]] such as [[gold]] and agricultural commodities, where prices tend to oscillate around production cost or fair-value anchors (Source: [[book-technical-analysis-of-the-financial-markets]]). In commodity markets, RSI divergences combined with [[cot-report-analysis|COT positioning]] data create powerful signals -- when commercials are heavily long and RSI shows bullish divergence on a weekly chart, the setup has historically been high-probability.

Murphy notes an important nuance regarding **RSI range shifts** in commodities: in strong commodity bull markets (like [[crude-oil]] during supply shocks or [[gold]] during monetary easing cycles), RSI oscillates between 40 and 80, rarely touching 30. Traders who wait for RSI to reach 30 before buying during a commodity supercycle will miss the entire move. Conversely, during commodity bear markets, RSI tends to oscillate between 20 and 60, and readings above 70 are fleeting selling opportunities rather than signs of sustained strength (Source: [[book-technical-analysis-of-the-financial-markets]]).

## Wilder's Original Work

J. Welles Wilder introduced RSI in his 1978 book *New Concepts in Technical Trading Systems*, the same work that gave traders the [[adx|Average Directional Index (ADX)]] and [[atr|Average True Range (ATR)]]. Wilder's three indicators are complementary: RSI measures momentum magnitude, ADX measures trend strength, and ATR measures volatility. Using all three together provides a comprehensive picture -- ADX tells you whether to use a trending or mean-reversion approach, RSI identifies overbought/oversold conditions within that regime, and ATR guides [[position-sizing]] and stop placement.

## Additional Strategies

Beyond the classic 70/30 framework, several RSI-based strategies have developed over the decades (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]):

- **RSI-2 pullback system**: Popularised by Larry Connors, uses a 2-period RSI to identify extreme short-term oversold conditions (RSI-2 below 10) for mean-reversion entries in uptrending stocks. The very short lookback makes it far more sensitive than standard RSI(14).
- **Hidden divergences**: While standard divergences warn of trend exhaustion, "hidden" divergences signal trend *continuation*. A hidden bullish divergence occurs when price makes a higher low but RSI makes a lower low — suggesting the uptrend is pausing, not reversing.
- **Best-practice combination**: [[bollinger-bands|Bollinger Bands]] + RSI is a classic mean-reversion pair for range-bound markets. Price touching the lower Bollinger Band while RSI is oversold creates a high-probability bounce setup.

## Backtesting Evidence

One illustrative backtesting study across US equities reported RSI(14) with a 79.4% win rate — the highest among all indicators tested. However, win-rate alone is misleading: high-win-rate mean-reversion systems like RSI often have poor payoff ratios (small average wins vs occasional large losses), while lower-win-rate trend systems generate most of their P&L from a few large winners (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy's comprehensive coverage of RSI, including Wilder's original formulation, divergence analysis, failure swings, and range-shift behavior in trending markets
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — RSI-2 pullback systems, hidden divergences, win-rate data, and best-practice combinations
- Wilder, J. Welles (1978), *New Concepts in Technical Trading Systems*, Trend Research — original RSI, ADX, and ATR formulations
- Connors, L. & Alvarez, C. (2009), *Short Term Trading Strategies That Work* — RSI-2 mean-reversion system

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

**Live dashboards:** [technical structure](https://cryptodataapi.com/technical-structure) · [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — `GET /api/v1/indicators/technical` returns the pre-computed SMA/BB/RSI structure state for the whole universe in one call; `GET /api/v1/indicators/technical/{symbol}` adds per-asset detail with a rolling 60d history
- **Compute** — for non-default lookbacks (e.g. Connors RSI-2), pull `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` and apply Wilder smoothing to the closes
- **Backtest** — replay RSI rules against `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08; Hyperliquid daily to 2023, 1m only since 2026-03-30)
- **Tip** — gate mean-reversion entries with the HMM state from `GET /api/v1/quant/market`: fading overbought RSI inside a `strong_trend_bull` regime is the classic failure mode this page warns about

## Related

- [[momentum]] -- RSI measures momentum strength
- [[stochastic]] -- another overbought/oversold oscillator
- [[macd]] -- complementary momentum indicator
- [[rsi-vs-stochastic]] -- comparison of RSI and stochastic oscillators
- [[macd-vs-rsi]] -- comparison of MACD and RSI for signal confirmation
- [[adx]] -- Wilder's trend strength indicator, complementary to RSI
- [[atr]] -- Wilder's volatility measure, from the same 1978 book
- [[commodities]] -- RSI range shifts are particularly relevant in commodity markets
- [[intermarket-analysis]] -- RSI applied across asset classes in Murphy's framework
- [[john-murphy]] -- covers RSI extensively in his technical analysis framework
