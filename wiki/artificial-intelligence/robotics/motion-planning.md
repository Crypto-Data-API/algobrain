---
title: "Motion Planning"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Motion Planning", "Path Planning", "Trajectory Planning"]
domain: [ai-trading]
difficulty: advanced
related: ["[[robotics-overview]]", "[[autonomous-vehicles]]", "[[graph-search-algorithms]]", "[[reinforcement-learning]]", "[[ai-planning]]", "[[constraint-optimisation]]", "[[artificial-intelligence]]"]
---

# Motion Planning

**Motion planning** generates a collision-free path or trajectory for a robot to move from one configuration to another. It is the core intelligence of any mobile robot — [[autonomous-vehicles|self-driving cars]], warehouse robots, drones, and [[humanoid-robots|humanoid robots]]. Motion planning sits at the intersection of [[graph-search-algorithms|search]], [[constraint-optimisation|optimisation]], and increasingly [[reinforcement-learning|learning]].

## The Planning Hierarchy

| Level | Question | Time Horizon | Method |
|-------|---------|-------------|--------|
| **Route planning** | Which roads/paths to take? | Minutes-hours | [[graph-search-algorithms|A*]], Dijkstra on road graph |
| **Behavioural planning** | Lane change? Yield? Overtake? | Seconds | State machines, decision trees, RL |
| **Trajectory planning** | Exact path and speed profile | 1-5 seconds | Optimisation, sampling, splines |
| **Control** | Steering angle, throttle, brake | Milliseconds | PID, MPC (Model Predictive Control) |

## Classical Approaches

| Algorithm | Type | How It Works | Use Case |
|-----------|------|-------------|---------|
| **RRT** (Rapidly-exploring Random Trees) | Sampling-based | Randomly samples points, grows a tree toward them | Complex spaces, high dimensions |
| **RRT*** | Sampling + optimisation | RRT with asymptotic optimality (rewires tree) | Near-optimal paths in complex environments |
| **PRM** (Probabilistic Roadmap) | Sampling-based | Pre-builds a roadmap of free space, searches it | Multi-query scenarios (warehouse robots) |
| **Lattice planner** | Graph-based | Pre-computes motion primitives, searches discrete graph | Autonomous driving (structured roads) |
| **Optimisation-based** | [[constraint-optimisation|Optimisation]] | Minimise cost (time, jerk, distance) subject to constraints | Smooth, comfortable trajectories |

## Learning-Based Planning

[[reinforcement-learning|RL]] and [[foundation-models|neural networks]] are increasingly used for planning:

| Approach | How | Advantage | Challenge |
|----------|-----|-----------|-----------|
| **End-to-end learning** | Neural net maps sensor input directly to trajectory | Handles complex, learned behaviours | Black box, hard to verify safety |
| **RL for behaviour** | RL agent decides high-level actions (lane change, yield) | Adapts to other agents' behaviour | [[sim-to-real|Sim-to-real]] gap |
| **Diffusion planning** | [[diffusion-models|Diffusion model]] generates trajectory distributions | Multi-modal (multiple plausible paths) | Computational cost |
| **LLM-assisted planning** | [[foundation-models|LLM]] reasons about complex scenarios | Handles novel situations via common sense | Latency, reliability |

Tesla's Full Self-Driving (FSD) v12+ uses an **end-to-end neural network** that maps camera inputs directly to vehicle controls — eliminating most hand-coded planning rules. This is the most aggressive bet on learning-based planning in the industry.

## The Trading Parallel

Motion planning and trading execution share deep structural similarities:

| Motion Planning | Trading Execution |
|----------------|-------------------|
| Navigate through physical space | Navigate through order book / market microstructure |
| Avoid obstacles | Avoid adverse selection, market impact |
| Minimise time/energy | Minimise cost, slippage |
| Dynamic obstacles (other cars) | Dynamic order book (other traders) |
| Predict other agents' behaviour | Predict institutional flow |
| [[constraint-optimisation|Constraints]]: road boundaries, physics | Constraints: position limits, lot sizes, venue rules |

This is not a metaphor — the same algorithmic toolbox ([[graph-search-algorithms|A*]], [[constraint-optimisation|optimisation]], [[reinforcement-learning|RL]]) solves both problems.

## See Also

- [[robotics-overview]] — Broader robotics context
- [[autonomous-vehicles]] — Primary application of motion planning
- [[graph-search-algorithms]] — Search algorithms for route planning
- [[constraint-optimisation]] — Trajectory optimisation
- [[reinforcement-learning]] — Learning-based planning
- [[ai-planning]] — Symbolic planning for task-level decisions
- [[sim-to-real]] — Where motion planning is trained
- [[artificial-intelligence]] — AI section hub

## Sources

- LaValle, S. — *Planning Algorithms* (Cambridge University Press, 2006) — RRT, PRM, sampling-based planning
- Karaman & Frazzoli (2011) — "Sampling-based Algorithms for Optimal Motion Planning" (RRT*)
- Tesla — FSD v12+ end-to-end neural-network planning architecture (AI Day / release notes)
- Standard references on Model Predictive Control (MPC) and A*/Dijkstra graph search
