---
title: "SSL Channel"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, trend-following, crypto]
aliases: ["SSL Channel", "SSL", "SSL Hybrid", "Semaphore Signal Level channel"]
domain: [indicators, technical-analysis]
prerequisites: ["[[simple-moving-average]]", "[[moving-average-crossover]]"]
difficulty: beginner
related: ["[[simple-moving-average]]", "[[moving-average-crossover]]", "[[donchian-channels]]", "[[qqe]]", "[[halftrend]]", "[[tradingview-community-scripts]]", "[[pine-script]]"]
---

The **SSL Channel** is a trend-direction overlay built from two moving averages, one of the highs and one of the lows. Its two lines swap places whenever the close breaks outside the high-low envelope, which produces a crossover-style trend flip. The TradingView reference version, *SSL channel*, was published open-source by **ErwinBeckers** on 2019-03-28 (https://www.tradingview.com/script/xzIoaIJC-SSL-channel/). The much more widely used extension is **SSL Hybrid** by **Mihkel00** (https://www.tradingview.com/script/C3MlAWCw-SSL-Hybrid/), which adds a configurable baseline, ATR bands and an exit line (Source: [[tradingview-community-scripts]]). "SSL" is usually expanded as *Semaphore Signal Level*. The name comes from older MetaTrader indicators and is not formally documented.

## How It Works

**Original SSL channel** (default period 10):

1. `sma_high = SMA(high, 10)` and `sma_low = SMA(low, 10)`.
2. A state variable `hlv`:
   - `+1` if `close > sma_high`
   - `−1` if `close < sma_low`
   - otherwise it keeps its previous value (hysteresis inside the envelope)
3. Lines:
   - `ssl_up = sma_high` when `hlv = +1`, else `sma_low`
   - `ssl_down = sma_low` when `hlv = +1`, else `sma_high`
4. **Signal**: `ssl_up` crossing above `ssl_down` is bullish and crossing below is bearish. In practice that is simply the moment `hlv` flips.

The hysteresis is the useful part. Price has to close beyond the *opposite* side of a 10-bar high/low envelope to flip the trend, so small oscillations inside the envelope are ignored. That is conceptually close to a very short [[donchian-channels|Donchian]] rule, but smoothed.

**SSL Hybrid** (Mihkel00) extends this with:

- A **baseline** moving average (selectable type, often HMA or JMA with a 60 default) with Keltner-style ATR bands around it. Entries are skipped when price has run more than about 1× ATR from the baseline.
- **SSL2** as a faster continuation line and an **exit SSL** line.
- Candle colouring and alerts. This makes SSL Hybrid a complete "baseline + confirmation + exit" template in the style of the No Nonsense Forex (NNFX) method that inspired it.

## Crypto Application

- **Baseline role.** SSL Hybrid is used mostly as the trend baseline in multi-indicator crypto systems, typically SSL for direction, [[qqe|QQE MOD]] for momentum and a volume or volatility filter for chop.
- **Short default period.** A 10-bar SSL on crypto 15m-1h charts flips several times a day. Swing traders lengthen it or read it on 4h-1d.
- **NNFX confirmation role.** Stonehill Forex profiles SSL as a "C1" confirmation indicator in the [[nnfx-method|NNFX method]], used as the primary entry signal after the baseline agrees (Source: [[stonehill-forex-nnfx]]).
- **Freqtrade ports.** The logic is short enough that Python ports are common, which makes it easy to re-test outside TradingView.

## Common Pitfalls

- **Pure whipsaw in ranges.** Like every MA-based trend flip, it loses repeatedly in sideways crypto markets ([[whipsaw]]).
- **Hybrid parameter count.** SSL Hybrid exposes more than 15 inputs (MA types, lengths, ATR multipliers, exit line). The combinatorial search space invites [[overfitting]].
- **MTF variants.** "SSL Channel MTF" style scripts call `request.security`. Verify they use a one-bar offset or `lookahead_off` ([[lookahead-bias]]).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200`: highs, lows and closes for the SMA envelope
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=500`: perp bars for Hyperliquid execution

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep archive for flip-frequency and trend-capture testing

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute**: from `GET /api/v1/market-data/klines`, track the `hlv` state with its hysteresis rule and emit flips only on closed bars
- **Trend gate**: cross-check with `GET /api/v1/indicators/signum-rgg`. Treat an SSL flip that disagrees with the ADX/DMI colour as low-conviction
- **Backtest**: `GET /api/v1/backtesting/klines` to measure average bars-per-trend and flip count by timeframe. SSL's viability depends on trends lasting long enough to cover costs
- **Tip**: for a baseline role, a 4h SSL gating 1h entries is a cheap way to cut lower-timeframe whipsaw

## Related

- [[moving-average-crossover]]: the broader family
- [[donchian-channels]]: the unsmoothed high/low-breakout cousin
- [[qqe]]: the momentum confirmation usually paired with SSL Hybrid
- [[halftrend]], [[supertrend]]: ATR-based alternatives
- [[nnfx-method]]: the baseline/confirmation framework SSL Hybrid is built for
- [[tradingview-community-scripts]], [[pine-script]]: where the scripts live

## Sources

- ErwinBeckers, "SSL channel", TradingView, 2019-03-28. Mihkel00, "SSL Hybrid", TradingView (Source: [[tradingview-community-scripts]])
