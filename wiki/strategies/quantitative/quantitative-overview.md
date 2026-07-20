---
title: "Quantitative Strategies"
type: overview
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [quantitative, algorithmic, mean-reversion, momentum]
aliases: ["Quant Strategies", "Quantitative Strategies"]
related: ["[[strategies-overview]]", "[[algorithmic-overview]]", "[[arbitrage-overview]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[backtesting-overview]]"]
---

# Quantitative Strategies

Quantitative strategies use mathematics and statistics to identify patterns, test hypotheses, and generate trading signals. Unlike discretionary trading, every decision is formalized in code and validated against historical data, enabling systematic execution, objective performance measurement, and continuous improvement.

## What Distinguishes This Family

- **Edge sources** — primarily *analytical* (better models of the same public data) and *behavioral* (systematically harvesting other participants' biases, e.g. overreaction fueling mean reversion, underreaction fueling momentum). Some entries shade into *structural* edges (calendar effects, tax-loss harvesting). See [[edge-taxonomy]].
- **Typical timeframes** — anywhere from intraday (session-overlap momentum, liquidation fades) to monthly rebalances (commodity carry/value, momentum rotation). Most pages here operate on daily bars.
- **Capital and data requirements** — the defining cost is data and research time, not capital: clean historical OHLCV at minimum, plus specialty datasets (funding rates, VIX term structure, sentiment feeds, on-chain data) for specific strategies. Rigorous [[backtesting-overview|backtesting]] with realistic costs is non-negotiable — naive backtests are the family's main trap (see [[overfitting-detection]]).
- **Who it suits** — traders comfortable with statistics and programming who prefer rule-based execution over discretion, and who can keep trading a validated system through drawdowns instead of second-guessing it.
- **Regime sensitivity** — most quant edges are regime-conditional: mean reversion works in ranges, momentum in trends, carry in calm markets. [[regime-detection]] and the [[regime-matrix]] are the glue that decides which models get capital.

## Strategies in This Category

### Mean Reversion & Statistical Arbitrage

- [[mean-reversion]] — The core concept: prices that stretch from fair value tend to snap back.
- [[bollinger-band-reversion]] — Fading moves beyond volatility bands back toward the mean.
- [[stretch-revert]] — A 14-member family fading price's deviation from an adaptive baseline; the members share one entry thesis and differ only in which estimator ([[frama|FRAMA]], [[kama|KAMA]], [[theil-sen-regression|Theil-Sen]], [[least-squares-moving-average|LSMA]] …) defines "the mean". See [[adaptive-moving-averages]].
- [[rsi-mean-reversion]] — Buying oversold / selling overbought readings on the RSI oscillator.
- [[ornstein-uhlenbeck]] — Modeling spreads as a mean-reverting stochastic process to time entries.
- [[pairs-trading]] — Long one asset, short a correlated peer when their spread diverges; the classic stat-arb trade.
- [[statistical-arbitrage]] — Portfolio-scale mean reversion across many correlated instruments.
- [[grid-trading]] — Laddered buy/sell orders that mechanically harvest oscillation in a range.

### Momentum & Trend

- [[momentum-rotation]] — Rotating capital into the strongest-performing assets on a fixed schedule.
- [[commodity-momentum]] — Time-series momentum applied to commodity futures.
- [[session-overlap-momentum]] — Exploiting directional persistence during overlapping market sessions.

### Carry & Value

- [[commodity-carry-strategy]] — Harvesting roll yield from futures-curve backwardation and contango.
- [[commodity-value-strategy]] — Buying commodities cheap relative to long-run anchors, selling expensive ones.
- [[volatility-carry]] — Collecting the spread between implied and realized volatility.

### Volatility & Tail Risk

- [[garch-volatility]] — Forecasting volatility with GARCH models to time vol exposure and sizing.
- [[vix-trading]] — Trading VIX futures and the term structure directly.
- [[skew-trading]] — Trading the richness or cheapness of out-of-the-money option skew.
- [[tail-risk-hedging]] — Systematically owning convexity against crash scenarios.

### Regime & Signal Processing

- [[regime-detection]] — Hidden Markov models and clustering to classify trending, mean-reverting, or crisis states.
- [[kalman-filter-trading]] — Adaptive filtering for dynamic hedge ratios and fair-value estimation.

### Crypto Microstructure

- [[liquidation-cascade-fade]] — Buying forced-liquidation overshoots in crypto perpetuals.
- [[miner-capitulation-bottom]] — Timing Bitcoin cycle bottoms from miner stress indicators.

### Calendar, Sentiment & Equity

- [[calendar-effects]] — Seasonal and day-of-week anomalies (turn-of-month, January effect, etc.).
- [[sentiment-trading]] — Converting news and social sentiment data into systematic signals.

## All Pages (auto)

```dataview
TABLE status, updated, tags
FROM "wiki/strategies/quantitative"
WHERE type != "index" AND type != "overview"
SORT updated DESC
```

## Coverage Gaps

Factor investing and ML-driven models currently live under [[algorithmic-overview|algorithmic]] (see [[factor-investing]]); Monte Carlo simulation methodology belongs in concepts/backtesting rather than here.

## Related

- [[strategies-overview]] — top-level strategy catalog
- [[algorithmic-overview]] — execution- and automation-focused sibling category
- [[arbitrage-overview]] — pure relative-value sibling category
- [[edge-taxonomy]] — classification of where quant edges come from
- [[regime-matrix]] — mapping strategies to market regimes
- [[overfitting-detection]] — the family's chief failure mode
- [[backtesting-overview]] — validation methodology for everything on this page
