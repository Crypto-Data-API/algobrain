---
title: "Search & Optimisation Algorithms"
type: overview
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Search Algorithms", "Optimisation", "Optimization"]
related: ["[[graph-search-algorithms]]", "[[evolutionary-algorithms]]", "[[swarm-intelligence]]", "[[simulated-annealing]]", "[[bayesian-optimisation]]", "[[constraint-optimisation]]", "[[hyperparameter-tuning]]", "[[ai-planning]]", "[[reinforcement-learning]]", "[[artificial-intelligence]]"]
---

# Search & Optimisation Algorithms

**Search and optimisation** algorithms find the best solution from a large space of possibilities. They are foundational to AI — before machine learning, AI *was* search. In trading, these algorithms solve portfolio optimisation, parameter tuning, execution scheduling, strategy discovery, and any problem where you need to find the best configuration among millions of candidates.

## The Optimisation Landscape

Every trading optimisation problem has:
- **Search space**: All possible solutions (e.g., all possible portfolio weight combinations)
- **Objective function**: What to maximise or minimise (Sharpe ratio, drawdown, tracking error)
- **Constraints**: Hard limits the solution must satisfy (position limits, turnover caps, sector bounds)

The challenge: search spaces are enormous (a 500-stock portfolio has effectively infinite weight combinations) and objective functions are noisy, non-convex, and regime-dependent.

## Algorithm Categories

| Category | Approach | Trading Strength | Pages |
|----------|---------|-----------------|-------|
| **[[graph-search-algorithms|Graph Search]]** | Systematic exploration of state spaces | Execution routing, order book navigation | A*, BFS, Dijkstra |
| **[[evolutionary-algorithms]]** | Population-based, survival of the fittest | Strategy discovery, portfolio optimisation | Genetic algorithms, GP, CMA-ES |
| **[[swarm-intelligence]]** | Collective behaviour of simple agents | Multi-objective optimisation, parameter tuning | PSO, ant colony |
| **[[simulated-annealing]]** | Gradually cooling random search | Escaping local optima in rugged landscapes | SA, threshold accepting |
| **[[bayesian-optimisation]]** | Model the objective, sample intelligently | [[hyperparameter-tuning|Hyperparameter tuning]], expensive evaluations | GP-based BO, TPE |
| **[[constraint-optimisation]]** | Optimise subject to hard constraints | Portfolio construction, margin optimisation | LP, QP, MILP, convex |

## When to Use What

| Problem | Best Approach | Why |
|---------|-------------|-----|
| **Portfolio weight optimisation** | [[constraint-optimisation|Convex optimisation]] (QP) | Quadratic objective + linear constraints = solved efficiently |
| **[[hyperparameter-tuning|Hyperparameter tuning]]** | [[bayesian-optimisation]] | Each evaluation is expensive (full backtest); need to minimise evaluations |
| **Strategy discovery** | [[evolutionary-algorithms|Genetic programming]] | Huge search space, need to explore creative solutions |
| **Order routing** | [[graph-search-algorithms|A* / Dijkstra]] | Route through venue/time graph to minimise cost |
| **Multi-objective** (Sharpe AND drawdown AND turnover) | [[evolutionary-algorithms|NSGA-II]] or [[swarm-intelligence|PSO]] | Multiple competing objectives, need Pareto frontier |
| **Scheduling** (execution over time) | [[constraint-optimisation|MILP]] or [[simulated-annealing]] | Discrete choices + timing constraints |

## Optimisation Pitfalls in Trading

| Pitfall | Description | Mitigation |
|---------|------------|-----------|
| **Overfitting** | Optimiser finds parameters that work on historical data but not forward | [[cross-validation-trading|Walk-forward validation]], regularisation |
| **Data snooping** | Running many optimisations on same data inflates apparent performance | Multiple testing correction (Bonferroni, FDR) |
| **Local optima** | Gradient-based methods get stuck in suboptimal solutions | Use global methods ([[evolutionary-algorithms|EA]], [[simulated-annealing|SA]]) or restart strategies |
| **Non-stationarity** | Optimal parameters shift as market regime changes | Re-optimise periodically, use regime-aware objectives |
| **Overly complex objective** | Optimising Sharpe ignores tail risk; optimising everything is intractable | Choose 1-2 primary objectives, constrain the rest |

## See Also

- [[graph-search-algorithms]] — A*, BFS, Dijkstra for state-space search
- [[evolutionary-algorithms]] — Genetic algorithms, genetic programming
- [[swarm-intelligence]] — Particle swarm, ant colony optimisation
- [[simulated-annealing]] — Temperature-based random search
- [[bayesian-optimisation]] — Model-based efficient search
- [[constraint-optimisation]] — LP, QP, MILP for constrained problems
- [[hyperparameter-tuning]] — Optimisation applied to ML model settings
- [[ai-planning]] — Search applied to action sequences
- [[reinforcement-learning]] — Optimisation through environment interaction
- [[artificial-intelligence]] — AI section hub
