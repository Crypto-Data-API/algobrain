---
title: "Cross-Chain Arbitrage"
type: strategy
created: 2026-04-14
updated: 2026-07-19
status: excellent
tags: [arbitrage, crypto, defi, cross-chain, bridges, mev, algorithmic, market-neutral, layer-2]
aliases: ["Cross-Chain Arb", "Inter-Chain Arbitrage", "Bridge Arbitrage", "Multi-Chain Arbitrage"]
strategy_type: algorithmic
timeframe: scalp|intraday
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [structural, latency, risk-bearing]
edge_mechanism: "Price fragmentation across independent blockchain ecosystems creates persistent mispricings; bridge latency and risk premiums prevent instant convergence, leaving profit for those willing to bear bridging risk and maintain multi-chain infrastructure."
data_required: [ohlcv-realtime, dex-pool-reserves, bridge-fees, gas-prices, mempool]
min_capital_usd: 10000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: 1.2
expected_max_drawdown: 0.10
breakeven_cost_bps: 50
related: ["[[cross-exchange-arbitrage]]", "[[flash-loan-arbitrage]]", "[[triangular-arbitrage]]", "[[mev-strategies]]", "[[cross-chain-bridges]]", "[[layer-2]]", "[[cctp]]", "[[arbitrage]]", "[[slippage]]", "[[smart-contract-risk]]", "[[2020-2024-bridge-exploits]]"]
---

# Cross-Chain Arbitrage

Cross-chain arbitrage exploits price discrepancies for the same token across different blockchain networks -- buying on the chain where the price is lower and selling (or bridging and selling) on the chain where the price is higher. Unlike [[cross-exchange-arbitrage]], which operates across centralized exchanges connected by internal ledgers, cross-chain arb requires moving assets between independent blockchains via [[cross-chain-bridges|bridges]], messaging protocols, or native transfer mechanisms, introducing latency, gas costs, and smart contract risk that do not exist in CEX-to-CEX arb.

The proliferation of [[layer-2]] rollups (Arbitrum, Optimism, Base, zkSync), alt-L1s (Solana, Avalanche, BSC), and hundreds of DEXs across these chains has made cross-chain arbitrage one of the most structurally rich arb domains in crypto. As of 2025-2026, professional cross-chain searchers extract millions of dollars weekly by maintaining infrastructure across 5-15+ chains and routing through bridges like [[layerzero|LayerZero]], [[wormhole|Wormhole]], [[stargate-finance|Stargate]], [[across-protocol|Across]], and [[cctp|Circle CCTP]].

## Edge Source

**Structural** + **Latency** + **Risk-bearing** (see [[edge-taxonomy]])

The edge is primarily structural: each blockchain is an independent execution environment with its own liquidity pools, order books, and price discovery. There is no atomic cross-chain transaction -- bridging assets takes seconds to minutes (or hours for optimistic rollup withdrawals), creating a window during which prices can diverge. The arbitrageur bears bridge risk (smart contract exploit, stuck transactions, oracle failure) and latency risk (prices moving during the bridge) that most participants avoid, earning a premium for this risk-bearing.

A secondary latency edge exists for searchers who maintain pre-positioned inventory on multiple chains, eliminating bridge delay entirely and competing on detection-to-execution speed.

## Why This Edge Exists

Cross-chain price discrepancies persist because of fundamental architectural constraints:

1. **No atomic cross-chain settlement.** Unlike a single-chain DEX arb (which can use [[flash-loan-arbitrage|flash loans]] for atomic execution), moving tokens between chains is inherently asynchronous. This latency prevents instantaneous price convergence.

2. **Fragmented liquidity.** The same token (e.g., USDC, WETH, ARB) may trade on Uniswap V3 on Ethereum, Camelot on Arbitrum, Aerodrome on Base, and Raydium on Solana -- each with independent liquidity depth and pricing.

3. **Bridge costs and friction.** Gas fees on source and destination chains, bridge protocol fees (0.01%-0.5%), and withdrawal delays (7 days for optimistic rollup canonical bridges) create a "no-arbitrage band" -- prices can diverge by the width of total bridging cost without triggering arb activity.

4. **Smart contract risk premium.** After $2.5B+ in [[2020-2024-bridge-exploits|bridge exploits]] (Ronin $625M, Wormhole $325M, Nomad $190M), sophisticated capital demands a risk premium for exposing funds to bridge contracts, keeping the no-arb band wider than it would be in a zero-risk environment.

5. **Heterogeneous market participants.** Retail users on different chains often trade based on local liquidity and are unaware of better prices on other chains. Solana-native traders may not check Ethereum DEX prices and vice versa.

The counterparty is any trader who transacts at a worse price on one chain when a better price is available on another -- effectively paying the cost of fragmented liquidity.

## Null Hypothesis

Under the null hypothesis of no edge, cross-chain price discrepancies would be smaller than total bridging costs (gas + bridge fees + slippage + risk premium), and any apparent profits would be consumed by adverse selection, bridge failures, and gas waste on failed transactions. A random strategy of bridging assets between chains would break even or lose money after costs.

## Rules

### Entry

1. **Monitor prices across chains.** Maintain real-time price feeds from DEXs on 5-15+ chains. For each target token, track the best bid and ask on each chain's deepest liquidity venue (e.g., ETH/USDC on Uniswap V3 Ethereum, Camelot Arbitrum, Aerodrome Base, Orca Solana).

2. **Calculate the cross-chain spread.** For each token pair, compute:
   ```
   net_spread = price_high_chain - price_low_chain - gas_source - gas_dest - bridge_fee - expected_slippage
   ```
   Only proceed if `net_spread > 0` and exceeds a minimum threshold (typically 0.1-0.3% to account for model error).

3. **Choose execution mode:**
   - **Pre-positioned inventory (fast path):** If capital is already deployed on both chains, execute buy and sell simultaneously -- no bridging needed. This is the competitive edge for professional searchers.
   - **Bridge-and-arb (slow path):** Buy on the cheap chain, bridge to the expensive chain, sell. Requires the spread to persist through the bridge duration (seconds to minutes for fast bridges, hours for canonical L2 bridges).
   - **Intent-based routing:** Submit the arb as an intent to a solver network (CoW Protocol, UniswapX, Across) that handles cross-chain execution. Lower control but eliminates bridge management.

4. **Validate bridge path.** Check bridge liquidity, relayer availability, and current bridge fees. Some bridges have limited liquidity for specific tokens or routes.

5. **Simulate the full transaction.** On EVM chains, use Tenderly or local forks to simulate each leg and confirm net profitability. Account for MEV risk -- other searchers may front-run or sandwich your bridge transaction on the destination chain.

### Exit

1. **Immediate completion (pre-positioned).** When using pre-positioned inventory, both legs execute within seconds. Profit is realized instantly.

2. **Post-bridge sell (bridge-and-arb).** After the bridge completes, immediately sell on the destination chain. If the spread has closed during bridging, cut the loss by selling at market rather than holding directional exposure.

3. **Periodic rebalancing.** Pre-positioned capital drifts as arbs execute in one direction. Rebalance across chains during low-gas periods using the cheapest available bridge.

### Position Sizing

- Size each arb to the minimum liquidity available across the buy venue, bridge capacity, and sell venue
- Never bridge more than 5-10% of total capital through a single bridge contract at once (bridge exploit risk)
- Diversify bridge exposure across 3-5 bridge protocols
- Keep a reserve on each chain for gas and unexpected rebalancing

## Implementation Pseudocode

```python
# Cross-chain arbitrage scanner (simplified)
import asyncio

CHAINS = ["ethereum", "arbitrum", "base", "optimism", "solana"]
TOKENS = ["WETH", "USDC", "ARB", "OP", "SOL"]

async def scan_cross_chain_arb():
    while True:
        for token in TOKENS:
            prices = {}
            for chain in CHAINS:
                prices[chain] = await get_best_price(token, chain)
            
            best_buy = min(prices, key=lambda c: prices[c]["ask"])
            best_sell = max(prices, key=lambda c: prices[c]["bid"])
            
            gross_spread = prices[best_sell]["bid"] - prices[best_buy]["ask"]
            
            # Calculate costs
            gas_buy = await estimate_gas(best_buy, "swap")
            gas_sell = await estimate_gas(best_sell, "swap")
            bridge_fee = await get_bridge_fee(best_buy, best_sell, token)
            slippage_est = estimate_slippage(
                prices[best_buy]["depth"], 
                prices[best_sell]["depth"],
                trade_size
            )
            
            net_spread = gross_spread - gas_buy - gas_sell - bridge_fee - slippage_est
            
            if net_spread > MIN_PROFIT_THRESHOLD:
                if has_inventory(best_sell, token):
                    # Fast path: simultaneous execution
                    await execute_simultaneous(
                        buy_chain=best_buy, 
                        sell_chain=best_sell,
                        token=token,
                        size=calculate_size(prices, token)
                    )
                else:
                    # Slow path: bridge and arb
                    if net_spread > BRIDGE_RISK_THRESHOLD:
                        await execute_bridge_arb(
                            buy_chain=best_buy,
                            sell_chain=best_sell,
                            bridge=select_optimal_bridge(best_buy, best_sell),
                            token=token,
                            size=calculate_size(prices, token)
                        )
        
        await asyncio.sleep(0.5)  # Poll every 500ms
```

## Indicators / Data Used

- **Cross-chain DEX prices** -- real-time bid/ask from AMMs and order books on each chain. WebSocket connections to major DEXs (Uniswap, SushiSwap, Curve, Raydium, Jupiter, Orca, Aerodrome, Camelot, GMX)
- **Bridge status and fees** -- real-time bridge availability, relayer liquidity, and fee quotes from LayerZero, Stargate, Across, Wormhole, CCTP, Hyperlane, Chainflip
- **Gas prices per chain** -- L1 and L2 gas costs determine the minimum profitable spread
- **DEX pool reserves / order book depth** -- determines maximum arb size before [[slippage]] eliminates profit
- **Bridge TVL and utilization** -- high utilization = slower settlement and higher fees
- **Wrapped vs native token tracking** -- USDC.e (bridged) vs native USDC trade at different prices; tracking which version is on which chain matters
- [[mempool]] monitoring (on applicable chains) -- detect competing arb transactions

## Bridge Comparison

The bridge layer is the defining infrastructure dependency of cross-chain arb. Different bridges trade off speed, cost, security model, and asset/route coverage. The "settlement model" column matters most: lock-and-mint and liquidity-network bridges settle in seconds to minutes; canonical optimistic-rollup bridges impose a 7-day challenge window for L2→L1 withdrawals.

| Bridge | Model | Typical Settlement | Notable For |
|--------|-------|--------------------|-------------|
| [[cctp]] (Circle CCTP) | Native burn-and-mint (USDC) | Minutes | Native USDC, no wrapped-token risk; converging stablecoin routes |
| [[across-protocol\|Across]] | Liquidity network + intents | Seconds–minutes | Fast fills, relayer-fronted liquidity |
| [[stargate-finance\|Stargate]] | Liquidity pools on [[layerzero\|LayerZero]] | Minutes | Unified stablecoin liquidity |
| [[layerzero\|LayerZero]] | Generic messaging | Varies by app | Messaging layer many bridges build on |
| [[wormhole\|Wormhole]] | Lock-and-mint (guardians) | Minutes | Broad chain coverage incl. Solana; prior $325M exploit |
| Hyperlane | Permissionless interchain messaging | Minutes | Custom security modules |
| Chainflip | Native cross-chain swaps (vaults) | Minutes | Native BTC/non-EVM assets |
| Canonical L2 bridges | Optimistic / ZK rollup bridge | 7 days (optimistic) / faster (ZK) | Lowest trust assumption; too slow for arb without fast-bridge overlay |

Searchers typically diversify across 3-5 of these (see Position Sizing) to cap exposure to any single bridge contract — the existential risk documented in [[2020-2024-bridge-exploits]] and [[smart-contract-risk]].

## Cost Stack

Every cross-chain arb must clear the full no-arbitrage band. Each cost component below subtracts from the gross spread; the trade is only viable when `gross_spread > sum(all costs) + risk_premium`:

| Cost Component | Typical Range | Notes |
|----------------|---------------|-------|
| Source-chain gas | $0.01–$15+ | L2s cheap; Ethereum mainnet spikes can kill the trade |
| Destination-chain gas | $0.01–$15+ | Same dynamics |
| DEX swap fee (each leg) | 0.01%–0.30% | Curve/stable pools low; volatile pairs higher |
| Bridge protocol fee | 0.01%–0.50% | Varies by bridge and route liquidity |
| [[slippage]] (each leg) | Depends on pool depth | Thinnest pool in the route caps size |
| Latency / price-drift risk | Variable | Only on the bridge-and-arb (slow) path |
| Risk premium | Implicit | Compensation for bearing bridge exploit + stuck-tx risk |

The pre-positioned (fast) path eliminates the bridge fee and latency-drift cost at execution time, paying those costs instead during periodic, batched rebalancing in low-gas windows — which is precisely why it is the professional searcher's edge.

## Example Trade

**Opportunity:** WETH trades at $3,380 on Aerodrome (Base) but $3,405 on Uniswap V3 (Ethereum mainnet). Spread: $25 (0.74%).

**Using pre-positioned inventory:**

1. **Buy 10 WETH on Base** via Aerodrome at $3,380 = $33,800. Gas: $0.05.
2. **Simultaneously sell 10 WETH on Ethereum** via Uniswap V3 at $3,405 = $34,050. Gas: $8.00.
3. **Gross spread:** $250.00.
4. **Costs:** Base gas ($0.05) + Ethereum gas ($8.00) + DEX fees (0.05% each side = $33.93) = $41.98.
5. **Net profit:** $250.00 - $41.98 = **$208.02** in ~2 seconds.
6. **Rebalance later:** Bridge 10 WETH from Ethereum back to Base via [[cctp|CCTP]] or [[across-protocol|Across]] during a low-gas window. Bridge cost: ~$3.00.

**Using bridge-and-arb (no pre-positioned inventory):**

1. **Buy 10 WETH on Base** at $3,380. Gas: $0.05.
2. **Bridge 10 WETH Base → Ethereum** via Across Protocol. Bridge fee: 0.06% ($20.28). Settlement: ~2 minutes.
3. **Sell 10 WETH on Ethereum** at $3,402 (price moved $3 against during bridge). Gas: $8.00. DEX fee: $17.01.
4. **Gross spread:** $220.00 (reduced due to price movement).
5. **Total costs:** $0.05 + $20.28 + $8.00 + $17.01 + $16.90 (buy-side DEX fee) = $62.24.
6. **Net profit:** $220.00 - $62.24 = **$157.76**, but with 2 minutes of directional exposure during bridging.

## Performance Characteristics

- **Win Rate:** 70-90% for pre-positioned inventory execution; 50-70% for bridge-and-arb (spread can close during bridge time)
- **Profit Factor:** 2.0-4.0 on pre-positioned arbs; 1.3-2.5 on bridge-and-arb
- **Average profit per trade:** $50-$500 depending on size and spread
- **Best conditions:** High [[volatility]], large DEX volume spikes, new token launches on specific chains, airdrop claim events (users bridge en masse creating temporary imbalances), chain-specific news (L2 incentive programs)
- **Worst conditions:** Low volatility, high gas (Ethereum mainnet congestion), bridge outages, periods of high MEV competition

## Capacity Limits

Cross-chain arb capacity is constrained by:

- **DEX pool depth.** The thinnest pool in the arb route determines max size. Many L2 DEX pools have $1-10M depth for mid-cap tokens.
- **Bridge throughput.** Bridges have per-transaction and daily volume limits. Across handles ~$500M/day; smaller bridges may cap at $10-50M.
- **Gas cost scaling.** Larger trades on AMMs face quadratic slippage, limiting profitable size per transaction.
- **Estimated total capacity:** $50-100M deployed across all active cross-chain arb participants before margins compress to near-zero. Individual strategies likely cap at $5-10M before the trader's own flow begins moving prices.

## What Kills This Strategy

- **Bridge unification.** If a single, fast, cheap bridge connects all chains with deep liquidity, cross-chain spreads converge to near-zero. [[cctp]] is moving in this direction for USDC. Chain abstraction protocols (Particle Network, NEAR's chain signatures) could eventually do this for all assets.
- **Intent-based trading systems.** UniswapX, CoW Protocol, and Across intents allow users to get cross-chain best execution without manually bridging, reducing the pool of uninformed flow that creates arb opportunities.
- **Bridge exploits.** A major hack on a bridge you're using can result in total loss of in-transit capital. See [[2020-2024-bridge-exploits]].
- **Chain consolidation.** If DeFi activity concentrates on fewer chains (e.g., Ethereum + 2-3 dominant L2s), the number of exploitable cross-chain pairs shrinks.
- **Regulatory action.** Sanctions screening on bridges (OFAC compliance) or bridge KYC requirements could restrict or slow bridging activity.
- **Faster L2 finality.** As L2s move toward real-time finality and shared sequencers, the latency window that creates arb opportunities narrows.

## Kill Criteria

- Rolling 30-day Sharpe < 0.5
- Average net spread after costs < 0.05% for 14 consecutive days
- Bridge exploit loss exceeding 10% of allocated capital
- Drawdown > 15%

## Advantages

- **Structurally persistent edge** -- blockchain fragmentation is an architectural feature, not a temporary inefficiency. As long as multiple chains exist with independent liquidity, cross-chain spreads will emerge
- **Higher margins than single-chain arb** -- bridge costs and risks create wider no-arb bands, meaning larger spreads persist longer than on single-chain DEX arbs
- **Scales with multi-chain expansion** -- every new L2 or alt-L1 launch creates new cross-chain pairs to arb. The Ethereum L2 ecosystem is actively expanding
- **Composable with other strategies** -- cross-chain arb can be combined with [[funding-rate-arbitrage]] (arbing funding rates across perp DEXs on different chains) or [[flash-loan-arbitrage]] (using flash loans on one leg)
- **MEV-resistant on the cross-chain leg** -- unlike single-chain arbs that can be sandwiched, the cross-chain bridging step is harder for MEV bots to front-run (though individual chain legs remain vulnerable)

## Disadvantages

- **Bridge risk is existential** -- $2.5B+ lost to bridge exploits historically. Every bridge interaction is a smart contract risk exposure. See [[2020-2024-bridge-exploits]] and [[smart-contract-risk]]
- **Capital fragmentation** -- must pre-position capital on 5-15+ chains, reducing capital efficiency and increasing operational complexity
- **Infrastructure complexity** -- requires maintaining RPC nodes, WebSocket feeds, bridge integrations, and gas management across multiple heterogeneous blockchains (EVM, SVM, Move, etc.)
- **Latency asymmetry** -- bridge-and-arb mode exposes capital to directional risk during bridge time (seconds to minutes). Price can move against you while funds are in transit
- **Gas cost volatility** -- Ethereum mainnet gas spikes can make L2-to-L1 arbs unprofitable without warning
- **Rebalancing overhead** -- continuous rebalancing of pre-positioned inventory across chains incurs gas and bridge costs that reduce net returns
- **Opaque bridge pricing** -- bridge fees and relayer margins vary dynamically and are not always transparent, making exact cost modeling difficult
- **Fragmented tooling** -- no single dashboard or API covers all chains and bridges. Searchers must build and maintain custom infrastructure

## Comparison to Related Arbitrage Strategies

| Strategy | Venue | Atomic? | Primary Risk | Settlement |
|----------|-------|---------|--------------|------------|
| **Cross-chain arbitrage** | Multiple blockchains | No | Bridge exploit + latency | Seconds–minutes (or 7 days canonical) |
| [[cross-exchange-arbitrage]] | Multiple CEXs | No (internal ledger transfer) | Counterparty / withdrawal halts | Internal transfer |
| [[flash-loan-arbitrage]] | Single chain | **Yes** | Reverts if unprofitable (no loss) | One block |
| [[triangular-arbitrage]] | Single venue | Often atomic | Slippage on legs | One block / one venue |
| [[funding-rate-arbitrage]] | Perp + spot | No | Funding flips, liquidation | Continuous |

The defining distinction: single-chain DEX arbs ([[flash-loan-arbitrage]], [[triangular-arbitrage]]) can be made atomic — they either complete profitably or revert with no principal loss. Cross-chain arb is fundamentally *non-atomic*, which is both the source of its persistent edge (no one can instantly close the spread) and its existential risk (capital is exposed in transit). See [[arbitrage]] for the theoretical foundations.

## Evolution and Key Developments

### Phase 1: Manual CEX-to-DEX (2020-2021)
Early cross-chain arb was manual: buy on a CEX, withdraw to a specific chain, sell on a DEX (or vice versa). The [[2017-2021-kimchi-premium|Kimchi Premium]] was a cross-border variant of this. Withdrawal times (30-60 minutes) and high gas limited profitability.

### Phase 2: Bridge-Native Arb (2021-2023)
The explosion of bridges (Wormhole, Multichain, Synapse, cBridge) enabled on-chain cross-chain arb for the first time. Wrapped tokens (USDC.e, WETH.e) created persistent pricing differences vs native tokens. The era was marred by massive bridge exploits: Ronin ($625M), Wormhole ($325M), Nomad ($190M). See [[2020-2024-bridge-exploits]].

### Phase 3: Intent-Based and Solver Networks (2024-2025)
Intent-based protocols (UniswapX, CoW Protocol, Across) abstracted cross-chain execution. Instead of the user choosing a bridge, solvers competed to fill cross-chain orders at the best price. This simultaneously improved user execution and created a new class of professional solvers who are effectively cross-chain arbitrageurs. The [[2025-defi-renaissance]] saw intent-based trading mature into production.

### Phase 4: Chain Abstraction and AI Agents (2025-2026)
Chain abstraction protocols (Particle Network, NEAR chain signatures, Socket) aim to make cross-chain transactions invisible to users. AI agents ([[ai-trading-agents]], [[ai-mev]]) increasingly operate across multiple chains simultaneously, using reinforcement learning to select optimal bridge routes and arb strategies. Cross-chain MEV is being formally studied as a distinct research domain (ACM measurement study, Sept 2023-Aug 2024). Shared sequencers and real-time L2 finality are beginning to compress the latency window.

## Sources

- General DeFi and cross-chain infrastructure knowledge; bridge exploit data from publicly reported incidents
- Cross-chain MEV research referenced in [[ai-mev]] (Source: [[2026-04-11-perplexity-ai-crypto-gaps]])
- [[layer-2]] — documents L2 scaling and cross-chain arb implications

## Getting the Data (CryptoDataAPI)

CryptoDataAPI serves the per-chain DEX price/depth that defines the gap; bridge rates, latency, and throughput are off-API (native bridge APIs). Chain coverage is Solana/Ethereum/Base/BSC/Arbitrum.

**Live data:**
- `GET /api/v1/dex/token/{chain}/{address}` — per-token price + top pools on each chain; diff the same asset across chains for the gap
- `GET /api/v1/dex/trending` / `GET /api/v1/dex/new-pools` — where cross-chain flow and fresh gaps concentrate
- `GET /api/v1/dex/security/{chain}/{address}` — screening before touching a wrapped/native pair
- `GET /api/v1/liquidity/depth` — depth at 10/25/50/100 bps to size against the thinner-chain pool

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for cross-chain spread research
- DEX is live-only — store `/dex/token` polls to build per-chain price history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/dex/token/base/0x4200000000000000000000000000000000000006"
```

Auth: `X-API-Key` header. Full catalogs: [[cryptodataapi-dex]], [[cryptodataapi-regimes]], [[cryptodataapi-backtesting]].

**Live dashboards:** [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can find and size the gap; bridging stays native:

- **Signal** — `GET /api/v1/dex/token/{chain}/{address}` for the same asset on two chains yields the cross-chain gap; `GET /api/v1/dex/trending` shows where imbalances form. Bridge rates/latency are off-API.
- **Depth + safety** — `GET /api/v1/liquidity/depth` bounds size to the thinner-chain pool; `GET /api/v1/dex/security/{chain}/{address}` gates wrapped-token traps.
- **Regime gate** — `GET /api/v1/liquidity/regime` fragility + `GET /api/v1/security/regime` (bridge-exploit tail — the existential risk of this trade).
- **Backtest** — `GET /api/v1/backtesting/klines` for spread studies; no per-chain reserve archive, so pre-positioned-inventory economics must be modelled from stored polls.
- **Tip** — the pre-positioned (fast) path avoids the bridge fee at execution; size for the thinner chain and respect `new_listing` flags on new-L2 pools.

## Related

- [[cross-exchange-arbitrage]] -- the CEX equivalent; same concept, different infrastructure
- [[flash-loan-arbitrage]] -- atomic single-chain arb; can be combined with cross-chain strategies
- [[triangular-arbitrage]] -- multi-pair arb on a single venue
- [[mev-strategies]] -- on-chain MEV extraction including cross-chain MEV
- [[ai-mev]] -- ML-driven cross-chain MEV research
- [[cross-chain-bridges]] -- the infrastructure that enables cross-chain arb
- [[cctp]] -- Circle's native USDC transfer protocol; key bridge for stablecoin arbs
- [[layer-2]] -- L2 ecosystem creating the fragmentation that drives cross-chain arbs
- [[smart-contract-risk]] -- the primary risk in bridge-based arb
- [[2020-2024-bridge-exploits]] -- historical timeline of bridge exploits
- [[arbitrage]] -- theoretical foundations of arbitrage
