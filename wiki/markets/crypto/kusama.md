---
title: "Kusama"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["KSM"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://kusama.network/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[polkadot]]", "[[proof-of-stake]]"]
---

# Kusama

**Kusama** (ticker **KSM**) is a public [[layer-1]] blockchain that runs essentially the same codebase as [[polkadot]], serving as Polkadot's **canary network** — a real-economic, lower-stakes proving ground where new features, runtime upgrades, and parachains are tested under live conditions before reaching Polkadot. Because of its experimental "expect chaos" ethos, Kusama iterates faster and with lower governance friction than its mainnet sibling. KSM is the native [[proof-of-stake]] token, used for staking, parachain-slot bonding, fees, and governance on the Kusama relay chain.

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | KSM |
| **Current Price** | $3.49 |
| **Market Cap** | $64,255,905 |
| **Market Cap Rank** | #376 |
| **24h Volume** | $4,950,099 |
| **24h Change** | +0.13% |
| **7d Change** | -5.71% |
| **All-Time High** | $621.71 (2021-05-18) — **-99.4%** |
| **All-Time Low** | $0.877 (2020-01-14) |
| **Categories** | Smart Contract Platform, Polkadot Ecosystem, Proof of Stake (PoS), Pantera Capital Portfolio, Coinbase 50 Index |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Macro backdrop:** The 2026-06-21 snapshot is in an *Established Bear Market* with the [[fear-and-greed-index|Crypto Fear & Greed Index]] at **23 (extreme fear)**. KSM was roughly flat over 24h but underperformed over the prior week (-5.71% 7d) and remains down ~99.4% from its 2021 all-time high — a multi-year drawdown that mirrors the broader decline of the [[polkadot]] ecosystem.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~18.39M KSM |
| **Total Supply** | ~18.39M KSM |
| **Max Supply** | Uncapped (inflationary, ~10%/yr target) |
| **Fully Diluted Valuation** | ~$64.3M |
| **Market Cap / FDV Ratio** | ~1.00 |

KSM is fully circulating (MC/FDV ≈ 1.00) and inflationary, with a target annual issuance (historically around ~10%) split between staking rewards and the on-chain treasury. KSM secures the network through Nominated [[proof-of-stake]] (NPoS): holders nominate validators and earn staking rewards, while un-staked supply is diluted by inflation. KSM is also used to bond/lease **parachain slots** (via crowdloans/auctions), to pay transaction fees, and to vote in Kusama's fast on-chain governance.

**Dilution note:** Because issuance is uncapped, the *real* yield to a holder is staking reward minus inflation. A nominator who stakes captures roughly the network inflation rate; an un-staked holder is diluted at roughly that same rate. This makes staking near-mandatory for passive holders simply to preserve their proportional share — a structural drag distinct from supply-capped assets like [[bitcoin]] or [[ravencoin]].

---

## Market Structure & Derivatives

### Spot venues

| Exchange | Pair | Type |
|---|---|---|
| Binance | KSM/USDT | CEX spot |
| Kraken | KSM/USD | CEX spot |
| Bitget | KSM/USDT | CEX spot |
| KuCoin | KSM/USDT | CEX spot |
| Crypto.com Exchange | KSM/USD | CEX spot |
| Hydration (Polkadot DeFi) | KSM pools | DEX / on-chain |

KSM trades on major CEXs including Binance and Kraken. A representation also exists within the Polkadot/Hydration DeFi ecosystem (Hydration asset registry `asset_registry%2F1000771`), allowing on-chain swaps inside the Polkadot ecosystem. ~$4.95M in 24h volume against a ~$64M cap is modest turnover (~8% of cap), so order books are shallow and slippage on size is material.

**Derivatives.** No active perpetual/derivatives listing on [[hyperliquid]] is recorded in the current snapshot. KSM perps have historically appeared on large CEX futures venues (e.g., Binance, OKX) but with thin open interest; [[funding-rate]] and open-interest dynamics are not a primary price driver for KSM the way they are for the larger-cap perp-listed alts. Confirm any live perp depth on-venue before sizing.

---

## Technology & Consensus

Kusama shares Polkadot's architecture, built on the Substrate framework and the Polkadot SDK:

- **Relay chain + parachains:** a central relay chain provides shared security and consensus, while specialized **parachains** connect to it for scalable, app-specific execution and cross-chain messaging (XCM).
- **Nominated Proof-of-Stake (NPoS):** validators are selected and backed by nominators; both earn rewards for honest participation under [[proof-of-stake]] security.
- **GRANDPA + BABE:** the chain uses BABE for block production and GRANDPA for finality.
- **Forkless upgrades:** on-chain governance can enact runtime upgrades without hard forks — and on Kusama these ship faster and more aggressively than on [[polkadot]].

---

## Use Case, Narrative & Category

Kusama's narrative is the **"canary network" for Polkadot** — a live, real-value sandbox where teams deploy and battle-test parachains, runtime changes, and governance experiments before committing to the more conservative Polkadot mainnet. It anchors a distinct ecosystem of experimental parachains and is positioned within the [[polkadot]] / [[layer-1]] interoperability category.

---

## Valuation Framing (qualitative)

KSM is best understood as a **leveraged, higher-beta proxy for the Polkadot thesis**: its value is downstream of whether the Polkadot SDK / parachain model wins meaningful interoperability share against alternatives ([[ethereum]] L2s, [[cosmos]]-style app-chains). Because KSM is fully circulating and inflationary, there is no unlock overhang to fade — the principal valuation question is whether canary-network demand (parachain auctions, governance experimentation) and staking demand can outpace ~10%/yr issuance. With the chain trading ~99.4% below ATH at a ~$64M cap, the market is pricing Kusama as a deeply out-of-favor experimental sidechain. Any re-rating is tightly coupled to renewed interest in Polkadot itself rather than to a standalone Kusama catalyst.

---

## Peer Comparison

| Asset | Ticker | Mkt-cap rank | Role | Consensus | Supply model | From ATH |
|---|---|---|---|---|---|---|
| **Kusama** | KSM | #376 | Polkadot canary network | NPoS ([[proof-of-stake]]) | Uncapped, inflationary | -99.4% |
| [[polkadot]] | DOT | — (larger cap) | Production relay chain | NPoS | Uncapped, inflationary | deep drawdown |
| [[cosmos]] | ATOM | — | App-chain hub / IBC | Tendermint PoS | Inflationary | deep drawdown |
| [[ethereum]] | ETH | top 2 | General-purpose L1 | PoS | ~Net-flat (EIP-1559 burn) | below ATH |

KSM is the smallest and highest-beta of the interoperability-L1 cohort, sharing Polkadot's exact architecture but with a faster, more chaotic governance cadence.

---

## Notable History

- Launched in 2019 as Polkadot's canary chain, founded by the same Web3 Foundation / Parity Technologies lineage behind [[polkadot]].
- Pioneered **parachain slot auctions** and crowdloans ahead of Polkadot, locking large amounts of KSM in early auctions.
- All-time high of **$621.71** on 2021-05-18; all-time low of **$0.877** on 2020-01-14. Price is down ~99.4% from the 2021 peak as of the 2026-06-21 snapshot.

---

## Risks

- **Experimental by design:** the "expect chaos" mandate means bugs, aggressive upgrades, and governance turbulence are intentional features, not accidents.
- **Dependence on Polkadot's relevance:** KSM's value is tightly coupled to the health and adoption of the broader [[polkadot]] ecosystem.
- **Inflationary supply:** un-staked KSM is diluted by ongoing issuance.
- **Bear-market beta:** as a small-cap alt (rank #376), KSM is highly sensitive to the prevailing extreme-fear regime (F&G 23), and underperformed over the prior week (-5.71% 7d).
- **Liquidity:** ~$4.95M of 24h volume against a ~$64M cap means shallow books and material slippage on larger orders.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[polkadot]]
- [[cosmos]]
- [[layer-1]]
- [[proof-of-stake]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko).

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | KSM |
| **Market Cap Rank** | #382 |
| **Market Cap** | $59.86M |
| **Current Price** | $3.23 |
| **Categories** | Smart Contract Platform, Proof of Stake (PoS), Made in USA |
| **Website** | [https://kusama.network/](https://kusama.network/) |

---

## Overview

Kusama is a public blockchain network that is running the exact same codebase as Polkadot. It is aimed to be a canary build for the Polkadot network which is an experimental and development environment for new features that will eventually be deployed to Polkadot. Because of the experimental nature of Kusama, the developmental speed is much faster and it has seen significant traction since launched in 2019.

Kusama is an early, highly experimental version of Polkadot presenting real economic conditions. The community will own the network – there will be no central kill switch. Kusama will exist as long as its community maintains it and we envision it will cater to new, early functionality and projects preparing to develop and deploy on Polkadot.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 18.52M KSM |
| **Total Supply** | 18.52M KSM |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $59.86M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $621.71 (2021-05-18) |
| **Current vs ATH** | -99.48% |
| **All-Time Low** | $0.8766 (2020-01-14) |
| **Current vs ATL** | +268.87% |
| **24h Change** | -2.12% |
| **7d Change** | -1.52% |
| **30d Change** | -15.06% |
| **1y Change** | -79.21% |

---

## Platform & Chain Information

**Native Chain:** Multiple chains (see contract addresses below)

### Contract Addresses

| Chain | Address |
|---|---|
| Hydration | `asset_registry%2F1000771` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | KSM/USDT | N/A |
| Kraken | KSM/USD | N/A |
| Bitget | KSM/USDT | N/A |
| KuCoin | KSM/USDT | N/A |
| Crypto.com Exchange | KSM/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://kusama.network/](https://kusama.network/) |
| **Twitter** | [@kusamanetwork](https://twitter.com/kusamanetwork) |
| **GitHub** | [https://github.com/paritytech/polkadot-sdk](https://github.com/paritytech/polkadot-sdk) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 31 |
| **GitHub Forks** | 23 |
| **Commits (4 weeks)** | 8 |
| **Pull Requests Merged** | 33 |
| **Contributors** | 17 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $5.63M |
| **Market Cap Rank** | #382 |
| **24h Range** | $3.23 — $3.37 |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]

---
