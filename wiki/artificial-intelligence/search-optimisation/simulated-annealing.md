---
title: "Simulated Annealing"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Simulated Annealing", "SA", "Threshold Accepting"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[search-optimisation-overview]]", "[[evolutionary-algorithms]]", "[[swarm-intelligence]]", "[[bayesian-optimisation]]", "[[artificial-intelligence]]"]
---

# Simulated Annealing

**Simulated annealing** (SA) is an optimisation algorithm inspired by the metallurgical process of heating and slowly cooling metal to reduce defects. It searches by randomly perturbing the current solution — accepting improvements always, and accepting *worse* solutions with decreasing probability as the "temperature" cools. This ability to temporarily accept worse solutions lets SA escape local optima that trap greedy algorithms.

## How It Works

```
1. Start with random solution S, high temperature T
2. Generate neighbour S' by small random perturbation
3. If S' is better: accept it (move to S')
4. If S' is worse: accept it with probability exp(-(cost(S')-cost(S)) / T)
5. Reduce temperature: T = T * cooling_rate
6. Repeat from step 2 until T ≈ 0 or budget exhausted
```

| Phase | Temperature | Behaviour | Trading Analogy |
|-------|-----------|-----------|----------------|
| **Early** (hot) | High | Accepts many worse solutions — explores broadly | Trying wildly different strategies, no commitment |
| **Middle** (warm) | Medium | Occasionally accepts worse — balanced exploration | Refining promising strategies, still open to pivots |
| **Late** (cool) | Low | Rarely accepts worse — exploits best found | Fine-tuning the best strategy, minor parameter adjustments |

## Trading Applications

### Portfolio Optimisation
When the objective landscape is non-convex (fat tails, regime switches, non-linear constraints):
- SA escapes local optima that gradient descent gets stuck in
- Works well with integer constraints (number of positions must be ≤ 20)
- Handles non-standard objectives (minimise CVaR, maximise Omega ratio)

### Execution Scheduling
Optimise the timing and sizing of a large order's child slices:
- Discrete time slots × venue choices = combinatorial problem
- SA explores the schedule space, accepting temporarily worse splits to find globally better ones

### Strategy Discovery
Perturb an existing strategy's rules and parameters:
- Start with a reasonable base strategy
- SA explores neighbourhoods: slightly different indicator periods, different thresholds, alternative exit rules
- Cooling schedule prevents over-exploration (too random) and under-exploration (stuck near starting point)

## SA vs Other Methods

| Dimension | Simulated Annealing | [[evolutionary-algorithms|GA/EA]] | [[bayesian-optimisation|Bayesian Opt]] |
|-----------|-------------------|-------|-------------|
| **Population** | Single solution | Population | Model of objective |
| **Parallelism** | Sequential (but can restart) | Naturally parallel | Sequential |
| **Discrete problems** | Excellent | Good | Poor |
| **Continuous problems** | Good | Good | Excellent |
| **Noisy objectives** | Robust | Robust | Handles with GP uncertainty |
| **Computation** | Low per iteration | Higher (population) | Higher (model fitting) |
| **Guarantee** | Convergence to global optimum (in theory, infinite time) | No formal guarantee | No formal guarantee |

## Cooling Schedules

| Schedule | Formula | Behaviour |
|----------|---------|-----------|
| **Geometric** | T = T₀ × α^k (α ≈ 0.95-0.99) | Most common, steady cooling |
| **Linear** | T = T₀ - k × ΔT | Simple, may cool too fast |
| **Logarithmic** | T = T₀ / log(1 + k) | Very slow cooling, theoretically optimal |
| **Adaptive** | Adjust α based on acceptance rate | Self-tuning, practical for trading |

## See Also

- [[search-optimisation-overview]] — Search & optimisation hub
- [[evolutionary-algorithms]] — Population-based alternative
- [[swarm-intelligence]] — Multi-agent alternative
- [[bayesian-optimisation]] — Model-based alternative
- [[artificial-intelligence]] — AI section hub
