---
title: "UT Bot Alerts"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, trend-following, volatility, crypto]
aliases: ["UT Bot", "UT Bot Alerts", "UTBot"]
domain: [indicators, technical-analysis]
prerequisites: ["[[atr]]", "[[trailing-stop]]"]
difficulty: beginner
related: ["[[atr]]", "[[atr-trailing-stop]]", "[[supertrend]]", "[[chandelier-exit]]", "[[heikin-ashi]]", "[[halftrend]]", "[[tradingview-community-scripts]]", "[[pine-script]]"]
---

**UT Bot Alerts** is an [[atr|ATR]] trailing-stop indicator that prints buy and sell labels when price crosses a volatility-scaled stop line. The widely used TradingView version was published by **QuantNomad** on 2020-02-08. The script page credits **Yo_adriiiiaan** as the original developer and **HPotter** with the original idea (https://www.tradingview.com/script/n8ss8BID-UT-Bot-Alerts/). With about 1.6M views as of 2026-09-28 it is one of the most-viewed open-source trend tools on the platform, and it is widely wired into webhook bots for crypto perps (Source: [[tradingview-community-scripts]]).

## How It Works

Two inputs: **Key Value** `a` (sensitivity multiplier, default 1) and **ATR Period** `c` (default 10), plus an option to use [[heikin-ashi]] closes as the source.

1. `n_loss = a × ATR(c)`.
2. A **trailing stop** that ratchets:
   - If price was above the prior stop and still is, the stop becomes `max(prev_stop, src − n_loss)`, so it only rises.
   - If price was below the prior stop and still is, the stop becomes `min(prev_stop, src + n_loss)`, so it only falls.
   - If price crosses the stop, it resets to `src − n_loss` (now long) or `src + n_loss` (now short).
3. **Signals**: a **buy** when the source crosses above the stop (the script compares an EMA(1) of the source, which is simply the source itself, with the stop), and a **sell** when it crosses below.

This is the generic [[atr-trailing-stop]] turned into a stop-and-reverse signal generator. It differs from [[supertrend]] in two ways: the stop is anchored on the close (not `hl2`), and the default multiplier is 1× ATR rather than 3×. That makes UT Bot far more sensitive, and it flips much more often.

```python
n_loss = key * atr(high, low, close, period)
stop = np.zeros(len(src)); pos = 0
for i in range(1, len(src)):
    p, s = stop[i-1], src.iat[i]
    if s > p and src.iat[i-1] > p:   stop[i] = max(p, s - n_loss.iat[i])
    elif s < p and src.iat[i-1] < p: stop[i] = min(p, s + n_loss.iat[i])
    else: stop[i] = s - n_loss.iat[i] if s > p else s + n_loss.iat[i]
buy  = (src > stop) & (src.shift(1) <= pd.Series(stop).shift(1).values)
```

## Parameter Behaviour

| Key Value | ATR period | Behaviour |
|---|---|---|
| 1 (default) | 10 | Very sensitive. Many flips, suited to scalping with a separate trend filter |
| 2 | 10 | Moderate. A common swing-trade setting on crypto 1h-4h |
| 3+ | 10-14 | Close to SuperTrend or Chandelier behaviour. Fewer, longer trades |

## Crypto Application

- **Bot trigger.** The alert conditions ("UT Long" / "UT Short") make it a favourite webhook source for perp bots. Because of that popularity, the default-setting signal is crowded and its flips cluster with other retail stops.
- **Heikin-Ashi option.** Enabling HA smooths flips, but see the pitfall below.
- **Needs a filter.** At Key Value 1 in ranging crypto markets it whipsaws continuously. Most published UT Bot strategies add an EMA-200 trend filter, a higher-timeframe UT Bot, or a chop filter such as [[qqe|QQE MOD]]'s grey state.

## Common Pitfalls

- **Heikin-Ashi fills.** With HA enabled, TradingView strategy wrappers can fill at synthetic HA prices, not real prices. That massively inflates backtests. Signals may use HA, but fills must use real OHLC ([[heikin-ashi]]).
- **Whipsaw cost.** Default settings on 15m crypto charts can produce hundreds of flips a year. At 10 bps round trip, turnover alone can erase the gross edge ([[whipsaw]], [[transaction-costs]]).
- **Intrabar signals.** Alerts set to "once per bar" instead of "once per bar close" fire and then disappear. Only closed-bar signals are reproducible.
- **Paid clones.** "Elite", "Pro" and "2026 Edition" repackagings are common. The open-source original is the reference to audit.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1h&limit=200`: OHLCV for ATR and the trailing stop
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=15m&limit=500`: perp bars when executing on Hyperliquid

**Historical data:**
- `GET /api/v1/backtesting/klines`: deep kline archive for sweeping Key Value and ATR period
- `GET /api/v1/backtesting/funding`: historical funding to charge carry on held perp positions

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=BTC&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-hyperliquid]], [[cryptodataapi-backtesting]].

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can work with this indicator directly:

- **Compute**: build the ratcheting stop from `GET /api/v1/market-data/klines` closes and ATR(10). Flip only on closed bars
- **Sensitivity sweep**: from `GET /api/v1/backtesting/klines`, test Key Value 1/2/3 × ATR 10/14 and report flips per year next to net return. The turnover column usually decides the setting
- **Carry**: on perps, charge `GET /api/v1/backtesting/funding` history against every bar a position is held, because stop-and-reverse systems are always in the market
- **Regime gate**: suppress new flips when `GET /api/v1/volatility/regime` reads compressed or range conditions, where UT Bot whipsaws most

## Related

- [[atr-trailing-stop]]: the generic family UT Bot belongs to
- [[supertrend]], [[chandelier-exit]], [[halftrend]]: sibling ATR trend lines
- [[heikin-ashi]]: the optional smoothed source
- [[whipsaw]]: the main failure mode at default settings
- [[tradingview-community-scripts]], [[pine-script]]: where the script lives

## Sources

- QuantNomad, "UT Bot Alerts", TradingView, 2020-02-08. Credits Yo_adriiiiaan and HPotter (Source: [[tradingview-community-scripts]])
