---
title: "Akamai Technologies"
type: entity
created: 2026-04-13
updated: 2026-06-17
status: excellent
tags: [company, sp500, stocks]
entity_type: company
aliases: ["AKAM", "Akamai"]
headquarters: "Cambridge, Massachusetts"
ticker: "AKAM"
exchange: "NASDAQ"
sector: "Information Technology"
sp500: true
related: ["[[s-and-p-500]]", "[[technology]]", "[[cloudflare]]", "[[fastly]]", "[[alphabet]]", "[[amazon]]", "[[microsoft]]", "[[artificial-intelligence]]"]
founded: 1998
industry: "Internet Services & Infrastructure"
website: "https://www.akamai.com"
fundamentals_updated: 2026-06-10
fundamentals_period_end: 2024-12-31
fundamentals_source: stockmarketapi
pe_ratio: 42.14
ebitda_margin_5y_avg: 0.9595
roe_5y_avg: 0.0629
roa_5y_avg: 0.0308
data_completeness_pct: 100
fred_profile: Mixed-quality
---

Akamai Technologies (NASDAQ: AKAM) is the world's largest and oldest content delivery network (CDN) and cybersecurity company. Founded in 1998 at MIT, Akamai pioneered the commercial CDN model and today delivers 15-30% of all web traffic globally. The company has pivoted from pure content delivery toward a security-first edge platform, with security now comprising over 50% of revenue. It is a constituent of the [[s-and-p-500]] index.

---

## Business Segments

### Security Technology (~55% of Revenue)

Security is Akamai's growth engine and the strategic focus of the company. Products include:

- **Web Application Firewall (WAF)** — Enterprise-grade WAF with industry-leading detection accuracy (~100% in some benchmarks vs [[cloudflare]]'s ~69%)
- **DDoS Mitigation** — Prolexic platform for network-layer DDoS protection
- **Bot Management** — Behavioral bot detection and mitigation
- **API Security** — Protecting API endpoints (bolstered by Neosec acquisition)
- **Zero Trust / Microsegmentation** — Guardicore acquisition (2021) provides east-west traffic segmentation within data centres, a key zero-trust capability
- **Account Protector** — Credential stuffing and account takeover prevention

### Delivery (~30% of Revenue)

The legacy CDN business that built Akamai. This segment is mature and declining as CDN commoditises:

- **Media Delivery** — Video streaming delivery (OTT platforms, live sports, software downloads)
- **Web Performance** — Website acceleration, dynamic site acceleration
- **Download Delivery** — Large file and software distribution
- **NetStorage** — Cloud-based content storage

This segment faces pricing pressure from [[cloudflare]] (aggressive free-tier and lower pricing), AWS CloudFront (ecosystem lock-in), and the general commoditisation of static content delivery.

### Compute (~15% of Revenue)

Akamai's newest strategic pillar, built through acquisition:

- **Linode** — Acquired in 2022 for $900M. Cloud computing platform competing with AWS, Azure, and GCP at the lower end of the market. Provides VMs, Kubernetes, block storage, and object storage.
- **Connected Cloud** — Akamai's vision of distributed cloud computing combining Linode's IaaS with Akamai's 4,300+ edge locations
- **Edge Compute** — Serverless compute at the edge, similar to [[cloudflare]]'s Workers

---

## Economic Moat & Competitive Position

Akamai's [[economic-moat|economic moat]] is **narrow-to-moderate** and shifting in character as the business mix moves from commoditising delivery toward security and compute:

- **Edge-network scale** — one of the largest distributed networks in the world (4,300+ PoPs across ~135 countries, embedded deep inside carrier and ISP networks). Reproducing this physical footprint is capital- and relationship-intensive, and it is the asset Akamai is now repurposing for low-latency AI inference.
- **Enterprise switching costs** — large media, commerce, and financial-services customers run mission-critical delivery and security on Akamai with deep integrations, custom rules, and long procurement cycles; rip-and-replace is disruptive and risky, giving sticky, contracted revenue.
- **WAF detection accuracy / security reputation** — Akamai's web-application-firewall and DDoS (Prolexic) products are regarded as best-in-class for accuracy in enterprise benchmarks, a credibility moat in security where false negatives are costly.
- **Threat-intelligence flywheel** — sitting in front of 15-30% of web traffic gives Akamai a large, real-time view of attacks that feeds its security models — a data advantage rivals struggle to match at scale.

The moat is **eroding on the delivery side** (CDN is commoditising under [[cloudflare]]'s free-tier pricing and hyperscaler bundling) while Akamai tries to **rebuild it on the security and compute side**, where margins are higher and contracts stickier. The whole investment case is whether the security/compute moat widens faster than the delivery moat decays.

---

## History and Significance

| Date | Event |
|---|---|
| **1998** | Founded by Tom Leighton (MIT professor) and Danny Lewin (MIT grad student) based on applied mathematics for solving internet congestion |
| **1999** | IPO during dot-com boom |
| **Sep 2001** | Co-founder Danny Lewin killed on American Airlines Flight 11 on September 11 — reportedly the first victim of the hijacking. Lewin, a former Israeli military officer, is believed to have attempted to stop the hijackers. |
| **2001-2003** | Survived dot-com bust; CDN demand grew as broadband adoption increased |
| **2012** | Acquired Prolexic Technologies for $370M (DDoS mitigation) — beginning of security pivot |
| **2017** | Acquired Nominum (DNS security) |
| **2021** | Acquired Guardicore for ~$600M (microsegmentation / zero trust) |
| **2022** | Acquired Linode for $900M (cloud computing) — most significant strategic bet |
| **2023** | Acquired Neosec (API security) |
| **2024-2025** | Continued integration of Linode into "Akamai Connected Cloud" platform |
| **2025-2026** | Pivot to AI inference at the edge; cloud infrastructure becomes the growth engine alongside security |

### The Danny Lewin Story

Danny Lewin's death on 9/11 is one of the most poignant stories in technology history. A dual Israeli-American citizen and former member of the Israeli Defence Forces' elite Sayeret Matkal unit, Lewin was seated in business class on Flight 11. According to FAA documents and flight attendant communications, Lewin was likely the first person killed in the hijacking — possibly while attempting to intervene. He was 31 years old. The company he co-founded now handles 15-30% of all internet traffic.

### Name Origin

The company name "Akamai" comes from the Hawaiian word meaning "intelligent," "clever," or "cool." This reflects the company's MIT mathematical origins — Akamai's founding insight was using algorithms to intelligently route internet traffic around congestion.

---

## 2025-2026 Developments

- **FY2025 revenue ~$4.21B** with the long-running mix shift intact: security and compute growth offsetting delivery decline; ~11,400 employees.
- **Q1 2026 (reported May 2026): revenue $1.074B, +6% YoY** — Security +11% YoY to $590M, Cloud Infrastructure Services +40% YoY to $95M, Delivery -7% YoY. The compute bet is finally showing up in the growth algorithm.
- **$1.8B, seven-year AI compute commitment** disclosed alongside Q1 2026 — a major customer commitment for AI inference capacity on Akamai's distributed cloud, strengthening the "edge AI inference" narrative and re-rating the stock from pure value toward AI infrastructure.
- Strategy under CEO Tom Leighton: position the 4,300+ PoP edge network for low-latency AI inference workloads where centralized hyperscaler regions are disadvantaged.

---

## Growth Drivers & Catalysts

- **Security mix shift** — security is now ~55% of revenue and growing double digits (WAF, Prolexic DDoS, bot management, API security, Guardicore microsegmentation/zero-trust). Each point of mix shift toward security lifts the blended growth rate and margin.
- **Cloud / compute ramp** — Connected Cloud (Linode IaaS + edge) is the fastest-growing segment (Cloud Infrastructure Services +40% YoY in Q1 2026), turning a legacy CDN into a distributed-cloud and edge-AI story. The **$1.8B, seven-year AI compute commitment** disclosed with Q1 2026 is the clearest catalyst re-rating the stock from "value" toward "AI infrastructure."
- **Edge AI inference** — the thesis that latency-sensitive inference wants to run close to users, where Akamai's 4,300+ PoP footprint beats centralized hyperscaler regions.
- **Margin expansion** — security and compute carry better unit economics than commodity delivery; continued mix shift plus buybacks support EPS even on modest top-line growth.
- **M&A optionality** — Akamai has reliably bought into new TAMs (Prolexic, Guardicore, Linode, Neosec) and could continue to.
- **Recurring catalysts** — quarterly earnings and the security/compute vs delivery growth split, AI-compute commitment disclosures, buyback cadence, and read-throughs from [[cloudflare]]/[[fastly]] prints on CDN and edge demand.

---

## Bull Case vs Bear Case

### Bull case
- The security + compute mix shift re-accelerates the growth algorithm and expands margins, turning a low-single-digit grower into a high-single-digit one.
- The 4,300+ PoP edge network is a genuinely scarce asset for low-latency AI inference; the $1.8B AI compute commitment validates demand and the stock re-rates from value toward AI infrastructure.
- Strong, durable free cash flow and buybacks compound EPS even with modest revenue growth — a cheap way to own the edge-AI theme versus [[cloudflare]]'s premium multiple.
- WAF/DDoS reputation and enterprise stickiness defend the high-margin security base.

### Bear case
- Delivery decline is structural and may outrun security/compute growth, keeping consolidated growth stuck in the low single digits.
- Linode/Connected Cloud puts Akamai in direct competition with [[amazon]], [[microsoft]], and [[alphabet]] hyperscalers where it has no scale advantage — a capex-heavy distraction, per the bears.
- [[cloudflare]] keeps taking share with a broader platform, aggressive free-tier pricing, and stronger developer mindshare.
- The "edge AI inference" TAM may prove smaller or slower than hoped, leaving the re-rating premium exposed.

---

## Key Risks

- **CDN commoditisation** — the legacy delivery business faces persistent price and volume pressure from [[cloudflare]], AWS CloudFront, and bundled hyperscaler CDNs; the segment is in secular decline.
- **Mix-shift execution** — the entire equity story depends on security and compute growing fast enough to offset delivery; a stall in security growth would undercut the thesis.
- **Hyperscaler competition in compute** — Linode competes against AWS/Azure/GCP with vastly larger R&D and capex budgets; sub-scale cloud economics are a real risk.
- **AI-compute commitment concentration** — the $1.8B AI deal is a large multi-year commitment whose realisation depends on a customer's continued demand and ramp.
- **Capital intensity** — building out compute and AI-inference capacity raises capex and could pressure the strong free-cash-flow profile that underpins the value case.
- **Valuation/positioning** — re-rating toward an "AI infrastructure" multiple raises the bar; any disappointment in the compute ramp can de-rate the stock back to a value multiple.

---

## Valuation & How the Stock Trades

Akamai trades as a **profitable, cash-generative "value-growth" infrastructure name** rather than a high-multiple growth stock — the deliberate counterpoint to [[cloudflare]]. Qualitatively:

- **Multiple** — a modest P/E versus high-growth security/CDN peers; the stock has historically been valued on free cash flow and buybacks, not top-line growth. The 2026 AI-compute commitment is nudging the multiple toward an AI-infrastructure framing.
- **Profitability** — strongly free-cash-flow positive with healthy non-GAAP operating margins (~30%), funding consistent share repurchases that support EPS.
- **Catalysts** — earnings night turns on the **security/compute vs delivery growth split** and any new AI-compute disclosures more than on the headline; guidance on segment mix moves the stock.
- **Capital return** — buybacks (no dividend historically) are the capital-return story; the bull case is "cheap compounder," the bear case is "value trap if delivery decline wins."
- **Lower beta** than [[cloudflare]] — a steadier, less crowded way to own edge/CDN/security exposure, with re-rating optionality from the AI-inference narrative.

---

## Trading Relevance

### The "Boring Infrastructure" Stock

Akamai occupies a different investment profile than its competitors. Compared to [[cloudflare]] (high-growth, high-multiple, GAAP unprofitable), Akamai is a mature, profitable infrastructure company:

| Metric | Akamai | [[cloudflare|Cloudflare]] |
|---|---|---|
| Revenue Growth | ~5-8% YoY | ~28-30% YoY |
| Operating Margin | ~15% GAAP, ~30% non-GAAP | Negative GAAP |
| Valuation Multiple | ~20-25x P/E | ~500x+ P/E (or N/A on GAAP) |
| Free Cash Flow | Strongly positive | Turning positive |

This makes Akamai a "value-growth" play in tech — investors buying it expect steady cash flow and margin expansion from the security pivot, not explosive top-line growth.

### Security Pivot as Defensive Strategy

Akamai's shift from CDN to security is strategically defensive. CDN revenue is declining as content delivery commoditises — [[cloudflare]] offers a generous free tier, and cloud providers bundle CDN with their platforms. By pivoting to security (higher margins, stickier contracts, growing TAM), Akamai is attempting to offset CDN decline with higher-value revenue. The success of this pivot is the key question for Akamai investors.

### Acquisition-Driven Strategy

Akamai has used M&A aggressively to enter new markets:

| Acquisition | Year | Price | Strategic Rationale |
|---|---|---|---|
| Prolexic | 2012 | $370M | DDoS mitigation — started security pivot |
| Guardicore | 2021 | ~$600M | Microsegmentation / zero trust |
| Linode | 2022 | $900M | Cloud compute — compete with AWS/Azure/GCP |
| Neosec | 2023 | Undisclosed | API security |

The Linode acquisition is the most debated — it puts Akamai in direct competition with hyperscalers (AWS, Azure, GCP) where it has no natural advantage. Bulls argue it creates a "distributed cloud" alternative; bears argue it is a distraction from the security focus.

---

## Competitive Landscape

| Dimension | Akamai | [[cloudflare|Cloudflare]] | [[fastly|Fastly]] | AWS CloudFront |
|---|---|---|---|---|
| **Revenue** | ~$3.8B | ~$2.2B | ~$540M | Undisclosed (part of AWS) |
| **Market Cap** | ~$16B | ~$69B | ~$3-4B | N/A (Amazon subsidiary) |
| **CDN Market Share** | ~30-40% (enterprise) | ~15-25% (enterprise) | ~5-10% | ~15-25% |
| **Edge Locations** | 4,300+ PoPs | 335+ cities | ~70 PoPs | 600+ edge locations |
| **Core Strength** | Enterprise scale, WAF accuracy | Integrated security + dev platform | Developer ergonomics, edge compute | AWS ecosystem integration |
| **Security Revenue** | ~55% of total | Growing (SASE, Zero Trust) | WAF only (Signal Sciences) | AWS WAF (separate) |
| **Compute Offering** | Linode (IaaS) + edge | Workers (serverless) | Fastly Compute (Wasm) | Lambda@Edge |
| **Growth Rate** | ~5-8% | ~28-30% | ~7-10% | N/A |
| **Profitability** | ~30% non-GAAP operating margin | Non-GAAP profitable | Not profitable | N/A |

Akamai's moat is its massive edge network (4,300+ PoPs in 135 countries), deep enterprise relationships, and industry-leading WAF detection accuracy. However, [[cloudflare]] is gaining share rapidly with a broader platform, more aggressive pricing, and stronger developer mindshare.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: AKAM |
| **Sector** | [[technology|Information Technology]] |
| **Industry** | Internet Services & Infrastructure |
| **Founded** | 1998 |
| **Founders** | Tom Leighton, Danny Lewin |
| **CEO** | Tom Leighton (co-founder, CEO since 2013) |
| **Headquarters** | Cambridge, Massachusetts |
| **Edge Network** | 4,300+ PoPs, 135 countries |
| **CIK** | 0001086222 |
| **S&P 500** | Yes |

---


## Fundamentals

*Source: [[stockmarketapi-fundamentals-2026-05-10]] · period end 2024-12-31 · primary sec_edgar · completeness 100% · pulled 2026-06-10*

### Snapshot

| Metric | Latest | 5y avg | Note |
|---|---|---|---|
| PE ratio | 42.1x | — | compare to sector / index avg |
| Gross margin | — | — | trend matters — rising = pricing power |
| Operating margin | 13.4% | 53.5% | — |
| EBITDA margin | 29.6% | 95.9% | >20% strong; >27% Fred's 'excellent' tier |
| Net margin | 12.7% | 14.4% | — |
| ROE | 10.4% | 6.3% | API uses book equity — high values reflect leverage / buybacks |
| ROA | 4.9% | 3.1% | Fred's bar: ≥5% |
| Debt-to-equity | — | — | Fred: <1.0 healthy, >2.0 leveraged (sector-adjusted) |
| Liabilities-to-equity | 1.13x | — | broader leverage |
| Current ratio | 1.23x | — | Fred: >2.0 (N/A for retail / staples / banks) |
| Quick ratio | — | — | Fred: >1.0 |
| Interest coverage | 19.7x | — | Fred: <1.5 dangerous, >3.0 comfortable |
| EPS (diluted) | 3.27 | — | — |
| Dividend per share | — | — | — |
| Dividend yield (API) | — | — | API definition — see source page; not directly = market yield |
| Dividend payout | — | — | — |

### 5-period trend

| Period | EBITDA margin | Operating margin | ROE | D/E |
|---|---|---|---|---|
| 2024-12-31 (FY) | 29.6% | 13.4% | 10.4% | — |
| 2023-12-31 (FY) | 31.7% | 16.7% | 11.9% | — |
| 2022-12-31 (FY) | 136.8% | 72.9% | 3.0% | — |
| 2021-12-31 (FY) | 147.3% | 86.5% | 3.5% | — |
| 2020-12-31 (FY) | 134.3% | 77.8% | 2.7% | — |

### Fred-framework view

**Profile:** *Mixed-quality* — passes 3/6 of Fred's hurdles.

| Bar | Result | Value |
|---|---|---|
| ROA ≥5% | ✗ | 3.1% |
| ROE ≥15% | ✗ | 6.3% |
| Net margin ≥10% | ✓ | 12.7% |
| EBITDA margin ≥20% | ✓ | 95.9% |
| Current ratio ≥2 | ✗ | 1.23x |
| Interest coverage ≥3x | ✓ | 19.67x |

- **Suits:** investors who weight specific bull-case metrics and accept failures elsewhere
- **Watch for:** the failed Fred bars listed below — each is a known-risk vector, not a quirk
- **Sector context:** Information Technology — Fred's standard bars apply (D/E <1.0, current >2, interest coverage >3x).

## Related

- [[s-and-p-500]]
- [[technology|Information Technology]]
- [[economic-moat]]
- [[cloudflare]]
- [[fastly]]
- [[crowdstrike]]
- [[zscaler]]
- [[datadog]]
- [[alphabet]]
- [[amazon]]
- [[microsoft]]
- [[apple]]
- [[accenture]]
- [[adobe]]
- [[analog-devices]]
- [[autodesk]]

## Sources

- (Source: [[stockmarketapi-sp500-2026-04-13]])
- (Source: [[stockmarketapi-fundamentals-2026-05-10]])
- Akamai Q1 2026 financial results (StockTitan/press release): https://www.stocktitan.net/news/AKAM/akamai-reports-first-quarter-2026-financial-mjpy0c3zgmps.html
- Akamai company overview (FY2025 revenue, headcount): https://www.akamai.com/company
- Verified via Perplexity (sonar), 2026-06-10
