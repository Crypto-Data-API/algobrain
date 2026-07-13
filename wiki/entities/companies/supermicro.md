---
title: Supermicro
type: entity
created: 2026-04-13
updated: 2026-06-18
status: excellent
tags: [company, sp500, stocks, technology, ai-trading, machine-learning, volatility]
entity_type: company
aliases: ["SMCI", "Super Micro Computer", "Super Micro Computer Inc."]
headquarters: San Jose, California, USA
website: "https://www.supermicro.com"
ticker: SMCI
exchange: NASDAQ
sector: Information Technology
sp500: true
related: ["[[s-and-p-500]]", "[[technology]]", "[[artificial-intelligence]]", "[[ai-trading-overview]]", "[[nvidia]]", "[[dell-technologies]]"]
founded: 1993
industry: Technology Hardware, Storage & Peripherals
ai_category: "AI Server Infrastructure"
market_cap_tier: "Mid Cap"
fundamentals_updated: 2026-06-10
fundamentals_period_end: 2025-06-30
fundamentals_source: stockmarketapi
pe_ratio: 24.19
ebitda_margin_5y_avg: 0.0729
roe_5y_avg: 0.2012
roa_5y_avg: 0.101
data_completeness_pct: 100
fred_profile: Mixed-quality
---

Super Micro Computer (NASDAQ: SMCI) designs and builds high-performance servers, storage, and rack-scale systems, and has become one of the dominant integrators of AI compute infrastructure — particularly liquid-cooled, [[nvidia]] GPU-based rack systems for hyperscale and enterprise data centers. For traders, SMCI is a high-beta, headline-driven AI proxy with a turbulent recent history: explosive AI-server revenue growth collided in 2024-2025 with a short-seller report, a delayed annual filing, an auditor resignation, and a brush with Nasdaq delisting (since resolved). It is a constituent of the [[s-and-p-500]] index in the [[technology|Information Technology]] sector and a core expression of the [[ai-trading-overview|AI-capex trade]].

## AI Involvement

[[artificial-intelligence|AI]] server and rack-scale solutions for data centers — Supermicro is a leading integrator of [[nvidia]] HGX/GB200/Blackwell GPU systems, with a particular edge in liquid-cooled "rack-scale" deployments shipped at volume. As rack power densities climb past the limits of air cooling, SMCI's direct-liquid-cooling (DLC) systems make it a direct beneficiary of [[ai-data-center-power-demand|AI data-center power demand]].

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: SMCI |
| **Sector** | [[technology|Information Technology]] |
| **Industry** | Technology Hardware, Storage & Peripherals |
| **Founded** | 1993 (Charles Liang, who remains CEO) |
| **Headquarters** | San Jose, California |
| **CIK** | 0001375365 |
| **Fiscal year end** | June 30 |
| **FY2025 revenue** | ~$23.5-25B (guided range) |
| **FY2026 revenue target** | at least $36B |

## Business Overview & Segments

Supermicro sells server and storage "building blocks" — a modular, configure-to-order (CTO) approach that lets it bring new CPU/GPU generations to market faster than larger rivals. Its edge is **time-to-market and density**: it was early and aggressive on liquid cooling, which is increasingly mandatory for high-power AI racks. Revenue today is dominated by AI/GPU server systems, with significant **customer concentration** (a handful of large AI buyers can swing a quarter) and **supplier concentration** (the business is gated by its [[nvidia]] GPU allocation). The structural tension is margin: gross margins are thin (~11%) and have been falling under competitive pressure — SMCI is a high-volume integrator, not a high-margin IP owner.

| Line of business | What it is | Revenue mix (qualitative) |
|---|---|---|
| **AI / GPU server systems** | [[nvidia]] HGX/GB200/Blackwell GPU servers and complete AI compute platforms | Dominant — the overwhelming majority of revenue and the entire growth story |
| **Rack-scale & liquid-cooled (DLC) solutions** | Full integrated racks with direct-liquid-cooling, plant-side coolant distribution, shipped at volume | Fast-growing, the key differentiator; "rack-scale" sells systems, not boxes |
| **General-purpose servers & storage** | Mainstream x86 servers, storage and edge "building blocks" via the modular CTO model | The historical core; now a minority next to AI systems |
| **Components, software & services** | Motherboards, subsystems, management software, deployment/support services | Small attach; supports the integration model |

The "building-block" architecture — standardized, swappable subsystems — is what lets Supermicro field a new GPU platform quickly, but it is replicable engineering rather than a deep proprietary moat.

## Economic Moat & Competitive Position

Supermicro's [[economic-moat|economic moat]] is **narrow and contested**. The advantages are real but shallow and time-limited:

- **Time-to-market** — the modular building-block design lets SMCI ship new [[nvidia]] GPU generations earlier than most rivals, capturing the high-price early window of each product cycle.
- **Liquid-cooling / density lead** — an early, at-volume position in direct-liquid-cooled rack-scale systems, the increasingly mandatory format for high-power AI racks.
- **Engineering velocity & customization** — a deep SKU catalog and configure-to-order flexibility that hyperscalers and neoclouds value.

What it is **not**: SMCI does not own a high-margin software ecosystem or proprietary silicon. It is a **volume integrator** whose key input ([[nvidia]] GPUs) and key differentiator (rack engineering) are both available to well-capitalized competitors. [[dell-technologies|Dell]] and HPE have moved aggressively into AI servers with stronger balance sheets, enterprise sales channels, and their own liquid-cooling designs; [[nvidia]] itself sells reference DGX systems. The thin (~11%) and falling gross margin is the financial signature of a moat under pressure — the lead is in execution speed, not durable pricing power, so the position must be re-earned every product cycle.

## Competitors / Peer Set

| Company | Primary battleground | Notes |
|---|---|---|
| [[dell-technologies]] | AI servers / rack-scale | Largest direct rival; stronger balance sheet, enterprise channel, and its own liquid-cooling and integration scale |
| HPE (Hewlett Packard Enterprise) | AI servers, HPC | Cray-derived HPC heritage; pushing AI systems and DLC; deep enterprise relationships |
| [[nvidia]] | GPU supplier — and occasional competitor | Gates SMCI via GPU allocation; also sells reference DGX systems that compete at the high end |
| [[arista-networks]] | AI networking adjacency | Not a server rival but a peer in the AI data-center buildout; correlated read-through |
| ODMs (Quanta, Wiwynn, Foxconn) | White-box / direct-to-hyperscaler | Taiwanese original-design manufacturers that build for hyperscalers directly, the low-cost commoditization threat |

Supermicro competes on speed and configuration breadth rather than premium economics; the watch item is margin compression as larger and lower-cost players crowd the same AI-server demand.

## Growth Drivers & Catalysts

- **AI data-center capex super-cycle** — SMCI revenue is effectively a derivative of hyperscaler, neocloud, and enterprise AI spending; demand tracks the [[ai-trading-overview|AI-capex theme]] directly.
- **[[nvidia]] product cadence** — each Blackwell → Blackwell Ultra → Rubin transition resets system value and pricing; SMCI's early-shipping advantage matters most at each launch.
- **Liquid cooling becoming mandatory** — as rack power climbs, air cooling fails; DLC adoption is a structural tailwind tied to [[ai-data-center-power-demand]].
- **FY2026 scale target** — management has guided to at least **$36B** FY2026 revenue, citing a rapidly expanding order book including **$13B+** of Nvidia Blackwell Ultra orders, with Blackwell-based systems fully available.
- **Recurring catalysts** — quarterly results and guidance, Nvidia GPU-allocation news, margin commentary, liquid-cooling adoption data points, and any governance/legal update.

## Bull Case vs Bear Case

### Bull case
- Pure-play, at-scale exposure to the AI data-center buildout with a genuine early-mover lead in liquid-cooled rack-scale systems.
- FY2026 guidance to at least $36B revenue and a multi-billion Blackwell Ultra order book imply the AI-server volume story is intact.
- The 2024-25 accounting overhang has been resolved (delinquent 10-K filed, new auditor, delisting avoided), removing an existential tail risk.
- Asset-light, configure-to-order model scales revenue fast as each new [[nvidia]] generation ships.

### Bear case
- **Governance & legal:** the 2024 Hindenburg short report, EY auditor resignation, delayed annual filing, and the **March 2026 DOJ indictment** of co-founder Wally Liaw over alleged chip-smuggling keep a credibility discount on the stock.
- **Margin compression:** ~11% and falling gross margins reveal a commoditizing, capital-intensive integration business with little pricing power against [[dell-technologies|Dell]]/HPE/ODMs.
- **Dependence:** revenue is gated by [[nvidia]] GPU allocation and concentrated among a few large customers — either can swing a quarter.
- **Volatility:** an extremely high-beta, heavily-shorted name where headlines, not fundamentals, often set the price.

## Key Risks

- **Governance / accounting history** — the 2024 Hindenburg short report, the resignation of auditor EY, the delayed 10-K, and the brush with Nasdaq delisting (resolved Feb 2025 with new auditor BDO) left a lasting credibility discount; the **March 2026 DOJ indictment** of co-founder Yih-Shyan "Wally" Liaw and two others for allegedly conspiring to smuggle ~$2.5B of Nvidia-chip AI servers to China is a fresh, live legal overhang.
- **Thin & falling margins / commoditization** — ~11% gross margin under pressure from [[dell-technologies|Dell]], HPE, and ODMs; the integration model has limited defenses against price competition.
- **[[nvidia]] GPU-allocation dependence** — shipments are capped by GPU supply; any reallocation directly throttles revenue.
- **Customer concentration** — a small number of large AI buyers drive a large share of revenue; order timing alone can miss or beat a quarter.
- **Extreme volatility & short interest** — one of the most heavily shorted, most violently moving AI names; gap and squeeze risk in both directions.
- **AI-capex cyclicality** — a synchronized hyperscaler/neocloud capex pause would hit volumes and the multiple together.

## Valuation & How the Stock Trades

Supermicro trades less on a steady-state earnings multiple than on AI-capex sentiment and headline flow; the data block above shows thin (~11%) and falling gross margins and only mid-single-digit operating/net margins, the financial signature of a commoditizing integrator rather than a high-margin compounder. Mechanically:

- **Very high beta** — among the most volatile S&P 500 members; an amplified expression of the AI-capex trade that moves violently on [[nvidia]] GPU-allocation news, margin commentary, and governance/legal headlines.
- **Heavily shorted** — persistently one of the most-shorted AI names, which adds squeeze risk on top of fundamental moves.
- **Extremely liquid options with elevated IV** — popular for earnings and event plays; headline risk makes naked positions hazardous and implied vol stays structurally high.
- **Headline-driven gap risk** — filing/governance/legal news, guidance revisions, and Nvidia product-cycle timing routinely gap the stock double digits.
- **No dividend** — there is no capital-return cushion; total return is entirely price (the data block shows no dividend per share).

## Notable History & Milestones

| Year | Milestone |
|---|---|
| 1993 | Founded in San Jose by Charles Liang (still CEO) on a modular "building-block" server design |
| 2007 | IPO on Nasdaq |
| 2018-2020 | Temporary Nasdaq compliance issues over delayed filings; later regained compliance |
| 2023-24 | AI-server revenue explodes as liquid-cooled [[nvidia]] GPU racks ship at volume |
| 2024 | Added to the [[s-and-p-500]]; then hit by a Hindenburg short report, EY auditor resignation, and a delayed annual 10-K |
| Feb 2025 | Filed delinquent 10-K with new auditor BDO; avoided Nasdaq delisting, lifting the existential overhang |
| 2025-26 | FY2025 guidance trimmed to ~$23.5-25B on timing/margin pressure; FY2026 guided to at least $36B on a $13B+ Blackwell Ultra order book |
| Mar 2026 | DOJ indicts co-founder Wally Liaw and two others over alleged ~$2.5B Nvidia-server smuggling to China — a fresh governance/legal overhang |


## Fundamentals

*Source: [[stockmarketapi-fundamentals-2026-05-10]] · period end 2025-06-30 · primary sec_edgar · completeness 100% · pulled 2026-06-10*

### Snapshot

| Metric | Latest | 5y avg | Note |
|---|---|---|---|
| PE ratio | 24.2x | — | compare to sector / index avg |
| Gross margin | 11.1% | 14.6% | trend matters — rising = pricing power |
| Operating margin | 5.7% | 6.9% | — |
| EBITDA margin | 5.9% | 7.3% | >20% strong; >27% Fred's 'excellent' tier |
| Net margin | 4.8% | 6.0% | — |
| ROE | 16.6% | 20.1% | API uses book equity — high values reflect leverage / buybacks |
| ROA | 7.5% | 10.1% | Fred's bar: ≥5% |
| Debt-to-equity | — | — | Fred: <1.0 healthy, >2.0 leveraged (sector-adjusted) |
| Liabilities-to-equity | 1.22x | — | broader leverage |
| Current ratio | 5.25x | — | Fred: >2.0 (N/A for retail / staples / banks) |
| Quick ratio | 3.25x | — | Fred: >1.0 |
| Interest coverage | — (not in source) | — | Fred: <1.5 dangerous, >3.0 comfortable |
| EPS (diluted) | 1.68 | — | — |
| Dividend per share | — | — | — |
| Dividend yield (API) | — | — | API definition — see source page; not directly = market yield |
| Dividend payout | — | — | — |
| GMROI | 51.9 | — | Retail-only — Fred's bar: >100 |

### 5-period trend

| Period | EBITDA margin | Operating margin | ROE | D/E |
|---|---|---|---|---|
| 2025-06-30 (FY) | 5.9% | 5.7% | 16.6% | — |
| 2024-06-30 (FY) | 8.3% | 8.1% | 21.3% | — |
| 2023-06-30 (FY) | 11.1% | 10.7% | 32.5% | 0.15x |
| 2022-06-30 (FY) | 6.9% | 6.5% | 20.0% | 0.42x |
| 2021-06-30 (FY) | 4.3% | 3.5% | 10.2% | 0.09x |

### Fred-framework view

**Profile:** *Mixed-quality* — passes 4/6 of Fred's hurdles.

| Bar | Result | Value |
|---|---|---|
| ROA ≥5% | ✓ | 10.1% |
| ROE ≥15% | ✓ | 20.1% |
| Net margin ≥10% | ✗ | 4.8% |
| EBITDA margin ≥20% | ✗ | 7.3% |
| Current ratio ≥2 | ✓ | 5.25x |
| Quick ratio ≥1 | ✓ | 3.25x |

- **Suits:** investors who weight specific bull-case metrics and accept failures elsewhere
- **Watch for:** the failed Fred bars listed below — each is a known-risk vector, not a quirk
- **Sector context:** Information Technology — Fred's standard bars apply (D/E <1.0, current >2, interest coverage >3x).

## Related

- [[s-and-p-500]]
- [[technology|Information Technology]]
- [[artificial-intelligence]]
- [[ai-trading-overview]]
- [[ai-data-center-power-demand]]
- [[economic-moat]]
- [[nvidia]]
- [[dell-technologies]]
- [[arista-networks]]
- [[apple]]
- [[analog-devices]]

## Sources

- (Source: [[stockmarketapi-sp500-2026-04-13]])
- [Supermicro Q1 FY2026 financial results](https://ir.supermicro.com/news/news-details/2025/Supermicro-Announces-First-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx)
- [Super Micro stock surges on 2026 targets, avoids delisting](https://finance.yahoo.com/news/super-micro-stock-surges-after-outlining-ambitious-2026-targets-assuring-investors-it-will-avoid-delisting-131411657.html)
- [Company website](https://www.supermicro.com)
- Verified via WebSearch, 2026-06-10
