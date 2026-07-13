---
title: "WAX"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, nft, altcoins]
aliases: ["WAXP", "Worldwide Asset eXchange"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://wax.io/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]"]
---

# WAX

**WAX** (Worldwide Asset eXchange, token WAXP) is a [[layer-1|layer-1]] blockchain purpose-built for gaming, NFTs, and digital collectibles, designed to make e-commerce and asset transactions fast and fee-less for end users. It uses **Delegated [[proof-of-stake]] (DPoS)** consensus, is technically descended from / backward-compatible with EOS, and markets itself as carbon-neutral. WAX is best known as a high-volume NFT and gaming chain (home to titles like Alien Worlds and Splinterlands-era collectibles) and for features like the WAX Cloud Wallet and **vIRL** NFTs that link to physical items. It ranks **#823** by market capitalization.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).* WAXP trades at **$0.00437716**, market cap **$20,247,724** (rank **#823**), up **+3.45%** over 24h and down **-5.11%** over 7 days, in a broad bear-market regime (BTC ~$64,390).

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | WAXP |
| **Market Cap Rank** | #823 |
| **Market Cap** | $20,247,724 |
| **Current Price** | $0.00437716 |
| **24h Change** | +3.45% |
| **7d Change** | -5.11% |
| **Genesis Date** | 2017-12-19 |
| **Consensus** | Delegated Proof-of-Stake (DPoS) |
| **Categories** | Gaming (GameFi), NFT, Layer 1 (L1), Play To Earn, Gaming Blockchains, Smart Contract Platform, Wax Ecosystem |
| **Website** | [https://wax.io/](https://wax.io/) |
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

---

## Overview

WAX is a purpose-built [[layer-1]] blockchain designed to make digital-asset and e-commerce transactions fast and frictionless, with a focus on gaming and NFTs. It uses Delegated [[proof-of-stake]] (DPoS) consensus and is technically related to EOS (sharing its antelope/EOSIO lineage). The chain's custom incentive mechanisms encourage holders to vote for "guilds" (block producers) and proposals.

WAX provides a suite of tools on which dApps, marketplaces, and native non-fungible tokens (NFTs) are built: the WAX Cloud Wallet (email/social onboarding), SSO and OAuth integrations, a native on-chain RNG service (useful for games and provably fair mechanics), and a developer portal. The chain is marketed as effectively fee-less for end users (with resource costs largely abstracted away) and as carbon-neutral.

---

## Architecture & Consensus (deep dive)

WAX is an [[eos|EOSIO/Antelope]]-family chain: it forked the EOS codebase, retaining its account model, C++ smart-contract framework, and resource economics, while customizing consensus and adding NFT-native primitives. The key components:

- **Delegated Proof of Stake (DPoS):** WAXP holders stake and vote to elect a limited set of ~21 active block producers ("guilds") plus standby producers that secure the chain. DPoS prioritizes high throughput (sub-second block times, claimed thousands of TPS) at the cost of a smaller, elected validator set — the classic centralization/decentralization trade-off common to EOS-family chains. Guilds also run infrastructure (RPC nodes, history APIs, IPFS) and are paid from inflation.
- **WAX-specific consensus additions:** WAX layered on **WAX Stake-Weighted Voting** and a planned **WAX Proof of Stake (WPS)** / OIG (Object Identification Game) reward design intended to distribute rewards to active participants beyond just guilds. Treat exact mechanics as project-stated and verify against current documentation.
- **Resource model:** like EOS, WAX uses a CPU/NET/RAM resource model. Users (or dApps via "fee-less" sponsorship and resource staking) reserve compute/bandwidth by staking WAXP rather than paying a per-transaction gas fee in the conventional Ethereum sense — this is what enables the "fee-less for end users" UX.
- **NFT-native stack:** WAX is closely tied to the **AtomicAssets** NFT standard and the **AtomicHub** marketplace (community-built but ecosystem-central), giving it a mature, low-cost minting and trading layer. On-chain **RNG (WAX RNG)** provides provably fair randomness for game mechanics (loot, packs). **vIRL** NFTs link a digital token to a redeemable physical good.
- **Cloud Wallet & onboarding:** the **WAX Cloud Wallet** abstracts key management behind email/social login, a major UX differentiator for mainstream gaming audiences versus seed-phrase wallets like [[metamask|MetaMask]].
- **Carbon-neutral positioning:** as a PoS/DPoS chain, WAX consumes a tiny fraction of the energy of proof-of-work chains and markets itself as carbon-neutral.

DAG ledgers and monolithic L1s aside, WAX's bet is that abstracting fees and keys is more important for consumer/gaming adoption than maximal decentralization.

---

## What the WAXP Token Does (value accrual & governance)

- **Staking & resources:** WAXP is staked to reserve network resources (CPU/NET/RAM model) and to power dApp "fee-less" sponsorship.
- **Governance / voting rewards:** holders stake and vote for guilds and proposals, earning voting/staking rewards funded by protocol inflation. This is the primary native demand sink for the token.
- **Inflation:** WAXP has an **unlimited max supply** with ongoing inflation funding guild pay and staking rewards — a structural headwind for price unless offset by burns or demand growth.
- **Settlement & fees:** WAXP underpins on-chain settlement and marketplace activity (NFT mints, trades, swaps).
- **WAXE bridge token:** a separate Ethereum-bridged variant (**WAXE**) has historically let stakers capture a share of network economics and access [[ethereum|Ethereum]] [[defi]]. Verify current status of the WAXE program against project sources.

**Value-accrual summary:** WAXP is a gas/staking/governance token whose demand is tied to NFT/gaming throughput on the chain. Because it is feeless at the user level and inflationary, value accrual leans on (a) staking lock-up reducing float and (b) NFT/marketplace activity requiring WAXP — both cyclical with the GameFi sector.

---

## Comparison vs Competing NFT/Gaming Chains

| Dimension | **WAX (WAXP)** | [[immutable-x\|Immutable (IMX)]] | [[flow\|Flow (FLOW)]] | [[ronin\|Ronin (RON)]] |
|---|---|---|---|---|
| **Architecture** | DPoS L1 (EOSIO/Antelope fork) | Ethereum L2 (zk-rollup / StarkEx + zkEVM) | Purpose-built L1 (multi-role nodes) | Ethereum sidechain (DPoS) |
| **Core focus** | NFTs, collectibles, casual games | NFT/gaming via Ethereum security | Consumer NFTs (NBA Top Shot, Dapper) | Game-specific (Axie Infinity ecosystem) |
| **Fees to user** | Fee-less (resource staking) | Gas-free minting/trading (protocol-paid) | Low, FLOW-denominated | Low, RON gas |
| **Flagship apps** | Alien Worlds, Splinterlands-era assets, Farmers World | Gods Unchained, Guild of Guardians, Immutable Play | NBA Top Shot, NFL All Day | Axie Infinity, Pixels |
| **Security model** | ~21 elected guilds | Inherits [[ethereum\|Ethereum]] L1 | Own validator set | Bridge-dependent (suffered 2022 $625M Ronin Bridge hack) |
| **Token role** | Gas/staking/governance, inflationary | Gas, staking, ecosystem fees | Gas, staking, secured-by-FLOW | Gas, staking, governance |

WAX's relative strengths are a mature low-cost NFT stack and seamless onboarding; its relative weaknesses are EOSIO-ecosystem decline and an inflationary, unlimited-supply token versus more security-anchored rivals like Immutable (Ethereum) or Flow.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 4.58B WAXP |
| **Total Supply** | 4.58B WAXP |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $29.77M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.77 (2018-01-09) |
| **Current vs ATH** | -99.77% |
| **All-Time Low** | $0.00588044 (2026-02-06) |
| **Current vs ATL** | +10.49% |
| **24h Change** | -1.95% |
| **7d Change** | +0.42% |
| **30d Change** | +5.23% |
| **1y Change** | -64.40% |

---

## Platform & Chain Information

**Native Chain:** Wax

### Contract Addresses

| Chain | Address |
|---|---|
| Wax | `WAX-wax-eosio.token` |
| Ethereum | `0x2a79324c19ef2b89ea98b23bc669b7e7c9f8a517` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | WAXP/USDT | N/A |
| Upbit | WAXP/KRW | N/A |
| Bitget | WAXP/USDT | N/A |
| KuCoin | WAX/USDT | N/A |
| Crypto.com Exchange | WAXP/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X2A79324C19EF2B89EA98B23BC669B7E7C9F8A517/0XDAC17F958D2EE523A2206206994597C13D831EC7 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://wax.io/](https://wax.io/) |
| **Twitter** | [@WAX_io](https://twitter.com/WAX_io) |
| **Reddit** | [https://www.reddit.com/r/WAX_io](https://www.reddit.com/r/WAX_io) |
| **Telegram** | [wax_io](https://t.me/wax_io) (6,777 members) |
| **GitHub** | [https://github.com/worldwide-asset-exchange/wax-blockchain-legacy](https://github.com/worldwide-asset-exchange/wax-blockchain-legacy) |
| **Whitepaper** | [https://github.com/worldwide-asset-exchange/whitepaper](https://github.com/worldwide-asset-exchange/whitepaper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $1.76M |
| **Market Cap Rank** | #794 |
| **24h Range** | $0.00648067 — $0.00668026 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## How & Where WAXP Trades

- **Spot venues:** WAXP lists on multiple Tier-1/Tier-2 centralized exchanges — **Binance** (WAXP/USDT), **Upbit** (WAXP/KRW, a historically important Korean-retail venue for WAXP), **Bitget**, **KuCoin**, and **Crypto.com**. Korean Won pairs have at times driven outsized volume and volatility.
- **On-chain / DEX:** the Ethereum-bridged contract trades on **Uniswap V3**; native WAXP liquidity also exists in the WAX/Antelope DEX ecosystem (e.g., Alcor).
- **Liquidity profile:** with ~$1–2M reported 24h volume against a ~$20M cap (rank ~#823), WAXP is **thin**. Order books are shallow, slippage on size is meaningful, and CEX-driven moves (especially Korean pairs) dominate price discovery.
- **Derivatives:** perpetual/futures coverage is limited relative to large caps; any leverage carries elevated liquidation risk given thin spot depth. Do not assume deep, continuous perp liquidity.

---

## Narrative, Category & Catalysts

- **Category:** GameFi / NFT / play-to-earn infrastructure L1 — a sector that led the 2021 bull and has been deeply out of favor since. WAX is one of the longest-running pure-play NFT/gaming chains.
- **Bull catalysts:** a renewed NFT/gaming cycle; breakout traction for a flagship on-chain game; expansion of the AtomicHub/vIRL physical-redemption use case; partnerships bringing branded IP collectibles on-chain.
- **Bear/structural headwinds:** EOSIO/Antelope ecosystem decline (developer mindshare migrating to EVM, Solana, and modular L2s); inflationary unlimited supply; GameFi sector still in a multi-year drawdown; competition from Ethereum-secured NFT venues (Immutable, Base, Blast) and Solana NFTs.

---

## History / Timeline

- **2017:** WAX founded by the team behind OPSkins (a large CS:GO/Steam skin marketplace), pitching a decentralized marketplace for virtual items.
- **2017-12-19:** WAXP genesis / token launch.
- **2018-01-09:** all-time high of **$2.77** during the prior cycle peak.
- **2019–2020:** WAX migrated to its own DPoS chain (EOSIO-based) and rolled out the WAX Cloud Wallet and NFT tooling.
- **2021:** NFT/play-to-earn boom — WAX became one of the highest transaction-count chains, driven by **Alien Worlds**, **Farmers World**, and a large collectibles marketplace via AtomicHub.
- **2022–2025:** GameFi downturn; on-chain activity and price cooled sharply alongside the broader sector.
- **2026-02-06:** all-time low around **$0.00588** recorded amid the 2026 bear market.
- **2026-06-21/22:** trades ~$0.0044, ~99.8% below ATH, in an Extreme-Fear regime.

> Dates above reflect the page's recorded market data and widely documented project history; verify specific partnership claims against primary sources before relying on them.

---

## Trading Playbook (bear / Extreme-Fear regime)

> Context: F&G = 21 (Extreme Fear), established bear market, [[btc-bitcoin|BTC]] ~$64k (~16% below 200-day MA). Small-cap GameFi tokens are the highest-beta, lowest-liquidity corner of the market right now.

- **Bias:** capital-preservation. WAXP is a high-beta, sector-dependent micro-cap deep in a structural drawdown; it has no near-term fundamental catalyst priced in.
- **Longs:** only as small, asymmetric "sector-recovery option" positions sized for total loss. The thesis requires a broad NFT/gaming narrative revival *and* WAX-specific traction — both speculative. Prefer accumulation near prior ATL zones rather than chasing CEX-driven spikes.
- **Avoid:** leverage. Thin spot depth + Korean-pair volatility = violent liquidation risk.
- **Risk controls:** position-size as a lottery ticket; predefine invalidation (e.g., a new ATL on rising sell volume); treat Upbit/KRW-driven pumps as exit liquidity, not trend confirmation.
- **Watch:** AtomicHub/on-chain NFT volume, active-game user counts, and broad GameFi index strength as leading tells before price.

---

## Risks

- **DPoS centralization:** a small elected guild set can concentrate influence and raises governance-capture and censorship concerns relative to larger validator sets.
- **Sector dependence:** WAX's fortunes are tied to NFT/GameFi cycles, which are highly cyclical; the prolonged downturn has pressured on-chain activity and price.
- **EOSIO-family ecosystem risk:** the broader EOS/Antelope ecosystem has seen declining mindshare, which can affect tooling, developer interest, and liquidity.
- **Small-cap volatility & drawdown:** at ~$20M market cap (rank #823) and down >99% from ATH, WAXP is volatile and thinly traded.

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[proof-of-stake]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.
