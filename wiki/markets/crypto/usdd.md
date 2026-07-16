---
title: "USDD"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi]
aliases: ["Decentralized USD", "USDD", "USDD 2.0"]
entity_type: protocol
founded: 2022
headquarters: "Decentralized (TRON DAO Reserve)"
website: "https://usdd.io/"
related: ["[[crypto-markets]]", "[[htx-dao]]", "[[stablecoin]]", "[[stablecoins]]", "[[tron]]", "[[usdt]]"]
---

# USDD

**USDD** (Decentralized USD; ticker **USDD**) is the [[tron|TRON]]-native [[stablecoin]] backed by the TRON DAO Reserve and closely associated with Justin Sun. Originally launched in May 2022 as an algorithmic stablecoin (weeks after Terra's UST collapse, briefly depegging to $0.928 in June 2022), it was relaunched in January 2025 as **USDD 2.0** — an overcollateralized design paying a heavily subsidized 20% APY. For traders it is primarily a [[stablecoin-yields|stablecoin-yield]] instrument and a depeg-risk monitor within the Justin Sun complex.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | USDD |
| **Current Price** | $0.998948 |
| **Market Cap** | $1,365,526,035 |
| **Market Cap Rank** | #56 |
| **24h Volume** | $20,653,224 |
| **24h Change** | -0.02% |
| **7d Change** | -0.04% |
| **Circulating Supply** | ~1.367B USDD |
| **Total Supply** | ~1.367B USDD |
| **Max Supply** | Uncapped (mint/burn vs collateral) |
| **Peg** | $1.00 (ATH $1.052 2023-10-23; ATL $0.928067 2022-06-19) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: as of 2026-06-21 USDD is **on peg at $0.9989** (a ~10 bps discount, within normal stablecoin trading bands) with ~$1.37B circulating — confirming the supply-growth trajectory Justin Sun flagged (1.1B in January 2026, targeting 2B). The peg has held tightly through the **"Established Bear Market"** ([[fear-and-greed-index|Fear & Greed]] 23); for a stablecoin the relevant read is peg integrity, not directional price. The persistent small sub-$1 discount is consistent with USDD's history of trading slightly below peg and reflects the market pricing in TRX-collateral and counterparty risk.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | USDD |
| **Sector** | Stablecoin (overcollateralized since USDD 2.0; formerly algorithmic) |
| **Collateral** | TRX, sTRX, USDT — collateralization ratio above 100% (e.g., $611M collateral vs $565M supply, August 2025) |
| **Yield** | ~20% APY on USDD 2.0, subsidized by TRON DAO |
| **Native chain** | [[tron|TRON]]; natively on Ethereum since September 2025; spans ~10 networks |
| **Website** | [https://usdd.io/](https://usdd.io/) |

---

## Overview

USDD is a decentralized stablecoin on TRON whose price stability is managed and guaranteed by the TRON DAO Reserve. The original 2022 design was algorithmic (TRX mint/burn), launched into the immediate aftermath of the UST collapse; it survived a June 2022 stress episode that took it to an all-time low of $0.9281 but traded persistently below peg for stretches of 2022.

**USDD 2.0**, launched **25 January 2025**, replaced the algorithmic model with an overcollateralized framework backed by TRX, sTRX and [[usdt|USDT]]. Its headline feature is a **20% APY** fully subsidized by TRON DAO — when pressed on sustainability, Justin Sun answered, "Simply because we have plenty of money."

---

## 2025–2026 Developments

- **USDD 2.0 launch (25 January 2025)** — overcollateralized redesign with 20% subsidized APY.
- **Native Ethereum deployment (8 September 2025)** — USDD launched natively on Ethereum; the coin now spans ~10 networks (TRON, Ethereum, BNB Chain, Avalanche, Polygon, etc.) with bridges via Stargate, Symbiosis, and DeBridge.
- **Supply growth** — Justin Sun announced on 18 January 2026 that USDD supply reached **1.1B**, targeting "2B soon"; supply was ~1.37B by the 2026-06-21 snapshot (rank #56), confirming continued growth.
- Peg held near $1.00 throughout 2025–H1 2026 under the overcollateralized model.

---

## Tokenomics & Supply

| Metric | Value (2026-06-21 snapshot) |
|---|---|
| **Circulating Supply** | ~1.367B USDD |
| **Total Supply** | ~1.367B USDD |
| **Max Supply** | Uncapped (mint against >100% collateral) |
| **Peg** | $1.00 (ATH $1.052 2023-10-23; ATL $0.928067 2022-06-19) |

Unlike a fixed-cap token, USDD supply expands and contracts via mint/redemption against TRON DAO Reserve collateral. There is no "dilution" in the equity sense — each USDD is meant to be backed by >$1 of TRX/sTRX/USDT — but supply growth concentrates more value in the reserve's TRX-heavy backing, which is the core risk (see below). Circulating ≈ total, so there is no vesting overhang.

---

## Valuation & Peg Framing

A stablecoin is "valued" not by upside but by **peg integrity and backing quality**. USDD screens as follows:

- **Peg**: trading at $0.9989 — a routine ~10 bps discount, well inside normal stablecoin bands. No active de-peg.
- **Backing**: overcollateralized (>100%) since USDD 2.0, but with **endogenous collateral** (TRX/sTRX) — the same structural failure-mode family as UST/LUNA, only with an overcollateralization buffer. A sharp TRX drawdown mechanically erodes the backing.
- **Yield**: the ~20% APY is a **marketing subsidy, not organic revenue** (Sun: "Simply because we have plenty of money"). The correct framing per [[stablecoin-yields]] is harvest-while-monitoring: collect the subsidy but watch for subsidy withdrawal and peg stress. Contrast [[ethena-usde|Ethena USDe]] (organic basis yield) and [[gho|GHO]]/sGHO.
- **Bottom line**: USDD is a higher-risk, higher-yield stablecoin whose "fair value" is $1.00 *conditional on* the reserve and the Justin Sun complex remaining solvent. The persistent sub-$1 discount is the market's standing risk premium.

---

## Peer Comparison

| Stablecoin | Price | Market Cap | Rank | Backing model | Yield |
|---|---|---|---|---|---|
| **USDD** | $0.9989 | $1.37B | #56 | Overcollateralized (TRX/sTRX/USDT) | ~20% subsidized |
| [[usdt\|USDT]] | ~$1.00 | tens of $B | top-5 | Fiat/T-bill reserves | none native |
| [[usdc\|USDC]] | ~$1.00 | tens of $B | top-10 | Fiat/T-bill reserves (Circle) | none native |
| [[euro-coin\|EURC]] | $1.15 | $439M | #111 | Euro fiat reserves (Circle) | none native |
| [[ethena-usde\|USDe]] | ~$1.00 | multi-$B | top-tier | Delta-neutral basis | organic |

> *Only USDD and EURC figures are from the 2026-06-21 snapshot; USDT/USDC/USDe shown qualitatively. USDD pairs the highest headline yield with the weakest (endogenous, TRX-linked) backing of the group.*

---

## Trading Relevance

- **Yield instrument**: the subsidized ~20% APY is one of the highest "stable" yields in crypto — a classic case for the [[stablecoin-yields]] framework: the yield is a marketing subsidy, not organic revenue, so the trade is harvesting it while monitoring subsidy withdrawal and peg health. Compare [[ethena-usde|Ethena USDe]] (organic basis yield) and [[gho|GHO]]/sGHO.
- **Where it trades**: [[kraken|Kraken]] (USDD/USD), KuCoin, HTX, TRON DEXs (SunSwap), Curve-style pools on Ethereum. Depth is far below [[usdt|USDT]]/[[usdc|USDC]].
- **Depeg monitoring**: USDD's 2022 history and its dependence on TRX collateral make the USDD/USDT spread a useful early-warning signal for stress in the **Justin Sun complex** ([[tron|TRX]], [[htx-dao|HTX]], HTX exchange). A TRX drawdown mechanically weakens the collateral backing.
- **Risk flags**: collateral concentration in TRX/sTRX (endogenous collateral — same failure mode family as UST/LUNA, though overcollateralized), opaque reserve governance via TRON DAO Reserve, key-man/regulatory exposure to Justin Sun, and an unsustainable subsidized yield that can be cut at any time.

### Contract Addresses (April 2026 snapshot)

| Chain | Address |
|---|---|
| Tron | `TXDk8mbtRbXeYuMNS83CfKPaYYT8XWv9Hz` |
| Ethereum | `0x4f8e5de400de08b164e7421b3ee387f461becd1a` |
| Binance Smart Chain | `0x45e51bc23d592eb2dba86da3985299f7895d66ba` |

---

## Risks

> **Peg / de-peg and Tron-counterparty risk are the dominant risks here.** USDD is a higher-yield stablecoin whose stability depends on the TRON DAO Reserve and the solvency of the Justin Sun complex — treat the 20% APY as compensation for that risk, not a free lunch.

- **De-peg risk**: USDD already broke peg once (to $0.928 in June 2022) and has a history of trading persistently below $1. The current $0.9989 is on-peg but the standing discount signals continuous market wariness.
- **Endogenous collateral**: backing is concentrated in TRX/sTRX — the same reflexive failure family as UST/LUNA. A TRX crash mechanically weakens collateral exactly when redemptions spike, even with an overcollateralization buffer.
- **Tron / key-man counterparty risk**: the reserve, governance, and yield subsidy all route through the Justin Sun / [[tron|TRON]] / [[htx-dao|HTX]] complex. Regulatory action against Sun or stress at HTX would transmit directly to USDD.
- **Subsidy withdrawal**: the ~20% APY is discretionary and can be cut at any time; yield-chasing inflows could reverse quickly if the subsidy ends.
- **Opaque reserve governance**: collateral disclosures via the TRON DAO Reserve are less transparent and less audited than [[usdc|USDC]]/[[usdt|USDT]] attestations.
- **Liquidity depth**: far thinner than USDT/USDC; large redemptions or swaps can move the peg.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://usdd.io/](https://usdd.io/) |
| **Twitter** | [@usddio](https://twitter.com/usddio) |
| **Docs** | [https://docs.usdd.io/](https://docs.usdd.io/) |

---

## Related

- [[tron]]
- [[stablecoin]]
- [[stablecoins]]
- [[stablecoin-yields]]
- [[usdt]]
- [[usdc]]
- [[euro-coin]]
- [[ethena-usde]]
- [[htx-dao]]
- [[fear-and-greed-index]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — April 2026 market snapshot
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko markets data (price $0.9989, cap $1.37B, rank #56)
- [Justin Sun unveils USDD 2.0 with 20% APY — Crypto Briefing](https://cryptobriefing.com/usdd-2-offers-20-apy/)
- [USDD launches natively on Ethereum — The Block, 2025-09](https://www.theblock.co/post/369855/usdd-the-justin-sun-backed-stablecoin-launches-natively-on-ethereum)
- [Justin Sun: USDD at 1.1B now, 2B soon — Blockchain.News, 2026-01-18](https://blockchain.news/flashnews/justin-sun-usdd-at-1-1b-now-2b-soon-stablecoin-update-traders-should-watch)
- [Dubious 20% Returns Offered as Justin Sun Unveils USDD 2.0 — Cryptonews Australia](https://cryptonews.com.au/news/dubious-20-returns-offered-as-justin-suns-unveils-usdd-2-0-stablecoin-125785/)
- Web search verification, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.45B USDD |
| **Total Supply** | 1.45B USDD |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $1.45B |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.05 (2023-10-23) |
| **Current vs ATH** | -5.01% |
| **All-Time Low** | $0.9281 (2022-06-19) |
| **Current vs ATL** | +7.65% |
| **24h Change** | -0.01% |
| **7d Change** | -0.04% |
| **30d Change** | -0.00% |
| **1y Change** | -0.12% |

---

## Platform & Chain Information

**Native Chain:** Tron

### Contract Addresses

| Chain | Address |
|---|---|
| Tron | `TXDk8mbtRbXeYuMNS83CfKPaYYT8XWv9Hz` |
| Ethereum | `0x4f8e5de400de08b164e7421b3ee387f461becd1a` |
| Binance Smart Chain | `0x45e51bc23d592eb2dba86da3985299f7895d66ba` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | USDD/USD | N/A |
| KuCoin | USDD/USDT | N/A |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $25.20M |
| **Market Cap Rank** | #52 |
| **24h Range** | $0.9989 — $0.9995 |
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

---
