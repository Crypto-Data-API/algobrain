---
title: "Aroon"
type: concept
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [indicators, technical-analysis, trend-following, momentum]
aliases: ["Aroon Indicator", "Aroon Up/Down", "aroon", "Aroon Oscillator"]
domain: [indicators]
prerequisites: ["[[trend-following]]", "[[adx]]"]
difficulty: intermediate
related: ["[[tushar-chande]]", "[[adx]]", "[[trend-following]]", "[[moving-averages]]", "[[momentum]]", "[[breakout]]", "[[chande-momentum-oscillator]]"]
---

Aroon is a trend identification indicator developed by [[tushar-chande|Tushar Chande]] in 1995. The name derives from Sanskrit for "dawn's early light," reflecting its purpose: detecting the earliest stages of a new trend (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## How It Works

Aroon answers a question no other classic indicator frames quite the same way: *how many bars ago did the market last print a fresh high (or low) within the lookback window?* It converts that "time since extreme" into a 0–100 scale.

- **Aroon Up**: ((N − periods since N-period high) / N) × 100
- **Aroon Down**: ((N − periods since N-period low) / N) × 100
- Both oscillate between 0 and 100; default lookback is typically 25 periods

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

Read the formula literally. If today's bar is itself the highest high of the last N bars, then "periods since N-period high" = 0 and Aroon Up = ((N − 0)/N) × 100 = **100**. If the highest high in the window occurred N bars ago (the oldest bar), Aroon Up = ((N − N)/N) × 100 = **0**. Every fresh high resets Aroon Up to 100 and it then decays one step at a time (by 100/N per bar) until the next new high. Aroon Down behaves identically for new lows.

### Step values

With the default N = 25, each bar that passes without a new extreme drops the line by 100/25 = **4 points**. Choosing N changes both sensitivity and the step size:

| Lookback N | Step per bar (100/N) | Character |
|-----------|----------------------|-----------|
| 14 | ~7.1 | Fast, noisy — intraday / short swings |
| 25 (default) | 4.0 | Chande's original setting — swing trading |
| 50 | 2.0 | Slow, smooth — position / weekly trends |

A shorter N reacts to new highs/lows faster but whipsaws more; a longer N is steadier but lags trend changes — the same tradeoff that governs any [[moving-averages|moving average]] length.

### Worked example

Suppose N = 25 and the highest high of the last 25 daily bars occurred **6 bars ago**, while the lowest low occurred **20 bars ago**:

- Aroon Up = ((25 − 6)/25) × 100 = (19/25) × 100 = **76**
- Aroon Down = ((25 − 20)/25) × 100 = (5/25) × 100 = **20**
- Aroon Oscillator = 76 − 20 = **+56**

Reading: a recent high (Up = 76, above 70) and a stale low (Down = 20, below 30) with a strongly positive oscillator confirm a healthy, established uptrend. If price then prints a brand-new 25-day high tomorrow, Aroon Up snaps back to **100** and the bar count restarts.

## Key Signals

- **Aroon Up > 70, Aroon Down < 30**: strong uptrend
- **Aroon Down > 70, Aroon Up < 30**: strong downtrend
- **Crossovers**: Aroon Up crossing above Aroon Down suggests bullish trend emergence
- **Both below 50**: consolidation / no clear trend

(Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]])

### Signal reference table

| Condition | Aroon Up | Aroon Down | Oscillator | Interpretation |
|-----------|----------|-----------|-----------|----------------|
| Strong uptrend | > 70 | < 30 | strongly + | Frequent new highs, stale lows — ride / hold longs |
| Strong downtrend | < 30 | > 70 | strongly − | Frequent new lows, stale highs — ride / hold shorts |
| Bullish crossover | rising through Down | falling | crosses above 0 | Emerging uptrend — early long trigger |
| Bearish crossover | falling | rising through Up | crosses below 0 | Emerging downtrend — early short / exit long |
| Consolidation | < 50 | < 50 | near 0 | No fresh extremes either way — stand aside |
| Parallel high (both > 70) | high | high | near 0 | Volatile, two-sided — new highs *and* lows; avoid |

The "both lines high" case is an underappreciated one: it means the market is making fresh highs *and* fresh lows inside the window — a wide, volatile range, not a clean trend. It is the inverse of the both-below-50 quiet consolidation and is a poor environment for trend entries.

## Comparison with ADX

Both Aroon and [[adx|ADX]] measure trend strength, but through different lenses. ADX measures the magnitude of directional movement; Aroon measures the *recency* of new highs/lows. Aroon tends to signal trend changes earlier, while ADX confirms established trends (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]).

## Aroon Oscillator

A common derived form is the **Aroon Oscillator = Aroon Up − Aroon Down**, which fluctuates between −100 and +100. Readings above zero indicate an uptrend bias and below zero a downtrend bias, with the magnitude reflecting trend strength. The oscillator form is convenient for systematic rules because it collapses the two lines into a single momentum-style series.

## Other Chande Contributions

Tushar Chande also created the [[chande-momentum-oscillator|Chande Momentum Oscillator]] and QStick indicator (Source: [[2026-04-20-comprehensive-guide-technical-trading-indicators]]). All three reflect Chande's signature design philosophy: build indicators that are normalized to a fixed bounded scale and that respond to the *structure* of price (timing of extremes, ratio of up-days to down-days) rather than to raw price magnitude.

## How Traders Use Aroon

- **Trend confirmation filter.** Many [[trend-following]] systems use Aroon as a gate: only take long signals from a primary system when Aroon Up > 70 (or the oscillator > 0), and stand aside entirely when both lines are below 50. This filters the chop where most trend systems bleed via whipsaws.
- **Early entry timing.** Because Aroon resets to 100 on the very bar of a new extreme, an Aroon Up crossover above Aroon Down often fires *before* a price [[breakout]] is confirmed by a [[moving-averages|moving-average]] cross — useful for getting in early, at the cost of more false starts.
- **Exit / trail signal.** A long held in an uptrend can be exited when Aroon Up drops back below 50 or the oscillator turns negative, signaling the most recent high is now stale and momentum has rotated.
- **Pairing with [[adx]].** A common two-stage rule: use Aroon for *direction and timing* (which way, how recently), and ADX for *strength confirmation* (is the trend strong enough to hold). Aroon turns first; ADX confirms it is worth the risk.

## Common Pitfalls

- **Premature flips in ranges.** Aroon's strength — reacting to recent extremes — is also its weakness. In a choppy [[support-and-resistance|range]], minor new highs and lows toggle the lines back and forth, generating whipsaw crossovers. Always combine with a regime filter (e.g., a long-period [[moving-averages|moving average]] slope or ADX threshold).
- **Misreading "100" as bullish strength.** Aroon Up = 100 only means a new high printed *this bar*; it says nothing about how far price will travel. It is a recency flag, not a magnitude or momentum forecast.
- **Lookback mismatch.** Using N = 25 on a 1-minute chart is far more sensitive than on a daily chart in clock terms. Match N to the timeframe and the holding period you actually trade.
- **Ignoring the both-lines-high case.** Treating two simultaneously high lines as "strong" is a classic error; it is a volatile, two-sided market, not a trend.

## Trading Relevance

Aroon's distinguishing feature is that it measures *time since the last extreme* rather than price magnitude, so it answers a specific question: "How recently did this market make a fresh high or low?" Trend-following traders use Aroon Up/Down crossovers as early entry triggers and the both-lines-below-50 condition as a filter to stand aside during consolidation (where most trend systems bleed via whipsaws). Because Aroon turns earlier than [[adx]], a common pairing is Aroon for entry timing and ADX for confirming the trend is strong enough to hold the position. Its main weakness is the same as its strength: by reacting to recent extremes it can flip prematurely in choppy ranges, so it is best combined with a [[moving-averages|moving-average]] regime filter.

## Sources

- Chande, Tushar S. & Kroll, Stanley (1994), *The New Technical Trader* (Wiley) — original publication of the Aroon indicator and Aroon Oscillator.
- Achelis, Steven B. (2000), *Technical Analysis from A to Z* (McGraw-Hill) — reference entry on Aroon construction and interpretation.
- [[2026-04-20-comprehensive-guide-technical-trading-indicators]] — Comprehensive Guide to Technical Trading Indicators (compiled research, 29 references)

## Related

- [[tushar-chande]]
- [[adx]]
- [[trend-following]]
