---
title: RSI Divergence Strategy
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: good
tags:
  - momentum
  - rsi
  - divergence
  - reversal
  - oscillator
strategy_type: momentum
timeframe: swing
markets:
  - stocks
  - crypto
  - forex
complexity: intermediate
backtest_status: untested
related:
  - "[[cryptodataapi]]"
  - "[[macd-crossover]]"
  - "[[support-resistance-breakout]]"
  - "[[rate-of-change]]"
  - "[[mean-reversion]]"
---

# RSI Divergence Strategy

## Overview

RSI divergence occurs when price action and the [[relative-strength-index]] (RSI) move in opposite directions, signaling a potential reversal. This is one of the most powerful tools in a technical trader's arsenal because it reveals weakening [[momentum]] beneath the surface of price. **Regular divergence** signals reversals: bearish divergence (price makes a higher high, RSI makes a lower high) and bullish divergence (price makes a lower low, RSI makes a higher low). **Hidden divergence** confirms trend continuation. Combining divergence with key [[support-resistance]] levels dramatically improves accuracy.

## Rules

### Entry Rules
1. **Bearish Divergence (Short):** Price prints a **higher high** while RSI prints a **lower high**. RSI should ideally be in or near the overbought zone (above 60-70). Enter short when price confirms the reversal with a bearish candle pattern (e.g., [[bearish-engulfing]], [[evening-star]]) at a [[resistance]] level.
2. **Bullish Divergence (Long):** Price prints a **lower low** while RSI prints a **higher low**. RSI should be in or near oversold territory (below 30-40). Enter long on a bullish confirmation candle at a [[support]] level.
3. **Hidden Divergence (Trend Continuation):** In an uptrend, price makes a higher low but RSI makes a lower low -- this confirms the trend will continue. Enter on the pullback.
4. **Multi-Timeframe Confirmation:** Identify divergence on the daily chart, then drop to the 4H or 1H chart for precise entry timing.

### Exit Rules
1. **Target:** Aim for the previous swing high (for longs) or swing low (for shorts) as the first target.
2. **RSI Extreme Exit:** Close when RSI reaches the opposite extreme (e.g., overbought after a bullish divergence entry).
3. **Stop Loss:** Place stops beyond the extreme of the divergence pattern -- below the lowest low for bullish divergence, above the highest high for bearish.
4. **Trailing Stop:** Use a [[chandelier-exit]] or ATR-based trailing stop once the trade moves 1R in your favor.

## Indicators Used

| Indicator | Settings | Purpose |
|-----------|----------|---------|
| [[relative-strength-index]] | 14-period (standard) | Divergence detection |
| [[support-resistance]] | Key horizontal levels | Confluence for entries |
| [[volume]] | N/A | Confirm exhaustion at extremes |
| [[candlestick-patterns]] | N/A | Entry confirmation |
| [[atr]] | 14-period | Stop loss sizing |

## Example Trade

**Setup:** ETH/USD daily chart. Price rallies to $3,800, printing a higher high compared to the prior swing at $3,600. However, RSI reads 62, lower than the prior swing's RSI of 71. Bearish divergence identified at a known [[resistance]] zone.

**Entry:** A [[bearish-engulfing]] candle forms at $3,780. Enter short at $3,760 on the next candle open.

**Management:** Stop loss placed at $3,850 (above the high). Risk = $90 per unit. First target at prior support $3,500 (reward = $260, R/R = 2.9:1).

**Exit:** Price drops to $3,500 target. Partial profit taken. Remaining position trailed with 2x [[atr]] stop, eventually closing at $3,350.

## Performance Characteristics

- **Win Rate:** 55-65% when combined with support/resistance and confirmation candles
- **Best Conditions:** Extended trends approaching exhaustion at key levels
- **Worst Conditions:** Strong trending markets where divergence can persist for extended periods before resolving
- **Average Holding Period:** 3-15 days depending on timeframe
- **Key Risk:** Divergence can "stack" -- multiple divergences may form before price actually reverses

## Advantages

- Identifies reversals **before** they happen, offering excellent risk/reward entries
- Works on all timeframes and all liquid markets
- Hidden divergence provides a powerful trend continuation tool often overlooked by traders
- Combines naturally with [[support-resistance]], [[fibonacci-retracements]], and [[candlestick-patterns]]
- RSI is available on every charting platform

## Disadvantages

- Divergence is **not** a timing tool -- it shows potential, not certainty, and can persist for many bars
- Requires patience and discretion; not easily automated without additional filters
- In strong trends, bearish divergence can form repeatedly while price keeps rising (the "divergence trap")
- Subjective element in identifying swing points for comparison
- Should always be confirmed with price action; never trade divergence alone without [[confluence]]

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
