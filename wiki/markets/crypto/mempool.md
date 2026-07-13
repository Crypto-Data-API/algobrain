---
title: "Mempool"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [crypto, market-microstructure, mev]
aliases: ["Memory Pool"]
domain: [crypto, market-microstructure]
difficulty: intermediate
related: ["[[flashbots]]", "[[mev]]", "[[mev-strategies]]", "[[gas-fees]]", "[[ethereum]]", "[[bitcoin]]"]
---

The mempool (short for "memory pool") is a waiting area for unconfirmed transactions on a blockchain network. When a user broadcasts a transaction, it enters the mempool where it sits until a validator (or miner) includes it in a block. The mempool is central to understanding [[mev|MEV]], transaction ordering, and blockchain [[market-microstructure]]. It is best understood as a blockchain's **order book for block space**: pending transactions bid (via fees) for a scarce resource — inclusion in the next block — and the public visibility of those bids is what makes on-chain front-running possible.

## How the Mempool Works

1. **User submits transaction**: A signed transaction is broadcast to the network
2. **Propagation**: The transaction propagates across nodes, each maintaining their own local mempool
3. **Waiting**: The transaction sits in the mempool, visible to all nodes, until selected for inclusion in a block
4. **Inclusion**: A validator selects transactions from the mempool (typically prioritized by gas price / fee) and includes them in a new block
5. **Confirmation**: Once the block is added to the chain, the transaction is confirmed and removed from the mempool

### Key Properties
- **Public by default**: On most networks, pending transactions in the mempool are visible to anyone running a node
- **Not guaranteed**: Transactions can be dropped from the mempool if they sit too long or if the mempool becomes congested
- **Replaceable**: On [[ethereum|Ethereum]], users can replace a pending transaction by submitting a new one with the same nonce but higher gas price (Replace-By-Fee / RBF)
- **Local variation**: Each node maintains its own mempool, so not all nodes see exactly the same pending transactions at the same time

## The Fee Market

The mempool is where the **fee market** clears. Because block space is finite, transactions compete on price, and how that price is set differs by chain:

| Mechanism | Chain(s) | How it works |
|-----------|----------|--------------|
| **Pure first-price auction** | Pre-2021 Ethereum, Bitcoin | Users bid a fee; highest bidders included first; overpay risk is high |
| **EIP-1559 base fee + tip** | Ethereum (post-Aug 2021) | A protocol-set **base fee** (burned) adjusts up/down per block to target ~50% fullness; users add a **priority fee** (tip) to validators to jump the queue |
| **Fee rate (sat/vByte)** | Bitcoin | Fee per byte of transaction size; miners pack highest-rate txs first |
| **Local fee markets** | Solana | Per-account priority fees so congestion on one program does not price out the whole chain |

Under EIP-1559 the base fee is the floor everyone pays and the **priority fee is what actually orders transactions within a block** — which is precisely the lever [[mev|MEV]] searchers pull when racing to front-run. See [[gas-fees]] for the full fee mechanics. When the mempool is congested, the base fee rises and marginal users get priced out until demand falls — a continuous, on-chain congestion-pricing loop.

## Mempool and MEV

The public visibility of the mempool is the foundation of [[mev|MEV extraction]] — see the [[mev]] page for the full taxonomy and the [[flashbots]] page for the infrastructure built to mitigate it:

### Front-Running
MEV searchers monitor the mempool for profitable opportunities:
- A large buy order on a [[defi|DEX]] is detected in the mempool
- A searcher submits the same buy order with a higher gas price, getting included before the victim's transaction
- The searcher profits from the price movement caused by the original trade

### Sandwich Attacks
A more sophisticated form of MEV:
1. **Front-run**: Searcher buys the asset before the victim's large purchase
2. **Victim trade**: The victim's buy pushes the price higher
3. **Back-run**: Searcher immediately sells at the higher price

The victim gets worse execution, and the searcher captures the price impact as profit. [[flashbots|Flashbots]] estimates millions of dollars in daily sandwich attack volume on Ethereum.

### Liquidation Hunting
Monitoring for transactions that will trigger [[liquidation|liquidation]] events on [[defi-lending|DeFi lending]] protocols, then front-running the liquidation to claim the collateral discount.

## Private Mempools and Protection

The problems created by public mempools have driven innovation in transaction privacy:

### Flashbots Protect
[[flashbots|Flashbots Protect]] allows users to submit transactions directly to block builders, bypassing the public mempool entirely. Transactions are invisible to searchers until included in a block, preventing front-running and sandwich attacks.

### Private RPCs
Several services offer private transaction submission:
- MEV Blocker (by CoW Protocol)
- Blocknative
- Various exchange-specific private relayers

### Encrypted Mempools
Emerging research into encrypting mempool transactions so that searchers cannot read transaction content until after ordering has been finalized. Projects like Shutter Network and Threshold Encryption are exploring this approach.

## Bitcoin Mempool

The [[bitcoin|Bitcoin]] mempool operates differently from Ethereum's:
- Transactions are prioritized by fee rate (satoshis per byte)
- No smart contract execution, so MEV is more limited (though some forms exist via RBF sniping)
- Mempool congestion directly affects transaction confirmation times and fees
- Mempool visualization tools (mempool.space) help users estimate appropriate fee rates

## Mempool as a Data Source

For traders and analysts, the live mempool is itself a real-time information feed, not just plumbing:

- **Pending DEX swaps** reveal imminent buy/sell pressure before it confirms — the same data MEV bots exploit can inform short-horizon flow reads.
- **Stablecoin mints/burns and large transfers** appearing in the mempool can front-run on-chain reporting of [[exchange-flows|exchange flows]].
- **Gas spikes** (a surge of high-tip transactions) often coincide with NFT mints, liquidations, or volatile market events — a congestion signal.
- **Stuck-transaction backlog** (large queue of low-fee txs) signals network stress that can delay one's own execution.

Tools like mempool.space (Bitcoin), Etherscan's pending view, Blocknative's mempool API, and EigenPhi/MEV dashboards expose this data.

## Trading Implications

- **Transaction timing**: Monitoring mempool congestion helps traders time transactions for lower [[gas-fees|gas fees]] — submitting during low-base-fee windows can save materially on cost.
- **MEV awareness**: DeFi traders must account for [[mev|MEV]] as a hidden cost; large swaps on public mempools will likely be sandwiched unless protected.
- **Slippage and protection**: Setting tight slippage limits and routing through private RPCs / [[flashbots|Flashbots Protect]] are the standard defences against mempool-based extraction.
- **Strategy design**: Sophisticated crypto strategies use private transaction channels and MEV-aware routing to minimize value extraction; latency to well-connected nodes can be an edge for arbitrage.
- **Block space as a market**: The mempool represents demand for block space; analyzing mempool dynamics provides insight into network activity and user behavior.

## Related

- [[mev]] -- The extractable value the public mempool makes possible
- [[flashbots]] -- Infrastructure for mitigating negative MEV via private transaction submission
- [[mev-strategies]] -- Trading strategies that exploit mempool visibility
- [[gas-fees]] -- Fees are set in the mempool fee market and track congestion
- [[ethereum]] -- The primary network where mempool-based MEV occurs
- [[bitcoin]] -- A simpler, fee-rate-driven mempool with limited MEV
- [[market-microstructure]] -- the mempool is crypto's order book for block space

## Sources

- Mempool mechanics are documented in Ethereum and Bitcoin protocol specifications and Flashbots research
- General market knowledge; no specific wiki source ingested yet.
