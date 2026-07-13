---
title: "dYdX"
type: entity
created: 2026-04-06
updated: 2026-06-10
status: good
tags: [crypto, defi, exchange, futures, derivatives]
entity_type: exchange
founded: 2017
website: "https://dydx.exchange"
aliases: ["DYDX", "dYdX Chain"]
related: ["[[decentralized-exchanges]]", "[[perpetual-futures]]", "[[defi]]", "[[hyperliquid]]", "[[gmx]]", "[[binance]]", "[[crypto-perp-backtesting-pitfalls]]", "[[ccxt]]"]
---

# dYdX

**dYdX** is a decentralized [[perpetual-futures|perpetual futures]] exchange and one of the pioneering platforms for on-chain derivatives trading. Originally built on [[ethereum]] (using StarkEx L2), dYdX migrated to its own **dYdX Chain** -- a sovereign Layer 1 blockchain built on Cosmos SDK -- to achieve fully decentralized order book matching and higher throughput.

---

## Key Features

| Feature | Detail |
|---|---|
| **Architecture** | Own L1 chain (dYdX Chain, Cosmos-based) |
| **Order Type** | Central limit order book (CLOB) -- not an AMM |
| **Markets** | 100+ perpetual futures pairs |
| **Leverage** | Up to 20x on major pairs |
| **Token** | DYDX -- governance and staking on dYdX Chain |
| **Fee Model** | Maker/taker fee structure; staking DYDX provides fee discounts |

---

## dYdX Chain Migration

The move from an Ethereum L2 to a sovereign Cosmos chain was significant:
- **Full decentralization** -- validators run the order book matching engine, removing any centralized sequencer
- **Customization** -- dedicated block space for trading; no competition with unrelated transactions
- **Revenue distribution** -- trading fees flow to DYDX stakers rather than to Ethereum validators

This migration positioned dYdX as arguably the most decentralized derivatives exchange in operation.

---

## 2025-2026 Market Position

dYdX was the first mover and, through its StarkEx-era v3, the dominant on-chain perpetuals venue. That leadership did **not** survive the rise of [[hyperliquid|Hyperliquid]]. By H1 2025 Hyperliquid held the large majority of decentralized perpetual volume (~73% of DEX perp share per BitMEX's 2025 state-of-perps review, cited on [[crypto-perp-backtesting-pitfalls]]), leaving dYdX, [[gmx|GMX]], and newer entrants competing for the remainder. The decentralized-perp segment as a whole remained a single-digit percentage of centralized-venue volume, so [[binance|Binance]], Bybit, and OKX still set the benchmark for liquidity, funding, and price discovery.

dYdX's architectural bet (a sovereign Cosmos CLOB chain) is the cleanest decentralization story among major perp DEXs, but Hyperliquid's tighter spreads, deeper books, hourly funding, and aggressive listing cadence drew the marginal taker flow. By August 2025 Hyperliquid held roughly 70-80% of decentralized perp market share with $350B+ monthly volume and $1.5T+ cumulative volume, versus dYdX's ~$1.46T cumulative since 2021. For a trader, dYdX remains relevant primarily as a **comparator venue** for DEX perp design and as a cross-venue reference for basis and lead-lag work.

### Key numbers and events

- **2024 activity**: ~$270B trading volume and ~$46M net protocol fees across 150+ markets; cumulative volume passed **$1.46 trillion** since 2021.
- **dYdX Unlimited** (November 2024): permissionless market listings plus **MegaVault**, a protocol-owned liquidity vault that seeds new markets; part of the response to Hyperliquid's listing cadence.
- **October 2024**: dYdX Trading cut roughly a third of staff and founder Antonio Juliano returned as CEO — a signal of how hard the competitive environment had become.
- **DYDX buyback program** (March 2025): the first-ever DYDX buyback allocated **25% of protocol fees** to repurchasing DYDX, with bought-back tokens restaked to secure the chain; over **5 million DYDX** repurchased by late 2025.
- **Buyback escalation (late 2025)**: governance raised the buyback allocation from 25% to **75% of protocol revenue**, and a community-proposed *experimental* program ran **November 2025 - January 2026** directing **100% of net fees** to buybacks.
- dYdX has also broadened beyond perps toward a multi-asset trading hub (spot, EVM support on dYdX Chain) through 2025-2026.

---

## Backtesting Relevance

dYdX is a useful venue to *study*, but its differences from Hyperliquid and the CEXs matter for any low-timeframe backtest:

- **CLOB, not an AMM.** Unlike [[gmx|GMX]]'s pool/oracle model, dYdX matches on a central limit order book, so [[intrabar-fill-modeling|intrabar fill]] and queue-position logic apply much as they do on a CEX -- maker fills depend on price trading through your level *and* the queue ahead clearing, not on price merely touching it.
- **Data access.** Historical and live data come from the dYdX indexer API (and via aggregators such as [[ccxt|CCXT]]). Survivorship matters: markets listed and delisted across the v3 (StarkEx) and v4 (dYdX Chain) eras must be reassembled to avoid a [[crypto-perp-backtesting-pitfalls|survivorship-biased]] universe.
- **Funding cadence.** dYdX uses its own funding mechanism; align funding accrual to the venue's actual cycle when modelling holds, rather than copying Hyperliquid's hourly or a CEX 8h assumption. See [[crypto-perp-backtesting-pitfalls]].
- **Cross-venue divergence.** Because dYdX liquidity is thinner than the majors, a strategy backtested on dYdX fills is not portable to Binance fills and vice versa -- single-venue results are venue-specific, not strategy-specific. This is the single-venue-assumption pitfall.

---

## Trading Relevance

- dYdX was a first mover in decentralized perps, proving that complex derivatives trading could work on-chain
- Competes directly with [[hyperliquid]] and [[gmx]] for decentralized perps market share
- DYDX token is a proxy bet on DEX derivatives volume growth — and since 2025 a direct claim on protocol revenue via the 75%-of-revenue buyback-and-stake program, making fee trends the primary token driver
- The Cosmos-based architecture means dYdX operates independently from Ethereum ecosystem dynamics
- Buyback-rate changes (25% → 75% → experimental 100% of net fees) are governance-driven catalysts: each escalation was a tradeable event for DYDX

---

## Related

- [[hyperliquid]] -- Primary competitor in decentralized perps
- [[gmx]] -- Alternative DEX perps model on Arbitrum
- [[decentralized-exchanges]] -- Broader DEX landscape
- [[perpetual-futures]] -- The instrument dYdX specializes in
- [[crypto-perp-backtesting-pitfalls]] -- venue-specific backtest caveats
- [[ccxt]] -- data access library covering dYdX

---

## Sources

- dYdX blog — "dYdX Community Launches First-Ever DYDX Buyback Program" (March 2025): https://www.dydx.xyz/blog/dydx-buyback-program
- BeInCrypto — "dYdX's Community-Driven Buyback Program" (CEO Charles d'Haussy interview): https://beincrypto.com/dydx-ceo-charles-dhaussy-buybacks-staking-ecosystem/
- MEXC News — "dYdX Announces 3-Month Experimental Token Buyback Plan": https://www.mexc.com/news/146504
- OKX Learn — "Hyperliquid vs dYdX: How This Decentralized Futures Platform Captured 60% Market Share": https://www.okx.com/en-us/learn/hyperliquid-dydx-market-share
- BitMEX Research — state of crypto perps 2025 (DEX perp share), cited on [[crypto-perp-backtesting-pitfalls]]
- Web verification via Perplexity/WebSearch, 2026-06-10.
