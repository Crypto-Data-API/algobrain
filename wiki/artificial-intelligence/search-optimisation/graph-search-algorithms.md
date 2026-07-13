---
title: "Graph Search Algorithms"
type: concept
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [ai-trading, education]
aliases: ["A*", "A-Star", "Dijkstra", "BFS", "DFS", "Graph Search"]
domain: [ai-trading]
difficulty: intermediate
related: ["[[search-optimisation-overview]]", "[[ai-planning]]", "[[knowledge-graphs-finance]]", "[[artificial-intelligence]]"]
---

# Graph Search Algorithms

**Graph search algorithms** systematically explore nodes and edges in a graph to find optimal paths or solutions. They are the classical AI algorithms — A*, Dijkstra, BFS, DFS — that power shortest-path problems, state-space search, and [[ai-planning|planning]]. In trading, they apply to order routing, execution venue selection, and navigating [[knowledge-graphs-finance|financial knowledge graphs]].

## Core Algorithms

| Algorithm | Strategy | Guarantee | Trading Use |
|-----------|---------|-----------|-------------|
| **BFS** (Breadth-First Search) | Explore all neighbors before going deeper | Finds shortest path (unweighted) | Enumerate all 2-hop corporate connections |
| **DFS** (Depth-First Search) | Explore as deep as possible first | Finds *a* path (not necessarily optimal) | Trace ownership chains through corporate hierarchies |
| **Dijkstra's** | Expand lowest-cost node first | Optimal shortest path (non-negative weights) | Cheapest execution route across venues |
| **A*** | Dijkstra + heuristic estimate of remaining cost | Optimal with admissible heuristic | Smart order routing with estimated fill probability |
| **Bellman-Ford** | Iterative relaxation of all edges | Handles negative weights | Detect [[arbitrage]] cycles (negative-cost cycles = risk-free profit) |

## Trading Applications

### Order Routing (A* / Dijkstra)

Model execution venues as a graph:
- **Nodes**: Exchanges, dark pools, internal crossing engines
- **Edges**: Cost to route between them (fees, latency, market impact)
- **Goal**: Find the lowest-cost path to fill an order

```
Start: 10,000 shares to buy
  ├── Binance (fee: 0.1%, liquidity: 8K) ──→ Partial fill
  ├── Coinbase (fee: 0.2%, liquidity: 5K) ──→ Partial fill  
  └── Hyperliquid (fee: 0.02%, liquidity: 3K) ──→ Partial fill
A* finds: Fill 8K on Binance + 2K on Hyperliquid = lowest total cost
```

### Arbitrage Detection (Bellman-Ford)

Currency/crypto [[arbitrage]] is a negative-cycle detection problem:
```
BTC → ETH → USDT → BTC
If the product of exchange rates > 1.0, there's a risk-free profit cycle.
Bellman-Ford on the log-transformed graph detects negative cycles = arbitrage.
```

This is how triangular arbitrage bots work on crypto exchanges.

### Knowledge Graph Traversal

Navigate [[knowledge-graphs-finance|financial knowledge graphs]] to answer relational queries:
- "What companies are within 2 hops of this sanctioned entity?" → BFS with depth limit
- "What's the shortest ownership chain from Company A to Person B?" → Dijkstra on ownership graph
- "Find all supply chain paths from TSMC to Apple" → DFS with path recording

### State-Space Search for Planning

[[ai-planning|Planning]] problems (portfolio rebalancing, execution scheduling) can be modeled as graph search:
- **Nodes**: Portfolio states
- **Edges**: Trades that transition between states
- **Goal**: Reach target allocation state with minimum cost
- A* searches the state space with a heuristic estimating remaining rebalancing cost

## A* in Detail

A* is the most important graph search algorithm for trading because it balances **optimality** with **efficiency**:

```
f(n) = g(n) + h(n)
```

| Component | Meaning | Trading Interpretation |
|-----------|---------|----------------------|
| **g(n)** | Actual cost to reach node n | Execution cost so far |
| **h(n)** | Estimated cost from n to goal | Estimated remaining fill cost |
| **f(n)** | Total estimated cost through n | Expected total execution cost |

A* always expands the node with lowest f(n), guaranteeing the optimal solution if h(n) never overestimates (admissible heuristic).

## See Also

- [[search-optimisation-overview]] — Search & optimisation hub
- [[ai-planning]] — Planning as graph search
- [[knowledge-graphs-finance]] — Graphs these algorithms traverse
- [[arbitrage]] — Arbitrage detection via negative cycles
- [[artificial-intelligence]] — AI section hub
