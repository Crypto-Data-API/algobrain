---
title: "HalfTrend"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, trend-following, volatility, crypto]
aliases: ["HalfTrend", "Half Trend", "HalfTrend [everget]"]
domain: [indicators, technical-analysis]
prerequisites: ["[[atr]]", "[[simple-moving-average]]"]
difficulty: intermediate
related: ["[[supertrend]]", "[[atr]]", "[[ut-bot-alerts]]", "[[ssl-channel]]", "[[chandelier-exit]]", "[[tradingview-community-scripts]]", "[[pine-script]]"]
---

**HalfTrend** is an [[atr|ATR]]-based trend line that flips between an up-trend and a down-trend state when price makes a meaningful break of recent extremes. It is often described as a smoother alternative to [[supertrend|SuperTrend]]. The open-source TradingView version by **everget** was published on 2021-01-24 (https://www.tradingview.com/script/U1SJ8ubc-HalfTrend/). everget describes it as "similar to the SuperTrend but uses a different trend's identification logic", and his page warns against buying paid scripts that repackage the same logic under other names (Source: [[tradingview-community-scripts]]). The indicator itself predates the TradingView port and comes from the MetaTrader community.

## How It Works

Inputs: **Amplitude** (default 2) and **Channel Deviation** (default 2), with ATR(100).

1. `high_price = highest(high, amplitude)` and `low_price = lowest(low, amplitude)` over the recent window.
2. `high_ma = SMA(high, amplitude)` and `low_ma = SMA(low, amplitude)`.
3. **In an uptrend** the line tracks `max_low_price`, the highest recent low, which ratchets upward. The trend flips down when `high_ma` falls below that level **and** the close is below the prior bar's low.
4. **In a downtrend** the line tracks `min_high_price`, the lowest recent high, which ratchets downward. The trend flips up when `low_ma` rises above that level **and** the close is above the prior bar's high.
5. **ATR channel**: `ATR(100) / 2 × channel_deviation` is plotted around the line. That halved ATR is where the name comes from. The channel is visual context and not part of the flip rule.
6. Arrows mark each flip.

The practical difference from SuperTrend is that HalfTrend flips on a **structure break** (the smoothed highs falling through the highest recent low, confirmed by a close beyond the prior bar), not on a close through an ATR-offset band. It therefore reacts to swing structure more than to volatility, and tends to give fewer flips in low-volatility grinds.

## Crypto Application

- **Swing-structure trend filter.** On 1h-4h crypto charts HalfTrend acts as a "higher lows intact" detector. Longs stay valid while the line rises and the structure holds.
- **Pairing.** It is commonly combined with a momentum filter ([[qqe]], [[wavetrend-oscillator|WaveTrend]]) or a higher-timeframe HalfTrend, the same way SuperTrend is stacked.
- **Amplitude as the key knob.** Raising amplitude from 2 to 3-5 makes flips require larger swing breaks, which cuts crypto noise at the cost of later entries.

## Common Pitfalls

- **Not a stop level.** The line is a trend state, not a volatility-scaled stop. Use the ATR channel or a separate [[atr-trailing-stop]] for risk.
- **Whipsaw in tight ranges.** With amplitude 2 on low timeframes, the "structure break" can be a two-bar wiggle ([[whipsaw]]).
- **Strategy wrappers.** Community strategies built on HalfTrend (for example "Strategy #3 HalfTrend (Originally By everget)" by Mhd_Jawish) should be re-tested with fees, because their published defaults are the Strategy Tester's zero-commission settings.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=300`: highs, lows and closes for the amplitude windows, plus the ATR(100) channel, which needs at least 100 bars of warm-up
- `GET /api/v1/hyperliquid/candles?coin=ETH&interval=1h&limit=500`: perp bars for Hyperliquid execution

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep archive for amplitude sweeps and flip-count analysis

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=300"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute**: from `GET /api/v1/market-data/klines`, fetch at least 300 bars so ATR(100) is warmed up. Track the ratcheting max-low/min-high levels and flip on closed bars only
- **Compare**: compute [[supertrend]] (10, 3) on the same bars and report flip counts and average trend duration for both, which shows whether HalfTrend's structure logic actually cuts whipsaw on this asset
- **Regime gate**: `GET /api/v1/regimes/current`. Only act on flips that agree with the macro regime label, and log counter-regime flips separately
- **Backtest**: `GET /api/v1/backtesting/klines` for amplitude 2/3/5 sweeps, net of costs, across the 2018, 2022 and 2025 drawdown windows

## Related

- [[supertrend]]: the closest ATR trend-line sibling
- [[ut-bot-alerts]], [[chandelier-exit]]: other popular ATR trend tools from the same library
- [[ssl-channel]]: high/low-MA trend flip with similar hysteresis
- [[atr]]: the channel width
- [[tradingview-community-scripts]], [[pine-script]]: where the script lives

## Sources

- everget, "HalfTrend", TradingView, 2021-01-24 (updated 2021-02-12) (Source: [[tradingview-community-scripts]])
