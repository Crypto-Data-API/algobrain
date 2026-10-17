---
title: "Layer 1"
type: concept
created: 2026-07-17
updated: 2026-10-17
status: review
tags: [crypto, blockchain, ethereum, bitcoin]
domain: [market-microstructure, crypto]
difficulty: beginner
---

# Layer 1

A **Layer 1 (L1)** is a base blockchain that settles transactions on its own network, enforces its own consensus rules, and provides its own security — as opposed to a [[layer-2]] network that inherits security from a Layer 1 beneath it. Bitcoin, Ethereum, Solana, and Avalanche are the canonical examples. Every other blockchain product — [[layer-2|Layer 2 rollups]], sidechains, app-chains — either derives security from an L1 or builds its own separate L1 with its own validator set.

## How It Works

An L1 consists of:

1. **A peer-to-peer network** of nodes that propagate transactions and blocks.
2. **A consensus mechanism** that determines which nodes can propose new blocks and how agreement is reached. The two dominant designs are Proof of Work (Bitcoin) and Proof of Stake (Ethereum post-Merge, Solana, Avalanche).
3. **An execution environment** where transactions modify state — Bitcoin uses a minimal scripting language; Ethereum uses the EVM (Ethereum Virtual Machine), which enables arbitrary smart contract logic.
4. **A native token** that pays transaction fees (gas) and, in PoS chains, secures the network via staking.

**Security model:** An L1's security is the cost to attack its consensus. In Proof of Work this is the cost to acquire 51% of hashrate; in Proof of Stake it is the cost to acquire 33%–67% of staked tokens. L1 security is the bedrock that L2s borrow — Ethereum rollups are secure *because* Ethereum L1 is secure.

**Throughput trade-offs:** No L1 has solved the blockchain trilemma — the impossibility of simultaneously maximising decentralisation, security, and scalability. Bitcoin (~7 TPS) prioritises security and decentralisation. Solana (~65,000 theoretical TPS) makes hardware-requirement trade-offs for throughput. Ethereum sits between the two, with most throughput now delegated to [[layer-2|L2 rollups]].

## Concrete Examples

- **Bitcoin (launched 2009):** The original L1. PoW consensus, minimal scripting, ~10-minute blocks. The most decentralised and battle-tested L1; optimised for settlement, not computation.
- **Ethereum (launched 2015; PoS since Sep 2022 "Merge"):** The dominant smart-contract L1. EVM enables DeFi, NFTs, and L2s. ~12-second blocks; most complex execution capability.
- **Solana (mainnet 2020):** High-throughput PoS L1 with sub-second finality and ~$0.001 fees. Different validator hardware requirements and history of partial outages (e.g., September 2021, January 2022).
- **Avalanche (mainnet 2020):** Subnet architecture allowing app-chains with customisable validator sets anchored to the primary Avalanche network.
- **Bitcoin L1 as settlement:** The [[lightning-network]] and the emerging [[babylon-bitcoin-staking-arbitrage|Babylon]] ecosystem treat Bitcoin's L1 as a security layer, building Lightning payment channels and BTC staking on top.

## Trading Relevance

L1 dynamics matter directly to multiple AlgoBrain strategies:

- **[[funding-rate-arbitrage]] and [[basis-trade]]:** L1 native tokens (ETH, SOL, AVAX) are the collateral and the underlying for the largest perpetual futures markets. L1 network upgrades (e.g., Ethereum's EIP-1559, the Merge) have historically been major catalysts for funding rate regime shifts.
- **[[cross-chain-arbitrage]] and [[cross-l2-arbitrage]]:** Price discrepancies between the same asset on different L1s (or between an L1 and its L2s) are the direct source of cross-chain arb edge. Bridging latency and L1 finality times are key risk inputs.
- **[[on-chain-analysis]] and [[on-chain-flow-trading]]:** L1 blockchains expose settlement data transparently — exchange flows, large wallet movements, MVRV, and staking yields are all L1-sourced on-chain signals.
- **[[jito-solana-mev-arbitrage]] and [[mev-strategies]]:** MEV is L1-specific. Ethereum's PBS (Proposer-Builder Separation) via [[flashbots]] and Solana's Jito Block Engine are different L1 MEV architectures. Understanding which L1 you operate on determines the MEV toolchain. See [[mev]].

### Trading L1 tokens as a sector

L1 native tokens are also the largest *directional* sector after BTC itself, and several AlgoBrain strategies trade them as a group rather than as infrastructure:

- **Sector basket:** [[l1-blockchains-basket]] holds alt-L1 perps as a group; [[solana-ecosystem-basket]] isolates the Solana beta. Both are high-beta to BTC — an alt-L1 sleeve is a leveraged BTC bet unless it is hedged.
- **Relative value:** [[cross-sectional-relative-value]] and [[pairs-trading]] rank L1s against each other (e.g. long the strongest-momentum L1, short the weakest) to strip out the common crypto beta.
- **Supply events:** newer L1s (launched 2020+) typically carry large insider and foundation allocations on vesting schedules. [[unlock-aware-momentum]] and [[token-unlock-supply-event]] trade the dated cliffs; see [[token-unlocks]].
- **App-specific L1s:** [[hyperliquid]] runs its own L1 (HyperCore order books plus HyperEVM), so its token economics and outage risk are L1 risks, not L2 risks. When choosing a venue, chain halts and validator concentration count as counterparty risk.
- **Outage risk:** L1 halts (Solana's September 2021 and January 2022 incidents above) freeze on-chain collateral and bridges. Any strategy holding on-chain collateral on a single L1 should size for a multi-hour halt.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/coins/category-groups` — curated themes including a Layer-1 / platform group, with each member's price, market cap, rank and 24h/7d change
- `GET /api/v1/coins/{symbol}` — per-coin market data (e.g. `/api/v1/coins/SOL`)
- `GET /api/v1/supply/unlocks?symbol=SUI` — forward vesting-cliff calendar, sized against float (a cliff calendar, not an emissions feed)
- `GET /api/v1/market-health/altcoin-breadth` — share of alts above their moving average, a check on whether an alt-L1 rally is broad

**Historical data:**
- `GET /api/v1/backtesting/klines?symbol=SOLUSDT&interval=1d&start=2021-01-01` — Binance OHLCV for L1 relative-value backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/coins/category-groups"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-coins]], [[cryptodataapi-supply]], [[cryptodataapi-backtesting]].

## Related

- [[layer-2]] — networks that borrow L1 security (rollups, state channels)
- [[ethereum]] — the dominant smart-contract L1
- [[solana]] — the dominant high-throughput L1
- [[bitcoin]] — the original PoW L1
- [[blockchain]] — the underlying data structure
- [[proof-of-stake]] — the consensus mechanism of most modern L1s
- [[cross-chain-arbitrage]] — arbitrage across L1 price differences
- [[mev-strategies]] — L1-specific block-ordering value
- [[layer-2]] — the scaling layer that competes with L1 throughput improvements

## Sources

- General blockchain/crypto knowledge; no specific wiki source ingested yet.
