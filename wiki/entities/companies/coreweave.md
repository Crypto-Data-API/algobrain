---
title: "CoreWeave, Inc."
type: entity
created: 2026-04-13
updated: 2026-06-19
status: excellent
tags: [company, stocks, ai-trading, machine-learning, technology]
entity_type: company
founded: 2017
headquarters: "Livingston, New Jersey, USA"
website: "https://www.coreweave.com"
aliases: ["CRWV", "CoreWeave, Inc.", "Atlantic Crypto"]
ticker: "CRWV"
exchange: "NASDAQ"
sector: "AI Cloud Infrastructure"
industry: "AI Cloud Infrastructure"
sp500: false
ai_category: "AI Cloud Infrastructure"
market_cap_tier: "Large Cap"
related: ["[[ai-trading-overview]]", "[[amazon]]", "[[artificial-intelligence]]", "[[cloud-trading-infrastructure]]", "[[cloudflare]]", "[[datadog]]", "[[microsoft]]", "[[nvidia]]", "[[nvidia-ai]]", "[[supermicro]]", "[[nebius-group]]", "[[ai-capex-vs-cash-flow-divergence]]", "[[ai-microcap-pump-pattern]]"]
---

CoreWeave, Inc. (NASDAQ: CRWV) is an American [[artificial-intelligence|AI]] cloud-computing company specializing in GPU-based infrastructure for AI training and inference workloads. Founded in 2017 by three commodities traders -- Michael Intrator, Brian Venturo, and Brannin McBee -- the company originally operated as Atlantic Crypto, a cryptocurrency mining operation, before pivoting to GPU cloud services in 2019. Headquartered in Livingston, New Jersey, CoreWeave went public on March 28, 2025 in the largest AI-related IPO by amount raised ($1.5B), and operates 32 data centers with approximately 250,000 GPUs. The company's anchor customer is OpenAI, which signed a ~$12B five-year cloud-computing contract with CoreWeave for its [[artificial-intelligence|AI]] infrastructure needs.

## AI Involvement

[[nvidia-ai|GPU]] cloud computing for [[artificial-intelligence|AI]] workloads, OpenAI partner

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: CRWV |
| **AI Category** | AI Cloud Infrastructure |
| **Market Cap Tier** | Large Cap |

## Business Overview

CoreWeave is the leading "neocloud" — a pure-play GPU cloud renting Nvidia compute to AI labs and hyperscalers under long-dated take-or-pay contracts, with a capital model built on debt secured against GPU contracts and data-center assets. [[nvidia]] is simultaneously its key supplier, an equity holder, and (since 2025) a backstop customer. The bear case is the circularity and leverage: massive capex funded by high-cost debt, extreme customer concentration (Microsoft, OpenAI, Meta are the vast majority of committed revenue), and dependence on AI demand staying ahead of depreciation on rapidly-aging GPU fleets.

## Business Model (Detail)

CoreWeave is not diversified across product lines; it is a single, highly specialized engine. The structure that matters is the **financial architecture**, not a segment split:

| Element | Description |
|---|---|
| **Product** | GPU-as-a-service: bare-metal and managed Nvidia clusters (Hopper/Blackwell-class), high-speed networking (InfiniBand), and an orchestration/software layer tuned for AI training and inference |
| **Revenue shape** | Long-dated **take-or-pay** contracts (multi-year) with AI labs and hyperscalers — converts to a large **backlog / RPO** (remaining performance obligations) that anchors the equity story |
| **Cost base** | GPU procurement from [[nvidia]] (largest input), power, data-center leases/build-out, and **interest expense** on the debt used to fund capex |
| **Capital model** | Debt **secured against GPU contracts and assets** (delayed-draw term loans, asset-backed facilities); equity raised at IPO; capex front-loaded ahead of revenue |
| **Key dependency** | The spread between contracted revenue and the combined cost of capital + GPU depreciation must stay positive across the GPU's useful life |

The core economic question: GPUs depreciate fast (and face residual-value risk at each [[nvidia]] product-cycle transition), while the debt funding them is fixed and high-cost. The model works only if AI compute demand — and the contracted rates — stay ahead of depreciation and interest.

## Competitive Positioning / Peers

CoreWeave competes against both the hyperscaler in-house clouds and a cohort of other "neoclouds."

| Company | Relationship to CRWV | Axis |
|---|---|---|
| [[nebius-group]] | Closest listed peer — a cash-funded neocloud alternative | GPU cloud, but lower leverage |
| [[microsoft]] / Azure | Largest *customer* and a hyperscaler *competitor* | Frenemy: buys capacity yet builds its own |
| [[amazon]] AWS / Google Cloud | Hyperscaler rivals with in-house AI clouds | Scale, integration, balance sheet |
| [[oracle]] (OCI) | Competing AI-cloud capacity provider | Large AI-infra contracts |
| [[core-scientific]] | Data-center landlord / hosting (rejected ~$9B acquisition) | Power + hosting supply chain |
| [[iren]] / [[applied-digital]] | Smaller power/data-center-to-GPU-cloud converts | Capacity and power |
| [[supermicro]] | Hardware supplier to the ecosystem | Server hardware |

CoreWeave's edge is being **first and biggest** in pure-play GPU cloud with deep [[nvidia]] alignment (early access to new GPUs, equity tie). Its structural vulnerability versus hyperscalers is the balance sheet: rivals fund AI capex from operating cash flow, while CoreWeave funds it with leverage.

## Bull vs Bear Case

**Bull case**
- **Backlog** of ~$99B (RPO) provides multi-year contracted revenue visibility, dominated by creditworthy counterparties (Microsoft, OpenAI, Meta).
- Fastest cloud provider in history to $5B annual revenue; +112% YoY growth in Q1 2026.
- **Nvidia alignment** — early GPU access, capacity backstop, and equity stake.
- Pure-play exposure to the secular AI-compute demand wave; take-or-pay contracts de-risk utilization.
- Adjusted EBITDA margin ~60% shows the unit economics can work at scale.

**Bear case**
- **Leverage**: debt-to-equity ~4.5x; a ~$4.2B principal repayment due late 2026 makes refinancing terms a live risk.
- **Customer concentration**: a handful of customers are the vast majority of committed revenue.
- **Circularity**: [[nvidia]] is supplier, shareholder, and backstop customer — see [[ai-capex-vs-cash-flow-divergence]].
- **GPU depreciation / residual-value risk** at each Nvidia product-cycle transition (Hopper → Blackwell → next).
- GAAP net loss ($1.17B in FY2025); margins compressing as scale-up costs and interest bite.
- Highly sensitive to any cooling in AI-capex sentiment.

## Valuation Framework (Qualitative)

CoreWeave is valued on the tension between **AI-compute backlog** and **balance-sheet risk** — the two poles of the equity. Drivers of the multiple:

1. **Backlog / RPO growth and quality** — the headline bull metric; the market underwrites contracted revenue and the credit of the counterparties behind it.
2. **Capex-to-revenue conversion** — how efficiently front-loaded capex turns into recognized revenue and EBITDA; utilization of contracted capacity.
3. **Cost of capital & leverage** — debt-to-equity (~4.5x) and the late-2026 ~$4.2B maturity; refinancing rates directly hit the equity's discount rate and viability.
4. **GPU depreciation schedule vs contract life** — residual-value risk at each Nvidia transition is the hidden variable in the EBITDA-to-cash bridge.
5. **AI-capex sentiment beta** — as the purest listed AI-compute proxy, the multiple expands and contracts with the broader AI-spend narrative far more than with company-specific fundamentals.

The central debate is whether to value CoreWeave on its $99B backlog (growth/infra multiple) or on its leverage and cash-burn profile (distressed/credit lens). See [[ai-capex-vs-cash-flow-divergence]] for the framework and [[discounted-cash-flow]] for the discount-rate sensitivity.

## Capital Return

CoreWeave returns no capital to shareholders — no dividend, no buyback. It is in an intensive capital-*deployment* phase: essentially all cash plus substantial debt is directed into GPU procurement and data-center build-out. The relevant capital-markets variable is the opposite of return — **dilution and refinancing**: convertible/debt raises and the late-2026 maturity are recurring supply and risk events.

## Key financials — as of June 2026 (approximate)

*Not covered by the stockmarketapi fundamentals feed (non-S&P-500). Figures from company reports:*

- **FY2025 revenue:** **$5.13B** (vs $1.92B in 2024) — the fastest cloud provider in history to reach $5B annual revenue. GAAP net loss $1.17B; adjusted EBITDA ~$3.1B (~60% margin).
- **Backlog:** $66.8B at end-2025 (>4x the start of year); **$99.4B revenue backlog / $98.8B RPO after Q1 2026**.
- **Q1 2026 (reported 7 May 2026):** revenue **$2.08B, +112% YoY**, beating consensus (~$1.97B); margins compressing as scale-up costs and interest expense bite.
- **Capacity:** >850 MW active power (added 260 MW in 2025); ~3.1 GW total contracted power.
- **Leverage:** debt-to-equity around 4.5x; a ~$4.2B principal repayment falls due in late 2026 — roughly the company's cash plus one quarter of revenue, making refinancing terms a live risk factor.

## 2025–2026 Developments

- **28 March 2025:** IPO at $40/share (below the indicated range), raising ~$1.5B — the largest AI-related IPO by proceeds; the stock was extremely volatile through 2025 (multi-fold rally post-IPO, then deep drawdowns on dilution/debt concerns).
- **2025 contract wins:** OpenAI commitments expanded to roughly **$22.4B** total; **Meta signed commitments of up to ~$35.2B** if fully utilized; Microsoft remained the largest revenue contributor; Nvidia provided a capacity backstop agreement.
- **October 2025:** Core Scientific shareholders **rejected CoreWeave's ~$9B all-stock acquisition**; CoreWeave instead exercised its final ~120 MW hosting option with [[core-scientific]], keeping the landlord relationship contractual rather than owned.
- **26 February 2026:** FY2025 results — $5.13B revenue, $66.8B backlog.
- **7 May 2026:** Q1 2026 beat with backlog jumping to $99.4B on the Meta/OpenAI expansions; stock rose on the print but remains hostage to AI-capex sentiment and its 2026 debt maturities.

## Trading Relevance

- **Profile:** the purest listed expression of AI-compute demand — extremely high beta to AI capex headlines, Nvidia results, and OpenAI/Meta spending news. High short interest and elevated implied volatility since IPO; lock-up expiries and convert/debt raises have been recurring supply events.
- **Catalysts:** quarterly earnings (Feb/May/Aug/Nov), new hyperscaler/AI-lab contracts, the late-2026 $4.2B debt repayment/refinancing, Nvidia product-cycle transitions (GPU residual-value risk), any revival of data-center M&A.
- **Bull/bear hinge:** backlog ($99B) vs balance sheet (4.5x D/E) — see [[ai-capex-vs-cash-flow-divergence]] for the framework.
- **Correlated names:** [[nvidia]], [[nebius-group]], [[core-scientific]], [[iren]], [[applied-digital]], [[supermicro]], [[microsoft]], [[oracle]].

## Trading & Options Playbook

- **Catalyst calendar**: quarterly earnings (≈Feb / May / Aug / Nov) — focus on backlog/RPO, revenue growth, margin trajectory, and balance-sheet/leverage updates. Major non-earnings movers: new hyperscaler/AI-lab contract announcements, [[nvidia]] results and product-cycle transitions (GPU residual-value read-through), the late-2026 ~$4.2B debt repayment/refinancing, lock-up expiries, convert/debt raises, and any data-center M&A revival.
- **Index & ETF membership**: lists on [[nasdaq]]; a recent IPO, so index inclusion is still maturing. Appears in AI-infrastructure and some thematic baskets; the file records CRWV as **not** an [[s-and-p-500]] member. Tracks AI-theme ETFs and trades with the [[smh-vaneck-semiconductor-etf]] / [[qqq]] complex on a beta basis.
- **Volatility behavior**: the purest listed expression of AI-compute demand — extremely high beta to AI-capex headlines and [[nvidia]] news. High short interest and elevated [[implied-volatility]] since IPO; supply events (lock-ups, converts, debt raises) produce sharp dislocations.
- **Setups to know**: event-driven trades around contract wins and debt-maturity news, AI-theme beta alongside [[nvidia]], and earnings volatility plays given the wide expected move.

## Risks

- **Leverage & refinancing** — ~4.5x debt-to-equity and a ~$4.2B late-2026 maturity; refinancing terms are a live solvency-adjacent risk.
- **Customer concentration** — a few customers (Microsoft, OpenAI, Meta) are the vast majority of committed revenue.
- **Circularity** — [[nvidia]] as supplier + shareholder + backstop customer; see [[ai-capex-vs-cash-flow-divergence]].
- **GPU depreciation / residual-value** risk at each Nvidia product-cycle transition.
- **AI-capex sentiment** — high beta to any cooling in the AI-spend narrative.
- **Dilution** — recurring convert/debt/equity raises.
- **Power & data-center supply** — dependence on contracted power and landlords (e.g., [[core-scientific]]).

## Related

- [[artificial-intelligence]]
- [[ai-trading-overview]]
- [[amazon]]
- [[cloud-trading-infrastructure]]
- [[cloudflare]]
- [[datadog]]
- [[microsoft]]
- [[nvidia]]
- [[nvidia-ai]]
- [[supermicro]]
- [[mongodb]]
- [[gitlab]]
- [[nebius-group]] — closest publicly-listed peer (cash-funded neocloud alternative)
- [[ai-capex-vs-cash-flow-divergence]] — framework for cycle outcomes
- [[ai-microcap-pump-pattern]] — counter-example pattern (CRWV is the legitimate real-business comp)

- [[core-scientific]]
- [[oracle]]
- [[iren]]
- [[applied-digital]]
- [[nasdaq]]
- [[s-and-p-500]]
- [[smh-vaneck-semiconductor-etf]]
- [[qqq]]
- [[implied-volatility]]
- [[technology]]

## Sources

- (Source: [[stockmarketapi-ai-stocks-2026-04-13]])
- [CoreWeave reports strong Q4 and fiscal year 2025 results (26 Feb 2026)](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Fourth-Quarter-and-Fiscal-Year-2025-Results/)
- [CoreWeave reports strong first quarter 2026 results (7 May 2026)](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-First-Quarter-2026-Results/)
- [CNBC — CoreWeave (CRWV) Q1 2026 earnings report](https://www.cnbc.com/2026/05/07/coreweave-crwv-q1-earnings-report-2026.html)
- [Investing.com — CoreWeave Q1 2026 slides: revenue surges 112% as margins compress](https://www.investing.com/news/company-news/coreweave-q1-2026-slides-revenue-surges-112-as-profit-margins-compress-93CH-4671014)
- [Yahoo Finance — CoreWeave reports 2025 revenue of $5.13B with $66.8B backlog](https://finance.yahoo.com/news/coreweave-crwv-reports-2025-revenue-195641826.html)
- Verified via Perplexity (sonar) and web search, 2026-06-10
