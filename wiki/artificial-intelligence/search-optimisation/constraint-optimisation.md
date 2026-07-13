---
title: "Constraint Optimisation"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Constraint Optimisation", "Linear Programming", "Quadratic Programming", "Convex Optimisation", "LP", "QP", "MILP"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[search-optimisation-overview]]", "[[ai-planning]]", "[[expert-systems]]", "[[knowledge-reasoning-overview]]", "[[artificial-intelligence]]"]
---

# Constraint Optimisation

**Constraint optimisation** finds the best solution to an objective function subject to hard constraints that must be satisfied. It is the mathematical backbone of portfolio construction, margin calculation, and execution optimisation — any trading problem where the answer must respect rules (position limits, budget constraints, regulatory requirements).

## Problem Types

| Type | Objective | Constraints | Trading Use | Solver |
|------|----------|------------|-------------|--------|
| **LP** (Linear Programming) | Linear | Linear equalities/inequalities | Transaction cost minimisation, simple portfolio allocation | Simplex, interior point |
| **QP** (Quadratic Programming) | Quadratic | Linear | Mean-variance portfolio optimisation (Markowitz) | OSQP, Gurobi |
| **SOCP** (Second-Order Cone) | Conic | Conic | Portfolio optimisation with tracking error | MOSEK, ECOS |
| **MILP** (Mixed-Integer Linear) | Linear | Linear + some variables must be integers | Lot-size constrained trading, cardinality constraints ("hold at most 20 stocks") | Gurobi, CPLEX |
| **Convex** (general) | Convex | Convex | Most well-behaved portfolio problems | CVXPY (auto-detects) |

## The Markowitz Portfolio Problem (QP)

The foundational constrained optimisation in trading:

```
Minimise: w^T Σ w           (portfolio variance)
Subject to: w^T μ ≥ r_target  (minimum expected return)
           Σ w_i = 1          (weights sum to 1)
           w_i ≥ 0            (no short selling, optional)
           w_i ≤ 0.05         (max 5% in any single name)
```

This is a **quadratic program** — solvable in milliseconds for hundreds of assets.

## Trading Applications

| Application | Problem Type | Objective | Key Constraints |
|-------------|------------|-----------|----------------|
| **Mean-variance optimisation** | QP | Min variance for target return | Budget, position limits, sector limits |
| **Risk parity** | Convex | Equal risk contribution per asset | Budget, long-only |
| **Tracking error minimisation** | QP | Min deviation from benchmark | Turnover limit, tracking error bound |
| **Tax-loss harvesting** | MILP | Max harvested losses | Wash sale rules, position constraints, integer lots |
| **Execution scheduling** | MILP | Min market impact over time | Volume limits per interval, completion deadline |
| **Margin optimisation** | LP | Min margin posted | Clearing house margin rules |
| **Rebalancing** | QP | Min turnover to reach target | Target weights, turnover budget |

## Tools

| Library | Language | Strengths |
|---------|---------|-----------|
| **CVXPY** | Python | High-level modelling, auto-selects solver, academic standard |
| **Gurobi** | Python/C++ | Fastest commercial solver, handles MILP |
| **CPLEX** (IBM) | Python/C++ | Industry standard for large-scale problems |
| **MOSEK** | Python/C++ | Excellent for conic and SDP problems |
| **scipy.optimize** | Python | Basic LP/QP, built into scipy |
| **OR-Tools** (Google) | Python/C++ | Constraint programming, scheduling |

## Why Not Use ML Instead?

| | Constraint Optimisation | [[supervised-learning|ML]] |
|---|----------------------|-----|
| **Guarantees** | Provably optimal solution | Approximate, no guarantees |
| **Constraints** | Enforced exactly | Must be learned or post-hoc checked |
| **Interpretability** | Complete — see objective + constraints | Black box |
| **Handles new objectives** | Change the objective function | Retrain the model |
| **Requires data** | No — just objective + constraints | Yes — training data |
| **Handles uncertainty** | Robust optimisation variants | Naturally handles noise |

For portfolio construction, constraint optimisation is almost always the right tool. ML is better for *predicting inputs* (expected returns, covariance) that feed into the optimisation.

## See Also

- [[search-optimisation-overview]] — Search & optimisation hub
- [[ai-planning]] — Planning as constrained search
- [[expert-systems]] — Rules as constraints
- [[knowledge-reasoning-overview]] — KR&R hub
- [[portfolio-construction]] — Where QP is applied
- [[artificial-intelligence]] — AI section hub

## Sources

- Markowitz, H. (1952) — "Portfolio Selection" (the foundational mean-variance QP)
- Boyd & Vandenberghe — *Convex Optimization* (Cambridge University Press, 2004)
- CVXPY, Gurobi, MOSEK, CPLEX, and Google OR-Tools solver documentation
