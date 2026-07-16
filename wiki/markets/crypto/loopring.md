---
title: "Loopring"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, ethereum]
aliases: ["LRC"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://loopring.io"
related: ["[[automated-market-maker]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[ethereum]]", "[[governance-token]]", "[[layer-2]]", "[[order-book]]", "[[zk-rollup]]"]
---

# Loopring

**Loopring** ([[lrc|LRC]]) is an [[ethereum]] [[layer-2]] scaling protocol and [[decentralized-exchange|DEX]] built on **[[zk-rollup|zkRollup]]** technology. It combines both [[automated-market-maker|AMM]]-based and [[order-book|order-book]]-based decentralized trading on a high-throughput, low-cost L2 that inherits Ethereum's security via zero-knowledge proofs. Loopring is one of the earliest zkRollup deployments in production and pioneered non-custodial, order-book-style trading at near-CEX speed and cost.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Price $0.01346408 · rank #899 · market cap $16,776,383 · 24h +0.63% · 7d -1.23%. Market-wide sentiment: Fear & Greed Index 21 (Extreme Fear).*

As of 2026-06-22, LRC trades at **$0.01346408**, ranked **#899** by market capitalization with a market cap of **$16,776,383**. The token was up modestly over the prior day (**+0.63%** 24h) and slightly down over the week (**-1.23%** 7d) amid an Extreme-Fear market regime (Fear & Greed Index 21). LRC remains down over 99% from its November 2021 all-time high near $3.75.

zkRollup is an Ethereum L2 scaling solution that migrates computation off-chain while posting validity proofs on-chain.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LRC |
| **Market Cap Rank** | #899 |
| **Market Cap** | $16,776,383 |
| **Current Price** | $0.01346408 |
| **24h Change** | +0.63% |
| **7d Change** | -1.23% |
| **Genesis Date** | 2017-08-01 |
| **Founder** | Daniel Wang |
| **Categories** | Decentralized Exchange (DEX), Smart Contract Platform, Exchange-based Tokens, Decentralized Finance (DeFi), Arbitrum Ecosystem, Ethereum Ecosystem, Layer 2 (L2), Zero Knowledge (ZK), Loopring Ecosystem, Rollup, Energi Ecosystem, Governance |
| **Website** | [https://loopring.io](https://loopring.io) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Fear & Greed Index 21 (Extreme Fear).*

---

## Overview

Loopring is a Decentralized Exchange (DEX) built on an Ethereum Layer-2 (L2) solution called zkRollup. It has both Automated Market Maker (AMM)-based and orderbook-based exchanges.&nbsp;

zkRollup is an Ethereum L2 scaling solution that migrates computations off the blockchain. Loopring protocol only uses the underlying Ethereum blockchain as a data layer and a verification layer. As a result, Loopring's throughput is as high as 2,025 trades per second compared to Ethereum’s current throughput of 15 transactions per second. The result is that the cost per trade settlement is as small as $0.00015.

Loopring's performance is sufficient for professional traders and market makers to deploy algorithmic strategies and other automated trading bots. This was not previously possible on any DEX as it was prohibitively slow and expensive. By building on top of Loopring 3.0, orderbook-based DEXs can be commercially viable for the first time. Loopring expects non-custodial exchanges can begin to outcompete and displace many centralized counterparts.

---

## Mechanism & Architecture

Loopring is a **[[zk-rollup]]** (zero-knowledge rollup) — a [[layer-2]] scaling design that batches many trades and transfers off-chain, then posts a single succinct **validity proof** (a SNARK) to [[ethereum]] mainnet to prove the batch was executed correctly. Ethereum is used only as a data-availability and verification layer, so users get the security guarantees of L1 with the throughput and cost profile of an off-chain system. Unlike optimistic rollups, zkRollups have no multi-day fraud-proof challenge/withdrawal window, enabling faster finality.

Key properties:

- **High throughput, low cost** — Loopring has cited throughput on the order of thousands of trades per second with per-trade settlement costs measured in fractions of a cent.
- **Hybrid exchange** — supports both an [[order-book]]-based DEX (matched off-chain, settled with proofs on-chain) and [[automated-market-maker|AMM]]-style [[liquidity-pool|pools]].
- **Non-custodial** — users retain control of funds; the operator cannot steal balances because state transitions must satisfy the proof system.
- **Smart wallet** — Loopring also shipped a consumer L2 smart-contract wallet for low-fee transfers, payments, and trading.

### zkRollup vs the alternatives, intuitively

- **Mainnet-only DEX (e.g., [[uniswap]] V2 on L1)** — every trade is an Ethereum transaction: maximally secure but slow and gas-heavy, unworkable for an [[order-book]] that needs many rapid order placements/cancels.
- **Optimistic rollup ([[arbitrum|Arbitrum]], [[optimism|Optimism]])** — assumes batches are valid unless challenged, requiring a multi-day fraud-proof window before withdrawals finalize.
- **zkRollup (Loopring, [[zksync|zkSync]], Starknet)** — proves *each* batch correct with a succinct **validity proof** posted to L1. There is no challenge window, so withdrawals finalize as soon as the proof verifies — better capital efficiency and stronger guarantees, at the cost of heavy proving computation and complex circuits.

For an order-book DEX this matters: Loopring can match orders off-chain at high frequency and settle them in proven batches, giving traders CEX-like UX while Ethereum guarantees the operator cannot forge balances or trades.

### Worked example (illustrative)

A market maker wants to quote a tight two-sided book in an ETH/USDC pair and update quotes many times per minute. On Ethereum L1 each cancel-and-replace would cost gas and confirm in ~12s — economically and operationally impossible. On Loopring, those order operations happen off-chain on the operator; periodically the operator submits a batch with a zk validity proof, and per-trade settlement cost is a fraction of a cent. The MM gets near-CEX responsiveness while the trader keeps non-custodial control — the operator cannot move funds in any way the proof system would not accept. Throughput and cost figures are protocol-cited and illustrative.

---

## Comparison vs Competitors

| Protocol | Type | Execution | Distinctive edge | Main constraint |
|---|---|---|---|---|
| **Loopring (LRC)** | App-specific zkRollup DEX (L2) | Off-chain order book + AMM, on-chain validity proofs | One of the first production zkRollups; non-custodial order-book trading | Single-app rollup → limited composability/liquidity |
| [[zksync\|zkSync]] / Starknet / Scroll | General-purpose zkEVM L2 | Full smart-contract platform with ZK proofs | Hosts entire DeFi ecosystems | Younger; fragmented liquidity |
| [[arbitrum\|Arbitrum]] / [[optimism\|Optimism]] | General-purpose optimistic L2 | EVM with fraud proofs | Largest L2 liquidity & app ecosystems | Multi-day withdrawal challenge window |
| [[dydx\|dYdX]] | App-chain perps order book | Off-chain matching, on-chain settlement | Mature perps order book | Perps-only; own chain |
| [[uniswap\|Uniswap]] (L1/L2) | AMM DEX | Constant product / concentrated | Deepest liquidity, broadest reach | Generic; no native order book |

Loopring's historical position as a *pioneer* of application-specific zkRollups is now also its strategic problem: general-purpose zkEVMs and large optimistic rollups host whole ecosystems, while a single-app DEX rollup struggles to attract the composability and liquidity that compound network effects.

---

## Token Role (LRC)

LRC is Loopring's native [[governance-token]] and protocol-utility token:

- **Staking / fees** — LRC can be staked, historically by protocol participants and liquidity providers, and the protocol's economic model directs a portion of trading-fee revenue to LRC stakers / the DAO.
- **Security/insurance role** — in Loopring's design, staking has been used to back exchange operation and align operators.
- **Governance** — LRC holders participate in protocol governance via the Loopring DAO.

Supply is large (~1.25B circulating of ~1.37B), with a market-cap/FDV ratio around 0.9.

---

## History & Notable Events

- **2017** — Loopring founded by Daniel Wang; LRC token launched (ICO era).
- **2019–2020** — Loopring 3.0 and the launch of Loopring's zkRollup exchange and protocol, one of the first zkRollups live on Ethereum mainnet.
- **2021** — Loopring drew significant attention amid the L2 narrative and a widely discussed (and ultimately materialized) GameStop NFT-marketplace collaboration, contributing to LRC's run to its ~$3.75 all-time high in November 2021.
- **2022–2026** — As the L2 landscape expanded with general-purpose zkEVMs ([[zksync]], Starknet, Polygon zkEVM, Scroll, Linea) and large optimistic rollups ([[arbitrum]], [[optimism]]), Loopring's application-specific DEX rollup ceded mindshare; LRC declined sharply through the bear market.

---

## Competitive Position

Loopring was a pioneer of **application-specific zkRollups** for trading, predating most general-purpose zkEVMs. Its strength is a purpose-built, low-cost, non-custodial exchange stack. However, the broader L2 ecosystem has shifted toward general-purpose zkEVMs and large optimistic rollups that host entire DeFi ecosystems, leaving Loopring's single-app rollup with comparatively limited composability and developer activity. It competes with both other DEXs ([[uniswap]], [[dydx]]) and with the wider [[layer-2]] field for liquidity and users.

---

## Risks

- **Competitive / relevance risk (primary)** — general-purpose zkEVMs and major rollups have largely captured the L2 narrative; an app-specific DEX rollup faces an uphill battle for liquidity and developer attention.
- **Adoption / network-effects risk** — DEX value depends on liquidity depth; thin liquidity drives users to larger venues.
- **Smart-contract and prover risk** — zkRollups rely on complex circuits and provers; bugs in proof systems or contracts are high-severity.
- **Centralization vector** — sequencer/operator roles and any upgrade keys are governance/centralization considerations common to L2s.
- **Microcap risk** — at a ~$16.7M market cap and >99% below its ATH, LRC is small, volatile, and sentiment-driven.

This is not investment advice; figures are point-in-time and crypto assets are highly volatile.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.25B LRC |
| **Total Supply** | 1.37B LRC |
| **Max Supply** | 1.37B LRC |
| **Fully Diluted Valuation** | $23.28M |
| **Market Cap / FDV Ratio** | 0.91 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $3.75 (2021-11-10) |
| **Current vs ATH** | ~-99.6% |
| **All-Time Low** | $0.0164 (2026-04-07) |
| **24h Change** | +0.63% |
| **7d Change** | -1.23% |
| **30d Change (2026-04-09 snapshot)** | -45.49% |
| **1y Change (2026-04-09 snapshot)** | -78.29% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xbbbbca6a901c926f240b89eacb641d8aec7aeafd` |
| Energi | `0x193da10f8a969d4c081b9097b15337b1488cbbec` |
| Arbitrum One | `0x46d0ce7de6247b0a95f67b43b589b4041bae7fbe` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | LRC/USD | N/A |
| KuCoin | LRC/USDT | N/A |
| Crypto.com Exchange | LRC/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XBBBBCA6A901C926F240B89EACB641D8AEC7AEAFD/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0XBBBBCA6A901C926F240B89EACB641D8AEC7AEAFD/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://loopring.io](https://loopring.io) |
| **Twitter** | [@loopringorg](https://twitter.com/loopringorg) |
| **Reddit** | [https://www.reddit.com/r/loopringorg/](https://www.reddit.com/r/loopringorg/) |
| **Telegram** | [loopring_en](https://t.me/loopring_en) (3,875 members) |
| **Discord** | [https://discord.com/invite/KkYccYp](https://discord.com/invite/KkYccYp) |
| **GitHub** | [https://github.com/Loopring/protocols](https://github.com/Loopring/protocols) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 335 |
| **GitHub Forks** | 124 |
| **Pull Requests Merged** | 1,264 |
| **Contributors** | 27 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.01346408 |
| **Market Cap** | $16,776,383 |
| **Market Cap Rank** | #899 |
| **24h Change** | +0.63% |
| **7d Change** | -1.23% |
| **24h Range (2026-04-09 snapshot)** | $0.0169 — $0.0180 |
| **CoinGecko Sentiment (2026-04-09 snapshot)** | 100% positive |
| **Last Updated** | 2026-06-22 (price/cap); intraday range/sentiment from 2026-04-09 snapshot |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---

## Related

- [[zk-rollup]]
- [[layer-2]]
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[order-book]]
- [[defi]]
- [[governance-token]]
- [[arbitrum]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot). Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no specific wiki source ingested yet.
