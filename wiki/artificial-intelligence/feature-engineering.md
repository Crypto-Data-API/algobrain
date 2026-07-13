---
title: "Feature Engineering"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, quantitative, indicators, backtesting]
aliases: ["Feature Engineering", "Feature Construction", "Feature Selection", "feature-engineering"]
domain: [ai-trading]
difficulty: intermediate
prerequisites: ["[[machine-learning-overview]]"]
related: ["[[machine-learning-overview]]", "[[supervised-learning]]", "[[overfitting-in-trading]]", "[[ml-trading-pipeline]]", "[[walk-forward-analysis]]", "[[indicators-overview]]", "[[deep-learning-overview]]", "[[random-forest-trading]]"]
---

Feature engineering is the process of transforming raw data into the input variables ("features") that a machine-learning model actually learns from. In trading it is usually the single highest-leverage activity in the modelling pipeline: a model is only as good as the features it sees, and well-constructed, predictive features routinely matter more than the choice of algorithm. Most of the alpha in classical financial ML lives in the features, not the model.

## Why It Matters in Trading

Raw market data -- a stream of prices and volumes -- is noisy, non-stationary, and barely predictive in its raw form. Feature engineering encodes domain knowledge into representations a model can exploit: turning a price series into momentum, mean-reversion, volatility, and microstructure signals that carry actual information about future returns. Tree-based models ([[random-forest-trading|random forests]], gradient boosting), which dominate tabular financial ML, depend entirely on hand-built features; even [[deep-learning-overview|deep-learning]] models, which learn features automatically, benefit from sensible inputs in the low-data, low-signal regime of markets.

## Common Trading Features

- **Price-derived / momentum** -- returns over multiple horizons, moving-average crossovers, RSI, MACD and other [[indicators-overview|technical indicators]], distance from moving averages.
- **Volatility** -- realised volatility, ATR, GARCH estimates, volatility-of-volatility, regime flags.
- **Volume / microstructure** -- order-flow imbalance, bid-ask spread, volume-weighted measures, trade-size distribution, depth.
- **Cross-sectional / relative** -- a stock's return rank vs its sector, beta, correlation to an index, factor exposures.
- **Fundamental** -- valuation ratios, earnings surprise, growth and quality metrics (point-in-time to avoid look-ahead).
- **Alternative / text** -- [[nlp-sentiment-analysis|sentiment scores]], news counts, satellite/foot-traffic data.
- **Calendar / event** -- day-of-week, time-to-earnings, days since FOMC, seasonality dummies.

## Techniques

- **Transformations** -- log returns, differencing, and **fractional differentiation** (López de Prado) to make a series stationary while retaining memory.
- **Scaling/normalisation** -- z-scoring, rolling normalisation, and ranking to keep features comparable across time and assets.
- **Lags and rolling windows** -- the core of time-series features; choosing window lengths is itself a modelling decision.
- **Interaction features** -- combining signals (e.g., momentum conditioned on volatility regime).
- **Feature selection** -- mutual information, model-based importance (with López de Prado's MDA/MDI caveats), and dimensionality reduction (PCA, autoencoders) to cut redundancy.

## The Look-Ahead and Leakage Trap

The defining hazard of financial feature engineering is **data leakage**: accidentally building a feature using information that was not available at decision time. Examples include using restated fundamentals instead of point-in-time data, normalising over a window that includes the future, or labelling with information that leaks across the train/test boundary. Leakage produces gorgeous backtests that collapse live. Features must be constructed strictly causally, validated with [[walk-forward-analysis|walk-forward analysis]] rather than random K-fold splits, and tested with purging/embargoing to prevent overlap between train and test labels.

## Overfitting Risk

Because you can generate effectively unlimited features from the same price series, feature engineering is a primary driver of [[overfitting-in-trading|overfitting]]. Every feature you try is a researcher degree of freedom; mining hundreds of candidates and keeping the best guarantees spurious "edge." Discipline -- a small, economically-motivated feature set, out-of-sample validation, and deflated performance metrics -- is what separates feature engineering from curve-fitting.

## Related

- [[machine-learning-overview]] · [[supervised-learning]] -- where features feed the model
- [[ml-trading-pipeline]] -- where feature engineering sits in the workflow
- [[overfitting-in-trading]] -- the central risk
- [[walk-forward-analysis]] -- causal validation that catches leakage
- [[indicators-overview]] -- a rich source of price-derived features
- [[random-forest-trading]] · [[deep-learning-overview]] -- consumers of features

## Sources

- López de Prado, *Advances in Financial Machine Learning* (2018) -- fractional differentiation, labelling, leakage, purged cross-validation, and feature-importance pitfalls
- Géron, *Hands-On Machine Learning* -- general feature-engineering and pipeline practice
- Standard quantitative-finance literature on technical and cross-sectional factor construction
