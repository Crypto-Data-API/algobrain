---
title: "Squeeze Momentum Indicator"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, volatility, momentum, breakout, crypto]
aliases: ["Squeeze Momentum", "SQZMOM_LB", "Squeeze Momentum Indicator [LazyBear]", "TTM Squeeze", "BB/KC Squeeze"]
domain: [indicators, technical-analysis]
prerequisites: ["[[bollinger-bands]]", "[[keltner-channels]]", "[[linear-regression]]"]
difficulty: intermediate
related: ["[[bollinger-bands]]", "[[keltner-channels]]", "[[volatility-breakout]]", "[[squeeze-momentum-breakout]]", "[[tradingview-community-scripts]]", "[[pine-script]]", "[[volatility-clustering]]"]
---

The **Squeeze Momentum Indicator** flags volatility compression and shows which way momentum is leaning when it is released. It marks a "squeeze" when [[bollinger-bands|Bollinger Bands]] contract inside [[keltner-channels|Keltner Channels]], and plots a [[linear-regression]] momentum histogram around a zero line. It is a free re-implementation of John Carter's TTM Squeeze (*Mastering the Trade*, ch. 11). The open-source TradingView version, *Squeeze Momentum Indicator [LazyBear]*, was published by **LazyBear** on 2014-07-04 and is one of the most-viewed community scripts, with about 3.09M views on 2026-09-28 (https://www.tradingview.com/script/nqQ1DT5a-Squeeze-Momentum-Indicator-LazyBear/) (Source: [[tradingview-community-scripts]]).

## How It Works

Two independent pieces share one pane:

**1. Squeeze state (dots on the zero line)**

- Bollinger Bands: 20-period SMA ± 2.0 standard deviations.
- Keltner Channels: 20-period SMA ± 1.5 × the moving average of true range (LazyBear's default uses true range; a plain high-low range is an option).
- **Squeeze on** when both BB lines sit inside the KC. Volatility has compressed below its "normal" ATR-scaled envelope. LazyBear plots this as a **black** cross.
- **Squeeze off (released)** when the BB expand back outside the KC. This plots as a **grey** cross.
- Neither condition (a mixed state) plots blue.

**2. Momentum histogram**

- Take the close minus the midpoint of (a) the average of the 20-bar highest high and lowest low and (b) the 20-bar SMA of close.
- Smooth that series with a 20-bar linear-regression value (the end-point of the least-squares line), not a raw momentum difference.
- Bars are coloured four ways. Above zero and rising is bright green, above zero and falling is dark green, below zero and falling is bright red, and below zero and rising is dark red.

Carter's rule, as quoted in the LazyBear description, is to wait for the **first grey cross after a run of black crosses** and trade in the direction of the histogram.

```python
# pandas sketch; bars must be confirmed closes only
basis = close.rolling(20).mean()
dev   = 2.0 * close.rolling(20).std(ddof=0)
tr    = true_range(high, low, close)
kc_w  = 1.5 * tr.rolling(20).mean()
sqz_on  = (basis - dev > basis - kc_w) & (basis + dev < basis + kc_w)
sqz_off = (basis - dev < basis - kc_w) & (basis + dev > basis + kc_w)
mid = ((high.rolling(20).max() + low.rolling(20).min()) / 2 + basis) / 2
mom = rolling_linreg_endpoint(close - mid, 20)
fire_long  = sqz_off & sqz_on.shift(1) & (mom > 0) & (mom > mom.shift(1))
```

## Reading It

| Visual | Meaning |
|---|---|
| Run of black crosses | Compression. Volatility is below its ATR envelope and a larger move is building |
| First grey after black | Squeeze fired, so expansion is starting |
| Histogram above zero, rising | Bullish momentum building |
| Histogram above zero, fading (dark green) | Bullish momentum waning, a common exit cue |
| Histogram below zero, falling | Bearish momentum building |

The squeeze itself is **directionless**. It says volatility is likely to expand, not which way. Direction comes only from the histogram, which lags because it is regression-smoothed.

## Crypto Application

- **Volatility clustering makes the setup common.** Crypto spends long stretches in low realised vol before sharp expansions ([[volatility-clustering]]), so squeezes on BTC and ETH 4h/1d charts fire several times a year. Altcoins fire more often and with more false releases.
- **Perp context matters.** A squeeze that fires into crowded one-sided funding often ends in a liquidation cascade in the crowded direction's disfavour. Checking funding before taking the fire direction is a common filter.
- **Timeframe.** On 1h and below, weekend and Asia-session lulls create "squeezes" that just reflect session volume and resolve into nothing. The signal is cleaner on 4h and above.

## Common Pitfalls

- **Treating the squeeze as directional.** Half the edge claimed in marketing comes from pairing the squeeze with hindsight direction. The histogram only turns after the move starts.
- **Histogram repaint on the live bar.** The linreg value changes intrabar, so act on bar close only. Derivative scripts that add higher-timeframe `request.security` calls can add lookahead repainting ([[lookahead-bias]]).
- **Parameter drift.** Many copies change the KC multiplier (1.0/1.5/2.0 "tiers", as in Carter's later TTM Squeeze Pro). A tighter KC gives fewer squeezes and a looser KC gives more. Pick one before testing, not after.
- **Duplicate evidence.** The Bollinger/Keltner squeeze is already the contraction filter in [[volatility-breakout]]. Stacking the two is not independent confirmation.

## Variants

- **TTM Squeeze** (John Carter / Simpler Trading): the original, closed-source. It uses a slightly different momentum calculation.
- **Squeeze Momentum Indicator [LazyBear] vX by DGT** (dgtrd): overlays squeeze state on the price chart (https://www.tradingview.com/script/Dsr7B2xE-Squeeze-Momentum-Indicator-LazyBear-vX-by-DGT/).
- **Strategy wrappers**: several community strategy versions (for example by PineIndicators and 03.freeman) turn the fire signal into entries. Re-test them with fees on. See [[squeeze-momentum-breakout]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200`: OHLCV to compute BB, KC and the linreg histogram
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=4h&limit=200`: perp-side bars for Hyperliquid execution
- `GET /api/v1/indicators/technical`: server-side SMA/BB/RSI structure state, useful for screening the universe for tight bands before computing KC locally

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep kline archive for measuring squeeze frequency and fire outcomes across cycles

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-indicators]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Screen**: pull `GET /api/v1/indicators/technical` to shortlist assets with contracted Bollinger structure, then fetch `GET /api/v1/market-data/klines` per shortlist symbol and compute the full BB-inside-KC state locally
- **Signal**: flag the first bar where the squeeze releases after ≥ 6 consecutive squeeze bars. Read direction from the sign and slope of the linreg histogram on the closed bar only
- **Regime gate**: `GET /api/v1/volatility/regime` reads a compressed regime as the precondition. Skip fires that occur while the asset is already in a high-vol state
- **Backtest**: `GET /api/v1/backtesting/klines` (1h/4h/1d back to 2017-08) to count fires per year and measure forward 5/10/20-bar returns by histogram sign, net of fees

## Related

- [[bollinger-bands]]: the inner band that defines the squeeze
- [[keltner-channels]]: the ATR envelope it is compared against
- [[volatility-breakout]]: NR7/BB-squeeze contraction-expansion strategy
- [[squeeze-momentum-breakout]]: the strategy built on this indicator
- [[volatility-clustering]]: why compression tends to precede expansion
- [[tradingview-community-scripts]], [[pine-script]]: where the script lives

## Sources

- LazyBear, "Squeeze Momentum Indicator [LazyBear]", TradingView, 2014-07-04 (Source: [[tradingview-community-scripts]])
- John F. Carter, *Mastering the Trade*, McGraw-Hill (ch. 11, TTM Squeeze), as referenced in the script description
