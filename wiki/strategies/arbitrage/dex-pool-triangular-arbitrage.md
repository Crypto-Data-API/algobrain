---
title: "DEX Pool Triangular Arbitrage"
type: strategy
created: 2026-04-25
updated: 2026-07-19
status: good
tags: [arbitrage, defi, crypto, ethereum, algorithmic, market-microstructure]
aliases: ["Cyclic AMM Arbitrage", "On-Chain Triangle Arb", "Atomic Triangle Arbitrage"]
related: ["[[mev-strategies]]", "[[flash-loan-arbitrage]]", "[[triangular-arbitrage]]", "[[liquidation-cascade-arbitrage]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [latency, structural, analytical]
edge_mechanism: "AMM constant-product pools (Uniswap, Curve, Balancer) reprice at different speeds across pools. After a large external trade or oracle update, cross-pool implied rates form an exploitable cycle that closes only when an arbitrageur or the next price-update transaction lands."
data_required: [pool-reserves, mempool-txs, gas-price-feed, dex-router-quotes]
min_capital_usd: 10000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 2.5
expected_max_drawdown: 0.2
breakeven_cost_bps: 5
decay_evidence: "Eigenphi reports cyclic-arb extracted MEV declined ~40% from 2022 peak as searcher competition intensified and Uniswap v3 concentrated liquidity reduced cross-pool dislocations."
---

# DEX Pool Triangular Arbitrage

Atomic on-chain triangular arbitrage executed across Automated Market Maker (AMM) pools — typically Uniswap v2/v3, Curve, Balancer, SushiSwap. A searcher detects a 3+-pool cycle whose implied product exceeds 1, executes the entire trade in one transaction (often via [[flash-loan-arbitrage|flash loan]]), and pockets the difference net of gas. Foundational MEV strategy on Ethereum and major L2s; the on-chain incarnation of [[triangular-arbitrage|triangular FX arb]].

## Edge Source

**Latency** + **structural** + **analytical**.

- **Latency:** Price moves on one pool (e.g. Uniswap WETH/USDC) before another (e.g. Curve cWETH/cUSDC) updates.
- **Structural:** Each AMM has a different bonding curve (constant product, stableswap, weighted) — implied rates differ by design until rebalanced.
- **Analytical:** Detecting profitable cycles in a graph of 1000+ pools requires graph algorithms (Bellman-Ford, Johnson's) and live state.

## Why This Edge Exists

Every Uniswap-style swap moves the pool price. A trader buying 100 ETH for USDC on Pool A pushes USDC/ETH up there, but does not affect Pool B. Pool B is now cheap relative to Pool A. Arb closes the gap.

The triangular variant: ETH/USDC, USDC/WBTC, WBTC/ETH — three pools, one cycle. Buying along the cycle rebalances all three; profit accrues if the cycle product > 1.

Counterparty: large directional swappers (whales, treasury rebalancers, retail aggregator trades), and the operators of inferior arbitrage bots whose bundles lose the priority gas auction.

## Null Hypothesis

Under efficient markets, all pool implied rates equal the global mid-price up to gas + slippage costs, and no cycle product would exceed 1 net of costs. Empirically, Eigenphi tracked hundreds of thousands of profitable cyclic-arb transactions on Ethereum in 2024, totalling on the order of $300M extracted — a clear rejection of the no-edge null.

## Rules

1. Run a graph of all relevant pools, updated each block.
2. For every cycle (length 3-5) compute the product of effective swap rates.
3. Solve for optimal trade size (∂profit/∂x = 0 — closed-form for v2 constant-product).
4. Bundle trade via Flashbots / private mempool to avoid front-running.
5. Pay competitive priority fee (gas) — typically 30-90% of expected profit goes to the validator.
6. Use flash loan to avoid capital lockup for legs.

## Implementation Pseudocode

```python
graph = build_pool_graph()
for block in chain:
    graph.update(block.events)
    cycles = find_cycles(graph, max_length=5)
    for cycle in cycles:
        x_opt = solve_optimal_input(cycle)
        profit = simulate(cycle, x_opt) - gas_estimate(cycle)
        if profit > min_threshold:
            tx = build_flash_loan_swap_chain(cycle, x_opt)
            submit_to_flashbots(tx, priority_fee=profit * 0.7)
```

## Indicators / Data Used

- Pool reserves (read directly from contract state).
- Mempool monitoring (Flashbots, BloxRoute, Eden).
- Gas price oracle (next-block prediction).
- Eigenphi / EigenTx for backtesting historical extraction.

## Example Trade

**Stylized example, representative of 2024 mainnet conditions: ETH/USDC/WBTC cycle on Uniswap v3.**

Block N: large $50M ETH buy on Uniswap v3 ETH/USDC 0.05% pool pushed effective ETH/USDC up 0.4%. ETH/WBTC and WBTC/USDC pools unchanged.

Cycle: USDC → ETH → WBTC → USDC. Product 1.0028 → 0.28% gross.

Searcher executes: flash-loan 5M USDC, swap to ~2,000 ETH, swap to ~67 WBTC, swap to 5,014,000 USDC. Profit $14,000 gross, $4,000 to validator, $10,000 net. Latency: 1 block (~12s).

## Performance Characteristics

Eigenphi MEV reports 2024:
- Median cyclic arb profit: $30-150 per trade.
- Top searchers (jaredfromsubway.eth, MEV-bot-v2) extracted $5-50M each.
- Validator capture: 60-90% of extractable value via priority fees.
- Total Ethereum atomic-arb volume: highly regime-dependent — order of $100M-1B/day notional, spiking during volatile periods.

## Capacity Limits

Per-trade limited by pool depth (typical sweet spot $50K-2M per trade). Strategy-level capacity ~$50M+ via flash loans (no working capital constraint), but most profit goes to validators in mature competition.

## What Kills This Strategy

- Concentrated liquidity (Uniswap v3) reduces cross-pool dislocations.
- Order-flow auctions (CoW, MEV-Share, OFA) internalize MEV before it reaches public mempool.
- L2 sequencer ordering (Arbitrum, Optimism) eliminates Flashbots auction.
- Intent-based execution shrinks the public-mempool surface.

## Kill Criteria

- Median trade profit drops below gas cost for 90 days.
- Validator capture exceeds 95% of gross profit.
- Pool fragmentation collapses (DEX consolidation).

## Advantages

- Atomic — no leg risk.
- Capital-efficient via flash loans.
- High frequency, high Sharpe.

## Disadvantages

- Hyper-competitive — dominated by 5-10 searchers.
- Validator captures most value via gas auction.
- Failed bundles lose priority fee + gas.

## Sources

- Daian et al., *Flash Boys 2.0* (2019).
- Eigenphi MEV Inspect data.
- Flashbots Transparency Dashboard.
- jaredfromsubway.eth and other searcher post-mortems.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI serves pool discovery, token screening, and depth for building the cycle graph; per-block reserves, mempool, and the priority-gas auction are off-API (native RPC + Bellman-Ford solver + Flashbots).

**Live data:**
- `GET /api/v1/dex/trending` / `GET /api/v1/dex/new-pools` — candidate pools/venues for cycle construction across supported chains
- `GET /api/v1/dex/token/{chain}/{address}` — token + top pools to build the pool graph
- `GET /api/v1/liquidity/depth` — depth at 10/25/50/100 bps to bound optimal cycle size before slippage kills the edge
- `GET /api/v1/dex/security/{chain}/{address}` — token-trap screening for any leg of the triangle

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV for cross-pool dislocation research

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/trending"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-dex]], [[cryptodataapi-regimes]].

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can pre-filter routes; execution stays on-chain:

- **Pool graph** — `GET /api/v1/dex/trending`, `/dex/new-pools`, and `/dex/token/{chain}/{address}` seed the pool graph and candidate 3-5-leg cycles; per-block reserves and mempool are off-API.
- **Safety + sizing** — `GET /api/v1/dex/security/{chain}/{address}` screens each leg's token; `GET /api/v1/liquidity/depth` bounds the optimal input before slippage kills the cycle.
- **Regime gate** — `GET /api/v1/liquidity/regime` fragility flags when concentrated liquidity has collapsed cross-pool dislocations.
- **Backtest** — `GET /api/v1/backtesting/klines` for cross-pool spread research; validator-capture economics must be modelled off-API.
- **Tip** — atomic execution means no leg risk, but most gross goes to validators via priority fee — pre-filter routes here, price inclusion on-chain.

## Related

[[mev-strategies]] · [[flash-loan-arbitrage]] · [[triangular-arbitrage]] · [[liquidation-cascade-arbitrage]] · [[cross-chain-arbitrage]] · [[mev-execution-guide]]
