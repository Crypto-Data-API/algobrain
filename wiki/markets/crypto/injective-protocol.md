---
title: "Injective"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["INJ", "Injective Protocol"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized (Injective Labs: New York, USA)"
website: "https://injective.com"
related: ["[[cosmos]]", "[[crypto-markets]]", "[[ethereum]]", "[[solana]]"]
---

# Injective

**Injective** (INJ) is a finance-focused Layer 1 built on the [[cosmos|Cosmos]] SDK, providing on-chain orderbook, derivatives, and RWA modules for dApps such as the Helix DEX. Its November 2025 native EVM launch turned it into a MultiVM chain (EVM + WASM with shared state), and its deflationary burn/buyback mechanics make INJ one of the few L1 tokens with an explicit, recurring supply-reduction program — a structural fact traders price around monthly. With a fixed ~100M supply (effectively fully circulating), INJ is unusually clean of unlock overhang relative to peers, though it trades ~90% below its all-time high in the 2026 [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23).

---

## Market Data

| Metric | Value (2026-06-20) |
|---|---|
| **Price** | $5.08 |
| **Market Cap** | $508.5M |
| **Market Cap Rank** | #100 |
| **24h Volume** | $61.7M |
| **24h Change** | -0.17% |
| **7d Change** | -1.36% |
| **Circulating Supply** | 100.0M INJ |
| **Total Supply** | 100.0M INJ |
| **Max Supply** | None (uncapped nominal; net-deflationary via burns) |
| **All-Time High** | $52.62 (2024-03-14) — ≈ -90.3% |
| **All-Time Low** | $0.6574 (2020-11-03) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

> Earlier snapshots: April 2026 low-water ~$2.89 / $289M mcap; an interim June 2026 quote of ~$5.6–6.5 has been superseded by the 2026-06-20 figures above.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | INJ |
| **Asset class** | Layer 1 gas/staking/governance token (deflationary via burns) |
| **Native Chain** | Injective L1 ([[cosmos|Cosmos]] SDK, [[proof-of-stake|PoS]]); ERC-20 and IBC representations exist |
| **Market Cap** | $508.5M, rank #100 (2026-06-20; price $5.08) |
| **Categories** | Smart Contract Platform, DeFi, Cosmos Ecosystem, Layer 1, RWA, Binance Launchpad, PoS |
| **Backers** | Binance Labs (incubator), Pantera Capital, Jump, Mark Cuban |
| **Website** | [https://injective.com](https://injective.com) |

---

## Overview

Injective is an interoperable Layer 1 blockchain designed for DeFi applications. It provides developers with on-chain financial infrastructure modules to build dApps such as decentralized exchanges, prediction markets, and lending protocols. Its decentralized cross-chain bridging infrastructure offers compatibility with most blockchains, including EVM chains like [[ethereum|Ethereum]] and non-EVM chains like [[solana|Solana]].

(Note: earlier CoinGecko-derived data listed "Native Chain: Ethereum" — that refers to the ERC-20 representation of INJ; the protocol itself runs its own Cosmos-SDK chain.)

---

## Protocol & Technology

Injective is a **finance-specialized Layer 1** rather than a general-purpose smart-contract chain. Its architecture is purpose-built for on-chain markets:

- **[[cosmos|Cosmos SDK]] + Tendermint/CometBFT [[proof-of-stake]]** — Injective is an app-chain in the Cosmos ecosystem with instant finality (~0.64s block times post-EVM upgrade) and native [[cosmos|IBC]] interoperability with the wider Cosmos zone. This gives it sovereign control over its module set rather than competing for blockspace on a shared chain.
- **Native on-chain orderbook module** — unlike AMM-based DeFi, Injective bakes a fully on-chain central-limit orderbook (CLOB) into the protocol layer, with frequent-batch-auction matching to mitigate front-running/MEV. dApps like the **Helix** DEX plug into shared liquidity. This is the structural differentiator: spot, perps, and exchange-style markets are first-class primitives.
- **MultiVM (EVM + WASM)** — the **native EVM mainnet (11 Nov 2025)** added a native EVM execution layer alongside the existing CosmWasm (WASM) environment, with unified assets and liquidity via the **MultiVM Token Standard**. Solidity developers can deploy with standard Ethereum tooling while sharing state and liquidity with WASM contracts — broadening the developer funnel without fragmenting liquidity.
- **iAssets / RWA modules** — Injective provides modules for tokenized real-world assets and synthetic/"iAssets" exposure (equities, FX, commodities) as on-chain markets, anchoring its [[real-world-assets|RWA]] and on-chain-finance narrative.
- **Cross-chain bridging** — decentralized bridges connect INJ to [[ethereum|Ethereum]] (ERC-20), [[solana|Solana]], and IBC chains, so the same asset can move across ecosystems.

The combined thesis: Injective is "finance as infrastructure" — the orderbook, derivatives, and RWA logic live in the protocol, and the MultiVM upgrade lets the broadest possible developer base build on top.

---

## 2025–2026 Developments

- **Native EVM mainnet (11 Nov 2025)** — the largest upgrade in network history: a native EVM layer alongside WASM ("MultiVM"), with unified assets/liquidity via the MultiVM Token Standard, 0.64s block times, ~$0.00008 fees, and 30+ dApps/infra providers at launch (Injective blog, The Block).
- **Community BuyBack program (institutionalized monthly)** — a portion of protocol fees buys and burns INJ each month; participants committing INJ receive ~10% yield from ecosystem revenue. The **June 2026 buyback event was valued at over $315,000**. This extends Injective's long-running burn-auction design.
- **IIP-632 mainnet upgrade (28 Apr 2026)** — performance optimization and a strengthened buyback mechanism.
- **First regulated INJ fund in Asia (5 June 2026)** — Merkle Capital launched Thailand's first SEC-supervised investment vehicle dedicated to INJ.
- **Price**: $5.08 / $508.5M mcap, rank #100 as of 2026-06-20, up sharply from the ~$2.89 / $289M April 2026 low-water mark; still ~-90% from the $52.62 ATH (14 Mar 2024).

---

## Tokenomics & Supply

| Metric | Value (2026-06-20) |
|---|---|
| **Circulating Supply** | 100.0M INJ |
| **Total Supply** | 100.0M INJ |
| **Max Supply** | None (uncapped nominal) |
| **Market Cap** | $508.5M |
| **FDV** | ≈ $508.5M |
| **MC / FDV** | ≈ 1.00 |
| **ATH / ATL** | $52.62 (2024-03-14) / $0.6574 (2020-11-03) |

**Dilution flag — minimal.** INJ is effectively fully circulating: market cap equals FDV (MC/FDV ≈ 1.0), so there is *no unlock overhang* — a rare and bullish structural feature among L1s (contrast with [[aptos|Aptos]] at ~0.40 and [[sei-network|Sei]] at ~0.67 on max/total supply). Supply mechanics:

- **PoS inflation** — INJ has a target staking ratio with a dynamic inflation band (historically ~5–10% annualized, adjusting toward the target). New issuance rewards stakers/validators.
- **Weekly burn auctions** — a basket of protocol fees collected across dApps is auctioned for INJ each week; the winning INJ bid is **burned**. This has been the protocol's signature deflationary sink since launch.
- **Monthly Community BuyBack** — institutionalized program where a portion of ecosystem revenue buys and burns INJ monthly (the **June 2026 event was valued at over $315,000**); participants committing INJ earn ~10% yield from ecosystem revenue.

Net effect: when fee revenue is high enough, burns exceed inflation and INJ becomes **net-deflationary**. The key dependency is that on-chain activity must generate enough fees for burns to matter — in a bear market, fee revenue (and thus burn size) compresses.

---

## Valuation Framework

INJ is one of the few L1 tokens with a quasi-cash-flow valuation lens because of its explicit burn mechanics. Metrics to track (pull live; no invented values):

- **Weekly + monthly burn size (USD)** — the clearest "buyback yield" proxy. Annualize burns and compare to market cap for a crude shareholder-yield analogue.
- **Protocol/dApp fee revenue (REV)** — feeds the burn auction; the upstream driver of deflation.
- **Helix and ecosystem DEX volume** — trading volume on the native orderbook drives fees.
- **Net supply change** — burns minus inflation; if negative, supply is shrinking.
- **Staking ratio** — share of INJ staked; affects inflation and liquid float.
- **RWA / iAsset notional on-chain** — adoption proxy for the finance-infrastructure thesis.

The bull framing: a fixed supply with recurring burns means flow analysis (burn size vs CEX inflows) is more informative for INJ than for most L1s. The bear framing: in a low-activity regime, burns shrink and inflation dominates.

---

## Market Structure & Derivatives

- **Spot venues**: Binance, Kraken, Upbit (KRW), Bitget, KuCoin, Crypto.com, Uniswap (ERC-20). Deep, liquid, top-100 asset.
- **Derivatives**: **INJ-PERP on [[hyperliquid|Hyperliquid]]** and all major CEX futures (Binance, Bybit, OKX). 24h spot volume ~$61.7M (2026-06-20).
- **Perps / funding / OI**: liquid perp market; funding and OI are worth tracking around the monthly buyback and any regulated-product news. The fixed supply makes squeeze dynamics distinct from inflationary L1s.
- **Korean flow**: Upbit INJ/KRW is a meaningful share of spot turnover.

---

## Trading Playbook

- **Calendar trades**: monthly buyback/burn events and weekly burn auctions are scheduled, calendar-tradeable catalysts. Track burn size vs CEX inflows.
- **Narrative baskets**: DeFi L1s, [[cosmos|Cosmos]] ecosystem, [[real-world-assets|RWA]]/on-chain finance, deflationary-tokenomics plays. Post-EVM launch it also trades with the "MultiVM/EVM-compatibility" basket. See [[narrative-trading]].
- **Key catalysts**: EVM ecosystem dApp growth, regulated products (Thailand SEC-supervised fund 5 Jun 2026; US staked-INJ ETF filings in the 2025–26 institutional narrative), RWA/iAsset module adoption.
- **Structural edge**: no unlock overhang (MC/FDV ≈ 1.0) + recurring burns — rallies don't have to absorb mechanical new supply, unlike most L1 peers.
- **Volatility profile**: INJ has a history of violent narrative-driven swings (-58% in the year to April 2026 before the Q2 recovery); size accordingly in the [[crypto-market-regimes|Established Bear Market]].

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum (ERC-20) | `0xe28b3b32b6c345a34ff64674606124dd5aceca30` |
| BNB Chain | `0xa2b726b1145a4773f68593cf171187d8ebe4d495` |
| Cosmos/Osmosis (IBC) | `ibc/64BA6E31FE887D66C6F8F31C7B1A80C7CA179239677B4088BB55F5EA07DBE273` |
| Terra 2 (IBC) | `ibc/25BC59386BB65725F735EFC0C369BB717AA8B5DAD846EAF9CBF5D0F18F207211` |
| Secret | `secret14706vxakdzkz9a36872cs62vpl5qd84kpwvpew` |

### Developer Activity (April 2026 snapshot)

| Metric | Value |
|---|---|
| **GitHub Stars** | 117 |
| **GitHub Forks** | 79 |
| **Pull Requests Merged** | 517 |
| **Contributors** | 14 |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://injective.com](https://injective.com) |
| **Twitter** | [@injective](https://twitter.com/injective) |
| **Telegram** | [joininjective](https://t.me/joininjective) |
| **Discord** | [https://discord.com/invite/NK4qdbv](https://discord.com/invite/NK4qdbv) |
| **Docs** | [https://docs.injective.network](https://docs.injective.network) |

---

## Ecosystem & Use Cases

- **Helix** — flagship native-orderbook DEX (spot + perps) built directly on Injective's CLOB module.
- **Derivatives & prediction markets** — perps, futures, and event/prediction markets are protocol-level primitives.
- **iAssets / RWA** — tokenized equities, FX, and commodities as on-chain markets; the [[real-world-assets|RWA]] thesis.
- **Lending & structured products** — money markets and yield products built on shared liquidity.
- **MultiVM dApps** — post-Nov-2025 EVM launch, Solidity teams deploy alongside WASM apps with shared state/liquidity (30+ dApps/infra at launch).
- **Cross-chain finance** — IBC + bridges to [[ethereum|Ethereum]]/[[solana|Solana]] let assets flow in from other ecosystems.

---

## Competitive Positioning

| Chain | Niche | Token vs INJ (2026-06-20) | Notes |
|---|---|---|---|
| **Injective** | Finance-specialized Cosmos L1 + native CLOB + MultiVM | rank #100, ~$508M cap, MC/FDV ≈ 1.0 | Burn/buyback deflation; no unlock overhang |
| [[hyperliquid]] | Vertically-integrated perp DEX / L1 | far larger | The dominant on-chain perps venue; direct mindshare rival |
| [[cosmos]] (ATOM) | App-chain hub / IBC | larger | Injective is a Cosmos app-chain; shares IBC interop |
| [[sei-network|Sei]] | Parallelized-EVM "trading chain" | smaller | Competes for exchange-style workloads |
| dYdX | Orderbook perp app-chain (Cosmos) | — | Closest pure-play orderbook-DEX competitor |

Injective's edge is being a *finance-native* L1 with deflationary tokenomics; its biggest threat is [[hyperliquid|Hyperliquid]], which has absorbed enormous on-chain-derivatives mindshare with a tightly integrated exchange model.

---

## Risks

- **Fee-revenue dependency** — burns only matter if on-chain activity generates enough fees; bear-market activity compresses burns and lets inflation dominate.
- **Intense competition** — [[hyperliquid|Hyperliquid]] and other finance chains contest the same trader mindshare.
- **Volatility** — INJ has a history of violent narrative swings; high beta to alt sentiment.
- **Bear-market regime** — trades ~90% below ATH in an [[crypto-market-regimes|Established Bear Market]] (Fear & Greed 23).
- **Smart-contract / bridge risk** — cross-chain bridges and DeFi modules carry exploit risk.
- **Regulatory** — on-chain derivatives and RWAs/iAssets (synthetic equities/FX) sit in contested regulatory territory across jurisdictions.

> Data disclaimer: market figures are point-in-time (2026-06-20). Crypto is volatile and high-risk; nothing here is investment advice. Verify against live data before trading.

---

## Related

- [[cosmos]]
- [[ethereum]]
- [[solana]]
- [[proof-of-stake]]
- [[real-world-assets]]
- [[crypto-markets]]
- [[hyperliquid]]
- [[sei-network]]
- [[narrative-trading]]
- [[crypto-market-regimes]]
- [[bitcoin-etfs]]

---

## Sources

- CoinGecko / cryptodataapi.com market snapshot, 2026-06-20 (current price, market cap, supply, ATH/ATL)
- CoinGecko April 2026 snapshot (Source: [[coingecko-top-1000-2026-04-09]])
- Injective blog — "Welcome to the Injective Era: Native EVM Mainnet Launch": https://injective.com/blog/welcome-to-the-injective-era-native-evm-mainnet-launch-opens-new-frontiers-for-finance
- The Block — "Injective rolls out native EVM support": https://www.theblock.co/post/378418/injective-rolls-out-native-evm-support-on-its-high-performance-cosmos-based-chain
- CoinMarketCap AI updates (June 2026 buyback ~$315k; IIP-632 28 Apr 2026; Merkle Capital Thailand fund 5 June 2026): https://coinmarketcap.com/cmc-ai/injective/latest-updates/
- CoinGecko / CoinMarketCap live pages, June 2026 (mcap ~$547–562M, rank #74–95): https://www.coingecko.com/en/coins/injective
- Verified via web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 100.00M INJ |
| **Total Supply** | 100.00M INJ |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $505.34M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $52.62 (2024-03-14) |
| **Current vs ATH** | -90.39% |
| **All-Time Low** | $0.6574 (2020-11-03) |
| **Current vs ATL** | +669.26% |
| **24h Change** | +1.17% |
| **7d Change** | +4.99% |
| **30d Change** | -14.95% |
| **1y Change** | -61.56% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xe28b3b32b6c345a34ff64674606124dd5aceca30` |
| Cosmos | `ibc/64BA6E31FE887D66C6F8F31C7B1A80C7CA179239677B4088BB55F5EA07DBE273` |
| Terra 2 | `ibc/25BC59386BB65725F735EFC0C369BB717AA8B5DAD846EAF9CBF5D0F18F207211` |
| Osmosis | `ibc/64BA6E31FE887D66C6F8F31C7B1A80C7CA179239677B4088BB55F5EA07DBE273` |
| Secret | `secret14706vxakdzkz9a36872cs62vpl5qd84kpwvpew` |
| Binance Smart Chain | `0xa2b726b1145a4773f68593cf171187d8ebe4d495` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | INJ/USDT | N/A |
| Kraken | INJ/USD | N/A |
| Upbit | INJ/KRW | N/A |
| Bitget | INJ/USDT | N/A |
| KuCoin | INJ/USDT | N/A |
| Crypto.com Exchange | INJ/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0XE28B3B32B6C345A34FF64674606124DD5ACECA30/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 118 |
| **GitHub Forks** | 80 |
| **Pull Requests Merged** | 519 |
| **Contributors** | 16 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $101.63M |
| **Market Cap Rank** | #101 |
| **24h Range** | $5.00 — $5.20 |
| **CoinGecko Sentiment** | 70% positive |
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
