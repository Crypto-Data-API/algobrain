---
title: "R-Core"
type: concept
created: 2026-04-13
updated: 2026-06-11
status: good
tags: [risk-management, portfolio-theory, methodology]
aliases: ["R-Core", "R Core", "Rcore", "dollar winners over dollar losers"]
related: ["[[sharpe-ratio]]", "[[risk-management-overview]]", "[[equity-curve]]", "[[itpm-god-like-trader-status]]", "[[expectancy]]", "[[win-loss-ratio]]", "[[anton-kreil]]"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[win-loss-ratio]]", "[[expectancy]]"]
difficulty: intermediate
---

**R-Core** is a performance statistic used in [[anton-kreil|ITPM]]'s trader-evaluation framework, defined as the ratio of total dollars made on winning trades to total dollars lost on losing trades over a measurement period. It is a variant of the classic **profit factor** and is used alongside the [[win-loss-ratio|win/loss rate]], average days in trade, and [[equity-curve]] shape to judge whether a discretionary trader has a durable edge (Source: [[itpm-god-like-trader-status]], [[itpm-master-compounding]]).

## Definition

```
R-Core = (sum of dollar winners) / (sum of dollar losers)
```

An R-Core of 2.0 means the trader booked twice as many dollars in profit from winners as they gave back to losers over the period. Because it is denominated in dollars rather than per-trade R-multiples, R-Core captures both the hit rate and the relative size of wins versus losses in a single number — a trader can run a sub-50% [[win-loss-ratio|win rate]] and still post a strong R-Core if winners are large relative to losers.

## Target Levels (ITPM Benchmarks)

ITPM publishes explicit thresholds for what it calls "god-like trader status":

- **Minimum acceptable**: R-Core of **1.5** (Source: [[itpm-master-compounding]])
- **Top traders**: R-Core "with a 2 in front of it" — i.e., 2.0 or higher (Source: [[itpm-master-compounding]])
- **Statistical validity**: claims require a minimum of ~150 trades over at least one year before the R-Core figure is meaningful (Source: [[itpm-god-like-trader-status]])

Worked example from the ITPM material: in a single month, exiting $7,500 of winners against $3,500 of losers yields $4,000 net profit and an R-Core of 2.14 (Source: [[itpm-master-compounding]]).

A real-trader example (Philip Klein, 32 months / ~400 trades): won $1.97M, lost $1.5M for an R-Core of **1.28** (improving to 1.31 in 2024), with a 52.5% win rate — below the 1.5 target, yet still producing roughly 100% annual returns through credit collection and compounding (Source: [[itpm-master-compounding]]). This illustrates that R-Core is one input, not the whole picture: position sizing, compounding, and win rate interact.

## Relationship to Other Metrics

- **Profit factor**: R-Core is effectively the profit factor (gross profit / gross loss) under a different name. A profit factor / R-Core below 1.0 means the trader is net-losing.
- **[[expectancy]]**: expectancy folds in win rate and average win/loss per trade; R-Core aggregates the same information at the dollar-flow level across the whole sample.
- **[[win-loss-ratio]]**: a high win rate with a low R-Core indicates many small wins and a few large losses (negative skew / blow-up risk); a low win rate with a high R-Core indicates trend-following-style payoffs.
- **[[sharpe-ratio]]** and **[[equity-curve]]**: R-Core says nothing about path or volatility, so it is read together with the Sharpe ratio and the smoothness of the equity curve (ITPM's ideal is a 45-degree line).

## Trading Relevance

R-Core is a fast diagnostic for whether a discretionary book has genuine edge:

- It exposes the common failure mode of "cutting winners and letting losers run" — that pattern crushes the numerator and inflates the denominator, dragging R-Core below 1.5 even with a high win rate.
- Tracking R-Core trend over time (e.g., rising from 1.28 to 1.31) signals improving trade management.
- Combined with the 150-trade minimum, it imposes a sample-size discipline that guards against declaring an edge from a small lucky streak.

## Related

- [[expectancy]] — per-trade edge incorporating win rate and average win/loss
- [[win-loss-ratio]] — the hit-rate component R-Core complements
- [[sharpe-ratio]] — risk-adjusted return; pairs with R-Core for the volatility view
- [[equity-curve]] — the path R-Core ignores
- [[itpm-god-like-trader-status]] / [[itpm-master-compounding]] — source frameworks defining R-Core targets
- [[anton-kreil]] — originator of the ITPM statistics

## Sources

- (Source: [[itpm-god-like-trader-status]])
- (Source: [[itpm-master-compounding]])
