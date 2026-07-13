---
title: "Evening Star"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [indicators, technical-analysis]
aliases: ["Evening Star", "Evening Star Pattern", "Evening Doji Star"]
related: ["[[candlestick-patterns]]", "[[morning-star]]", "[[doji]]", "[[shooting-star]]", "[[support-resistance]]", "[[dow-theory]]", "[[munehisa-homma]]"]
domain: [indicators]
prerequisites: ["[[candlestick-patterns]]"]
difficulty: beginner
---

The evening star is a three-candle bearish reversal pattern that signals a potential top after an uptrend. It is the mirror image of the bullish [[morning-star]] and is one of the most reliable reversal formations in Japanese candlestick analysis, popularized in the West by Steve Nison.

## How It Works

The pattern forms over three trading sessions:

1. **Candle 1** — a large bullish (up) candle, confirming the prevailing uptrend and bullish sentiment.
2. **Candle 2** — a small-bodied candle (the "star") that gaps up from candle 1. The small body — bullish, bearish, or a [[doji]] — signals indecision and a loss of upward momentum. When candle 2 is a doji, the pattern is called an *evening doji star* and is considered a stronger signal.
3. **Candle 3** — a large bearish (down) candle that closes well into the body of candle 1 (ideally below its midpoint). This confirms that sellers have seized control.

The story the pattern tells: buyers push price higher (candle 1), momentum stalls at a new high (candle 2), then sellers overwhelm the market and reverse the move (candle 3). The deeper candle 3 penetrates candle 1's body, the stronger the reversal signal.

### Anatomy at a glance

| Candle | Body | Direction | Meaning |
|--------|------|-----------|---------|
| 1 | Large | Bullish (up) | Trend intact; bulls in control |
| 2 ("the star") | Small (or [[doji]]) | Either / indecision | Momentum stalls; buyers and sellers balanced |
| 3 | Large | Bearish (down) | Sellers take over; closes deep into candle 1's body |

A useful checklist for a "textbook" evening star: (a) a clear prior [[trend|uptrend]]; (b) candle 2's body is small and sits at the top, ideally gapping up; (c) candle 3 closes below the midpoint of candle 1's body; (d) confirmation from [[support-resistance|resistance]], [[volume]], or an overbought [[rsi]].

## Worked Example

Suppose a stock has been climbing and prints these three daily candles:

1. **Candle 1:** opens at **$50**, closes at **$56** — a strong green day; midpoint of the body is **$53**.
2. **Candle 2 (star):** gaps up, trades in a tight band between **$56.50** and **$57.20**, and closes near where it opened (~$56.80) — a small, indecisive body at a new high.
3. **Candle 3:** opens at **$56**, sells off all day, and closes at **$51** — a large red candle that closes *below* candle 1's midpoint of $53.

The evening star is complete. A trader might short on the close of candle 3 at **$51**, place a stop just above the star's high at **$57.30** (risk ≈ $6.30/share), and target the next [[support-resistance|support]] shelf at, say, **$45** (reward ≈ $6) — roughly a 1:1 setup before confirmation, improving if the breakdown accelerates. Waiting for a fourth lower candle to *confirm* trades a few dollars of entry for a higher hit-rate.

## Confirmation and Reliability

- **Location matters**: an evening star is only meaningful at the top of an established uptrend, ideally near [[support-resistance|resistance]], a prior high, or a Fibonacci extension. The same shape mid-range is noise.
- **Volume**: heavier [[volume]] on candle 3 strengthens the signal, indicating real selling pressure rather than a thin pullback.
- **Confirmation candle**: many traders wait for a fourth candle to close lower before acting, trading reliability for a later (and slightly worse) entry.
- **Gaps**: traditional Japanese versions require gaps between the bodies. In 24-hour markets like [[crypto]] and [[forex]], gaps are rare, so traders relax this requirement and focus on the small middle body and the bearish close.

## Trading Relevance

Traders use the evening star as a signal to exit longs or initiate short positions. A common approach: enter short on the close of candle 3 (or on confirmation), place a stop above the high of the star (candle 2), and target the nearest [[support-resistance|support]] level or a measured move. As a [[candlestick-patterns|candlestick pattern]], it works best as a trigger within a broader trend context — confluence with [[dow-theory]] trend exhaustion, overbought [[rsi]], or a resistance level greatly improves the win rate over trading the pattern in isolation. Like all single-pattern signals, it produces frequent false positives and should be combined with [[risk-management|risk management]] rather than treated as a standalone system.

### How traders use it across contexts

- **Exit signal for longs.** Even traders who never short use the evening star to take profits on an existing long after an extended run.
- **Short entry trigger.** Discretionary swing traders use the candle-3 close (or confirmation candle) as a defined-risk short entry with the star's high as a natural stop.
- **Multi-timeframe filter.** An evening star on the daily aligned with a [[death-cross]] or a falling [[moving-averages|moving average]] on the weekly is far stronger than the daily pattern alone.

## Comparison With Related Reversals

| Pattern | Candles | Bias | Note |
|---------|---------|------|------|
| **Evening star** | 3 | Bearish (top) | Small star between a strong up candle and a strong down candle |
| [[morning-star]] | 3 | Bullish (bottom) | Exact mirror image |
| [[shooting-star]] | 1 | Bearish (top) | Single candle, long upper wick |
| [[bearish-engulfing]] | 2 | Bearish (top) | Down candle fully engulfs prior up candle |

## Common Pitfalls

- **Trading it mid-range.** The same three-candle shape in the middle of a range is noise — location at the top of an established uptrend is what gives it meaning.
- **Ignoring penetration depth.** If candle 3 barely dips into candle 1's body, the reversal is weak; demand a close below the midpoint.
- **Skipping confirmation in choppy tape.** Without volume or a structural level, the pattern produces frequent false positives.
- **Forcing the gap requirement in 24-hour markets.** In [[crypto]] and [[forex]], gaps are rare; insisting on them filters out valid signals — focus on the small middle body and bearish close instead.

## Related

- [[candlestick-patterns]] — the broader family of price-action patterns
- [[morning-star]] — the bullish mirror image (bottom reversal)
- [[doji]] — the indecision candle that forms the strongest version of the star
- [[shooting-star]] — a related single-candle bearish reversal
- [[support-resistance]] — context that validates the reversal
- [[munehisa-homma]] — the historical originator of candlestick analysis

## Sources

- Nison, Steve. *Japanese Candlestick Charting Techniques* (1991) — the definitive Western reference on candlestick patterns including the evening star.
- Bulkowski, Thomas. *Encyclopedia of Candlestick Charts* (2008) — statistical reliability data for the evening star pattern.
