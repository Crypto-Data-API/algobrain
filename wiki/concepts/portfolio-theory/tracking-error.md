---
title: "Tracking Error"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [portfolio-theory, quantitative, education, stocks]
domain: [portfolio-theory, quantitative]
difficulty: intermediate
aliases: ["Tracking Error", "Active Risk", "Tracking Difference"]
prerequisites: ["[[index-investing]]", "[[volatility]]"]
related: ["[[etf]]", "[[index-funds]]", "[[etf-vs-mutual-fund-vs-index-fund]]", "[[expense-ratio]]", "[[information-ratio]]", "[[treynor-ratio]]", "[[sharpe-ratio]]", "[[alpha]]", "[[active-vs-passive-investing]]", "[[passive-investing]]", "[[nav]]", "[[etf-arbitrage]]", "[[s-and-p-500]]"]
---

**Tracking error** measures how closely a fund's returns follow those of its benchmark. Formally, it is the **standard deviation of the difference between the fund's return and the benchmark's return** over a series of periods. For an index fund or [[etf|ETF]], low tracking error is a sign of good replication; for an actively managed fund, tracking error (often called **active risk**) quantifies how far the manager strays from the index in pursuit of [[alpha]].

## Why it matters

The whole promise of a [[index-funds|passive index fund]] is to deliver the benchmark's return minus a small, known cost. Tracking error tells you whether that promise is being kept. Two funds tracking the same index — say the [[s-and-p-500|S&P 500]] — can charge similar fees yet deliver different real-world results because of how tightly each replicates the index day to day. For active funds, tracking error is the denominator of the **[[information-ratio]]** (active return ÷ tracking error), the standard measure of how efficiently a manager converts deviation from the benchmark into outperformance.

## Tracking error vs. tracking difference

These two terms are often confused but answer different questions:

- **Tracking difference** is the *cumulative return gap* between the fund and its benchmark over a period (e.g. the fund returned 9.7% vs. the index's 10.0%, a −0.3% difference). This is what most directly affects an investor's wealth.
- **Tracking error** is the *volatility* of the period-by-period return gaps — how consistent or erratic the tracking is, not its net size. A fund can have a small average tracking difference but a high tracking error if it sometimes leads and sometimes lags.

## How it is calculated

The common formula is the standard deviation of the return differences:

```
tracking error = StdDev( R_fund − R_benchmark )
```

measured over a window (e.g. monthly returns annualised). An alternative regression-based form computes the standard deviation of the residuals from regressing fund returns on benchmark returns. Index ETFs typically report annualised tracking error well below 0.10% for large, liquid benchmarks; emerging-market or thinly traded benchmarks run higher.

## What drives tracking error

- **Fees and costs.** The [[expense-ratio]] is deducted from fund returns but not from the index, creating a structural drag.
- **Sampling / optimisation.** Funds tracking huge or illiquid indices may hold a representative *sample* rather than every constituent, introducing deviation.
- **Cash drag.** Uninvested cash held for redemptions earns the cash rate, not the index return.
- **Rebalancing and trading costs.** [[rebalancing|Index reconstitution]] forces trades at costs the index ignores.
- **Securities lending, dividend timing, and currency hedging.** Each adds or removes small amounts relative to the index.
- **For active funds — deliberate active bets**, which are the *intended* source of tracking error.

## How it is used

- **Choosing index funds/ETFs.** All else equal, prefer the vehicle with the lowest tracking error *and* lowest [[expense-ratio]] (the two are linked but not identical — see [[etf-vs-mutual-fund-vs-index-fund]]).
- **Evaluating active managers.** A high [[information-ratio]] is more impressive than a high raw return if it is achieved with controlled tracking error. Many institutional mandates cap tracking error (e.g. "no more than 4% active risk").
- **Risk budgeting.** Tracking error is the natural unit for an "enhanced index" or "core-satellite" portfolio: a tight tracking-error budget around a passive [[index-investing|core]] with active satellites.

## Worked example (hypothetical)

Suppose an index ETF posts these monthly return gaps versus its benchmark: +0.02%, −0.05%, +0.01%, −0.03%, +0.04%, −0.06% (illustrative). The *average* gap (tracking difference) is roughly −0.01% per month — tiny. But the **standard deviation** of those gaps (the tracking error) is what tells you how predictable the replication is: a fund whose gaps cluster tightly around zero is doing its job, while one with the same average but wild swings between +0.5% and −0.5% would alarm a risk manager. The numbers here are made up to show the mechanic, not a real fund's results.

## Limitations

- **Low tracking error is not the same as good performance.** A fund can track a *bad* benchmark perfectly. Tracking error judges fidelity to the index, not whether the index is worth owning.
- **Sign-blind.** Because it is a standard deviation, tracking error treats outperformance and underperformance identically — it does not tell you *which way* the fund tends to miss. Pair it with tracking difference.
- **Window- and frequency-dependent.** Daily, monthly, and annual measurements give different numbers; comparisons are only fair on a like-for-like basis.
- **Backward-looking.** Historical tracking error may not persist if the fund changes its replication method, the index changes constituents, or liquidity conditions shift.

## Related

- [[etf]] · [[index-funds]] — vehicles for which tracking error is the key quality metric
- [[etf-vs-mutual-fund-vs-index-fund]] — comparison where tracking error is a deciding factor
- [[expense-ratio]] — a structural driver of tracking error
- [[information-ratio]] — active return per unit of tracking error
- [[alpha]] · [[active-vs-passive-investing]] — the active side of the trade-off
- [[etf-arbitrage]] — the mechanism that keeps ETF price near [[nav]]

## Sources

- Andrew Ang, *Asset Management: A Systematic Approach to Factor Investing*
- Richard Grinold & Ronald Kahn, *Active Portfolio Management*
- CFA Institute curriculum, *Portfolio Management* (active risk and the information ratio)
