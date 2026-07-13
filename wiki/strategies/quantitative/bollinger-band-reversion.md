---
title: "Bollinger Band Reversion"
type: strategy
created: 2026-04-06
updated: 2026-07-13
status: good
tags: [mean-reversion, bollinger-bands, volatility, quantitative, john-bollinger]
aliases: ["Bollinger Band Mean Reversion", "Bollinger Bounce", "BB Reversion Strategy"]
strategy_type: quantitative
timeframe: swing|intraday
markets: [stocks, crypto, forex]
complexity: beginner
backtest_status: untested
related: ["[[bollinger-bands]]", "[[rsi-mean-reversion]]", "[[mean-reversion]]", "[[keltner-channels]]", "[[donchian-channel-breakout]]", "[[cryptodataapi]]"]
---

# Bollinger Band Reversion

## Overview

Bollinger Bands, created by **John Bollinger** in the 1980s, consist of a 20-period [[simple-moving-average|SMA]] (middle band) with upper and lower bands set at 2 standard deviations above and below. Since standard deviation measures volatility, the bands expand when volatility increases and contract when it decreases. Statistically, approximately 95% of price action falls within 2 standard deviation bands.

The **Bollinger Band Reversion** strategy is a [[mean-reversion]] approach: buy when price touches or pierces the lower band (statistically cheap relative to recent history) and sell when price reaches the upper band (statistically expensive). The premise is that extreme moves to the bands are unsustainable and price will revert toward the middle band (the 20-period SMA).

A critical concept is the **Bollinger Squeeze**: when the bands narrow to an unusually tight range, it signals a period of low volatility that typically precedes a significant breakout. The squeeze itself is not directional -- it signals that a big move is coming but not which way. Combining the squeeze with [[rsi-mean-reversion|RSI]] or [[volume]] can help determine direction.

## Rules

### Entry
1. **Long Entry:** Price closes at or below the lower Bollinger Band. For stronger confirmation, wait for the next candle to close back inside the bands (a "touch and recover").
2. **Short Entry / Sell:** Price closes at or above the upper Bollinger Band. Wait for a candle close back inside for confirmation.
3. **RSI Confirmation (recommended):** Combine with [[rsi]]. Buy only when price touches the lower band AND RSI(14) < 30. Sell only when price touches the upper band AND RSI(14) > 70. This dual-confirmation dramatically reduces false signals.

### Exit
1. **Middle Band Exit:** Close the position when price reaches the 20-period SMA (middle band). This is the most conservative target and captures the "reversion to mean."
2. **Opposite Band Exit:** Hold until price reaches the opposite Bollinger Band for maximum profit (lower band to upper band).
3. **Stop-Loss:** Place a stop 1-2x [[atr]] beyond the entry band (e.g., if buying at the lower band, stop at lower band minus 1.5x ATR).

### Bollinger Squeeze Setup
1. Identify a squeeze: Bollinger Band Width (upper - lower) / middle drops to its lowest level in 6+ months.
2. Wait for the squeeze to "fire" -- a decisive close outside either band with expanding volume.
3. Trade in the breakout direction. This is a momentum/breakout play, not mean-reversion.

## Indicators Used
- [[bollinger-bands]] (20-period SMA, 2 standard deviations)
- [[rsi]] (14-period) for oversold/overbought confirmation
- [[atr]] for stop-loss placement
- **Bollinger Band Width** or **%B** for squeeze detection
- [[volume]] to gauge conviction at band touches

## Example Trade
**Asset:** MSFT (Microsoft), daily chart
1. MSFT has been ranging between $380-$410 for 6 weeks. Bollinger Bands: upper $412, middle $395, lower $378.
2. A broad market selloff drops MSFT to $376, closing below the lower band. RSI(14) = 26 (oversold). Dual confirmation.
3. Next day, MSFT opens at $378 and closes at $382 (back inside the bands). Enter long at $382.
4. Stop-loss: lower band ($378) minus 1.5x ATR ($4.50) = $373.50. Risk = $8.50.
5. Over 5 trading days, MSFT reverts to the middle band at $395. Exit at $395.
6. **Result:** +$13 per share (3.4% gain), risking $8.50. Reward-to-risk: 1.53:1.

## "Walking the Bands" Warning
When price "walks" along a Bollinger Band -- closing repeatedly at or beyond the band for multiple sessions -- it signals a powerful trend, NOT an imminent reversal. Selling the upper band walk in a strong uptrend or buying the lower band walk in a strong downtrend is a common and costly mistake. Always confirm mean-reversion conditions: the market should be range-bound, not trending. Use [[adx]] < 25 or the 200-day SMA slope as a ranging filter.

## Performance Characteristics
- **Win Rate:** 55-65% when combined with RSI confirmation. Lower (45-50%) without confirmation.
- **Profit Factor:** 1.3-1.8. The middle-band target is conservative but reliable.
- **Best Market Conditions:** Range-bound, low-ADX markets where price oscillates between the bands.
- **Worst Market Conditions:** Strong trending markets where price walks the bands for extended periods.

## Advantages
- Statistically grounded -- standard deviation bands have a mathematical basis
- Dynamically adapts to volatility (bands widen in volatile markets, narrow in quiet ones)
- The Bollinger Squeeze provides a high-probability setup for breakout trades
- Combines naturally with [[rsi-mean-reversion|RSI]] for powerful dual-confirmation signals
- Works across all markets and timeframes

## Disadvantages
- **Walking the bands** traps mean-reversion traders in trending markets
- The 20/2 default parameters are not optimal for every instrument -- may need tuning
- Targets are modest (middle band) unless you hold for the opposite band
- Standard deviation assumes a normal distribution, but financial returns are fat-tailed
- Requires patience -- the best setups (lower band + RSI < 30 + ranging market) are infrequent

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
- [[rsi-mean-reversion]] -- the ideal companion strategy for dual confirmation
- [[bollinger-bands]] -- detailed indicator explanation
- [[mean-reversion]] -- the broader strategy category
- [[donchian-channel-breakout]] -- a breakout (not reversion) channel strategy for comparison
- [[keltner-channels]] -- ATR-based channels that pair with Bollinger Bands for squeeze detection
