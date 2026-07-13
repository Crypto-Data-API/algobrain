---
title: "Shiba Inu"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, altcoins, ethereum]
aliases: ["SHIB", "SHIB Army", "Shibarium"]
entity_type: protocol
founded: 2020
headquarters: "Decentralized (anonymous founder 'Ryoshi')"
website: "https://shibatoken.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[dogecoin]]", "[[official-trump]]"]
---

# Shiba Inu

**Shiba Inu** (SHIB) is a decentralized, community-led ERC-20 token launched in August 2020 by the anonymous "Ryoshi" as a self-styled "Dogecoin killer". For traders it is one of the two benchmark large-cap **[[meme-coin|meme coins]]** (with [[dogecoin|Dogecoin]]) — a pure retail-sentiment beta instrument — even as the project keeps building utility around it: the ShibaSwap DEX, the Shibarium [[layer-2|Layer 2]], and a 2026 privacy-focused L3 ("Shib Alpha Layer").

---

## Market Data

| Metric | Value |
|---|---|
| **Price** | $0.00000471 |
| **Market Cap** | $2,776,007,673 (~$2.78B) |
| **Market Cap Rank** | #35 |
| **24h Volume** | $46,884,022 (~$46.9M) |
| **24h Change** | -0.10% |
| **7d Change** | -4.62% |
| **Circulating Supply** | 589,243,170,274,984 SHIB (~589.24T) |
| **Total Supply** | 589,499,835,792,924 SHIB (~589.50T) |
| **Max Supply** | Uncapped (no max) |
| **All-Time High** | $0.00008616 (2021-10-28) — current is **-94.53%** below ATH |
| **All-Time Low** | $0.000000000056366 (2020-11-28) |

**Macro backdrop:** Crypto Fear & Greed Index = **22 (extreme fear)**; market regime classed as an **Established Bear Market** — high-beta meme assets like SHIB typically bleed hardest in this environment. See [[crypto-markets]].

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SHIB |
| **Market Cap Rank** | #35 (2026-06-20); was #32 at April 2026 snapshot |
| **Market Cap** | ~$2.78B (2026-06-20) |
| **Chain / Sector** | ERC-20 on [[ethereum|Ethereum]] + Shibarium [[layer-2|L2]] + Shib Alpha Layer L3; sector: [[meme-coin\|meme]] / community token |
| **Categories** | Meme, Ethereum Ecosystem, Animoca Brands Portfolio, Dog-Themed, GMCI Meme Index, GMCI 30 Index, GMCI Index, Coinbase 50 Index |
| **Website** | [https://shibatoken.com/](https://shibatoken.com/) |

---

## Overview

Shiba Inu (SHIB) is a decentralized, community-led cryptocurrency ecosystem built on the Ethereum blockchain. Originally launched as a meme-based project, it has evolved into a comprehensive financial ecosystem designed to offer a decentralized alternative to traditional banking. Its main value proposition lies in its transition from a social phenomenon into a functional utility network, supported by a vast global community known as the ShibArmy and a commitment to 100% community ownership with no central leadership.

The ecosystem features its own decentralized exchange, ShibaSwap, where users can trade, provide liquidity, and earn rewards. To address Ethereum’s high costs and slow speeds, the project utilizes Shibarium, a Layer 2 scaling solution that processes transactions faster and more affordably.

The project employs a unique three-token model to manage its economy and governance. SHIB serves as the primary currency for trading and payments, while LEASH offers scarcity-based incentives for dedicated supporters. BONE acts as the governance token, allowing holders to vote on proposals through the Doggy DAO and serving as the native gas token for the Shibarium network.

---

## Technology & Consensus

SHIB has **no consensus mechanism of its own** — it is an [[ethereum|Ethereum]] ERC-20 token whose security, finality, and settlement are inherited from Ethereum's [[proof-of-stake]] validator set. This is a key distinction from coins like [[dogecoin]] (its own [[proof-of-work]] Scrypt chain) or [[litecoin]]: SHIB pays Ethereum gas, depends on Ethereum's reorg/MEV environment, and rides Ethereum's roadmap. The broader ecosystem then layers its own infrastructure on top.

| Layer | Component | Role / Architecture |
|---|---|---|
| **L1** | [[ethereum]] | Settlement and security for the SHIB ERC-20 token (secured by Ethereum [[proof-of-stake]]) |
| **L2** | **Shibarium** | EVM-compatible [[layer-2]] using a Polygon-style **Heimdall (consensus/checkpoint) + Bor (block production)** architecture; **BONE is the native gas token**; checkpoints settle to Ethereum |
| **L3** | **Shib Alpha Layer** | Privacy-focused L3 introduced 2026 with **Fully Homomorphic Encryption (FHE) via Zama**, targeting confidential on-chain transactions and private smart contracts |

Shibarium exists to give the ecosystem cheap, fast execution (typical gas fees $0.001–0.005) while still anchoring to Ethereum for security — the standard [[layer-2]] tradeoff. The Shib Alpha Layer extends this with confidentiality, a direct response to the September 2025 bridge exploit (see History below).

---

## Tokenomics & Supply

SHIB runs an **uncapped** supply with a famous (and misunderstood) burn narrative. The economy is governed by a **three-token model**:

| Token | Role | Notes |
|---|---|---|
| **SHIB** | Primary meme/payment token | ~589T circulating; the asset traders speculate on |
| **LEASH** | Scarcity/incentive token | Very small supply; rewards dedicated holders |
| **BONE** | Governance + Shibarium gas | Used for Doggy DAO votes and L2 transaction fees |

**Burn mechanism.** Community and Shibarium-linked burns permanently remove SHIB from circulation; cumulative burns passed **410 trillion SHIB by March 2026** and Shibarium-linked burns removed ~15B SHIB since the network stabilized in late 2025. **Critically, this is a sentiment signal, not a supply squeeze:** against a ~589T circulating supply, even trillions of burns barely dent float, and there is no hard max supply, so issuance/burn balance does not create [[bitcoin]]-style scarcity. Burn-rate *spikes* matter to traders because they correlate with retail attention, not because they meaningfully tighten supply.

With near-1.00 market-cap / FDV (no large locked-token overhang), SHIB price action is almost entirely **flow- and sentiment-driven** rather than unlock-driven.

---

## Ecosystem & Use Cases

| Component | What it is |
|---|---|
| **ShibaSwap** | Native decentralized exchange (DEX) for swapping, LP'ing, and earning rewards |
| **Shibarium** | EVM [[layer-2]] for cheap/fast transactions; cumulative transactions exceeded **500M by early 2026** |
| **Shib Alpha Layer** | Privacy L3 (Zama FHE) for confidential transactions and private contracts |
| **Metaverse / Games** | "Shib: The Metaverse" and gaming initiatives extend the brand beyond a pure token |
| **ShibArmy** | The large, vocal retail community — the project's core distribution and marketing engine, and the source of its meme beta |

The strategic thesis is the migration from "pure meme" to "meme + utility network," but for trading purposes SHIB's value is still overwhelmingly driven by [[meme-coin]] sentiment rather than ecosystem cash flows.

---

## Market Structure & Derivatives

- **Spot venues:** [[binance|Binance]], [[coinbase|Coinbase]], [[kraken|Kraken]], Upbit, Bitget, KuCoin, Crypto.com, plus [[uniswap|Uniswap]] V2/V3 on Ethereum. Deep, globally distributed spot books.
- **Derivatives:** SHIB perpetual futures are listed across all major derivatives venues; funding and open interest swing with retail positioning. Because SHIB is a high-beta [[meme-coin]], implied/realized volatility runs well above the majors, and funding can flip sharply during meme-rotation phases.
- **ETF speculation (qualitative):** the 2025–2026 US altcoin-ETF wave — including the first US spot [[dogecoin|DOGE]] ETFs — keeps recurring "SHIB ETF" speculation alive as a headline trade. **No SHIB ETF figures are asserted here**; the DOGE precedent simply makes the narrative a periodic catalyst rather than a confirmed product.
- **Float dynamics:** uncapped supply and near-1.00 MC/FDV mean price is set at the margin by exchange flow and sentiment, not by scheduled unlocks.

---

## Trading Playbook

- **What it is in a book:** SHIB is a **high-beta retail-sentiment proxy** — alongside [[dogecoin]] it anchors the large-cap [[meme-coin]] basket. It outperforms late in risk-on phases and bleeds in chop and bear regimes (like the current Established Bear Market).
- **Basket behavior:** GMCI Meme Index constituent with [[dogecoin]], PEPE, BONK and [[official-trump|TRUMP]]. When DOGE leads and SHIB follows with higher beta, meme-season rotation is typically on; see [[narrative-trading]].
- **Catalysts:** burn-rate spikes (sentiment trigger, not supply math), Shibarium/L3 privacy milestones, exchange burn integrations, broad meme-cycle rotation, and "SHIB ETF" headlines.
- **Risk framing:** in extreme-fear regimes (F&G = 22 today) high-beta meme assets are the first to be cut; size accordingly and treat SHIB as a tactical, sentiment-timed position rather than a hold.

---

## History & Cycles

- **2020 (August)** — launched by anonymous founder "Ryoshi" as a community ERC-20 "Dogecoin killer"; half the supply famously sent to Vitalik Buterin (who later burned a large portion).
- **2021** — peak meme mania; SHIB hit its ATH of **$0.00008616 (2021-10-28)**, briefly reaching a top-10 market cap.
- **2022–2024** — bear-market drawdown; pivot toward utility (ShibaSwap, Shibarium development).
- **2025 (September)** — **Shibarium bridge hack** (~$4.1M drained via flash loans + compromised validator keys); bridge frozen, attacker permissions revoked; SHIB sold off and BONE collapsed.
- **2026** — **Shib Alpha Layer (L3)** privacy roadmap (Zama FHE) targeting confidentiality, partly in response to the exploit; cumulative burns >410T; Shibarium transactions >500M.

---

## Competitive Positioning

SHIB and [[dogecoin]] are the two benchmark large-cap meme assets; PEPE and BONK round out the high-beta meme basket.

| Coin | MC Rank (2026-06-20) | Chain | Supply Model | Utility / Ecosystem | Narrative |
|---|---|---|---|---|---|
| [[dogecoin\|DOGE]] | #11 | Own Scrypt PoW L1 | Uncapped, ~5B/yr tail | Payments/tipping; US spot ETFs; commodity status | OG meme; retail-sentiment benchmark |
| **SHIB** | **#35** | ERC-20 on [[ethereum]] + Shibarium L2 + L3 | Uncapped, burn narrative | ShibaSwap, Shibarium, Shib Alpha Layer | "Doge killer"; meme + utility build-out |
| PEPE | top-50 range | ERC-20 on [[ethereum]] | Fixed supply | Minimal (pure meme) | High-beta meme momentum play |
| BONK | top-100 range | Solana SPL | Large fixed supply | Solana meme/ecosystem | Solana-cycle meme beta |

Relative to DOGE, SHIB carries **more ecosystem ambition** (its own L2/L3) but **less liquidity, no commodity status, no confirmed ETF, and higher beta** — it tends to lag DOGE up and lead DOGE down.

---

## 2025–2026 Developments

- **Shibarium bridge hack (September 2025)** — attackers drained ~**$4.1M** from the Shibarium bridge using flash loans plus compromised validator signing keys. Lead developer Kaal Dhairya called it a months-in-planning "sophisticated" attack; the team froze bridge operations and revoked attacker permissions. SHIB sold off and BONE collapsed on the news.
- **Shib Alpha Layer (L3) + privacy roadmap** — partly in response to the exploit, the team introduced an L3 with **Fully Homomorphic Encryption via Zama**, targeting full on-chain confidentiality and private smart contracts by **Q2 2026**.
- **Burn program** — community burns passed **410 trillion SHIB cumulative by March 2026**; Shibarium-linked burns removed ~15B SHIB since the network's late-2025 stabilization; burn rate briefly spiked >10,000% at the start of 2026. (Context: with ~589T circulating, burns remain small relative to supply — a sentiment signal more than a supply squeeze.)
- **Shibarium scale** — cumulative transactions exceeded **500M by early 2026**, with typical gas fees of $0.001-0.005.

---

## Tokenomics (snapshot table)

> *Figures as of 2026-06-20; see [[#Tokenomics & Supply]] above for mechanism detail.*

| Metric | Value |
|---|---|
| **Circulating Supply** | 589.24T SHIB |
| **Total Supply** | 589.50T SHIB |
| **Max Supply** | Unlimited (uncapped) |
| **Fully Diluted Valuation** | ~$2.78B |
| **Market Cap / FDV Ratio** | ~1.00 |

---

## Price History (snapshot: 2026-06-20, CoinGecko)

| Metric | Value |
|---|---|
| **Price** | $0.00000471 |
| **All-Time High** | $0.00008616 (2021-10-28) |
| **Current vs ATH** | -94.53% |
| **All-Time Low** | $0.000000000056366 (2020-11-28) |
| **24h Change** | -0.10% |
| **7d Change** | -4.62% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SHIB/USDT | N/A |
| Kraken | SHIB/USD | N/A |
| Upbit | SHIB/KRW | N/A |
| Bitget | SHIB/USDT | N/A |
| KuCoin | SHIB/USDT | N/A |
| Crypto.com Exchange | SHIB/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X95AD61B0A150D79219DCF64E1E6CC01F0B64C4CE/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X95AD61B0A150D79219DCF64E1E6CC01F0B64C4CE/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://shibatoken.com/](https://shibatoken.com/) |
| **Twitter** | [@shibarium_](https://twitter.com/shibarium_) |
| **Reddit** | [https://www.reddit.com/r/SHIBArmy/](https://www.reddit.com/r/SHIBArmy/) |
| **Telegram** | [ShibaInu_Dogecoinkiller](https://t.me/ShibaInu_Dogecoinkiller) (83,267 members) |
| **Discord** | [https://discord.com/invite/shibatoken](https://discord.com/invite/shibatoken) |
| **Whitepaper** | [https://shib.io/documents/SHIBPAPER-ABRIDGED-V.1.pdf](https://shib.io/documents/SHIBPAPER-ABRIDGED-V.1.pdf) |

---

## Trading Characteristics (snapshot: 2026-06-20)

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$46.9M |
| **Market Cap Rank** | #35 |
| **Price** | $0.00000471 |
| **Macro Regime** | Established Bear Market; Fear & Greed = 22 (extreme fear) |
| **Last Updated** | 2026-06-20 |

---

## Trading Relevance

- **Where it trades**: spot everywhere — [[binance|Binance]], [[kraken|Kraken]], [[coinbase|Coinbase]], Upbit, Bitget, KuCoin, Crypto.com, plus Uniswap V2/V3; SHIB perps are listed on all major derivatives venues. A US spot DOGE ETF already exists (2025-2026 altcoin-ETF wave), keeping "SHIB ETF" speculation alive as a recurring headline trade.
- **Narrative basket**: the **meme basket** — GMCI Meme Index constituent alongside [[dogecoin]], PEPE, BONK and [[official-trump|TRUMP]]. SHIB is a high-beta retail-sentiment proxy: it outperforms late in risk-on phases and bleeds in chop.
- **Catalysts**: burn-rate spikes (sentiment trigger, not supply math), Shibarium/L3 privacy launch (Q2 2026 target), exchange burn integrations, and broad meme-cycle rotation signals.
- **Risk profile**: ~94.5% below its October 2021 ATH (2026-06-20); near-1.00 MC/FDV means no unlock overhang — price action is almost entirely flow/sentiment-driven. The September 2025 bridge hack is a reminder of ecosystem-infrastructure risk that bleeds into SHIB itself.

---

## Risks

| Risk | Description |
|---|---|
| **Meme / sentiment dependence** | SHIB has no cash flows; price is set by retail attention and [[meme-coin]] rotation. It outperforms in mania and bleeds first in fear (F&G = 22 today). |
| **Infinite supply** | Uncapped supply with no hard max; burns are a sentiment signal, not a meaningful supply squeeze against ~589T circulating — no [[bitcoin]]-style scarcity thesis. |
| **Ecosystem-infrastructure risk** | The **September 2025 Shibarium bridge hack** (~$4.1M, compromised validator keys) shows L2/bridge exploits can crater BONE and bleed into SHIB. |
| **Narrative dependence** | Value leans on the "Doge killer" / meme + utility story; if the meme cycle fades or DOGE consolidates the meme bid, SHIB underperforms. |
| **Liquidity in a bear** | High-beta, retail-heavy float means thin two-sided liquidity in drawdowns — slippage and gap risk rise exactly when you want to exit. |
| **Competitive crowding** | Faces [[dogecoin]] (deeper liquidity, ETFs, commodity status) above it and faster meme rotations (PEPE, BONK) below it. |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[ethereum]] — base chain (security via [[proof-of-stake]])
- [[layer-2]] — Shibarium's scaling category
- [[dogecoin]] — the original meme benchmark and closest peer
- [[meme-coin]] — the asset class SHIB anchors
- [[official-trump]] — political meme-basket peer
- [[uniswap]] — primary DEX venue
- [[narrative-trading]] — meme-cycle / rotation framework

---

## Sources

- CoinGecko top-1000 snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- [CCN — $4.1M Shibarium Bridge Hack: SHIB Tanks, BONE Collapses & Validator Keys Compromised (Sep 2025)](https://www.ccn.com/education/crypto/shibarium-bridge-hack-shib-bone-crash-explained/)
- [Cointribune — Shiba Inu: Shibarium Privacy Upgrade Targets 2026](https://www.cointribune.com/en/shiba-inu-shibarium-privacy-upgrade-targets-2026/)
- [U.Today — Major Privacy Roadmap for Shibarium Revealed (Zama FHE)](https://u.today/shiba-inu-shib-news-major-privacy-roadmap-for-shibarium-revealed)
- [TradingKey — Shiba Inu 2026: L3 Evolution, burn rate, Shibarium](https://www.tradingkey.com/analysis/cryptocurrencies/more/261631516-shiba-inu-coin-swap-burn-rate-shibarium-tradingkey)
- [KuCoin — Complete Guide to the SHIB Burn](https://www.kucoin.com/blog/shiba-inu-burn)
- Verified via Perplexity (sonar) and web search, 2026-06-10.
