---
title: "Average Candle Range (ACR)"
type: concept
created: 2026-06-19
updated: 2026-06-20
status: good
tags: [technical-analysis, indicators, volatility, range]
aliases: ["ACR", "Average Candle Range", "average bar range", "average box range"]
domain: [technical-analysis]
prerequisites: ["[[candlestick-patterns]]"]
difficulty: beginner
related: ["[[arc-strategy]]", "[[average-true-range]]", "[[candlestick-patterns]]", "[[box-and-swing-structure]]", "[[support-and-resistance]]"]
---

# Average Candle Range (ACR)

**Average Candle Range (ACR)** is the mean high-to-low distance of recent candles (or of a defined price "box") over a chosen lookback, used as a volatility filter and as the basis for range-derived profit targets. It answers a single practical question: *how far does this instrument typically travel in a candle or a session, and is the current move large enough to act on?* ACR is the quantitative backbone of the [[arc-strategy|ARC (Area-Range-Candle)]] method's middle step.

## Overview

ACR generalizes a simple idea that price-action traders apply manually: measure the distance an instrument moves and express trade filters and targets as a fraction of that distance, rather than as fixed dollar or pip amounts. This makes rules portable across instruments and adaptive across volatility regimes — a 60-cent move means something very different on a $3-range stock than on a $300-range stock.

In the [[arc-strategy|ARC]] method, the relevant "candle range" is the **box range** — the vertical distance between the box high and box low (see [[box-and-swing-structure]]). The educator in the source video measures this box and then uses it in two distinct ways: as a minimum-move filter and as a profit-target scale (Source: gap-finder Perplexity research 2026-06-19).

## Calculation

The rolling form is straightforward:

```
candle_range[i]   = high[i] - low[i]
ACR(n)            = mean(candle_range[i-n+1 .. i])     # average over last n candles
```

For the box-based form used by ARC, the "range" is a single session/box measurement rather than a rolling average:

```
box_range = box_high - box_low
```

Lookback choice (`n`) trades responsiveness against stability: short lookbacks (5-10) track recent volatility expansion and contraction; longer lookbacks (20-50) give a smoother baseline less distorted by single outlier candles.

## Use 1: Volatility / Minimum-Move Filter

ACR (or box range) sets a threshold below which a setup is ignored as noise. In ARC, the rule is that price must travel **at least 20% of the box range in one uninterrupted, un-pulled-back move** before a reversal setup is considered valid (Source: gap-finder Perplexity research 2026-06-19, [video](https://www.youtube.com/watch?v=T7QN-yqryr4)).

Worked example from the source: a box spanning ~$3.00 per share gives a minimum move of `0.20 × $3.00 = $0.60`. The trader waits to see at least a 60-cent one-way move before looking for an entry. The purpose is to avoid taking reversals too early in choppy, mean-reverting conditions where the move may still be in its noisy early phase.

## Use 2: Range-Based Profit Targets

The same range measure sets exits. ARC targets are typically placed at **50-100% of the box range**, often aligned with the opposite-side level (box low/swing low for a short from the box high, and vice versa) (Source: gap-finder Perplexity research 2026-06-19). On the ~$3.00 box example, that is roughly a $1.50-$3.00 target. Expressing targets as a fraction of measured range keeps profit objectives proportional to the day's actual volatility rather than chosen arbitrarily.

## Relationship to ATR

ACR is closely related to [[average-true-range|Average True Range (ATR)]] but not identical. ATR incorporates gaps by using the *true range* — the greatest of (high-low), (high-prior close), and (low-prior close) — so it accounts for overnight jumps. A naive ACR using only `high - low` ignores gaps. For gap-prone instruments, ATR is the more conservative volatility estimate; for intraday range-and-target work where each candle is treated on its own terms, the simpler candle range is often what practitioners actually measure. Both serve the same role: a volatility yardstick for sizing filters, stops, and targets.

## Limitations and False Signals

ACR is a descriptive measure of how far price has been moving, not a predictive one — it tells you the size of recent ranges, not their direction or whether the next range will be similar. Several pitfalls recur:

- **Lagging by construction.** Any average of past bars reacts after volatility has already changed. A sudden expansion (news, a gap, a volatility-of-volatility spike) will not show up in the ACR until several bars have passed, so an ACR-based filter can wave through a setup just as conditions break, or block one just as they normalise.
- **Outlier sensitivity on short lookbacks.** A single abnormally large bar (a flash spike, an earnings candle) can inflate a short-window ACR for the duration of the lookback, distorting thresholds and targets. Longer windows smooth this but lag more.
- **Gap blindness.** A naive `high - low` candle range ignores overnight gaps entirely. On gap-prone instruments this understates true volatility; see the [[average-true-range|ATR]] comparison above.
- **Regime mismatch.** A threshold calibrated in a quiet regime can be far too small once volatility expands (every bar clears the filter, including noise) and far too large once it contracts (no setup ever qualifies).

### Caution: Avoid Overfitting the Threshold

The "20% minimum move" and "50-100% target" figures are guidelines from a single creator's discretionary method, not independently validated parameters. A fixed percentage that works on one instrument or volatility regime may be too tight or too loose on another. Traders moving from discretion toward systematic implementation should treat the lookback and threshold as parameters to be calibrated and [[backtesting|backtested]], being mindful that tuning thresholds to specific past examples risks curve-fitting.

## Related Concepts

- [[arc-strategy]] — uses box range as both filter and target scale
- [[average-true-range]] — gap-aware sibling volatility measure
- [[box-and-swing-structure]] — where the box range is defined
- [[volatility]] — what ACR is ultimately measuring
- [[breakout]] — range expansion past the recent ACR is a common breakout trigger
- [[candlestick-patterns]]
- [[support-and-resistance]]
- [[backtesting]]

## Sources

- gap-finder Perplexity deep research (2026-06-19)
- Source video: https://www.youtube.com/watch?v=T7QN-yqryr4
- General market knowledge
