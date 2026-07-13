---
title: Candlestick Patterns
type: concept
created: 2026-04-06
updated: 2026-07-13
status: excellent
tags: [technical-analysis, indicators]
aliases: ["candle patterns", "candlestick charting", "japanese candlesticks", "hammer", "doji", "red candle", "green candle", "morning star", "evening star", "shooting star"]
domain: [technical-analysis]
prerequisites: ["[[price-action-trading]]"]
difficulty: beginner
related:
  - "[[cryptodataapi]]"
  - "[[price-action-trading]]"
  - "[[trend]]"
  - "[[trading-volume]]"
  - "[[bullish-engulfing]]"
  - "[[bearish-engulfing]]"
  - "[[support-and-resistance]]"
  - "[[book-technical-analysis-of-the-financial-markets]]"
  - "[[munehisa-homma]]"
---

# Candlestick Patterns

Candlestick patterns are visual formations on Japanese candlestick charts that traders use to anticipate future price direction based on historical price action.

## Overview

Developed by [[munehisa-homma|Munehisa Homma]], an 18th-century Japanese rice merchant, at the Dojima Rice Exchange. Homma embedded crowd psychology into price visualisation, producing patterns that remain in use more than 300 years later — the earliest known form of technical analysis, predating Western methods by over a century (Source: [[book-technical-analysis-of-the-financial-markets]], [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). Steve Nison introduced the methodology to Western markets in 1991. Each candlestick shows the open, high, low, and close for a given period. The "body" represents the open-to-close range, while "wicks" (shadows) show the high and low extremes.

## Anatomy of a Candle

```
        | <- upper wick (high)
      +---+
      |   |  <- body (open-to-close)
      +---+
        | <- lower wick (low)
```

- **Body colour:** a *bullish* (commonly green/white) body means close > open; a *bearish* (red/black) body means close < open.
- **Body size:** a long body signals strong directional conviction; a tiny body signals indecision.
- **Wick length:** long wicks show rejection of a price level — a long lower wick means buyers stepped in below; a long upper wick means sellers capped the advance.

## Catalog of Major Patterns

Patterns are grouped by the number of candles and whether they signal continuation or reversal.

| Pattern | Candles | Type | Bias | Quick description |
|---------|---------|------|------|-------------------|
| [[doji]] | 1 | Neutral / reversal | Indecision | Open ≈ close; momentum exhaustion |
| Hammer | 1 | Reversal | Bullish (at support) | Small body, long lower wick |
| Hanging Man | 1 | Reversal | Bearish (at resistance) | Same shape as hammer, in an uptrend |
| [[shooting-star]] | 1 | Reversal | Bearish (top) | Small body, long upper wick |
| Inverted Hammer | 1 | Reversal | Bullish (bottom) | Small body, long upper wick at a low |
| Marubozu | 1 | Continuation | Strong directional | Full body, little/no wick |
| Spinning Top | 1 | Neutral | Indecision | Small body, wicks both sides |
| [[bullish-engulfing]] | 2 | Reversal | Bullish | Up candle engulfs prior down candle |
| [[bearish-engulfing]] | 2 | Reversal | Bearish | Down candle engulfs prior up candle |
| Harami | 2 | Reversal | Either | Small candle inside prior large body |
| Piercing Line | 2 | Reversal | Bullish | Up candle closes >50% into prior down body |
| Dark Cloud Cover | 2 | Reversal | Bearish | Down candle closes >50% into prior up body |
| Tweezer Top/Bottom | 2 | Reversal | Either | Matching highs (top) or lows (bottom) |
| [[morning-star]] | 3 | Reversal | Bullish (bottom) | Down → small star → strong up |
| [[evening-star]] | 3 | Reversal | Bearish (top) | Up → small star → strong down |
| Three White Soldiers | 3 | Reversal/continuation | Bullish | Three rising long-bodied up candles |
| Three Black Crows | 3 | Reversal/continuation | Bearish | Three falling long-bodied down candles |

## How Traders Use Patterns

- **As triggers, not systems.** A pattern marks *where* to act; the broader [[trend]] and [[support-and-resistance]] context decide *whether* to act. A hammer at a major support level is far more meaningful than one in the middle of a range.
- **With confluence.** Combine patterns with [[trading-volume|volume]] spikes, [[rsi]] extremes, or [[moving-averages|moving-average]] levels. Multi-candle patterns ([[evening-star]], [[bullish-engulfing]]) carry more weight than single-candle ones.
- **For defined risk.** Patterns supply natural stop levels — e.g. above the high of a [[shooting-star]] or [[evening-star]], below the low of a hammer.
- **For exits as much as entries.** Even buy-and-hold traders use bearish reversal candles to lock in gains after an extended run.

## Trading Relevance

Candlestick patterns are most reliable when confirmed by [[trading-volume]], key support/resistance levels, or other indicators. Single-candle patterns provide weaker signals than multi-candle formations. They form the foundation of [[price-action-trading]] and are used across all timeframes and asset classes.

## Limitations and Common Pitfalls

- **Subjectivity.** "Small body" and "long wick" are eyeballed judgments; the same chart yields different reads from different traders.
- **Overfitting in backtests.** Loosely defined patterns are easy to data-mine; many "edges" vanish once costs and out-of-sample data are applied (see [[overfitting]]).
- **Context over shape.** Context matters more than the pattern itself — a hammer at a major support level is far more meaningful than one in the middle of a range.
- **Timeframe dependence.** A reversal candle on a 1-minute chart is noise relative to the same shape on a weekly chart; align signals across timeframes.
- **No price targets.** Patterns suggest *direction and timing*, not magnitude — pair them with measured moves, [[support-and-resistance]], or [[risk-management|risk-management]] rules.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=BTCUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats
- `GET /api/v1/market-data/short-term-price` — short-term momentum metrics

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/btc-price-history?days=730` — BTC history + 200D MA
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

## Related

- [[price-action-trading]] — the discipline candlesticks are the foundation of
- [[evening-star]] / [[morning-star]] — three-candle reversal patterns
- [[bullish-engulfing]] / [[bearish-engulfing]] — two-candle reversals
- [[shooting-star]] / [[doji]] — single-candle signals
- [[support-and-resistance]] — the context that validates patterns
- [[trading-volume]] — confirmation for any pattern
- [[technical-analysis]] — the broader discipline

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- Murphy dedicates a full chapter to Japanese candlestick charting, covering pattern identification, historical origins, and integration with Western technical analysis
- Nison, Steve. *Japanese Candlestick Charting Techniques* (2nd ed., 2001) -- the definitive Western reference that introduced candlestick analysis to U.S. markets; catalogs every major single- and multi-candle pattern
- Bulkowski, Thomas N. *Encyclopedia of Candlestick Charts* (2008) -- statistical study of pattern reliability and frequency across thousands of historical examples
