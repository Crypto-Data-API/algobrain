---
title: "Bitcoin Cash"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, bitcoin, crypto]
aliases: ["BCH", "BCash"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://bch.info/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[dogecoin]]", "[[hyperliquid]]", "[[litecoin]]"]
---

# Bitcoin Cash

**Bitcoin Cash** (BCH) is a big-block hard fork of [[bitcoin|Bitcoin]] launched on 1 August 2017 to scale [[bitcoin]] as on-chain electronic cash. It keeps Bitcoin's [[proof-of-work|SHA-256 proof-of-work]] and 21M hard cap but rejects Segregated Witness (SegWit), raising the block-size limit (1MB → 8MB → 32MB) and upgrading mainly through hard forks rather than soft forks. For traders it is the archetypal **"cheap BTC proxy"** — a high-beta [[bitcoin]] payments fork that now ships annual May protocol upgrades expanding its smart-contract scripting. After a strong 2025, BCH has retraced hard with the broader alt market into mid-2026, sitting in the top 25–30 by market capitalization.

---

## Market Data

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Price** | $199.10 |
| **Market Cap** | $3,991,772,609 (~$3.99B) |
| **Market Cap Rank** | #26 |
| **24h Volume** | $101,585,182 (~$101.6M) |
| **24h Change** | +2.87% |
| **7d Change** | -2.72% |
| **Circulating Supply** | 20,050,231 BCH (~20.05M) |
| **Total Supply** | 20,050,275 BCH |
| **Max Supply** | 21,000,000 BCH (21M hard cap) |
| **All-Time High** | $3,785.82 (2017-12-20) — current is **-94.74%** below |
| **All-Time Low** | $76.93 (2018-12-16) — current is **+158.8%** above |

> **Macro backdrop (2026-06-20):** Crypto Fear & Greed Index = **22 (extreme fear)**; the market is in an **Established Bear Market**. BCH has fallen materially from its strong 2025 (the +64% y/y, "best-performing L1" framing was true at the *April 2026* snapshot near ~$440 and is now historical) — at ~$199 it is roughly half the April print, dropping it from ~#16 to **#26** by cap. As a high-beta [[bitcoin]] proxy, BCH tends to fall harder than BTC in risk-off regimes and snap back violently on BTC-led rallies. See [[narrative-trading]].

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BCH |
| **Market Cap Rank** | #26 (2026-06-20 — see [[#Market Data]]); historically top 15–20 |
| **Market Cap** | ~$3.99B (2026-06-20 — see [[#Market Data]]) |
| **Sector** | [[bitcoin]] fork, [[proof-of-work]] payments L1 with growing scripting (CashTokens/CHIPs) |
| **Supply** | 21M hard cap, ~20.05M circulating; same halving schedule family as BTC (last halving April 2024) |
| **Hashing Algorithm** | SHA-256 ([[proof-of-work]]) |
| **Block size** | 32MB (vs Bitcoin's ~1MB base / ~4MB weight) |
| **Categories** | Smart Contract Platform, Layer 1 (L1), [[bitcoin]] Fork, Proof of Work (PoW), Coinbase 50 Index |
| **Website** | [https://bch.info/](https://bch.info/) |

---

## Technology & Consensus

Bitcoin Cash shares [[bitcoin|Bitcoin]]'s core architecture — UTXO model, [[proof-of-work|SHA-256 proof-of-work]], ~10-minute target block time, 21M supply cap, and the same four-year halving schedule — but diverges on the scaling philosophy that caused the 2017 split.

| Property | Bitcoin Cash | Bitcoin (for contrast) |
|---|---|---|
| **Consensus** | [[proof-of-work\|SHA-256 PoW]] | [[proof-of-work\|SHA-256 PoW]] |
| **Block size limit** | 32MB | ~1MB base / ~4MB weight units |
| **SegWit** | Rejected (no witness segregation) | Activated 2017 |
| **Scaling approach** | On-chain (bigger blocks) | Off-chain ([[lightning-network\|Lightning]] / L2) |
| **Upgrades** | Mostly **hard forks** (annual May CHIPs) | Mostly soft forks |
| **Smart contracts** | CashTokens + expanding Script (Loops, Functions, BigInt) | Limited Script / Taproot |
| **Supply cap** | 21M | 21M |

**Fork lineage.** BCH forked from [[bitcoin]] on **2017-08-01** to lift the block-size limit (1MB → 8MB, later 32MB), letting miners process far more on-chain payments per second at lower fees. On **2018-11-16** a contentious "hash war" split BCH again into **Bitcoin Cash (ABC)** — the surviving BCH chain — and **Bitcoin SV (BSV)**, which pushed for even larger blocks and a different scripting roadmap.

**CashTokens & annual upgrades.** Since 2023 BCH adds native fungible/non-fungible tokens (CashTokens) and ships a predictable annual upgrade each **May 15** via the community CHIP (Cash Improvement Proposal) process:

- **2025-05-15 — "VELMA":** CHIP-2021-05 (Targeted VM Limits — removed the 201-opcode limit, raised stack elements from 520 bytes to 10,000 bytes) and CHIP-2024-07 (BigInt high-precision arithmetic), enabling heavier on-chain computation including zero-knowledge-proof and post-quantum-crypto applications.
- **2026-05-15 — "LAYLA":** four approved CHIPs — **Loops, Pay-to-Script, Functions, and Bitwise operations** — a major expansion of BCH Script toward reusable, more complex smart contracts.

Because BCH and [[bitcoin]] share SHA-256, the same ASIC fleets can mine either chain; BCH's security budget therefore depends on miners toggling from BTC when BCH is relatively profitable.

---

## Overview

Bitcoin Cash is a hard fork of Bitcoin with a protocol upgrade to fix on-chain capacity. Bitcoin Cash intends to be a Bitcoin without Segregated Witness (SegWit) as soft fork, where upgrades of the protocol are done mainly through hard forks and without changing the original economic rules of the Bitcoin.

Bitcoin Cash (BCH) is released on 1st August 2017 as an upgraded version of the original Bitcoin Core software. The main upgrade is the increase in the block size limit from 1MB to 8MB. This effectively allows miners on the BCH chain to process up to 8 times more payments per second in comparison to Bitcoin. This makes for faster, cheaper transactions and a much smoother user experience.

Why was Bitcoin Cash Created?

The main objective of Bitcoin Cash is to to bring back the essential qualities of money inherent in the original Bitcoin software. Over the years, these qualities were filtered out of Bitcoin Core and progress was stifled by various people, organizations, and companies involved in Bitcoin protocol development. The result is that Bitcoin Core is currently unusable as money due to increasingly high fees per transactions and transfer times taking hours to complete. This is all because of the 1MB limitation of Bitcoin Core’s block size, causing it unable to accommodate to large number of transactions.

Essentially Bitcoin Cash is a community-activated upgrade (otherwise known as a hard fork) of Bitcoin that increased the block size to 8MB, solving the scaling issues that plague Bitcoin Core today.

Nov 16th 2018: A hashwar resulted in a split between Bitcoin SV and Bitcoin ABC

---

## Tokenomics & Supply

> *Supply figures from the 2026-06-20 CoinGecko snapshot (see [[#Market Data]]).*

| Metric | Value |
|---|---|
| **Circulating Supply** | ~20.05M BCH (~95.5% of cap mined) |
| **Total Supply** | ~20.05M BCH |
| **Max Supply** | 21.00M BCH (same hard cap as [[bitcoin]]) |
| **Fully Diluted Valuation** | ~$3.99B (FDV ≈ market cap) |
| **Market Cap / FDV Ratio** | ~1.00 |

BCH inherits [[bitcoin]]'s **fixed 21M supply schedule** and the same four-year **halving** cadence — the last halving was **April 2024** (block reward 6.25 → 3.125 BCH), and the next is due around 2028. With ~20.05M already mined, BCH is ~95% of the way to its cap, so new issuance is small and falling. There is no premine and no foundation allocation; supply economics are identical to Bitcoin's, which is precisely the "same scarcity, lower price" pitch behind the cheap-BTC-proxy trade.

---

## Price History

> Current figures from the 2026-06-20 snapshot (see [[#Market Data]]); ATH/ATL are all-time anchors.

| Metric | Value |
|---|---|
| **All-Time High** | $3,785.82 (2017-12-20) |
| **Current vs ATH** | -94.74% |
| **All-Time Low** | $76.93 (2018-12-16) |
| **Current vs ATL** | +158.8% |
| **24h Change** | +2.87% |
| **7d Change** | -2.72% |

BCH peaked at **$3,785.82 in December 2017**, weeks after its August fork, during the original ICO-era mania. It has never reclaimed that level. BCH staged a strong run through 2025 (cited as a top-performing major L1, near ~$440 at the April 2026 snapshot, +64% y/y at that time) but has since retraced sharply with the broader alt market — the 2026-06-20 print of ~$199 is roughly half the April level, leaving it ~94.7% below ATH while still ~2.6× above its 2018 cycle low.

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | BCH/USDT | N/A |
| Kraken | BCH/USD | N/A |
| Upbit | BCH/KRW | N/A |
| Bitget | BCH/USDT | N/A |
| KuCoin | BCH/USDT | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | BCH-PERP | Perpetual |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://bch.info/](https://bch.info/) |
| **Reddit** | [https://www.reddit.com/r/btc](https://www.reddit.com/r/btc) |
| **Telegram** | [bchchannel](https://t.me/bchchannel) (3,552 members) |
| **GitHub** | [https://github.com/bitcoincashorg/bitcoincash.org](https://github.com/bitcoincashorg/bitcoincash.org) |
| **Whitepaper** | [https://bch.info/bitcoin.pdf](https://bch.info/bitcoin.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 322 |
| **GitHub Forks** | 225 |
| **Pull Requests Merged** | 454 |
| **Contributors** | 57 |

---

## Trading Characteristics

> *Current figures as of 2026-06-20 (see [[#Market Data]]).*

| Characteristic | Detail |
|---|---|
| **Price** | $199.10 |
| **24h Volume** | ~$101.6M |
| **Market Cap Rank** | #26 |
| **24h Change** | +2.87% |
| **Last Updated** | 2026-06-20 |

Volume of ~$101.6M against a ~$3.99B cap is subdued — consistent with the **extreme-fear / bear-market** backdrop (F&G = 22). BCH's exchange float is modest, which is exactly why it is squeeze-prone in BTC-led rallies and why Korean ([[#Market Structure & Derivatives|Upbit]]) flow can move it violently.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events (2025–2026)

- **2025-05-15 — "VELMA" network upgrade.** Activated CHIP-2021-05 (Targeted VM Limits — removed the 201-opcode limit, raised stack elements from 520 bytes to 10,000 bytes) and CHIP-2024-07 (BigInt high-precision arithmetic), enabling heavier on-chain computation including zero-knowledge-proof and post-quantum-crypto applications.
- **2025 — standout performance (historical).** BCH was repeatedly cited as the best-performing major L1 of *2025* (+64% y/y as measured at the April 2026 snapshot, while most alt majors were down). *Note: this gain has since been given back — by 2026-06-20 BCH had retraced to ~$199, see [[#Market Data]].*
- **2026-05-15 — annual upgrade ("LAYLA").** Activated four approved CHIPs: Loops, Pay-to-Script, Functions, and Bitwise operations — a major expansion of BCH Script toward reusable, more complex smart contracts.
- Historical anchors retained: fork from Bitcoin 2017-08-01 (8MB blocks, later 32MB); 2018-11-16 hash-war split with Bitcoin SV.

---

## Ecosystem & Use Cases

BCH is positioned first as **electronic cash** — fast, low-fee on-chain payments — and second as an increasingly capable smart-contract chain.

| Use case | Detail |
|---|---|
| **Low-fee payments** | Sub-cent fees and large blocks make BCH viable for everyday transactions and remittances; the original "peer-to-peer electronic cash" thesis |
| **Merchant acceptance** | Long-running merchant adoption push via the Bitcoin.com ecosystem and payment processors; point-of-sale and tipping tooling |
| **CashTokens** | Native fungible + non-fungible tokens (since 2023) enable stablecoins, NFTs, and DeFi-style apps directly on BCH without a separate L2 |
| **Smart contracts** | Expanding Script (post-VELMA/LAYLA: BigInt, Loops, Functions, Pay-to-Script) supports more complex covenants and on-chain logic |
| **Bitcoin.com wallet** | A large consumer wallet/brand historically aligned with BCH, anchoring retail distribution |

Unlike [[ethereum]]-class chains, BCH keeps the UTXO model and a minimalist design — it competes on cheap, reliable payments and lightweight programmability rather than a sprawling DeFi/dApp stack.

---

## Market Structure & Derivatives

| Venue type | Detail |
|---|---|
| **Spot CEX** | Deep books on [[binance\|Binance]], [[coinbase\|Coinbase]], [[kraken\|Kraken]], **Upbit** (notably strong Korean flow), Bitget, KuCoin |
| **Perpetuals** | **BCH-PERP** on [[hyperliquid]] and all major perp venues; a liquid, frequently-shorted altcoin perp |
| **Funding / OI** | Funding flips positive in BTC-led rallies (crowded longs / squeeze fuel) and negative in capitulation; OI spikes flag crowded positioning |
| **ETP** | Accessible to US equity traders via **Grayscale's Bitcoin Cash Trust**; no broad spot BCH ETF as of this writing |
| **CME futures** | No standardized CME BCH future; perp funding is the primary derivatives signal |

**Squeeze-prone modest float.** Exchange float is small relative to cap, so BCH is prone to sharp short squeezes when BTC rallies and shorts are crowded. The **Korean-pump signature** — sudden Upbit-driven KRW volume spikes that decouple BCH from global pricing, then reverse violently — is a recurring, tradable (and dangerous) BCH pattern.

---

## Trading Playbook

- **Role in a book:** BCH trades as a **high-beta [[bitcoin]] proxy** — same SHA-256 mining economics and halving cycle, a fraction of the price. Beta to BTC is >1 in both directions.
- **Cheap-BTC catch-up trade:** in the **"payments / PoW legacy" basket** with [[litecoin]] and [[dogecoin]], BCH periodically rotates as the "cheap BTC" catch-up play *late* in BTC-led cycles — after BTC has run and capital rotates down the quality curve.
- **Squeeze setups:** modest exchange float + crowded shorts in a BTC-dominance basket make BCH a recurring squeeze candidate; watch perp funding/OI and the BCH/BTC ratio.
- **Korean-volume signal:** sudden Upbit KRW volume spikes are a classic BCH pump signature — high-momentum but mean-reverting; size and stops matter.
- **Catalysts to trade:** annual **May 15** upgrades (scripting capability is becoming a differentiator), hashrate migration vs BTC profitability, Korean-exchange volume spikes, and any US ETP developments for non-BTC PoW assets.
- **Short side:** BCH is a perennial **short candidate in "BTC dominance" baskets** — when capital concentrates into BTC, forks like BCH bleed relative value.
- **Regime note:** in the current **extreme-fear / bear** backdrop (F&G = 22), high-beta forks like BCH typically underperform BTC until risk appetite returns.

---

## History & Cycles

| Date | Event |
|---|---|
| **2017-08-01** | BCH forks from [[bitcoin]] over the block-size debate (1MB → 8MB, later 32MB) |
| **2017-12-20** | All-time high $3,785.82 amid ICO-era mania |
| **2018-11-16** | "Hash war" split into **Bitcoin Cash (ABC)** and **Bitcoin SV (BSV)** |
| **2020 / 2024** | Halvings (reward cut; April 2024 → 3.125 BCH) |
| **2023** | CashTokens launch — native tokens on BCH |
| **2025-05-15** | **VELMA** upgrade — VM limits + BigInt arithmetic |
| **2025** | Cited as a top-performing major L1 of *2025* (≈+64% y/y at the April 2026 snapshot) — *a 2025-dated historical claim* |
| **2026-05-15** | **LAYLA** upgrade — Loops, Pay-to-Script, Functions, Bitwise ops |
| **2026-06** | ~$199 in an Established Bear Market (F&G = 22) — ~94.7% below ATH, rank #26 |

BCH's price cycles closely track [[bitcoin]]'s with higher amplitude: it overshoots in late-cycle alt rotations and gives back outperformance fastest in bear markets — exactly the round trip seen between its strong 2025 and the mid-2026 retrace.

---

## Competitive Positioning

The two legacy [[bitcoin]] forks/proxies traders most often pair are **[[litecoin|Litecoin (LTC)]]** and **Bitcoin Cash (BCH)** — both are old, high-liquidity PoW payments coins with hard caps, but they differ on algorithm, block design, and fork lineage.

| Coin | Rank (2026-06-20) | Algorithm | Block time / size | Supply cap | Fork lineage | Niche |
|---|---|---|---|---|---|---|
| **Bitcoin Cash (BCH)** | #26 | SHA-256 | ~10 min / 32MB | 21M | Direct [[bitcoin]] fork (2017); BSV split (2018) | Big-block on-chain payments + CashTokens scripting |
| **[[litecoin\|Litecoin (LTC)]]** | #30 | Scrypt | 2.5 min / ~1MB | 84M | 2011 [[bitcoin]] code fork | "Digital silver"; merge-mined with [[dogecoin]]; LTCC ETF |
| **[[bitcoin\|Bitcoin (BTC)]]** | #1 | SHA-256 | ~10 min / ~1MB base | 21M | Original | Reserve asset / "digital gold" |

**BCH vs Bitcoin directly:** BCH bets on *on-chain* scaling (bigger blocks, lower fees) while [[bitcoin]] scales *off-chain* (Lightning/L2) and keeps blocks small for decentralization. BCH shares BTC's SHA-256 mining and 21M cap, so it competes on cheaper transactions and faster scripting — at the cost of far less liquidity, security budget, and developer mindshare than BTC.

---

## Risks

- **Liquidity & mindshare:** BCH's liquidity and developer mindshare remain far below [[bitcoin]]; in bear regimes its depth thins, amplifying slippage and squeeze risk.
- **Security-budget dependence:** the chain's security depends on SHA-256 miners toggling over from BTC when BCH is relatively profitable — a structural vulnerability if BCH price/fees fall versus BTC.
- **Violent Korean-driven reversals:** sudden Upbit-led KRW pumps can spike and then collapse, trapping momentum chasers.
- **Contentious-fork history:** the 2018 BSV hash war showed BCH governance can fracture; future CHIP disagreements carry split risk.
- **High beta in drawdowns:** as a BTC proxy, BCH falls harder than BTC in risk-off markets (currently ~94.7% below ATH, F&G = 22).
- **Narrative competition:** newer payments/L1s and stablecoins compete for the "cheap on-chain money" use case BCH targets.

---

## See Also

- [[crypto-markets]]
- [[bitcoin]] — parent chain; dominant price driver; BCH/BTC ratio
- [[litecoin]] — fellow legacy-PoW fork/proxy (peer)
- [[dogecoin]] — payments/PoW-legacy basket member
- [[proof-of-work]] — consensus mechanism (SHA-256)
- [[hyperliquid]] — BCH-PERP venue
- [[narrative-trading]] — cheap-BTC / PoW-legacy rotation framework

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- bch.info: "May 15th, 2025 Bitcoin Cash network upgrade" — https://bch.info/en/upgrade
- The Bitcoin Cash Podcast: "What is the 2025 (Velma) upgrade?" — https://bitcoincashpodcast.com/faqs/Tech/Protocol-Upgrades/2025-velma
- Buy Hodl Sell: "Bitcoin Cash May 2026 Upgrade Preview" (Loops, Pay-to-Script, Functions, Bitwise CHIPs) — https://buyhodlsell.com/articles/bch-may-2026-upgrade-preview
- AInvest: "Why Bitcoin Cash (BCH) is the Best Performing L1 Blockchain of 2025" (Dec 2025) — https://www.ainvest.com/news/bitcoin-cash-bch-performing-l1-blockchain-2025-strong-buy-2026-2512/
- Verified via Perplexity (sonar) + web search, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 20.06M BCH |
| **Total Supply** | 20.06M BCH |
| **Max Supply** | 21.00M BCH |
| **Fully Diluted Valuation** | $4.43B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
