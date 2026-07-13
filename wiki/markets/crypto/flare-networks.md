---
title: "Flare"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto]
aliases: ["FLR", "Flare Networks"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://flare.network/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[bitcoin]]", "[[layer-1]]", "[[proof-of-stake]]", "[[oracles]]"]
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
