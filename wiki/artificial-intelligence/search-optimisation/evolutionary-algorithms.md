---
title: "Evolutionary Algorithms"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Evolutionary Algorithm", "Genetic Algorithm", "Genetic Programming", "GA", "GP", "CMA-ES", "NSGA-II"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[search-optimisation-overview]]", "[[swarm-intelligence]]", "[[simulated-annealing]]", "[[hyperparameter-tuning]]", "[[overfitting-in-trading]]", "[[backtesting-pitfalls]]", "[[artificial-intelligence]]"]
---

# Evolutionary Algorithms

**Evolutionary algorithms** (EAs) optimise by mimicking biological evolution — maintaining a population of candidate solutions that undergo selection, crossover (recombination), and mutation over generations. The fittest individuals (best-performing solutions) survive and reproduce, gradually improving the population. In trading, EAs discover strategies, optimise portfolios, tune parameters, and solve multi-objective problems where gradient-based methods fail.

## How They Work

```
1. INITIALISE random population of N candidate solutions
2. EVALUATE fitness of each candidate (backtest, objective function)
3. SELECT the fittest individuals (tournament selection, roulette wheel)
4. CROSSOVER: combine pairs of parents to create offspring
5. MUTATE: randomly perturb some offspring
6. REPLACE: new generation replaces old
7. REPEAT from step 2 until convergence or budget exhausted
```

## Key Variants

| Algorithm | Representation | Best For | Trading Application |
|-----------|---------------|---------|-------------------|
| **Genetic Algorithm (GA)** | Fixed-length binary or real-valued vectors | Parameter optimisation | Optimise indicator thresholds, weight vectors |
| **Genetic Programming (GP)** | Tree-structured programs / expressions | Strategy discovery | Evolve trading rules as expression trees |
| **CMA-ES** (Covariance Matrix Adaptation) | Real-valued vectors with learned covariance | Continuous optimisation, noisy landscapes | Portfolio weight optimisation, robust parameter tuning |
| **NSGA-II** (Non-dominated Sorting GA) | Any | Multi-objective optimisation | Pareto-optimal portfolios (maximise return AND minimise risk) |
| **Differential Evolution (DE)** | Real-valued vectors | Global optimisation, few hyperparameters | Strategy parameter search |

## Trading Applications

### Strategy Discovery (Genetic Programming)

GP evolves trading rules as expression trees:
```
Generation 1: IF (SMA(20) > SMA(50)) THEN BUY          [simple, weak]
Generation 50: IF (RSI(14) < 30 AND ADX(20) > 25 AND   [complex, evolved]
               Volume > SMA(Volume, 10) * 1.5) THEN BUY
```

Each generation, the best-performing rules (highest Sharpe on training data) breed and mutate. After hundreds of generations, the algorithm discovers non-obvious rule combinations.

**Critical warning**: GP-discovered strategies are extremely prone to [[overfitting-in-trading|overfitting]]. The algorithm is very good at finding patterns in historical noise. Rigorous [[cross-validation-trading|walk-forward validation]] and [[backtesting-pitfalls|out-of-sample testing]] are mandatory.

### Portfolio Optimisation (CMA-ES)

Optimise portfolio weights where the objective function is noisy (simulated returns) and the landscape is non-convex:
- Objective: Maximise Sharpe ratio
- Variables: Weights for N assets
- CMA-ES adapts its search distribution based on successful weight combinations
- More robust than gradient descent for noisy, non-convex financial objectives

### Multi-Objective Optimisation (NSGA-II)

Trading involves competing objectives. NSGA-II finds the **Pareto frontier** — the set of solutions where no objective can be improved without worsening another:

```
Objective 1: Maximise annual return
Objective 2: Minimise maximum drawdown
Objective 3: Minimise turnover (transaction costs)

NSGA-II returns: 50 Pareto-optimal portfolios along the frontier
Trader chooses: The portfolio matching their risk/return preference
```

### Parameter Tuning

Optimise strategy parameters (indicator periods, thresholds, stop-loss levels):
- GA/DE search over parameter combinations
- Fitness = backtest Sharpe ratio (or other metric)
- More efficient than grid search for high-dimensional parameter spaces
- But: same [[hyperparameter-tuning|overfitting]] risks as any parameter optimisation

## Overfitting Risk

Evolutionary algorithms are **overfitting machines** in trading:
- They're designed to maximise a fitness function — if that function is an in-sample backtest, they will find parameters that exploit historical noise
- GP is especially dangerous: it can evolve arbitrarily complex rules that perfectly fit past data
- The more generations and the larger the population, the higher the overfitting risk

**Mitigation**:
1. Fitness function uses [[cross-validation-trading|walk-forward validation]], not single backtest
2. Penalise complexity (shorter GP trees, fewer parameters)
3. Test final solutions on truly out-of-sample data
4. Ensemble multiple evolved solutions rather than picking the single best

## See Also

- [[search-optimisation-overview]] — Search & optimisation hub
- [[swarm-intelligence]] — Alternative population-based optimisation
- [[simulated-annealing]] — Alternative global optimisation
- [[bayesian-optimisation]] — Efficient optimisation for expensive evaluations
- [[hyperparameter-tuning]] — Optimisation applied to ML models
- [[overfitting-in-trading]] — The primary risk of evolutionary strategy search
- [[backtesting-pitfalls]] — Validating evolved strategies
- [[artificial-intelligence]] — AI section hub

## Sources

- Holland, J. (1975) — *Adaptation in Natural and Artificial Systems* (genetic algorithms)
- Koza, J. (1992) — *Genetic Programming* (evolving programs/expressions)
- Hansen, N. — CMA-ES reference; Deb et al. (2002) — NSGA-II; Storn & Price (1997) — Differential Evolution
- López de Prado, M. (2018) — *Advances in Financial Machine Learning* (on overfitting risk in automated strategy search)
