---
title: "Backtesting & Strategy Optimization Wiki"
type: source
created: 2026-04-14
updated: 2026-04-14
status: good
tags: [backtesting, python, algorithmic, quantitative, meta]
source_type: article
source_url: ""
source_author: "Research compilation"
source_date: 2026-04-14
source_file: "r2://trader-wiki/misc/2026-04-14-backtesting-strategy-optimization-wiki.md"
confidence: medium
claims_count: 20
aliases: ["Backtesting & Strategy Optimization Wiki"]
related:
  - "[[optuna]]"
  - "[[pybroker]]"
  - "[[backtesting-py]]"
  - "[[pyfolio]]"
  - "[[quantstats]]"
  - "[[optimization-objectives]]"
  - "[[execution-model-differences]]"
  - "[[hummingbot]]"
  - "[[vectorbt]]"
  - "[[backtrader-framework]]"
  - "[[walk-forward-analysis]]"
  - "[[deflated-sharpe-ratio]]"
  - "[[backtesting-overview]]"
---

A comprehensive research compilation covering the backtesting and strategy optimization ecosystem: framework comparisons, hyperparameter optimization with Optuna, portfolio analytics tools, optimization objective selection, execution model differences across frameworks, and market-making infrastructure. Compiled from framework documentation, academic papers, and practitioner experience.

## Key Claims

### Hyperparameter Optimization [HIGH]
1. [HIGH] Optuna's TPE (Tree-structured Parzen Estimator) is significantly more sample-efficient than grid search for strategy parameter optimization — achieving comparable results in 5-20x fewer trials
2. [HIGH] Running 100+ Optuna trials on in-sample data without walk-forward validation is a recipe for guaranteed overfitting
3. [HIGH] A backtest Sharpe above 2.0 more likely signals overfitting than genuine alpha
4. [HIGH] Live Sharpe is approximately 50% of backtest Sharpe — target 1.0-1.5 in-sample to expect 0.5-0.75 live

### Framework Performance [HIGH]
5. [HIGH] VectorBT processes 1000 strategy variations in the time Backtrader completes one, due to vectorized NumPy operations vs event-driven Python loops
6. [HIGH] Different frameworks produce different results on identical strategies due to execution model differences (fill-at-close vs fill-at-next-open)
7. [HIGH] Fill-at-close vs fill-at-next-open differences can change annualized returns by 2-5%

### ML-Driven Backtesting [HIGH]
8. [HIGH] PyBroker provides native Optuna + scikit-learn integration for ML-driven backtesting with automatic temporal windowing
9. [HIGH] Purged k-fold cross-validation with embargo periods prevents data leakage in time-series model evaluation

### Validation [HIGH]
10. [HIGH] Walk-forward optimization is the gold standard for validating trading strategies — it simulates how a strategy would have been deployed in real time
11. [HIGH] The deflated Sharpe ratio corrects for the number of trials tested, accounting for selection bias
12. [HIGH] Point-in-time index data is essential — survivorship bias inflates returns 1-4% annually
13. [HIGH] Minimum 1000 Monte Carlo simulation runs recommended for statistical stability

### Execution Models [HIGH]
14. [HIGH] Backtesting.py fills at the same bar's close by default (optimistic), while Backtrader fills at the next bar's open (more realistic)
15. [HIGH] Forgetting .shift(1) in vectorized backtests creates invisible look-ahead bias
16. [HIGH] Bar magnification (unknown intrabar sequencing of high/low) creates ambiguity when stop-loss and take-profit are both hit on the same bar

### Analytics Tools [MEDIUM]
17. [MEDIUM] QuantStats is the more actively maintained alternative to pyfolio and better suited for crypto/futures strategies
18. [MEDIUM] pyfolio's Fama-French factor decomposition remains unique — no direct replacement in QuantStats

### Market Making [MEDIUM]
19. [MEDIUM] Hummingbot's order book replay backtesting is more realistic for market-making strategies than price-bar-based backtesting
20. [MEDIUM] TrendSpider's walk-forward optimization reduces overfitting by ~20% compared to in-sample-only optimization

### Optimization Objectives [MEDIUM]
21. [MEDIUM] Strategies that pass Monte Carlo testing show 30-50% lower live failure rates
22. [MEDIUM] Sortino ratio is preferred over Sharpe for asymmetric strategies (trend-following, long options)
23. [MEDIUM] Multi-objective Pareto optimization produces more robust strategy selections than single-objective optimization

## Pages Created from This Source

- [[optuna]] — Optuna hyperparameter optimization framework
- [[pybroker]] — ML-first backtesting framework with native Optuna integration
- [[backtesting-py]] — Lightweight event-driven backtesting library
- [[pyfolio]] — Portfolio analytics and tear sheet library
- [[quantstats]] — Modern portfolio analytics library
- [[optimization-objectives]] — Optimization objective selection for strategy tuning
- [[execution-model-differences]] — Why identical strategies produce different results across frameworks
- [[hummingbot]] — Open-source market-making and arbitrage bot framework
