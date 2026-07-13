---
title: "USD1 (World Liberty Financial)"
type: entity
created: 2026-04-09
updated: 2026-06-20
status: excellent
tags: [crypto, regulation, news]
aliases: ["USD1", "WLFI USD1", "World Liberty Financial USD"]
entity_type: protocol
founded: 2025
headquarters: "United States (World Liberty Financial)"
website: "https://www.worldlibertyfinancial.com/"
related: ["[[crypto-markets]]", "[[bnb]]", "[[binance]]", "[[stablecoins]]", "[[tether]]", "[[narrative-trading]]"]
---

# USD1 (World Liberty Financial)

**USD1** (ticker **USD1**, native to [[bnb|BNB Chain]]) is the fiat-backed, Treasury-reserve [[stablecoin]] issued by **[[world-liberty-financial|World Liberty Financial]] (WLFI)**, the Trump-family-affiliated crypto venture. Launched in March 2025, it became the fastest-growing fiat-backed stablecoin of the period — but its growth is dominated by a single event (the $2B MGX→[[binance|Binance]] investment settled in USD1) and ~87% of supply reportedly sits on Binance. For traders it is less a neutral settlement asset than a **political-risk instrument** inside the "Trump trade" basket.

---

## Market Data

| Metric | Value |
|---|---|
| **Market Cap Rank** | #22 |
| **Market Cap** | ~$4.78B |
| **Current Price** | $1.0000 |
| **24h Volume** | ~$767.3M |
| **24h Change** | +0.05% |
| **7d Change** | +0.02% |
| **Circulating Supply** | ~4.78B USD1 |
| **Max Supply** | Unlimited (elastic mint/redeem) |
| **All-Time High** | $1.025 (2025-05-12) — **-2.39%** |
| **All-Time Low** | $0.98963 (2025-10-01) — **+1.08%** |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

USD1 holds its **$1.00 peg** exactly at the snapshot. Supply has grown to **~$4.78B**, up from ~$4.29B at the April 2026 snapshot — continued expansion even through the **"Established Bear Market"** ([[crypto-fear-and-greed-index|Fear & Greed]] = 23) regime, reflecting ongoing Trump-affiliated / Gulf-capital flows rather than broad organic usage. The very high ~$767M daily volume relative to a usage-light asset is largely **Binance pair churn**. See [[market-regime]].

---

## Technology / Protocol & Backing

USD1 is a **centralized, fiat-backed stablecoin** — structurally closer to [[tether|USDT]]/USDC than to decentralized peers like [[gho|GHO]] or [[usds|USDS]].

- **Backing** — 1:1 reserves in **short-term US Treasuries, US-dollar deposits, and cash equivalents**, custodied via **BitGo**.
- **Mint / redeem** — issued and redeemed against fiat through WLFI's issuance pipeline; supply is elastic (no max).
- **Multi-chain** — launched on **[[bnb|BNB Chain]] + [[ethereum|Ethereum]]** (Mar 2025); now also Solana, Tron, Aptos, Plume, Monad, Mantle, and Morph L2.
- **Issuer economics** — WLFI earns the reserve yield (estimated ~$60–80M/yr from the $2B MGX tranche alone; ~$150M total 2026 revenue run-rate); the **Trump family receives 75% of WLFI net token-sale proceeds**.

---

## Peg Mechanism, De-Peg Risk & Redemption

- **Peg type** — hard 1:1 fiat backing with authorized **mint/redeem** at $1, the standard fiat-stablecoin model. The peg's *credit* quality (reserve composition) is solid; the peg's *behavioral* risk is political, not financial.
- **Concentration risk** — with **~87% of supply on Binance**, peg defense depends heavily on **Binance market-making** rather than broad redemption arbitrage. Monitor **USD1/USDT on Binance** for stress and Curve/Uniswap pools for on-chain discounts.
- **De-peg catalysts** — unlike a reserve-quality wobble, USD1's depeg risk is **headline-driven**: congressional probe escalations, litigation, an adverse political cycle. A **brief depeg occurred in April 2026** during what WLFI called a "coordinated attack." See [[stablecoin-depegs]].
- **Redemption** — institutional/authorized redemption at $1 via the issuer; retail exits mostly route through Binance liquidity.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~4.78B USD1 |
| **Total Supply** | ~4.78B USD1 |
| **Max Supply** | Unlimited (elastic, mint/redeem) |
| **Fully Diluted Valuation** | ~$4.78B |
| **Market Cap / FDV Ratio** | 1.00 |

Supply is **demand-elastic** (mint on deposit, burn on redemption); no dilution in the equity sense (MC = FDV). The defining structural feature is **flow concentration**: roughly half the float was seeded by the single **$2B MGX tranche**, and ~87% of supply sits on Binance — so USD1's "supply growth" is better read as a **political-flow signal** than as organic adoption.

---

## Market Structure & Trading Relevance

- **Not yield, but signal** — USD1 supply growth is a real-time proxy for Trump-affiliated crypto flows and Gulf-capital deployment; supply spikes have preceded [[bnb|BNB]]-ecosystem strength (USD1 is BNB-native).
- **Peg-risk trading** — political shock events are the depeg catalysts, not reserve quality; with ~87% on one venue, peg defense leans on Binance.
- **Basket membership** — core of the **"Trump trade" basket** alongside the WLFI token and the TRUMP memecoin; headlines move all three together — USD1 with the smallest beta, WLFI with the largest. See [[narrative-trading]].
- **Counterparty due diligence** — for USD1 as settlement collateral, the relevant risks are **issuer-political** (congressional action, sanctions optics on Gulf flows), not reserve credit. GENIUS Act compliance keeps it inside the US regulated perimeter, unlike [[tether]].

### Exchange Listings

| Venue | Pair | Notes |
|---|---|---|
| Binance | USD1/USDT | ~87% of total supply reportedly held on Binance |
| Kraken | USD1/USD | |
| Bitget | USD1/USDT | |
| KuCoin | USD1/USDT | |
| Uniswap V3 (Ethereum) | USD1/USDT | Spot (DEX) |

### Contract Addresses (selected)

| Chain | Address |
|---|---|
| BNB Chain | `0x8d0d000ee44948fc98c9b98a4fa4921476f08b0d` |
| Ethereum | `0x8d0d000ee44948fc98c9b98a4fa4921476f08b0d` |
| Solana | `USD1ttGY1N17NEEHLmELoaybftRBUSErhqYiQzvEmuB` |
| Tron | `TPFqcBAaaUMCSVRCqPaQ9QnzKhmuoLR6Rc` |
| Plume / Monad / Mantle / Morph | `0x111111d2bf19e43c34263401e0cad979ed1cdb61` |

---

## Narrative & Category

USD1 is a **fiat-backed USD stablecoin with a political overlay** — a unique category among the top stablecoins. Where [[tether|USDT]]/USDC compete on neutrality and [[gho|GHO]]/[[usds|USDS]] on decentralization, USD1 competes on **political distribution advantage**: exchange support, a pro-crypto administration tailwind, and Gulf-capital relationships. That same affiliation is its defining *risk*. It is the most "newsy" stablecoin and the cleanest on-chain expression of the "Trump trade."

---

## Valuation Framing (qualitative)

As a pegged asset USD1 is not "valued"; the economics accrue to **WLFI** (reserve yield, ~$150M 2026 run-rate, 75% of net proceeds to the Trump family). Frame USD1 via: **supply trend** (political/Gulf-flow proxy), **venue concentration** (Binance share = peg fragility), **peg deviations** under headline stress, and **regulatory standing** (GENIUS Act compliance vs probe/litigation overhang). Rising supply at a firm peg is bullish for the WLFI complex; concentration + political risk caps how "neutral" USD1 can ever be treated.

---

## Peer Comparison

| Stablecoin | Model | Backing | Mkt Cap (rank) | Distinctive risk |
|---|---|---|---|---|
| **USD1** | Fiat-backed (centralized) | T-bills + cash (BitGo) | ~$4.78B (#22) | Political / concentration |
| [[tether\|USDT]] | Fiat-backed (centralized) | Cash + T-bills + other | huge (#3-tier) | Reserve opacity / offshore |
| USDC | Fiat-backed (centralized) | Cash + T-bills | huge | Banking-channel risk |
| [[usds\|USDS]] | Decentralized + RWA | Crypto + treasuries | ~$10.26B (#12) | Smart-contract / governance |
| [[gho\|GHO]] | Decentralized, overcollateralized | Aave collateral | ~$598M (#91) | Collateral cascade |

> *Peer market caps point-in-time (2026-06-20 where shown); others are category context.*

---

## Risks

- **Political / headline risk** — congressional probes, litigation, and election-cycle shifts are the primary depeg catalysts.
- **Venue concentration** — ~87% on Binance means peg defense depends on a single market-maker; a Binance-specific shock would be acute.
- **Single-flow dependence** — roughly half of float traces to the one MGX tranche; redemption of a large holder would shrink supply sharply.
- **Conflict-of-interest litigation** — Justin Sun's April 2026 lawsuit (alleged extortion, frozen wallets) and circular-collateral comparisons (WLFI pledging 5B WLFI to borrow $75M) are reputational overhangs.
- **Regulatory** — GENIUS Act compliance helps, but political scrutiny of a sitting-administration-affiliated issuer is unprecedented.
- **Established Bear Market backdrop** — risk-off macro (Fear & Greed 23) raises sensitivity to any peg-stress headline.

> *This page is informational, not investment advice. As a stablecoin, deviations from $1 are the signal to watch.*

---

## Major News & Events

- **2025-03** — USD1 launches on [[ethereum|Ethereum]] + [[bnb|BNB Chain]].
- **2025-05** — **$2B MGX→Binance investment settled in USD1** (Fortune), the largest stablecoin-settled transaction in crypto history; Binance CEO Richard Teng later (Nov 2025) denied any tie to CZ's presidential pardon.
- **2025-12-25** — Supply crosses **$3B** (Business Wire); Trump-family profits reach ~$1B.
- **2026-02-05** — **House probe targets WLFI** after reports an Abu Dhabi-linked entity secretly agreed to buy a 49% WLFI stake for $500M shortly before the inauguration.
- **2026-02-26** — Supply tops **$4.7B**; WLFI ties governance voting power to staking (CoinDesk).
- **2026-04** — **Justin Sun sues WLFI** (alleged extortion, frozen wallets); WLFI circular-collateral controversy (5B WLFI pledged to borrow $75M); a **brief USD1 depeg** during a claimed "coordinated attack" (DL News).
- **2026 (Jun)** — Supply ~$4.78B; peg firm at $1.00; on track for ~$150M 2026 revenue.

---

## Whale & Holder Information

> *Reported concentration: ~87% of USD1 supply on Binance; the $2B MGX tranche is the single dominant holder flow. DefiLlama tracks per-chain supply: https://defillama.com/stablecoin/world-liberty-financial-usd*

---

## Related

- [[crypto-markets]]
- [[world-liberty-financial]] — issuer
- [[bnb]] — native chain; USD1 growth is a BNB-ecosystem flow signal
- [[binance]] — dominant holding/trading venue and peg backstop
- [[stablecoins]] — USD1 vs [[tether]] USDT and USDC under the GENIUS Act
- [[narrative-trading]] — "Trump trade" basket (USD1, WLFI, TRUMP)
- [[usds]], [[gho]] — decentralized stablecoin contrast
- [[stablecoin-depegs]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data 2026-06-20 from `raw/data/crypto-loop/coingecko-markets.json` (cryptodataapi.com / CoinGecko); macro backdrop from `raw/data/crypto-loop/_digest.md`.
- Fortune — "How the Trump family is poised to profit from a $2 billion Middle East crypto deal with Binance" (2025-05-07): https://fortune.com/crypto/2025/05/07/world-liberty-financial-wlfi-trump-binance-mgx-stablecoin-deal/
- CoinDesk — "World Liberty Financial ties voting power to staking as USD1 supply tops $4.7 Billion" (2026-02-26): https://www.coindesk.com/markets/2026/02/26/world-liberty-financial-ties-voting-power-to-staking-as-usd1-supply-tops-usd4-7-billion
- CoinDesk — "House probe targets WLFI after report of $500 Million UAE stake" (2026-02-05): https://www.coindesk.com/policy/2026/02/05/house-probe-targets-wlfi-after-report-of-usd500-million-uae-stake
- CNBC — "Binance CEO dismisses claims the firm boosted a Trump crypto venture ahead of CZ pardon" (2025-11-04): https://www.cnbc.com/2025/11/04/binance-ceo-richard-teng-denies-changpeng-zhao-trump-crypto-project-cz-pardon-world-liberty-financial-mgx-.html
- DL News — "USD1 stablecoin breaks peg as World Liberty Financial suffers 'coordinated attack'": https://www.dlnews.com/articles/defi/usd1-stablecoin-breaks-peg-as-world-liberty-financial-suffers-coordinated-attack/
- Stablecoin Insider — "WLFI's USD1 Q1 2026 Stablecoin Report": https://stablecoininsider.org/usd1-q1-2026-stablecoin-report/
- Verified via Perplexity sonar + web search, 2026-06-10
