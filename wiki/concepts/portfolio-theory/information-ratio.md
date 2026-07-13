---
title: "Information Ratio"
type: concept
created: 2026-06-30
updated: 2026-07-01
status: review
tags: [portfolio-theory, risk-management, quantitative, backtesting]
aliases: ["Information Ratio", "IR", "Appraisal Ratio"]
domain: [portfolio-theory, risk-management]
prerequisites: ["[[sharpe-ratio]]", "[[alpha]]", "[[expected-return]]"]
difficulty: intermediate
related: ["[[sharpe-ratio]]", "[[treynor-ratio]]", "[[sortino-ratio]]", "[[alpha]]", "[[beta]]", "[[fundamental-law-of-active-management]]", "[[active-management]]", "[[modern-portfolio-theory]]"]
---

The **information ratio (IR)** measures a portfolio's return *relative to a benchmark* per unit of the risk taken to deviate from that benchmark. It is the standard yardstick for [[active-management|active managers]]: it answers "how much excess return did this manager add for each unit of active risk, and how consistently?" Where the [[sharpe-ratio|Sharpe ratio]] compares a portfolio to the risk-free asset, the information ratio compares it to a chosen benchmark (such as the S&P 500) — making it the natural measure of skill at beating an index rather than at delivering absolute return.

## Formula

```
Information Ratio = (R_p − R_b) / Tracking Error

  where  Tracking Error = std( R_p − R_b )
```

Where:
- **R_p** = portfolio return
- **R_b** = benchmark return
- **R_p − R_b** = **active return** (also called excess return over the benchmark, or [[alpha]] when the benchmark is the appropriate factor model)
- **Tracking error** = the standard deviation of the active return series — the "active risk" the manager takes by deviating from the benchmark

The numerator rewards beating the benchmark; the denominator penalizes *erratic* deviations from it. A manager who beats the index by a steady 2% per year has a higher IR than one who beats it by a lumpy 2% with wild swings around the benchmark.

## Interpretation

| Information Ratio | Interpretation |
|---|---|
| < 0 | Underperformed the benchmark — negative skill (or fees) |
| 0 – 0.4 | Below average for an active manager |
| 0.4 – 0.6 | Good |
| 0.6 – 1.0 | Very good |
| > 1.0 | Exceptional — rare and hard to sustain |

These bands are widely cited industry rules of thumb (associated with Grinold & Kahn's *Active Portfolio Management*), not laws. A consistently positive IR is the quantitative signature of genuine skill; a high IR sustained over many years is very difficult to achieve because active return is hard to generate and tracking error compounds.

Like the Sharpe ratio, the IR is usually **annualized** by multiplying a per-period figure by √(periods per year), and it is most informative over long samples — a high IR from one or two years carries wide confidence intervals.

## The Fundamental Law of Active Management

Grinold's **Fundamental Law of Active Management** decomposes the achievable information ratio into skill and breadth:

```
IR ≈ IC × √Breadth
```

Where **IC** (information coefficient) is the correlation between the manager's forecasts and realized outcomes — a measure of skill per bet — and **Breadth** is the number of *independent* bets made per year. The insight: a modestly skilled manager who makes many independent bets can have a higher IR than a brilliant manager who makes only a few. This is the formal argument for [[diversification|diversifying]] across many uncorrelated positions rather than concentrating in a handful of high-conviction ideas, and it underpins how quant funds think about [[portfolio-construction]].

## Worked example (hypothetical)

*Illustrative arithmetic, not a backtest.* An active equity fund is measured against its benchmark over five years. Its annual active returns (fund minus benchmark) are:

```
+3%, +1%, +4%, −1%, +3%
```

```
Mean active return      = (3 + 1 + 4 − 1 + 3) / 5 = +2.0% per year
Tracking error (std dev of those five numbers) ≈ 2.0%
Information Ratio        = 2.0% / 2.0% = 1.0
```

An IR of **1.0** is exceptional: the fund added 2% of active return per year for every 2% of active risk, and did so fairly consistently (no year deviated wildly). Now suppose a second fund posted the *same* +2% average active return but with active returns of `+12%, −8%, +9%, −7%, +4%` — its tracking error is far larger (~9%), so its IR is only about `2% / 9% ≈ 0.22`. Same average outperformance, far less consistency, much weaker measured skill.

## Information ratio vs related metrics

| Metric | Compares portfolio to | Risk denominator | Best for |
|---|---|---|---|
| **Information Ratio** | a **benchmark** index | tracking error (active risk) | active managers vs an index |
| [[sharpe-ratio\|Sharpe]] | the **risk-free** rate | total [[standard-deviation\|std dev]] | absolute risk-adjusted return |
| [[treynor-ratio\|Treynor]] | the **risk-free** rate | [[beta]] (systematic risk) | well-diversified portfolios |
| [[sortino-ratio\|Sortino]] | a target return | downside deviation only | asymmetric / skewed returns |

The **appraisal ratio** is a closely related variant: [[alpha]] divided by the standard deviation of residual (idiosyncratic) risk from a factor regression, isolating skill that is orthogonal to systematic factor exposures.

## Limitations

1. **Benchmark-sensitive.** The IR is only as meaningful as the benchmark is appropriate. An ill-fitting benchmark can make a closet-indexer look skilled or a genuine stock-picker look poor.
2. **Tracking error assumes normality.** Active returns are often skewed and fat-tailed; tracking error (a standard deviation) understates the risk of strategies with hidden [[tail-risk]].
3. **Gameable and unstable.** Like the Sharpe ratio it can be inflated by selection bias, short samples, or illiquid, smoothly-marked holdings; the point estimate has wide confidence intervals over short periods.
4. **Says nothing about absolute return.** A high IR against a falling benchmark can still mean losing money — IR measures *relative*, not absolute, performance.
5. **Breadth must be of *independent* bets.** In the Fundamental Law, correlated positions count for far less than their raw number; over-counting breadth overstates the achievable IR.

## Related

- [[sharpe-ratio]] — the absolute-return analogue (benchmark = risk-free rate)
- [[treynor-ratio]] — risk-adjusted return per unit of beta
- [[alpha]] — the active return the IR's numerator captures
- [[fundamental-law-of-active-management]] — IR ≈ IC × √Breadth
- [[active-management]] — where the IR is the headline skill metric
- [[modern-portfolio-theory]] — the framework these ratios sit within
