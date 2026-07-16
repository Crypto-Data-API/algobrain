---
title: "DIA"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, data-provider, defi, indicators]
aliases: ["DIA", "DIA Data", "DIAdata"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://diadata.org/"
related: ["[[band-protocol]]", "[[chainlink]]", "[[crypto-markets]]", "[[data-provider]]", "[[defi]]", "[[ethereum]]", "[[real-world-assets]]"]
---

# DIA

**DIA** (Decentralised Information Asset) is an open-source, transparent data oracle network that supplies customizable, fully traceable price and information feeds to smart contracts across many blockchains. Its defining feature versus competitors such as [[chainlink|Chainlink]] and [[band-protocol|Band Protocol]] is **transparency and customizability**: DIA sources raw trade data directly from a large number of on-chain and centralized venues and lets integrators tailor a feed's source set, methodology, and update frequency rather than consuming a one-size-fits-all aggregate. It ranks **#981** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, DIA trades at **$0.118947** with a market cap of about **$14,234,817** (rank **#981**). The token was down **-1.61%** over 24 hours and down **-5.92%** over the trailing 7 days, in line with an "Extreme Fear" market regime (Fear & Greed Index **21**). DIA remains well below its 2021 high near $5.73.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | DIA |
| **Market Cap Rank** | #981 |
| **Market Cap** | $14,234,817 |
| **Current Price** | $0.118947 |
| **24h Change** | -1.61% |
| **7d Change** | -5.92% |
| **Categories** | Oracle, Infrastructure, Decentralized Finance (DeFi), Real World Assets (RWA), Ethereum Ecosystem, BNB Chain Ecosystem |
| **Website** | [https://diadata.org/](https://diadata.org/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

DIA addresses the oracle problem with a model built around openness. Rather than delivering opaque aggregated values, DIA's pipeline collects raw, individual trade data from a wide set of exchanges and on-chain pools and applies transparent, auditable methodologies (e.g., volume-weighted averages, median filters, configurable windows) to produce a price. Integrators can inspect exactly which sources and which computation produced any given value, and can request bespoke feeds suited to their asset's liquidity profile.

This emphasis on **traceability and customization** positions DIA particularly for long-tail and newly launched assets, [[real-world-assets|RWA]] tokenization, NFT-floor pricing, and other use cases where standard major-asset price feeds are insufficient. The DIA token is the network's utility and [[governance-token|governance]] asset, used to incentivize honest data provision, secure the data pipeline through staking, and govern protocol parameters.

---

## Architecture and Mechanism

- **Open, multi-source data collection** — DIA scrapes raw trade-level data directly from numerous centralized and decentralized venues, rather than relying on pre-aggregated third-party APIs. This reduces dependence on any single data vendor.
- **Transparent, customizable methodologies** — feed consumers can configure the source basket and computation method; every published value is intended to be reproducible from public inputs.
- **Cross-chain delivery** — DIA publishes feeds to a broad set of blockchains, enabling [[defi|DeFi]] protocols on many networks to consume the same transparent pipeline.
- **Token-secured pipeline** — the DIA token underpins staking and incentive mechanisms designed to align data providers and node operators with feed accuracy, and to govern the network.

> *Note: claims of exact source/asset/chain counts are project marketing figures and are not independently verified here; they are described qualitatively rather than asserted as precise facts.*

---

## Competitive Position

DIA competes with [[chainlink|Chainlink]] (the market leader), [[band-protocol|Band Protocol]], Pyth, API3 and others. Its differentiation is methodological transparency and per-feed customization, which appeals to projects needing oracles for assets the incumbents do not cover well, and to teams that want to audit exactly how a price is formed. As with all oracle challengers, DIA faces strong incumbent network effects and a much smaller share of total value secured; at ~$14.2M market cap (rank ~#981) it is a small-cap relative to the sector leader.

| Oracle | Data sourcing model | Update / delivery model | Distinguishing angle | Relative scale |
|---|---|---|---|---|
| **DIA** | First-party scraping of raw trade data from many CEX/DEX venues | Customizable: per-feed source basket, methodology, frequency; push to many chains | Transparency + bespoke long-tail/RWA/NFT feeds | Small-cap challenger |
| **[[chainlink\|Chainlink]]** | Decentralized node operators sourcing from data aggregators | Push (heartbeat/deviation); CCIP, Data Streams | Largest integration moat; broad DeFi standard | Market leader |
| **Pyth** | First-party data from exchanges/market makers (publishers) | Pull (on-demand), low-latency; cross-chain via wormhole | Institutional first-party price publishers, sub-second | Major, fast-growing |
| **[[band-protocol\|Band Protocol]]** | Validator-sourced via Cosmos-based oracle chain | Pull/push, cross-chain (IBC) | Cosmos-native; customizable scripts | Smaller |
| **API3** | First-party "Airnode" feeds run by data providers themselves | Push; OEV (oracle-extractable-value) auctions | Provider-operated feeds, dAPIs, OEV capture | Niche |

DIA's clearest wedge is **assets the majors under-serve** — newly launched tokens, long-tail pairs, [[real-world-assets|RWA]] pricing, NFT-floor feeds — plus full auditability of how a number was computed. The trade-off is that transparency does not by itself overcome Chainlink/Pyth integration network effects, so DIA's growth depends on niches where customization is decisive.

### Data pipeline and value accrual

- **First-party, raw-trade sourcing.** DIA's open-source pipeline ingests trade-level data directly from venues, then applies transparent, reproducible transforms (VWAP, medians, configurable windows) — the published value can in principle be re-derived from public inputs, the core of its "transparent oracle" claim.
- **Token utility.** The DIA token is used for [[governance-token|governance]] and to underpin staking/incentive mechanisms intended to align data providers and node operators with feed accuracy.
- **Fee-capture dependency.** Token value ultimately hinges on sustained *paid* demand for feeds. If integration revenue does not grow, economics lean on emissions/incentives rather than usage fees — a common challenge for infrastructure tokens.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 119.68M DIA |
| **Total Supply** | 168.82M DIA |
| **Max Supply** | 200.00M DIA |
| **Fully Diluted Valuation** | $30.13M |
| **Market Cap / FDV Ratio** | 0.71 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $5.73 (2021-05-05) |
| **Current vs ATH** | -96.88% |
| **All-Time Low** | $0.1613 (2026-03-28) |
| **Current vs ATL** | +10.81% |
| **24h Change** | -4.77% |
| **7d Change** | +3.67% |
| **30d Change** | +0.18% |
| **1y Change** | -41.48% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x84ca8bc7997272c7cfb4d0cd3d55cd942b3c9419` |
| Sora | `0x001f7a13792061236adfc93fa3aa8bad1dc8a8e8f889432b3d8d416b986f2c43` |
| Binance Smart Chain | `0x99956d38059cf7beda96ec91aa7bb2477e0901dd` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | DIA/USDT | N/A |
| KuCoin | DIA/USDT | N/A |
| Crypto.com Exchange | DIA/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Sushiswap | 0X84CA8BC7997272C7CFB4D0CD3D55CD942B3C9419/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |
| Uniswap V2 (Ethereum) | 0X84CA8BC7997272C7CFB4D0CD3D55CD942B3C9419/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X84CA8BC7997272C7CFB4D0CD3D55CD942B3C9419/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://diadata.org/](https://diadata.org/) |
| **Twitter** | [@DIAdata_org](https://twitter.com/DIAdata_org) |
| **Reddit** | [https://www.reddit.comr/DIAdata](https://www.reddit.comr/DIAdata) |
| **Telegram** | [DIAdata_org](https://t.me/DIAdata_org) (5,496 members) |
| **Discord** | [https://discord.com/invite/zFmXtPFgQj?utm_source=CG](https://discord.com/invite/zFmXtPFgQj?utm_source=CG) |
| **GitHub** | [https://github.com/diadata-org/diadata](https://github.com/diadata-org/diadata) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 253 |
| **GitHub Forks** | 135 |
| **Commits (4 weeks)** | 2 |
| **Pull Requests Merged** | 409 |
| **Contributors** | 77 |

---

## Risks

- **Competitive / network-effect risk** — the oracle market is dominated by [[chainlink|Chainlink]]; transparent/customizable feeds are a real differentiator but must overcome the incumbent's integration moat.
- **Oracle integrity risk** — any oracle is a manipulation target. Although DIA's openness aids auditing, thinly traded long-tail assets are inherently easier to manipulate at the source, which can propagate into dependent [[defi|DeFi]] contracts.
- **Liquidity / small-cap risk** — at ~$14.5M market cap (rank ~#971), DIA is small and volatile; it is highly sensitive to broad [[bitcoin|BTC]]-led sentiment and can suffer meaningful slippage.
- **Demand / fee-capture risk** — token value depends on sustained, paid demand for feeds; absent organic usage growth, token economics lean on incentives rather than revenue.
- **General crypto risk** — smart-contract bugs, regulatory uncertainty, and prolonged bear-market drawdowns.

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
- [[band-protocol]]
- [[defi]]
- [[data-provider]]
- [[real-world-assets]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko); Fear & Greed Index 21 (Extreme Fear).
- General market knowledge; no specific narrative wiki source ingested yet.

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.03M |
| **Market Cap Rank** | #1050 |
| **24h Range** | $0.1024 — $0.1054 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---
