---
title: "Brazilian Digital"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, forex, stablecoin]
aliases: ["BRZ"]
entity_type: protocol
headquarters: "Brazil / Switzerland (Transfero Group)"
website: "https://transfero.com/stablecoins/brz/"
related: ["[[brazilian-real]]", "[[brla-digital-brla]]", "[[crown-brlv]]", "[[crypto-markets]]", "[[depeg]]", "[[ethereum]]", "[[forex]]", "[[stablecoin]]"]
---

# Brazilian Digital

**Brazilian Digital** (BRZ) is a fiat-backed [[stablecoin]] that tracks the **[[brazilian-real|Brazilian real]] (BRL)**, not the US dollar. Issued by the **Transfero Group**, BRZ lets users hold, move, and trade the Brazilian currency on-chain across many blockchains, and is one of the longest-standing and most widely distributed BRL stablecoins. It is the BRL counterpart to dollar coins like [[usdt]] / [[usdc]] and competes directly with [[brla-digital-brla|BRLA]] and [[crown-brlv|Crown BRLV]] inside the Brazilian on-chain economy.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

## Why the ~$0.19 USD price is the peg, not a depeg

BRZ is pegged to **one Brazilian real**, and one real is currently worth roughly **0.19 US dollars** on the [[forex]] market (i.e., about 5.2 reais per dollar). A USD-denominated quote of **$0.193839** for BRZ therefore reflects the BRL/USD exchange rate and means the peg is **holding correctly** — it is **not** a depegged dollar stablecoin. To assess whether BRZ is on-peg, measure it against **BRL**, where it should trade at ~1.00 real. This is the same FX framing that applies to [[brla-digital-brla]] and [[crown-brlv]] (the other BRL stablecoins) and to [[frankencoin]] for the Swiss franc. A genuine BRZ depeg would appear as a gap between BRZ's price and the prevailing BRL/USD rate, not as the price sitting below $1.00.

## Market Snapshot (2026-06-21)

| Field | Value |
|---|---|
| **Ticker** | BRZ |
| **Price (USD)** | $0.193839 (≈ 1.00 BRL — on peg) |
| **Market Cap Rank** | #443 |
| **Market Cap** | $51,615,164 |
| **24h Change** | +0.19% |
| **7d Change** | -1.60% |
| **Currency tracked** | Brazilian real (BRL) |

The 24h/7d changes in USD terms (+0.19% / -1.60%) largely track the BRL/USD exchange rate rather than any movement away from the real peg.

## Issuer & Jurisdiction

BRZ is issued by the **Transfero Group**, a financial-services company with operations spanning **Brazil and Switzerland**. Transfero positions BRZ as a fully-backed real stablecoin, with backing held in reserves and redeemable for fiat reais inside Brazil. Operating across both a Brazilian operational base and a Swiss corporate footprint lets Transfero pair domestic BRL banking and ramp infrastructure (including the [[pix|Pix]] instant-payment system) with a European regulatory/corporate wrapper. The token has been issued and bridged across many chains over its lifetime, including [[ethereum]], BNB Chain, Solana, Polygon, Avalanche, Algorand, Stellar, and Rootstock — a multi-chain footprint that maximises composability but also spreads bridge surface area.

## Architecture — How It Works

### Reserve & collateral model
BRZ is a **fiat-collateralised** stablecoin: each token is intended to be backed by an equivalent value of Brazilian reais held as cash and cash-equivalent reserves. This is the simplest of the three major reserve models — distinct from the **sovereign-bond-backed** design of [[crown-brlv|Crown BRLV]] (reserves in Brazilian government bonds via the BRLY collateral layer) and the **reais-in-reserve-managed-by-Avenia** structure of [[brla-digital-brla|BRLA]]. Reserve transparency and the cadence/quality of attestations are the central trust question for a BRL fiat coin, just as they are for dollar coins.

### Peg & redemption mechanism
The peg is maintained by **primary issuance and redemption at par against BRL reserves**, plus secondary-market arbitrage. When BRZ trades above one real on-chain, arbitrageurs mint new BRZ at par and sell; when it trades below, they buy and redeem. The peg therefore depends on (a) reserves actually being there and (b) the redemption channel staying open.

### Mint / redeem, KYC gating, on/off-ramp rails
- **Mint:** Users acquire BRZ at par, historically described as purchasing for ~1 BRL per token through Transfero's on/off-ramp after KYC onboarding.
- **Redeem:** Holders can redeem BRZ for reais in Brazil; historically a redemption fee/discount (on the order of ~1%) has applied. Redemption availability depends on KYC and Transfero's compliance processes.
- **Rails:** On-ramp/off-ramp into the Brazilian banking system (and Pix) is the core utility — convert reais to on-chain BRZ, move it 24/7 across chains, and convert back.

## Tokenomics & Supply

BRZ is a centrally issued, supply-elastic token: supply expands when reais are deposited and minted, and contracts on redemption, so circulating supply tracks demand for on-chain BRL rather than a fixed schedule. There is no fixed max supply and no native yield — holders are long the real, not earning a coupon. At the snapshot, market cap was ~$51.6M (the dollar value of all reais represented on-chain at the prevailing FX rate).

## Comparison vs Other BRL Stablecoins

| | **BRZ** | **[[brla-digital-brla\|BRLA]]** | **[[crown-brlv\|Crown BRLV]]** | **USDT/USDC (for contrast)** |
|---|---|---|---|---|
| **Peg** | Brazilian real (BRL) | Brazilian real (BRL) | Brazilian real (BRL) | US dollar |
| **Issuer** | Transfero Group (Brazil/Switzerland) | BRLA Digital (Brazil) | Crown (São Paulo) | Tether / Circle |
| **Reserve model** | BRL cash reserves | BRL reserves (managed by Avenia) | Brazilian government bonds (BRLY layer) | USD cash + T-bills |
| **Primary chain(s)** | Multi-chain (ETH, BNB, SOL, Polygon, +) | Polygon (+ Celo, Gnosis, Base, ETH) | Base (+ Ethereum) | Multi-chain |
| **Focus** | Broad retail/trading distribution, longevity | B2B cross-border, audited, Pix-native | Institutional treasury, bankruptcy-remote, yield at collateral layer | Global USD settlement |
| **Mkt cap (snapshot)** | ~$51.6M | ~$40.8M | ~$71.7M | tens of billions |

BRZ's edge is its **age, multi-chain breadth, and exchange distribution**; BRLA's is **B2B compliance**; BRLV's is **sovereign-bond backing with a legally segregated, bankruptcy-remote reserve**.

## How & Where It Trades / Is Used

- **Trading:** BRZ has historically had the widest exchange and DEX distribution of the BRL stablecoins, listed on Brazilian and international venues and present as a quote/settlement asset for BRL pairs.
- **Payment corridors:** Cross-border BRL transfers and remittances into/out of Brazil, where moving value on-chain and settling via Pix can be faster and cheaper than correspondent banking.
- **DeFi composability:** As a standard fungible token across [[ethereum]] and other EVM chains, BRZ can be used in DEX pools, lending, and as on-chain BRL exposure — though depth for a ~$52M-cap regional coin is far below dollar majors.
- **Trading vs holding:** For a USD-based participant, holding BRZ is a way to be **long the real** on-chain without an FX broker.

## Narrative, Category & Catalysts

BRZ sits in the **regional / FX-denominated stablecoin** category. Catalysts that drive BRL stablecoin demand include: Brazil's large and crypto-active retail base; the maturation of **Pix** rails enabling instant fiat on/off-ramps; remittance and B2B cross-border flows; and the Brazilian central bank's **Drex** (digital real / CBDC) programme and evolving stablecoin rules, which could either legitimise or constrain private BRL coins. The broader 2026 backdrop — Extreme Fear (Fear & Greed 21), a bearish, bottoming/accumulation regime — tends to compress liquidity for small regional stablecoins even when their pegs are unaffected.

## History / Timeline

- BRZ is one of the **longest-standing BRL stablecoins**, issued and bridged across an expanding set of chains over its multi-year lifetime by the Transfero Group.

*(Specific dated launch/listing events are not verified in available wiki sources and are deliberately not stated here to avoid fabrication.)*

## Risks

- **FX risk for USD holders:** A USD-based holder of BRZ is implicitly **long the Brazilian real** and exposed to BRL/USD [[forex]] volatility, which can be substantial for an emerging-market currency.
- **Issuer / reserve-counterparty risk:** As a centrally issued fiat-backed coin, holders rely on Transfero actually holding sufficient reserves and on its banking counterparties; reserve-attestation transparency is the key consideration.
- **Regulatory risk:** Brazilian (Drex/central-bank stablecoin rules) and international stablecoin regulation is evolving and could affect issuance or redemption.
- **Redemption-gating risk:** Par redemption depends on KYC clearance and the off-ramp staying open; a freeze would break the arbitrage that holds the peg.
- **Liquidity / depeg risk:** With ~$52M market cap and modest 24h volume, large trades can push BRZ away from peg on-chain ([[depeg]] risk).
- **Multi-chain bridge risk:** BRZ exists on many chains; a bridge or contract vulnerability on any single chain could affect that chain's supply.

## Trading / Usage Playbook

- **As FX exposure:** Buy/hold BRZ to express a **long-BRL** view on-chain; remember the USD P&L is dominated by BRL/USD, not by the (tight) peg.
- **On/off-ramp use:** Use BRZ to move BRL value 24/7 across chains and settle into Brazilian banking via Pix; budget for the ~1% redemption discount and KYC.
- **Peg monitoring:** Judge "on-peg" against **BRL (~1.00 real)**, not against $1.00. Watch for a price gap vs the live BRL/USD rate as the true depeg signal.
- **Sizing:** Treat as a thin, regional market — size to on-chain/venue depth, not headline market cap.

## See Also

- [[stablecoin]]
- [[brazilian-real]]
- [[forex]]
- [[brla-digital-brla]]
- [[crown-brlv]]
- [[pix]]
- [[crypto-markets]]
- [[ethereum]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | BRZ |
| **Market Cap Rank** | #419 |
| **Market Cap** | $52.03M |
| **Current Price** | $0.1943 |
| **Hashing Algorithm** | Ethash |
| **Categories** | Stablecoins, Decentralized Finance (DeFi), Fiat-backed Stablecoin |
| **Website** | [https://transfero.com/stablecoins/brz/](https://transfero.com/stablecoins/brz/) |

---

## Overview

BRZ is the first stable coin backed by Brazilian Reais (BRL). It'll allow Brazilian residents to directly ramp up in international exchanges and actively trade the Brazilian currency against pairs of different classes, including Bitcoin, other stable coins, utility and security tokens. It will be a powerful tool that will allow Brazilians to move and hedge Brazilians reais internationally. BRZ is always fully backed and holders can either purchase it for 1BRL or redeem it with a discount of 1% in Brazil.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 266.27M BRZ |
| **Total Supply** | 266.27M BRZ |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $52.03M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $9.99 (2023-10-29) |
| **Current vs ATH** | -98.04% |
| **All-Time Low** | $0.00196567 (2026-03-07) |
| **Current vs ATL** | +9840.27% |
| **24h Change** | -0.11% |
| **7d Change** | +0.47% |
| **30d Change** | -1.57% |
| **1y Change** | +8.43% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x01d33fd36ec67c6ada32cf36b31e88ee190b1839` |
| Algorand | `112866019` |
| Rootstock | `0xe355c280131dfaf18bf1c3648aee3c396db6b5fd` |
| Solana | `BRZbFNQDcWLfcdHmAkqEVnLHCAWKTRf6eHyEaWdZp3JN` |
| Polygon Pos | `0x4ed141110f6eeeaba9a1df36d8c26f684d2475dc` |
| Binance Smart Chain | `0x71be881e9c5d4465b3fff61e89c6f3651e69b5bb` |
| Avalanche | `0x491a4eb4f1fc3bff8e1d2fc856a6a46663ad556f` |
| Stellar | `BRZ-GABMA6FPH3OJXNTGWO7PROF7I5WPQUZOB4BLTBTP4FK6QV7HWISLIEO2` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://transfero.com/stablecoins/brz/](https://transfero.com/stablecoins/brz/) |
| **Twitter** | [@BrzToken](https://twitter.com/BrzToken) |
| **Telegram** | [brztoken](https://t.me/brztoken) (283 members) |
| **GitHub** | [https://github.com/TransferoSwiss](https://github.com/TransferoSwiss) |
| **Whitepaper** | [https://drive.google.com/drive/folders/1p5IJH9xi0NOFHam42rFN59-XL0JvHg4t](https://drive.google.com/drive/folders/1p5IJH9xi0NOFHam42rFN59-XL0JvHg4t) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $34,027.00 |
| **Market Cap Rank** | #419 |
| **24h Range** | $0.1941 — $0.1957 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
