---
title: "Electroneum"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, payments]
aliases: ["ETN"]
entity_type: protocol
founded: 2017
headquarters: "United Kingdom (origin)"
website: "http://electroneum.com/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[payments]]", "[[proof-of-work]]", "[[smart-contracts]]", "[[ethereum]]"]
---

# Electroneum

**Electroneum** (ETN) is a mobile-first cryptocurrency that originated in 2017 as a smartphone-friendly [[payments]] coin (famous for in-app "cloud mining") and has since re-architected itself into a [[layer-1]] EVM-compatible blockchain. Its stated mission targets the unbanked and emerging-market users, and its ecosystem includes the freelance gig marketplace **AnyTask**, where users earn and spend ETN. It ranks **#949** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

At the snapshot date ETN traded at **$0.00084822** with a market cap of **$15,250,925** (rank #949), up **0.19%** over 24 hours and up **1.91%** over 7 days — one of the few names in this cohort showing positive weekly momentum despite the "Extreme Fear" backdrop (Fear & Greed Index 21).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ETN |
| **Market Cap Rank** | #949 |
| **Market Cap** | $15,250,925 |
| **Current Price** | $0.00084822 |
| **24h Change** | +0.19% |
| **7d Change** | +1.91% |
| **Genesis Date** | 2017-10-30 |
| **Original Algorithm** | CryptoNight ([[proof-of-work|PoW]], legacy) → IBFT PoA (current L1) |
| **Categories** | [[payments|Payments]], [[smart-contracts|Smart Contract Platform]], [[layer-1|Layer 1 (L1)]] |
| **Website** | [http://electroneum.com/](http://electroneum.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Electroneum launched in 2017 with a deliberately consumer-friendly angle: a mobile app that let everyday smartphone users participate in the network through a simulated "cloud mining" experience (which dispensed small ETN rewards without genuinely mining on the device). The original chain used a CryptoNight [[proof-of-work|proof-of-work]] algorithm. Over time the project repositioned around real-world [[payments]] and remittances for the unbanked and underbanked in emerging markets, pursuing regulatory engagement (KYC/AML) earlier than most peers.

### Migration to an L1 smart-contract chain

Electroneum re-architected its mainnet from the original [[proof-of-work|CryptoNight]] (Monero-family, privacy-oriented) chain into a [[layer-1]] **EVM-compatible** blockchain. The redesigned network is described as using **IBFT** (Istanbul Byzantine Fault Tolerant) proof-of-authority style consensus with a **permissioned set of known validators** — the project has publicized targeting universities and Web3 infrastructure firms as validators. The EVM compatibility allows standard Solidity [[smart-contracts]] and tooling (the same developer surface as [[ethereum|Ethereum]]), with the project emphasizing fast (~few-second) settlement and very low fees.

The migration is a deliberate architectural trade: the original PoW design was permissionless but slow and energy-hungry; the IBFT proof-of-authority model gives **deterministic, fast finality and near-zero fees** suited to micro-payments and remittances, at the cost of **permissioned, more centralized** block production. This is a common pattern for payments-first chains that prioritize predictable settlement over maximal decentralization.

> **Data caveat:** Figures such as "4+ million users," "5-second" finality and "lowest fees available" are project-stated marketing claims and have not been independently verified here. Treat them as qualitative positioning, not audited metrics.

### AnyTask and the ETN ecosystem

ETN's flagship real-world utility is **AnyTask.com**, a freelance/gig marketplace built by the Electroneum team where sellers (often in regions with limited access to traditional payment rails) can offer services and receive ETN — providing earnings without requiring a bank account or credit card. This "earn-and-spend" loop is the project's main bid for organic, non-speculative demand.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 17.98B ETN |
| **Total Supply** | 17.98B ETN |
| **Max Supply** | 21.00B ETN |
| **Fully Diluted Valuation** | $18.37M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.2079 (2018-01-06) |
| **Current vs ATH** | ~-99.6% |
| **All-Time Low** | $0.00084381 (2026-03-14) |
| **24h Change** | +0.19% |
| **7d Change** | +1.91% |

ETN reached its all-time high in the January 2018 cycle and now trades near its all-time low, having recently set a new low in March 2026. The current price sits only marginally above that level, so the positive 24h/7d moves (Fear & Greed 21 on 2026-06-22) come off a depressed base.

---

## Token Role

| Function | Description |
|---|---|
| **Payments / gas** | ETN is the native unit for transaction fees and on-chain transfers, and the medium of exchange on AnyTask. |
| **Remittance / earn-and-spend** | Used by gig workers and recipients in emerging markets to receive and spend value without a bank. |
| **Network economics** | Supply is capped at 21B ETN (a deliberate nod to Bitcoin's 21M), with circulating supply near the cap. |

ETN's value-accrual thesis is **utility-payment demand** rather than fee burn or staking yield: with circulating supply already near the 21B cap, there is little inflation overhang, so price depends on whether real remittance/AnyTask volume and on-chain transfers create sustained demand for the token. The risk is that this demand is largely **project-stated** and hard to verify, and that stablecoins and faster general-purpose chains compete directly for the same remittance use case.

---

## History

- **September–November 2017** — Electroneum runs one of the era's largest ICOs (reportedly ~$40M, hundreds of thousands of contributors), founded in the UK by **Richard Ells**; mainnet genesis 2017-10-30 on a [[proof-of-work|CryptoNight]] chain.
- **2017–2018** — the mobile app with simulated "cloud mining" drives mass sign-ups; ETN peaks at ~$0.21 in January 2018.
- **2018–2019** — pivot toward real-world [[payments]] and emerging-market remittances, with early, proactive **KYC/AML** compliance (unusual for the period) to position as a regulator-friendly payments coin.
- **2020** — launch of **AnyTask.com**, a freelance/gig marketplace where sellers earn ETN without needing a bank account or card — the project's main bid for organic demand.
- **Migration era** — re-architecture into a [[layer-1]] **EVM-compatible** chain using **IBFT** proof-of-authority consensus, opening Solidity smart-contract support and targeting institutional validators.
- **March 2026** — ETN sets a fresh all-time low (~$0.000844); as of 2026-06-22 it trades just above that level.

---

## Governance

- **Permissioned validator set:** Under IBFT proof-of-authority, a known, vetted group of validators (the project has named universities and Web3 infrastructure firms as targets) produces blocks. This is more centralized and more accountable than permissionless [[proof-of-stake|PoS]]/[[proof-of-work|PoW]], but security and censorship-resistance hinge on that operator group.
- **Company-led direction:** Electroneum's roadmap, the AnyTask product, and validator onboarding are steered by the founding company, making it a corporate-led network rather than a community-governed protocol.
- **Compliance posture:** Early KYC/AML adoption reflects a deliberate, regulator-engaged stance — a governance choice that distinguishes ETN from privacy-first peers but also ties it to off-chain compliance processes.

---

## Electroneum vs. Peer Payments / Mobile Chains

| Dimension | Electroneum (ETN) | Stellar (XLM) | [[ethereum|Ethereum]] (ETH) | Pi Network / mobile coins |
|---|---|---|---|---|
| **Primary use** | Mobile [[payments]] / remittance | Cross-border payments | General smart contracts | Mobile-distributed coin |
| **Consensus** | IBFT PoA (permissioned) | SCP (federated) | PoS (permissionless) | App-gated |
| **Smart contracts** | EVM-compatible | Limited (Soroban) | Full EVM | Limited |
| **Decentralization** | Lower (known validators) | Medium (federated) | High | Low |
| **Flagship utility** | AnyTask gig marketplace | Anchors / on-off ramps | DeFi/NFT ecosystem | App engagement |
| **Supply** | 21B cap (BTC-style) | Fixed (post-burn) | Low net issuance | Varies |
| **Origin** | 2017, UK | 2014 | 2015 | Varies |

Electroneum's differentiation is the **mobile-first, emerging-market payments funnel plus AnyTask earn-and-spend loop** — a real-world utility bid that most micro-cap L1s lack. The trade-offs are a **permissioned validator model** (lower decentralization than its EVM peers) and a **crowded remittance niche** where stablecoins and faster chains compete hard.

---

## Platform & Chain Information

**Native Chain:** Own [[layer-1]] EVM-compatible blockchain

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| KuCoin | ETN/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://electroneum.com/](http://electroneum.com/) |
| **Twitter** | [@electroneum](https://twitter.com/electroneum) |
| **Reddit** | [https://www.reddit.com/r/Electroneum](https://www.reddit.com/r/Electroneum) |
| **Telegram** | [officialelectroneum](https://t.me/officialelectroneum) (20,431 members) |
| **GitHub** | [https://github.com/electroneum/electroneum](https://github.com/electroneum/electroneum) |
| **Whitepaper** | [http://electroneum.com/overview-white-paper.pdf](http://electroneum.com/overview-white-paper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 383 |
| **GitHub Forks** | 194 |
| **Pull Requests Merged** | 60 |
| **Contributors** | 12 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.00084822 |
| **Market Cap (2026-06-22)** | $15,250,925 |
| **Market Cap Rank** | #949 |
| **24h Change** | +0.19% |
| **7d Change** | +1.91% |
| **CoinGecko Sentiment** | 67% positive |
| **Last Updated** | 2026-06-22 |
| **Historical (2026-04-09)** | 24h volume $462,998; rank #954; 24h range $0.00098973–$0.00105454 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks & Considerations

- **Permissioned validators** — the IBFT proof-of-authority model with a known validator set is more centralized than permissionless PoS/PoW chains; security and censorship-resistance depend on a small operator group.
- **Price near all-time low** — ETN set a fresh ATL in March 2026 and trades just above it; recent gains are off a low base.
- **Adoption-dependent thesis** — value rests heavily on real-world payments/AnyTask traction; usage metrics are project-stated and hard to verify.
- **Crowded payments narrative** — competes with stablecoins and many faster/cheaper chains for the remittance use case.
- **Liquidity** — small market cap and limited exchange depth.
- *Not investment advice — point-in-time data; micro-cap altcoin risk applies.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[payments]]
- [[smart-contracts]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
