---
title: "Supertrend"
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [trend-following, supertrend, atr, trailing-stop, technical-analysis]
aliases: ["Supertrend Indicator", "Supertrend Strategy", "ATR Trailing Stop"]
strategy_type: technical
timeframe: scalp|intraday|swing
markets: [stocks, crypto]
complexity: beginner
backtest_status: untested
related: ["[[parabolic-sar]]", "[[atr]]", "[[moving-average-crossover]]", "[[ichimoku-cloud]]", "[[cryptodataapi]]"]
---

# Supertrend

## Overview

The Supertrend indicator is an [[atr]]-based trend-following overlay that plots a single line above or below price, flipping sides when the trend changes direction. When the Supertrend line is below price and colored green, the trend is bullish. When above price and colored red, the trend is bearish. The flip from one side to the other generates the buy/sell signal.

The calculation uses a basic upper and lower band derived from the [[atr]]:
- **Upper Band** = (High + Low) / 2 + (Multiplier x ATR)
- **Lower Band** = (High + Low) / 2 - (Multiplier x ATR)

The Supertrend value follows the lower band during uptrends (it can only rise, never fall) and the upper band during downtrends (it can only fall, never rise). This ratcheting behavior makes it an effective [[trailing-stop]].

The indicator has become especially popular in Indian equity markets (NSE/BSE) and in [[crypto]] trading, where its clean visual output and simple interpretation appeal to retail traders. It is available on virtually every charting platform including TradingView, Zerodha Kite, and MetaTrader.

## Rules

### Entry
1. **Long Entry:** Supertrend flips from red (above price) to green (below price). Enter at the candle close that triggers the flip.
2. **Short Entry:** Supertrend flips from green (below price) to red (above price). Enter at the candle close.
3. **Trend Filter (optional):** Only take long signals when a higher-timeframe Supertrend is also green, and short signals when it is red. For example, use the daily Supertrend as a filter for 1-hour signals.

### Exit
1. **Supertrend Flip:** Exit the trade when Supertrend flips to the opposite color. This is the primary exit.
2. **Fixed Target:** Take profit at a predefined risk-reward ratio (e.g., 2:1 or 3:1) using the distance from entry to the Supertrend line as the risk unit.
3. **Supertrend as Trailing Stop:** Simply trail your stop at the Supertrend value, adjusting each period.

### Parameters
| Parameter | Default | Description |
|-----------|---------|-------------|
| ATR Period | 10 | Lookback for [[atr]] calculation |
| Multiplier | 3.0 | How many ATRs away from median price |

- **Higher multiplier** (e.g., 4.0) = fewer signals, wider stops, stays in trends longer, misses fewer big moves.
- **Lower multiplier** (e.g., 2.0) = more signals, tighter stops, earlier entries/exits, more whipsaws.
- Popular alternative: ATR Period 7, Multiplier 2.0 for faster signals on lower timeframes.

## Indicators Used
- **Supertrend** (ATR period + multiplier)
- [[atr]] (built into the Supertrend calculation)
- [[volume]] for confirming breakout strength on flips
- [[rsi]] or [[macd]] as optional momentum filters to reduce false flips

## Example Trade
**Asset:** NIFTY 50 Index, 15-minute chart (intraday)
1. Morning session opens. NIFTY is at 22,400. Supertrend (10, 3) is red at 22,480 (above price, bearish).
2. At 10:15 AM, a strong bullish candle closes at 22,500, above the Supertrend. The indicator flips green at 22,350.
3. Enter long at 22,500. Stop-loss at the Supertrend line: 22,350. Risk = 150 points.
4. NIFTY rallies through the session. The Supertrend trails upward: 22,380... 22,420... 22,460... 22,510.
5. At 2:30 PM, NIFTY stalls at 22,650 and pulls back. Supertrend is at 22,540. Price hits 22,540 and the indicator flips red.
6. Exit at 22,540. **Result:** +40 points net (entry 22,500, exit 22,540), or target a fixed 2:1 earlier at 22,800 if still trending.

## Performance Characteristics
- **Win Rate:** 35-45% on its own. Rises to 50%+ with a higher-timeframe trend filter.
- **Profit Factor:** 1.3-2.0. The trailing nature captures meaningful trend moves but returns profits during whipsaws.
- **Best Market Conditions:** Clean trending markets with sustained directional momentum. Crypto bull runs, equity breakouts, trending forex pairs.
- **Worst Market Conditions:** Sideways, mean-reverting markets. The indicator flips repeatedly, producing a sequence of small losses.

## Advantages
- Extremely simple: one line, two colors. No interpretation ambiguity
- Built-in [[trailing-stop]] that adapts to volatility via [[atr]]
- Works on all timeframes from 1-minute scalping to weekly position trading
- Low computational cost -- easy to code in Pine Script, Python, or any platform
- Multi-timeframe confirmation (daily + hourly) significantly improves signal quality

## Disadvantages
- **Whipsaw-prone** in sideways markets, like all trend-following indicators
- The default parameters (10, 3) are not universally optimal -- each instrument may need tuning
- **Late entries:** By the time the Supertrend flips, a significant portion of the move has already occurred
- No volume or momentum component -- purely price-based
- The simplicity can be a trap: beginners may over-rely on it without understanding market context

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

## See Also
- [[parabolic-sar]] -- Wilder's classic trailing stop indicator; Supertrend is often viewed as its modern successor
- [[atr]] -- the volatility measure at the core of Supertrend's calculation
- [[moving-average-crossover]] -- another beginner-friendly trend signal, but uses two lines instead of one
- [[ichimoku-cloud]] -- a more comprehensive (but more complex) trend system
- [[trailing-stop]] -- the general concept Supertrend implements
