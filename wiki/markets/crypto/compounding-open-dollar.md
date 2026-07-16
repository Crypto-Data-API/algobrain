---
title: "Compounding OpenDollar"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, real-world-assets, stablecoin]
aliases: ["CUSDO", "Compounding Open Dollar", "cUSDO"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://openeden.com"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[real-world-assets]]", "[[stablecoins]]", "[[treasury-bonds]]"]
---

# Compounding OpenDollar

**Compounding OpenDollar (cUSDO)** is a **yield-bearing, T-bill-backed dollar [[stablecoin|stablecoin]]** issued by OpenEden Digital ("OED"), a Bermuda Monetary Authority ("BMA")-licensed digital-asset issuer. It is the compounding wrapper of OpenEden's USDO: backing is held in high-quality, liquid reserves — primarily short-dated [[treasury-bonds|U.S. Treasury bills]] and reverse repurchase agreements — and the yield those reserves earn is rolled (compounded) into the token, making cUSDO a [[real-world-assets|real-world-asset (RWA)]] dollar.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* cUSDO trades at **$1.05** (rank **#870**, market cap **$18,106,772**, 24h **+0.32%**, 7d **+0.04%**). The price **above $1.00 is by design, not a [[depeg]]**: as the underlying T-bill reserves accrue interest, that yield is **compounded into cUSDO's unit value**, so each token is worth progressively more than $1.00. The $1.05 quote therefore reflects accrued T-bill yield, and the tiny 24h/7d moves are consistent with steady, low-volatility yield accrual.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | CUSDO |
| **Market Cap Rank** | #870 |
| **Market Cap** | $18,106,772 |
| **Current Price** | $1.05 |
| **Value Model** | Yield-compounding (price > $1.00 by design) |
| **Categories** | BNB Chain Ecosystem, Ethereum Ecosystem, Real World Assets (RWA), Base Ecosystem |
| **Website** | [https://openeden.com](https://openeden.com) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

The OpenEden Compounding Open Dollar ("cUSDO") is a yield-bearing stablecoin issued by OpenEden Digital ("OED"), a Bermuda Monetary Authority ("BMA")-licensed digital-asset issuer. cUSDO is backed by high-quality, liquid reserves, primarily consisting of [[treasury-bonds|U.S. Treasury bills]] and reverse repurchase agreements. It is deployed across [[ethereum|Ethereum]], BNB Chain and Base.

### Value-accrual mechanism (why cUSDO trades above $1)
cUSDO is the **compounding** form of OpenEden's USDO. Rather than paying interest out or rebasing the holder's balance, the yield earned on the T-bill / repo reserves is **reinvested into each token's unit value**, so the price climbs steadily above $1.00 as interest compounds. The current **$1.05** quote represents the accrued, compounded T-bill yield captured since issuance — it is *value accrual by design, not a de-peg*. This places cUSDO in the appreciating-unit-value class of [[yield-bearing-stablecoin|yield-bearing stablecoins]], alongside tokens like Piku's [[usp-yield-optimized-stablecoin|USP]], and makes it a tokenized-Treasury [[real-world-assets|RWA]] instrument comparable to other on-chain T-bill products (e.g., [[ondo-finance|Ondo]] tokenized dollar tokens).

### Architecture deep-dive — USDO vs cUSDO, reserves & regulatory wrapper

OpenEden runs a **two-token design** around the same reserve pool:

- **USDO** — the base unit, intended to track $1.00. It is the "spendable" form.
- **cUSDO** — the **compounding** wrapper. Holding cUSDO is economically equivalent to holding USDO plus a continuously reinvested claim on the reserve's interest. The exchange rate of cUSDO→USDO rises over time, which is why cUSDO's market price sits above $1.00 (≈$1.05) and climbs as T-bill interest compounds. A holder can move between the two: wrap USDO into cUSDO to start compounding, unwrap to stop.

**Reserve model.** Backing is high-quality, liquid, short-duration: primarily short-dated **US Treasury bills** and **reverse repurchase agreements** collateralized by Treasuries. This is the same low-risk carry archetype as a tokenized money-market fund — there is no crypto collateral, no leverage, and no delta-neutral basis trade. Yield is the reserve's T-bill/repo interest net of issuer fees.

**Regulatory wrapper.** OpenEden Digital ("OED") is licensed by the **Bermuda Monetary Authority (BMA)**, issuing cUSDO/USDO as a regulated digital-asset instrument. The BMA wrapper is the credibility anchor versus unregulated yield dollars: it implies defined reserve, attestation and redemption obligations. Mint/redeem is permissioned through OED's issuance flow with KYC/minimums typical of regulated RWA issuers.

**Multi-chain.** Deployed on [[ethereum|Ethereum]], BNB Chain and [[base|Base]] (see Contract Addresses), letting cUSDO compose into DeFi venues across those ecosystems while the reserve stays in regulated off-chain custody.

### Mint / redeem
cUSDO is minted and redeemed against USDO through OpenEden's issuance flow; redemption ultimately settles against the underlying short-duration Treasury and repo reserves, subject to the issuer's redemption windows and any minimums/KYC requirements typical of regulated RWA issuers.

### Comparison vs. peer T-bill / yield dollars

| Dimension | **cUSDO** | [[ondo-finance\|OUSG/USDY]] | [[sygnum-fiusd-liquidity-fund\|FIUSD]] | sDAI |
|---|---|---|---|---|
| **Backing** | US T-bills + reverse repo | US Treasuries / bank deposits | Fidelity money-market fund units | DAI in the DSR |
| **Issuer / wrapper** | OpenEden Digital (BMA) | Ondo Finance | Sygnum Bank (FINMA/MAS) | MakerDAO / Sky |
| **Yield distribution** | Compounding into unit value | Accruing (USDY) / rebasing | Accumulating NAV | Savings-rate accrual |
| **Unit price** | ~$1.05 | ~$1.0x (USDY) | ~$11,921 (fund denomination) | ~$1.0x |
| **Access** | Permissioned issuance, KYC | Permissioned (tiers) | Permissioned, institutional | Permissionless |
| **Chains** | Ethereum, BNB, Base | Multi-chain | zkSync, Arbitrum | Ethereum + bridges |

cUSDO competes most directly with Ondo's USDY/OUSG and other tokenized-Treasury dollars; its differentiators are the **BMA regulatory wrapper**, the **compounding** (rather than rebasing) distribution, and multi-chain reach. All of these instruments ultimately earn the same short-Treasury carry, so they compete on wrapper, redemption mechanics, chain coverage and fee drag.

### Narrative, category & catalysts

cUSDO sits at the center of the **tokenized US Treasury / yield-bearing stablecoin** narrative — the most TradFi-validated crypto theme.

- **Rates:** cUSDO's appreciation is a direct function of short-term US rates; a Fed cutting cycle compresses the yield it compounds. Conversely, higher-for-longer keeps the carry attractive.
- **Risk-off flight-to-yield:** as of 2026-06-23 crypto is in **Extreme Fear** (Fear & Greed 21, market-health 29/100, bottoming/accumulation regime, [[bitcoin|BTC]] ≈ $64,568). Capital de-risking from volatile tokens into regulated, yield-bearing dollars is a structural tailwind for cUSDO's category even in a bear tape — aggregate stablecoin supply is the key "capital entering crypto" proxy.
- **Regulatory tailwind:** clearer tokenized-securities and stablecoin frameworks favour fully-reserved, licensed issuers like OED over algorithmic designs.

### History & timeline

| Date | Event |
|---|---|
| 2025-07-17 | All-time low unit price of $0.8955 (early/illiquid print) |
| 2025-08-17 | All-time high unit price of $1.09 |
| 2026-04-09 | Captured in CoinGecko top-1000 listing snapshot (Source: [[coingecko-top-1000-2026-04-09]]) |
| 2026-06-22 | Market snapshot: $1.05, ~$18.11M cap, rank #870 |

> The $0.8955 ATL is an early illiquid print, not a reserve impairment — cUSDO's value tracks accrued T-bill yield. Only verifiable price/listing events are recorded; issuance milestones will be added as primary OpenEden sources are ingested.

### How & where it's used / Usage playbook

- **Yield-bearing cash.** cUSDO's natural use is a buy-and-hold on-chain savings dollar: hold it and the unit value compounds with T-bill interest, no claiming or restaking required.
- **DeFi collateral / composability.** Across Ethereum, BNB and Base, cUSDO can be supplied as collateral or LP'd; its RWA backing and BMA wrapper make it relatively attractive collateral, though secondary depth (~$205K daily volume on ~$18M cap) is modest.
- **Playbook:** treat as a low-volatility yield allocation. Watch the **Fed path** (yield compresses if rates fall), **OED issuer/regulatory standing**, and **redemption windows** (primary redemption may not be instant; forced secondary exits can trade below accrued value). Prefer primary redemption for size.

### Risks
- **Yield-source / rate risk** — accrual depends on prevailing short-term US rates; falling rates slow appreciation.
- **Off-chain / RWA custody risk** — backing is off-chain Treasuries and repo; custody, settlement and counterparty failures could impair reserves (see [[real-world-assets]]).
- **Redemption-gating risk** — redemptions depend on the issuer's windows and reserve liquidity; primary redemption may not be instant, and forced secondary-market exits can trade below accrued value.
- **Regulatory / issuer risk** — OED operates under a BMA licence; regulatory change or issuer distress is a live risk.
- **[[depeg]] (downside) risk** — although the price floats upward with yield, a reserve impairment or confidence shock could push cUSDO below its accrued value; "compounding" does not guarantee the floor.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 28.28M CUSDO |
| **Total Supply** | 28.28M CUSDO |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $29.56M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.09 (2025-08-17) |
| **Current vs ATH** | -3.71% |
| **All-Time Low** | $0.8955 (2025-07-17) |
| **Current vs ATL** | +16.72% |
| **24h Change** | +0.32% |
| **7d Change** | +0.04% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xad55aebc9b8c03fc43cd9f62260391c13c23e7c0` |
| Binance Smart Chain | `0x64748ea3e31d0b7916f0ff91b017b9f404ded8ef` |
| Base | `0x83db73ef5192de4b6a4c92bd0141ba1a0dc87c65` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://openeden.com](https://openeden.com) |
| **Twitter** | [@OpenEden_Labs](https://twitter.com/OpenEden_Labs) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $204,652.00 |
| **Market Cap Rank** | #856 |
| **24h Range** | $1.04 — $1.05 |
| **Last Updated** | 2026-04-09 |

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
- [[stablecoins]]
- [[yield-bearing-stablecoin]]
- [[real-world-assets]]
- [[treasury-bonds]]
- [[ondo-finance]] — peer tokenized-Treasury issuer
- [[usp-yield-optimized-stablecoin]] — peer yield-bearing dollar
- [[sygnum-fiusd-liquidity-fund]] — peer tokenized money-market dollar
- [[base]]
- [[depeg]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge and OpenEden / OpenEden Digital public documentation; market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.
