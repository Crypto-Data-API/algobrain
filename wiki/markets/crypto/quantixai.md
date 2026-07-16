---
title: "Quantix Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [artificial-intelligence, crypto, defi]
aliases: ["QFI", "Quantix Finance", "QuantixAI"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.quantixfinance.xyz/"
related: ["[[ai-agent-tokens]]", "[[ai-agents]]", "[[crypto-markets]]", "[[defai]]", "[[tron]]"]
---

# Quantix Finance

**Quantix Finance** (ticker **QFI**, CoinGecko id `quantixai`) is an on-chain credit / lending protocol on the [[tron|Tron]] chain that brands itself as AI-powered. CoinGecko tags it across *Artificial Intelligence (AI)*, *Decentralized Finance (DeFi)*, *Lending/Borrowing Protocols*, *Trading Bots* and *Governance* categories — making it a [[defai|DeFAI]]-flavoured credit protocol within the broader [[ai-agents|AI meta]]. It pairs permissioned infrastructure aimed at institutions with open-access frameworks for DeFi users.

## Market Data

> | Metric | Value |
> |---|---|
> | **Market-cap rank** | #421 |
> | **Market cap** | $55.20M |
> | **Price** | $55.13 |
> | **24h change** | -0.004% |
> | **7d change** | -0.39% |
> | **Circulating supply** | 1.00M QFI |
> | **Total supply** | 10.00M QFI |
> | **Max supply** | 10.00M QFI |
> | **FDV** | $551.97M |
> | **All-time high** | $109.60 (2025-07-13), now ~-50% |
> | **All-time low** | $0.2284 (2024-03-19) |
>
> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**MC/FDV dilution flag (severe):** only **1.0M of 10.0M** tokens circulate — a **~10% float**. FDV ($551.97M) is **10×** the market cap ($55.20M). At a high $55 unit price this is a classic **low-float / high-FDV** setup: the headline cap understates the fully-diluted valuation by an order of magnitude, and future unlocks of the remaining ~9M tokens are a large structural overhang. Value this token on FDV, not market cap.

## Architecture / how it works

Quantix Finance describes itself as an on-chain credit protocol supporting **lenders, borrowers and pool managers** across curated credit pools. The stated architecture has three actor roles and several layered functions:

- **Credit pools** — segregated pools with their own underwriting parameters, collateral rules and risk tiers, so a default in one pool does not contaminate others (risk segmentation).
- **Underwriting & risk scoring** — the protocol claims to assess borrower quality and price risk per pool. The "AI / trading-bots" framing implies algorithmic credit-risk scoring and/or automated strategy execution, but the wiki holds **no independent verification** that any genuine machine-learning model is in the loop. Treat the AI layer as a **design claim** pending evidence.
- **Dual-track access** — Quantix advertises two operating environments: (1) **permissioned, compliance-aligned** pools intended for institutions (KYC'd counterparties, standardized reporting), and (2) **open-market, permissionless** configurations for ordinary DeFi users. This "institutional + retail" split is the protocol's main differentiator versus pure-retail money markets.
- **Monitoring & reporting** — real-time pool monitoring, performance tracking and standardized reporting are advertised as first-class features, positioning QFI as credit *infrastructure* rather than a single product.

Docs are published on GitBook (`quantixfinance.gitbook.io`). The contract lives on Tron (`TMVnKncD9NhAYEPoR6EutBrAKi8x6oZdR6`). Because the protocol is credit-based, the core economic engine is the spread between borrower interest and lender yield plus any pool-management/origination fees — but whether and how that spread accrues to QFI holders is **not confirmed** in the wiki.

## Tokenomics & supply

- **Float:** 1.0M circulating / 10.0M total / 10.0M max — only ~10% in circulation.
- **MC/FDV = 0.10:** the most diluted of the six pages in this batch; ~9M tokens remain to enter circulation.
- **High unit price ($55):** does not imply value — it reflects the small circulating supply, not scarcity of the full supply. A 10× unlock of the remaining float, absent demand growth, is a direct headwind to price.
- **Fixed cap (10M):** no open-ended inflation, but the unlock *schedule* (team, treasury, ecosystem) is the variable that matters and is not disclosed in the wiki snapshot.

## Value accrual / governance

**Honest flag: no confirmed fee/burn/governance loop is documented in the wiki.** CoinGecko's "Governance" tag implies QFI may carry voting rights over pool parameters or treasury, and a credit protocol *could* route origination/interest-spread fees or bad-debt insurance premiums to holders or stakers — but none of this is verified here. Until the docs confirm a concrete value-capture mechanism (fee share, buy-back/burn, staking-for-yield, or veToken governance), QFI should be treated as **speculative exposure to the protocol's narrative**, not a claim on cash flows.

## Comparison vs competitors

QFI is best compared to other on-chain credit/RWA-credit protocols and to DeFAI peers, rather than to conversational AI-agent tokens.

| Dimension | **Quantix (QFI)** | **Maple Finance (SYRUP)** | **Centrifuge (CFG)** | **Velvet ([[velvet|VELVET]])** |
|---|---|---|---|---|
| Category | AI-branded on-chain credit | Institutional on-chain credit | RWA credit / tokenized assets | DeFAI asset management |
| Chain | [[tron|Tron]] | Ethereum / Solana | Ethereum / Centrifuge L1 | [[bnb|BNB]] + [[base|Base]] |
| Core model | Curated credit pools, dual-track access | Permissioned lending pools to institutions | Real-world-asset financing pools | Tokenized on-chain portfolios |
| Verified AI | No (design claim) | No (not AI-branded) | No | Partial (DeFAI tooling) |
| Float / dilution | ~10% float, FDV 10× MC (severe) | Higher float | Higher float | ~42% float, FDV ~2.4× MC |
| CEX presence | None in snapshot (DEX-only) | Multiple CEXs | Multiple CEXs | Kraken/Bitget/KuCoin |

Takeaway: Quantix occupies the same *conceptual* niche as Maple/Centrifuge (on-chain credit with an institutional angle) but with an **AI wrapper, a far smaller and more diluted float, and no major CEX footprint** — a higher-risk, less-proven version of the institutional-credit thesis.

## How & where it trades

- **Native chain:** [[tron|Tron]] (contract `TMVnKncD9NhAYEPoR6EutBrAKi8x6oZdR6`).
- **Primary liquidity:** Tron DEX pools; the wiki snapshot shows **no major centralized-exchange listings**.
- **Liquidity:** 24h volume ~$2.75M against a ~$55.2M cap (turnover ~5%) — the highest *relative* turnover in this batch, but still modest and concentrated. No evidence of perpetual-futures markets, so there is no funding-rate or short-side mechanism to hedge.
- **Unlock overhang:** the ~9M locked tokens (90% of supply) are the dominant structural feature; any large unlock against a thin DEX book could move price sharply. Size positions against FDV, not the headline cap.

## Narrative / category & catalysts

QFI sits at the **AI + on-chain credit / RWA-adjacent DeFi** intersection on Tron. Unlike the pure conversational-agent meta, its narrative is "institutional credit infrastructure with AI risk tooling." The low-float/high-FDV structure makes the chart highly reflexive: a small free float can be marked up aggressively on thin volume, then face heavy supply as tokens unlock. The ~-50% drawdown from the July 2025 ATH tracks the broader cooling of the AI-DeFi cycle.

**Catalysts (potential, unverified):** a verifiable institutional credit-pool launch with disclosed TVL/AUM; a tier-1 CEX listing improving discoverability; published proof of a real AI/ML underwriting model; or a concrete value-accrual mechanism for holders. Conversely, an unlock cliff or evidence of bad debt would be a sharp negative catalyst.

## History / timeline

- **2024-03-19** — All-time low of $0.2284 recorded (early/illiquid history).
- **2025-07-13** — All-time high of $109.60; the run coincides with the AI-DeFi enthusiasm peak.
- **2026-06-21** — Snapshot: ~$55 price, ~-50% from ATH, ~$55.2M cap, #421 rank.

*(Only dated events present in the market-data snapshot are listed; no TGE/launch date is asserted because none is verified in the wiki.)*

## Risks

- **Low float / high FDV (10× MC):** dominant risk — large latent dilution; value on FDV. Unlock schedule undisclosed in the snapshot.
- **AI-narrative reflexivity:** price is tied to AI-meta sentiment; rotation away from DeFAI de-rates the token hard.
- **Unverified AI / credit performance:** AI and underwriting claims are not independently confirmed; on-chain credit protocols carry borrower-default and bad-debt risk, and Quantix's actual loan book is opaque in the wiki.
- **No confirmed value accrual:** holders may have no claim on protocol cash flows.
- **Chain & venue concentration:** Tron-only DEX liquidity in the snapshot; no CEX backstop.
- **Liquidity:** moderate but thin relative to FDV; thin float amplifies volatility.
- **Vaporware/execution risk:** broad "institutional + AI + credit" branding with limited verifiable product.
- **Macro:** the tape on 2026-06-23 is Extreme Fear ([[fear-and-greed-index|Fear & Greed]] 21, market-health 29/100, BEARISH) in a long-horizon **Bottoming / Accumulation** regime — low-float speculative credit tokens are especially vulnerable to unlock-driven downside even as the broader market bottoms.

## Trading playbook

High-beta, low-float AI-credit names like QFI behave violently in both directions. In the current Extreme-Fear, bottoming tape:

- **Bias:** treat as a high-risk speculative satellite, not a core hold. The 10× FDV/MC gap means *any* serious size should be valued on fully-diluted terms.
- **Entry:** demand confirmation of a real catalyst (CEX listing, disclosed AUM, value-accrual mechanism) rather than buying narrative alone; in a bottoming regime, prefer accumulation only on capitulation flushes with rising real volume.
- **Risk control:** keep position size small; pre-define a hard stop given DEX-only thin liquidity and no perp hedge. Watch the Tron contract for unlock transfers — a large treasury/team unlock is the most likely sharp drawdown trigger.
- **Avoid** chasing high-turnover spikes on a ~$2.75M/day book — that turnover is the same liquidity you would have to exit through.

## See Also

- [[crypto-markets]]
- [[tron]]
- [[defi]]
- [[defai]]
- [[ai-agents]]
- [[ai-agent-tokens]]
- [[velvet]]
- [[token-unlocks]]

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko snapshot).
- Macro framing as of 2026-06-23 (cryptodataapi.com / CoinGecko): Fear & Greed 21 (Extreme Fear), Bottoming / Accumulation regime.
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | QFI |
| **Market Cap Rank** | #368 |
| **Market Cap** | $62.80M |
| **Current Price** | $62.80 |
| **Categories** | Decentralized Finance (DeFi), Yield Farming, Lending/Borrowing Protocols |
| **Website** | [https://www.quantixfinance.xyz/](https://www.quantixfinance.xyz/) |

---

## Overview

Quantix Finance is an on-chain credit protocol that provides both permissioned infrastructure for institutions and open access frameworks within decentralized finance. It enables structured capital allocation across digital credit markets through a combination of identity based participation and blockchain native financial primitives.

The platform supports multiple participant roles, including lenders, borrowers, and pool managers, operating across curated credit pools with transparent underwriting, risk segmentation, and performance tracking. Institutional participants engage through permissioned environments with compliance aligned access, while DeFi users can access structured yield opportunities within open market configurations.

Built to improve capital efficiency in digital asset markets, Quantix Finance integrates real time monitoring, standardized reporting, and modular capital deployment systems. By combining institutional grade infrastructure with accessible on-chain credit markets, Quantix delivers a unified framework for scalable, transparent, and risk aware lending across the QFI ecosystem.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.00M QFI |
| **Total Supply** | 10.00M QFI |
| **Max Supply** | 10.00M QFI |
| **Fully Diluted Valuation** | $627.99M |
| **Market Cap / FDV Ratio** | 0.10 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $109.60 (2025-07-13) |
| **Current vs ATH** | -42.71% |
| **All-Time Low** | $0.2284 (2024-03-19) |
| **Current vs ATL** | +27394.88% |
| **24h Change** | -1.51% |
| **7d Change** | +5.71% |
| **30d Change** | +14.26% |
| **1y Change** | -40.20% |

---

## Platform & Chain Information

**Native Chain:** Tron

### Contract Addresses

| Chain | Address |
|---|---|
| Tron | `TMVnKncD9NhAYEPoR6EutBrAKi8x6oZdR6` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.quantixfinance.xyz/](https://www.quantixfinance.xyz/) |
| **Twitter** | [@quantixfinance](https://twitter.com/quantixfinance) |
| **Telegram** | [quantixfinance](https://t.me/quantixfinance) (14,173 members) |
| **Whitepaper** | [https://quantixfinance.gitbook.io/quantixfinance-docs](https://quantixfinance.gitbook.io/quantixfinance-docs) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.96M |
| **Market Cap Rank** | #368 |
| **24h Range** | $62.54 — $64.41 |
| **CoinGecko Sentiment** | 0% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
