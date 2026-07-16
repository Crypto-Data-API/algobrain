---
title: "Compound"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, lending]
aliases: ["COMP"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://compound.finance/"
related: ["[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[funding-rate]]", "[[hyperliquid]]", "[[lending]]"]
---

# Compound

**Compound** (ticker **COMP**) is the [[governance-token|governance token]] of **Compound Finance**, one of the original [[ethereum|Ethereum]]-based decentralized [[lending|lending/borrowing]] protocols where users supply assets to earn interest and borrow against collateral algorithmically. COMP lets holders delegate voting rights and propose or vote on protocol changes — collateral factors, interest-rate models, supported assets, and other parameters — through on-chain governance. Compound's June 2020 distribution of COMP to users is widely credited with kicking off the "DeFi Summer" [[yield-farming]] era.

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | COMP |
| **Native Chain** | [[ethereum|Ethereum]] (multi-chain: Base, Arbitrum, Polygon, Optimism, others) |
| **Market Cap Rank** | #190 |
| **Market Cap** | $172.79M |
| **Current Price** | $17.87 |
| **24h Change** | -1.43% |
| **7d Change** | +1.52% |
| **24h Volume** | $17.10M |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: amid **extreme fear** (Crypto [[fear-and-greed-index|Fear & Greed Index]] = 23) and an **Established Bear Market** regime as of 2026-06-21, COMP is down ~1.4% on the day but still modestly positive (+1.5%) on the week — relative resilience for an established blue-chip DeFi lending token with a tight, nearly fully-circulating hard cap. Trades roughly 9.9% of market cap daily.

---

## Technology & Protocol

Compound is an **algorithmic money market**, not a [[dex|DEX]]. Suppliers deposit assets into shared liquidity pools and receive interest; borrowers post collateral and draw against it. The defining mechanics:

- **Utilization-driven interest rates** — supply and borrow APYs are set by a deterministic curve based on each market's utilization (borrowed / supplied). High utilization pushes rates up to attract suppliers and ration borrowing; this is a *rate engine*, not an order book.
- **cTokens (Compound v2)** — depositing an asset mints an interest-bearing **cToken** (e.g., cUSDC) that continuously accrues value, a composable "money lego" reused across DeFi.
- **Collateral factors & liquidations** — each asset has a collateral factor; if a borrower's health falls below the threshold, third-party liquidators repay debt and seize collateral at a discount, keeping the protocol solvent. This depends on accurate **price oracles**.
- **Compound III ("Comet")** — the modern redesign uses **single-borrowable-asset markets** (e.g., a USDC market) with **isolated collateral** posted *but not lent*, improving capital efficiency and risk containment versus the v2 pooled-collateral model. Comet is deployed across Ethereum, Base, Arbitrum, Polygon, Optimism and more.
- **Governance** — COMP holders/delegates control collateral factors, interest-rate models, asset listings, and treasury via on-chain proposals executed by a Timelock.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~9.67M COMP |
| **Total Supply** | 10.00M COMP |
| **Max Supply** | 10.00M COMP |
| **Market Cap / FDV** | ~0.97 |
| **All-Time High** | $854.45 (2021) |
| **All-Time Low** | $15.21 |

COMP has a **hard cap of 10 million tokens**, and ~97% is already in circulation, meaning almost no dilution overhang remains (MC/FDV ~0.97). The original distribution allocated tokens to shareholders, the team, and — critically — to protocol users via **liquidity-mining emissions**, which seeded its governance distribution and triggered DeFi Summer. The low absolute supply and high per-token price are distinctive among DeFi tokens. A standing criticism: COMP is a **pure governance token** with no direct cash-flow claim on protocol interest revenue, so value capture rests on governance optionality (e.g., a future fee switch) rather than yield. With price near $18 versus an ATH of ~$854, the token has derated ~98% in line with the broader DeFi-governance complex.

---

## Market Structure & Derivatives

**Spot venues (CEX):** COMP trades on **Binance**, **Kraken**, **Upbit** (KRW), **Bitget**, **KuCoin**, and **Crypto.com** Exchange, with deep USD/USDT/KRW pairs.

**On-chain spot:** COMP is liquid across [[uniswap|Uniswap]] V2/V3 and SushiSwap on [[ethereum]] (paired with WETH), and is bridged to numerous chains (Base, Arbitrum, Polygon, BNB Chain, Avalanche, and others).

**Protocol context:** Compound is *not* a [[dex|DEX]] — it is a money market. COMP itself has no native trading venue beyond standard DEX/CEX listings; its on-chain "use" is governance and (historically) being supplied/borrowed within Compound itself. Borrowers and suppliers interact with algorithmic interest-rate curves rather than an order book, so the protocol's "trading mechanics" are really *rate mechanics* — utilization-driven supply/borrow APYs.

**Derivatives:** COMP is listed as a perpetual on [[hyperliquid|Hyperliquid]] (COMP-PERP). As an established DeFi token with reasonable liquidity, its perp [[funding-rate|funding rate]] is generally less erratic than micro-cap perps, but open interest still rises around governance events and DeFi-sector momentum (see [[perpetual-futures]]).

---

## Narrative & Category

Compound is a foundational **DeFi [[lending|lending/borrowing]]** primitive — alongside [[aave|Aave]], it defines the decentralized money-market category. The narrative is less about price speculation and more about durable protocol infrastructure: composable lending markets, an autonomous interest-rate engine, and a governance token that coordinates risk parameters. Compound III ("Comet") refined the design toward single-borrowable-asset markets with isolated collateral, focusing on capital efficiency and risk containment.

---

## Valuation Framing

Qualitatively, COMP screens as a **mature, low-dilution DeFi blue chip with a value-capture overhang**. The protocol holds meaningful TVL and is battle-tested, but the token does not directly receive interest revenue, so its ~$173M market cap embeds (a) governance optionality over a large money market and (b) a potential future fee switch, more than current cash flows. Relative to [[aave|Aave]] — which has grown larger and activated revenue-sharing mechanics — COMP trades at a discount that reflects both its smaller market share and the absence of holder cash flow. A re-rating catalyst would most plausibly be governance turning on protocol-fee distribution to COMP.

---

## Peer Comparison

| Protocol | Token | Category | MC Rank | Market Cap | Notes |
|---|---|---|---|---|---|
| **Compound** | COMP | Money market | #190 | ~$173M | Comet (isolated collateral); pure governance |
| [[aave\|Aave]] | AAVE | Money market | top-50 | multi-B | Larger TVL; safety module; fee mechanics |
| Morpho | MORPHO | Lending optimizer / markets | mid-cap | — | Peer-to-peer matching atop pools |
| MakerDAO / Sky | MKR / SKY | CDP / stablecoin | top-tier | multi-B | Mints DAI; different lending model |

*Figures for non-Compound peers are illustrative category placement, not snapshot data.*

---

## Notable History

- **2018:** Compound v1 launched as an early on-chain money market.
- **June 2020:** COMP token distribution began, igniting **DeFi Summer** and the yield-farming/liquidity-mining boom.
- **2021:** COMP reached an all-time high near $850 during the bull market.
- **Compound III (Comet):** Redesigned protocol with isolated collateral and a single base borrowable asset per market, deployed across multiple chains.
- COMP has since drawn down >95% from its ATH, in line with the broader DeFi-token derating.

---

## Risks

- **Smart-contract / liquidation risk:** As a lending protocol, Compound is exposed to oracle failures, bad-debt events, and cascading liquidations during sharp market moves.
- **Token value capture:** COMP is primarily a governance token; it does not entitle holders to direct protocol revenue, a perennial criticism of DeFi governance tokens.
- **Competitive pressure:** Aave and other money markets have grown larger; Compound's relative share has declined.
- **Bear-market / sector risk:** The current extreme-fear (F&G 23), Established Bear Market backdrop weighs on DeFi valuations broadly.
- **Regulatory risk:** On-chain lending faces ongoing regulatory scrutiny over securities and lending-product classification.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[lending]]
- [[defi]]
- [[aave]]
- [[hyperliquid]]
- [[funding-rate]]
- [[yield-farming]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-21 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | COMP |
| **Market Cap Rank** | #185 |
| **Market Cap** | $168.71M |
| **Current Price** | $17.44 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Lending/Borrowing Protocols, Made in USA, Governance, Base Native |
| **Website** | [https://www.compound.xyz](https://www.compound.xyz) |

---

## Overview

The Compound Governance Token is a governance token on the Compound Finance lending protocol, COMP allows the owner to delegate voting rights to the address of their choice; the owner’s wallet, another user, an application, or a DeFi expert. Anybody can participate in Compound governance by receiving delegation, without needing to own COMP.

Anybody with 1% of COMP delegated to their address can propose a governance action; these are simple or complex sets of actions, such as adding support for a new asset, changing an asset’s collateral factor, changing a market’s interest rate model, or changing any other parameter or variable of the protocol that the current administrator can modify.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 9.67M COMP |
| **Total Supply** | 10.00M COMP |
| **Max Supply** | 10.00M COMP |
| **Fully Diluted Valuation** | $174.50M |
| **Market Cap / FDV Ratio** | 0.97 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $854.45 (2021-05-12) |
| **Current vs ATH** | -97.96% |
| **All-Time Low** | $14.98 (2026-06-25) |
| **Current vs ATL** | +16.30% |
| **24h Change** | +3.14% |
| **7d Change** | +2.57% |
| **30d Change** | -3.11% |
| **1y Change** | -65.10% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc00e94cb662c3520282e6f5717214004a7f26888` |
| Near Protocol | `c00e94cb662c3520282e6f5717214004a7f26888.factory.bridge.near` |
| Base | `0x9e1028f5f1d5ede59748ffcee5532509976840e0` |
| Harmony Shard 0 | `0x32137b9275ea35162812883582623cd6f6950958` |
| Energi | `0x66bc411714e16b6f0c68be12bd9c666cc4576063` |
| Sora | `0x00dbd45af9f2ea406746f9025110297469e9d29efc60df8d88efb9b0179d6c2c` |
| Polygon Pos | `0x8505b9d2254a7ae468c0e9dd10ccea3a837aef5c` |
| Binance Smart Chain | `0x52ce071bd9b1c4b00a0b92d298c512478cad67e8` |
| Arbitrum One | `0x354a6da3fcde098f8389cad84b0182725c6c91de` |
| Avalanche | `0xc3048e19e76cb9a3aa9d77d8c03c29fc906e2437` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | COMP/USDT | N/A |
| Kraken | COMP/USD | N/A |
| Upbit | COMP/KRW | N/A |
| Bitget | COMP/USDT | N/A |
| KuCoin | COMP/USDT | N/A |
| Crypto.com Exchange | COMP/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XC00E94CB662C3520282E6F5717214004A7F26888/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0XC00E94CB662C3520282E6F5717214004A7F26888/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.compound.xyz](https://www.compound.xyz) |
| **Twitter** | [@Compound_xyz](https://twitter.com/Compound_xyz) |
| **Discord** | [https://compound.finance/discord](https://compound.finance/discord) |
| **GitHub** | [https://github.com/compound-finance/compound-protocol](https://github.com/compound-finance/compound-protocol) |
| **Whitepaper** | [https://compound.finance/documents/Compound.Whitepaper.pdf](https://compound.finance/documents/Compound.Whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 2,039 |
| **GitHub Forks** | 1,266 |
| **Pull Requests Merged** | 50 |
| **Contributors** | 20 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $11.57M |
| **Market Cap Rank** | #185 |
| **24h Range** | $16.81 — $17.57 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
