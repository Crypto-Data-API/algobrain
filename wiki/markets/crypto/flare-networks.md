---
title: "Flare"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["FLR", "Flare Networks"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://flare.network/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[oracles]]", "[[proof-of-stake]]"]
---

# Flare

**Flare** (FLR) is an EVM-compatible [[layer-1]] blockchain focused on decentralized data and cross-chain interoperability. Its native protocols — the **Flare Time Series Oracle (FTSO)**, the **State Connector**, and the **FAssets** bridging system — are secured by the network itself, letting smart contracts consume high-integrity price feeds and external blockchain/internet data without relying on a single centralized provider. FLR is the network's native [[proof-of-stake]] token.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | FLR |
| **Current Price** | $0.00736535 |
| **Market Cap** | $637,752,721 |
| **Market Cap Rank** | #89 |
| **24h Volume** | $2,188,141 |
| **24h Change** | +0.31% |
| **7d Change** | -6.98% |
| **All-Time High** | $0.150073 (2023-01-10) |
| **Current vs ATH** | -95.1% |
| **All-Time Low** | $0.0064918 (2026-06-06) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Oracle, DWF Labs Portfolio |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** As of 2026-06-20 the broader market sits in an *Established Bear Market* with the Crypto Fear & Greed Index at **23 (extreme fear)**. FLR is down -7.0% on the week and is trading just above its all-time low of $0.0064918 set on 2026-06-06 — a fresh-low, bleeding-out profile. Its thin ~$2.2M daily volume against a $637M cap signals weak liquidity typical of mid-cap alts during risk-off conditions; slippage risk is elevated for larger size.

---

## Tokenomics & Supply

| Metric | Value (2026-06-20, CoinGecko) |
|---|---|
| **Circulating Supply** | ~86.55B FLR |
| **Total Supply** | ~106.02B FLR |
| **Max Supply** | Uncapped (inflationary) |
| **Fully Diluted Valuation** | ~$781.2M |
| **Market Cap / FDV Ratio** | ~0.82 |

FLR has an **inflationary emission schedule** with no hard cap. The token is used for transaction fees (anti-spam), payments, and staking to validator nodes. FLR can be wrapped into **WFLR** (an ERC-20 variant); WFLR can be delegated to FTSO data providers to earn rewards, or used in governance and across the EVM dApp ecosystem. Staking and FTSO delegation reward holders for securing the network and supplying honest price data, partially offsetting inflation for active participants.

**Dilution flag:** the MC/FDV ratio of **~0.82** means ~18% of value still sits in not-yet-circulating supply, and the uncapped inflationary schedule continues to add tokens over time. Passive holders who do not stake or delegate are diluted by emissions; only active FTSO delegators/stakers offset that drag with rewards.

---

## Protocol / Product

Flare is EVM-based and secured by [[proof-of-stake]]. Its differentiator is **native interoperability and data infrastructure** built into the L1 itself, rather than bolted on via third-party services. Three protocols define it:

### Flare Time Series Oracle (FTSO)

The FTSO delivers **decentralized price and time-series data feeds** to dApps on Flare, sourced from a large set of independent data providers rather than a single centralized oracle. Providers are rewarded (and slashable) for accurate submissions, and FLR/WFLR holders **delegate** to providers to share in rewards. By incentivizing many independent providers to query and process data, the FTSO aims to reduce the single-point-of-failure risk inherent in conventional [[oracles]].

### State Connector

The State Connector enables information from **other blockchains and the internet** to be used trustlessly within Flare smart contracts — verifying that an external event (e.g. a payment on another chain) actually occurred. This is the backbone for cross-chain applications and underpins FAssets.

### FAssets

**FAssets** is Flare's system for bringing **non-smart-contract assets** (e.g. BTC, XRP, DOGE, LTC) onto Flare as collateral-backed, EVM-usable representations (f-assets). Agents lock collateral to mint f-assets against deposited originals, with the State Connector verifying underlying deposits/redemptions. This is Flare's core value proposition: making otherwise "passive" assets programmable and usable in DeFi on an EVM chain, without trusting a centralized custodian/bridge. By building this data and bridging layer natively and incentivizing independent providers, Flare aims to minimize the trust assumptions of conventional oracles and bridges.

---

## Ecosystem & Use Cases

- **Oracle-as-infrastructure:** dApps on Flare consume FTSO feeds directly, avoiding external oracle integration.
- **Cross-chain DeFi:** FAssets let BTC/XRP/DOGE/LTC holders deploy those assets into Flare DeFi (lending, LPs, derivatives) as f-assets.
- **Staking & delegation:** FLR/WFLR delegation to FTSO providers and validator staking is the primary on-chain yield.
- **Governance:** WFLR holders vote on protocol parameters and upgrades.
- **Smart-contract platform:** as an EVM L1, Flare hosts general dApps competing in the broad smart-contract-platform category.

---

## Market Structure & Derivatives

### Spot venues

| Exchange | Pair |
|---|---|
| Kraken | FLR/USD |
| KuCoin | FLR/USDT |
| Crypto.com Exchange | FLR/USD |

FLR trades on several centralized venues. With ~$2.2M in 24h volume at the 2026-06-20 snapshot, order books are relatively thin and slippage risk is elevated for larger size. No active perpetual/derivatives listing on [[hyperliquid]] is recorded in the current snapshot, so leveraged/short expression is limited and price discovery is spot-driven. The combination of thin volume, a fresh all-time low, and extreme-fear macro makes FLR vulnerable to sharp, low-liquidity moves in either direction.

---

## Valuation Framework (qualitative)

FLR is best framed as a **bet on adoption of its native data/interoperability stack**, discounted heavily for inflation and bear-market beta:

1. **Data-network value.** If FTSO becomes a widely used oracle and FAssets attracts meaningful cross-chain TVL, demand for FLR (fees, staking, delegation) grows with usage — a network-value framing.
2. **Inflation drag.** Any fundamental valuation must net out the uncapped emission schedule; passive holders are diluted, so "fair value" is lower than headline network metrics suggest.
3. **Category beta.** FLR competes in two crowded categories (L1 smart-contract platforms and oracles); its multiple should be discounted for the strength of incumbents like [[ethereum]] and established oracle providers.
4. **Regime beta.** As a mid-cap alt it is highly sensitive to the prevailing bear market; in extreme fear it trades at or near lows regardless of fundamentals.

---

## Trading Playbook

- **Adoption-catalyst trade.** Position around FAssets TVL growth, new FTSO integrations, and major dApp launches — these are the structural catalysts that could rerate FLR above its inflation drag.
- **Bear-market caution.** With FLR printing fresh all-time lows in extreme-fear macro and thin liquidity, avoid fighting the downtrend; momentum/trend filters argue against premature bottom-fishing.
- **Yield-offset hold.** Holders who want exposure should stake/delegate FLR to FTSO providers to offset emission dilution rather than holding passively.
- **Liquidity discipline.** ~$2.2M daily volume means scale entries/exits and use limit orders; size for elevated slippage.

---

## Notable History

- Originated as a project to bring smart-contract utility and data interoperability to assets and chains lacking it, with a large airdrop distribution of FLR to qualifying holders.
- All-time high of **$0.150073** on 2023-01-10; the price is down ~95% from that peak as of the 2026-06-20 snapshot.
- All-time low of **$0.0064918** printed on **2026-06-06**, into the broad bear market; FLR trades just above that level on 2026-06-20.

---

## Competitive Positioning

| Project | Category | Distinctive feature | vs Flare |
|---|---|---|---|
| **Flare** | L1 + native oracle + bridge | FTSO, State Connector, FAssets baked into the chain | Data/interop infra is native, not third-party |
| [[ethereum\|Ethereum]] | L1 smart-contract platform | Dominant L1, deepest dev ecosystem | Far larger network effects; relies on external oracles |
| Chainlink (oracle) | Oracle network | Dominant cross-chain oracle, off-chain reporting | Flare embeds oracle natively rather than as a service |
| Other interop L1s | L1 + bridging | Various cross-chain designs | Flare's FAssets targets non-smart-contract assets specifically |

Flare's differentiation is **owning the data/interoperability layer at the protocol level** rather than depending on external oracle and bridge providers. Its challenge is that it competes simultaneously against incumbent L1s (network effects) and incumbent oracle providers (adoption), and must drive FAssets/FTSO usage faster than emissions dilute holders.

---

## Risks

- **Inflationary supply:** uncapped emissions dilute holders who do not stake/delegate.
- **Thin liquidity:** ~$2.2M daily volume makes the token vulnerable to volatility and slippage, especially in the current extreme-fear regime.
- **Fresh lows / downtrend:** FLR set a new all-time low on 2026-06-06 and trades near it — weak momentum.
- **Competition:** the oracle and L1 spaces are crowded; adoption of FTSO/FAssets/State Connector must outpace incumbents.
- **Beta to market regime:** as a mid-cap alt, FLR is highly sensitive to the prevailing bear market.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[layer-1]]
- [[proof-of-stake]]
- [[oracles]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- CoinGecko / cryptodataapi.com snapshot, 2026-06-20 (market data baseline).

## What is Flare (FLR)?

Flare is an EVM-based Layer 1 blockchain designed to allow developers to build applications that are interoperable with blockchains and the internet. By providing decentralized access to high-integrity data, Flare enables new use cases and monetisation models.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | FLR |
| **Market Cap Rank** | #94 |
| **Market Cap** | $571.00M |
| **Current Price** | $0.00657701 |
| **Categories** | Smart Contract Platform, Layer 1 (L1) |
| **Website** | [https://flare.network/](https://flare.network/) |

---

## Overview

Flare is a blockchain for building applications that are interoperable with other blockchains and the internet.

## What makes Flare unique?

Flare's native interoperability protocols, the State Connector and the FTSO are secured by the network itself, allowing it to reliably deliver data from a wide variety of off-chain sources in a decentralized way. 

The Flare Time Series Oracle delivers highly-decentralized price and data feeds to dapps on Flare, without relying on centralized providers. 

The State Connector protocols enable information, both from other blockchains and the internet to be used securely, scalably and trustlessly with smart contracts on Flare.

Risk is minimized by building this decentralized data infrastructure natively into the blockchain, powered by a large number of independent data providers.

By incentivizing sets of independent providers to query, acquire, and process data without relying on single, centralized sources, Flare’s core protocols can facilitate the development of interoperable dapps with a broad range of potential innovative use cases.

## What is the Flare (FLR) token used for?

FLR is the native token used for payments, transaction fees to prevent spam attacks and staking in validator nodes. FLR can also be wrapped into an ERC-20 variant, WFLR. WFLR tokens serve various functions; they can be delegated to FTSO data providers, for example, or staked to participate in governance. These two uses are not mutually exclusive and do not prevent the tokens from being used in other EVM-compatible dapps and smart contracts on Flare.

Wrapped FLR (WFLR) can be minted by depositing native FLR tokens into a smart contract and withdrawing the newly minted

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 86.81B FLR |
| **Total Supply** | 106.18B FLR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $698.37M |
| **Market Cap / FDV Ratio** | 0.82 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1501 (2023-01-10) |
| **Current vs ATH** | -95.62% |
| **All-Time Low** | $0.00633330 (2026-07-13) |
| **Current vs ATL** | +3.74% |
| **24h Change** | -0.75% |
| **7d Change** | -0.34% |
| **30d Change** | -17.81% |
| **1y Change** | -62.41% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | FLR/USD | N/A |
| KuCoin | FLR/USDT | N/A |
| Crypto.com Exchange | FLR/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://flare.network/](https://flare.network/) |
| **Twitter** | [@FlareNetworks](https://twitter.com/FlareNetworks) |
| **Reddit** | [https://www.reddit.com/r/FlareNetworks](https://www.reddit.com/r/FlareNetworks) |
| **Telegram** | [FlareNetwork](https://t.me/FlareNetwork) (16,262 members) |
| **Discord** | [https://discord.com/invite/flarenetwork](https://discord.com/invite/flarenetwork) |
| **Whitepaper** | [https://flare.network/whitepapers](https://flare.network/whitepapers) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.75M |
| **Market Cap Rank** | #94 |
| **24h Range** | $0.00654529 — $0.00671265 |
| **CoinGecko Sentiment** | 60% positive |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
