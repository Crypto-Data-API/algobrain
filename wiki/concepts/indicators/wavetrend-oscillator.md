---
title: "WaveTrend Oscillator"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, momentum, mean-reversion, crypto]
aliases: ["WaveTrend", "WT", "WaveTrend [LazyBear]", "WaveTrend Oscillator [WT]", "WT_LB"]
domain: [indicators, technical-analysis]
prerequisites: ["[[exponential-moving-average]]", "[[cci]]", "[[overbought-oversold]]"]
difficulty: intermediate
related: ["[[cci]]", "[[stochastic-oscillator]]", "[[rsi]]", "[[overbought-oversold]]", "[[divergence]]", "[[wavetrend-reversal]]", "[[tradingview-community-scripts]]", "[[pine-script]]"]
---

The **WaveTrend Oscillator** (WT) is a smoothed, [[cci|CCI]]-style momentum oscillator. It plots a fast line (WT1) and a slow signal line (WT2) against fixed overbought/oversold bands and generates reversal signals when the two cross at an extreme. It entered TradingView as *Indicator: WaveTrend Oscillator [WT]*, published by **LazyBear** on 2014-05-27 as a port of an older TradeStation/MetaTrader indicator (https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/). It is one of the most-copied scripts on the platform, with about 1.4M views on 2026-09-28, and a staple of crypto chart setups, including the WaveTrend dots used by many "cipher"-style composite indicators (Source: [[tradingview-community-scripts]]).

## How It Works

Construction, using LazyBear's defaults (channel length 10, average length 21):

1. **Typical price**: `ap = (high + low + close) / 3`.
2. **Smoothed baseline**: `esa = EMA(ap, 10)`.
3. **Smoothed absolute deviation**: `d = EMA(|ap − esa|, 10)`.
4. **Normalised channel index**: `ci = (ap − esa) / (0.015 × d)`. This is the same 0.015 scaling constant Lambert used for [[cci|CCI]], so the output lives on a roughly ±100 scale.
5. **WT1** = `EMA(ci, 21)`, the main line.
6. **WT2** = `SMA(WT1, 4)`, the signal line.
7. **Bands**: overbought at +60 and +53, oversold at −60 and −53.

In effect WT is a doubly smoothed CCI with a short moving-average signal line. The EMA smoothing is what traders like about it: it swings less than a raw CCI or [[stochastic-oscillator|Stochastic]] and turns early relative to MACD.

```python
ap  = (high + low + close) / 3
esa = ap.ewm(span=10, adjust=False).mean()
d   = (ap - esa).abs().ewm(span=10, adjust=False).mean()
ci  = (ap - esa) / (0.015 * d)
wt1 = ci.ewm(span=21, adjust=False).mean()
wt2 = wt1.rolling(4).mean()
buy  = (wt1 > wt2) & (wt1.shift(1) <= wt2.shift(1)) & (wt1 < -53)
sell = (wt1 < wt2) & (wt1.shift(1) >= wt2.shift(1)) & (wt1 > 53)
```

## Signals

| Signal | Condition | Typical read |
|---|---|---|
| **Oversold cross (buy)** | WT1 crosses above WT2 while below the oversold band | Downswing exhausted, so mean-reversion long |
| **Overbought cross (sell)** | WT1 crosses below WT2 while above the overbought band | Upswing exhausted, so mean-reversion short or exit |
| **Mid-zone cross** | Cross near zero | Weak, and usually filtered out |
| **Divergence** | Price makes a lower low while WT1 makes a higher low (or the reverse) | Momentum [[divergence]], a higher-conviction reversal cue |
| **WT1 − WT2 histogram** | The gap between the lines | Momentum acceleration or deceleration |

LazyBear's own description says crossovers are only some of the useful signals. He calls a sell when the oscillator is above the overbought band and crosses down through the signal line, and the mirror condition a buy.

## Crypto Application

- **Range-heavy regimes.** WT's oversold and overbought crosses behave like other bounded oscillators. They work in ranges and fail in strong trends, where WT pins at an extreme and every "sell" cross in a bull run is premature. Pair it with a trend gate ([[adx]], a higher-timeframe MA or the CryptoDataAPI Signum RGG classifier).
- **Multi-timeframe stacking.** A common crypto practice is to require the 4h WT to cross up from oversold while the 1d WT is not overbought.
- **Composite "cipher" indicators.** Many popular protected and invite-only crypto indicators wrap WaveTrend together with money flow and RSI. The open-source WT is the core you can audit.

## Common Pitfalls

- **Fixed bands on a non-stationary scale.** ±53/±60 were set on 2014 charts. Highly volatile alts sit beyond the bands for long stretches, so recalibrate bands per asset or use percentile bands.
- **Over-signalling on low timeframes.** On 5m-15m charts crosses fire constantly, and costs eat most of the edge.
- **Lagging signal line.** WT2 is a 4-bar SMA of an already smoothed series. Entries arrive after the pivot, so the claimed "early" turns are only early relative to slower oscillators.
- **Repainting in derivatives.** The base script uses only current-timeframe EMAs and does not repaint on closed bars. Many multi-timeframe variants add `request.security` with lookahead. Check before trusting their charts ([[lookahead-bias]]).

## Variants

- **WaveTrend with Crosses [LazyBear]** (republished by lonestar108): adds cross markers (https://www.tradingview.com/script/jFQn4jYZ-WaveTrend-with-Crosses-LazyBear/)
- **WaveTrend [LazyBear] vX by DGT** (dgtrd): adds divergence and signal filtering (https://www.tradingview.com/script/cYG1lqRI-WaveTrend-LazyBear-vX-by-DGT/)
- **WaveTrend [LazyBear] with Long/Short Labels** (thomcam): labelled entries (https://www.tradingview.com/script/S5vz6tsG-WaveTrend-LazyBear-with-Long-Short-Labels/)

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200`: OHLCV for hlc3, EMAs and WT1/WT2
- `GET /api/v1/hyperliquid/candles?coin=ETH&interval=1h&limit=500`: perp bars for Hyperliquid-traded coins
- `GET /api/v1/indicators/signum-rgg`: ADX/DMI trend colour, a ready-made trend gate for WT reversal signals

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep archive for calibrating per-asset bands and testing crosses

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=4h&limit=200"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-indicators]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute**: from `GET /api/v1/market-data/klines`, build WT1/WT2 with the 10/21/4 defaults on closed bars. Emit crosses only beyond ±53
- **Gate**: take oversold-cross longs only when `GET /api/v1/indicators/signum-rgg/{symbol}` is not RED, because in a strong downtrend WT oversold crosses repeatedly fail
- **Calibrate**: from `GET /api/v1/backtesting/klines`, compute each asset's WT1 5th/95th percentiles and use them in place of the fixed ±60 bands for high-vol alts
- **Backtest**: measure forward 6/12/24-bar returns after crosses, net of a 10-15 bps round trip, split by the trend state above

## Related

- [[cci]]: the normalisation WT is built from
- [[stochastic-oscillator]], [[rsi]]: alternative bounded oscillators
- [[overbought-oversold]]: the band logic it relies on
- [[divergence]]: the higher-conviction WT signal
- [[wavetrend-reversal]]: the strategy built on WT crosses
- [[tradingview-community-scripts]], [[pine-script]]: where the script lives

## Sources

- LazyBear, "Indicator: WaveTrend Oscillator [WT]", TradingView, 2014-05-27 (Source: [[tradingview-community-scripts]])
