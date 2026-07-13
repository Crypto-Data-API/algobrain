---
title: "Recency Bias"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [behavioral-finance, risk-management]
aliases: ["recency bias", "recency effect", "extrapolation bias", "trend extrapolation"]
domain: [behavioral-finance]
prerequisites: ["[[behavioral-finance]]"]
difficulty: beginner
related: ["[[availability-bias]]", "[[herding]]", "[[fomo]]", "[[overconfidence-bias]]", "[[market-bubbles]]", "[[mean-reversion]]", "[[trading-psychology]]", "[[cognitive-biases]]", "[[market-regime]]", "[[risk-management]]"]
---

Recency bias is the tendency to give disproportionate weight to recent events and to assume that the recent past will continue into the future. In markets it shows up as extrapolation — *"it has gone up for weeks, so it will keep going up"* — and it answers a very common ALFRED user question: *"why do I keep assuming the current trend will just continue?"* The recent stretch of price action feels far more representative of "how things are" than a longer, calmer history would justify.

## How It Shows Up in Trading

- **Trend extrapolation.** A few strong weeks get projected forward indefinitely, encouraging buying high into [[market-bubbles]] and selling low into capitulations.
- **Chasing recent winners.** Allocating to whatever has performed best lately — the fund, sector, or coin with the hottest trailing return — just as it is most extended. This overlaps heavily with [[fomo]] and performance chasing.
- **Recency-weighted risk perception.** After a long calm period, volatility and tail risk feel impossible, so position sizes creep up; right after a crash, even good setups feel too dangerous to touch.
- **Overweighting your own last few trades.** A short winning streak breeds [[overconfidence-bias]] and size creep; a short losing streak breeds timidity or abandoning a sound system mid-drawdown.
- **Forgetting the regime can change.** Recent conditions get mistaken for permanent ones, so traders are slow to recognise a shift in [[market-regime]].

## Why It Happens

Recent and vivid information is simply easier to recall and feels more relevant — a close cousin of [[availability-bias]]. The mind builds its forecast from the small, salient sample it can retrieve quickly rather than from the full historical base rate. Two reinforcing effects:

- **Small-sample over-inference** — we treat a handful of recent observations as if they reliably describe the underlying process, ignoring how noisy a short window is.
- **Pattern-seeking** — humans are wired to detect and extend trends, even in data that is partly or entirely random (see [[narrative-fallacy]]).

Because many financial series mean-revert over longer horizons, naive extrapolation of the recent move is frequently exactly the wrong call — see [[mean-reversion]].

## A Hypothetical Example

*This example is illustrative, not a real event.* A trader, "Riley," watches an asset rise smoothly for eight weeks with low volatility. The calm, rising recent history dominates Riley's sense of the asset, so they conclude it is "a steady uptrend" and increase position size well beyond their usual rules, reasoning that the recent low volatility means low risk. Volatility then normalises and the asset gives back two months of gains in a week. The error was treating a short, calm recent window as representative of the asset's true risk and forward path — the long-run distribution always included sharper moves; they just had not happened *recently*.

## How to Counter It

- **Anchor decisions to a long lookback, not the last few weeks.** Look at multi-year ranges, drawdowns, and volatility, not just the recent stretch.
- **Use base rates and full-sample statistics.** Ask how this setup has resolved across a long history, not how the last three trades felt.
- **Fix position sizing by rule, not by mood.** Pre-set [[position-sizing]] and [[risk-management]] rules stop recent calm from inflating size and recent pain from shrinking it.
- **Assume mean reversion is possible.** Before extrapolating a trend, explicitly consider the scenario where it reverts (see [[mean-reversion]]).
- **Keep a long [[trading-journal]].** Reviewing older periods counteracts the pull of the most recent results and reminds you that regimes change.
- **Separate "recent" from "likely."** Recency makes something feel probable; probability comes from the data, not the timestamp.

## Recency Bias vs Related Biases

- **vs [[availability-bias]]** — availability is about *ease of recall* in general; recency is the specific case where the most *recent* events are the easiest to recall and therefore overweighted.
- **vs [[gamblers-fallacy]]** — the gambler's fallacy expects a *reversal* ("it's due to bounce"), while recency bias expects *continuation* ("it'll keep going"). They are opposite extrapolations of a short streak, and which one fires often depends on framing.
- **vs [[fomo]]** — recency bias supplies the belief ("the trend will continue"); FOMO supplies the emotional urgency to act on it before missing out.

## Related

- [[availability-bias]] — the broader ease-of-recall effect recency sits within
- [[herding]] and [[fomo]] — recency-driven extrapolation fuels chasing
- [[overconfidence-bias]] — short winning streaks breed overconfidence
- [[market-bubbles]] — extrapolation of recent gains inflates manias
- [[mean-reversion]] — the dynamic that punishes naive extrapolation
- [[market-regime]] — what recency bias makes traders slow to recognise changing
- [[trading-psychology]] and [[cognitive-biases]] — the broader context

## Sources

- Tversky, A. & Kahneman, D. (1973). "Availability: A Heuristic for Judging Frequency and Probability." *Cognitive Psychology* 5(2), 207-232 — the availability heuristic underlying recency effects.
- Kahneman, D. & Tversky, A. (1972). "Subjective Probability: A Judgment of Representativeness." *Cognitive Psychology* — small-sample over-inference ("law of small numbers").
- Greenwood, R. & Shleifer, A. (2014). "Expectations of Returns and Expected Returns." *Review of Financial Studies* — evidence that investor return expectations extrapolate recent performance.
