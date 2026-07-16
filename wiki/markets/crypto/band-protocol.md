---
title: "Band Protocol"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, data-provider, defi, indicators]
aliases: ["BAND", "Band", "Band Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://bandprotocol.com/"
related: ["[[chainlink]]", "[[cosmos]]", "[[crypto-markets]]", "[[data-provider]]", "[[defi]]", "[[ethereum]]"]
---

# Band Protocol

**Band Protocol** (BAND) is a cross-chain data oracle platform that aggregates and connects real-world data and APIs to smart contracts. It is one of the longest-running competitors to [[chainlink|Chainlink]] in the decentralized oracle sector, distinguished by its use of a purpose-built Cosmos-SDK blockchain, **BandChain**, to compute and verify data feeds before relaying them to destination chains such as [[ethereum|Ethereum]]. It ranks **#657** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, BAND trades at **$0.16366** with a market cap of roughly **$29.05M** (rank **#657**). The token was down **-0.51%** over 24 hours and down **-3.78%** over the trailing 7 days, consistent with the broader bear-market regime ([[bitcoin|BTC]] near $64,508, with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at 21 — "Extreme Fear"). BAND remains roughly 99% below its April 2021 all-time high near $22.83, reflecting the deep multi-year drawdown across mid-cap oracle and infrastructure tokens.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BAND |
| **Market Cap Rank** | #657 |
| **Market Cap** | $29,046,899 |
| **Current Price** | $0.16366 |
| **24h Change** | -0.51% |
| **7d Change** | -3.78% |
| **Native Infrastructure** | BandChain (Cosmos-SDK / Tendermint) |
| **Categories** | Oracle, Decentralized Finance (DeFi), Cosmos Ecosystem, Ethereum Ecosystem, Governance |
| **Website** | [https://bandprotocol.com/](https://bandprotocol.com/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Band Protocol solves the oracle problem: smart contracts cannot natively access off-chain data (prices, weather, sports results, API responses), yet most [[defi|DeFi]] applications depend on accurate external inputs. Band aggregates data from multiple independent sources, reaches consensus on a value, and delivers a cryptographically verifiable result to the requesting smart contract, reducing single-source and counterparty risk.

Band's flagship product family has evolved through several versions. Its current architecture (Band 2.0 onward) runs oracle computation on **BandChain**, a dedicated public blockchain built with the Cosmos SDK and Tendermint consensus. Off-chain data is fetched and aggregated by BandChain validators according to programmable **oracle scripts**, then proofs are relayed cross-chain to consumer networks. This design lets Band serve many destination chains while keeping the heavy data-aggregation work off the (more expensive) destination chain itself.

---

## Architecture and Mechanism

- **BandChain** — a Cosmos-SDK blockchain where validators stake BAND, run data-source and oracle-script execution, and produce signed, verifiable data results. Building oracle logic as on-chain scripts is a key differentiator from competitors that rely primarily on off-chain node operators.
- **Data sources and oracle scripts** — developers define *data sources* (how to query an API) and *oracle scripts* (how to aggregate and post-process multiple source results). This composability lets the network support custom feeds beyond simple price data.
- **Cross-chain relay** — results computed on BandChain are relayed with Merkle proofs to destination chains, where a lightweight verifier confirms authenticity before a contract consumes the value.
- **Validator set and staking** — BAND is staked by validators and delegators; honest data provision is incentivized by staking rewards and penalized via slashing for misbehavior.

### Token Role of BAND

BAND is the native [[governance-token|governance and staking]] asset of the network. It is used to:

1. **Secure BandChain** — validators bond BAND and earn rewards for producing valid oracle results; delegators stake to validators.
2. **Pay for / settle data requests** — the token underpins the economic flow for oracle queries on the network.
3. **Govern** — BAND holders vote on protocol parameters and upgrades.

### Value Accrual

Band's token-value thesis rests on **fee demand from oracle queries** flowing back to BAND stakers, in the same spirit as [[chainlink|Chainlink]]'s "staking + fee" roadmap. In practice, much of the recurring reward to validators and delegators is paid from **block emissions / inflationary staking rewards** rather than organic data-request fees, because paid query volume across the decentralized-oracle sector remains small relative to the value secured. This creates the classic infrastructure-token tension: the network is genuinely useful, but the link between *usage* and *token cash flow* is weak until query fees scale. Investors should treat BAND primarily as a **staked-infrastructure / governance** asset whose upside depends on (a) BandChain query volume growing and (b) a larger share of that fee flow being routed to stakers rather than subsidised by emissions.

### Standard Dataset (Band Standard Reference)

A practical pillar of Band's product is the **Standard Reference Dataset** — a curated set of widely-used price feeds (e.g., BTC/USD, ETH/USD, major stablecoins, FX pairs) maintained as ready-to-consume oracle scripts. Rather than every dApp authoring its own data sources and aggregation logic, integrators read from these vetted reference feeds, lowering the barrier to using Band as a drop-in [[chainlink|Chainlink]] alternative.

---

## Worked Example: How a Price Request Flows Through Band

Consider a lending dApp on [[ethereum|Ethereum]] that needs a fresh ETH/USD price to decide whether to liquidate a loan:

1. **Request** — the dApp's smart contract emits a request that references a Band **oracle script** (e.g., "median of ETH/USD from 8 exchange APIs").
2. **Off-chain fetch** — BandChain validators independently call the listed **data sources** (the exchange APIs), each retrieving a raw price.
3. **Aggregation on BandChain** — the oracle script computes the agreed result (e.g., the median) and BandChain validators reach Tendermint consensus on the value, producing a signed, finalised data result. Validators that report dishonestly risk **slashing** of their bonded BAND.
4. **Cross-chain relay** — the result, together with a **Merkle proof**, is relayed to Ethereum.
5. **On-chain verification** — a lightweight Band verifier contract on Ethereum checks the Merkle proof against BandChain's known validator set, then hands the trusted price to the lending dApp, which proceeds with (or cancels) the liquidation.

The key design point: the expensive multi-source aggregation happens on cheap, purpose-built BandChain, and only a compact *proof* is posted to the costly destination chain — the inverse of pushing every raw update on-chain.

---

## History

- **2017** — Band Protocol founded; early product focused on bonding-curve-based community tokens before pivoting to oracle infrastructure.
- **2019** — BAND token sale conducted via Binance Launchpad (IEO); backed by investors including Sequoia Capital (India) and what was then Binance Labs.
- **2020 (Band 2.0)** — Launch of BandChain, moving oracle computation onto a dedicated Cosmos-SDK chain; integrations expand across EVM and Cosmos ecosystems.
- **2021** — BAND reached its all-time high near $22.83 during the broad crypto bull market.
- **2022–2026** — Like most mid-cap oracle tokens, BAND retraced heavily during successive bear phases; the project has repositioned its messaging toward data infrastructure for both blockchains and AI/LLM applications.

---

## Governance

BandChain is governed through standard **Cosmos-SDK on-chain governance**: BAND holders (and their delegated validators) submit and vote on proposals — parameter changes, software upgrades, community-pool spending, and validator-set policy — with voting power proportional to staked BAND. Because the security model is delegated proof-of-stake, **validator concentration** is a real governance consideration: a small number of large validators can carry disproportionate weight in both block production and proposal outcomes, a risk common to Cosmos chains. Token holders who delegate rather than self-validate effectively outsource their data-integrity and governance trust to their chosen validator.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 174.18M BAND |
| **Total Supply** | 174.58M BAND |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $37.21M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $22.83 (2021-04-15) |
| **Current vs ATH** | -99.07% |
| **All-Time Low** | $0.1942 (2026-02-28) |
| **Current vs ATL** | +9.75% |
| **24h Change** | -2.00% |
| **7d Change** | +1.23% |
| **30d Change** | +1.33% |
| **1y Change** | -63.86% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xba11d00c5f74255f56a5e366f4f77f5a186d7f55` |
| Fantom | `0x46e7628e8b4350b2716ab470ee0ba1fa9e76c6c5` |
| Osmosis | `ibc/F867AE2112EFE646EC71A25CD2DFABB8927126AC1E19F1BBF0FF693A4ECA05DE` |
| Energi | `0xb2ef65460bf71a05d59fdf5e8f114a32d445d164` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BAND/USDT | N/A |
| Kraken | BAND/USD | N/A |
| Bitget | BAND/USDT | N/A |
| KuCoin | BAND/USDT | N/A |
| Crypto.com Exchange | BAND/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Sushiswap | 0XBA11D00C5F74255F56A5E366F4F77F5A186D7F55/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V2 (Ethereum) | 0XBA11D00C5F74255F56A5E366F4F77F5A186D7F55/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bandprotocol.com/](https://bandprotocol.com/) |
| **Twitter** | [@bandprotocol](https://twitter.com/bandprotocol) |
| **Reddit** | [https://www.reddit.com/r/bandprotocol](https://www.reddit.com/r/bandprotocol) |
| **Telegram** | [bandprotocol](https://t.me/bandprotocol) (4,867 members) |
| **Discord** | [https://discord.bandprotocol.com/](https://discord.bandprotocol.com/) |
| **GitHub** | [https://github.com/bandprotocol/](https://github.com/bandprotocol/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 222 |
| **GitHub Forks** | 51 |
| **Pull Requests Merged** | 910 |
| **Contributors** | 19 |

---

## Competitive Position

Band competes directly with [[chainlink|Chainlink]], the dominant decentralized oracle provider, as well as [[dia-data|DIA]], Pyth, API3 and others. Band's relative strengths are its Cosmos-native design (well-suited to the Cosmos/IBC ecosystem and to custom, non-price data feeds) and its on-chain oracle-script model. Its principal challenge is the same one facing all Chainlink alternatives: oracle integrations exhibit strong network effects, and Chainlink's incumbency advantage in total value secured and integration count is large. Band's market cap (~$29M) is a small fraction of the leading oracle provider's.

### Oracle Provider Comparison

| Provider | Architecture | Data delivery model | Notable strengths | Relative position |
|---|---|---|---|---|
| **Band Protocol (BAND)** | Dedicated Cosmos-SDK chain (BandChain) computes feeds; cross-chain relay with Merkle proofs | Mostly **pull / request-based**, plus standard reference feeds | Custom oracle scripts; Cosmos/IBC-native; cheap off-chain aggregation | Small mid-cap challenger (~$29M) |
| **[[chainlink|Chainlink]] (LINK)** | Decentralized off-chain node networks (DONs); on/off-chain reporting (OCR) | **Push** (data feeds) + functions, CCIP, VRF | Dominant integration count, highest total value secured, broadest product suite | Sector leader by a wide margin |
| **Pyth Network (PYTH)** | First-party publisher model (exchanges/market-makers push prices) on Pythnet; pull oracle | **Pull** (on-demand) with sub-second updates | Institutional first-party data, very low latency, strong on Solana/L2s | Leading low-latency price oracle |
| **API3 (API3)** | First-party "Airnode" — data providers run their own oracle nodes (dAPIs) | Push/pull; OEV (oracle-extractable-value) recapture | Removes middleman node layer; provider accountability | Niche first-party challenger |
| **[[dia-data|DIA]]** | Open-source, transparent sourcing; customizable feeds | Pull/push; bespoke feeds | Transparency, long-tail and custom asset coverage | Small specialist challenger |

The broad industry shift toward **pull / first-party** oracles (Pyth, API3) is a strategic headwind for both Band and Chainlink's older push-feed model, even as Chainlink's overall incumbency remains dominant.

---

## Risks

- **Competitive / network-effect risk** — the oracle market is winner-take-most; an entrenched leader (Chainlink) commands the majority of integrations and total value secured, limiting Band's addressable share.
- **Oracle integrity risk** — like any oracle, Band is a potential attack surface: manipulated source data, relay-verification bugs, or validator collusion could feed bad prices into dependent [[defi|DeFi]] protocols.
- **Liquidity / small-cap risk** — at a sub-$30M market cap and rank ~#658, BAND is thinly traded relative to large caps; slippage and volatility are elevated and the asset is sensitive to broad [[bitcoin|BTC]]-led risk sentiment.
- **Demand / fee-capture risk** — token value ultimately depends on sustained demand for paid oracle queries; if usage does not grow, staking rewards rely more on emissions than on organic fee revenue.
- **General crypto risk** — smart-contract vulnerabilities, regulatory shifts, and bear-market drawdowns (BAND is ~99% below its 2021 ATH).

*Nothing here is investment advice; figures are point-in-time snapshots that can change rapidly.*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[chainlink]]
- [[dia-data]]
- [[defi]]
- [[data-provider]]
- [[cosmos]]
- [[proof-of-stake]]
- [[staking]]
- [[governance-token]]
- [[fear-and-greed-index]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific narrative wiki source ingested yet.

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.64M |
| **Market Cap Rank** | #652 |
| **24h Range** | $0.1658 — $0.1704 |
| **CoinGecko Sentiment** | 75% positive |
| **Last Updated** | 2026-07-16 |

---
