---
title: "Royal Euro"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, forex, stablecoin]
aliases: ["REUR", "Royal Euro Token"]
entity_type: protocol
headquarters: "Hong Kong (RIB Digital Holdings)"
website: "https://www.rcoins.digital/"
related: ["[[crypto-markets]]", "[[depeg]]", "[[ethereum]]", "[[euro]]", "[[forex]]", "[[royal-dollar]]", "[[stablecoins]]"]
---

# Royal Euro

**Royal Euro (REUR)** is a **EUR-referenced fiat-backed [[stablecoins|stablecoin]]** — a crypto-asset designed to track a 1:1 value with the [[euro|Euro (EUR)]], subject to reserve sufficiency, redemption terms and market conditions. It is issued by **The RIB Digital Holdings Limited (Hong Kong)** under the **RCOINS** brand and settles across multiple public blockchains. Because it is pegged to the euro rather than the dollar, its USD quote moves with the EUR/USD [[forex|FX]] rate. REUR is the euro sibling of [[royal-dollar|Royal Dollar (RUSD)]] within the same issuer family.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* REUR trades at **$1.15** (rank **#887**, market cap **$17,217,209**, 24h **-0.03%**, 7d **-1.15%**). The **~$1.15 USD price is the EUR-to-USD [[forex|FX]] peg, NOT a [[depeg]]**: at the time of snapshot roughly €1 ≈ US$1.15, so a euro-pegged token correctly prints around $1.15 in dollar terms while holding its 1:1 euro peg. The small 7d move tracks normal EUR/USD fluctuation, not peg instability.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | REUR |
| **Market Cap Rank** | #887 |
| **Market Cap** | $17,217,209 |
| **Current Price** | $1.15 |
| **Peg Target** | €1.00 (EUR); ~$1.15 USD via EUR/USD FX |
| **Categories** | Stablecoins, EUR Stablecoin, BNB Chain Ecosystem, Ethereum Ecosystem, Tron Ecosystem, Fiat-backed Stablecoin |
| **Website** | [https://www.rcoins.digital/](https://www.rcoins.digital/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Royal Euro Token (REUR) is a EUR-referenced stable-value token designed to target a 1:1 value with the [[euro|Euro (EUR)]], subject to reserve sufficiency, redemption terms and market conditions. REUR is issued by **The RIB Digital Holdings Limited, Hong Kong** (the "Issuer"), the licensed/regulated digital division of the **Royal Investment Bank Group (RIB GROUP)** within the broader **RCCG Group**, and is engineered for fast settlement across [[ethereum|Ethereum]], BNB Chain and Tron. RCOINS comprises three Royal Stablecoins — **RUSD (USD), REUR (EUR), and RXAU (gold)** — that share the same issuance, reserve, and settlement infrastructure (the hybrid **RxBridge** ecosystem). The design objective is to provide a bank-grade settlement instrument for payments, treasury operations, OTC trading and exchange liquidity, with transparency around reserves and circulating supply.

## Architecture — How It Works

### Reserve & collateral model
REUR is a **fiat-collateralised euro stablecoin**: reserves are intended to cover circulating supply 1:1 in euros, with the issuer publishing **proof-of-reserve** as part of the RCOINS model (the issuer markets tokens as fully — and in places over- — collateralised, with on-chain-verifiable reserves). As with any off-chain-reserve coin, peg confidence ultimately depends on the **quality, custody, and attestation cadence** of those euro reserves (see [[stablecoin-attestations]]).

### Regulatory wrapper & jurisdiction
The issuer is a **Hong Kong** entity (RIB Digital Holdings), so REUR sits under Hong Kong's evolving digital-asset/stablecoin regime rather than the EU's. A euro-denominated stablecoin distributed into the EU additionally faces **MiCA** considerations (MiCA imposes specific rules on euro-referenced e-money tokens), which is a distribution/eligibility factor for any EUR coin not issued under an EU authorisation.

### Peg mechanism (why REUR quotes near $1.15)
REUR's peg is to the **euro**, not the US dollar. It targets a fixed 1:1 ratio with EUR, so its **US-dollar price simply equals the EUR/USD exchange rate** — around **$1.15** on 2026-06-22 — and the dollar quote rises and falls with EUR/USD even while the euro peg holds firm. This makes REUR an [[forex|FX]]-exposed instrument from a USD investor's perspective: a stable euro and a *floating* dollar. A genuine REUR [[depeg]] would show as a gap between REUR's price and the prevailing EUR/USD rate, not as the price being above $1.00.

### Mint / redeem, KYC gating, on/off-ramp rails
As a fiat-backed euro stablecoin, REUR is intended to be **minted on receipt of euro reserves and redeemed 1:1 for euros**, with peg maintenance via primary issuance/redemption and secondary-market arbitrage against the EUR/USD rate. Primary mint/redeem runs through the issuer's permissioned, KYC-gated channel; the RxBridge ecosystem is positioned to move value between the classic fiat framework and the on-chain Royal tokens.

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 15.00M REUR |
| **Total Supply** | 5.00B REUR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $5.83B |

Note the **large gap between circulating (15.00M) and total (5.00B) supply**: only a tiny fraction of the authorised supply is in circulation, and FDV ($5.83B) is therefore a theoretical ceiling, not an economically meaningful figure for a deposit-backed coin (each circulating REUR should correspond to one euro of reserve). The headline FDV should not be read as latent dilution in the way an unvested-allocation token's FDV would be — supply is mint-on-deposit.

## Comparison vs Other EUR / Fiat Stablecoins

| | **REUR** | **[[royal-dollar\|RUSD]] (sibling)** | **EURC (Circle)** | **EURS (Stasis)** |
|---|---|---|---|---|
| **Peg** | Euro (EUR) | US dollar (USD) | Euro (EUR) | Euro (EUR) |
| **Issuer** | RIB Digital Holdings (Hong Kong) | RIB Digital Holdings (Hong Kong) | Circle | STASIS |
| **Reserve model** | EUR reserves, proof-of-reserve | USD reserves | EUR reserves (regulated) | EUR reserves |
| **Regulatory frame** | Hong Kong (+ MiCA for EU distribution) | Hong Kong | EU/MiCA-aligned | EU |
| **Chains** | Ethereum, BNB Chain, Tron | Ethereum, BNB Chain, Tron | Multi-chain | Multi-chain |
| **USD quote behaviour** | tracks EUR/USD (~$1.15) | ~$1.00 | tracks EUR/USD | tracks EUR/USD |
| **Mkt cap (snapshot)** | ~$17.2M | ~$250M | larger | larger |

REUR is a **small, issuer-specific** euro coin; the larger EUR stablecoins (EURC, EURS) have deeper liquidity and clearer EU regulatory standing, which matters for European distribution.

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.17 (2026-04-08) |
| **Current vs ATH** | -0.56% |
| **All-Time Low** | $1.14 (2026-03-30) |
| **Current vs ATL** | +1.83% |
| **24h Change** | -0.03% |
| **7d Change** | -1.15% |

The ATH/ATL band ($1.14–$1.17) is an **EUR/USD band**, not peg drift — it maps to the euro trading between roughly $1.14 and $1.17 over the period.

## How & Where It Trades / Is Used

- **Trading:** REUR is designed for OTC trading and exchange liquidity within the RCOINS/RxBridge ecosystem; no major centralised-exchange order books are surfaced in the CoinGecko data (see Exchange Listings below), so on-chain and issuer/OTC channels dominate.
- **Payment corridors:** euro-denominated payments, treasury operations, and settlement between fiat and on-chain rails via RxBridge.
- **DeFi composability:** standard multi-chain token (Ethereum, BNB Chain, Tron), but depth for a ~$17M-cap coin is thin relative to EURC/EURS.

## Narrative, Category & Catalysts

REUR is a **regional / FX-denominated (euro) stablecoin** in the **bank-issuer / proof-of-reserve** niche. Catalysts: demand for on-chain euro settlement; the build-out of the RxBridge fiat↔crypto ecosystem; and the regulatory trajectory — **MiCA** materially shapes who can distribute euro stablecoins into the EU, which is both a constraint (Hong Kong issuer) and an opportunity (clear rules favour compliant euro coins). The 2026 macro backdrop (Extreme Fear, bottoming/accumulation regime) compresses liquidity for small stablecoins regardless of peg.

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x3ed0b3c4c0168a560d34e361b8130dcca4677736` |
| Binance Smart Chain | `0x3ed0b3c4c0168a560d34e361b8130dcca4677736` |
| Tron | `TXUi9vL8Ltz4dVpC6RM8CdtKSTHxFZuFbz` |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.rcoins.digital/](https://www.rcoins.digital/) |
| **Twitter** | [@rcoins_official](https://twitter.com/rcoins_official) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $60.15M |
| **Market Cap Rank** | #887 |
| **24h Range** | $1.16 — $1.17 |
| **Last Updated** | 2026-04-09 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Risks

- **FX risk (for USD holders)** — the dollar value tracks EUR/USD; euro weakness lowers the USD price even with a perfect euro peg.
- **Reserve / off-chain dependency** — backing and redemption rely on the issuer holding sufficient euro reserves at banks; banking or custody disruption is the classic fiat-backed [[depeg]] trigger.
- **Redemption-gating / issuer risk** — redemption at par depends on the issuer's terms and solvency; RIB Digital Holdings is a single Hong Kong entity, concentrating counterparty risk.
- **Regulatory risk** — Hong Kong stablecoin licensing is evolving, and EU distribution of a euro stablecoin engages **MiCA**; either could affect issuance, redemption, or eligibility.
- **Transparency risk** — peg confidence depends on the quality and frequency of reserve attestations (see [[stablecoin-attestations]]).
- **Liquidity / concentration risk** — at ~$17M market cap with no surfaced major CEX books, large redemptions can be slippage-prone.

## Trading / Usage Playbook

- **As FX exposure:** REUR is a **long-EUR** instrument on-chain; USD P&L is dominated by EUR/USD, not by the (tight) euro peg.
- **On/off-ramp use:** use primary mint/redeem (KYC-gated) and RxBridge for euro settlement; do not assume deep open-market secondary liquidity.
- **Peg monitoring:** "on-peg" = ~€1.00, which prints as ~EUR/USD (≈$1.15) in dollars; the depeg signal is a **gap vs the live EUR/USD rate**, not a price above $1.00.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[stablecoins]]
- [[forex]]
- [[euro]]
- [[euro-coin]]
- [[royal-dollar]]
- [[stablecoin-attestations]]
- [[stablecoin-depegs]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- General market knowledge and Royal Euro / RIB Digital Holdings (rcoins.digital) public documentation; market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). No additional specific wiki source ingested yet.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 15.00M REUR |
| **Total Supply** | 5.00B REUR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $5.70B |

---
