---
title: "Eurite"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["EURI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.eurite.com/"
related: ["[[crypto-markets]]", "[[stablecoins]]", "[[euro-coin]]", "[[societe-generale-forge-eurcv]]", "[[bnb]]", "[[ethereum]]"]
---

# Eurite

**Eurite (EURI)** is a **Euro (EUR) [[stablecoins|stablecoin]]** deployed natively on the [[bnb|BNB Chain]] and on [[ethereum|Ethereum]]. It targets a 1:1 peg to the euro and is marketed as a MiCA-compliant, fiat-backed stablecoin. As of the latest snapshot it ranks **#412** by market capitalization. It is a euro-denominated peer to [[euro-coin|EURC]] and the bank-issued [[societe-generale-forge-eurcv|EURCV]], and is most notable for its **Binance listing** and BNB-ecosystem distribution.

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko). Note: EURI pegs to the euro, not the US Dollar — its USD price reflects the EUR/USD FX rate (1 EUR ≈ $1.15), so a quote near $1.15 is the token holding its peg, not a de-peg or premium.*

| Field | Detail |
|---|---|
| **Ticker** | EURI |
| **Peg target** | Euro (1 EURI ≈ €1.00) |
| **Issuer / chain** | Eurite — BNB Chain (also Ethereum) |
| **Current price** | $1.15 (= ~€1.00 at prevailing EUR/USD FX) |
| **Market cap** | $56.86M |
| **Market cap rank** | #412 |
| **24h volume** | $5.28M |
| **Circulating supply** | 49.62M EURI |
| **Total supply** | 49.62M EURI |
| **24h change** | -0.02% |
| **7d change** | -0.72% |
| **All-time high** | $1.21 (2026-01-27) |
| **All-time low** | $1.008 (2025-01-13) |

The USD quote of ~$1.15 is **the euro exchange rate, not a de-peg or premium** — one EURI is worth roughly one euro, which currently converts to about $1.15. The ATH/ATL band ($1.01–$1.21) tracks EUR/USD movement over time rather than peg instability.

---

## Architecture: Peg & Backing Mechanism

Eurite is a **fiat-collateralized (custodial) euro stablecoin** — the same conservative design family as [[euro-coin|EURC]] and [[societe-generale-forge-eurcv|EURCV]], distinct from DeFi/crypto-backed euro tokens like agEUR.

- **Backing:** each EURI is intended to be backed 1:1 by **euro-denominated reserves (cash and cash-equivalents)** held by the issuer in segregated accounts; there is no algorithmic or crypto-collateral component.
- **MiCA framing:** it is marketed as compliant with the EU's **Markets in Crypto-Assets (MiCA)** regulation, the framework that governs euro-referenced e-money / asset-referenced tokens in the EU. (The strength of any MiCA claim depends on the specific licensing and attestation the issuer maintains; transparency here is thinner than for bank-issued [[societe-generale-forge-eurcv|EURCV]].)
- **Mint / redeem & gating:** authorized participants mint EURI against euro deposits and redeem EURI 1:1 for euros through the issuer; the peg is maintained by this primary mint/redeem channel plus secondary-market arbitrage. Retail typically accesses EURI via exchanges (notably Binance) rather than direct redemption.
- **Attestation:** as a fiat-reserve token, peg integrity depends on the issuer holding adequate, liquid euro reserves and on the quality/frequency of reserve attestations — a key diligence point for holders.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 49.62M EURI |
| **Total Supply** | 49.62M EURI |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | 1.00 |

Supply is **fully reserve-backed and elastic** (circulating = total, market-cap/FDV = 1.00), expanding and contracting with euro deposits and redemptions. There is no fixed cap, no emissions schedule, and no seigniorage — the issuer earns yield on the euro reserve float, the standard fiat-stablecoin model.

---

## Comparison vs Euro Stablecoins

| Stablecoin | Issuer | Backing | Distribution | Note |
|---|---|---|---|---|
| **EURI** | Eurite | Euro cash-equivalents | BNB Chain + Binance | Best CEX access of small EUR coins |
| [[euro-coin\|EURC]] | Circle | Euro cash + short instruments | Multi-chain, deep | Largest EUR stablecoin |
| [[societe-generale-forge-eurcv\|EURCV]] | SG-FORGE (Société Générale) | Euro cash + HQLA, segregated | Multi-chain, institutional | Bank-issued; strongest regulatory wrapper |
| EURS (Stasis) | Stasis | Euro reserves | EU venues | One of the oldest euro stablecoins |
| agEUR (Angle) | Angle Protocol | Crypto/RWA (DeFi) | DeFi-native | Not fiat-custodial |

EURI's distinguishing trait is its **BNB-ecosystem and Binance distribution**, which gives it more visible CEX liquidity than most small euro coins; its weakness relative to [[euro-coin|EURC]]/[[societe-generale-forge-eurcv|EURCV]] is issuer scale and reserve-transparency pedigree.

---

## How & Where It Trades / Is Used

Eurite has more visible exchange presence than the other small stablecoins on this list — it is listed on **Binance** (EURI/USDT) and trades on the BNB Chain and Ethereum.

- **24h volume is moderate (~$5.3M)** — healthier than many small RWA/savings tokens but still small relative to flagship USD stablecoins.
- **Primary use case:** euro-denominated on/off ramp and EUR-pair trading within the BNB ecosystem; on-chain composability as a euro unit of account in BNB-Chain DeFi.
- **Liquidity caveat:** while better than peers here, depth is thin versus major stablecoins, so large trades can move the price.

---

## Platform & Chain Information

**Native Chain:** BNB Chain (also Ethereum)

### Contract Addresses

| Chain | Address |
|---|---|
| BNB Chain | `0x9d1a7a3191102e9f900faa10540837ba84dcbae7` |
| Ethereum | `0x9d1a7a3191102e9f900faa10540837ba84dcbae7` |

---

## Exchange Listings

| Exchange | Pair |
|---|---|
| Binance | EURI/USDT |

---

## Narrative, Category & Catalysts

EURI sits in the **regulated/marketed-compliant euro stablecoin** category, with a BNB-ecosystem distribution angle. Catalysts: MiCA-driven demand for compliant euro settlement, continued Binance/BNB-Chain support and listings, and broader growth of non-USD stablecoin rails. The dominant counter-trend is the overwhelming USD-stablecoin dominance (USDT ≈ $186B, USDC ≈ $74.8B) and the thinness of euro-stablecoin liquidity overall. In the current **Extreme Fear / bottoming-accumulation** regime (Fear & Greed 21), stablecoins broadly attract risk-off demand, but a small euro coin like EURI captures only a sliver of that flow.

---

## Risks

- **FX risk (holder, not peg flaw):** a USD-based holder is exposed to EUR/USD; the token holds its euro peg but its dollar value moves with the euro.
- **De-peg risk:** reserve shortfalls, redemption friction, or loss of confidence could move EURI off €1.00.
- **Collateral / reserve-counterparty risk:** peg depends on the issuer actually holding adequate, liquid euro reserves and honoring redemptions; reserve transparency/audit quality matters and is weaker here than for bank-issued peers.
- **Custodial / banking risk:** euro reserves sit with banks/custodians, exposing the peg to banking-sector stress (a key risk demonstrated by USDC's 2023 depeg during a banking failure).
- **Redemption-gating risk:** direct mint/redeem runs through the issuer's onboarded participants; retail exit at par depends on secondary (mostly Binance) liquidity.
- **Regulatory risk:** euro stablecoins are directly in scope of MiCA; non-compliance or rule changes could restrict issuance or distribution.
- **Liquidity risk:** while better than peers here, volume is still thin versus major stablecoins, so large trades can move the price.

---

## Trading Playbook

- **Read the peg in euros** — quote EURI against EUR (target €1.00); USD-chart swings are mostly EUR/USD.
- **FX exposure** — holding EURI in a USD book is implicitly long EUR/USD; hedge if unwanted.
- **Best access via Binance** — EURI/USDT is the primary liquid venue; size DEX trades to thinner on-chain pools.
- **Macro:** in a risk-off, bottoming regime, treat as a euro cash-equivalent rather than a return asset.

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.eurite.com/](https://www.eurite.com/) |
| **Twitter** | [@Eurite_BC](https://twitter.com/Eurite_BC) |

---

## Related

- [[stablecoins]]
- [[euro-coin]]
- [[societe-generale-forge-eurcv]]
- [[bnb]]
- [[ethereum]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge; no specific wiki source ingested yet.
