---
title: "Hyperparameter Tuning"
type: concept
created: 2026-04-09
updated: 2026-06-11
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Hyperparameter Tuning", "Hyperparameter Optimization", "HPO"]
domain: [ai-trading]
prerequisites: ["[[supervised-learning]]", "[[cross-validation-trading]]"]
difficulty: intermediate
related: ["[[supervised-learning]]", "[[overfitting-in-trading]]", "[[cross-validation-trading]]", "[[xgboost-trading]]", "[[bias-variance-tradeoff]]", "[[machine-learning-overview]]", "[[artificial-intelligence]]", "[[optuna]]", "[[pybroker]]", "[[walk-forward-analysis]]", "[[optimization-objectives]]", "[[deflated-sharpe-ratio]]"]
---

# Hyperparameter Tuning

**Hyperparameters** are settings that control how a model learns — they're set before training, not learned from data. Tuning them correctly is the difference between a model that generalizes to live markets and one that overfits to historical noise. Over-tuning hyperparameters is one of the most common ways traders inadvertently [[overfitting-in-trading|overfit]].

## Parameters vs Hyperparameters

| | Parameters | Hyperparameters |
|---|-----------|----------------|
| **What** | Model weights (learned from data) | Model settings (set by you) |
| **Example** | XGBoost tree split thresholds | Number of trees, learning rate, max depth |
| **Learned?** | Yes (during training) | No (you choose them) |
| **Risk** | Underfitting if model too small | Overfitting if tuned too aggressively |

## Key Hyperparameters by Model

| Model | Critical Hyperparameters |
|-------|------------------------|
| **[[xgboost-trading|XGBoost]]** | n_estimators, max_depth, learning_rate, subsample, colsample_bytree, min_child_weight |
| **[[random-forest-trading|Random Forest]]** | n_estimators, max_depth, max_features, min_samples_leaf |
| **[[lstm-trading|LSTM]]** | Number of layers, hidden units, dropout rate, learning rate, batch size |
| **Logistic Regression** | Regularization strength (C), penalty type (L1/L2) |

## Tuning Methods

| Method | How | Speed | Risk of Overfitting |
|--------|-----|-------|-------------------|
| **Grid Search** | Try every combination | Slow | Moderate (exhaustive) |
| **Random Search** | Try random combinations | Faster | Lower (less systematic) |
| **Bayesian Optimization** | Model the hyperparameter space, sample intelligently | Fast | Moderate |
| **Manual tuning** | Expert intuition | Fastest | Lowest (if experienced) |

## The Overfitting Trap

The biggest danger: **tuning hyperparameters on the same data you evaluate performance on.** This is equivalent to fitting the model to the test set — you'll find settings that look great historically but fail live.

**Solution**: Use a three-way split:
1. **Training set** — fit model parameters
2. **Validation set** — tune hyperparameters
3. **Test set** — final evaluation (only used ONCE)

For time series, this means [[cross-validation-trading|walk-forward validation]] with a separate holdout period.

## Optuna: The Recommended Framework for Trading

[[optuna|Optuna]] is the dominant choice for trading strategy optimization. Its default TPE (Tree-structured Parzen Estimator) sampler is a form of [[bayesian-optimization|Bayesian optimization]] and is typically far more sample-efficient than grid search (commonly cited as 5-20x fewer trials for comparable results). The define-by-run API lets you use Python control flow (if/else) inside the objective function — essential when some parameters only matter for certain strategy configurations. Native multi-objective support for optimizing Sharpe + drawdown simultaneously (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]).

## Trading-Specific Guidelines

1. **Fewer hyperparameters is better** — every tunable knob is a dimension of overfitting
2. **Use conservative defaults** — XGBoost defaults are surprisingly good
3. **Random search > grid search** — more efficient, equally effective
4. **Don't tune on the full period** — tune on a subset, validate on the rest
5. **Suspect any setting that seems too good** — if one specific max_depth produces amazing results but +/-1 is terrible, it's overfitting
6. **Always use temporal train/test splits** (not random) — combine with [[walk-forward-analysis]] to optimize in-sample, test out-of-sample, and roll forward (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
7. **Use [[deflated-sharpe-ratio]] to correct for multiple testing** — the more parameter combinations you try, the more likely you are to find one that looks good by chance
8. **Keep parameter count low relative to trade count** — a strategy with 10 parameters and 50 trades is almost certainly overfit
9. **Prefer [[optimization-objectives|objective functions]] that penalize drawdown**, not just maximize returns — pure return maximization finds fragile, leveraged strategies

## See Also

- [[overfitting-in-trading]] — The primary risk of over-tuning
- [[cross-validation-trading]] — Proper validation for tuning
- [[bias-variance-tradeoff]] — The theoretical framework
- [[xgboost-trading]] — Key hyperparameters for the most common trading model
- [[optuna]] — Recommended Bayesian optimization framework for trading
- [[pybroker]] — ML-first backtesting framework with native hyperparameter tuning integration
- [[walk-forward-analysis]] — The validation methodology that should wrap any tuning process
- [[optimization-objectives]] — Choosing what to optimize (Sharpe, Sortino, drawdown-adjusted)
- [[deflated-sharpe-ratio]] — Correcting for multiple testing during tuning
- [[machine-learning-overview]] — ML section hub
- [[artificial-intelligence]] — AI section hub

## Sources

- Bergstra, J. & Bengio, Y. (2012). "Random Search for Hyper-Parameter Optimization." *JMLR*, 13. (Foundational result that random search beats grid search.)
- Akiba, T. et al. (2019). "Optuna: A Next-generation Hyperparameter Optimization Framework." KDD. (TPE sampler, define-by-run API.)
- Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality." *Journal of Portfolio Management*.
- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]) — Optuna for trading strategy optimization and walk-forward integration.
