---
title: "Strategy Development"
type: overview
created: 2026-04-10
updated: 2026-04-10
status: good
tags: [strategy-development, research, backtesting, methodology]
aliases: ["Strategy R&D", "Strategy Research"]
related: ["[[edge-taxonomy]]", "[[hypothesis-to-backtest-workflow]]", "[[research-checklist]]", "[[data-snooping-and-p-hacking]]", "[[overfitting-detection]]", "[[failure-modes]]", "[[backtesting-overview]]"]
---

# Strategy Development

The discipline of producing new trading strategies — from observation, to hypothesis, to validated edge, to live capital. Most of this wiki catalogs *what strategies exist*. This section is about *how to make new ones that actually work*.

## The Core Loop

Strategy development is a loop, not a line:

1. **Observation** — notice an anomaly, dislocation, or repeatable pattern
2. **Hypothesis** — articulate *why* the edge exists (see [[edge-taxonomy]])
3. **Pre-mortem** — list everything that could kill it before writing code (see [[research-checklist]], [[failure-modes]])
4. **Data** — assemble a clean, point-in-time, survivorship-bias-free dataset
5. **Backtest** — implement, run in-sample, look for catastrophic bugs first
6. **Validate** — out-of-sample, walk-forward, sensitivity analysis (see [[overfitting-detection]])
7. **Cost overlay** — add realistic transaction costs, slippage, borrow, financing
8. **Statistical sanity** — multiple testing correction, deflated Sharpe (see [[data-snooping-and-p-hacking]])
9. **Paper trade** — run live but with no capital for 1-3 months
10. **Size up** — start at a fraction of intended size, scale only after validation

The vast majority of "promising" strategies die between steps 6 and 9. Building skill at killing your own ideas quickly is the single highest-leverage habit in this work.

## Why Most Strategies Fail

Three failure modes account for the overwhelming majority of dead strategies:

1. **The edge was never real** — it was a statistical artifact of multiple testing, lookahead bias, or fitting noise. See [[data-snooping-and-p-hacking]] and [[overfitting-detection]].
2. **The edge was real but uneconomic** — the gross returns existed, but transaction costs, slippage, borrow costs, or financing destroyed the net P&L. See [[transaction-cost-modeling]].
3. **The edge was real but decayed** — crowding, regime change, regulatory shift, or venue change killed the inefficiency. See [[failure-modes]].

A useful mental model: a backtest is a *biased estimator* of live performance. The bias is almost always toward optimism. Your job as a researcher is to systematically remove sources of bias until what remains is honest.

## Pages in This Section

- [[edge-taxonomy]] — Where do returns actually come from? Six categories of edge (five alpha sources + risk premia).
- [[hypothesis-to-backtest-workflow]] — The full pipeline from idea to live capital.
- [[research-checklist]] — Questions to answer *before* writing any code.
- [[data-snooping-and-p-hacking]] — Multiple testing, deflated Sharpe, the file-drawer problem.
- [[overfitting-detection]] — Walk-forward, purged k-fold, parameter sensitivity, Bailey-Borwein-Lopez de Prado.
- [[failure-modes]] — How strategies die in the wild. A catalog.
- [[strategy-monitoring]] — Dashboard design, alert thresholds, operationalizing kill criteria from failure-modes.

## Related Sections

- [[backtesting-overview]] — Mechanics of running honest backtests
- [[anomalies-overview]] — The raw material: documented market inefficiencies
- [[data-sources-overview]] — Where to get the data you need
- [[regime-matrix]] — Which strategies work in which conditions
- [[live-journal]] — What's currently in production and how it's performing

## Required Reading From Outside the Wiki

The single most important external resource is Marcos López de Prado's *Advances in Financial Machine Learning* — particularly the chapters on backtest overfitting, combinatorial purged cross-validation, and the deflated Sharpe ratio. The wiki summarizes these techniques but the book is the source. See [[book-advances-in-financial-machine-learning]] if it's been ingested; otherwise it should be the next research priority.

## Sources

- [[book-advances-in-financial-machine-learning]] — López de Prado on backtest overfitting and purged CV
- [[book-quantitative-trading-ernest-chan]] — Chan on the practical end-to-end research workflow
- [[book-evidence-based-technical-analysis]] — Aronson on statistical validation and data-snooping bias
