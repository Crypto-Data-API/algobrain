---
title: "Bitcoin ETFs"
type: concept
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [crypto, bitcoin, etf, institutional, tradfi, options]
aliases: ["bitcoin-etf", "btc-etf", "spot-bitcoin-etf", "BTC-ETF", "Bitcoin ETF", "Spot Bitcoin ETF", "crypto-etf", "spot-crypto-etf"]
domain: [crypto]
difficulty: beginner
related: ["[[bitcoin]]", "[[ethereum]]", "[[solana]]", "[[crypto-markets]]", "[[coinbase]]", "[[blackrock]]", "[[options]]", "[[etf-arbitrage]]", "[[basis-trading]]", "[[deribit]]", "[[index-inclusion-effect]]"]
---

# Bitcoin ETFs

**Bitcoin Exchange Traded Funds (ETFs)** are regulated investment vehicles that track the price of [[bitcoin|BTC]] and trade on traditional stock exchanges, allowing investors to gain Bitcoin exposure through conventional brokerage accounts without directly holding or custodying the underlying asset. The approval of **spot Bitcoin ETFs** by the U.S. SEC in **January 2024** was a watershed moment for institutional crypto adoption. This page is the **reference hub** for the spot crypto ETF complex — Bitcoin, [[#Ethereum ETFs|Ethereum]], and the emerging [[#The Wider Spot Crypto ETF Landscape|Solana/altcoin]] products.

### Spot vs. Futures vs. Trust — Why "Spot" Mattered

| Wrapper | What It Holds | Tracking | Problem It Had |
|---|---|---|---|
| **Spot ETF** (2024+) | Actual BTC in custody | Tight to NAV via create/redeem | None material — the breakthrough structure |
| **Futures ETF** (BITO, 2021) | CME BTC futures | Decays from roll cost ("contango bleed") | Underperforms spot in upward-sloping curves |
| **Closed-end trust** (GBTC pre-2024) | BTC, no redemption | Persistent premium/discount | Traded at up to ~50% discount to NAV in 2022 |

The spot ETF's **in-kind/cash create-redeem** arbitrage is what keeps price glued to NAV — the single most important structural improvement over the trust era.

---

## Key Spot Bitcoin ETFs

| Ticker | Issuer | Custodian | Notes |
|---|---|---|---|
| **IBIT** | BlackRock (iShares) | [[coinbase|Coinbase]] | Largest by AUM; fastest ETF to reach $10B in history |
| **FBTC** | Fidelity | Fidelity Digital Assets | Self-custodied |
| **ARKB** | ARK Invest / 21Shares | [[coinbase|Coinbase]] | ARK's flagship crypto product |
| **BITB** | Bitwise | Coinbase | Transparent on-chain proof of reserves |
| **GBTC** | Grayscale | Coinbase | Converted from closed-end trust; higher fee structure |

---

## How They Work

Spot Bitcoin ETFs hold actual BTC in custody (unlike earlier futures-based ETFs). Authorized participants create/redeem shares by delivering BTC to the fund's custodian, keeping the ETF's market price closely aligned with Bitcoin's spot price. This mechanism eliminates the persistent premium/discount that plagued Grayscale's GBTC trust structure.

---

## Market State (2025-2026)

By 2026 the spot Bitcoin ETF complex had become a permanent institutional fixture:

- **Total spot Bitcoin ETF AUM** ranged roughly **$100B-$130B in 2026** (briefly dipping below $100B during a February 2026 outflow episode, and reported as high as ~$128B in Q1 2026), depending on date and data vendor
- **IBIT (BlackRock)** remained the dominant fund, holding around **60% of all BTC owned by US spot ETFs**; the full ETF complex held roughly **1.26 million BTC** as of late February 2026. IBIT is the largest crypto ETF and one of the largest ETFs in the world by AUM, though not the single largest ETF globally
- The combined Bitcoin + gold ETF complex crossed ~$500B in August 2025
- **New spot crypto ETFs**: there are unconfirmed secondary reports of the first spot **Solana** ETFs receiving SEC approval around February 2026 and of capital rotation into Solana/XRP ETF products. These could not be confirmed from a primary SEC source as of 2026-06-11 — treat as unverified

(Sources: gitnux, bitcoingate, blockeden, bestbrokers. Verified via Perplexity (sonar), 2026-06-11)

## Market Impact

- ETFs attracted **tens of billions** in net inflows within their first year, representing significant new demand from institutional and retail TradFi investors
- Daily ETF flow data (available from Bloomberg, SoSoValue) has become a **leading indicator** for short-term BTC price direction
- [[coinbase|Coinbase]] serves as custodian for most major ETFs, making it systemically important infrastructure
- ETF approval opened Bitcoin to 401(k) plans, RIAs, and institutional mandates previously restricted from direct crypto exposure

---

## Issuer Landscape

| Issuer | Flagship BTC ETF | Distinguishing Feature |
|---|---|---|
| **[[blackrock\|BlackRock (iShares)]]** | IBIT | Dominant by AUM; deepest options market; institutional distribution |
| **Fidelity** | FBTC | Self-custodies BTC (no third-party custodian risk) |
| **ARK / 21Shares** | ARKB | Active-manager brand; among the cheapest fees |
| **Bitwise** | BITB | Crypto-native; on-chain proof of reserves |
| **VanEck** | HODL | Donates a share of profits to Bitcoin Core developers |
| **Grayscale** | GBTC + BTC (Mini) | Legacy trust converted to ETF; high-fee GBTC vs low-fee Mini |

[[coinbase|Coinbase]] is the custodian behind the majority of these funds, which makes it **systemically important infrastructure** for the entire US spot ETF complex — a single point of operational concentration worth monitoring.

## Trading Relevance

- ETF inflows/outflows are now among the most closely watched BTC trading signals
- Basis trades (spot BTC vs ETF shares vs futures) create [[arbitrage]] opportunities — see [[basis-trading]]
- ETF volumes on traditional exchanges add significant liquidity during US market hours
- Correlation between BTC and equities may increase as overlapping investor bases grow

## Key Metrics Traders Watch

| Metric | What It Tells You | Source |
|---|---|---|
| **Daily net flow** | Aggregate ETF buying/selling pressure — a leading short-term BTC direction signal | SoSoValue, Bloomberg |
| **IBIT share of complex** | Concentration; IBIT alone holds the majority of US ETF BTC | Issuer disclosures |
| **Total BTC held by ETFs** | Supply locked in regulated wrappers (~1.26M BTC reported late Feb 2026) | Issuer filings, on-chain |
| **Premium/discount to NAV** | Create-redeem arbitrage health; large gaps signal stress or illiquidity | Issuer NAV vs market price |
| **CME futures basis** | The annualised premium that drives the cash-and-carry [[basis-trading\|basis trade]] | CME, exchange data |
| **IBIT options IV vs Deribit** | Cross-market vol dislocation between regulated and crypto-native venues | OCC, [[deribit]] |

## Fee Comparison

| ETF | Expense Ratio | Notes |
|-----|---------------|-------|
| **IBIT** (BlackRock) | 0.25% (0.12% waived intro) | Fee waiver applied to first $5B or 12 months |
| **FBTC** (Fidelity) | 0.25% | Self-custody — no third-party custodian risk |
| **ARKB** (ARK/21Shares) | 0.21% | Among the cheapest |
| **BITB** (Bitwise) | 0.20% | Lowest fee; on-chain proof of reserves |
| **HODL** (VanEck) | 0.20% | Donates 5% of profits to Bitcoin Core devs |
| **GBTC** (Grayscale) | 1.50% | Highest fee — legacy from trust conversion. Investors have migrated to cheaper alternatives |
| **BTC** (Grayscale Mini) | 0.15% | Grayscale's low-cost alternative to GBTC |

The fee war has compressed expense ratios to 0.15-0.25% for most issuers. GBTC's persistent 1.50% fee has caused massive outflows — billions moved to IBIT, FBTC, and cheaper alternatives.

## Options on Bitcoin ETFs

The SEC approved options trading on **IBIT** in late 2024, creating the first regulated Bitcoin options market accessible through standard equity brokerages:

- IBIT options provide a regulated way to trade BTC [[volatility]] — previously only available on [[deribit]] (offshore) or CME Bitcoin futures options
- Covered call strategies on IBIT allow generating yield on Bitcoin holdings
- IBIT options implied volatility tracks but diverges from the crypto-native vol surface on Deribit, creating cross-market arbitrage opportunities
- Options approval was a significant step toward BTC's integration into traditional portfolio construction — pension funds and RIAs can now use options to define risk on Bitcoin positions

## Ethereum ETFs

Following the success of spot Bitcoin ETFs, the SEC approved **spot Ethereum ETFs** in May 2024, with trading beginning in July 2024:

| ETF | Issuer | Notes |
|-----|--------|-------|
| **ETHA** | [[blackrock\|BlackRock]] | Largest by AUM |
| **FETH** | Fidelity | Self-custodied |
| **ETHE** | Grayscale | Converted from trust; high fee like GBTC |
| **ETH** | Grayscale (Mini) | Low-cost successor to ETHE |

Ethereum ETF inflows have been significantly smaller than Bitcoin's, reflecting both lower institutional demand for ETH and the complexity of explaining Ethereum's value proposition to TradFi allocators. The lack of staking yield (ETFs initially could not stake ETH under SEC guidance) reduces the appeal compared to holding ETH natively — though **staked-ETH ETF structures** that pass [[staking]] yield to shareholders became a major point of issuer applications and regulatory debate through 2025-2026. A staking-enabled ETH ETF would materially change the relative-value calculus versus holding ETH directly.

## The Wider Spot Crypto ETF Landscape

After Bitcoin and Ethereum, the ETF wrapper began extending to other large-cap assets. Treat specific approval dates and tickers below as **directionally accurate but date-sensitive** — confirm against a primary SEC source before trading on them.

| Asset | Status (as reported) | Notes |
|---|---|---|
| **Bitcoin** | Live since Jan 2024 | The mature, deep complex |
| **Ethereum** | Live since Jul 2024 | Smaller flows; staking-yield variants pending/emerging |
| **Solana** ([[solana]]) | Spot SOL ETFs reportedly approved ~early 2026 | Secondary reports of capital rotation into SOL products — **unverified vs primary SEC source** |
| **XRP** | Reported product activity 2026 | Same caveat — treat as unconfirmed |
| **Multi-asset / index** | Emerging | Basket products tracking a crypto index rather than a single coin |

The structural pattern repeats with each new asset: a **futures ETF** or **closed-end trust** usually precedes the spot product, and the spot launch tends to compress the trust's discount and tighten the futures basis. The same flow-as-signal and basis-trade dynamics described below apply to each new spot product as it lists.

(Solana/XRP ETF status carried over from earlier verification: unconfirmed from a primary SEC source as of 2026-06-11 — treat as unverified.)

## The Basis Trade

The existence of spot BTC ETFs, CME Bitcoin futures, and the underlying spot market creates a multi-legged arbitrage complex:

- **Cash-and-carry basis**: buy IBIT (spot), short CME BTC futures. Earns the futures premium (~5-15% annualized) with minimal directional risk
- **ETF vs. spot arb**: authorized participants exploit deviations between ETF price and NAV through creation/redemption. See [[etf-arbitrage]]
- **Cross-venue**: IBIT price during US hours vs. BTC spot on crypto exchanges during non-US hours creates overnight basis opportunities

The basis trade has attracted significant capital from macro hedge funds and arb desks, contributing to the tightening of the BTC futures premium since ETF approval.

---

## See Also

- [[bitcoin]] — the underlying asset
- [[ethereum]] — second spot crypto ETF complex
- [[solana]] — emerging spot ETF asset
- [[crypto-markets]] — broader cryptocurrency market context
- [[coinbase]] — primary custodian for spot Bitcoin ETFs
- [[blackrock]] — IBIT/ETHA issuer; dominant by AUM
- [[options]] — IBIT options as a regulated BTC vol instrument
- [[basis-trading]] — cash-and-carry mechanics across spot/futures/ETF
- [[etf-arbitrage]] — creation/redemption mechanics
- [[deribit]] — crypto-native options venue for IV comparison
- [[staking]] — relevant to staked-ETH ETF structures

## Sources

- [SoSoValue — Bitcoin ETF flows](https://sosovalue.com/) — daily spot Bitcoin ETF flow and AUM data
- [Blockeden — Bitcoin ETF AUM / institutional permanence (2026)](https://blockeden.xyz/blog/2026/04/28/bitcoin-etf-150b-aum-60-40-portfolio-institutional-permanence/)
- 2025-2026 AUM and holdings figures verified via Perplexity (sonar), 2026-06-11
