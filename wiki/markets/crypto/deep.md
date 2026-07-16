---
title: "DeepBook"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["DEEP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://deepbook.tech/"
related: ["[[clob]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[decentralized-finance]]", "[[liquidity]]", "[[order-book]]", "[[serum]]", "[[sui]]"]
---

# DeepBook

**DeepBook** (ticker **DEEP**) is the native token of **DeepBook**, the first fully on-chain **central limit order book ([[clob|CLOB]])** built natively on the [[sui]] blockchain. DeepBook acts as shared liquidity infrastructure — a "public good" order book that [[decentralized-exchange]]s, aggregators, and dApps on Sui plug into rather than each building their own automated market maker. The DEEP token is used to pay trading fees and to govern the protocol. It is a small-cap infrastructure token, ranked **#508** by market capitalization.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Value |
|---|---|
| **Ticker** | DEEP |
| **Current Price** | $0.01662902 |
| **Market Cap** | $41.57M |
| **Market Cap Rank** | #508 |
| **24h Volume** | $3.99M |
| **24h Change** | +0.42% |
| **7d Change** | -6.18% |
| **Circulating Supply** | 2.50B DEEP (25% of max) |
| **Fully Diluted Valuation** | $166.28M |
| **Market Cap / FDV** | ~0.25 |
| **All-Time High** | $0.341085 (2025-01-18) — ~95% below |
| **All-Time Low** | $0.01073218 (2024-10-14) — ~55% above |

Trading backdrop: the broad crypto market sits in **extreme fear** (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] ≈ 23) amid what is being characterized as an **Established Bear Market** as of 2026-06-21. DEEP was roughly flat on the day (+0.42%) but down ~6% on the week, sliding alongside the wider [[sui]] ecosystem. At ~$0.0166 it is ~95% below its January 2025 high and only ~55% above its October 2024 all-time low — i.e. trading in the lower third of its lifetime range.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.50B DEEP |
| **Total Supply** | 10.00B DEEP |
| **Max Supply** | 10.00B DEEP |
| **Market Cap** | $41.57M |
| **Fully Diluted Valuation** | $166.28M |
| **MC / FDV Ratio** | ~0.25 |

The low **MC/FDV ratio of ~0.25** is the key tokenomics fact: only ~25% of the fixed 10B supply currently circulates, so roughly 7.5B DEEP remains locked behind future vesting/emissions. This represents significant latent dilution — the fully diluted valuation ($166M) is ~4x the circulating market cap, a structural headwind for price as unlocks proceed. See [[token-unlocks]].

---

## How & Where It Trades

**Spot venues.** DEEP trades as **DEEP/USD**, **DEEP/USDT**, and **DEEP/KRW** on centralized exchanges including [[kraken]], Upbit, Bitget, [[kucoin]], and Crypto.com, and natively on the Sui chain through DeepBook-powered DEXs and aggregators. Daily volume (~$3.9M) is modest, consistent with a sub-$50M cap; the Korean (Upbit) listing adds a regional retail liquidity pocket.

**On-chain order book mechanics (the actual product).** Unlike AMM-based DEXs (e.g. [[uniswap]]) that quote prices from constant-product pools, DeepBook runs a true **central limit order book ([[clob|CLOB]]) entirely on-chain**:

- **Maker/taker limit orders** are posted and matched on-chain on [[sui]], giving price-time priority and tight, deterministic pricing rather than slippage-curve pricing.
- **Composability** — because the order book is a shared on-chain module, any Sui dApp can route through it for deep, censorship-resistant liquidity without bootstrapping its own.
- **Fee/utility role** — DEEP is the protocol's fee and incentive token; traders and integrating apps interact with the book using DEEP-denominated economics.
- Sui's parallel execution and low fees make an on-chain CLOB practical, which is the technical thesis distinguishing DeepBook from order books on slower L1s.

**Derivatives.** DEEP has no material perpetual-futures / [[hyperliquid]] listing; no meaningful funding-rate or open-interest data is available. Treat it as a spot-only small-cap for trading.

---

## Use Case, Narrative & Category

DeepBook sits in the **DeFi infrastructure / liquidity layer** category. Its narrative is being the **liquidity backbone of the Sui ecosystem** — the canonical on-chain order book that other Sui protocols compose on top of, analogous to how [[serum]] aimed to be the shared [[clob|CLOB]] for [[solana]]. Value accrual depends on order flow routed through DeepBook and on the overall health and trading activity of the [[sui]] DeFi ecosystem.

---

## Valuation Framing

DEEP is a **bet on Sui DeFi throughput, levered to an unlock schedule**. The qualitative thesis: as the shared [[clob|CLOB]] for [[sui]], DeepBook should capture fee/utility value proportional to the order flow routed through it, so the token is effectively a claim on Sui's trading activity. Two facts dominate the valuation: (1) ecosystem concentration — DEEP's fortunes are tightly coupled to one L1, so a quiet Sui starves the book of flow; and (2) the ~0.25 MC/FDV means ~7.5B DEEP of latent dilution sits ahead of the price, so even flat demand can pressure the token as emissions vest. The cautionary historical analogue is [[serum]], the Solana CLOB that aspired to the same "shared liquidity public good" role and ultimately faded — execution and sustained order flow, not just elegant design, determine whether DeepBook accrues durable value. At ~$41.6M cap (vs ~$166M FDV) the market is pricing DEEP as a small-cap infrastructure option on Sui DeFi, with the unlock overhang as the chief headwind.

---

## Peer Comparison

| Token | Venue type | Chain | MC / FDV | Notes |
|---|---|---|---|---|
| **DeepBook (DEEP)** | On-chain [[clob|CLOB]] | [[sui]] | ~0.25 | Shared liquidity public good; heavy future unlocks |
| **[[serum]] (SRM)** | On-chain CLOB | [[solana]] | — | Aspired to same role; faded post-FTX |
| **[[uniswap]] (UNI)** | AMM DEX | Ethereum + L2s | high | Constant-product pools, not an order book |
| **[[hyperliquid]] (HYPE)** | On-chain perp CLOB (own L1) | Hyperliquid L1 | partial | Order-book derivatives, vertically integrated |

*DEEP ratio reflects the 2026-06-21 snapshot; peers shown qualitatively. DeepBook's differentiator is a genuine spot CLOB on a high-throughput, parallel-execution L1.*

---

## Notable History

- Built and shipped alongside the [[sui]] mainnet by Mysten Labs / the Sui Foundation as a community public good; the standalone DEEP token and "DeepBook v3" expanded it into a tokenized, governable protocol.
- All-time high of **$0.341 on 2025-01-18**, near peak Sui-ecosystem enthusiasm; since retraced ~95%.
- One of the few production examples of a fully on-chain CLOB, frequently cited as a differentiator for Sui's high-throughput design.

---

## Risks

- **Heavy future dilution** — only ~25% of supply circulates; ~7.5B DEEP of unlocks/emissions overhang the price.
- **Ecosystem-concentration risk** — DEEP's fortunes are tightly coupled to [[sui]] DeFi activity; a quiet Sui ecosystem starves the order book of flow.
- **Bear-market / drawdown** — down ~95% from ATH and only ~55% above its all-time low, trading in an extreme-fear (F&G 23), Established Bear Market environment.
- **Small-cap liquidity** — sub-$50M cap and ~$4M daily volume mean thin books and slippage outside top venues.
- **Smart-contract / matching-engine risk** — an on-chain CLOB is a complex, novel attack surface.

---

## See Also

- [[crypto-markets]]
- [[sui]]
- [[clob]]
- [[decentralized-exchange]]
- [[order-book]]
- [[serum]]
- [[hyperliquid]]
- [[decentralized-finance]]
- [[liquidity]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko bulk snapshot.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DEEP |
| **Market Cap Rank** | #473 |
| **Market Cap** | $44.26M |
| **Current Price** | $0.0177 |
| **Categories** | Infrastructure, Decentralized Finance (DeFi) |
| **Website** | [https://deepbook.tech/](https://deepbook.tech/) |

---

## Overview

DeepBook was built from the ground up to power the Sui ecosystem with unparalleled liquidity. From its inception, it has provided developers with reliable, composable on-chain applications, and enabled market makers and liquidity pools to operate seamlessly within the blockchain world.

As a community-driven public good, DeepBook has integrated with top DEXs and aggregators since Sui's mainnet launch, enhancing dApps with efficient, censorship-free liquidity. This synergy of orderbook efficiency and blockchain transparency positions DeepBook as the premier liquidity venue in web3.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 2.50B DEEP |
| **Total Supply** | 10.00B DEEP |
| **Max Supply** | 10.00B DEEP |
| **Fully Diluted Valuation** | $177.03M |
| **Market Cap / FDV Ratio** | 0.25 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.3411 (2025-01-18) |
| **Current vs ATH** | -94.82% |
| **All-Time Low** | $0.0107 (2024-10-14) |
| **Current vs ATL** | +64.76% |
| **24h Change** | -3.55% |
| **7d Change** | -2.70% |
| **30d Change** | -1.18% |
| **1y Change** | -90.80% |

---

## Platform & Chain Information

**Native Chain:** Sui

### Contract Addresses

| Chain | Address |
|---|---|
| Sui | `0xdeeb7a4662eec9f2f3def03fb937a663dddaa2e215b8078a284d026b7946c270::deep::DEEP` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | DEEP/USD | N/A |
| Upbit | DEEP/KRW | N/A |
| Bitget | DEEP/USDT | N/A |
| KuCoin | DEEP/USDT | N/A |
| Crypto.com Exchange | DEEP/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://deepbook.tech/](https://deepbook.tech/) |
| **Twitter** | [@DeepBookonSui](https://twitter.com/DeepBookonSui) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $3.74M |
| **Market Cap Rank** | #473 |
| **24h Range** | $0.0176 — $0.0186 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
