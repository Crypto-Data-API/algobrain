---
title: "PumpSwap"
type: entity
created: 2026-05-04
updated: 2026-06-12
status: draft
tags: [crypto, defi, solana, sniping, memecoin]
aliases: ["Pump.fun DEX", "PumpSwap DEX"]
entity_type: exchange
headquarters: "Decentralized"
website: "https://pump.fun"
related: ["[[pump-fun]]", "[[raydium]]", "[[solana]]", "[[token-migration-sniping]]", "[[memecoin-sniping]]", "[[jupiter-exchange-solana]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# PumpSwap

**PumpSwap** is the native decentralized exchange built by [[pump-fun]] for memecoins that have completed (graduated from) the bonding curve phase. Launched in late 2025, it serves as an alternative migration endpoint to [[raydium]] for tokens that hit the ~$69k market cap graduation threshold, keeping post-bond liquidity within the Pump.fun ecosystem instead of routing it to external Solana AMMs.

---

## Overview

When a memecoin launches on [[pump-fun]], it trades on a deterministic bonding curve until it reaches a market cap of roughly $69,000. At that point, the token "graduates" and its liquidity is migrated to a full automated market maker (AMM) pool. Historically that migration target was [[raydium]]. With the launch of PumpSwap, Pump.fun captures the migration step itself, providing a vertically integrated path from launch to post-graduation trading.

For traders, this matters because the graduation event is one of the most volatile and profitable moments in a memecoin's life cycle -- liquidity deepens, listings cascade across aggregators like [[jupiter-exchange-solana]], and price discovery accelerates. PumpSwap shifts where that liquidity lands, creating new venue-level dynamics for [[token-migration-sniping]] and short-term arbitrage between PumpSwap and [[raydium]] pools.

---

## Key Features

### Native Pump.fun Integration
- **Direct migration:** Tokens move from the bonding curve to a PumpSwap pool without an external AMM intermediary
- **Lower friction:** No third-party listing step -- trading is live the moment a token graduates
- **Unified UX:** Pump.fun's launch UI and PumpSwap's swap UI share the same ecosystem, reducing context-switching for retail traders

### Solana-Native AMM
- Built on [[solana]] for sub-second confirmation and low transaction fees
- Standard constant-product AMM mechanics for graduated memecoin pools
- Liquidity is seeded from the proceeds of the bonding curve at the moment of graduation

### Aggregator Routing
- Pools become routable through Solana DEX aggregators including [[jupiter-exchange-solana]], so end users may trade PumpSwap liquidity without knowing it
- This means swap volume on PumpSwap is amplified by aggregator-level order flow, not just direct UI users

---

## Pricing & Access

- **Trading fees:** Standard AMM swap fee paid by takers; specific bps schedule subject to Pump.fun's published parameters
- **Listing cost:** Free -- listing is automatic upon bonding curve completion. There is no separate listing fee or application
- **Wallet:** Any Solana wallet (Phantom, Solflare, Backpack) can interact via the Pump.fun UI or via aggregators
- **API access:** On-chain data is available via Solana RPC and via third-party indexers such as [[bitquery]] (which has dedicated Pump.fun and PumpSwap endpoints)

---

## Use Cases for Traders

- **Migration sniping:** Bots and manual traders watch the bonding curve approaching ~$69k MC and submit buys timed to the migration block on PumpSwap to capture the post-bond price expansion (see [[token-migration-sniping]])
- **Cross-venue arbitrage:** When a token is briefly listed on both PumpSwap and [[raydium]] (or via aggregator routing), short-lived spreads can be arbitraged
- **Post-graduation momentum trading:** Once a token has migrated, market-cap-level support/resistance trading (see [[memecoin-sniping]]) plays out on PumpSwap pools
- **Liquidity monitoring:** Tracking PumpSwap pool depth and liquidity changes is a leading signal for rug pulls or whale exits on graduated tokens
- **Volume signal:** Volume spikes on PumpSwap shortly after graduation are a common early signal of viral momentum

---

## Limitations

- **New venue:** Launched late 2025; less battle-tested than [[raydium]] which has years of audit history and incident data
- **Concentrated ecosystem risk:** Tying launch and post-launch liquidity to a single ecosystem (Pump.fun + PumpSwap) means a Pump.fun protocol issue can cascade
- **Limited to graduated memecoins:** Not a general-purpose DEX -- the asset universe is largely Pump.fun graduates, which are overwhelmingly speculative memecoins with extreme rug rates
- **Liquidity fragmentation:** Splitting graduations between PumpSwap and [[raydium]] can fragment liquidity for the same token across two venues, widening effective spreads when not aggregated
- **Regulatory exposure:** Memecoin venues face evolving regulatory scrutiny; jurisdiction-specific access restrictions may apply

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]])
- Bitquery Pump.fun API documentation (referenced in source)

---

## Related

- [[pump-fun]] -- the launchpad that feeds PumpSwap
- [[raydium]] -- the historical migration target and primary competitor venue for graduated tokens
- [[solana]] -- the underlying chain
- [[jupiter-exchange-solana]] -- aggregator that routes through PumpSwap pools
- [[token-migration-sniping]] -- core trading strategy around the bonding curve graduation event
- [[memecoin-sniping]] -- broader strategy family that PumpSwap fits into
- [[bitquery]] -- data provider with dedicated PumpSwap / Pump.fun endpoints
