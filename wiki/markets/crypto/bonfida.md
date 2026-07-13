---
title: "Bonfida"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, defi, decentralized-exchange]
aliases: ["FIDA", "Solana Name Service", "SNS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.bonfida.org/"
related: ["[[crypto-markets]]", "[[solana]]", "[[decentralized-exchange]]", "[[defi]]", "[[governance-token]]", "[[order-book]]", "[[ftx]]"]
---

# Bonfida

**Bonfida** (ticker **FIDA**) is a [[solana]]-ecosystem project that grew out of the early Solana DeFi/[[decentralized-exchange]] stack and is today best known for the **Solana Name Service (SNS)** — human-readable `.sol` domain names that map to Solana wallet addresses. Bonfida built much of the trading and infrastructure tooling around the original **Serum** order-book DEX, and its **FIDA** token is the project's governance and utility asset. It ranks **#787** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* FIDA: $0.02169495, rank #785, market cap $21,497,763, 24h -0.55%, 7d -6.46%. Market backdrop: Fear & Greed Index at 21 (Extreme Fear).

At the latest snapshot FIDA traded near **$0.02169495** (market cap **$21,497,763**, rank **#785**), down **0.55% over 24h** and down **6.46% over 7d** — soft weekly performance, consistent with the broad risk-off backdrop (Fear & Greed Index at 21 / Extreme Fear). FIDA remains far below its 2021 cycle highs.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FIDA |
| **Market Cap Rank** | #785 |
| **Market Cap** | $21,497,763 |
| **Current Price** | $0.02169495 |
| **24h Change** | -0.55% |
| **7d Change** | -6.46% |
| **Categories** | Infrastructure, Decentralized Finance (DeFi), Solana Ecosystem, Name Service |
| **Website** | [https://www.bonfida.org/](https://www.bonfida.org/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Bonfida is a long-standing [[solana]]-ecosystem builder. Its origins are tied to the early Solana DeFi era, when it produced trading front-ends and infrastructure for the **Serum** central-limit order-book [[decentralized-exchange]] — including tooling such as the Asset-Agnostic Order Book (AOB) and order-book front-ends — and it experimented with derivatives products on Solana.

Following the collapse of FTX/Alameda (which had backed Serum) in late 2022, the Serum order book was effectively deprecated and forked by the community. Bonfida's most durable product became the **Solana Name Service (SNS)**: a naming system that registers `.sol` domains as on-chain assets, letting users replace long base-58 wallet addresses with readable names and attach records (websites, profile data, sub-domains). SNS is one of the more widely used naming systems in the Solana ecosystem.

### FIDA token

**FIDA** is the project's governance and utility token (SPL token on [[solana]]). It is used for governance over Bonfida products and has historically been tied to fee/value flows from the name service and trading tooling. Maximum supply is 1 billion FIDA, with the large majority already circulating, so FDV and market cap are close to one another.

---

## Mechanism & Architecture (Solana Name Service)

The **Solana Name Service (SNS)** is Bonfida's durable flagship product. It works much like ENS does for Ethereum, but built on Solana's account model:

- **Domains as on-chain accounts** — registering a `.sol` name creates an on-chain **name-registry account** owned by the registrant's wallet. The domain *is* an account (and is increasingly represented/tradable as an NFT), so it can be transferred, sold, or listed on Solana NFT marketplaces.
- **Records and resolution** — a domain can store **records** (a primary wallet address for receiving funds, plus IPFS/Arweave content hashes, social handles, URLs, etc.). Wallets and dApps resolve a human-readable `name.sol` to the underlying base-58 address, replacing 32-44 character addresses with memorable names.
- **Subdomains** — owners can issue subdomains (`pay.name.sol`, `vault.name.sol`), enabling organizations or apps to delegate namespaces.
- **Registration economics** — names are priced (historically by length, shorter = pricier) and paid in stablecoins/SOL/FIDA; registration revenue is a core value flow for the protocol and a lever governed by FIDA holders.
- **Asset-Agnostic Order Book (AOB)** — Bonfida's legacy contribution to the [[order-book|central-limit order book]] DEX stack used by Serum; an on-chain matching primitive that any market could plug into. This tooling is largely dormant since Serum's deprecation but reflects the project's order-book heritage versus [[automated-market-maker|AMM]]-based DEXs.

### Illustrative SNS use

A user registers `alice.sol`, sets her primary wallet record, and shares "alice.sol" instead of a long base-58 address. A friend types `alice.sol` in a supporting Solana wallet; the wallet queries SNS, resolves it to the underlying address, and sends SOL. Alice later lists `alice.sol` on an NFT marketplace and sells the domain to another user, transferring the registry account. *(Illustrative.)*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 990.91M FIDA |
| **Total Supply** | 1.00B FIDA |
| **Max Supply** | 1.00B FIDA |
| **Fully Diluted Valuation** | $16.25M |
| **Market Cap / FDV Ratio** | 0.99 |

### Value accrual & governance

- **Fee flows from SNS** — domain registration and renewal revenue is the most tangible value driver, and FIDA governance controls pricing and how that revenue is used (treasury, buybacks, ecosystem funding).
- **Governance scope** — FIDA holders govern Bonfida products, treasury allocation, and the direction of SNS development. With max supply effectively fully circulating (~99% of 1B), there is little emission-driven dilution overhang.
- **Coupling to Solana** — because FIDA's utility is Solana-native (SNS, SPL token), its value is strongly correlated with overall [[solana|Solana]] network activity and the demand for on-chain identity/naming.

---

## History & Notable Events

- **2020–2021** — Bonfida launches as a leading builder on early Solana DeFi, providing trading front-ends, analytics, and infrastructure (the Asset-Agnostic Order Book) for the **Serum** [[order-book]] DEX, which was backed by Alameda/[[ftx|FTX]]. FIDA reaches an all-time high of **$18.77 on 2021-11-03**.
- **Late 2022 — FTX collapse** — the implosion of [[ftx|FTX]]/Alameda deprecated the Serum order book (its upgrade keys were compromised), and the community forked it into OpenBook. Bonfida's trading-infrastructure business was largely undermined, forcing a strategic pivot.
- **2022–2024 — pivot to SNS** — Bonfida concentrates on the **Solana Name Service** as its durable product, growing `.sol` domains into one of the most-used naming systems on Solana, riding subsequent waves of Solana on-chain activity.
- **2026-03-29** — FIDA records an all-time low around **$0.0122**, reflecting the cumulative damage from the FTX-era unwind and the broad de-rating of legacy DeFi tokens.

---

## Competitive Position

Bonfida competes in **on-chain naming/identity** and, historically, **DEX infrastructure**. Its SNS product is the dominant `.sol` naming service but faces the same structural questions as all naming protocols: durable monetization beyond one-time registrations, and competition from alternative implementations.

### Comparison vs naming-service peers

| Service | Chain | Domain | Token | Model | Position |
|---|---|---|---|---|---|
| **Bonfida / SNS** | [[solana\|Solana]] | `.sol` | FIDA | Registry accounts (NFT-tradable), records, subdomains | Dominant Solana naming service |
| ENS | [[ethereum\|Ethereum]] | `.eth` | ENS | Registrar + resolver, NFT domains | Largest, most established naming service |
| Unstoppable Domains | Multi-chain | `.crypto` etc. | (no live gov token historically) | One-time-purchase NFT domains | Web2-style branding, no renewals |
| Space ID | Multi-chain / BNB | `.bnb` etc. | ID | Multi-chain naming aggregator | Cross-chain identity focus |

SNS's edge is being native to Solana's fast, low-fee environment; its risk is dependence on a single chain's identity demand.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $18.77 (2021-11-03) |
| **Current vs ATH** | approx. -99.9% |
| **All-Time Low** | $0.0122 (2026-03-29) |
| **Current Price** | $0.02169495 |
| **24h Change** | -0.55% |
| **7d Change** | -6.46% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `EchesyfXePKdLtoiZSL8pBe8Myagyy8ZRqsACNCFGnvp` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | FIDA/USDT | N/A |
| Kraken | FIDA/USD | N/A |
| Bitget | FIDA/USDT | N/A |
| KuCoin | FIDA/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Orca | EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V/ECHESYFXEPKDLTOIZSL8PBE8MYAGYY8ZRQSACNCFGNVP | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.bonfida.org/](https://www.bonfida.org/) |
| **Twitter** | [@bonfida](https://twitter.com/bonfida) |
| **Discord** | [https://discord.com/invite/bonfida-778660171265474572](https://discord.com/invite/bonfida-778660171265474572) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Current Price** | $0.02169495 |
| **Market Cap** | $21,497,763 |
| **Market Cap Rank** | #785 |
| **24h Change** | -0.55% |
| **7d Change** | -6.46% |
| **Last Updated** | 2026-06-22 |

---

## Risks

- **Legacy / pivot risk** — Bonfida's original DEX-tooling business was largely undermined by the deprecation of Serum after the FTX collapse; the project's value now depends heavily on continued adoption of the Solana Name Service rather than trading infrastructure.
- **Low liquidity / micro-cap** — at roughly $22M market cap and rank #787, FIDA is thinly traded and prone to sharp moves and slippage.
- **Solana ecosystem beta** — FIDA's fortunes are tightly coupled to overall [[solana]] activity and sentiment.
- **Competition** — naming services and Solana tooling face competing implementations; market share is not guaranteed.
- **Severe historical drawdown** — FIDA sits roughly 99.9% below its 2021 ATH, reflecting both the bear market and the loss of its FTX-era backers.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[solana]]
- [[decentralized-exchange]]
- [[order-book]]
- [[ftx]]
- [[governance-token]]
- [[defi]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
