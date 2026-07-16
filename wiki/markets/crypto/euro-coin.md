---
title: "EURC"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, forex, regulation]
aliases: ["EURC", "EUROC", "Euro Coin"]
entity_type: protocol
founded: 2022
headquarters: "Issuer: Circle (New York, USA)"
website: "https://www.circle.com/eurc"
related: ["[[base]]", "[[circle]]", "[[crypto-markets]]", "[[ethereum]]", "[[mica]]", "[[solana]]", "[[stablecoin]]", "[[stablecoins]]", "[[usdc]]"]
---

# EURC

**EURC** (formerly EUROC, launched June 2022; ticker **EURC**) is [[circle|Circle]]'s euro-pegged [[stablecoin]], issued under the same full-reserve model as [[usdc|USDC]] and redeemable 1:1 for euros. It is the **largest [[mica|MiCA]]-compliant euro stablecoin** (~41% of the euro-stablecoin market as of early 2026) and the main on-chain instrument for euro cash legs — making it the closest thing to an on-chain EUR/USD FX market for traders.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | EURC |
| **Current Price (USD)** | $1.15 |
| **Market Cap** | $439,046,610 |
| **Market Cap Rank** | #111 |
| **24h Volume** | $10,794,273 |
| **24h Change** | +0.04% |
| **7d Change** | -0.80% |
| **Circulating / Total Supply** | ~382.93M EURC |
| **Max Supply** | Uncapped (mint/burn vs euro deposits) |
| **MC / FDV** | 1.00 |
| **Peg** | 1:1 EUR (USD price = spot EUR/USD) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: EURC's **USD price of $1.15 is the EUR/USD exchange rate, not a peg deviation** — each EURC remains 1:1 redeemable for one euro, so its dollar quote simply tracks the euro. The 7-day -0.80% move reflects EUR weakening vs. USD over the week, not any loss of backing. Supply has grown to ~383M EURC (cap ~$439M, rank #111), up from ~355M in April 2026, consistent with EURC's market-share gains under [[mica|MiCA]]. The broader **"Established Bear Market"** ([[fear-and-greed-index|Fear & Greed]] 23) is largely irrelevant to a fiat-backed euro stablecoin except insofar as risk-off conditions slow on-chain euro activity.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | EURC |
| **Sector** | EUR fiat-backed stablecoin ([[mica|MiCA]]-compliant) |
| **Issuer** | Circle (NYSE: CRCL since June 2025) |
| **Peg** | 1:1 euro, full-reserve euro-denominated bank deposits |
| **Chains** | Ethereum, Base, Solana, Stellar, Avalanche, World Chain (6 chains); settling on Circle's Arc L1 |
| **Regulatory status** | MiCA-compliant from day one of enforcement (Circle holds a French EMI license) |
| **Website** | [https://www.circle.com/eurc](https://www.circle.com/eurc) |

---

## Overview

Euro Coin is issued by Circle under the same reserve model as USDC: 100% backed by euros in euro-denominated accounts, with monthly attestations. Its price in USD floats with EUR/USD (~$1.15, June 2026), so the "price history" of EURC is essentially an FX chart, not a peg-quality chart.

---

## Major News & Events

- **Late 2024 / early 2025 — MiCA enforcement.** The EU's Markets in Crypto-Assets stablecoin provisions took full effect, forcing EEA exchanges to delist non-compliant stablecoins (including [[usdt|USDT]] and Tether's EURT). EURC, compliant from day one, absorbed the vacated euro-stablecoin demand.
- **Jun 2025 — Circle IPO.** Circle listed on the NYSE (ticker **CRCL**) in June 2025 — one of the year's defining crypto-equity events — raising the regulatory and institutional profile of both USDC and EURC.
- **2025–2026 — market share surge.** EURC's share of the euro-stablecoin market grew from **17% to 41% in twelve months**, reaching ~**$424M market cap / ~359M supply by February 2026** (Q1 2026 stablecoin reports).
- **2025 — Arc.** Circle announced **Arc**, its own Layer-1 blockchain; USDC, EURC and cirBTC settle natively on Arc with Circle Mint as the enterprise issuance API.

---

## Trading Relevance

- **On-chain FX:** EURC/USDC pools (Uniswap V3, Curve, Orca on Solana) are the deepest on-chain EUR/USD venue — usable for FX hedging, euro cash management in DeFi, and basis trades vs CME EUR futures. EURC/USDC pricing tracks spot EUR/USD within bps when liquidity is healthy.
- **Carry asymmetry:** unlike USDC, MiCA constrains interest-bearing features and euro rates have been below USD rates, so euro stablecoin growth is driven by compliance and payments demand, not yield.
- **Where it trades:** Kraken EURC/EUR (main CEX venue), Coinbase; DEX: Uniswap V3/V2 (Ethereum), Orca (Solana).
- **Signals:** EURC supply growth = European on-chain adoption gauge; watch MiCA enforcement actions against competitors, Circle (CRCL) earnings/disclosures, and Arc ecosystem rollout.
- **Macro angle:** a structural play on the euro digital-payments stack; the main competitive threat is a future ECB digital euro and bank-issued euro tokens (e.g., EURCV, EURI).

---

## Tokenomics & Supply

| Metric | Value (2026-06-21 snapshot) |
|---|---|
| **Circulating / Total Supply** | ~382.93M EURC |
| **Market Cap** | ~$439.05M |
| **Max Supply** | Uncapped (mint/burn vs euro deposits) |
| **MC / FDV** | 1.00 |

Supply is elastic: Circle mints EURC when authorized partners deposit euros and burns it on redemption, so circulating = total and there is no dilution overhang. Supply growth (from ~355M in April to ~383M in June 2026) is the cleanest read on **European on-chain adoption** — each new EURC corresponds to a euro placed in reserve.

---

## Valuation & Peg Framing

EURC is not valued for upside — its USD "return" is purely the EUR/USD exchange-rate path. The relevant quality dimensions are **backing and peg integrity**, where EURC is best-in-class for a euro stablecoin:

- **Backing**: 100% full-reserve euro bank deposits/short-dated instruments, monthly attestations, [[circle|Circle]] as a regulated NYSE-listed issuer (CRCL). This is exogenous, transparent collateral — the opposite of endogenous designs like [[usdd|USDD]].
- **Peg behavior**: the dollar quote tracks spot EUR/USD; on-chain EURC/USDC pools price within bps of FX spot when liquidity is healthy. A move like the recent -0.80% week is FX, not de-peg.
- **No native yield**: [[mica|MiCA]] constrains interest-bearing features and euro rates have sat below USD rates, so EURC growth is driven by compliance and payments demand, not carry.
- **Bottom line**: a low-risk, fiat-backed euro instrument; "fair value" is one euro, and the trade is access to on-chain EUR exposure / FX, not appreciation.

---

## Peer Comparison

| Stablecoin | Currency | Price (USD) | Market Cap | Rank | Backing |
|---|---|---|---|---|---|
| **EURC** | EUR | $1.15 | $439M | #111 | Circle full-reserve euro |
| [[usdc\|USDC]] | USD | ~$1.00 | tens of $B | top-10 | Circle full-reserve USD |
| [[usdt\|USDT]] | USD | ~$1.00 | tens of $B | top-5 | Tether reserves |
| [[usdd\|USDD]] | USD | $0.9989 | $1.37B | #56 | Overcollateralized TRX/sTRX |
| EURCV / EURI | EUR | ~$1.15 | smaller | — | Bank-issued euro (competitors) |

> *EURC and USDD figures from the 2026-06-21 snapshot. EURC is the largest MiCA-compliant euro stablecoin; its main euro competitors (EURCV, EURI) are bank-issued and far smaller.*

---

## Platform & Chain Information

| Chain | Address |
|---|---|
| Ethereum | `0x1abaea1f7c830bd89acc67ec4af516284b1bc33c` |
| Base | `0x60a3e35cc302bfa44cb288bc5a4f316fdb1adb42` |
| Solana | `HzwqbKZw8HxMN6bF2yFZNrht3c2iXXzpKcFu7uBEDKtr` |
| Stellar | `EURC-GDHU6WRG...` |
| Avalanche | `0xc891eb4cbdeff6e073e859e987815ed1505c2acd` |
| World Chain | `0x1c60ba0a0ed1019e8eb035e6daf4155a5ce2380b` |

---

## Risks

> **Euro-stablecoin and [[mica|MiCA]]-regulatory dynamics are the dominant risk/structure here** — not de-peg risk, which is low given full-reserve backing.

- **FX, not credit**: the main "risk" to a USD holder is simply EUR depreciation vs. USD; EURC's dollar value falls when the euro falls. This is currency exposure, not a stablecoin failure.
- **Regulatory dependence**: EURC's entire moat is [[mica|MiCA]] compliance and Circle's French EMI license. Adverse MiCA reinterpretation, license issues, or new EU stablecoin rules could disrupt issuance/redemption.
- **ECB digital euro**: a future ECB CBDC could crowd out private euro stablecoins for retail/payments use.
- **Bank-issued competition**: EURCV (Societe Generale-Forge), EURI (Banking Circle) and other bank-issued euro tokens compete for the same regulated euro on-chain demand.
- **Issuer / reserve risk**: dependence on [[circle|Circle]] as issuer and on the banks holding the euro reserves; a banking-sector stress (cf. the March 2023 USDC/SVB episode) could transiently affect confidence.
- **Liquidity depth**: euro on-chain liquidity is far shallower than USD stablecoins; large EURC/USDC swaps can move pricing and widen the spread vs. FX spot.

---

## Social & Community

| Platform | Link |
|---|---|
| **Website** | [https://www.circle.com](https://www.circle.com) |
| **Twitter** | [@circlepay](https://twitter.com/circlepay) |

---

## Related

- [[circle]] — issuer (NYSE: CRCL)
- [[usdc]] — sister USD stablecoin
- [[mica]] — the regulation that defines EURC's moat
- [[stablecoin]], [[stablecoins]], [[stablecoin-supply]], [[usdt]], [[usdd]]
- [[ethereum]], [[base]], [[solana]], [[crypto-markets]]

---

## Sources

- CoinGecko top-1000 snapshot, 2026-04-09 (historical market data)
- Market snapshot 2026-06-21: cryptodataapi.com / CoinGecko markets data (price $1.15, cap $439M, rank #111, supply ~382.93M)
- [Circle — EURC official page](https://www.circle.com/eurc)
- [Circle — MiCA-compliant stablecoins (EEA)](https://www.circle.com/circle-eea)
- [Stablecoin Insider — Circle's EURC Q1 2026 stablecoin report](https://stablecoininsider.org/eurc-q1-2026-stablecoin-report/) (41% euro-stablecoin share, $424M cap, Feb 2026)
- [Utila — Euro stablecoin landscape 2026: what MiCA means for fintechs](https://utila.io/blog/euro-stablecoin-report-what-mica-means-for-fintechs)
- WebSearch verification, 2026-06-10

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 373.22M EURC |
| **Total Supply** | 373.22M EURC |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $427.65M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.35 (2023-03-14) |
| **Current vs ATH** | -15.24% |
| **All-Time Low** | $0.0528 (2022-12-09) |
| **Current vs ATL** | +2068.45% |
| **24h Change** | +0.42% |
| **7d Change** | +0.30% |
| **30d Change** | -1.22% |
| **1y Change** | -1.40% |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | EURC/USDC | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X1ABAEA1F7C830BD89ACC67EC4AF516284B1BC33C/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |
| Orca | HZWQBKZW8HXMN6BF2YFZNRHT3C2IXXZPKCFU7UBEDKTR/EPJFWDD5AUFQSSQEM2QN1XZYBAPC8G4WEGGKZWYTDT1V | Spot |
| Uniswap V2 (Ethereum) | 0X1ABAEA1F7C830BD89ACC67EC4AF516284B1BC33C/0X9D39A5DE30E57443BFF2A8307A4256C8797A3497 | Spot |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $38.29M |
| **Market Cap Rank** | #111 |
| **24h Range** | $1.14 — $1.15 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
