---
title: "Cup and Handle"
type: concept
created: 2026-04-07
updated: 2026-07-19
status: good
tags: [technical-analysis, breakout, momentum]
aliases: ["Cup with Handle", "Cup & Handle Pattern"]
related: ["[[breakout-strategies]]", "[[volume-analysis]]", "[[chart-patterns]]", "[[relative-strength]]"]
domain: [technical-analysis]
difficulty: intermediate
---

The cup and handle is a bullish continuation [[chart-patterns|chart pattern]] identified by william-o-neil as one of the most powerful base formations preceding major price advances. It consists of a rounded bottom (the cup) followed by a smaller downward consolidation (the handle), which resolves with a [[breakout-strategies|breakout]] to new highs. The pattern appears across all markets and timeframes but is most significant on daily and weekly charts.

## Overview

William O'Neil documented the cup and handle extensively in book-how-to-make-money-in-stocks, finding it in the majority of the best-performing stocks before their largest advances. The pattern represents a natural cycle of selling pressure, gradual recovery, a final shakeout of weak holders (the handle), and then the resumption of the uptrend with strong demand.

The cup and handle is central to the canslim methodology, where the "base breakout" is the primary buy signal. O'Neil's research, spanning decades of market history, showed that stocks forming proper cup-and-handle bases with strong [[relative-strength]] and fundamentals had the highest probability of producing outsized gains.

Key characteristics:
- **Duration**: cups typically form over 7 to 65 weeks; handles over 1 to several weeks
- **Depth**: the cup should correct 12-35% from the prior high (in normal markets; deeper in bear markets)
- **Shape**: a smooth, rounded bottom is preferred over a V-shaped or jagged bottom
- **Volume**: should dry up at the bottom of the cup and surge on the breakout

## How It Works

### Cup Formation

The cup begins after a stock has advanced and then pulls back. The left side of the cup forms as selling pressure drives the price down. The bottom represents a period where selling exhausts and buyers gradually step in. The right side forms as the stock recovers toward the prior high.

**What to look for**:
- A smooth, U-shaped bottom rather than a sharp V -- the rounded shape indicates gradual accumulation and a healthier base
- Volume should contract as the cup forms, especially at the bottom, indicating selling pressure is drying up
- The right side of the cup should recover to within 5-15% of the prior high before the handle forms
- Strong [[relative-strength]] during the cup formation -- the stock holds up better than the general market

### Handle Formation

The handle is a short, mild pullback from the right lip of the cup. It serves a critical function: it shakes out the last remaining weak holders who bought near the prior high and are eager to sell at breakeven.

**What to look for**:
- The handle should drift downward, not upward -- an upward-sloping handle (wedging up) is a warning sign
- Handle depth should be no more than 10-15% of the stock price, and ideally less than the cup's depth
- Handle duration is typically 1-4 weeks on a daily chart
- Volume should contract to very low levels during the handle -- this indicates that selling pressure is exhausted
- The handle should form in the upper half of the cup, not dipping below the cup's midpoint

### Breakout and Confirmation

The buy point is the price at the top of the handle's resistance line (often the right lip of the cup plus a small amount, typically 10 cents for stocks). Confirmation requires:

1. **Price closes above the buy point** -- a clear, decisive move
2. **Volume surges** -- breakout day volume should be at least 40-50% above average. O'Neil considered this essential; a breakout on low volume is suspect
3. **Follow-through** -- additional gains in the days following the breakout confirm institutional buying

### Measured Move Target

The minimum price target is the depth of the cup projected upward from the breakout point. For example, if a stock forms a cup between $50 (high) and $35 (low), the cup depth is $15. The minimum target after breaking out above $50 would be $65. Many winning stocks far exceed their measured move targets.

## Trading Applications

### Entry Rules (O'Neil Method)
1. Identify a stock with strong fundamentals (earnings growth, sales growth, ROE)
2. Confirm the cup and handle meets the criteria above
3. Buy as the stock breaks above the handle's resistance on heavy volume
4. Set a [[stop-loss]] 7-8% below the purchase price -- O'Neil's maximum loss rule

### Common Variations
- **Cup without handle** -- some stocks break out directly from the right lip without forming a handle; still valid but slightly lower probability
- **Double-bottom base** -- a W-shaped variant where the cup has two distinct troughs; O'Neil considered this a related pattern
- **High, tight flag** -- an extremely bullish relative of the cup and handle where the "cup" is very shallow and the stock consolidates near highs

### Failure Patterns
Cup and handle patterns fail when:
- The stock breaks out on weak volume (no institutional demand)
- The broader market is in a downtrend ([[market-breadth]] is deteriorating)
- The handle is too deep or too long, indicating persistent selling
- The stock has weak [[relative-strength]] or deteriorating fundamentals

A failed breakout that reverses below the buy point triggers the 7-8% stop-loss and signals that the pattern has been invalidated.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/ticker/24hr?symbol=BTCUSDT` — 24h ticker stats

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — daily OHLCV for base detection (cups form over weeks to months)
- `GET /api/v1/market-data/volume-history?days=90` — volume contraction/surge confirmation
- `GET /api/v1/backtesting/klines` — deep kline archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this pattern directly:

- **Detect** — scan daily bars from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` for the U-shaped base: 12-35% correction depth, rounded recovery, then a shallow handle in the upper half of the cup
- **Confirm** — require the breakout bar's volume well above average using `GET /api/v1/market-data/volume-history` — O'Neil's essential condition, automated
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot daily bars back to 2017-08) spans several full crypto cycles for base-breakout completion studies
- **Tip** — O'Neil's screen leaned on fundamentals; in crypto, substitute relative strength versus BTC and the market regime from `GET /api/v1/regimes/current` — breakouts in weak regimes fail like breakouts in bear markets

## Related

- [[chart-patterns]] -- broader category of price formations
- [[breakout-strategies]] -- trading approaches built around breakouts from bases
- [[volume-analysis]] -- essential for confirming breakouts
- [[relative-strength]] -- key filter for identifying the best cup and handle setups
- [[flags-and-pennants]] -- related continuation patterns

## Sources

- [[book-technical-analysis-of-the-financial-markets]] -- broader context of chart pattern analysis
