---
title: "Cross-L2 Arbitrage"
type: strategy
created: 2026-04-26
updated: 2026-07-19
status: good
tags: [arbitrage, crypto, defi, ethereum, algorithmic]
aliases: ["L2-to-L2 Arb", "Rollup Arbitrage", "Sequencer Arbitrage"]
related: ["[[cross-chain-arbitrage]]", "[[dex-pool-triangular-arbitrage]]", "[[multi-leg-arbitrage]]", "[[intent-based-arbitrage]]"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: live
edge_source: [latency, structural, informational]
edge_mechanism: "Each L2 (Arbitrum, Optimism, Base, zkSync, Polygon zkEVM, Linea, Scroll) has its own sequencer producing blocks at different cadences (~250ms-2s) with different liquidity. Same asset trades at different prices across L2s for seconds-to-minutes; arbs close the gap via fast bridges (Across, Hop, Stargate) or shared inventory."
data_required: [per-l2-pool-reserves, sequencer-block-feeds, fast-bridge-rates, l2-l2-message-latency]
min_capital_usd: 100000
capacity_usd: 200000000
crowding_risk: medium
expected_sharpe: 2
expected_max_drawdown: 0.12
breakeven_cost_bps: 12
decay_evidence: "L2 fragmentation grew through 2023-2025 as new rollups launched; cross-L2 arb gross volume doubled 2024 → 2025. Compression begins as Across/Hop and shared sequencers (Espresso, Astria 2025) mature."
---

# Cross-L2 Arbitrage

Arbitrage exploiting price divergence of the same asset across Ethereum Layer-2 rollups (Arbitrum, Optimism, Base, zkSync Era, Polygon zkEVM, Linea, Scroll, Mantle, Blast). Distinct from [[cross-chain-arbitrage|generic cross-chain arb]]: all participating L2s settle to Ethereum mainnet, share security assumptions, and have rapidly maturing fast-bridge infrastructure (Across, Hop, Stargate, Synapse) that closes 12s-3min latency windows for 0.05-0.20% bridge fees.

## Edge Source

**Latency** + **structural** + **informational**.

- **Latency:** Each L2 has its own sequencer cadence (Base ~2s, Optimism ~2s, Arbitrum ~250ms, zkSync ~2-5s). Trades on one L2 don't propagate to others until cross-L2 messages or arbitrageurs move price.
- **Structural:** Liquidity fragmentation — Uniswap on Base has different pools/depths than Uniswap on Arbitrum. Same with Aave, Curve, etc.
- **Informational:** Sequencer mempool monitoring per-L2 reveals incoming trades (Base sequencer is currently public; Arbitrum's was, becoming private 2025).

## Why This Edge Exists

Asset wrappers proliferate per L2: ETH on Base ≠ ETH on Arbitrum ≠ ETH on Optimism — same token, but the bridge between them costs 5-25 bp and 1-15 minutes. So the price of "ETH" on each L2 can drift before arb closes the gap.

Bridges:
- **Native L1 bridge:** 7-day challenge period for optimistic rollups; instant for ZK rollups.
- **Fast bridges:** Across, Hop, Stargate. 1-3 minute typical, 5-25 bp fee. Run by liquidity providers who hold inventory on both sides.
- **Native messaging:** LayerZero, Hyperlane, Wormhole. ~1-15 min, 1-5 bp.

Cross-L2 arb sits in the seconds-to-minutes window between sequencer divergence and fast-bridge close.

Counterparty: smaller arb bots running per-L2 in isolation; users of slow native bridges; liquidity providers on the slower side.

## Null Hypothesis

Under the null, each L2's price is a noisy observation of one common Ethereum-anchored price, and any observed cross-L2 divergence is exactly the cost of closing it: bridge fee + gas on both sides + adverse selection. A naive bot that fires on every spread > 0 would (a) pay bridge fees to trade mean-reverting noise that would have converged for free, and (b) get adversely selected when the "cheap" leg is cheap because toxic flow is mid-propagation from another venue — i.e., the spread is information, not mispricing. The null predicts realized per-trade PnL ≈ 0 after gas, bridge fees, failed-transaction costs, and inventory carry. The edge claim survives only if spreads persist longer than the fastest close path (currently 1-3 min fast-bridge or pre-positioned inventory at ~0 latency) often enough that the fill-rate-weighted net PnL stays positive — which per-searcher inventory-mode economics (median $80-400/trade net) currently support, and which shared sequencers would collapse.

## Rules

1. Run L2 nodes (or RPC subscriptions) for each target rollup.
2. Per-block on each L2: snapshot pool reserves for monitored pairs.
3. Compute pair-by-pair price divergence across L2s.
4. If divergence > bridge_fee + gas_both_sides + threshold:
   - Buy on cheap L2.
   - Sell on expensive L2.
   - Bridge via Across/Hop OR rely on inventory rebalance later.
5. Inventory mode: pre-position USDC, ETH on multiple L2s; rebalance via slow bridge weekly.
6. Sizing: cap each trade at the size where own price impact eats one-third of the gross spread, bounded by fast-bridge route depth and per-L2 inventory.

## Implementation Pseudocode

```python
l2s = ["arbitrum", "optimism", "base", "zksync", "polygon-zkevm"]
on tick:
    snapshots = {l2: snapshot_pools(l2, monitored_pairs) for l2 in l2s}
    for pair in monitored_pairs:
        prices = {l2: snapshots[l2][pair].mid for l2 in l2s}
        cheap, expensive = min(prices, key=prices.get), max(prices, key=prices.get)
        spread_bps = (prices[expensive] - prices[cheap]) / prices[cheap] * 10000
        if spread_bps > bridge_fee_bps + gas_bps + threshold:
            execute_cross_l2_arb(pair, cheap, expensive, size=optimal)
```

## Indicators / Data Used

- Per-L2 node or low-latency RPC/websocket subscriptions (own nodes preferred — Arbitrum's ~250ms cadence makes shared public RPC marginal).
- Pool-reserve snapshots per block for monitored pairs: Uniswap v3/v4, Curve, plus the dominant native DEX per L2 (Aerodrome on Base, Camelot on Arbitrum, Velodrome on Optimism).
- Sequencer feeds / mempools where public (Base sequencer; Arbitrum sequencer feed).
- Fast-bridge quote APIs and pool depth (Across, Hop, Stargate) — live fee + latency per route.
- Per-L2 gas oracles, including the L1 data-posting component (much cheaper post-EIP-4844 blobs, March 2024).
- L2Beat for rollup status, upgrade calendars, and sequencer-outage monitoring.

## Example Trade

**ETH/USDC across Base / Arbitrum, 2025-03-14, 14:23 UTC.**

Base sequencer published large $4M USDC → ETH swap. Local pool moved ETH/USDC up 0.22%. Arbitrum same pair unchanged.

Trade:
- Buy ETH on Arbitrum @ $2,847 (size 200 ETH = $570K).
- Sell ETH on Base @ $2,853 (same notional, depth permitting).
- Net spread captured: 0.21% gross = $1,200.
- Bridge ETH from Base back to Arbitrum via Across: $200 fee, 90 sec.
- OR: hold inventory, rebalance later.
- Net profit: $700-900 after gas both sides.

## Performance Characteristics

Estimated 2025 cross-L2 arb gross extraction: $200-400M/yr across all rollups. Top 5 searchers capture ~70%. Median per-trade profit $80-400; long-tail to $20K+ during volatility events.

Sharpe ~1.5-2.5 net of inventory cost.

## Capacity Limits

Bound by fast-bridge depth (Across pool depth $50-200M per asset on top L2s; deeper than Hop). Single-asset capacity per searcher ~$50-200M working capital across L2s.

## What Kills This Strategy

- **Shared sequencers** (Espresso, Astria, mid-2025+): unify L2 sequencing → eliminate sequencer-divergence edge.
- **Native ZK fast finality** (Polygon AggLayer, zkSync Hyperchains): collapse bridge latency to <1 block.
- **Solver internalization:** [[intent-based-arbitrage|CoW Protocol]] cross-chain intents (CoW Hooks) absorb the flow.
- L2 consolidation reducing fragmentation.

## Kill Criteria

- Median per-trade gross drops below combined gas + bridge cost for 30 days.
- Shared-sequencer adoption >50% of L2 volume.

## Advantages

- Lower competition than mainnet MEV.
- Shared Ethereum security assumption (vs riskier cross-chain bridges).
- Growing as new L2s launch.

## Disadvantages

- Inventory cost across many L2s.
- Bridge counterparty risk (Across, Hop have insurance funds but not zero risk).
- Sequencer outages strand inventory (Linea Jun 2024, zkSync Dec 2024 incidents).

## Sources

- L2Beat per-rollup analytics.
- Across Protocol docs and TVL dashboards.
- Hop Protocol stats.
- Espresso / Astria shared-sequencer specs.
- Vitalik Buterin, *Endgame* (2021) and rollup-centric roadmap updates 2024-2026.

## Getting the Data (CryptoDataAPI)

CryptoDataAPI serves DEX pool prices/depth on its supported chains (Base, Arbitrum, Ethereum, BSC). Sequencer feeds and the Optimism/zkSync/Linea/Scroll pools it does not cover need own L2 nodes.

**Live data:**
- `GET /api/v1/dex/token/{chain}/{address}` — per-token price + pools; diff the same asset across Base / Arbitrum / Ethereum / BSC
- `GET /api/v1/dex/trending` — per-chain flow concentration
- `GET /api/v1/liquidity/depth` — depth at 10/25/50/100 bps to size against the thinner L2 pool
- `GET /api/v1/dex/security/{chain}/{address}` — token screening

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for spread research
- DEX is live-only — store polls to build per-L2 price history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/token/arbitrum/0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-dex]], [[cryptodataapi-regimes]].

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can screen the covered-chain gaps:

- **Signal** — `GET /api/v1/dex/token/{chain}/{address}` on Base vs Arbitrum (and Ethereum/BSC) gives the same-asset gap; sequencer mempools and Optimism/zkSync/Linea/Scroll pools are off-API (own L2 nodes).
- **Depth gate** — `GET /api/v1/liquidity/depth` sizes against the thinner L2 pool; `GET /api/v1/dex/security/{chain}/{address}` screens the token.
- **Regime gate** — `GET /api/v1/liquidity/regime` fragility warns when an L2 pool cannot absorb the arb.
- **Backtest** — `GET /api/v1/backtesting/klines` for spread studies; no per-L2 reserve archive, so inventory-mode economics come from stored polls.
- **Tip** — the edge collapses under shared sequencers; treat pre-positioned inventory (≈0 latency) as the durable path, not bridge-and-arb.

## Related

[[cross-chain-arbitrage]] · [[dex-pool-triangular-arbitrage]] · [[multi-leg-arbitrage]] · [[intent-based-arbitrage]] · [[mev-strategies]] · [[private-mempool-arbitrage]] · [[bridge-risk]]
