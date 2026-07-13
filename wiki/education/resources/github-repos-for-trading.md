---
title: Best GitHub Repositories for AI Trading
type: concept
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [education, open-source, github, tools]
related:
  - "[[python-quant-stack]]"
  - "[[quantconnect-bootcamp]]"
  - "[[kaggle-finance]]"
---

# Best Open-Source Repositories for AI Trading

These GitHub repositories are the building blocks of the AI trading ecosystem. Each one solves a specific problem — from backtesting to deep reinforcement learning to exchange connectivity. Study the code, fork what you need, and contribute back.

## Deep Learning and RL for Trading

**FinRL** (30K+ stars) — The most comprehensive deep reinforcement learning framework for trading. Supports stocks, crypto, futures. Integrates with Stable-Baselines3, provides pre-built environments, handles data downloading and preprocessing. The go-to starting point for [[deep-reinforcement-learning]] in finance.

**qlib** (15K+ stars) — Microsoft's AI-oriented quantitative investment platform. Research framework for ML-based alpha generation, model training, backtesting, and portfolio management. Includes pre-built datasets and benchmark models. Production-quality code.

## Quantitative Finance Libraries

**mlfinlab** (4K+ stars) — Python implementation of methods from Marcos Lopez de Prado's "Advances in Financial Machine Learning." Triple barrier labeling, fractional differentiation, structural breaks, sample weighting. Essential reading paired with [[academic-papers-quant-finance]].

**pandas-ta** (5K+ stars) — Technical analysis library built on pandas. 130+ indicators with a clean API. An alternative to TA-Lib that is pure Python and easier to install.

## Backtesting Frameworks

**Lean** (9K+ stars) — QuantConnect's open-source algorithmic trading engine. C# and Python support. Institutional-quality event-driven backtesting. Powers [[quantconnect-bootcamp]].

**vectorbt** (4K+ stars) — Blazing-fast vectorized backtesting. Uses NumPy under the hood for portfolio simulation. Ideal for parameter sweeps and rapid prototyping.

**Backtrader** (13K+ stars) — Mature event-driven backtesting framework. Large community, extensive documentation, broker integration. The standard for Python algo trading.

**zipline-reloaded** (3K+ stars) — Continuation of Quantopian's zipline. Pipeline API for factor research, calendar-aware backtesting. Good for equity factor strategies.

## Crypto-Specific

**Freqtrade** (28K+ stars) — Complete crypto trading bot framework. Strategy development, backtesting, hyperparameter optimization, live trading. Supports many exchanges via CCXT. Active community and documentation.

**CCXT** (33K+ stars) — Unified JavaScript/Python/PHP library for cryptocurrency exchange APIs. Supports 100+ exchanges. The standard for crypto data fetching and order execution.

## How to Use These Repos

1. Star repos that interest you — they update frequently
2. Read the documentation before diving into source code
3. Run the example notebooks to understand capabilities
4. Fork and modify rather than building from scratch
5. Check issue trackers and commit history to gauge active maintenance
6. Combine repos: use CCXT for data, vectorbt for backtesting, FinRL for ML models
