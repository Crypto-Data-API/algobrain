---
title: "Reinforcement Learning"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, machine-learning, education]
aliases: ["Reinforcement Learning", "RL"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[supervised-learning]]", "[[unsupervised-learning]]", "[[reinforcement-learning-trading]]", "[[ai-trading-agents]]", "[[ai-market-making]]", "[[ai-agent-strategies]]", "[[google-deepmind]]", "[[types-of-ai]]", "[[artificial-intelligence]]"]
---

# Reinforcement Learning

**Reinforcement learning** (RL) trains an agent to make sequential decisions by rewarding desired outcomes and penalizing undesired ones. Unlike [[supervised-learning|supervised learning]] (which needs labeled data) or [[unsupervised-learning|unsupervised learning]] (which finds patterns), RL learns optimal behavior through **trial and error in an environment**. It is the paradigm most naturally suited to trading — where an agent must make a sequence of decisions (buy, hold, sell) to maximize cumulative profit.

## How It Works

The RL framework has five components:

| Component | Trading Analogy |
|-----------|----------------|
| **Agent** | The trading algorithm |
| **Environment** | The market (prices, order book, news) |
| **State** | Current portfolio, positions, market conditions |
| **Action** | Buy, sell, hold, adjust position size |
| **Reward** | PnL, Sharpe ratio, risk-adjusted return |

The learning loop:
1. Agent observes the current **state** (market conditions)
2. Agent takes an **action** (places a trade)
3. Environment returns a **reward** (profit or loss) and new **state**
4. Agent updates its **policy** (decision rules) to maximize cumulative reward
5. Repeat millions of times across simulated market episodes

## Key Algorithms

| Algorithm | Type | Best For |
|-----------|------|---------|
| **DQN** (Deep Q-Network) | Value-based | Discrete actions (buy/sell/hold) |
| **PPO** (Proximal Policy Optimization) | Policy gradient | Continuous actions (position sizing) |
| **SAC** (Soft Actor-Critic) | Actor-critic | Robust exploration, continuous control |
| **A3C** (Asynchronous Advantage Actor-Critic) | Actor-critic | Parallelized training |
| **TD3** (Twin Delayed DDPG) | Actor-critic | Stable training for continuous actions |

See [[reinforcement-learning-trading]] for applied implementations with these algorithms.

## Trading Applications

| Application | RL Approach | What the Agent Learns |
|-------------|-----------|---------------------|
| **Optimal execution** | PPO/SAC | Split large orders to minimize market impact |
| **[[ai-market-making|Market making]]** | DQN/SAC | Dynamic bid-ask spreads that maximize profit while managing inventory |
| **Portfolio allocation** | PPO | Rebalance weights based on predicted regime |
| **Position sizing** | SAC | How much capital to allocate per trade |
| **Order routing** | DQN | Which venue/exchange to route orders to |

## Why RL Is Hard for Trading

RL's theoretical fit for trading is perfect — sequential decisions, delayed rewards, uncertain environments. In practice, it's the hardest ML paradigm to make work:

| Challenge | Why It's Hard |
|-----------|-------------|
| **Non-stationary environment** | Markets change regime; the "rules" of the game shift |
| **Sparse rewards** | Many actions have no immediate measurable PnL impact |
| **Simulation-reality gap** | RL agents trained on backtests may fail live due to slippage, latency, and market impact not captured in simulation |
| **Sample inefficiency** | Requires millions of training episodes — limited by historical data length |
| **Reward hacking** | Agent finds degenerate strategies that maximize the reward function but wouldn't work live (e.g., trading at close to capture close-to-close returns) |
| **Catastrophic risk** | An RL agent without constraints can take unbounded risk to maximize reward |

## RL vs Supervised Learning for Trading

| Dimension | Supervised Learning | Reinforcement Learning |
|-----------|-------------------|----------------------|
| **Input** | Labeled historical data | Simulated environment |
| **Output** | Prediction (price up/down) | Action (buy/sell/size) |
| **Optimization** | Minimize prediction error | Maximize cumulative reward |
| **Decision making** | Separate step (human decides) | Integrated (agent decides) |
| **Risk management** | External to model | Can be learned, but dangerous |
| **Maturity for trading** | Production-ready | Mostly experimental |

## The AlphaGo Connection

[[google-deepmind|DeepMind's]] AlphaGo (2016) demonstrated that RL + deep learning could master complex strategic games at superhuman level. Trading is sometimes compared to Go — sequential decisions with incomplete information. However, Go has fixed rules and a clear win condition. Markets have shifting rules, adversarial participants, and ambiguous objectives, making them a harder RL problem than Go.

## See Also

- [[reinforcement-learning-trading]] — Applied RL algorithms for trading (DQN, PPO, SAC implementations)
- [[supervised-learning]] — Prediction-based alternative
- [[unsupervised-learning]] — Pattern-discovery alternative
- [[ai-trading-agents]] — Agents that may use RL for decision-making
- [[ai-market-making]] — RL for market making
- [[ai-agent-strategies]] — Strategy categories including RL-based approaches
- [[google-deepmind]] — AlphaGo and RL research
- [[types-of-ai]] — Where RL fits in the taxonomy
- [[machine-learning-vs-deep-learning]] — The broader hierarchy
- [[artificial-intelligence]] — AI section hub
