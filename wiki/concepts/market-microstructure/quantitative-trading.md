---
title: Quantitative Trading
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - quantitative
  - algorithmic
  - systematic
aliases:
  - quant-trading
  - quant
  - quantitative
  - quantitative finance
  - quantitative analysis
  - quantitative trading overview
  - quant trading
related:
  - "[[algorithmic-trading]]"
  - "[[backtesting]]"
  - "[[statistical-arbitrage]]"
  - "[[mean-reversion]]"
  - "[[factor-investing]]"
  - "[[renaissance-technologies]]"
domain: [market-microstructure, quantitative]
prerequisites: ["[[backtesting]]", "[[statistics-for-trading]]"]
difficulty: advanced
---

# Quantitative Trading

**Quantitative trading** is a systematic, data-driven approach to markets that uses mathematical models, statistical analysis, and computational algorithms to identify and execute trading opportunities. Rather than relying on discretionary judgment, quants encode hypotheses as explicit rules and let data determine entries, exits, and position sizes. The discipline sits at the intersection of mathematics, computer science, and finance, and now dominates institutional volume.

## Overview

Quantitative trading replaces intuition with measurable, repeatable processes. A quant defines a hypothesis about market behaviour (e.g. "stocks that have outperformed over 12 months tend to keep outperforming over the next month"), tests it on historical data, controls for transaction costs and overfitting, and — if it survives — deploys it as code. The defining advantage over discretionary trading is **testability**: a rule-based strategy can be [[backtesting|backtested]] across decades of history, removing hindsight bias and emotional interference. The defining risk is **overfitting** — a model that captures noise rather than genuine structure will look excellent in-sample and fail in live markets.

## How It Works — The Research Pipeline

A typical quant workflow is a research pipeline:

1. **Hypothesis** — articulate an economic or behavioural rationale for an edge (see [[edge-taxonomy]]).
2. **Data collection** — assemble clean, point-in-time price, fundamental, or alternative data; survivorship and look-ahead bias are the most common data sins.
3. **Feature engineering** — transform raw data into predictive signals (returns, ratios, momentum, volatility estimates).
4. **Model building** — fit a model: a simple ranking rule, a [[factor-investing|factor model]], or a machine-learning estimator.
5. **Backtesting** — simulate the strategy over history with realistic costs and slippage.
6. **Out-of-sample / walk-forward validation** — confirm the edge holds on data the model never saw; apply the [[deflated-sharpe-ratio|deflated Sharpe ratio]] to penalise multiple-testing.
7. **Live deployment** — route orders via [[algorithmic-trading|execution algorithms]] that minimise market impact.

## Major Approaches

- **Factor models** exploit persistent return drivers — value, [[momentum]], quality, size, low-volatility (see [[factor-investing]]).
- **[[statistical-arbitrage]]** trades mean-reverting spreads between related instruments (pairs, baskets, ETFs vs constituents).
- **High-frequency market making** captures the [[bid-ask-spread]] across millions of small trades.
- **Machine learning** models (gradient boosting, neural networks) discover nonlinear patterns; see [[xgboost-trading]].

## Trading Relevance

For an individual trader, the quant mindset is valuable even without a PhD: it forces explicit rules, honest backtesting, and cost-aware position sizing, all of which curb the behavioural errors that destroy discretionary accounts. The tooling is now accessible — [[python]] with pandas, NumPy, and scikit-learn, plus backtesting frameworks such as Backtrader, Zipline, and QuantConnect. The cautionary tale is equally important: most "edges" that survive a naive backtest are artifacts of overfitting, and the single most useful skill in quant trading is the discipline to reject strategies that cannot pass rigorous out-of-sample validation.

## Major Quant Firms

Pioneered by [[jim-simons]] at [[renaissance-technologies]] (Medallion Fund averaged ~66% gross annual returns 1988–2018), the field now includes Two Sigma, D.E. Shaw, Citadel Securities, and Jane Street, which employ mathematicians, physicists, and computer scientists to deploy billions systematically.

## Related

- [[algorithmic-trading]] — the execution layer of quant strategies
- [[backtesting]] — how quant strategies are validated
- [[statistical-arbitrage]] — a canonical quant approach
- [[factor-investing]] — systematic factor exposures
- [[mean-reversion]] — a common quant signal class
- [[overfitting-detection]] — the central failure mode
- [[renaissance-technologies]] — the archetypal quant fund

## Sources

- Ernest Chan, *Quantitative Trading: How to Build Your Own Algorithmic Trading Business* (Wiley, 2009) — see [[book-quantitative-trading-ernest-chan]]
- Gregory Zuckerman, *The Man Who Solved the Market* (2019) — see [[book-the-man-who-solved-the-market]]
- Marcos López de Prado, *Advances in Financial Machine Learning* (Wiley, 2018)
