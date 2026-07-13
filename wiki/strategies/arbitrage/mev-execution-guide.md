---
title: "MEV Execution Guide"
type: strategy
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [arbitrage, crypto, defi, execution, algorithmic, market-microstructure]
aliases: ["MEV Guide", "Flashbots Guide", "MEV Protection"]
strategy_type: algorithmic
timeframe: scalp
markets: [crypto, defi]
complexity: advanced
backtest_status: untested
edge_source: [latency, structural, informational]
edge_mechanism: "Block-ordering rights are auctioned to whoever pays builders the most. A searcher with faster detection, atomic execution, and private orderflow captures price discrepancies that arrive and vanish within a single block."
crowding_risk: high
related: ["[[mev-strategies]]", "[[mev]]", "[[flash-loan-arbitrage]]", "[[gas-fees]]", "[[flashbots]]", "[[defi-contract-registry]]", "[[cross-chain-arbitrage]]", "[[leg-risk]]", "[[arbitrage-parameter-cheatsheet]]", "[[liquidation-cascade-arbitrage]]", "[[stablecoin-pair-arbitrage]]"]
---

# MEV Execution Guide

[[mev-strategies]] describes *what* MEV (Maximal Extractable Value) is and the strategies that capture it. This page covers **how to actually execute** — Flashbots bundle construction, gas bidding strategy, MEV protection, mempool monitoring, and the operational infrastructure for running MEV-aware arbitrage. It is the execution layer beneath strategies like [[liquidation-cascade-arbitrage]] (which submits liquidations via bundles) and on-chain legs of [[stablecoin-pair-arbitrage]] and [[cross-chain-arbitrage]].

## Edge Source

**Latency** + **structural** + **informational** (see [[edge-taxonomy]]).

- **Latency:** Post-merge Ethereum auctions block-ordering rights via [[flashbots]]-style relays. The searcher who detects an opportunity and lands a bundle first wins it outright; everyone else's transaction reverts or arrives too late. Edge is measured in milliseconds and block positions.
- **Structural:** The MEV supply chain (searcher → builder → proposer) is a *designed* market. Builders run an open auction for inclusion; paying the highest priority fee is a structural, repeatable way to buy ordering — not a hidden exploit.
- **Informational:** The public mempool broadcasts pending intent. A searcher who decodes pending swaps, liquidations, and pool creations faster than rivals sees the opportunity before it settles on-chain.

## Why This Edge Exists

Blockchains order transactions discretely, one block at a time, and the right to order them is economically valuable. Three frictions sustain the edge: (1) most users broadcast to the public mempool, leaking their intent; (2) AMM price impact is deterministic and computable, so the profit of a back-run or sandwich is known in advance; and (3) inclusion is a pay-to-play auction, so capital-and-infrastructure-rich searchers can reliably outbid casual participants. The "other side" is the ordinary user whose swap moves a pool, the lending protocol that must pay a liquidation bonus, and slower searchers who lose the race. They keep losing because they either cannot see the opportunity in time or cannot pay enough to be ordered first.

## Null Hypothesis

If block-ordering were random and the mempool were fully private, expected MEV per searcher would equal the builder bid plus gas — i.e., zero net edge, with profits competed away. The observed reality (a small set of dominant searchers earning persistent positive net MEV, documented by [[flashbots]] and EigenPhi) rejects that null: latency and infrastructure create a durable, concentrated edge for the fastest operators.

## The MEV Supply Chain

Understanding the MEV supply chain is essential for knowing where your arb fits:

```
Opportunity → Searcher → Builder → Validator/Proposer → Block
```

| Role | What They Do | How You Interact |
|---|---|---|
| **Searcher** (you) | Detect arb opportunities, construct profitable transactions | Write detection + execution code |
| **Builder** | Assemble transactions into blocks, maximizing total MEV | Submit bundles via Flashbots or direct builder APIs |
| **Validator/Proposer** | Propose the block to the network | You don't interact directly — the builder does |
| **Relay** | Connects builders to proposers, mediates trust | Submit through relay APIs (Flashbots, bloXroute, etc.) |

As a searcher, you submit **bundles** (ordered groups of transactions) to builders. The builder includes your bundle if it's profitable for them (you share some MEV as a "bribe").

## Flashbots Bundle Submission

### Setup

1. **Get an RPC endpoint:** Use Flashbots Protect RPC (`https://rpc.flashbots.net`) for MEV-protected transactions, or the bundle relay (`https://relay.flashbots.net`) for submitting bundles
2. **Create a signing key:** Bundles are signed with an Ethereum private key that identifies you as a searcher. This is NOT the key that holds your funds
3. **Install client library:** `pip install flashbots` (Python) or `@flashbots/ethers-provider-bundle` (JavaScript)

### Bundle Structure

A bundle is an array of signed transactions with a target block number:

```python
from flashbots import flashbot
from eth_account import Account
from web3 import Web3

# Setup
w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY"))
signer = Account.from_key("YOUR_SEARCHER_PRIVATE_KEY")
flashbot(w3, signer)

# Construct bundle
bundle = [
    {
        "signed_transaction": signed_tx_1.rawTransaction,  # Your arb tx
    },
    {
        "signed_transaction": signed_tx_2.rawTransaction,  # Optional: follow-up tx
    }
]

# Submit for next block
result = w3.flashbots.send_bundle(
    bundle,
    target_block_number=w3.eth.block_number + 1,
)
```

### Key Parameters

| Parameter | Recommended Value | Why |
|---|---|---|
| **Target block** | `current_block + 1` (or +2 for latency buffer) | Submit for the next block. Too far ahead and the opportunity may be gone |
| **Max timestamp** | `current_time + 120` seconds | Bundle expires after 2 minutes if not included |
| **Reverting tx handling** | `False` (do NOT allow revert) | If your arb reverts, you want the entire bundle dropped — no wasted gas |

### Gas Bidding Strategy

You must pay the builder enough to include your bundle over competing searchers. The payment is the **priority fee** (tip) on your transactions.

**How much to bid:**
```
optimal_bid = arb_profit × bid_percentage
```

| Strategy | Bid % of Profit | Rationale |
|---|---|---|
| **Conservative** | 90-95% | Maximize inclusion rate. You keep only 5-10% but land more bundles |
| **Moderate** | 70-80% | Balance between inclusion and profit retention |
| **Aggressive** | 50-60% | Keep more profit but risk being outbid. Only viable if competition is low |

**Industry norm (2026):** Top searchers bid 90%+ of profit to builders. The MEV market is highly competitive — builders choose the highest-paying bundles.

**Coinbase builder (direct):** Coinbase's builder accepts bundles directly and typically requires lower bids than Flashbots relay because of less competition. Submit via `https://builder-relay.coinbase.com`.

## MEV Protection (When You're the Target)

If you're executing on-chain arbs via the public mempool (not Flashbots), you're vulnerable to **sandwich attacks**:

```
1. Bot detects your pending swap in mempool
2. Bot front-runs: buys the token before you, pushing price up
3. Your swap executes at worse price
4. Bot back-runs: sells the token after you, profiting from the price impact you caused
```

### Protection Methods

| Method | How It Works | Cost | Effectiveness |
|---|---|---|---|
| **Flashbots Protect RPC** | Transactions go to Flashbots-affiliated builders, skipping public mempool | Free | High — transactions not visible to public mempool searchers |
| **MEV-Share** | You share MEV with searchers in a controlled way (you get a kickback) | Share 50-90% of MEV | High — aligned incentives |
| **Private mempool (bloXroute)** | Transactions sent to bloXroute's private network | Paid (subscription) | High — limited visibility |
| **Slippage tolerance** | Set tight slippage (0.1-0.5%) so sandwiches are unprofitable | Free | Moderate — sandwicher may still profit within your tolerance |
| **Split transactions** | Break large swaps into multiple smaller ones | Higher gas cost | Moderate — each piece has less impact to sandwich |

**Recommendation for arb bots:** Always submit through Flashbots bundles (not raw transactions to mempool). This eliminates sandwich risk entirely because your transactions are never publicly visible.

## Mempool Monitoring

To find arb opportunities, monitor pending transactions in the public mempool:

### What to Monitor

| Signal | What It Reveals | Arb Opportunity |
|---|---|---|
| **Large pending swap** | Someone is about to move a DEX pool's price | Back-run: execute your arb after their swap moves the price |
| **Liquidation trigger** | A position is about to be liquidated | Liquidation arb: compete to liquidate and capture the bonus |
| **New pool creation** | New liquidity is being added to a DEX | Sniping: buy early in the new pool before price discovery |
| **Bridge deposit** | Large capital moving cross-chain | Cross-chain arb: anticipate price impact on destination chain |

### Monitoring Setup

```python
# Subscribe to pending transactions via WebSocket
import asyncio
from web3 import Web3

w3 = Web3(Web3.WebsocketProvider("wss://eth-mainnet.g.alchemy.com/v2/YOUR_KEY"))

async def monitor_mempool():
    pending_filter = w3.eth.filter("pending")
    while True:
        pending_txs = pending_filter.get_new_entries()
        for tx_hash in pending_txs:
            tx = w3.eth.get_transaction(tx_hash)
            # Decode tx.input to identify swap operations
            # Check if profitable to back-run
            if is_profitable_backrun(tx):
                submit_bundle(my_arb_tx, target_block=tx.blockNumber)
```

### Monitoring Tools

| Tool | Purpose | Cost |
|---|---|---|
| **Alchemy / QuickNode (Websocket)** | Pending transaction stream | $50-300/mo |
| **EigenPhi** | MEV transaction analysis and profit visualization | Free dashboard |
| **Flashbots MEV-Inspect** | Open-source MEV analysis tool | Free (self-hosted) |
| **Dune Analytics** | Historical MEV data queries | Free-$350/mo |
| **Custom RPC node** (Geth/Reth) | Direct mempool access, lowest latency | $200-500/mo (hardware) |

## Profitability Decision Framework

Before submitting any MEV bundle:

```
1. Detect opportunity (spread, liquidation, backrun)
2. Estimate gross profit: profit = output_tokens - input_tokens
3. Estimate gas cost: gas = gas_units × estimated_gas_price
4. Estimate builder bid: bid = gross_profit × bid_percentage (typically 90%)
5. Calculate net profit: net = gross_profit - gas - bid
6. Decision:
   if net > min_profit_threshold:
       submit_bundle()
   else:
       skip()  # Not worth the operational overhead
```

**Minimum profit thresholds (practical):**

| Chain | Min Gross Profit to Bother | Min Net Profit | Rationale |
|---|---|---|---|
| Ethereum mainnet | > $50 | > $5 | Gas + bid consume most; only large arbs viable |
| Arbitrum | > $1 | > $0.10 | Much cheaper gas; smaller arbs viable |
| Base | > $0.50 | > $0.05 | Cheapest EVM L2 |
| Solana | > $0.10 | > $0.01 | Near-zero gas; micro-arbs viable |

## Common Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| **Bundle not included** | Bid too low; competing searcher outbid you | Increase bid %. If consistently outbid, the arb is too competitive |
| **Transaction reverts** | Price moved between detection and execution | Tighten timing; use Flashbots (no gas cost for reverts) |
| **Stale opportunity** | By the time you submit, someone else took the arb | Improve detection speed; use dedicated RPC with lower latency |
| **Incorrect gas estimation** | Under-estimated gas → tx runs out of gas | Always add 20% gas buffer; use `eth_estimateGas` with exact calldata |
| **Front-run by builder** | The builder itself copies your strategy and executes it | Use trusted builders (Flashbots, Titan); avoid sharing strategy details in tx calldata |

## Performance Characteristics (cost-aware)

MEV economics are dominated by costs, not gross spread. The decision framework above exists precisely because gas plus the builder bid typically consume the large majority of gross profit. No fabricated return figures are given here — realized P&L depends entirely on competition, chain, and infrastructure latency, all of which vary continuously.

| Cost component | Where it lands | Notes |
|---|---|---|
| **Gas** | Paid regardless of inclusion strategy | Use Flashbots so reverts cost nothing |
| **Builder bid (priority fee)** | The dominant cost — often 90%+ of gross | Higher bid = higher inclusion, lower retention |
| **Infrastructure** | Fixed overhead (RPC node, indexers, co-lo) | $200–500/mo+ for a competitive node |
| **Failed-race gas** | Lost when outbid after public submission | Eliminated by private bundles |
| **Opportunity cost** | Capital locked for atomic legs | Mitigated by flash loans ([[flash-loan-arbitrage]]) |

Net edge is the small residual after these. The realistic per-chain minimum-profit thresholds in the [Profitability Decision Framework](#profitability-decision-framework) reflect that residual: on Ethereum mainnet only large arbs clear; on cheap L2s and Solana, micro-arbs become viable.

## Capacity Limits

- **Per-opportunity capacity** is bounded by the size of the underlying inefficiency (the swap being back-run, the position being liquidated) and the DEX depth available to execute against — not by the searcher's capital, since atomic flash-loan execution needs none.
- **Strategy-wide capacity** is bounded by the *number* of opportunities and the searcher's win rate against rivals. More capital does not buy more wins; faster detection and higher bids do.
- **Crowding is high.** A small set of dominant searchers captures most flow on Ethereum mainnet. Capacity for a *new* entrant is effectively the long tail of opportunities the incumbents miss, plus less-contested chains (newer L2s, app-chains).

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

- **Losing the latency race** — incumbents with lower-latency RPC, co-located nodes, and direct builder integrations win consistently; a slower entrant's bundles never land.
- **Bid compression to zero edge** — as competition intensifies, builders extract nearly all profit via the bid, leaving no residual.
- **Encrypted/private mempools** — SUAVE, Shutter, and threshold encryption erode the *informational* edge by hiding pending intent.
- **Protocol-internal capture** — liquidator vaults and protocol-owned ordering remove flow before external searchers can act (see [[liquidation-cascade-arbitrage]]).
- **Builder/relay trust failure** — a builder front-running or unbundling your transactions destroys the assumption that submission is safe.

## Kill Criteria

- Bundle inclusion rate falls below the level where infrastructure cost exceeds net MEV for 30 consecutive days.
- Median net profit per landed bundle drops below the gas-plus-overhead breakeven for the target chain.
- Failed/reverted submission rate via private bundles exceeds a level indicating chronic loss of races (sustained, not transient).
- A target venue introduces protocol-internal ordering or liquidator capture that removes the addressable flow.

## Advantages

- **Atomic execution** — bundles either land profitably or revert at no cost (when using Flashbots), eliminating leg risk and sandwich exposure.
- **No directional market risk** — pure arb/back-run profit is independent of market direction.
- **Capital-light** — flash loans ([[flash-loan-arbitrage]]) remove the need for large standing inventory.
- **Clearly defined economics** — gross profit and builder bid are computable before submission.

## Disadvantages

- **Extreme competition and crowding** — a few dominant searchers capture most flow.
- **Latency arms race** — competitive operation requires custom nodes, co-location, and direct builder relationships.
- **Smart-contract risk** — a bug in the searcher's execution contract can drain it.
- **Builder/relay counterparty risk** — reliance on trusted builders not to front-run.
- **Eroding edge** — private mempools and protocol-internal capture shrink the addressable opportunity over time.

## Sources

- [[mev-strategies]]
- [[flash-loan-arbitrage]]
- [[gas-fees]]
- [[flashbots]]
- [[defi-contract-registry]]
- Flashbots documentation (docs.flashbots.net)
- EigenPhi (eigenphi.io)
- General market knowledge; no specific wiki source ingested yet.

## Related

- [[mev]] — what MEV is, conceptually
- [[mev-strategies]] — the parent catalog of MEV strategies
- [[flash-loan-arbitrage]] — capital-free funding for atomic MEV legs
- [[liquidation-cascade-arbitrage]] — a primary MEV strategy that submits via bundles
- [[stablecoin-pair-arbitrage]] — on-chain legs can route through Flashbots
- [[cross-chain-arbitrage]] — multi-chain execution with MEV exposure
- [[gas-fees]], [[flashbots]], [[defi-contract-registry]]
- [[leg-risk]] — what atomic bundles eliminate
- [[arbitrage-parameter-cheatsheet]] — thresholds and parameters
- [[edge-taxonomy]], [[failure-modes]]
