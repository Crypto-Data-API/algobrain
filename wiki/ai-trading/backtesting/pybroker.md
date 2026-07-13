---
title: "PyBroker"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [backtesting, python, machine-learning, algorithmic]
aliases: ["PyBroker", "pybroker"]
domain: [backtesting]
difficulty: intermediate
related:
  - "[[optuna]]"
  - "[[vectorbt]]"
  - "[[backtrader-framework]]"
  - "[[zipline-framework]]"
  - "[[ml-trading-pipeline]]"
  - "[[cross-validation-trading]]"
  - "[[walk-forward-analysis]]"
  - "[[backtesting-py]]"
  - "[[purged-kfold-cv]]"
  - "[[lookahead-bias]]"
  - "[[backtesting]]"
  - "[[market-regime-detection-ml]]"
---

# PyBroker

**PyBroker** is an ML-first backtesting framework for Python that natively integrates [[optuna|Optuna]] hyperparameter optimization and scikit-learn model pipelines into the backtest loop. Unlike general-purpose backtesting frameworks that bolt on ML as an afterthought, PyBroker is designed from the ground up to train, evaluate, and deploy machine learning models with proper temporal awareness. Website: [pybroker.com](https://pybroker.com). (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Overview

Most backtesting frameworks treat strategy logic as a set of rules applied to price data. PyBroker treats it as a **prediction pipeline**: features are engineered, models are trained on historical windows, predictions generate signals, and orders are executed — all within a single framework that respects the temporal ordering of data and prevents [[lookahead-bias|look-ahead bias]].

### At a Glance

| Attribute | Detail |
|-----------|--------|
| **Author** | Edward West (open-source) |
| **Website / docs** | [pybroker.com](https://pybroker.com) |
| **Install** | `pip install lib-pybroker` |
| **Engine type** | [[event-driven-backtesting\|Event-driven]] + ML training loop |
| **Core abstraction** | `indicator` → `model` → `strategy(ctx)` prediction pipeline |
| **Model layer** | Any scikit-learn-compatible estimator (RandomForest, [[xgboost\|XGBoost]], LightGBM, etc.) |
| **Validation** | Built-in [[walk-forward-analysis\|walk-forward]] + [[purged-kfold-cv\|purged k-fold]] CV with embargo |
| **Optimization** | Native [[optuna\|Optuna]] integration |
| **Acceleration** | Vectorized with NumPy/Numba where possible; data + feature caching |
| **Multi-asset** | Yes |
| **Live trading** | Not a focus — research/backtest tool |

The conceptual lineage is explicit: PyBroker operationalizes the methodology of Marcos López de Prado's *Advances in Financial Machine Learning* — purged, embargoed cross-validation and walk-forward training — as first-class framework features rather than something the researcher must hand-roll. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Key Features

| Feature | Detail |
|---------|--------|
| **ML-First Design** | Train models inside the backtest loop with automatic temporal windowing |
| **Optuna Integration** | Native support — pass an Optuna study directly to PyBroker's optimization API |
| **scikit-learn Compatibility** | Plug in any sklearn model (RandomForest, XGBoost, LightGBM, etc.) |
| **Time-Series CV** | Built-in purged, embargo-aware cross-validation (prevents data leakage) |
| **Feature Engineering** | Define custom indicators and features that are computed before model training |
| **Walk-Forward** | Automated [[walk-forward-analysis|walk-forward optimization]] with configurable train/test windows |
| **Data Caching** | Caches downloaded data and computed features for fast re-runs |

---

## Core Workflow

```python
import pybroker as pb
from sklearn.ensemble import GradientBoostingClassifier

# Define custom indicator
@pb.indicator("rsi_14")
def rsi_14(data):
    return compute_rsi(data.close, period=14)

# Define model and training
model = pb.model("gbc", GradientBoostingClassifier, indicators=["rsi_14"])

# Define strategy using model predictions
@pb.strategy("ml_strategy", models=["gbc"])
def ml_strategy(ctx):
    if ctx.preds("gbc") > 0.6:
        ctx.buy_shares = 100
    elif ctx.preds("gbc") < 0.4:
        ctx.sell_shares = 100

# Configure and run backtest
config = pb.StrategyConfig(
    start_date="2020-01-01",
    end_date="2024-01-01",
    initial_cash=100_000
)
result = pb.backtest(config, strategy=ml_strategy)
```

The key insight: PyBroker automatically handles the temporal split so that the model is always trained on past data and tested on future data. No manual `.shift(1)` or custom windowing logic needed.

---

## Optuna Integration

PyBroker's Optuna integration is the tightest available in any backtesting framework:

```python
import optuna

def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 50, 500)
    max_depth = trial.suggest_int("max_depth", 3, 10)
    lookback = trial.suggest_int("lookback", 20, 252)

    model = pb.model("gbc", GradientBoostingClassifier,
                      n_estimators=n_estimators, max_depth=max_depth)

    result = pb.backtest(config, strategy=ml_strategy,
                         train_size=lookback)
    return result.sharpe_ratio

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)
```

The optimization searches over both model hyperparameters (tree depth, estimators) and strategy parameters (lookback windows, thresholds) simultaneously within proper walk-forward windows. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Time-Series Cross-Validation

PyBroker implements **purged k-fold cross-validation** with embargo periods — the same methodology advocated by Marcos Lopez de Prado in *Advances in Financial Machine Learning*:

- **Purged**: Removes training samples that overlap with the test set to prevent information leakage
- **Embargo**: Adds a gap between training and test sets to account for serial correlation in financial returns
- See [[purged-kfold-cv]] for the theoretical foundation

This is critical because standard k-fold CV (random splits) creates massive look-ahead bias in time-series data.

---

## How AI / ML Trading Systems Use It

PyBroker fits the role of the **research-and-validation engine** in an ML trading pipeline, sitting downstream of feature engineering and upstream of production execution:

1. **Feature → model → signal pipeline.** Indicators registered via `@pb.indicator` are computed before training; the registered model consumes them; the strategy function reads `ctx.preds(...)` to size orders. Because the framework owns the temporal split, the researcher does not manually `.shift()` features — the single most common source of [[lookahead-bias|look-ahead bias]] (source #7 in that page) is removed by construction.
2. **Walk-forward as the default evaluation.** Rather than reporting one in-sample Sharpe, PyBroker retrains on each rolling window and evaluates out-of-sample, which is the honest test for a learned model. This dovetails with [[market-regime-detection-ml|regime-aware]] evaluation: each walk-forward fold ideally spans a representative regime mix, not a single calm window.
3. **Joint hyperparameter + strategy search.** The [[optuna|Optuna]] integration optimizes model hyperparameters (tree depth, estimators) and strategy parameters (lookback, thresholds) *inside* proper walk-forward windows, so the search itself cannot cheat by peeking forward.
4. **Reproducible re-runs.** Data and feature caching makes large experiment sweeps tractable and repeatable — important for the kind of trial accounting that a [[deflated-sharpe-ratio|deflated Sharpe]] correction requires.

### Where leakage can still creep in

PyBroker prevents the *mechanical* leakage of training on future bars, but it cannot prevent leakage that is baked into the **input data** before it ever reaches the framework:

| Leakage source | Prevented by PyBroker? | Researcher must handle |
|----------------|------------------------|------------------------|
| Training on future bars | Yes — temporal windowing | — |
| Random CV splits on time series | Yes — purged k-fold + embargo | — |
| Restated fundamentals / revised macro | No | Supply [[point-in-time-data\|point-in-time]] inputs |
| Survivorship-biased universe | No | Supply point-in-time membership |
| Look-ahead inside a custom indicator | No | Author indicators carefully |

The framework moves the leak risk *upstream* into data provisioning — which is exactly where it should be addressed. See [[lookahead-bias]] for the full source taxonomy.

---

## Comparison with Other Frameworks

| Feature | PyBroker | [[backtrader-framework|Backtrader]] | [[vectorbt|VectorBT]] | [[zipline-framework|Zipline]] |
|---------|----------|------------|----------|--------|
| **Engine** | Event-driven + ML | Event-driven | Vectorized | Event-driven |
| **ML Integration** | Native (sklearn, Optuna) | None (manual) | None (manual) | Limited |
| **Speed** | Moderate | Slow | Fast (1000x) | Moderate |
| **Walk-Forward** | Built-in | Manual | Manual | Manual |
| **Multi-Asset** | Yes | Yes | Yes | Yes |
| **Time-Series CV** | Purged k-fold | None | None | None |
| **Complexity** | Moderate | Low-Moderate | Low | High |

**When to use PyBroker:** You are building ML-driven strategies and want proper temporal validation without manually coding walk-forward loops and purged CV. It is the right tool when the strategy's core logic is a trained model rather than a set of indicator rules.

**When NOT to use PyBroker:** For simple rule-based strategies ([[backtrader-framework|Backtrader]] or [[backtesting-py|Backtesting.py]] is simpler), for rapid parameter sweeps on vectorized strategies ([[vectorbt|VectorBT]] is 100-1000x faster), or for production deployment to a specific broker ([[zipline-framework|Zipline]]/Alpaca integration).

---

## Limitations

- Smaller community compared to Backtrader or VectorBT
- Less broker connectivity — primarily a research/backtesting tool, not a live trading framework
- Documentation is growing but not as extensive as more mature frameworks
- Vectorized operations are not the focus — slower than VectorBT for large parameter sweeps

---

## When to Reach for PyBroker (Decision Table)

| Your situation | Use PyBroker? | Better alternative |
|----------------|---------------|--------------------|
| Strategy core is a trained ML model | Yes | — |
| Need purged/embargoed CV without hand-coding it | Yes | — |
| Want walk-forward + Optuna in one place | Yes | — |
| Simple indicator-crossover rules | Overkill | [[backtesting-py]], [[backtrader-framework\|Backtrader]] |
| Thousands of fast parameter sweeps | No | [[vectorbt]] (vectorized) |
| Live deployment to a specific broker | No | [[zipline-framework\|Zipline]] / Alpaca, [[backtrader-framework\|Backtrader]] |

---

## Related

- [[backtesting-py]] — lighter single-asset prototyper (no ML loop)
- [[vectorbt]] — vectorized engine, far faster for parameter sweeps
- [[backtrader-framework]] — mature event-driven framework with live trading
- [[zipline-framework]] — production-oriented event-driven framework
- [[optuna]] — the optimizer PyBroker integrates natively
- [[purged-kfold-cv]] — the leak-free CV PyBroker implements
- [[walk-forward-analysis]] — PyBroker's default evaluation mode
- [[cross-validation-trading]] / [[ml-trading-pipeline]] — surrounding methodology
- [[lookahead-bias]] — the bias PyBroker structurally prevents (and where it cannot)
- [[market-regime-detection-ml]] — regime-aware evaluation that pairs with walk-forward
- [[backtesting]] — broader backtest hygiene

---

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
- PyBroker documentation: https://www.pybroker.com
