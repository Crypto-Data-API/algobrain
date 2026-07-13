---
title: "Applied Digital Corporation"
type: entity
created: 2026-05-31
updated: 2026-06-19
status: excellent
founded: 2001
headquarters: "Dallas, Texas, USA"
tags: [company, stocks, ai-trading, data-center, technology]
entity_type: company
website: "https://www.applieddigital.com"
aliases: ["APLD", "Applied Digital", "Applied Digital Corporation"]
ticker: "APLD"
exchange: "NASDAQ"
sector: "AI Cloud Infrastructure / Data Centers"
industry: "Data Centers"
sp500: false
ai_category: "AI Data Center Infrastructure"
market_cap_tier: "Small / Mid Cap"
related:
  - "[[coreweave]]"
  - "[[nebius-group]]"
  - "[[iren]]"
  - "[[core-scientific]]"
  - "[[ai-data-center-power-demand]]"
  - "[[ai-capex-vs-cash-flow-divergence]]"
  - "[[situational-awareness-lp]]"
---

Applied Digital Corporation (NASDAQ: APLD) is a US-based data centre developer and operator focused on AI / HPC cloud infrastructure, with a particular emphasis on building large-scale low-cost data centre capacity in regions with abundant power. The company originated as a Bitcoin mining hosting business but has progressively pivoted toward AI / HPC hosting as the underlying economics of crypto mining have been overtaken by AI training and inference workloads. As of 2026 Applied Digital is part of the AI-infrastructure-pivot cohort frequently grouped with [[iren|IREN]], [[core-scientific|Core Scientific]], and [[riot-platforms|Riot Platforms]], with the value framing shifting from "Bitcoin miner" to "scarce data centre and power capacity available to AI customers." Applied Digital is a $320M long position in [[situational-awareness-lp|Situational Awareness LP]] per late May 2026 13F filings — sized as a high-conviction expression of the physical-infrastructure-scarcity thesis.

## Why traders care

1. **AI HPC pivot is the value re-rating thesis** — the same physical assets that hosted Bitcoin miners can host GPU clusters, but the lease economics for AI customers are dramatically better (multi-year contracts, higher per-MW revenue, creditworthy hyperscaler counterparties)
2. **Power-scarcity beneficiary** — Applied Digital's existing power contracts at low rates have become structurally more valuable as US grid capacity tightens (see [[ai-data-center-power-demand]])
3. **Customer / contract concentration** — high-leverage to specific anchor-tenant announcements; stock moves materially on each
4. **Capital structure** — has used a mix of debt, equity, and customer prepayments to fund expansion; ongoing dilution / leverage risk is a recurring theme

## Business Model

Applied Digital is the **purest "landlord of compute"** in the listed bitcoin-miner / digital-infrastructure cohort — it has moved furthest away from crypto economics toward data-center leasing:

- **AI/HPC data-center leasing (the core business).** Long-duration (~15-year) leases to AI tenants — chiefly [[coreweave]] — where the tenant supplies the GPUs and Applied Digital supplies the **powered shell, power, and cooling**. Per-MW lease revenue from creditworthy hyperscaler counterparties is high and predictable, which is why the market values APLD on an infrastructure/REIT-style multiple rather than a mining or even a neocloud multiple. APLD is the *landlord*, one layer below the neoclouds ([[coreweave]], [[nebius-group]]) that operate the GPUs. See [[data-center]] and [[ai-data-center-power-demand]].
- **Legacy crypto-mining hosting (residual, being de-emphasized).** APLD originated as a bitcoin-mining *hosting* business; that residual still imports some crypto-cycle torque to the stock, but the value driver is now AI leasing. Because it hosted rather than self-mined at scale, APLD carries **less direct [[bitcoin]] beta** than the mining-heavy peers ([[mara]], [[riot-platforms]], [[hive-digital-technologies]]).
- **The scarce asset: low-cost power + buildable, interconnected land.** APLD's edge is securing abundant, low-rate power and grid interconnects in power-rich regions (e.g., North Dakota's Polaris Forge campuses). In a multi-year interconnection-queue backlog, that capacity is the moat — the reason a former crypto-hosting small-cap can sign multi-hundred-MW, multibillion-dollar leases.

The throughline matches the cohort ([[core-scientific]], [[terawulf]], [[hut-8]], [[iren]], [[mara]], [[hive-digital-technologies]]): convert energized megawatts into long-dated AI leases. APLD's distinctive position is being the **furthest along the pivot with the least crypto residual** — closest to a "pure AI data-center developer."

## Positioning in the AI infrastructure stack

| Layer | Examples |
|---|---|
| Chip designer | [[nvidia\|NVDA]], [[amd\|AMD]] |
| Foundry | [[taiwan-semiconductor-manufacturing\|TSM]] |
| Memory | [[micron\|MU]], [[sandisk\|SNDK]] |
| Hyperscaler | [[microsoft\|MSFT]], [[amazon\|AMZN]], [[alphabet\|GOOGL]] |
| Neocloud (large) | [[coreweave\|CRWV]], [[nebius-group\|NBIS]] |
| **Data centre developer / operator (HPC-pivot)** | **APLD**, [[iren\|IREN]], [[core-scientific\|CORZ]] |
| Power (distributed) | [[bloom-energy\|BE]] |
| Power (utility) | T1 Energy, others |

APLD sits one layer below the neoclouds: it's the **landlord** of compute rather than the operator. Its revenue comes from leasing physical capacity (rack space, power, cooling) rather than directly selling GPU hours.

## Notable holders / public positioning

- **[[situational-awareness-lp|Situational Awareness LP]]**: $320M long position per late May 2026 13F. Sized as part of the HPC-pivot miner basket (with IREN, CORZ, RIOT, HIVE) expressing the physical-infrastructure-scarcity thesis. (Source: [[2026-05-31-aschenbrenner-13f-snapshot]])

## 2025-2026 Developments

- **CoreWeave anchor leases**: in mid-2025 Applied Digital signed ~15-year leases with [[coreweave|CoreWeave]] for the full **400MW Polaris Forge 1** AI-factory campus at Ellendale, North Dakota, later adding a further **150MW**; in late 2025 it announced a ~15-year, ~**200MW** lease with a US investment-grade hyperscaler at the under-construction **Polaris Forge 2** campus (~$5B expected revenue). Total contracted capacity reached **~600MW** with aggregate prospective lease revenue of roughly **$16B**. (Company press releases / SEC 8-Ks, FY2026)
- **First revenue conversion**: Polaris Forge 1 achieved Ready-for-Service on its first 100MW building (ELN-02) in fiscal 2026, with CoreWeave payments (~$85M in the quarter, including fit-out) and initial lease revenue (~$12M partial-quarter) beginning to flow — the key proof point that contracts convert to cash.
- **Financing**: completed a **$2.35B private offering of 9.25% senior secured notes due 2030** to fund ELN-02/ELN-03 construction and repay the SMBC loan, on top of the earlier Macquarie-led financing; leverage and dilution remain the central bear points.
- Market cap roughly **$5-10B as of mid-2026 (approximate)** — the stock re-rated dramatically through 2025 on the CoreWeave leases and remains one of the most volatile AI-infrastructure names.

## Key Financials — as of June 2026 (approximate)

Fiscal year ends May. Revenue is transitioning from legacy crypto-hosting/cloud toward long-duration data-centre leases; reported quarterly revenue in fiscal 2026 was still small (tens of millions) relative to the ~$16B contracted backlog, so the equity trades on backlog conversion and financing terms, not trailing P&L. Heavy interest expense (9.25% notes) and construction capex keep GAAP earnings deeply negative during build-out. Not covered by the stockmarketapi fundamentals feed.

## Competitive Positioning / Peers

Applied Digital sits in the listed bitcoin-miner / digital-infrastructure cohort — names that compete for the same power, land, AI tenants, and capital, and that trade together as a basket. (The stack table above shows APLD's *vertical* position; this table shows its *direct cohort peers*.)

| Company | Ticker | Differentiator | HPC-pivot stage |
|---|---|---|---|
| **Applied Digital** | APLD | Pure data-center developer; CoreWeave anchor at Polaris Forge (~600 MW, ~$16B prospective) | Late (least crypto residual) |
| [[core-scientific]] | CORZ | Largest contracted HPC backlog (CoreWeave ~$10B, take-or-pay) | Late |
| [[terawulf]] | WULF | Low-carbon power; Fluidstack + Google-backstopped leases | Late |
| [[hut-8]] | HUT | Power-origination pipeline; American Bitcoin (ABTC) spin | Mid-to-late |
| [[iren]] | IREN | Australia/US renewable footprint; vertically integrated | Mid-to-late |
| [[mara]] | MARA | Largest hashrate + biggest BTC treasury; Starwood JV | Early-to-mid |
| [[hive-digital-technologies]] | HIVE | Nordic/Paraguay renewable footprint; BUZZ HPC cloud | Mid |
| [[riot-platforms]] | RIOT | Texas-scale mining; ERCOT power credits | Earlier-mid |

APLD's edge versus the cohort is that it is the **closest to a pure AI data-center developer** — least crypto residual, anchored by a marquee [[coreweave]] relationship and a large contracted backlog. Its key relative weakness is **customer concentration** (CoreWeave dominates) and a **levered capital structure** (9.25% notes) — both of which make it more like [[core-scientific]] in profile than the mining-heavy names.

## Bull vs Bear Case

**Bull case**
- Largest prospective lease backlog in the cohort relative to size (~600 MW contracted, ~$16B aggregate prospective revenue) anchored by [[coreweave]] and an investment-grade hyperscaler.
- First revenue conversion is proven: Polaris Forge 1's first 100 MW building (ELN-02) reached Ready-for-Service with CoreWeave payments beginning to flow — the key proof point that contracts become cash.
- Power-scarcity beneficiary: low-rate power contracts and buildable, interconnected land are structurally more valuable as US grid capacity tightens.
- Least crypto-dependent of the cohort — a cleaner AI-infrastructure expression with less [[bitcoin]] drag.

**Bear case**
- Customer concentration: heavy single-tenant exposure to CoreWeave; an anchor-tenant loss or renegotiation could break the thesis.
- Levered, expensive capital structure: $2.35B of 9.25% senior secured notes plus construction capex keep GAAP earnings deeply negative and add real interest expense.
- Backlog-conversion timing risk: most of the ~$16B is prospective; only a small slice is energized and billing.
- Capital intensity → recurring dilution/leverage as more campuses are funded.
- High beta and basket membership: sharp drawdowns in AI risk-off or [[ai-capex-vs-cash-flow-divergence|capex-divergence]] scares.

## Valuation Framework (qualitative)

APLD defies a single multiple; the market weighs several axes (no specific multiples beyond the figures already on this page are asserted here):

- **HPC-contract backlog / per-MW lease value.** The ~600 MW contracted capacity and ~$16B aggregate prospective lease revenue, valued as recurring infrastructure/REIT-style cash flow, are the dominant lens — the core re-rating driver.
- **Backlog conversion (RFS / energized MW).** How fast contracted MW reach Ready-for-Service and begin billing (ELN-02 → ELN-03 → Polaris Forge 2) is the key near-term value catalyst.
- **Power-cost per kWh and land/interconnect access.** Low-rate, abundant, interconnected power is the durable moat and competitiveness lever.
- **Cost and structure of financing.** Because the buildout is debt-heavy (9.25% notes), the *terms* of financing materially affect equity value — lower rates / equity-light funding are re-rating positives.
- **Residual [[bitcoin]] beta.** Small but nonzero — APLD still moves with crypto sentiment despite the AI thesis being the driver.
- **Dilution-adjusted per-share.** With ongoing equity, debt, and customer-prepayment funding, normalize all metrics for the share-count and interest-expense trajectory.

## Trading & Options Playbook

- **AI-infrastructure proxy with thin crypto torque.** APLD trades primarily on AI data-center sentiment and contract/financing headlines, with only residual [[bitcoin]] beta — a cleaner AI expression than the mining-heavy cohort members.
- **Headline-driven, high volatility.** The stock re-rated dramatically through 2025 on the CoreWeave leases and remains one of the most volatile AI-infrastructure names; moves materially on each anchor-tenant or financing announcement. Options exist with elevated [[implied-volatility]]; see [[options-greeks]].
- **Catalysts to trade around:** new/expanded anchor-tenant leases, Ready-for-Service / energization milestones (ELN-02/03, Polaris Forge 2), financing events and rate terms (the 9.25% notes are a key overhang), quarterly results (fiscal-year ends May), and broader AI-capex sentiment.
- **Basket behavior:** moves with [[core-scientific]], [[terawulf]], [[hut-8]], [[iren]], [[mara]], [[hive-digital-technologies]], [[riot-platforms]], and with the neocloud layer ([[coreweave]], [[nebius-group]]); cohort dispersion (lease/conversion leaders vs laggards) is a recurring setup.

## Capital Structure & Dilution Risk

- **Levered, expensive debt.** APLD completed a **$2.35B private offering of 9.25% senior secured notes due 2030** to fund ELN-02/ELN-03 construction and repay the SMBC loan, on top of earlier Macquarie-led financing. High-coupon debt adds real interest expense and is the central bear point.
- **Mixed funding stack.** Beyond the notes, APLD has used **equity issuance and customer prepayments** to fund expansion — each carries dilution or leverage; customer prepayments also deepen tenant dependence.
- **No BTC treasury buffer.** Unlike [[mara]]/[[hut-8]], APLD does not run a strategic BTC reserve, so funding leans entirely on external capital — making the financing calendar and rate environment central swing factors.
- **Implication for traders:** track the financing calendar, note maturities/refinancing, and any new raises alongside RFS/energization milestones; expensive raises or rate-driven overhang are recurring drawdown catalysts, while cheaper refinancing and lease wins are de-risking signals.

## Risk profile

- **Customer concentration**: high single-tenant exposure; anchor tenant loss can break thesis
- **Capital intensity**: like all data centre developers, requires significant capex per MW of capacity
- **HPC-pivot execution risk**: not every Bitcoin mining facility converts cleanly to AI HPC (different power densities, cooling, networking)
- **Crypto crossover**: residual Bitcoin mining exposure means stock can move with crypto sentiment even when the AI thesis is the value driver
- **Same [[ai-capex-vs-cash-flow-divergence|AI capex divergence]] cycle risk** as the broader AI infra cohort

## Related

- [[iren]] — direct peer in HPC-pivot miner basket
- [[core-scientific]] — direct peer (closest profile: pure HPC, levered)
- [[terawulf]] — direct peer (low-carbon power)
- [[hut-8]] — direct peer (power origination)
- [[mara]] — direct peer (mining-heavy, BTC treasury)
- [[hive-digital-technologies]] — direct peer (renewable footprint, BUZZ HPC)
- [[riot-platforms]] — direct peer (more crypto-mining-anchored)
- [[coreweave]] — customer / next layer up
- [[nebius-group]] — peer at the operator layer
- [[bitcoin]] — residual beta driver
- [[data-center]] — infrastructure layer
- [[ai-data-center-power-demand]] — demand-side framework
- [[ai-capex-vs-cash-flow-divergence]] — cycle framework
- [[situational-awareness-lp]] — notable holder
- [[aschenbrenner-bifurcated-ai-thesis]] — thesis that includes APLD long

## Sources

- (Source: [[2026-05-31-aschenbrenner-13f-snapshot]])
- Applied Digital fiscal Q2 2026 results: https://ir.applieddigital.com/news-events/press-releases/detail/142/applied-digital-reports-fiscal-second-quarter-2026-results
- Applied Digital fiscal Q3 2026 results: https://ir.applieddigital.com/news-events/press-releases/detail/148/applied-digital-reports-fiscal-third-quarter-2026-results
- Applied Digital — additional 150MW CoreWeave lease: https://ir.applieddigital.com/news-events/press-releases/detail/128/applied-digital-finalizes-additional-150mw-lease-with
- Verified via Perplexity (sonar) and web search, 2026-06-10
