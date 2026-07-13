---
title: "Swarm Intelligence"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Swarm Intelligence", "PSO", "Particle Swarm", "Ant Colony"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[search-optimisation-overview]]", "[[evolutionary-algorithms]]", "[[simulated-annealing]]", "[[artificial-intelligence]]"]
---

# Swarm Intelligence

**Swarm intelligence** algorithms optimise by simulating the collective behaviour of decentralised agents — flocks of birds, schools of fish, ant colonies. Each agent follows simple rules, but the swarm collectively discovers optimal solutions. In trading, swarm methods are used for portfolio optimisation, multi-objective parameter tuning, and feature selection.

## Key Algorithms

### Particle Swarm Optimisation (PSO)

Particles fly through the search space, influenced by their own best position and the swarm's global best:

```
For each particle i:
  velocity[i] = w * velocity[i]                      # inertia
              + c1 * rand() * (personal_best[i] - position[i])  # memory
              + c2 * rand() * (global_best - position[i])        # social
  position[i] = position[i] + velocity[i]
```

| Component | Meaning | Trading Analogy |
|-----------|---------|----------------|
| **Particle** | Candidate solution (e.g., portfolio weights) | A portfolio configuration |
| **Velocity** | Direction and speed of search | How fast we adjust weights |
| **Personal best** | Best solution this particle has found | Best weights this configuration tried |
| **Global best** | Best solution any particle has found | Best portfolio discovered by the swarm |
| **Inertia (w)** | Tendency to keep moving in current direction | Momentum in search |

### Ant Colony Optimisation (ACO)

Ants deposit pheromones on paths; better paths accumulate more pheromone, attracting more ants:

- Model the trading problem as a graph
- Ants traverse paths, deposit pheromone proportional to solution quality
- Good paths (high Sharpe, low drawdown) attract more ants over time
- Pheromone evaporates, preventing convergence on stale solutions

Best for: Combinatorial problems — feature selection (which indicators to include), trade scheduling (which orders to execute when).

### Artificial Bee Colony (ABC)

Three types of bees:
- **Employed bees**: Exploit known good solutions (intensification)
- **Onlooker bees**: Choose promising solutions to explore further
- **Scout bees**: Randomly explore new regions (diversification)

Balances exploitation of known good strategies with exploration of novel ones.

## Trading Applications

| Application | Algorithm | How |
|-------------|----------|-----|
| **Portfolio weight optimisation** | PSO | Particles = weight vectors; fitness = Sharpe ratio |
| **Feature selection** | ACO, binary PSO | Select which of 200+ indicators to include in model |
| **Multi-objective optimisation** | Multi-objective PSO (MOPSO) | Find Pareto frontier of return vs risk vs turnover |
| **Strategy parameter tuning** | PSO, ABC | Tune indicator periods, thresholds, stops |
| **Execution scheduling** | ACO | Route orders across time and venues |

## Swarm vs Evolutionary Algorithms

| Dimension | Swarm (PSO) | [[evolutionary-algorithms|Evolutionary]] (GA) |
|-----------|-------------|------|
| **Mechanism** | Agents move through continuous space | Population breeds via crossover + mutation |
| **Memory** | Each agent remembers its personal best | No individual memory |
| **Convergence** | Fast, risk of premature convergence | Slower, better diversity |
| **Discrete problems** | Less natural (needs adaptation) | Natural for binary/combinatorial |
| **Continuous problems** | Excellent | Good with real-valued encoding |
| **Hyperparameters** | Few (w, c1, c2) | More (crossover rate, mutation rate, selection method) |

## See Also

- [[search-optimisation-overview]] — Search & optimisation hub
- [[evolutionary-algorithms]] — Alternative population-based optimisation
- [[simulated-annealing]] — Single-agent global optimisation
- [[hyperparameter-tuning]] — Applied optimisation for ML
- [[artificial-intelligence]] — AI section hub
