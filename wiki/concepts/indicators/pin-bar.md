---
title: "Pin Bar"
type: concept
created: 2026-04-15
updated: 2026-06-22
status: excellent
tags: [indicators, technical-analysis, price-action, swing-trading]
aliases: ["Pin Bar", "pin-bar", "Pinocchio Bar", "Rejection Candle", "Pin Bars"]
related: ["[[candlestick-patterns]]", "[[price-action]]", "[[hammer]]", "[[support-and-resistance]]", "[[trend]]", "[[engulfing-pattern]]", "[[doji]]", "[[reversal-patterns]]", "[[confluence]]", "[[swing-high]]", "[[swing-low]]", "[[market-structure]]", "[[false-signals]]"]
domain: [indicators]
prerequisites: ["[[candlestick-patterns]]", "[[price-action]]"]
difficulty: beginner
---

A pin bar (short for "Pinocchio bar") is a single-candlestick [[price-action]] pattern with a small real body and one long wick (tail) that is at least two to three times the length of the body, signalling that price probed in one direction and was sharply **rejected**. It is one of the most widely used reversal signals in discretionary price-action trading, prized because it encodes a complete supply/demand story in a single bar.

## Overview

The defining geometry of a pin bar:

- A **long wick (tail/nose)** — typically ≥ 2/3 of the total bar range — pointing in the direction of the rejected move.
- A **small real body** at the opposite end of the bar.
- A **short or absent wick** on the body side.

Two orientations:

- **Bullish pin bar** — long lower wick, body near the top. Price was pushed down during the bar but buyers reclaimed control and closed it high. This is structurally identical to a [[hammer]] when it appears after a downtrend, and typically forms at [[support]] / a prior [[swing-low]].
- **Bearish pin bar** — long upper wick, body near the bottom. Price spiked up but sellers rejected the high (a "shooting star" in classic candlestick terms), typically at [[resistance]] / a prior [[swing-high]].

The wick is the signal: it marks a level that the market tested and refused to accept, leaving stranded orders and a clear invalidation point.

### Bullish vs Bearish Pin Bar

| Feature | Bullish pin bar | Bearish pin bar |
|---|---|---|
| Long wick | Lower (below the body) | Upper (above the body) |
| Body location | Upper third of range | Lower third of range |
| Classic name | [[hammer]] (after downtrend) | Shooting star (after uptrend) |
| Story | Sellers pushed down, buyers reclaimed | Buyers pushed up, sellers rejected |
| Best location | At [[support]] / [[swing-low]] | At [[resistance]] / [[swing-high]] |
| Entry trigger | Break of bar's high | Break of bar's low |
| Stop | Below the lower wick tip | Above the upper wick tip |

## How It Works

A pin bar's information comes from the path of price within the bar, not just its close. During the period, price extended into the wick region — hitting stops, triggering breakout entries, or sweeping liquidity — and then reversed hard enough to close back near the open. The long wick therefore represents trapped traders on the wrong side, whose stops become fuel for the reversal.

Practical recognition rules used by most price-action traders:

1. Wick length ≥ 2× (often 3×) the real body.
2. Real body in the upper third (bullish) or lower third (bearish) of the bar's range.
3. The "nose" should ideally protrude beyond surrounding bars, sweeping a recent swing high/low.

Context is everything: an isolated pin bar in the middle of a range is noise. A pin bar gains weight when it forms **at a [[confluence]]** — a [[support-and-resistance]] level, a prior [[swing-high|swing point]], a [[moving-averages|moving average]], or a Fibonacci retracement — and **with the trend** on the higher timeframe.

## Worked Example (illustrative)

A stock is in an [[trend|uptrend]] and pulls back to a rising 20-period [[moving-averages|moving average]] that coincides with a prior [[swing-low]] near $50 — a [[confluence]] zone. A daily candle then prints:

| Field | Price |
|---|---|
| Open | $50.40 |
| High | $50.70 |
| Low | $48.90 |
| Close | $50.30 |

- **Total range** = $50.70 − $48.90 = **$1.80**.
- **Real body** = |$50.40 − $50.30| = **$0.10** (tiny).
- **Lower wick** = $50.30 − $48.90 = **$1.40** (≈ 78% of the range; ~14× the body).
- **Upper wick** = $50.70 − $50.40 = **$0.30**.

This is a textbook **bullish pin bar**: wick ≫ 2× body, body in the upper third, lower wick sweeping below the prior swing low (a [[swing-low|liquidity sweep]]) before snapping back. The trade:

- **Entry** = $50.71, on a break above the pin bar's high.
- **Stop** = $48.85, just below the wick tip (the rejected level / invalidation). **Risk ≈ $1.86 per share.**
- **Target** = next [[resistance]] at $54.45, a 3:1 reward-to-risk ($3.74 reward vs $1.86 risk).

The small stop relative to the move is exactly why pin bars are prized: the rejected wick gives a logically defined, tight invalidation. Had the same candle printed in mid-range with no [[confluence]], it would be treated as noise, not a signal.

## Trading Relevance

A typical pin-bar trade:

- **Entry**: on a break of the pin bar's body in the rejection direction (e.g., above the high of a bullish pin), or on a 50% retracement entry into the bar.
- **Stop**: just beyond the tip of the wick — the level the market explicitly rejected. This gives a tight, logically-defined invalidation.
- **Target**: the next [[support-and-resistance]] level or a fixed reward-to-risk multiple (commonly 2:1 or 3:1, which the small stop distance makes achievable).

Pin bars work best as [[reversal-patterns|reversal]] signals at the edge of a range or as **continuation** signals when they form on a pullback within a trend (a bullish pin bar bouncing off [[support]] in an [[trend|uptrend]]). The chief weakness is subjectivity and noise: lower timeframes produce many pin bars, most of which fail. They are difficult to backtest systematically because the "quality" of a pin bar depends on contextual judgment — the same reason price-action methods in general resist mechanization. Filtering by trend, location, and timeframe (daily and 4H pin bars are far more reliable than 5-minute ones) is the standard way to raise the hit rate.

## How Traders Use It

- **With the trend, on a pullback.** The highest-probability use is a continuation signal: a bullish pin off [[support]] inside an [[trend|uptrend]], confirming the dip is being bought. See [[market-structure]].
- **At range extremes.** A bearish pin at the top of a range, or a bullish pin at the bottom, signals the boundary is holding — a [[mean-reversion]] fade.
- **Stacked with [[confluence]].** Pros require ≥2 reasons to be at the level (e.g., prior [[swing-high]] + 200-day MA + round number). The more reasons, the higher the conviction and the smaller the position-relative risk.
- **As an exit/scale signal.** A counter-trend pin bar against an open position is a warning to tighten stops or take partial profit.

## Common Pitfalls and Risks

- **Location-blind trading.** A pin bar mid-range or against the higher-timeframe [[trend]] is mostly noise and a leading source of [[false-signals]].
- **Lower-timeframe overtrading.** 1–5 minute charts spew pin bars that fail at a high rate; reliability rises sharply on 4H/daily.
- **Ignoring the close.** A long wick with a body in the *middle* of the range is a [[doji]] / indecision bar, not a pin bar — the body must sit at one extreme.
- **Stop too tight on the tip.** Placing the stop exactly at the wick tip invites [[false-signals|stop-hunting]] / [[whipsaw]]; a small buffer beyond the tip is safer.
- **Confirmation lag trade-off.** Waiting for the body break gives a later, worse entry but filters fakeouts — a deliberate cost, not a free lunch.

## Sources

- Steve Nison, *Japanese Candlestick Charting Techniques* (1991) — the canonical reference for the hammer/shooting-star formations that pin bars generalize.
- Martin Pring, *Technical Analysis Explained* — candlestick reversal patterns and confirmation.
- Al Brooks, *Reading Price Charts Bar by Bar* — price-action context and single-bar reversal signals.
- General market knowledge; worked example above is illustrative, not from a specific ingested wiki source.

## Related

- [[candlestick-patterns]]
- [[price-action]]
- [[reversal-patterns]] — the broader category
- [[hammer]] — the classic bullish single-bar reversal a pin generalizes
- [[doji]] — indecision bar, contrast with the pin's offset body
- [[engulfing-pattern]]
- [[support-and-resistance]]
- [[confluence]] — pins gain weight when stacked with other reasons
- [[swing-high]] / [[swing-low]] — pins often sweep these before reversing
- [[market-structure]] — trend context that validates a pin
- [[trend]]
- [[false-signals]] — out-of-context pins are a common fakeout
