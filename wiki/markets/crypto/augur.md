---
title: "Augur"
type: entity
created: 2026-07-16
updated: 2026-07-16
status: draft
tags: [crypto, defi]
aliases: ["REP", "Augur Protocol", "Augur"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "http://www.augur.net/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[polymarket]]", "[[kalshi]]", "[[prediction-markets]]", "[[prediction-market-strategies]]", "[[gnosis]]", "[[uma]]"]
---

# Augur

**Augur** (REP) is a decentralized protocol for prediction markets and oracle resolution, originally launched on the Ethereum network. Prediction markets allow users to trade on the outcome of future events, while oracles bring real-world results onchain so markets can settle correctly.

Augur combines these by using economic incentives to determine outcomes without centralized authorities. It ranks **#1676** by market capitalization.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | REP |
| **Market Cap Rank** | #1676 |
| **Market Cap** | $4.25M |
| **Current Price** | $0.8314 |
| **Categories** | Decentralized Finance (DeFi), Prediction Markets |
| **Website** | [http://www.augur.net/](http://www.augur.net/) |

---

## Overview

Augur is a decentralized protocol for prediction markets and oracle resolution, originally launched on the Ethereum network. Prediction markets allow users to trade on the outcome of future events, while oracles bring real-world results onchain so markets can settle correctly.

Augur combines these by using economic incentives to determine outcomes without centralized authorities. Participants stake value on outcomes, and incorrect positions lose funds while correct ones are rewarded.

Following a 2025 revival led by the Lituus Foundation, development now spans two tracks: a new prediction market system and Augur Lituus, a generalized oracle designed as infrastructure for other applications.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 5.12M REP |
| **Total Supply** | 5.12M REP |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $4.25M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $341.85 (2016-02-10) |
| **Current vs ATH** | -99.76% |
| **All-Time Low** | $0.00000000 (2016-01-22) |
| **Current vs ATL** | +0.00% |
| **24h Change** | -6.64% |
| **7d Change** | +5.85% |
| **30d Change** | +0.74% |
| **1y Change** | +20.99% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x221657776846890989a759ba2973e427dff5c9bb` |
| Energi | `0x2a2666f62157769d09a64488bbb51bd77036f6ce` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | REPV2/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X221657776846890989A759BA2973E427DFF5C9BB/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X221657776846890989A759BA2973E427DFF5C9BB/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [http://www.augur.net/](http://www.augur.net/) |
| **Twitter** | [@AugurProject](https://twitter.com/AugurProject) |
| **Reddit** | [https://www.reddit.com/r/Augur](https://www.reddit.com/r/Augur) |
| **GitHub** | [https://github.com/AugurProject/augur-core](https://github.com/AugurProject/augur-core) |
| **Whitepaper** | [https://bravenewcoin.com/assets/Whitepapers/Augur-A-Decentralized-Open-Source-Platform-for-Prediction-Markets.pdf](https://bravenewcoin.com/assets/Whitepapers/Augur-A-Decentralized-Open-Source-Platform-for-Prediction-Markets.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 587 |
| **GitHub Forks** | 129 |
| **Pull Requests Merged** | 561 |
| **Contributors** | 22 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $7,265.99 |
| **Market Cap Rank** | #1676 |
| **24h Range** | $0.8127 — $0.8965 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Protocol Overview

Augur is a decentralized [[prediction-markets|prediction market]] protocol built on [[ethereum|Ethereum]], launched in July 2018 by the Forecast Foundation. It pioneered the trustless, permissionless prediction-market design that [[polymarket|Polymarket]] and others later refined, using the REP (Reputation) token as the backbone of its staking-based oracle. Once the flagship of on-chain forecasting, Augur went dormant after 2021, eclipsed by Polygon-based and CLOB-style competitors — but a revival effort began in 2025, and in April 2026 the protocol's famous fork backstop was triggered for the first time in production.

### How It Works

Augur lets any user create a market on any future event — elections, sports, asset prices, arbitrary "yes/no" or scalar outcomes. Markets trade as ERC-20 outcome shares that pay 1 unit of collateral if their outcome resolves true, zero otherwise. A complete set of shares always sums to 1 unit of collateral.

Resolution is handled by REP holders acting as decentralized oracles. After an event ends, a designated reporter posts an initial outcome; if disputed, REP holders stake tokens on competing outcomes through escalating dispute rounds. Mis-reporters lose their stake; honest reporters earn fees. In an irreconcilable dispute, the protocol forks: REP splits into outcome-specific universes, and holders must migrate to the universe they believe represents truth.

## Key Milestones

| Date | Event |
|------|-------|
| 2014 | Augur whitepaper published by Jack Peterson and Joey Krug |
| 2015 | Token sale; ~$5.3M raised in REP |
| 2018-07 | V1 launched on Ethereum mainnet |
| 2020-07 | V2 launched: DAI as collateral, invalid-outcome handling, 0x-based order book |
| 2020-11 | Volume peaks around the US presidential election |
| 2021+ | Sharp decline as [[polymarket|Polymarket]] (Polygon L2) captures retail flow |
| 2025 | Revival effort begins; new team resumes development |
| 2026-04 | The Augur fork is triggered — REP holders enter an 8-week escalation game / migration window |

## REP Token Mechanics

REP is the work token used to secure Augur's oracle. Key mechanics:
- **Initial reporting** — designated reporter posts the initial outcome and stakes REP as a bond
- **Disputes** — any holder can dispute by staking REP on an alternative outcome; each round doubles the required stake
- **Forking** — if a dispute exceeds the threshold, the universe forks into one child universe per possible outcome; non-migrating REP becomes worthless in the parent
- **Fees** — settled markets pay reporting fees pro-rata to correctly-staked REP
- **REPv2** — the V2 migration introduced a new REP contract; a non-trivial fraction of REP was never migrated, effectively shrinking active supply

## Comparison to Polymarket

| Dimension | Augur | [[polymarket\|Polymarket]] |
|-----------|-------|----------------------------|
| Chain | Ethereum L1 | Polygon (L2) |
| Collateral | DAI (V2) | USDC |
| Oracle | REP staking + fork | [[uma\|UMA]] optimistic oracle |
| Order matching | On-chain 0x order book | Off-chain CLOB, on-chain settlement |
| Market creation | Permissionless, any user | Curated by Polymarket team |
| Typical fees | Gas-dominated, often >$10/trade in 2020 | Sub-cent on Polygon |
| Resolution speed | Days to weeks | Hours |
| Peak volume | ~$8M monthly (Nov 2020) | $1B+ monthly (2024 US election) |

## Decline and 2025-2026 Reboot

Augur's volume collapsed after the 2020 election cycle due to Ethereum L1 gas costs, slow resolution, UX friction, and Polymarket's superior design. By 2024 the front-end was largely abandoned. In 2025 a revival effort began, and as of mid-2026 REP holders were in week 5 of an 8-week Escalation Game — the first real-world test of the fork backstop. The fork has been formally triggered, with a migration window posted on 2026-04-09.

## Trading Relevance

1. **Historical lessons** — Augur is the canonical case study in why decentralization without UX kills retail adoption; referenced in any analysis of prediction-market design or DeFi product-market fit
2. **Cross-venue arbitrage history** — during 2020, the same election markets traded on Augur, Polymarket, FTX, and PredictIt at 3–8% spreads; gas costs often ate the edge but this is the template for the [[prediction-market-strategies|prediction-market arbitrage]] playbook
3. **Oracle-design reference** — Augur's fork mechanic remains the most security-maximalist oracle design shipped to mainnet; a comparison point for [[uma|UMA]]'s optimistic oracle

REP itself is not a useful trading vehicle in 2026 — too thin, no protocol revenue — though the live fork/escalation game is a binary event some speculators are watching.

## See Also

- [[prediction-markets]]
- [[polymarket]]
- [[kalshi]]
- [[ethereum]]
- [[gnosis]]
- [[uma]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])
- Augur whitepaper (Jack Peterson & Joey Krug, 2014) — https://arxiv.org/abs/1501.01042
- Augur official site (reboot, fork, and migration status) — https://www.augur.net (accessed 2026-06-10)
- CoinMarketCap — REP price and supply data
- Verified via Perplexity (sonar) and direct fetch, 2026-06-10
