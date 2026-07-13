---
title: "TRON"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, altcoins]
aliases: ["TRX", "Tron Network"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://tron.network"
related: ["[[crypto-markets]]", "[[tether]]", "[[ethereum]]", "[[hyperliquid]]", "[[stablecoins]]", "[[proof-of-stake]]"]
---

# TRON

**TRON** (TRX) is a high-throughput Layer 1 blockchain that has become the dominant settlement rail for [[tether|Tether (USDT)]], hosting roughly $86B of USDT — about half of all USDT in circulation — as of spring 2026. For traders, TRX is less a smart-contract-platform bet and more a levered proxy on global stablecoin payment flows, consistently ranking in the top 10 by market capitalization.

---

## Market Data

| Metric | Value |
|---|---|
| **Rank** | #8 |
| **Price** | $0.322326 |
| **Market Cap** | $30.57 billion |
| **24h Volume** | $584.03 million |
| **24h Change** | +0.59% |
| **7d Change** | +2.25% |
| **Circulating Supply** | 94,834,433,714 TRX |
| **Total Supply** | 94,835,804,498 TRX |
| **Max Supply** | None (no hard cap; fee burn keeps net issuance ~flat) |
| **All-Time High** | $0.4313 (2024-12-04) — currently -25.3% |
| **All-Time Low** | $0.00180434 (2017-11-12) — currently +17,764% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** [[crypto-market-sentiment|Fear & Greed]] = **22 (Extreme Fear)**; **Established Bear Market**. TRX is the clear **outperformer** of the six flagships in this drawdown — only ~25% below its Dec 2024 ATH while BTC/ETH/SOL are 50-76% off their highs. This low-beta resilience reflects TRX's fundamental tie to (relatively sticky) stablecoin transaction demand rather than speculative risk appetite.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | TRX |
| **Market Cap Rank** | #8 |
| **Market Cap** | $30.57B (2026-06-20) |
| **Consensus** | Delegated [[proof-of-stake|Proof-of-Stake]] (27 Super Representatives) |
| **Sector** | Layer 1, stablecoin settlement rail |
| **Supply** | ~94.8B TRX, no hard cap (fee burn makes net issuance roughly flat-to-deflationary) |
| **Genesis Date** | 2017-08-28 |
| **Founder** | Justin Sun (now a community-led DAO) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Alleged SEC Securities, FTX Holdings, DWF Labs Portfolio, Tron Ecosystem, Proof of Stake (PoS), GMCI Layer 1 Index, GMCI 30 Index, GMCI Index, World Liberty Financial Portfolio, Made in China |
| **Website** | [https://tron.network](https://tron.network) |

---

## Overview

TRON is a decentralized blockchain-based operating system designed to accelerate the decentralization of the internet and its underlying infrastructure. It serves as a global settlement layer for stablecoins and everyday digital purchases, providing a high-throughput environment to support large-scale decentralized applications. The network is governed by a decentralized autonomous organization (DAO), which allows the community to manage the protocol without a central authority. Its primary value proposition includes a unique resource model that utilizes bandwidth and energy to allow for high transaction volumes without traditional fee spikes.

The platform functions as a smart contract platform that enables the creation of decentralized applications and is compatible with the Ethereum Virtual Machine, allowing developers to easily migrate applications. TRON operates using a Delegated Proof of Stake consensus mechanism where token holders vote for 27 Super Representatives to verify transactions and maintain the ledger. This structure is built for scalability and fast finality, aiming to handle more transactions per second than many established legacy blockchains. Users can interact with the ecosystem for various purposes, including decentralized finance (DeFi) through platforms like JustLend DAO and decentralized storage via the BitTorrent File System.

Value moves through the system via its native utility token, TRX, which facilitates transactions and grants users access to network resources. Holders can lock their TRX in a staking mechanism to gain TRON Power, which is used to vote on network rules and elect Super Representatives, earning rewards for securing the network. Established by the TRON Foundation and led by founder Justin Sun, the project has transitioned into a community-led DAO. The ecosystem is supported by strategic partnerships with major global entities, including Samsung, which integrated TRON into its blockchain keystore, as well as BitTorrent, O...

---

## Technology & Consensus

TRON runs a **Delegated Proof-of-Stake (DPoS)** consensus: TRX holders stake to obtain **TRON Power** and vote for **27 Super Representatives (SRs)** who produce blocks (~3-second block time, high TPS, fast finality). This is a deliberately validator-light, throughput-first design — fewer block producers than [[ethereum|Ethereum's]] or [[solana|Solana's]] validator sets, trading decentralization for performance and cost.

A defining feature is TRON's **resource model**: instead of paying gas in TRX for every action, users consume **Bandwidth** (for transaction byte-size) and **Energy** (for smart-contract execution), both of which can be obtained by **freezing/staking TRX** rather than spending it. The result is that high-frequency, fee-sensitive flows — above all USDT transfers — can be effectively very cheap or free, which is precisely why USDT migrated en masse to TRON. The network is **EVM-compatible** (TVM, the TRON Virtual Machine), letting Solidity contracts port over easily.

---

## Tokenomics & Supply Schedule

| Metric | Value |
|---|---|
| **Circulating Supply** | 94.83B TRX |
| **Total Supply** | 94.84B TRX |
| **Max Supply** | None (no hard cap) |
| **MC / FDV** | ~1.00 (effectively fully circulating; no unlock overhang) |

- **Issuance & burn:** TRX is emitted to SRs/voters as block rewards, while transaction and resource fees are **burned**. With heavy USDT throughput, burn has at times offset or exceeded issuance, keeping net supply roughly **flat-to-slightly-deflationary** — a structurally different profile from inflationary L1s.
- **Staking:** freezing TRX yields TRON Power + voting rewards (~staking yield) *and* Bandwidth/Energy. Because staking serves a dual purpose (governance + free resources), a large share of supply is frozen, reducing liquid float.
- **No unlock cliffs:** MC/FDV ≈ 1.0 means there is no large locked allocation overhanging the market — a notable contrast to lower-float alts like [[solana|SOL]] or [[cardano|ADA]].

---

## Ecosystem & Use Cases

- **Stablecoin settlement (the core use case):** TRC-20 USDT is the dominant product; TRON is the primary low-cost rail for USDT in emerging markets, remittances, and OTC/CEX flows.
- **DeFi:** **JustLend DAO** (lending), **SunSwap** (AMM DEX), and **JUST** ecosystem assets; TVL is modest relative to ETH/SOL but stable.
- **Storage/media:** **BitTorrent (BTT)** and the BitTorrent File System (BTFS) — legacy acquisitions integrated into the ecosystem.
- **Stablecoin issuance:** USDD (TRON-native stablecoin) and TRC-20 USDT/USDC.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.4313 (2024-12-04) — currently -25.3% |
| **All-Time Low** | $0.00180434 (2017-11-12) — currently +17,764% |
| **24h Change** | +0.59% |
| **7d Change** | +2.25% |

> *Price figures as of 2026-06-20 (CoinGecko).*

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | TRX/USDT | N/A |
| Kraken | TRX/EUR | N/A |
| Bitget | TRX/USDT | N/A |
| KuCoin | TRX/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | TRX-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://tron.network](https://tron.network) |
| **Twitter** | [@trondao](https://twitter.com/trondao) |
| **Reddit** | [https://www.reddit.com/r/Tronix](https://www.reddit.com/r/Tronix) |
| **Telegram** | [tronnetworkEN](https://t.me/tronnetworkEN) (48,005 members) |
| **Discord** | [https://discord.com/invite/hqKvyAM](https://discord.com/invite/hqKvyAM) |
| **GitHub** | [https://github.com/tronprotocol/java-tron](https://github.com/tronprotocol/java-tron) |
| **Whitepaper** | [https://tron.network/static/doc/white_paper_v_2_0.pdf](https://tron.network/static/doc/white_paper_v_2_0.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 3,530 |
| **GitHub Forks** | 1,438 |
| **Commits (4 weeks)** | 19 |
| **Pull Requests Merged** | 3,262 |
| **Contributors** | 190 |

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **Rank** | #8 |
| **24h Volume** | $584.03M (2026-06-20) |
| **Liquidity** | Deep spot on [[binance]], Kraken, Bitget, KuCoin |
| **Volatility / beta** | **Low beta** vs other alt majors; trades on stablecoin demand, not risk sentiment |
| **Primary spot pairs** | TRX/USDT ([[binance]]), TRX/EUR (Kraken) |
| **Primary perp** | TRX-PERP ([[hyperliquid]]) + all major CEX perp venues |

TRX [[perpetual-futures|perps]] generally see **calmer [[funding-rate|funding]] and [[open-interest]]** dynamics than high-beta names like [[solana|SOL]] — consistent with its utility-driven, low-volatility profile. There is **no US spot TRX ETF**; the listed-equity proxy is **Tron Inc.** (Nasdaq), the largest public TRX holder.

---

## On-chain & Valuation Frameworks

The single most important fundamental signal for TRX is **on-chain USDT supply and flow** — TRX is essentially a levered claim on stablecoin payment volume.

| Metric | What it measures | Trading use |
|---|---|---|
| **TRC-20 USDT supply** | USDT minted/held on TRON (DefiLlama) | Core demand driver; mints = bullish, redemptions = bearish |
| **USDT chain share** | TRON's % of total USDT vs [[ethereum\|ETH]] | Rail-dominance trend |
| **Daily stablecoin transfer volume** | Settlement throughput | Real economic usage |
| **Net TRX burn** | Fees burned vs issuance | Supply-pressure input |
| **Staking/frozen ratio** | % of TRX frozen for resources | Liquid-float scarcity |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events (2025–2026)

- **June–July 2025 — Tron Inc. Nasdaq listing.** Nasdaq-listed SRM Entertainment executed a ~$100M reverse merger with TRON interests and renamed itself **Tron Inc.**; the ticker changed from SRM to **TRON** on 2025-07-17 and shares began trading under the new name on 2025-07-24, with founder Justin Sun ringing the opening bell. The deal placed more than 356M TRX into the company treasury, making Tron Inc. the largest publicly traded TRX holder — and giving equity traders a listed TRX proxy.
- **2025 — record stablecoin throughput.** The TRON network settled roughly **$7.9 trillion** in stablecoin transaction volume during 2025.
- **January 2026** — TRC-20 USDT reached ~**52%** of total USDT supply, overtaking [[ethereum]] as the largest single-chain USDT footprint.
- **March 2026** — Tether minted another $1B USDT on TRON, lifting on-TRON supply to ~**$85.3B** (~$86B by April 2026).
- **December 2024** — TRX all-time high of $0.4313 (still the reference high as of June 2026).

---

## Trading Relevance

- **What it proxies:** TRX is the market's cleanest listed bet on USDT payment-rail dominance. Watch USDT mints/redemptions on TRON (DefiLlama stablecoin dashboards) as the core fundamental signal.
- **Where it trades:** deep spot liquidity on Binance, Kraken, Bitget, KuCoin; perps as **TRX-PERP** on [[hyperliquid]] and all major CEX perp venues.
- **Narrative basket:** stablecoin-rails / payments basket (with [[tether]], [[bitcoin-cash]]-style payments names); also a "Justin Sun headline risk" name — SEC litigation history and Sun's ventures (World Liberty Financial ties, Tron Inc.) move the token.
- **Behavior:** historically low-beta vs other alt majors; supply is ~fully circulating (MC/FDV ≈ 1.0), so no unlock overhang.
- **Catalysts:** US stablecoin legislation flows, Tron Inc. treasury announcements, USDT supply migration between chains.

---

## Competitive Positioning

TRON competes primarily with [[ethereum|Ethereum]] (and, increasingly, [[solana|Solana]] and L2s) **for stablecoin settlement share**, not for general smart-contract dominance. Its moat is entrenched USDT distribution and ultra-low effective transfer cost.

| Asset | Rank | Mkt Cap | Consensus | Core thesis |
|---|---|---|---|---|
| **TRON (TRX)** | #8 | $30.6B | DPoS (27 SRs) | Stablecoin settlement rail |
| [[bitcoin\|Bitcoin (BTC)]] | #1 | $1.27T | [[proof-of-work]] | Digital gold |
| [[ethereum\|Ethereum (ETH)]] | #2 | $208B | [[proof-of-stake]] | Programmable settlement; rival USDT rail |
| [[solana\|Solana (SOL)]] | #7 | $41.5B | PoH + [[proof-of-stake\|PoS]] | High-throughput L1; emerging payments rail |
| [[cardano\|Cardano (ADA)]] | #18 | $6.1B | Ouroboros [[proof-of-stake\|PoS]] | Research-driven L1 |

> Peer market data as of 2026-06-20 (CoinGecko). TRX's low-beta, utility-driven profile makes it a relative-strength name in risk-off regimes like the current one.

---

## Regulatory

- **SEC litigation history:** TRON, Justin Sun, and affiliated entities were named in past SEC enforcement actions (alleged unregistered securities/market-manipulation claims) — an enduring "Justin Sun headline risk."
- **Stablecoin legislation:** US stablecoin frameworks directly affect USDT issuance and could shift settlement volume between chains — a double-edged catalyst for TRX.
- **Geopolitical:** heavy emerging-market USDT usage exposes TRON to sanctions/AML scrutiny around stablecoin rails.

---

## Risks

- **USDT concentration** — TRX's fortunes are tightly coupled to Tether; any USDT regulatory shock, depeg, or migration to [[ethereum|ETH]]/[[solana|SOL]] rails is a direct threat.
- **Founder/headline risk** — Justin Sun's ventures (World Liberty Financial ties, Tron Inc., past SEC actions) inject idiosyncratic volatility.
- **Centralization** — 27 SRs is a small validator set; governance and censorship-resistance concerns.
- **Competition** — Solana and L2 payments push, plus native stablecoin issuance elsewhere, could erode rail dominance.
- **Regulatory** — stablecoin and securities rulings.

> **Risk warning:** Crypto assets are highly volatile and speculative. Nothing here is investment advice. TRX's stability is contingent on continued Tether/USDT settlement demand.

---

## See Also

- [[crypto-markets]]
- [[tether]] / [[stablecoins]] — the core demand driver
- [[ethereum]] — rival USDT settlement rail
- [[solana]] — emerging payments competitor
- [[bitcoin]] — macro anchor
- [[proof-of-stake]] — consensus family
- [[hyperliquid]] / [[perpetual-futures]] / [[funding-rate]] / [[open-interest]] — derivatives venue & toolkit

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- CryptoRank / Stocktwits: Tron Inc. Nasdaq debut via SRM Entertainment reverse merger (July 2025) — https://cryptorank.io/news/feed/ee8fb-tron-inc-debuts-on-nasdaq-following-reverse-merger-with-srm-entertainment
- FXStreet: "TRON now holds more USDT than Ethereum: What $85.3 billion in stablecoins means for TRX" (2026-03-12) — https://www.fxstreet.com/cryptocurrencies/news/tron-now-holds-more-usdt-than-ethereum-what-853-billion-in-stablecoins-means-for-trx-202603121554
- The Coin Republic: "$1B USDT Minted on Tron as Stablecoin Supply Grows" (2026-03-13)
- DefiLlama TRON stablecoin dashboard — https://defillama.com/stablecoins/tron
- Verified via Perplexity (sonar) + web search, 2026-06-10
