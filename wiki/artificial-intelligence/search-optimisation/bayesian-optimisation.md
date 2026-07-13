---
title: "Bayesian Optimisation"
type: concept
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [ai-trading, machine-learning, education, backtesting]
aliases: ["Bayesian Optimisation", "Bayesian Optimization", "BO", "TPE"]
domain: [ai-trading]
prerequisites: ["[[hyperparameter-tuning]]", "[[cross-validation-trading]]"]
difficulty: advanced
related: ["[[search-optimisation-overview]]", "[[hyperparameter-tuning]]", "[[evolutionary-algorithms]]", "[[simulated-annealing]]", "[[cross-validation-trading]]", "[[artificial-intelligence]]", "[[optuna]]", "[[optimization-objectives]]", "[[walk-forward-analysis]]"]
---

# Bayesian Optimisation

**Bayesian optimisation** (BO) is an efficient strategy for optimising expensive black-box functions. It builds a probabilistic model of the objective function and uses it to decide where to evaluate next — maximising information gain per evaluation. The framework traces to Jonas Mockus's work in the 1970s on global optimisation using a Bayesian (probabilistic) prior over the objective, and was popularised in machine learning by Snoek, Larochelle and Adams (*Practical Bayesian Optimization of Machine Learning Algorithms*, 2012). In trading, BO is the gold standard for [[hyperparameter-tuning|hyperparameter tuning]] where each evaluation requires a full backtest (minutes to hours).

## How It Works

```
1. Evaluate objective at a few random points
2. Fit a surrogate model (Gaussian Process) to observed points
3. Use an acquisition function to choose the next point to evaluate
   (balance: explore uncertain regions vs exploit promising ones)
4. Evaluate objective at chosen point (run backtest)
5. Update surrogate model with new observation
6. Repeat from step 3 until budget exhausted
```

| Component | Role | Trading Analogy |
|-----------|------|----------------|
| **Surrogate model** | Cheap approximation of the expensive objective | "Mental model" of how parameter changes affect Sharpe |
| **Acquisition function** | Decides where to evaluate next | "Where should I run my next backtest?" |
| **Uncertainty estimate** | GP provides mean AND variance at each point | "How confident am I in this region of parameter space?" |

## Why BO for Trading

Each backtest evaluation is **expensive** — a full walk-forward backtest might take 5-30 minutes. If you have 10 hyperparameters and a budget of 100 evaluations:

| Method | Evaluations Needed | Strategy |
|--------|-------------------|---------|
| **Grid search** | 10^10 (impossible) | Evaluate every combination |
| **Random search** | 100-1000 | Random sampling |
| **[[evolutionary-algorithms|GA]]** | 500-2000 | Population-based evolution |
| **Bayesian optimisation** | **50-100** | Model-guided, maximally informative | 

BO uses 5-20x fewer evaluations than alternatives by intelligently choosing which parameter combinations to test.

## Acquisition Functions

| Function | Strategy | When to Use |
|----------|---------|-------------|
| **Expected Improvement (EI)** | Choose point with highest expected improvement over current best | Default, well-balanced |
| **Upper Confidence Bound (UCB)** | Choose point where mean + uncertainty is highest | When exploration matters |
| **Probability of Improvement (PI)** | Choose point most likely to beat current best | When you want quick convergence |
| **Thompson Sampling** | Sample from posterior, optimise the sample | Good for parallel evaluations |

## Surrogate Models

| Model | Strengths | Limitations |
|-------|-----------|-----------|
| **Gaussian Process (GP)** | Principled uncertainty, smooth functions | Scales poorly beyond ~1000 observations |
| **TPE** (Tree-structured Parzen Estimator) | Handles conditional/categorical parameters | Less principled uncertainty |
| **Random Forest** | Robust, handles many parameter types | Rougher uncertainty estimates |
| **Neural Network (BOHAMIANN)** | Scales to high dimensions | More complex to configure |

TPE was introduced by Bergstra, Bardenet, Bengio and Kégl (*Algorithms for Hyper-Parameter Optimization*, NIPS 2011). Rather than modelling `p(score | params)` directly like a GP, TPE models the densities of "good" and "bad" parameter configurations — `l(x)` for trials above a quantile threshold and `g(x)` for those below — and proposes points that maximise the ratio `l(x)/g(x)`. BOHAMIANN (Springenberg et al., 2016) uses a Bayesian neural network trained with stochastic-gradient Hamiltonian Monte Carlo as the surrogate, trading GP exactness for better scaling to high dimensions and large evaluation budgets.

## Tools

| Library | Surrogate | Language | Trading Notes |
|---------|----------|---------|---------------|
| **Optuna** | TPE | Python | Most popular, easy integration with ML pipelines |
| **Hyperopt** | TPE | Python | Mature, good for distributed tuning |
| **BoTorch** | GP | Python (PyTorch) | State-of-the-art, flexible, supports multi-objective |
| **Ax (Meta)** | GP | Python | High-level API on top of BoTorch |
| **SMAC3** | Random Forest | Python | Robust for noisy objectives |

## Trading Example

Tuning an [[xgboost-trading|XGBoost]] trading model:

```python
import optuna

def objective(trial):
    params = {
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('lr', 0.01, 0.3, log=True),
        'n_estimators': trial.suggest_int('n_estimators', 50, 500),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),
    }
    sharpe = walk_forward_backtest(params)  # expensive evaluation
    return sharpe

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)  # 100 intelligent evaluations
```

## Optuna's TPE Sampler

[[optuna|Optuna]] uses Tree-structured Parzen Estimator (TPE) rather than Gaussian Process (GP). TPE is more scalable to high dimensions, handles categorical and conditional parameters naturally, and is faster per iteration than GP-based methods. For trading, TPE is better than GP because strategy parameter spaces often include categorical choices (which indicator? which timeframe?) alongside continuous values (lookback period, threshold). Optuna's TPE implementation is the most mature and widely used in the Python ecosystem (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]).

## Trading Application Example

Optimizing a moving average crossover strategy with [[optuna|Optuna]]:

```python
import optuna

def objective(trial):
    fast_period = trial.suggest_int('fast_period', 5, 50)
    slow_period = trial.suggest_int('slow_period', 20, 200)
    stop_loss_pct = trial.suggest_float('stop_loss_pct', 0.01, 0.10)

    if fast_period >= slow_period:
        return float('-inf')  # invalid combination

    sharpe = backtest_ma_crossover(fast_period, slow_period, stop_loss_pct)
    return sharpe

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

# Examine which parameters actually matter
importances = optuna.importance.get_param_importances(study)
# Typically: slow_period > fast_period >> stop_loss_pct
```

After 100 trials, examining parameter importance reveals which parameters actually drive performance and which are noise — a critical diagnostic for avoiding overfitting (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]).

## Multi-Objective Optimization

[[optuna|Optuna]] supports Pareto-front optimization via `optuna.create_study(directions=["maximize", "minimize"])` — useful for trading where you want to maximize Sharpe AND minimize max drawdown simultaneously. The result is a set of Pareto-optimal strategies rather than a single "best" one, letting the trader choose their preferred risk/return tradeoff from the efficient frontier of parameter combinations (Source: [[2026-04-14-backtesting-strategy-optimization-wiki]]).

```python
def multi_objective(trial):
    params = {
        'lookback': trial.suggest_int('lookback', 10, 100),
        'threshold': trial.suggest_float('threshold', 0.5, 2.0),
    }
    sharpe, max_dd = backtest_with_metrics(params)
    return sharpe, max_dd  # maximize sharpe, minimize drawdown

study = optuna.create_study(directions=["maximize", "minimize"])
study.optimize(multi_objective, n_trials=200)
# study.best_trials returns the Pareto front
```

> Note: TPE is Optuna's default sampler for *single-objective* studies. For multi-objective studies, Optuna defaults to an NSGA-II genetic sampler (see [[evolutionary-algorithms]]) rather than TPE, unless a sampler is passed explicitly. Both are valid — the Pareto-front semantics above are unchanged.

See [[optimization-objectives]] for guidance on choosing which objectives to optimize.

## The Overfitting Trap (read this before tuning)

BO is dangerous *precisely because it is efficient*. By spending its evaluation budget on the highest-scoring regions of parameter space, it is unusually good at finding the configuration that best fits your particular historical sample — including its noise. The more efficiently you search, the more aggressively you mine the in-sample data for a lucky fit. This is the central paradox: **a better optimiser produces a worse out-of-sample strategy unless the evaluation is honest.**

| Failure mode | What happens | Mitigation |
|--------------|--------------|------------|
| In-sample peak chasing | BO converges on a parameter set that exploits noise specific to the backtest window | Score on [[walk-forward-analysis\|walk-forward]] / nested out-of-sample, never on the fit window |
| Multiple-comparisons inflation | 100 trials = 100 chances to find a spurious Sharpe; the reported best is biased upward | Apply the [[deflated-sharpe-ratio]] / [[probability-of-backtest-overfitting\|PBO]]; haircut the headline metric |
| Objective gaming | A naive objective (raw Sharpe) is maximised by fragile, high-turnover configs | Use cost-corrected, drawdown-aware objectives — see [[optimization-objectives]] |
| Too many free parameters | A 10-D space lets BO interpolate almost any in-sample curve | Reduce dimensionality; prefer few robust parameters over many |
| Reusing the test set | Iterating tuning → checking test → re-tuning leaks the test set | Lock a final holdout; touch it once |

Practical rules:

1. **Wrap BO inside walk-forward, not the other way around.** The objective function passed to `study.optimize` must already return an *out-of-sample* (or walk-forward-aggregated) metric. If the objective is an in-sample backtest, the whole exercise is overfitting with extra steps. See [[walk-forward-analysis]] and [[cross-validation-trading]].
2. **Deflate the result.** Because you ran many trials, the best observed Sharpe is upward-biased. Adjust with the [[deflated-sharpe-ratio]] before believing it. See [[overfitting]].
3. **Prefer parameter *plateaus* over *peaks*.** A robust strategy sits on a broad region where nearby parameters all perform similarly. A single sharp spike in the surrogate's mean is usually noise. Use `optuna.importance` and contour/slice plots to inspect the landscape, not just `study.best_params`.
4. **Fewer parameters, fewer trials.** The risk of overfitting scales with both the dimensionality of the search space and the number of trials. Resist the urge to tune everything.
5. **Hold out a final, untouched test period** and evaluate the chosen configuration exactly once.

> The efficiency of BO is a feature for *honest* objectives and a foot-gun for naive ones. If your evaluation procedure is sound, BO finds a good answer in far fewer backtests; if it is not, BO finds the most overfit answer faster than any other method. See [[overfitting]] and [[backtest-overfitting]].

## Method comparison summary

| Method | Eval budget | Handles categorical/conditional | Parallelism | Overfitting risk profile | Best when |
|--------|-------------|----------------------------------|-------------|--------------------------|-----------|
| Grid search | Explodes with dimensions | Yes | Embarrassingly parallel | High (exhaustive in-sample mining) | ≤2-3 params, cheap evals |
| Random search | Moderate | Yes | Embarrassingly parallel | Moderate | Baseline; good with few important dims |
| **Bayesian optimisation** | **Lowest** | TPE: yes; GP: limited | Moderate (async/Thompson) | High *if objective is in-sample* | Expensive evals (full backtests) |
| [[evolutionary-algorithms\|Genetic / NSGA-II]] | High | Yes | Population-parallel | Moderate-high | Cheap evals, rugged/multi-objective spaces |
| [[simulated-annealing]] | Moderate | Awkward | Single-agent | Moderate | Single-objective, rugged landscape |

The overfitting-risk column is conditional on the evaluation procedure: *any* optimiser overfits a dishonest objective, and BO does so most efficiently. The defence is the same for all of them — out-of-sample scoring plus a deflation step.

## Sources

- Mockus, J. (1989). *Bayesian Approach to Global Optimization*. Kluwer. (Foundational formulation of BO.)
- Snoek, J., Larochelle, H., & Adams, R. P. (2012). "Practical Bayesian Optimization of Machine Learning Algorithms." *NeurIPS 2012*. https://arxiv.org/abs/1206.2944
- Bergstra, J., Bardenet, R., Bengio, Y., & Kégl, B. (2011). "Algorithms for Hyper-Parameter Optimization." *NeurIPS 2011*. (Introduces TPE.)
- Springenberg, J. T., Klein, A., Falkner, S., & Hutter, F. (2016). "Bayesian Optimization with Robust Bayesian Neural Networks." *NeurIPS 2016*. (BOHAMIANN.)
- Shahriari, B., Swersky, K., Wang, Z., Adams, R. P., & de Freitas, N. (2016). "Taking the Human Out of the Loop: A Review of Bayesian Optimization." *Proceedings of the IEEE*. https://ieeexplore.ieee.org/document/7352306
- Optuna documentation — https://optuna.readthedocs.io
- BoTorch documentation — https://botorch.org ; Ax — https://ax.dev ; SMAC3 — https://automl.github.io/SMAC3 ; Hyperopt — http://hyperopt.github.io/hyperopt
- Library currency (Optuna, Hyperopt, BoTorch, Ax, SMAC3) and default-sampler behaviour verified via Perplexity (sonar), 2026-06-11.

## See Also

- [[search-optimisation-overview]] — Search & optimisation hub
- [[hyperparameter-tuning]] — The primary trading use case for BO
- [[optuna]] — The recommended BO framework for trading
- [[optimization-objectives]] — Choosing what to optimize
- [[walk-forward-analysis]] — The validation methodology that should wrap BO
- [[evolutionary-algorithms]] — Alternative when evaluations are cheap
- [[simulated-annealing]] — Alternative single-agent optimisation
- [[cross-validation-trading]] — The evaluation procedure BO wraps around
- [[xgboost-trading]] — Common model being tuned
- [[overfitting]] — The central risk when tuning with an efficient optimiser
- [[deflated-sharpe-ratio]] — Haircut for many-trial selection bias
- [[probability-of-backtest-overfitting]] — PBO diagnostic for tuned strategies
- [[artificial-intelligence]] — AI section hub
