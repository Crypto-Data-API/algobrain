---
title: "QQE (Quantitative Qualitative Estimation)"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, momentum, trend-following, crypto]
aliases: ["QQE", "Quantitative Qualitative Estimation", "QQE MOD", "QQE Mod"]
domain: [indicators, technical-analysis]
prerequisites: ["[[rsi]]", "[[atr]]", "[[exponential-moving-average]]"]
difficulty: intermediate
related: ["[[rsi]]", "[[atr]]", "[[bollinger-bands]]", "[[ssl-channel]]", "[[momentum]]", "[[tradingview-community-scripts]]", "[[pine-script]]"]
---

**QQE (Quantitative Qualitative Estimation)** is a smoothed-[[rsi|RSI]] momentum indicator. It surrounds the smoothed RSI with a volatility-scaled trailing band, built from an ATR-style measure of the RSI's own bar-to-bar movement, so it gives trend and flip signals on the RSI scale instead of on price. The version most crypto traders use is **QQE MOD** by **Mihkel00**, published on TradingView on 2020-01-20 and updated to Pine v6 on 2024-12-11 (https://www.tradingview.com/script/TpUW4muw-QQE-MOD/). It runs two QQE calculations and adds a [[bollinger-bands|Bollinger Band]] filter on the primary line (Source: [[tradingview-community-scripts]]).

## How It Works

**Classic QQE** (defaults RSI 14, smoothing 5, QQE factor 4.236):

1. `rsi_ma = EMA(RSI(close, 14), 5)`, the smoothed RSI.
2. `atr_rsi = |rsi_ma − rsi_ma[1]|`, a bar-to-bar "true range" of the smoothed RSI.
3. Double-smooth it with Wilder-style EMAs of length `2 × 14 − 1 = 27`, then multiply by the QQE factor (≈ 4.236) to get the band width `dar`.
4. Build a **trailing level** that ratchets like a [[supertrend|SuperTrend]] on the RSI axis. The long band is `rsi_ma − dar` and only rises while `rsi_ma` stays above it. The short band is `rsi_ma + dar` and only falls. The active band flips when `rsi_ma` crosses it.
5. Signals: `rsi_ma` crossing the trailing level, or crossing 50.

**QQE MOD** (Mihkel00) adds:

- A **primary QQE** (RSI 6, smoothing 5, factor 3) plotted as a histogram centred on 50 (so shown as `rsi_ma − 50`).
- **Bollinger Bands** (length 50, multiplier 0.35) around the primary QQE line. The histogram only turns the "strong" colour when the line breaks out of those bands.
- A **secondary QQE** (RSI 6, smoothing 5, factor 1.61) with a ±3 threshold as confirmation.
- Coloured bars: **blue** when both the primary Bollinger breakout and the secondary threshold agree on the upside, **red** when both agree on the downside, and grey otherwise.

The blue/red "both agree" bar is what the crypto trading community uses as the actual signal.

## Reading It

| Visual (QQE MOD) | Meaning |
|---|---|
| Blue histogram bars | Smoothed-RSI momentum is above its Bollinger band and confirmed by the secondary QQE, so bullish trend momentum |
| Red histogram bars | Bearish mirror image |
| Grey bars | Momentum inside its normal band, no signal. Often used as a "no-trade" filter |
| Line crossing its trailing level (classic QQE) | Momentum regime flip |

## Crypto Application

- **Trend-confirmation filter, not a trigger.** QQE MOD is mostly stacked with a baseline (for example [[ssl-channel|SSL]] Hybrid, an EMA or [[supertrend]]) as the "momentum agrees" condition. Retail systems such as "QQE MOD + SSL Hybrid + Waddah Attar Explosion" (kevinmck100, https://www.tradingview.com/script/YCob5r03-QQE-MOD-SSL-Hybrid-Waddah-Attar-Explosion/) are built this way.
- **Grey-bar chop filter.** Crypto trend systems whipsaw in ranges. Skipping entries while QQE MOD is grey is a cheap, parameter-light way to cut trade count.
- **NNFX role.** In the [[nnfx-method|NNFX]] stack, QQE fits the **C1/C2 confirmation** slot, and its grey-bar state can serve as a volatility filter. The kevinmck100 combo above follows the NNFX pattern: baseline, then confirmation, then [[waddah-attar-explosion]] as the volume filter. If QQE is C1, pick a C2 that isn't built on RSI, such as [[vortex-indicator]], because two RSI-based confirmations add little. Stonehill's indicator library doesn't list a QQE profile (checked 2026-09-28) (Source: [[stonehill-forex-nnfx]]).
- **Fast RSI length.** The default RSI length of 6 is very responsive. On 5m-15m crypto charts it flips constantly, so 1h-4h is the more common deployment.

## Common Pitfalls

- **Stacked lag.** An RSI, then an EMA, then a double-smoothed band, then Bollinger on top. By the time bars turn blue, a good part of a short move is gone.
- **Parameter surface.** Six to eight tunable inputs (two RSI lengths, two factors, BB length and multiplier, threshold) make QQE MOD easy to curve-fit. Fix the published defaults before testing ([[overfitting]]).
- **Magic constants.** The 4.236 factor is a Fibonacci-flavoured choice with no statistical derivation. Test it for robustness instead of assuming it is optimal.
- **Combo-strategy results.** Multi-indicator combos built on QQE MOD usually publish Strategy Tester results with default zero commission. Re-test them per the checklist in [[tradingview-platform#Community Scripts as an Idea Source]].

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500`: closes for RSI, the QQE bands and Bollinger on the QQE line
- `GET /api/v1/hyperliquid/candles?coin=SOL&interval=1h&limit=500`: perp bars for Hyperliquid coins

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep archive for testing blue/red-bar persistence and grey-bar filtering

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=500"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute**: from `GET /api/v1/market-data/klines`, build the primary and secondary QQE plus the 50/0.35 Bollinger filter on closed bars and emit a blue/red/grey state per bar
- **Use as a gate**: pass trend-system entries (for example [[supertrend]] flips) only when the QQE MOD state agrees, and log how many trades the grey filter removes
- **Regime check**: `GET /api/v1/regimes/current`. A persistent grey QQE state and a range regime label are two views of the same chop, so do not count them as independent confirmation
- **Backtest**: `GET /api/v1/backtesting/klines` to run with and without the QQE gate, net of costs, and compare trade count, win rate and drawdown

## Related

- [[rsi]]: the base input
- [[atr]]: the volatility logic QQE applies to the RSI axis
- [[bollinger-bands]]: the QQE MOD breakout filter
- [[ssl-channel]]: the baseline QQE MOD is most often paired with
- [[supertrend]]: the same ratcheting-band idea on price
- [[nnfx-method]]: the baseline/C1/C2/volume framework QQE is often slotted into
- [[tradingview-community-scripts]], [[pine-script]]: where the script lives

## Sources

- Mihkel00, "QQE MOD", TradingView, 2020-01-20 (updated 2024-12-11) (Source: [[tradingview-community-scripts]])
