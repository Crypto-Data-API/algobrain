---
title: "SMH (VanEck Semiconductor ETF)"
type: market
created: 2026-05-31
updated: 2026-06-19
status: excellent
tags: [etf, stocks, semiconductors, ai-trading, basket]
aliases: ["SMH", "VanEck Semiconductor ETF", "Semiconductor ETF"]
ticker: "SMH"
exchange: "NASDAQ"
sector: "Semiconductors (basket)"
related:
  - "[[nvidia]]"
  - "[[taiwan-semiconductor-manufacturing]]"
  - "[[asml-holding]]"
  - "[[broadcom]]"
  - "[[amd]]"
  - "[[micron]]"
  - "[[intel]]"
  - "[[semiconductor-earnings-cycle]]"
  - "[[ai-capex-vs-cash-flow-divergence]]"
  - "[[situational-awareness-lp]]"
---

**SMH** is the VanEck Semiconductor ETF, a market-cap-weighted basket of the largest publicly listed semiconductor and semiconductor equipment companies. It is the most-traded US-listed semiconductor basket ETF and the standard expression for systematic long or short exposure to the chip complex. Top holdings are heavily concentrated in [[nvidia|NVDA]] (typically 18-22% of the basket as of 2025-2026), [[taiwan-semiconductor-manufacturing|TSM]], [[broadcom|AVGO]], [[asml-holding|ASML]], [[amd|AMD]], and other megacap names — making SMH a high-beta proxy for the AI chip cycle. SMH is the largest single put position in [[situational-awareness-lp|Situational Awareness LP]] at $2.04B notional per late May 2026 13F filings — chosen as the basket short because it captures the systemic AI-chip-consensus thesis rather than betting on any single semiconductor name.

## Basket characteristics

| Field | Detail |
|---|---|
| **Issuer** | VanEck |
| **Listing** | NASDAQ |
| **Index tracked** | MVIS US Listed Semiconductor 25 Index (MVSMHTR) |
| **Expense ratio** | ~0.35% |
| **Number of holdings** | ~25 |
| **Concentration** | Top 10 typically 70%+ of basket |
| **NVDA weight** | Typically 18-22% (varies with index reweighting) |
| **Options market** | Highly liquid; deep monthly + LEAP options chains |

## Index Tracked & Methodology

SMH tracks the **MVIS US Listed Semiconductor 25 Index**, a rules-based benchmark of the 25 largest and most-liquid US-listed companies in semiconductors and semiconductor equipment (including ADRs of foreign chipmakers like [[taiwan-semiconductor-manufacturing|TSM]] and [[asml-holding|ASML]]). Methodology features that shape the fund:

- **Modified market-cap weighting with caps.** Holdings are weighted by float-adjusted market cap, but a capping scheme limits the largest names and the sum of the big names to keep the index investable and diversification-rule compliant. Even so, the cap on the top name is generous enough that [[nvidia|NVDA]] routinely sits near the top of the allowed range.
- **Narrow, deliberately concentrated roster.** Only ~25 names — by design a *focused* basket, not a broad sector fund. This is what makes SMH a clean systematic chip-cycle expression and also what makes it megacap-dominated.
- **Includes equipment makers.** [[asml-holding|ASML]], Applied Materials, Lam Research, and KLA sit alongside the chip designers/fabs, so SMH captures the *capital-equipment* leg of the cycle, not just chip sales.
- **Periodic rebalance/reconstitution** resets weights back toward the capped targets; between rebalances, a megacap rally (e.g., NVDA) lets the top weight drift upward until the next reset.

## Megacap Concentration Dynamics

SMH's behavior is dominated by a handful of names, and understanding the concentration is essential:

- **[[nvidia|NVDA]] is the keystone** at ~18-22% of the basket. Because NVDA is roughly one-fifth of SMH, **SMH puts are partially NVDA puts** and SMH's path is heavily tied to NVDA's earnings, product cadence (Hopper → Blackwell → Rubin), and AI-demand narrative.
- **Top 5 ≈ 50%, top 10 ≈ 70%+.** Below NVDA, [[broadcom|AVGO]], [[taiwan-semiconductor-manufacturing|TSM]], [[asml-holding|ASML]], and [[amd|AMD]] fill out the top tier. A small set of names therefore drives the vast majority of moves.
- **Earnings clustering.** The megacap chip names report within a compressed window each quarter; SMH realized volatility and gap risk concentrate sharply into that window, with NVDA's print the single biggest event.
- **Two-sided implication.** The concentration is *why* SMH is the canonical basket short (see below) — it captures cohort-level repricing — but it also means SMH is **not** diversified protection against any single name; it is a leveraged bet on the AI-chip leaders, NVDA above all.

## Why SMH is the canonical chip-cycle short expression

1. **Systemic exposure** — single-name shorts (e.g., NVDA puts) carry idiosyncratic earnings risk; SMH captures the cohort-level repricing without single-name binary outcomes
2. **Deep options liquidity** — large-notional put positions are practical; bid-ask is tight at the index level
3. **Lower borrow / locate friction** vs single-name short stock
4. **Higher convexity per dollar** during cycle inflections vs equally-weighted basket
5. **Tax efficiency** for institutional accounts vs assembled single-name basket

## Why short SMH in an AI bear thesis

Per [[ai-capex-vs-cash-flow-divergence]] and the [[aschenbrenner-bifurcated-ai-thesis|Aschenbrenner thesis]]:

- AI scaling continues but **value rotates from chips to physical infrastructure**
- Hyperscaler in-house ASIC adoption (Microsoft Maia, Google TPU, Meta MTIA, Amazon Trainium) compresses merchant chip margins even in a bull AI scenario
- NVDA's pricing power has already been priced in at peak multiples; downside scenarios require any margin compression to translate to multiple compression
- Memory / HBM share competition (Samsung, Hynix, Micron) caps Micron's upside even in HBM bull case

SMH captures all of these dynamics in a single position. Single-name puts on NVDA, AVGO, AMD individually do not aggregate cleanly because of correlated idiosyncratic risk; SMH provides clean systematic exposure to chip-complex repricing.

## AI & Cycle Sensitivity

Semiconductors are **structurally cyclical** even within a secular AI uptrend, and SMH packages both forces:

- **AI capex super-cycle.** The dominant 2023-2026 driver is hyperscaler AI infrastructure spending (data-center GPUs, custom ASICs, HBM memory, advanced-node fab capacity). SMH is the most direct equity expression of this capex wave, which links it tightly to the [[ai-capex-vs-cash-flow-divergence|AI-capex-vs-cash-flow]] debate and to [[hyperscaler-capex|hyperscaler capex]] guidance.
- **Classic silicon cycle underneath.** Beneath AI, the industry still oscillates through inventory builds/draws, foundry utilization, memory pricing (DRAM/NAND/HBM), and equipment-order cycles — the [[semiconductor-earnings-cycle|semiconductor earnings cycle]]. These can turn even while AI demand holds, producing the cyclicality SMH inherits.
- **Memory leg.** HBM and conventional memory (Micron, Samsung, Hynix) add a sharply cyclical, commodity-priced layer; memory up-cycles and down-cycles are violent.
- **Geopolitical / supply-chain risk.** Taiwan concentration (TSM), China export controls, and CHIPS-Act-style reshoring are structural overhangs unique to this basket.
- **Rate sensitivity.** As the highest-beta, longest-duration growth cohort, SMH is acutely sensitive to real yields and risk appetite — it leads on the way up *and* on the way down.

Net: SMH is best understood as **AI super-cycle beta layered on top of the classic silicon cycle**, with NVDA as the dominant swing factor.

## How It Trades vs the Broad Index

SMH is a **high-beta amplifier** of the [[nasdaq-100|Nasdaq-100]] / [[spy|SPY]] tape:

- **Beta typically 1.3-1.5x SPX**, rising in stress; SMH leads the market in AI-driven rallies and falls harder in growth/risk-off selloffs.
- Because NVDA, AVGO, and AMD are themselves large Nasdaq-100 / S&P 500 weights, SMH correlates very highly with [[qqq|QQQ]] and [[xlk|XLK]] — it offers *concentrated leverage to* the megacap-growth complex rather than diversification from it.
- The **SMH/SPY** and **SMH/[[xlk|XLK]]** ratios are watched as AI-leadership gauges; when they rise, the chip complex is leading risk appetite.
- SMH frequently *leads* turns in the broad growth tape — chip strength/weakness is treated as a leading signal for the whole AI trade.

## Seasonality

SMH has no clean calendar edge of its own; its rhythm is set by the **megacap earnings cluster** (the quarterly window around NVDA/AVGO/TSM/AMD reports concentrates volatility four times a year, with NVDA's late-quarter print the marquee event) and by the **industry's order/inventory cadence** plus key catalysts (CES in January, major GPU/architecture launches, hyperscaler capex guidance on big-tech earnings calls). Beyond that it tracks broad large-cap-growth [[seasonality|seasonality]] (Nov-Apr strength, summer softness) because it moves with the growth complex. Treat the *earnings cluster*, not the calendar, as the dominant seasonal feature.

## Notable positioning

- **[[situational-awareness-lp|Situational Awareness LP]]**: $2.04B notional put exposure — the fund's largest single-line position by notional. Held alongside additional single-name puts on NVDA, ORCL, AVGO, AMD, MU, TSM, ASML, INTC totalling ~$5.7-6.5B more — the SMH position is the systemic anchor of the chip-complex short. (Source: [[2026-05-31-aschenbrenner-13f-snapshot]])

## Peer & Related-ETF Comparison

| ETF | Issuer | Universe | Weighting | Concentration | Notes |
|-----|--------|----------|-----------|---------------|-------|
| **SMH** | VanEck | 25 US-listed semis + equip | Cap-weighted (capped) | Top-heavy; NVDA ~20% | Most-traded chip basket; deepest options |
| **SOXX** | iShares | ~30 US semis (ICE Semiconductor index) | Cap-weighted (capped) | Slightly less top-heavy historically | Direct competitor; similar exposure, different index |
| **SOXL / SOXS** | Direxion | 3x leveraged/inverse of semis | Daily-rebalanced | n/a | Leveraged daily traders only; decay risk |
| **[[xlk\|XLK]]** | State Street | S&P 500 technology | Cap-weighted (capped) | Apple/Microsoft/Nvidia | Broad tech, NOT pure semis; software-heavy |
| **[[qqq\|QQQ]]** | Invesco | Nasdaq-100 | Cap-weighted | Megacap growth | Includes semis but diluted by software/comm/consumer |
| **PSI / FTXL** | Invesco | US semis (alt indices) | Various | Varies | Smaller, less liquid chip baskets |

Key distinctions:

- **SMH vs SOXX.** The two are the dominant pure-semiconductor baskets and track each other closely. They differ in index provider (MVIS vs ICE Semiconductor), exact roster, and capping rules; SMH has historically run *slightly more concentrated in the very top names* and carries deeper, more liquid options, which is why it is the preferred institutional short vehicle. SOXX is the natural substitute when an allocator wants near-identical exposure from a different issuer/index.
- **SMH vs [[xlk|XLK]].** XLK is **not** a semiconductor fund — it is the broad S&P 500 *technology* sector, dominated by Apple and Microsoft (software/hardware platforms) with chips as only one component. SMH is a pure, far higher-beta chip play. The **SMH/XLK ratio** isolates "semis vs the rest of tech," a clean read on whether the AI trade is being expressed through silicon or through software/platforms.
- **SMH vs leveraged (SOXL/SOXS).** These are *daily-rebalanced* 3x products with path-dependent decay — tools for short-horizon tactical traders, not buy-and-hold or clean basket-short expression.

## Options Usage

SMH options are **highly liquid** with deep monthly and LEAP chains and active weeklies, making SMH a primary venue for expressing chip-cycle views with defined risk:

- **Basket puts** (the [[situational-awareness-lp|Situational Awareness LP]] use case) capture systemic AI-chip downside without single-name binary risk; LEAP puts mitigate (but don't eliminate) theta drag on a long-horizon bear thesis.
- **Earnings-cluster vol.** Front-month IV bids up into the NVDA/AVGO/TSM/AMD reporting window and crushes afterward — SMH is a classic venue for both event-vol buyers (long the cluster) and post-earnings premium sellers (short the crush).
- **Vol surface** blends the single-name surfaces of its top holdings (NVDA above all), so SMH IV tends to track NVDA's own implied vol and the broader AI-narrative vol cycle.
- **Relative-vol trades.** SMH vs [[xlk|XLK]] or vs [[qqq|QQQ]] options express "semis vol vs broad-tech vol" views.

## Risk profile (if shorting via puts)

- **Chip cycle reacceleration** — NVDA next-gen (Blackwell, Rubin) or unexpected hyperscaler capex re-acceleration crushes put values
- **Implied vol expansion** — SMH IV expansion benefits long-put positions; IV compression hurts them
- **Time decay** — put theta works against long-put holders; LEAP structures mitigate but don't eliminate
- **NVDA single-name effect** — because NVDA is ~20% of SMH, NVDA earnings moves dominate the basket; SMH puts are partially NVDA puts

## Risk profile (if longing as portfolio exposure)

- High beta — typical 1.3-1.5x SPX in stress
- Concentration risk — top 5 names ~50% of basket
- Cyclical earnings — semiconductor revenue is structurally cyclical even in AI bull cycles

## Related

- [[nvidia]] — dominant holding
- [[taiwan-semiconductor-manufacturing]] — major holding
- [[asml-holding]] — major holding
- [[broadcom]], [[amd]], [[micron]], [[intel]] — major holdings
- [[semiconductor-earnings-cycle]] — broader cycle framework
- [[ai-capex-vs-cash-flow-divergence]] — short thesis framework
- [[situational-awareness-lp]] — notable holder (short via puts)
- [[aschenbrenner-bifurcated-ai-thesis]] — thesis using SMH as basket short
- [[xlk]] — broad tech SPDR; semis-vs-rest-of-tech comparison
- [[qqq]] — Nasdaq-100; megacap-growth benchmark SMH amplifies
- [[nasdaq-100]] — index SMH closely tracks at high beta
- [[spy]] — broad benchmark; SMH beta ~1.3-1.5x
- [[hyperscaler-capex]] — AI capex demand driver
- [[seasonality]] — earnings-cluster and calendar context

## Sources

- VanEck SMH product page
- (Source: [[2026-05-31-aschenbrenner-13f-snapshot]])
