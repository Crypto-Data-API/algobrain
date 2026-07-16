---
title: "eCash"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["BCHA", "XEC"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://e.cash/"
related: ["[[bitcoin-cash]]", "[[bitcoin]]", "[[crypto-markets]]"]
---

# eCash

**eCash** (ticker **XEC**) is a **Layer-1 "digital cash" network developed by Bitcoin ABC**, descended from the [[bitcoin-cash|Bitcoin Cash]] lineage (itself a [[bitcoin|Bitcoin]] fork). Launched 15 November 2020 (originally as BCHA, the result of the Bitcoin Cash ABC split), eCash distinguishes itself by layering **Avalanche consensus on top of the core Proof-of-Work layer** — a Nakamoto/Avalanche hybrid that aims to deliver instant transaction finality, staking rewards, subnet extensibility, and fork-free protocol upgrades. XEC is a very-high-supply, micro-priced token positioned as scalable peer-to-peer electronic cash.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | XEC |
| **Current Price** | $0.00000547 |
| **Market Cap** | $109.71M |
| **Market Cap Rank** | #254 |
| **24h Volume** | $3.52M |
| **24h Change** | +2.08% |
| **7d Change** | -0.38% |
| **Fully Diluted Valuation** | $109.71M |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: the backdrop is risk-off — the [[fear-and-greed-index|Crypto Fear & Greed Index]] reads **23 (extreme fear)** in an **"Established Bear Market."** XEC ticked up ~+2% on the day but is roughly flat on the week, tracking the weak tape. It sits ~6.6% above its fresh all-time low (set 2026-06-06).

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~20.04T XEC |
| **Total Supply** | ~20.04T XEC |
| **Max Supply** | 21.00T XEC |
| **Market Cap / FDV** | 1.00 |

eCash inherits Bitcoin's **21-million-coin schedule scaled up by 1,000,000** to **21 trillion XEC** (each old BCH unit became 1,000,000 XEC in the redenomination). With ~20.04T already circulating, the **MC/FDV is ~1.00 and the residual PoW issuance overhang is small** — most supply is mined out. The micro unit price is purely a function of the enormous token count. New issuance comes from PoW mining plus the Avalanche staking-reward mechanism.

### All-Time Range

| Metric | Value |
|---|---|
| **All-Time High** | $0.00038001 (2021-09-04) — −98.6% |
| **All-Time Low** | $0.00000513 (2026-06-06) |

XEC trades **~98.6% below** its 2021 ATH and made a **fresh all-time low on 2026-06-06** — a vivid marker of the current established bear market. At ~$0.00000547 it is only ~6.6% off that low.

---

## Technology / Protocol

eCash's defining architectural choice is a **two-layer consensus stack**:

| Layer | Mechanism | Role |
|---|---|---|
| **Base** | Nakamoto [[proof-of-work\|Proof-of-Work]] (SHA-256, ASIC-mined, Bitcoin-derived) | Block production, issuance, censorship resistance |
| **Overlay** | **Avalanche** consensus (BFT-style sampling) | Pre-consensus / fast finality, anti-reorg protection, staking |

This **PoW + Avalanche hybrid** is the headline differentiator versus its [[bitcoin-cash|Bitcoin Cash]] / [[bitcoin|Bitcoin]] roots:

- **Fast finality** — Avalanche pre-consensus aims to make confirmations effectively final in seconds rather than waiting for multiple PoW blocks, addressing the slow-finality complaint against pure Nakamoto chains.
- **Staking rewards** — node operators stake XEC to participate in Avalanche, an unusual feature for a Bitcoin-derived chain and the basis for the staking-yield layer.
- **Fork-free upgrades & subnets** — the roadmap targets EtherDB/subnet extensibility and protocol upgrades without contentious hard forks (a direct reaction to the BCH/BTC fork history).
- **Throughput roadmap** — scaling targets move from ~100 tps toward a long-term 5,000,000 tps via larger blocks plus the Avalanche layer.

XEC also inherited the **CashTokens / eToken** capability from the Bitcoin Cash lineage, enabling simple token issuance on the UTXO base layer.

## How & Where It Trades

XEC is a **spot** asset with Tier-1 CEX coverage. On-file CoinGecko venues:

### Centralized Exchanges
| Exchange | Pair |
|---|---|
| Binance | XEC/USDT |
| Upbit | XEC/KRW |
| KuCoin | XEC/USDT |

Notably, eCash has a strong presence on **Korean exchanges (Upbit, XEC/KRW)**, where retail flow can drive outsized volume and volatility. No perpetual-futures / [[hyperliquid|Hyperliquid]] listing is recorded on file, so funding/open-interest metrics are not applicable — exposure is spot. Daily volume (~$3.1M) is moderate for the cap.

---

## Use Case / Narrative / Category

CoinGecko categorises XEC under **Smart Contract Platform, Layer 1, Bitcoin Fork, and Proof of Work (PoW).** The core narrative is **scalable electronic cash**: the published roadmap targets scaling throughput from ~100 tps toward 5,000,000 tps, sub-3-second finality, and fork-free upgradeability — all enabled by the PoW + Avalanche hybrid. The staking-reward layer is unusual for a Bitcoin-derived chain and is meant to fund Avalanche node operation. eCash therefore sits in the "fast, cheap Bitcoin-style payments" camp, competing with [[bitcoin-cash|Bitcoin Cash]], [[litecoin|Litecoin]] and [[stablecoin|stablecoin]] payment rails.

---

## Peer Comparison

| Asset | Lineage | Consensus | Approx. cap | Differentiator |
|---|---|---|---|---|
| **eCash** | XEC | BCH/ABC fork | PoW + Avalanche | ~$110M | Avalanche fast finality + staking; trillion-unit supply |
| [[bitcoin-cash\|Bitcoin Cash]] | BCH | BTC fork | PoW | Multi-$B | Larger blocks, broadest "cash" brand recognition |
| [[litecoin\|Litecoin]] | LTC | BTC-era | Scrypt PoW | Multi-$B | Established payments, deep liquidity, MWEB privacy |
| [[bitcoin\|Bitcoin]] | BTC | — | PoW | Multi-$T | Settlement base layer; "cash" only via L2s |

eCash is the **smallest, most experimental** of the Bitcoin-derived payment chains, betting on Avalanche-driven finality and staking to stand out — but it remains far behind BCH and LTC in liquidity and mindshare.

---

## Valuation Framing (qualitative)

- **Supply-unit illusion** — XEC's micro price ($0.00000547) is purely a function of its ~20T-unit count, not a sign of being "cheap." Compare on market cap (~$110M), not unit price.
- **Network value vs usage** — as a payments chain, the fair lens is transaction throughput, active addresses, and merchant/exchange adoption versus network value. XEC's payment usage is modest relative to BCH/LTC, so the cap is largely **narrative/option value** on the Avalanche-scaling roadmap delivering.
- **MC/FDV ~1.00** — almost all supply is mined; there is no major emission overhang, so dilution is not the bear case (unlike many DeFi tokens). The bear case is **adoption stagnation** in a crowded "fast Bitcoin cash" niche.
- **Regime** — with [[fear-and-greed-index|Fear & Greed]] at 23 and a fresh ATL printed two weeks ago, momentum is firmly negative; XEC trades as a low-beta-of-a-low-beta payments small-cap.

---

## Notable History

- Born **15 November 2020** as **BCHA**, from the Bitcoin Cash / Bitcoin ABC split.
- Rebranded to **eCash (XEC)** in 2021 with a 1:1,000,000 redenomination and the Avalanche-consensus roadmap.
- ATH of **$0.00038** on 2021-09-04 during the prior cycle.
- **Fresh ATL of $0.00000513 on 2026-06-06**, set during the current bear market.

> *Additional dated events will be added through the wiki's source-ingestion workflow as relevant articles are processed.*

---

## Risks

- **Bear-market beta / fresh lows** — XEC printed a new ATL on 2026-06-06 amid extreme fear ([[fear-and-greed-index|Fear & Greed]] = 23); downtrend remains intact.
- **Narrative crowding** — "scalable Bitcoin cash" is a contested niche; XEC competes with BCH, LTC and stablecoins, none of which it has decisively beaten.
- **Roadmap-execution risk** — the multi-million-tps targets are aspirational; delivery and real-world adoption are unproven at that scale.
- **Concentration of development** — heavily reliant on the Bitcoin ABC team for protocol direction.
- **Exchange/regional flow risk** — meaningful Korean (Upbit) exposure can amplify volatility on regional sentiment shifts.

---

## See Also

- [[crypto-markets]]
- [[bitcoin]]
- [[bitcoin-cash]]
- [[litecoin]]
- [[proof-of-work]]
- [[fear-and-greed-index]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko snapshot.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | XEC |
| **Market Cap Rank** | #221 |
| **Market Cap** | $128.17M |
| **Current Price** | $0.00000639 |
| **Categories** | Smart Contract Platform, Layer 1 (L1), Bitcoin Fork, Proof of Work (PoW) |
| **Website** | [https://e.cash/](https://e.cash/) |

---

## Overview

eCash (XEC) is a Layer-1 digital cash network, developed by Bitcoin ABC. It was created on Nov 15th, 2020, and has since distinguished itself from its predecessors and other Bitcoin clients by integrating the breakthrough Avalanche consensus with its core proof-of-work (PoW) layer, extending its security and fundamental capabilities.

This Nakamoto/Avalanche hybrid consensus integration gives it unique properties for a Bitcoin-like chain, such as instant transaction finality, staking rewards, extensibility through subnets, and flexible protocol governance.

The development roadmap is set with three main goals:
Scaling transaction throughput from ~100 tps to more than 5.000.000 tps
Improving the payment experience with a less than 3 second transaction finality time
Extending the protocol and establishing fork-free upgrades, allowing for more rapid, iterative development

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 20.06T XEC |
| **Total Supply** | 20.06T XEC |
| **Max Supply** | 21.00T XEC |
| **Fully Diluted Valuation** | $128.17M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.00038001 (2021-09-04) |
| **Current vs ATH** | -98.32% |
| **All-Time Low** | $0.00000481 (2026-07-01) |
| **Current vs ATL** | +32.78% |
| **24h Change** | -6.61% |
| **7d Change** | +24.63% |
| **30d Change** | +11.67% |
| **1y Change** | -71.22% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | XEC/USDT | N/A |
| Upbit | XEC/KRW | N/A |
| KuCoin | XEC/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://e.cash/](https://e.cash/) |
| **Twitter** | [@ecash](https://twitter.com/ecash) |
| **Reddit** | [https://www.reddit.com/r/ecash/](https://www.reddit.com/r/ecash/) |
| **Discord** | [https://discord.com/invite/HaVRXcST7n](https://discord.com/invite/HaVRXcST7n) |
| **GitHub** | [https://github.com/bitcoin-abc](https://github.com/bitcoin-abc) |
| **Whitepaper** | [https://e.cash/bitcoin.pdf](https://e.cash/bitcoin.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $16.23M |
| **Market Cap Rank** | #221 |
| **24h Range** | $0.00000640 — $0.00000707 |
| **CoinGecko Sentiment** | 80% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
