---
title: "Gas Fees"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [crypto, defi, market-microstructure, execution]
aliases: ["Gas Fees", "Gas Costs", "Transaction Fees", "Gwei", "EIP-1559"]
related: ["[[ethereum]]", "[[solana]]", "[[layer-2]]", "[[flash-loan-arbitrage]]", "[[cross-chain-arbitrage]]", "[[mev-strategies]]", "[[mev-execution-guide]]", "[[fees]]", "[[transaction-costs]]", "[[defi-contract-registry]]", "[[defi]]"]
---

# Gas Fees

Gas fees are the cost of executing transactions on blockchain networks. For on-chain arbitrage ([[flash-loan-arbitrage]], [[cross-chain-arbitrage]], [[mev-strategies]]), gas is often the **binding constraint on profitability** — a strategy may detect a profitable spread but cannot execute because the gas cost exceeds the expected profit. This page is the **reference hub** for fee mechanics across chains; it sits alongside [[fees]] (exchange/trading fees) and [[transaction-costs]] (the full cost stack).

### Why Gas Fees Matter to Traders

- **They set the floor on viable arb size** — see the [[#Breakeven Spread Formula|breakeven spread formula]] below.
- **They are a real-time congestion gauge** — spiking base fees signal a busy chain (NFT mint, liquidation cascade, memecoin launch).
- **They drive chain selection** — the same DeFi strategy is profitable on [[#Gas Costs by Chain|Base or Solana]] and unprofitable on Ethereum mainnet.
- **They are part of MEV** — priority fees and the [[mev-strategies|priority gas auction]] are how searchers compete for block position.

## How Gas Works (Ethereum)

Every operation on Ethereum costs a fixed amount of **gas units**. The total transaction cost is:

```
transaction_cost = gas_units_used × gas_price_per_unit (in gwei)
cost_in_ETH = transaction_cost / 1,000,000,000
cost_in_USD = cost_in_ETH × ETH_price
```

### Post-EIP-1559 Fee Structure

Since August 2021, Ethereum uses a two-component fee model:

| Component | Description | Behavior |
|---|---|---|
| **Base fee** | Algorithmically set by the protocol based on block utilization | Burns ETH. Increases when blocks are >50% full, decreases when <50%. Changes max ±12.5% per block |
| **Priority fee (tip)** | Optional tip to the block builder for inclusion priority | Goes to the validator/builder. Higher tip = faster inclusion |

```
total_gas_price = base_fee + priority_fee
```

The **base fee is burned** (removed from supply), making ETH deflationary during high-activity periods — this is the "ultrasound money" mechanism. The **priority fee (tip)** goes to the validator/builder and is what searchers bid up in a [[mev-strategies|priority gas auction (PGA)]] to win block ordering. EIP-1559 replaced the old first-price-auction model, where users blindly overbid and frequently overpaid; the algorithmic base fee makes fees far more predictable block-to-block (the ±12.5% cap means the next block's base fee is knowable within a tight band).

### Fee Models Differ by Chain

EIP-1559 is Ethereum's model. Other chains price computation and congestion differently — this matters when porting a strategy across chains.

| Chain / Class | Fee Model | Congestion Pricing |
|---|---|---|
| **Ethereum (L1)** | EIP-1559 base + priority; gas-unit metered | Base fee adjusts ±12.5%/block on utilization |
| **Ethereum L2 rollups** | Tiny L2 execution fee **+ amortised L1 data-availability cost** | L1 data cost dominates; cut sharply by EIP-4844 "blobs" (Mar 2024) |
| **[[solana]]** | Flat base fee per signature **+ optional priority fee (per compute unit)** + localised fee markets | Priority fees spike on hot accounts (popular mints) without congesting the whole chain |
| **BNB Chain / Polygon PoS** | EIP-1559-style on EVM, but far lower base | Cheaper validator set / different security model |

Two big structural shifts cut Ethereum-ecosystem fees materially: **EIP-1559** (Aug 2021, predictable base fee) and **EIP-4844 / proto-danksharding "blobs"** (Mar 2024), which gave rollups a dedicated, cheap data channel and dropped L2 fees by an order of magnitude — a key reason activity migrated to [[layer-2|L2s]].

### Typical Gas Costs by Operation

| Operation | Gas Units | Cost at 20 gwei ($3,000 ETH) | Cost at 100 gwei |
|---|---|---|---|
| ETH transfer | 21,000 | $1.26 | $6.30 |
| ERC-20 transfer | 65,000 | $3.90 | $19.50 |
| Uniswap V3 swap | 150,000-300,000 | $9-18 | $45-90 |
| Flash loan (Aave) | 300,000-500,000 | $18-30 | $90-150 |
| Multi-hop swap (3 pools) | 400,000-800,000 | $24-48 | $120-240 |
| Flash loan arb (full cycle) | 500,000-1,500,000 | $30-90 | $150-450 |

### Historical Gas Price Ranges (Ethereum Mainnet)

| Period | Median Base Fee (gwei) | 95th Percentile | Driver |
|---|---|---|---|
| DeFi Summer (Aug-Nov 2020) | 40-100 | 200-500 | Yield farming frenzy |
| NFT mania (Mar-May 2021) | 50-150 | 300-1000+ | NFT mints, gas wars |
| Merge era (Sep 2022-2023) | 10-30 | 50-100 | Lower activity post-merge |
| L2 migration (2024) | 8-20 | 40-80 | Activity moving to L2s |
| Current (early 2026) | 5-15 | 30-60 | Mature L2 ecosystem, lower mainnet demand |

## Gas Costs by Chain

| Chain | Typical Transaction Cost | Speed | Finality | Best For |
|---|---|---|---|---|
| **Ethereum mainnet** | $1-50+ (gas dependent) | 12 sec blocks | ~12 min (64 slots) | High-value arbs where $50+ gas is negligible |
| **Arbitrum** | $0.01-0.50 | 0.25 sec blocks | ~10 min (L1 finality) | Most DeFi arbs — 100x cheaper than mainnet |
| **Optimism** | $0.01-0.50 | 2 sec blocks | ~10 min (L1 finality) | Similar to Arbitrum |
| **Base** | $0.005-0.20 | 2 sec blocks | ~10 min (L1 finality) | Cheapest Ethereum L2; Aerodrome DEX |
| **Polygon PoS** | $0.001-0.05 | 2 sec blocks | ~3 min | Very cheap but different security model |
| **Solana** | $0.001-0.01 | 0.4 sec slots | ~0.4 sec | Fastest and cheapest; Jupiter DEX |
| **BNB Chain (BSC)** | $0.05-0.30 | 3 sec blocks | ~15 sec | Cheap; PancakeSwap DEX |

**Arb implication:** On Ethereum mainnet, a flash loan arb needs >$30-90 profit to break even on gas. On Arbitrum/Base, the breakeven drops to $0.50-5.00 — making many more arbs viable. On Solana, nearly any arb >$0.01 is gas-feasible.

## Gas as an Arbitrage Cost

### Breakeven Spread Formula

For any on-chain arb:
```
min_profitable_spread = gas_cost / trade_notional
```

| Trade Size | Ethereum ($30 gas) | Arbitrum ($0.30 gas) | Solana ($0.005 gas) |
|---|---|---|---|
| $1,000 | 3.0% min spread | 0.03% | 0.0005% |
| $10,000 | 0.30% | 0.003% | 0.00005% |
| $100,000 | 0.03% | 0.0003% | 0.000005% |

**Takeaway:** Small arbs ($1-10K) are only viable on L2s or Solana. Ethereum mainnet requires either large size or very wide spreads.

### Failed Transaction Cost

Reverted transactions still consume gas (up to the point of revert). For arb bots, failed attempts are a major cost:
```
total_gas_cost = successful_gas + failed_gas
net_profit = arb_profit - total_gas_cost
```

If a bot attempts 100 arbs and only 20 succeed (80% revert rate), the effective gas cost per successful arb is 5x higher than the single-transaction cost. This is why [[mev-strategies|Flashbots]] bundles are critical — bundles that fail are never included, so failed bundles cost zero gas.

### Gas Price Prediction

Arb bots must predict gas prices for the *next block* to decide whether to submit:
- **EIP-1559 base fee** is predictable: current_base_fee × (1 ± 0.125) max per block
- **Priority fee** depends on mempool congestion — monitor pending transactions
- **Block utilization** signals direction: >50% target = base fee will increase next block

## Gas Optimization Techniques

1. **Use L2s** for arbs below $10K notional — 100x cheaper than mainnet
2. **Batch operations** — combine multiple swaps into a single transaction using a custom contract
3. **Flashbots bundles** — zero cost for failed bundles (see [[mev-execution-guide]])
4. **Gas token optimization** — use Solidity `unchecked` blocks, minimize storage writes, use calldata efficiently
5. **Time transactions** — gas is cheapest on weekends and during Asian night hours (US/EU traders inactive)
6. **Set max gas price** — reject arb if gas exceeds profitability threshold

## Key Metrics & Tools Traders Watch

| Metric / Tool | What It Tells You | Where |
|---|---|---|
| **Current base fee (gwei)** | The mandatory, burned portion of every tx; sets the next-block floor | Etherscan Gas Tracker |
| **Priority fee percentiles** | What tip is needed for fast vs slow inclusion right now | Etherscan, Blocknative |
| **Block utilization (% of gas target)** | >50% = base fee rising next block; <50% = falling | Etherscan |
| **Blob fee / blob count** | The L1 data-availability cost driving L2 fees post-EIP-4844 | blobscan.com |
| **L2 fee comparison** | Cheapest chain to route an arb of a given size | L2Fees.info, L2Beat |
| **ETH burn rate** | Net issuance/deflation; a proxy for sustained on-chain demand | ultrasound.money |
| **Mempool size** | Pending-tx backlog; predicts near-term priority-fee pressure | Blocknative, Etherscan |

## Risks & Pitfalls

| Risk | Description | Mitigation |
|---|---|---|
| **Gas spike mid-execution** | Base fee jumps between detection and submission, turning a profitable arb into a loss | Set a hard max gas price; abort if exceeded |
| **Failed-tx gas drain** | Reverted transactions still burn gas up to the revert point | Use [[mev-strategies\|Flashbots]] bundles — failed bundles cost zero |
| **Underpriced tip → stuck tx** | Too low a priority fee leaves the tx pending and exposed | Dynamic tip sizing from live percentiles |
| **L1 data-cost surge on L2** | An L2 looks cheap until L1 blob/calldata costs spike during congestion | Monitor blob fees, not just L2 execution fee |
| **Cross-chain fee asymmetry** | Bridging/settlement gas on one leg can exceed the arb edge | Model gas on *every* leg of a [[cross-chain-arbitrage]] |
| **Sandwich/front-run via gas** | Competitors outbid your priority fee to reorder around you | Private mempools / Flashbots / Jito bundles |

## Related

**Concepts**: [[layer-2]], [[transaction-costs]], [[fees]], [[mev-strategies]], [[defi]]
**Chains**: [[ethereum]], [[solana]]
**Strategies**: [[flash-loan-arbitrage]], [[cross-chain-arbitrage]], [[mev-execution-guide]]
**Infra**: [[defi-contract-registry]]

## Sources

- Ethereum EIP-1559 specification; EIP-4844 (proto-danksharding) specification
- Etherscan gas tracker (historical data)
- L2Fees.info (L2 cost comparison); blobscan.com (blob fee data)
- General market knowledge; no specific wiki source ingested yet.
