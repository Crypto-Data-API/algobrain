---
title: "Backtesting"
type: overview
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [backtesting, methodology, validation, statistics]
aliases: ["Backtest", "Strategy Validation", "backtesting"]
related: ["[[walk-forward-analysis]]", "[[purged-kfold-cv]]", "[[transaction-cost-modeling]]", "[[survivorship-bias]]", "[[lookahead-bias]]", "[[deflated-sharpe-ratio]]", "[[strategy-development-overview]]"]
---

# Backtesting

Backtesting is the practice of simulating a trading strategy over historical data to estimate how it would have performed. It is the central tool of quantitative research and the central source of false confidence. A backtest is a *biased estimator* of live performance — almost always biased upward — and the discipline of backtesting is mostly the discipline of removing those biases.

This page is the index for the backtesting techniques and pitfalls covered in this wiki. The deeper conceptual content lives in the [[strategy-development-overview]] section.

## What a Backtest Can and Cannot Tell You

A backtest **can** tell you:
- Whether a strategy *would have* worked in conditions similar to those in the historical sample
- The general shape of the return distribution (skew, kurtosis, drawdown profile)
- Whether the strategy is broken (negative returns suggest something is wrong)
- The order of magnitude of capacity, turnover, and cost sensitivity

A backtest **cannot** tell you:
- Whether the strategy will work in the future (regime, structure, and crowding all change)
- The true Sharpe ratio (it gives a *biased estimate*)
- How the strategy will behave in conditions absent from the sample (e.g., a 2008-style crash if your sample is 2010-2020)
- Anything reliable if the data has lookahead, survivorship, or selection bias

## The Five Sources of Backtest Bias

Every honest backtester is fighting these five things:

1. **[[lookahead-bias]]** — using information in the test that wasn't available at decision time
2. **[[survivorship-bias]]** — testing only on instruments that survived to the present
3. **Selection bias** — testing only on a non-representative subset (e.g., cherry-picked dates)
4. **[[data-snooping-and-p-hacking]]** — running many tests and reporting the best
5. **Optimistic execution assumptions** — fee-free fills, midpoint trades, no slippage

Each of these biases the result toward *higher than reality*. None of them bias toward lower. This asymmetry is why honest backtests almost always look worse than the first naive run.

## Validation Techniques

Once you have a backtest result, validation tools determine whether it's real:

- [[walk-forward-analysis]] — slide a train/test window through the data
- [[purged-kfold-cv]] — combinatorial purged k-fold cross-validation, the López de Prado method
- [[monte-carlo-permutation-test]] — break time-series structure to test the null
- [[deflated-sharpe-ratio]] — correct for trial count and higher moments
- [[probabilistic-sharpe-ratio]] — confidence interval on the observed Sharpe
- Out-of-sample hold-out — the simplest and still one of the most powerful

## Cost Modeling

A backtest without realistic costs is fiction. See [[transaction-cost-modeling]] for the full treatment. Required components:

- Commissions
- Bid-ask spread (full or half, per side)
- Market impact (square-root law for institutional sizes)
- Borrow costs (for shorts)
- Funding rates (for perpetual futures)
- Financing costs (for leveraged longs)
- Taxes (if applicable)

A strategy that's profitable gross but unprofitable net is not a strategy. It's a capacity discovery.

## Performance Metrics

How to measure what came out of the backtest:

- [[sharpe-sortino-calmar]] — the three classic risk-adjusted return ratios
- [[deflated-sharpe-ratio]] — multiple-testing-corrected Sharpe
- [[probabilistic-sharpe-ratio]] — confidence-aware Sharpe
- Maximum drawdown, drawdown duration, recovery time
- Win rate, profit factor, average win/loss ratio
- Turnover, capacity, breakeven cost

The Sharpe ratio is the most common single number but is famously misleading on its own. Always pair it with drawdown metrics and a return distribution plot.

## Pages in This Section

### Validation methods
- [[walk-forward-analysis]]
- [[purged-kfold-cv]]
- [[monte-carlo-permutation-test]]

### Bias detection
- [[survivorship-bias]] *(also under behavioral-finance)*
- [[lookahead-bias]]
- [[selection-bias-research]]

### Cost modeling
- [[transaction-cost-modeling]]
- [[market-impact-models]]
- [[slippage-modeling]]

### Performance metrics
- [[sharpe-sortino-calmar]]
- [[deflated-sharpe-ratio]]
- [[probabilistic-sharpe-ratio]]
- [[minimum-track-record-length]]

## Sources

- [[book-advances-in-financial-machine-learning]] — López de Prado, comprehensive coverage
- [[book-quantitative-trading-ernest-chan]] — Chan on practical backtesting workflows
- [[book-evidence-based-technical-analysis]] — Aronson on statistical validation

## Related

- [[strategy-development-overview]]
- [[hypothesis-to-backtest-workflow]]
- [[overfitting-detection]]
- [[data-snooping-and-p-hacking]]
- [[backtesting]] — the older single-page version (now superseded)
