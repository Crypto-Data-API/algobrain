---
title: "Hedera"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["HBAR", "Hedera Hashgraph"]
entity_type: protocol
founded: 2018
headquarters: "Hedera Council (global); Hashgraph/Swirlds — Texas, USA"
website: "https://www.hedera.com/"
related: ["[[avalanche]]", "[[bitcoin-etfs]]", "[[chainlink]]", "[[crypto-markets]]", "[[hyperliquid]]", "[[layer-1-blockchains]]", "[[proof-of-stake]]"]
---

# Hedera

**Hedera** (HBAR) is an enterprise-grade public ledger built on the hashgraph consensus algorithm (a DAG, not a conventional blockchain), governed by a council of global corporations including Google, IBM, Boeing, Deutsche Telekom, LG and Nomura. For traders it is the flagship "enterprise/RWA adoption" altcoin: it was the **third cryptocurrency to get a US spot ETF** (Canary HBR, October 2025), yet remains a case study in adoption-price divergence — strong enterprise metrics with persistently weak price action.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #29 |
| **Market Cap** | $3.48B |
| **Current Price** | $0.080039 |
| **24h Volume** | $58.64M |
| **24h Change** | +1.32% |
| **7d Change** | +3.33% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: with the broad market in **extreme fear** ([[fear-and-greed-index|Fear & Greed]] = 22) and an Established [[bear-market|Bear Market]] backdrop, HBAR is mildly green on the day (+1.32%) and week (+3.33%) but sits around **$0.08** — well below the early-2026 ~$0.11 area and ~86% under its September 2021 ATH of $0.5692. Note the relatively **thin 24h volume (~$58.6M)** versus its ~$3.5B market cap, a recurring liquidity tell that amplifies HBAR's moves on headlines.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | HBAR |
| **Market Cap Rank** | #29 (2026-06-20) |
| **Market Cap** | $3.48B (2026-06-20) |
| **Consensus / Sector** | Hashgraph (DAG), aBFT, [[proof-of-stake|proof-of-stake]]; sectors: enterprise L1, RWA tokenization, payments |
| **Hashing Algorithm** | Directed Acyclic Graph (DAG) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Hedera Ecosystem, GMCI Layer 1 Index, GMCI 30 Index, GMCI Index, Outlier Ventures Portfolio, Made in USA, Directed Acyclic Graph (DAG) |
| **Website** | [https://www.hedera.com/](https://www.hedera.com/) |

---

## Overview

Hedera is a decentralized public network where developers can build secure, fair applications with near real-time consensus. The platform is owned and governed by a council of global innovators including Avery Dennison, Boeing, Deutsche Telekom, DLA Piper, FIS (WorldPay), Google, IBM, LG Electronics, Magalu, Nomura, Swirlds, Tata Communications, University College London (UCL), Wipro, and Zain Group.

The Hedera Consensus Service (HCS) acts as a trust layer for any application or permissioned network and allows for the creation of an immutable and verifiable log of messages. Application messages are submitted to the Hedera network for consensus, given a trusted timestamp, and fairly ordered. Use HCS to track assets across a supply chain, create auditable logs of events in an advertising platform, or even use it as a decentralized ordering service.

---

## Technology & Consensus

Hedera's core differentiator is the **hashgraph consensus algorithm** — a directed-acyclic-graph (DAG) protocol, not a linear blockchain — invented by Dr. Leemon Baird and licensed exclusively to Hedera (open-sourced in 2022 onward).

| Component | Detail |
|---|---|
| **Data structure** | DAG of "events" rather than a chain of blocks |
| **Consensus** | Hashgraph "gossip about gossip" + virtual voting, achieving **asynchronous Byzantine Fault Tolerance (aBFT)** |
| **Security model** | aBFT — the strongest BFT guarantee; resilient even if the network is partitioned or messages are arbitrarily delayed, tolerant of up to 1/3 malicious stake |
| **Throughput / fees** | Tens of thousands of TPS; sub-cent, fixed-USD-denominated fees; ~3–5 second finality |
| **Staking** | [[proof-of-stake|Proof-of-stake]] over the public network; consensus nodes initially permissioned (council-run), with a roadmap toward permissionless nodes |
| **Native services** | Token Service (HTS — native tokenization without smart contracts), Consensus Service (HCS — ordered, timestamped logs), Smart Contract Service (EVM-compatible) |

**Gossip about gossip + virtual voting.** Each node randomly shares ("gossips") the transactions it knows plus the *history of who told it what*. Because every node can reconstruct the full communication graph, nodes compute consensus order *locally* via "virtual voting" — no actual vote messages are sent. This yields aBFT with high throughput. The trade-off versus permissionless [[proof-of-work|PoW]]/PoS chains is the **council governance / permissioned-node model**, which buys performance and finality at the cost of decentralization optics — the central tension in any HBAR thesis.

**HTS and HCS** are the enterprise hooks: HTS lets institutions mint regulated tokens (RWAs, stablecoins) without writing Solidity, and HCS provides a tamper-evident, fairly-ordered audit log — the basis for Hedera's supply-chain, RWA, and recordkeeping deployments.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | ~43,473,263,316 HBAR |
| **Total Supply** | 50,000,000,000 HBAR |
| **Max Supply** | 50,000,000,000 HBAR |
| **Market Cap / FDV Ratio** | ~0.87 |

- **Fixed 50B cap** — no inflation beyond the predefined release of the remaining treasury supply. Circulating is ~43.5B of 50B, so MC/FDV ~0.87 leaves a modest remaining-supply release schedule (lower overhang than [[sui|Sui]] but not as clean as fully-unlocked names).
- **Treasury releases**: the Hedera treasury (controlled by the council/Foundation) releases HBAR over a multi-year schedule to fund ecosystem, grants and network rewards — a known, scheduled supply input traders watch.
- **Staking rewards**: paid from the treasury rather than via new issuance, so staking does not increase the hard cap.
- **Fee model**: transaction fees are denominated in USD and paid in HBAR at sub-cent rates; high transaction counts (see network growth) translate to small but real fee demand.

---

## Ecosystem & Use Cases

- **RWA tokenization** — Hedera's marquee vertical. Lloyds Banking Group and Aberdeen used tokenized funds and UK government bonds on Hedera as FX collateral in a landmark UK trial; Santiment ranked Hedera **#1 in RWA development activity in Q1 2026**, ahead of [[chainlink|Chainlink]] and [[avalanche|Avalanche]].
- **Government / public sector** — the country of Georgia moved its property-records system onto Hedera; Australia advanced a digital-currency initiative using Stablecoin Studio on Hedera.
- **Enterprise consortia** — council members (Google, IBM, Boeing, Deutsche Telekom, LG, Nomura) provide built-in enterprise distribution and run consensus nodes.
- **Payments / stablecoins** — sub-cent fixed fees and HTS make Hedera a payments/stablecoin rail candidate.
- **Network activity** — daily active wallets +190% YoY and dApp transaction volume +386% (to 2.7M) reported into 2026 — strong usage metrics that have not translated into price.

---

## Market Structure & Derivatives

- **Spot venues**: [[binance|Binance]] (HBAR/USDT), [[kraken|Kraken]], Upbit (large KRW flow), Bitget, KuCoin, Crypto.com. Note **thin 24h volume (~$58.6M on 2026-06-20)** relative to a ~$3.5B cap.
- **Perps / funding / OI**: perps on [[hyperliquid|Hyperliquid]] (HBAR-PERP) and major CEX futures. With thin spot liquidity, HBAR perps are prone to sharp squeezes around ETF/regulatory headlines; OI builds around ETF-flow prints and council announcements.
- **ETF exposure**: the **Canary HBR spot ETF (Nasdaq)** launched 28 October 2025, making HBAR the **third crypto asset with a US spot ETF**. By mid-2026 it had absorbed ~**549M HBAR (~1.3% of circulating supply)** and ~**$93M in inflows** — an ongoing supply-squeeze input. ~15 further ETF filings (incl. Grayscale and Bitwise) were active at the SEC.
- **Native chain**: own L1 (hashgraph DAG); HBAR is the native asset.

---

## Trading Playbook

- **Adoption-price divergence is the central trade**: strong fundamentals (RWA leadership, +386% dApp tx) have NOT translated into price (HBAR fell from ~$0.11 toward $0.08 into mid-2026). HBAR rewards **event-driven trading around ETF/regulatory headlines** rather than adoption-thesis buy-and-hold.
- **Narrative baskets**: enterprise/RWA-adoption basket (with [[avalanche|Avalanche]], [[chainlink|Chainlink]], XRP-style "institutional alt" flows); GMCI 30 / GMCI L1 index constituent; popular retail "ISO-20022 / enterprise chain" theme. Trade via [[narrative-trading]] within the RWA cohort.
- **Catalysts**: HBR ETF flow prints (1.3% of supply already absorbed), additional spot ETF approvals (Grayscale, Bitwise), the US CLARITY Act process (a tailwind for utility-classified assets), council-member enterprise announcements.
- **Liquidity caution**: thin 24h volume vs. market cap means slippage and violent headline moves — use limit orders, expect gaps. Heavy retail sentiment (93% positive at the April snapshot) layered on a weak tape is a contrarian caution flag.
- **Regime note (2026-06-20)**: HBAR's mild green into extreme fear is noise, not trend; the structural adoption-price disconnect persists.

---

## History

- **2018** — Hedera founded by Mance Harmon and Leemon Baird (Swirlds); Hedera Governing Council formed with global enterprises.
- **2019** — Mainnet open access; HBAR public listing.
- **Sep 2021** — Bull-market ATH of **$0.5692 (2021-09-15)**.
- **2022** — Hashgraph algorithm patents released to the Hedera community (open governance step).
- **2022–2024** — Bear-market derating; enterprise/RWA pipeline builds (Google, IBM, financial institutions).
- **28 Oct 2025** — **Canary HBR spot ETF** launches on Nasdaq — third crypto with a US spot ETF.
- **Q1 2026** — Santiment ranks Hedera #1 in RWA development activity; Lloyds/Aberdeen UK bond-collateral trial; Georgia property records on Hedera.
- **2026** — Adoption-price divergence persists; HBAR drifts toward ~$0.08 in an Established Bear Market.

---

## Competitive Positioning

| Project | Consensus | Decentralization | Niche | MC rank (2026-06-20) |
|---|---|---|---|---|
| **Hedera** | Hashgraph DAG, aBFT, council-governed | Permissioned consensus nodes (lower) | Enterprise / RWA / payments | #29 |
| [[avalanche|Avalanche]] | Snowman/Avalanche consensus, PoS | Permissionless | RWA, subnets, DeFi | mid-cap |
| [[chainlink|Chainlink]] | Oracle network (not an L1) | Decentralized oracle nodes | RWA data / oracles / CCIP | top-tier |
| XRP Ledger | XRPL consensus (UNL) | Federated | Payments / institutional | top 5 |
| [[solana|Solana]] | PoH + PoS | Permissionless | High-throughput general L1 | top 10 |

Hedera's edge is **enterprise distribution** (a council of blue-chip corporations) and **aBFT finality** with fixed sub-cent fees; its discount is **decentralization optics** (permissioned consensus nodes). Its closest thematic peers for traders are [[avalanche|Avalanche]] and [[chainlink|Chainlink]] in the RWA basket and XRP in the "institutional/payments alt" basket.

---

## Regulatory

- **Asset classification**: HBAR is positioned as a utility token; the Canary HBR spot ETF and ~15 pending filings imply issuers expect commodity-style treatment. The US **CLARITY Act** (market-structure legislation) is viewed as a potential tailwind for utility-classified assets like HBAR.
- **Council-governance scrutiny**: the permissioned-node / council model invites questions about decentralization and securities classification, but the live US ETF is evidence regulators have so far been comfortable.
- **Enterprise/RWA compliance**: Hedera's institutional deals (Lloyds, Aberdeen, Georgia) run inside regulated frameworks, which is part of the bull thesis but also ties HBAR's adoption to slow-moving institutional/regulatory cycles.

---

## Risks

- **Adoption-price disconnect** — the defining risk: usage and enterprise wins have repeatedly failed to lift price, frustrating fundamentals-based longs.
- **Decentralization discount** — permissioned consensus nodes and council control limit credible-neutrality appeal and invite regulatory/centralization critiques.
- **Thin liquidity** — low 24h volume vs. market cap amplifies downside and slippage.
- **Treasury supply releases** — scheduled treasury unlocks (MC/FDV ~0.87) add ongoing, known supply.
- **Competition** — crowded RWA/enterprise field ([[avalanche|Avalanche]], [[chainlink|Chainlink]], XRP, permissioned enterprise chains).
- **Macro/regime** — high-beta alt in an Established Bear Market; ~86% off ATH.

---

## Platform & Chain Information

**Native Chain:** Own ledger (hashgraph DAG, Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | HBAR/USDT | N/A |
| Kraken | HBAR/USD | N/A |
| Upbit | HBAR/KRW | N/A |
| Bitget | HBAR/USDT | N/A |
| KuCoin | HBAR/USDT | N/A |
| Crypto.com Exchange | HBAR/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | HBAR-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.hedera.com/](https://www.hedera.com/) |
| **Twitter** | [@hedera](https://twitter.com/hedera) |
| **Reddit** | [https://www.reddit.com/r/Hedera/](https://www.reddit.com/r/Hedera/) |
| **Telegram** | [hederahashgraph](https://t.me/hederahashgraph) (21,470 members) |
| **Discord** | [https://hedera.com/discord](https://hedera.com/discord) |
| **GitHub** | [https://github.com/hashgraph](https://github.com/hashgraph) |
| **Whitepaper** | [https://hedera.com/wp-content/uploads/2025/12/hh_whitepaper.pdf](https://hedera.com/wp-content/uploads/2025/12/hh_whitepaper.pdf) |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[avalanche]] — rival RWA/enterprise L1
- [[chainlink]] — RWA/oracle peer in the institutional basket
- [[bitcoin-etfs]] — context for the spot-ETF wave HBR extends
- [[hyperliquid]] — HBAR-PERP venue
- [[bitcoin]], [[ethereum]] — market beta drivers
- [[proof-of-stake]], [[layer-1-blockchains]], [[narrative-trading]]

---

## Sources

- CoinGecko top-1000 snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- cryptodataapi.com / CoinGecko markets snapshot, 2026-06-20 (current Market Data block)
- [Business Wire — Canary Capital Launches Spot HBAR ETF (28 Oct 2025)](https://www.businesswire.com/news/home/20251028164577/en/Canary-Capital-Launches-Spot-HBAR-ETF-Opening-Access-to-the-Next-Generation-of-Digital-Assets)
- [Canary Capital — HBAR ETF (HBR) fund page](https://canaryetfs.com/hbr/)
- [OpenPR — Canary HBAR ETF Absorbs 549M Tokens and $93M in Capital (2026)](https://www.openpr.com/news/4442203/canary-hbar-etf-absorbs-549m-tokens-and-93m-in-capital-as)
- [Bitcoin Foundation — Hedera Price Prediction 2026: Institutional Adoption](https://bitcoinfoundation.org/news/altcoins/hedera-hbar-price-prediction-2026/)
- [Hedera whitepaper](https://hedera.com/wp-content/uploads/2025/12/hh_whitepaper.pdf)
- Verified via Perplexity (sonar) and web search, 2026-06-10.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 43.79B HBAR |
| **Total Supply** | 50.00B HBAR |
| **Max Supply** | 50.00B HBAR |
| **Fully Diluted Valuation** | $3.36B |
| **Market Cap / FDV Ratio** | 0.88 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.5692 (2021-09-15) |
| **Current vs ATH** | -88.20% |
| **All-Time Low** | $0.00986111 (2020-01-02) |
| **Current vs ATL** | +581.07% |
| **24h Change** | -0.20% |
| **7d Change** | -5.21% |
| **30d Change** | -19.75% |
| **1y Change** | -71.96% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $47.53M |
| **Market Cap Rank** | #31 |
| **24h Range** | $0.0669 — $0.0683 |
| **CoinGecko Sentiment** | 81% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
