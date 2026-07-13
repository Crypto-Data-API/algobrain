---
title: "Optuna"
type: concept
created: 2026-04-14
updated: 2026-06-20
status: excellent
tags: [backtesting, python, algorithmic, machine-learning, quantitative]
aliases: ["Optuna", "Optuna Framework"]
domain: [backtesting]
difficulty: intermediate
related:
  - "[[bayesian-optimisation]]"
  - "[[hyperparameter-tuning]]"
  - "[[walk-forward-analysis]]"
  - "[[overfitting-in-trading]]"
  - "[[overfitting-detection]]"
  - "[[pybroker]]"
  - "[[vectorbt]]"
  - "[[backtrader-framework]]"
  - "[[hummingbot]]"
  - "[[deflated-sharpe-ratio]]"
  - "[[optimization-objectives]]"
  - "[[ml-trading-pipeline]]"
  - "[[cross-validation-trading]]"
  - "[[backtesting-py]]"
---

# Optuna

**Optuna** is an open-source automatic hyperparameter optimization framework for Python. Originally built for machine learning model tuning, it has become an essential tool for trading strategy parameter optimization due to its sample-efficient Bayesian search, pruning of unpromising trials, and multi-objective optimization capabilities. Install with `pip install optuna`. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Overview

Optuna uses a **define-by-run** API: the search space is defined inside the objective function itself, trial by trial, rather than declared upfront (as in older frameworks like Hyperopt). This means parameters can be conditionally sampled — e.g., only suggest `rsi_threshold` if the trial has already chosen `use_rsi = True`. The default sampler is **TPE (Tree-structured Parzen Estimator)**, a Bayesian optimization algorithm that models the relationship between parameters and objective values to focus search on the most promising regions of the parameter space. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Core Workflow

The fundamental Optuna pattern for strategy optimization:

```python
import optuna

def objective(trial):
    # Optuna suggests parameters from defined ranges
    ema_fast = trial.suggest_int("ema_fast", 5, 50)
    ema_slow = trial.suggest_int("ema_slow", 50, 200)
    sl_pct   = trial.suggest_float("sl_pct", 0.01, 0.05)

    # Run your backtest with these parameters
    result = run_backtest(ema_fast, ema_slow, sl_pct)

    # Return the metric to optimize
    return result.sharpe_ratio

# Create a study and run optimization
study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)

# Best parameters found
print(study.best_params)
print(f"Best Sharpe: {study.best_value:.3f}")
```

Each call to `study.optimize()` runs `n_trials` iterations. On each trial, Optuna's TPE sampler uses the history of all previous trials to propose the next set of parameters, concentrating on regions that have historically produced good results.

---

## Why TPE Beats Grid and Random Search

| Method | How It Works | Trials for 4 params × 10 values each | Sample Efficiency |
|--------|-------------|---------------------------------------|-------------------|
| **Grid Search** | Tests ALL combinations | 10,000 (10^4) | Worst — exponential in dimensions |
| **Random Search** | Samples randomly | ~500-1000 to find near-optimal | Better — works in high dimensions |
| **TPE (Optuna)** | Bayesian model guides search | ~50-200 to find near-optimal | Best — 5-20x more efficient than grid |

Grid search is exhaustive but suffers from the **curse of dimensionality**: adding one more parameter multiplies the total trials by the number of grid points. Random search is provably better in high dimensions (Bergstra & Bengio, 2012) because it samples each dimension independently. But TPE goes further: it builds two probability distributions — one for parameter values that produced good results (l(x)) and one for bad results (g(x)) — and samples new points that maximize l(x)/g(x). This focuses computation where it matters. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Parameter Suggestion API

The define-by-run API exposes a small set of `suggest_*` methods on the `trial` object. These are the building blocks of every objective function:

| Method | Returns | Trading Use |
|--------|---------|-------------|
| `trial.suggest_int(name, low, high, step=1, log=False)` | integer | Indicator periods (EMA, RSI lookback), bars held |
| `trial.suggest_float(name, low, high, step=None, log=False)` | float | Stop-loss %, Kelly fraction, ATR multiplier |
| `trial.suggest_categorical(name, choices)` | one of choices | Which indicator set, regime filter on/off, exit style |
| `trial.suggest_int(..., log=True)` / `suggest_float(..., log=True)` | log-scaled | Learning rate, regularization strength (spans orders of magnitude) |

The `log=True` flag is important for ML hyperparameters that span orders of magnitude (e.g., learning rate 1e-5 to 1e-1) — it samples uniformly in log space so each decade gets equal attention. `suggest_categorical` enables conditional search spaces: only suggest `rsi_threshold` inside an `if use_rsi:` branch.

## Samplers and Pruners Reference

Optuna decouples the **sampler** (how the next trial's parameters are chosen) from the **pruner** (when to abort a running trial). Both are configurable on `create_study`:

| Sampler | Algorithm | Best For |
|---------|-----------|----------|
| `TPESampler` (default) | Tree-structured Parzen Estimator | General-purpose; the default for most strategy tuning |
| `CmaEsSampler` | CMA-ES evolution strategy | Continuous, high-dimensional parameter spaces |
| `GPSampler` | Gaussian-process Bayesian optimization | Expensive objectives with few parameters |
| `RandomSampler` | Uniform random | Baseline / sanity check against TPE |
| `GridSampler` | Exhaustive grid | Small, fully enumerable spaces |
| `NSGAIISampler` | Genetic multi-objective | Many-objective Pareto problems |

| Pruner | Behavior | Aggressiveness |
|--------|----------|----------------|
| `MedianPruner` | Prune below median of completed trials at the same step | Moderate |
| `PercentilePruner` | Prune below Nth percentile at the same step | Tunable |
| `SuccessiveHalvingPruner` | ASHA-style resource halving | High |
| `HyperbandPruner` | Adaptive resource allocation across brackets | Highest |
| `NopPruner` | Disable pruning | None |

```python
study = optuna.create_study(
    sampler=optuna.samplers.TPESampler(seed=42),
    pruner=optuna.pruners.MedianPruner(n_warmup_steps=3),
    direction="maximize",
)
```

Setting a `seed` on the sampler makes a study reproducible — important when reporting backtest results so the parameter search itself is auditable.

---

## Trading-Specific Usage

### Indicator Parameter Optimization
- EMA/SMA periods, RSI lookback windows, [[bollinger-bands|Bollinger Band]] widths
- MACD fast/slow/signal periods, ATR multipliers for stops
- Any numerical parameter in a [[technical-analysis|technical]] strategy

### Execution Parameter Optimization
- Stop-loss distances (fixed %, ATR-based multiplier)
- Take-profit levels and risk/reward ratios
- Position sizing parameters (Kelly fraction, fixed fractional %)
- Trailing stop activation and offset distances

### ML Model Hyperparameter Optimization
- Learning rate, tree depth, number of estimators for gradient boosting
- Feature selection: which features to include/exclude
- Regularization strength, dropout rates
- Lookback window for training data

### Objective Function = Backtest Result
The objective function wraps your entire backtest. It receives parameters from Optuna, runs the backtest, and returns a scalar metric. Common choices:

- [[sharpe-sortino-calmar|Sharpe Ratio]] — risk-adjusted return (most common)
- [[sharpe-sortino-calmar|Sortino Ratio]] — downside-risk-adjusted return
- [[sharpe-sortino-calmar|Calmar Ratio]] — return / max drawdown
- Profit factor — gross profit / gross loss
- Custom composites — see [[optimization-objectives]]

---

## Integration with Backtesting Libraries

Optuna is framework-agnostic — any Python function that returns a number can be an objective. But some frameworks have particularly clean integration patterns:

### PyBroker (Native Integration)
[[pybroker|PyBroker]] has built-in Optuna support. Pass an Optuna study directly to PyBroker's optimization API, and it handles walk-forward windowing, model training, and parameter search in one unified loop. This is the tightest integration available. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

### Backtrader
Wrap [[backtrader-framework|Backtrader]]'s `cerebro.run()` in an Optuna objective function:

```python
def objective(trial):
    cerebro = bt.Cerebro()
    cerebro.adddata(data)
    cerebro.addstrategy(MyStrategy,
        fast_period=trial.suggest_int("fast", 5, 50),
        slow_period=trial.suggest_int("slow", 50, 200))
    cerebro.broker.setcash(100000)
    results = cerebro.run()
    return results[0].analyzers.sharpe.get_analysis()["sharperatio"]
```

### VectorBT
Wrap [[vectorbt|VectorBT]]'s `Portfolio.from_signals()`:

```python
def objective(trial):
    fast = trial.suggest_int("fast", 5, 50)
    slow = trial.suggest_int("slow", 50, 200)
    fast_ma = vbt.MA.run(close, fast)
    slow_ma = vbt.MA.run(close, slow)
    entries = fast_ma.ma_crossed_above(slow_ma)
    exits = fast_ma.ma_crossed_below(slow_ma)
    pf = vbt.Portfolio.from_signals(close, entries, exits)
    return pf.sharpe_ratio()
```

### Hummingbot (Built-In)
[[hummingbot|Hummingbot]] has built-in Optuna optimization for market-making controller parameters — spread, order amount, inventory skew, refresh time — using TPE with historical exchange data replay. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

### Backtesting.py
Wrap [[backtesting-py|Backtesting.py]]'s `bt.run()` in an Optuna objective. This replaces Backtesting.py's built-in grid optimizer with a smarter search.

### Custom Loops
Any custom Python backtesting loop works. If your function takes parameters and returns a number, Optuna can optimize it.

---

## Pruning (Early Stopping of Bad Trials)

Optuna can terminate unpromising trials before they complete, saving significant computation:

```python
def objective(trial):
    params = {...}  # suggest parameters
    for month in range(12):
        partial_sharpe = run_backtest_partial(params, months=month+1)
        trial.report(partial_sharpe, month)
        if trial.should_prune():
            raise optuna.TrialPruned()
    return run_backtest_full(params).sharpe_ratio
```

Built-in pruners:
- **MedianPruner** — prune if below median of completed trials at same step
- **PercentilePruner** — prune if below Nth percentile
- **HyperbandPruner** — adaptive resource allocation (most aggressive)

Pruning is especially valuable when backtests are computationally expensive (e.g., tick-level simulation, ML model training inside the loop).

---

## Multi-Objective Optimization

Optuna supports **Pareto-front optimization** — optimizing for multiple objectives simultaneously:

```python
def objective(trial):
    params = {...}
    result = run_backtest(params)
    return result.sharpe_ratio, result.max_drawdown  # maximize Sharpe, minimize drawdown

study = optuna.create_study(directions=["maximize", "minimize"])
study.optimize(objective, n_trials=200)

# Returns the set of Pareto-optimal solutions
for trial in study.best_trials:
    print(f"Sharpe: {trial.values[0]:.2f}, MaxDD: {trial.values[1]:.2%}")
```

Instead of a single "best" result, you get the **Pareto front**: the set of non-dominated solutions where improving one objective necessarily worsens another. This is invaluable for trading because you almost always care about multiple dimensions (return vs risk vs drawdown vs trade frequency). See [[optimization-objectives]] for guidance on choosing objectives.

---

## Visualization

Optuna includes built-in Plotly visualizations:

| Function | What It Shows |
|----------|---------------|
| `plot_optimization_history(study)` | Objective value over trials — see convergence |
| `plot_param_importances(study)` | Which parameters affect the objective most |
| `plot_parallel_coordinate(study)` | Parameter relationships across all trials |
| `plot_contour(study)` | 2D contour plot of parameter interactions |
| `plot_slice(study)` | Objective vs each parameter individually |

`plot_param_importances()` is particularly useful: if a parameter has near-zero importance, it means the strategy is insensitive to it, which is actually a good sign (robust to that parameter's exact value).

---

## Critical Warning: Overfitting Risk

Running 100+ Optuna trials on in-sample data without proper validation is a recipe for **guaranteed overfitting**. The more trials you run, the more likely you are to find a parameter set that fits noise rather than signal. A backtest Sharpe above 2.0 more likely signals overfitting than genuine alpha. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

**ALWAYS pair Optuna with one or more of the following:**

1. **[[walk-forward-analysis|Walk-forward optimization]]** — optimize in-sample, test out-of-sample, roll forward. The gold standard. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
2. **Temporal train/test split** — at minimum, hold out the most recent 20-30% of data as a final out-of-sample test
3. **[[deflated-sharpe-ratio]]** — corrects the Sharpe ratio for the number of trials tested. If you ran 200 Optuna trials, the deflated Sharpe accounts for the selection bias of picking the best one
4. **[[monte-carlo-permutation-test|Monte Carlo permutation test]]** — shuffle returns to test whether the strategy's performance could have arisen by chance
5. **Parameter sensitivity analysis** — if the best parameters are a narrow spike surrounded by poor performance, the result is likely overfit. Good strategies have broad, plateau-like optima

**Rule of thumb:** Expect live Sharpe to be roughly 50% of backtest Sharpe. A backtest Sharpe of 1.0-1.5 is a healthy target; if you see 3.0+ from Optuna optimization, be suspicious. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## How AI and Trading Systems Consume Optuna

Optuna sits at a specific layer of the [[ml-trading-pipeline|ML / strategy pipeline]]: it is the *outer optimization loop* that wraps a backtest or model-training step. Understanding where it fits clarifies how to use it without corrupting the validation:

| Pipeline Layer | Role of Optuna | Guardrail |
|----------------|----------------|-----------|
| Feature engineering | Tune lookback windows, smoothing | Lock features per fold to avoid leakage |
| Model training (ML) | Tune learning rate, depth, regularization | Tune on inner CV fold only ([[cross-validation-trading]]) |
| Strategy parameters | Tune indicator periods, stops, sizing | Optimize in-sample, score out-of-sample |
| Validation | Count trials for [[deflated-sharpe-ratio]] | Record `len(study.trials)` |
| Deployment | Persist `best_params` + study DB | Version the study with the strategy |

The cleanest pattern nests Optuna *inside* a walk-forward loop: for each in-sample window, run a study to pick parameters, then evaluate those frozen parameters on the next out-of-sample window. This is exactly how [[pybroker|PyBroker]] integrates Optuna natively. The number of trials per window directly determines the selection bias the [[deflated-sharpe-ratio]] must correct for — so log it.

For agentic / LLM-driven research, an AI agent can drive Optuna programmatically (define the objective, launch the study, read `study.best_params` and `plot_param_importances`), but the same overfitting discipline applies: an agent that maximizes in-sample Sharpe across hundreds of trials produces the same inflated, non-reproducible result a human would. The agent should be instructed to report the deflated Sharpe and the out-of-sample score, not the raw `best_value`.

## Best-Practice Checklist

1. Define the search space as wide as is economically plausible, not as narrow as you "expect" — narrow priors smuggle in [[overfitting-in-trading|overfitting]].
2. Seed the sampler for reproducibility; persist the study DB.
3. Wrap the study in [[walk-forward-analysis|walk-forward]]; never optimize and evaluate on the same data.
4. Use `suggest_float(..., log=True)` for scale-spanning parameters.
5. Enable a pruner when each backtest is expensive (tick data, ML training).
6. Check `plot_param_importances` — near-zero importance is a *good* robustness sign.
7. Prefer broad, plateau-like optima over sharp spikes (parameter sensitivity analysis).
8. Record `n_trials` and apply the [[deflated-sharpe-ratio]].
9. Expect live Sharpe ≈ 50% of backtest Sharpe; treat 3.0+ as a red flag.

## Storage and Persistence

Optuna studies can be persisted to a database for resumption and collaboration:

```python
# SQLite (local)
study = optuna.create_study(storage="sqlite:///optuna.db", study_name="ema_cross")

# PostgreSQL (shared)
study = optuna.create_study(storage="postgresql://user:pass@host/db", study_name="ema_cross")
```

This allows you to:
- Resume optimization after interruption
- Share results across team members
- Run distributed optimization across multiple machines

---

## Optuna vs Alternatives

| Framework | Search Algorithm | API Style | Distributed | Multi-Objective | Trading Ecosystem |
|-----------|-----------------|-----------|-------------|-----------------|-------------------|
| **Optuna** | TPE, CMA-ES, GP | Define-by-run | Yes (via DB) | Yes | Best ([[pybroker]], [[hummingbot]]) |
| **Hyperopt** | TPE | Define-and-run | Yes (MongoDB) | No | Moderate |
| **scikit-optimize** | GP, RF, ET | Functional | No | No | Minimal |
| **Ray Tune** | Many (wraps Optuna, etc.) | Config-based | Yes (native) | Via Optuna | Moderate |
| **Ax (Facebook)** | GP, Bayesian | OOP | Yes | Yes | Minimal |

Optuna is the default recommendation for trading strategy optimization due to its flexibility, TPE efficiency, native multi-objective support, and direct integrations with [[pybroker]] and [[hummingbot]]. (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])

---

## Sources

- (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]])
- Optuna documentation: https://optuna.readthedocs.io/
- Akiba et al. (2019), "Optuna: A Next-generation Hyperparameter Optimization Framework"
- Bergstra & Bengio (2012), "Random Search for Hyper-Parameter Optimization" — the random-vs-grid result
- [[deflated-sharpe-ratio]] — why trial count must be corrected for
- [[walk-forward-analysis]] — the validation wrapper Optuna must sit inside

## Related

- [[bayesian-optimisation]] — the family TPE belongs to
- [[hyperparameter-tuning]] — the general problem Optuna solves
- [[walk-forward-analysis]] — pair Optuna with this, always
- [[overfitting-in-trading]] / [[overfitting-detection]] — the core risk
- [[deflated-sharpe-ratio]] — corrects for the number of trials
- [[cross-validation-trading]] — inner-loop validation for ML tuning
- [[optimization-objectives]] — choosing the objective function
- [[ml-trading-pipeline]] — where Optuna fits in the stack
- [[pybroker]] · [[vectorbt]] · [[backtrader-framework]] · [[backtesting-py]] · [[hummingbot]] — integrations
- [[backtesting]] — parent concept
