---
title: Average Directional Index (ADX)
type: concept
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [adx, technical-analysis, indicators, trend-following]
aliases: [ADX, Average Directional Movement Index]
domain: [indicators]
prerequisites: ["[[trend]]", "[[atr]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[trend]]"
  - "[[trend-following]]"
  - "[[divergence]]"
  - "[[john-murphy]]"
  - "[[j-welles-wilder]]"
  - "[[rsi]]"
  - "[[atr]]"
  - "[[donchian-channels]]"
  - "[[technical-analysis-of-the-financial-markets]]"
  - "[[commodities]]"
  - "[[trend-following-cta]]"
  - "[[crude-oil]]"
---

# Average Directional Index (ADX)

The Average Directional Index (ADX) is a technical indicator developed by J. Welles Wilder that measures the strength of a [[trend]], regardless of its direction.

## How It Works

The ADX is derived from two directional movement indicators: +DI (positive directional indicator) and -DI (negative directional indicator). From these, Wilder computes the Directional Index, DX = 100 × |(+DI) − (−DI)| / |(+DI) + (−DI)| — the normalized absolute difference between the two lines. The ADX is the smoothed (Wilder-smoothed) moving average of DX, typically over 14 periods. Because DX is normalized to a 0–100 scale, ADX is too.

- **ADX below 20** - Weak or absent trend (range-bound market)
- **ADX 20-25** - Trend may be emerging
- **ADX above 25** - Strong trend in place
- **ADX above 50** - Extremely strong trend (relatively rare)

## Components

- **+DI** - Measures upward directional movement
- **-DI** - Measures downward directional movement
- When +DI crosses above -DI, it suggests bullish momentum; the reverse suggests bearish momentum

## Trading Relevance

Traders use ADX to decide which strategy to apply. High ADX readings favor [[trend-following]] approaches; low ADX readings favor range-trading or mean-reversion strategies. The ADX does not indicate trend direction -- only strength. Direction comes from comparing +DI and -DI or from the price itself.

## Strategy Selection Framework

This is ADX's primary practical use -- deciding WHICH strategy to apply in current market conditions (Source: [[book-technical-analysis-of-the-financial-markets]]). Murphy frames ADX not just as an indicator but as a meta-tool that determines which other tools are appropriate:

- **ADX > 25**: Use [[trend-following]] strategies -- [[moving-averages|moving average]] crossovers, breakout entries, trailing stops. The market is trending and mean-reversion approaches will produce losing trades.
- **ADX < 20**: Use mean-reversion strategies -- [[rsi|RSI]] overbought/oversold signals, [[bollinger-bands|Bollinger Band]] band-to-band trades, oscillator crossovers. The market is range-bound and trend-following will produce whipsaws.
- **ADX between 20-25**: Transition zone. Either reduce position size or wait for a clear regime to establish.

This framework prevents the most common mistake in technical trading: applying trending strategies to range-bound markets and vice versa. A systematic trader who checks ADX before selecting their entry method will avoid a large proportion of losing trades that come from strategy-regime mismatch.

**Practical implementation**: Some systematic traders use ADX as a binary filter -- only take trend-following signals when ADX > 25 and only take mean-reversion signals when ADX < 20. Others use ADX as a continuous scaling factor, increasing trend-following position size as ADX rises and decreasing it as ADX falls.

## Commodity Applications

Commodity markets often exhibit stronger trends than equities due to supply/demand imbalances, weather shocks, and geopolitical disruptions (Source: [[book-technical-analysis-of-the-financial-markets]]). As a result, ADX readings above 40 are more common in commodities than in stock indices.

- **Energy markets**: [[crude-oil]] and [[natural-gas]] during geopolitical events (sanctions, wars, OPEC production decisions) routinely produce ADX readings of 40-60+. The 2022 energy crisis following Russia's invasion of Ukraine saw ADX on crude oil sustained above 50 for weeks.
- **Agricultural markets**: Weather shocks in [[corn]], [[wheat]], and [[soybeans]] produce some of the strongest trends in any market. Droughts, floods, or export bans can push ADX to extreme levels as supply disruptions override all other market dynamics.
- **Precious metals**: [[gold]] during monetary policy pivots and [[silver]] during industrial demand surges both produce sustained high-ADX environments.

For [[trend-following-cta|CTA funds]], ADX serves as a position-sizing input: higher ADX readings justify larger trend-following positions, while declining ADX triggers partial profit-taking. Many CTAs incorporate ADX into their systematic models alongside [[moving-averages]] crossovers and [[atr|ATR]]-based stops.

## Limitations

ADX is a lagging indicator. By the time ADX rises above 25, a significant portion of the trend move may have already occurred. It can also remain elevated during extended consolidation periods that follow strong trends, producing misleading signals.

## Turtle-Style Breakout Stack

ADX serves as a key filter in the professional **Turtle-style breakout stack**: [[donchian-channels|Donchian]] 20/55 breakout + [[atr|ATR]] position sizing + ADX filter. The ADX filter ensures breakout entries are only taken when the market is trending (ADX > 25), avoiding the whipsaw trades that degrade pure breakout systems in range-bound conditions (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Backtesting Evidence

One illustrative backtesting study across US equities reported ADX with a 53.6% win rate — moderate, reflecting ADX's nature as a trend-strength filter rather than a direct entry signal. ADX is most effective as a qualifier for other signals rather than as a standalone indicator (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Sources

- J. Welles Wilder Jr., *New Concepts in Technical Trading Systems* (Trend Research, 1978) — the original publication defining the Directional Movement System (+DI, −DI, DX, ADX).
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — covers ADX within Wilder's Directional Movement System and its use for strategy selection.
- [[book-technical-analysis-of-the-financial-markets]] -- Murphy covers ADX in the context of Wilder's Directional Movement System, including the +DI/-DI framework, ADX interpretation for trend strength, and its role as a strategy selection tool
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Turtle-style breakout stack, win-rate data, cross-market applicability

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

**Live dashboards:** [SIGNUM RGG](https://cryptodataapi.com/signum-rgg-coin-trend-indicator) · [technical structure](https://cryptodataapi.com/technical-structure)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Live state** — `GET /api/v1/indicators/signum-rgg` returns the ADX(14)+DMI classification (RED/GREY/GREEN) for the whole asset universe in one call; `GET /api/v1/indicators/signum-rgg/{symbol}` adds per-asset detail plus a rolling 60-day history
- **Compute** — for custom periods or intraday ADX, pull raw OHLCV from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=1000` and apply Wilder smoothing yourself
- **Backtest** — `GET /api/v1/backtesting/klines` serves Binance spot 1h/4h/1d back to 2017-08 — enough to test "trend-follow only when ADX > 25" gates across full cycles (1m bars exist only since 2026-03-30)
- **Tip** — use the RGG colour as the strategy-selection switch this page describes: GREEN favours trend entries, GREY/RED favour mean-reversion or standing aside; check colour persistence in the 60d history before trusting a fresh flip

## Related

- [[trend]] -- ADX measures trend strength
- [[trend-following]] -- ADX > 25 favors trend-following strategies
- [[rsi]] -- Wilder's companion momentum indicator
- [[atr]] -- Wilder's companion volatility indicator, from the same 1978 book
- [[bollinger-bands]] -- mean-reversion tool favored when ADX is low
- [[commodities]] -- commodity markets produce higher ADX readings than equities
- [[trend-following-cta]] -- CTA funds use ADX as a position-sizing input
- [[crude-oil]] -- energy markets produce extreme ADX readings during geopolitical events
- [[moving-averages]] -- MA crossovers are the primary trend-following entry when ADX confirms
- [[john-murphy]] -- covers ADX as part of the Directional Movement System in his framework
