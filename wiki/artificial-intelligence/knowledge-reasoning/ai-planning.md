---
title: "AI Planning"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["AI Planning", "Automated Planning", "Goal-Directed AI"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[knowledge-reasoning-overview]]", "[[logic-based-ai]]", "[[ai-trading-agents]]", "[[reinforcement-learning]]", "[[ai-agent-strategies]]", "[[artificial-intelligence]]"]
---

# AI Planning

**AI planning** is the process of generating a sequence of actions to achieve a goal from a given starting state. Unlike [[reinforcement-learning|reinforcement learning]] (which learns through trial and error), planning systems reason about actions and their consequences **before execution** — using world models to simulate outcomes and select optimal action sequences.

## Planning in Trading

Trading is inherently a planning problem: given current market conditions and portfolio state, what sequence of actions (trades, hedges, rebalances) achieves the goal (target return, risk reduction, rebalancing)?

| Planning Problem | Start State | Goal | Actions |
|-----------------|-------------|------|---------|
| **Portfolio rebalancing** | Current weights deviate from target | Weights within tolerance | Buy/sell specific amounts |
| **Multi-leg execution** | Need to fill 100K shares with minimal impact | Complete fill at VWAP | Split across venues, time slices |
| **Options strategy construction** | Directional view + risk budget | Target payoff profile | Select strikes, expirations, quantities |
| **Tax-loss harvesting** | Unrealized losses in portfolio | Harvest losses by year-end | Sell losers, buy substitutes, avoid wash sales |
| **Liquidation** | Need to exit large position | Fully closed with minimal slippage | Staged selling across time and venues |

## Planning Approaches

### Classical Planning
Define the world with states, actions, and preconditions. Search for an action sequence reaching the goal state.

```
State: {portfolio: [100 AAPL, 50 GOOG], cash: $10K, target: [80 AAPL, 70 GOOG]}
Actions: buy(stock, qty), sell(stock, qty)
Preconditions: sell requires position >= qty; buy requires cash >= price * qty
Goal: portfolio matches target within 2% tolerance
Plan: sell(AAPL, 20) → buy(GOOG, 20)
```

### Hierarchical Task Networks (HTN)
Decompose complex tasks into subtasks recursively:

```
Rebalance Portfolio
├── Compute target weights
├── For each overweight position:
│   └── Sell excess
│       ├── Check liquidity
│       ├── Choose execution venue
│       └── Submit orders
├── For each underweight position:
│   └── Buy deficit (using proceeds from sells)
└── Verify final weights within tolerance
```

### Planning Under Uncertainty
Markets are stochastic — plans must handle uncertainty:

- **Contingency planning**: "If price drops below $X during execution, switch to passive strategy"
- **Probabilistic planning**: Assign probabilities to outcomes, optimize expected utility
- **Replanning**: Continuously update the plan as new information arrives

### LLM-Assisted Planning
[[foundation-models|LLMs]] bring natural language reasoning to planning:

```
User: "I need to exit my 50,000 share position in AAPL over the next 3 days 
       without moving the price more than 0.5%"
LLM: Generates a structured execution plan with time slices, venue allocation, 
     and contingency rules
```

This is how [[ai-trading-agents|AI trading agents]] approach multi-step problems — using LLM reasoning for high-level planning and deterministic systems for constraint enforcement.

## Planning vs Reinforcement Learning

| Dimension | Planning | [[reinforcement-learning|RL]] |
|-----------|---------|-----|
| **World model** | Explicit (knows the rules) | Learned (discovers rules by interaction) |
| **Computation** | Before execution (think first) | During training (trial and error) |
| **Optimality** | Provably optimal for known models | Approximately optimal for learned models |
| **Novel situations** | Handles if model is accurate | Struggles outside training distribution |
| **Trading use** | Execution, rebalancing, tax | Market making, position sizing |

Modern systems often combine both: plan at the high level (what to trade), use RL at the low level (how to execute).

## See Also

- [[knowledge-reasoning-overview]] — KR&R hub
- [[logic-based-ai]] — Logic underlying planning rules
- [[ai-trading-agents]] — Agents that use planning for multi-step execution
- [[reinforcement-learning]] — Alternative approach to sequential decisions
- [[ai-agent-strategies]] — Strategy categories using planning
- [[artificial-intelligence]] — AI section hub

## Sources

- Russell & Norvig, "Artificial Intelligence: A Modern Approach" — standard reference for classical planning, HTN, and planning under uncertainty.
- Almgren & Chriss, "Optimal Execution of Portfolio Transactions" (2000) — the canonical framework for the multi-leg / liquidation execution-planning problems described here.
- General agentic-AI literature on LLM-assisted planning and tool-using trading agents (mid-2026); see [[ai-trading-agents]].
