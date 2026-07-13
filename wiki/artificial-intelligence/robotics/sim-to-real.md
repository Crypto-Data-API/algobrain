---
title: "Sim-to-Real Transfer"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["Sim-to-Real", "Simulation to Reality", "Digital Twin"]
domain: [ai-trading]
difficulty: advanced
related: ["[[robotics-overview]]", "[[autonomous-vehicles]]", "[[reinforcement-learning]]", "[[nvidia-ai]]", "[[backtesting-pitfalls]]", "[[gan-synthetic-data]]", "[[artificial-intelligence]]"]
---

# Sim-to-Real Transfer

**Sim-to-real** is the practice of training AI policies in simulation and deploying them on physical hardware. It solves a fundamental problem: training robots in the real world is slow, expensive, and dangerous (a robot learning to walk will fall thousands of times). Simulation is fast, cheap, and safe — but the gap between simulated and real physics (**the reality gap**) can cause policies trained in simulation to fail on hardware.

## How It Works

```
Simulation Environment (fast, cheap, safe)
  → Train RL agent on millions of episodes
  → Domain randomisation (vary physics, textures, lighting)
  → Policy transfer to real hardware
  → Fine-tune with real-world data (optional)
```

## Key Techniques

| Technique | How | Purpose |
|-----------|-----|---------|
| **Domain randomisation** | Randomly vary simulation parameters (friction, mass, lighting, textures) | Forces policy to be robust to real-world variation |
| **System identification** | Measure real-world physics precisely, calibrate simulation | Reduce the sim-real gap directly |
| **Progressive transfer** | Train in increasingly realistic simulations | Gradual bridging from simple to complex |
| **Real-world fine-tuning** | Adapt sim-trained policy with small amounts of real data | Close remaining gap |
| **Digital twins** | High-fidelity simulation matched to specific real environment | Factory/warehouse-specific deployment |

## Simulation Platforms

| Platform | Provider | Focus |
|----------|---------|-------|
| **Isaac Sim** | [[nvidia-ai|NVIDIA]] | Robot manipulation, navigation, Omniverse |
| **CARLA** | Open-source | [[autonomous-vehicles|Autonomous driving]] |
| **Gazebo** | Open Robotics | General-purpose robotics |
| **MuJoCo** | Google DeepMind | Physics simulation for RL |
| **Unity ML-Agents** | Unity | Game engine for diverse environments |
| **Unreal Engine** | Epic Games | Photorealistic simulation |

## The Trading Parallel: Backtesting

Sim-to-real in robotics is **exactly analogous** to [[backtesting-overview|backtesting]] in trading:

| Robotics Sim-to-Real | Trading Backtesting |
|----------------------|-------------------|
| Simulated physics ≠ real physics | Simulated market ≠ real market |
| The reality gap | [[backtesting-pitfalls|The backtest-to-live gap]] |
| Domain randomisation | Robustness testing across market regimes |
| Overfitting to simulation | [[overfitting-in-trading|Overfitting to historical data]] |
| Policy works in sim, fails on robot | Strategy works in backtest, fails live |
| Fine-tune on real-world data | Paper trading → small live allocation → scale up |
| Digital twin of specific factory | [[gan-synthetic-data|Synthetic data]] matching specific market conditions |

The lessons are identical: **the simulation is never the reality.** Robust transfer requires randomisation, progressive deployment, and continuous monitoring.

## Investment Angle

- **[[nvidia-ai|NVIDIA]]** dominates robotics simulation through Isaac Sim and Omniverse — every major robotics company uses NVIDIA's simulation stack
- Simulation compute demand grows with fleet size — more robots = more simulation hours for training and validation
- Digital twin companies (Ansys, Siemens, Dassault) provide industrial simulation for manufacturing robotics

## See Also

- [[robotics-overview]] — Broader robotics context
- [[autonomous-vehicles]] — AVs rely heavily on sim-to-real
- [[reinforcement-learning]] — The learning paradigm used in simulation
- [[nvidia-ai]] — Dominant simulation platform provider
- [[backtesting-pitfalls]] — The trading equivalent of the reality gap
- [[gan-synthetic-data]] — Synthetic data for augmenting training
- [[artificial-intelligence]] — AI section hub

## Sources

- Tobin et al. (2017) — "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World"
- OpenAI (2019) — "Solving Rubik's Cube with a Robot Hand" (domain randomisation at scale)
- NVIDIA Isaac Sim / Omniverse documentation; CARLA, Gazebo, MuJoCo, Unity ML-Agents project docs
- Standard references on the reality gap in robotics RL
