---
title: "Automatic Data Processing"
type: entity
created: 2026-04-13
updated: 2026-06-18
status: excellent
tags: [company, sp500, stocks]
entity_type: company
aliases: ["ADP"]
headquarters: "Roseland, New Jersey"
website: "https://www.adp.com"
ticker: "ADP"
exchange: "NASDAQ"
sector: "Industrials"
sp500: true
related: ["[[industrials]]", "[[s-and-p-500]]"]
founded: 1949
industry: "Human Resource & Employment Services"
fundamentals_updated: 2026-06-10
fundamentals_period_end: 2025-06-30
fundamentals_source: stockmarketapi
pe_ratio: 23.16
debt_to_equity: 0.64
ebitda_margin_5y_avg: 0.2733
roe_5y_avg: 0.7659
roa_5y_avg: 0.0625
dividend_yield_5y_avg: 2.0412
data_completeness_pct: 100
fred_profile: "Quality compounder"
---

Automatic Data Processing (NASDAQ: ADP) is the world's largest payroll and human-capital-management (HCM) provider, paying roughly 1 in 6 US private-sector workers. For traders it is a [[s-and-p-500]] quality compounder and dividend aristocrat (50+ consecutive annual increases), and the publisher of the **ADP National Employment Report** — itself a market-moving macro release. It is classified in [[industrials]] (business services) but operates as a [[technology]]-and-[[financials|financial]]-services hybrid: a software/outsourcing platform whose embedded "float" on client payroll cash makes it rate-sensitive like a financial.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | NASDAQ: ADP |
| **Sector** | [[industrials|Industrials]] |
| **Industry** | Human Resource & Employment Services |
| **Founded** | 1949 |
| **Headquarters** | Roseland, New Jersey |
| **CIK** | 0000008670 |

## Business Overview & Segments

ADP, founded in 1949, is a payroll and HCM outsourcing platform whose scale (paying ~1 in 6 US private-sector workers) is itself the product. It reports two segments, and two structural kickers define the economics.

| Segment | What it is | Role in the model |
|---|---|---|
| **Employer Services** | Payroll, tax filing, HR outsourcing, benefits administration; the RUN (small business) and Workforce Now (mid-market) platforms | The larger, higher-margin core; recurring subscription/transaction revenue across hundreds of thousands of clients |
| **PEO Services (TotalSource)** | Professional-employer-organization / co-employment bundling payroll, benefits and workers' comp for SMBs | Faster-growing, deeply embedded outsourcing relationship; high switching costs |

Two structural kickers matter to the model:

- **Client-funds float** — ADP holds tens of billions of dollars of client payroll funds in transit and earns interest on the balance ("interest on funds held for clients"). This makes EPS directly sensitive to short-term interest rates and is a financial-services-like profit lever layered on a software business.
- **Retention (~92%+)** — once a company runs payroll, tax filing and benefits through ADP, switching is risky (tax-compliance errors, year-end W-2 disruption) and rare, making revenue highly recurring.

Main competitors: [[paychex]] (down-market SMB), Paycom and Dayforce (mid-market cloud HCM), and [[workday]] (up-market enterprise HCM). Note the API's 7.6x liabilities-to-equity ratio largely reflects client-fund obligations (money owed back to clients), not operating leverage.

## Economic Moat & Competitive Position

ADP holds a wide [[economic-moat|economic moat]] from scale, switching costs and float:

- **High [[switching-costs]]** — payroll and tax filing are mission-critical and compliance-heavy; an error means fines or unpaid employees, so clients almost never switch (~92%+ retention). Year-end (W-2/1099) cutovers further discourage moving.
- **Scale economics** — as the largest processor, ADP amortizes compliance, security and product R&D (tax-jurisdiction coverage in thousands of localities) across the biggest base, a cost advantage smaller rivals cannot match.
- **Client-funds float** — the tens of billions of dollars of payroll cash in transit generate interest income that is, in effect, a structural subsidy unavailable to sub-scale competitors and a [[financials|financial]]-services-grade earnings lever.
- **Data and distribution** — the breadth of payroll data (the basis for the National Employment Report) and a vast distribution/partner network reinforce the position.
- **Regulatory complexity as a barrier** — maintaining accurate tax tables across every US and many foreign jurisdictions is a high fixed-cost barrier that favors incumbents.

The moat is durable; the competitive pressure comes from cloud-native HCM platforms moving down-market and from fintech payroll entrants, not from any credible threat to ADP's compliance scale.

## Competitors / Peer Set

| Company | Primary battleground | Notes |
|---|---|---|
| [[paychex]] | SMB payroll/HR (down-market) | The closest direct comp; both report payroll/HCM and benefit from client-funds float and rate sensitivity |
| Paycom | Mid-market cloud HCM | Single-database cloud platform competing for mid-market clients |
| Dayforce (Ceridian) | Mid-market cloud HCM/payroll | Cloud-native rival pushing into ADP's mid-market |
| [[workday]] | Enterprise HCM (up-market) | The premium enterprise HCM/financials platform; competes for large-employer deals |
| Intuit / fintech payroll | Micro/SMB payroll | QuickBooks Payroll and fintech entrants contest the smallest accounts |

ADP straddles the market from micro-SMB (RUN) to large enterprise, with [[paychex]] the most direct structural comp and [[workday]] the up-market premium rival.

## Growth Drivers & Catalysts

- **Interest on client funds** — higher-for-longer short rates lift float income; the rate path is a direct EPS lever (and a risk if rates fall sharply).
- **PEO growth** — TotalSource co-employment expanding faster than core, deepening client relationships.
- **Pricing + new-business bookings** — annual price increases and HCM module attach (benefits, time, talent, analytics) lift revenue per client.
- **Margin expansion** — ongoing automation and AI in service delivery drive adjusted-EBIT margin gains (guided 70–80 bps).
- **Dividend growth** — continued increases preserve dividend-aristocrat status and anchor the total-return case.
- **Macro employment** — "pays per control" (worker counts at existing clients) rises with employment, though a softening labor market is a modest headwind.
- **Recurring catalysts** — quarterly earnings (fiscal year ends June), the monthly ADP National Employment Report, and the Fed-rate path.

## Bull Case vs Bear Case

### Bull case
- A wide-moat, recurring-revenue quality compounder with ~92%+ retention and dividend-aristocrat consistency.
- Client-funds float gives a rate-geared earnings lever on top of steady subscription growth — a feature in a higher-for-longer world.
- Best-in-class margins and high ROE/ROIC with a strong balance sheet (see fundamentals); reliable buybacks and dividend growth.
- Scale and compliance barriers protect share against cloud-native entrants.
- Defensive, low-beta profile prized by quality- and dividend-factor portfolios.

### Bear case
- Rate sensitivity cuts both ways — a sharp fall in short rates compresses high-margin float income.
- A weakening US labor market reduces pays-per-control and new-business formation (ADP's own data has shown softening payrolls).
- Cloud-native HCM rivals (Workday, Dayforce, Paycom) and fintech payroll keep pressuring growth and pricing.
- It is a premium-multiple defensive — valuation re-rates down in risk-on rotations toward higher-growth names.
- Mature core growth (mid-single-digit revenue) limits the upside versus faster compounders.

## Key Risks

- **Rate cycle** — float income falls if the Fed cuts aggressively; a key, sometimes underappreciated, earnings swing factor.
- **Labor-market softening** — fewer workers at existing clients (pays per control) and slower SMB formation reduce volume.
- **Competitive disruption** — cloud-native and fintech payroll players eroding mid-market and SMB share.
- **Client-fund / regulatory exposure** — handling tens of billions in transit carries operational, cyber and compliance risk; tax-filing errors are reputationally costly.
- **Valuation** — a premium defensive multiple that can compress if growth or rate tailwinds fade.

## 2025-2026 Developments

- **FY2025 (ended June 2025)**: revenue **+7% to $20.6 billion**, net earnings +9% to **$4.1 billion**, adjusted diluted EPS **$10.01** (+9%).
- **FY2026 guidance raised at Q3 (reported ~April-May 2026)**: revenue growth lifted to **6-7%**, adjusted EBIT margin expansion 70-80 bps, adjusted EPS growth **10-11%** (initial guide had been 5-6% revenue, 8-10% EPS).
- **Dividend**: continued annual increases, keeping its dividend-aristocrat status intact.
- **Macro signal**: ADP's own employment data showed a softening US labour market through late 2025 (e.g., -32,000 private payrolls in September 2025) — soft employment is a modest headwind to ADP's pays-per-control metric.

## Trading Relevance

- **Index membership**: [[s-and-p-500]], Nasdaq-100; a staple in dividend-growth and quality-factor ETFs.
- **Options**: good liquidity in monthlies; modest IV — typically traded for earnings drift and dividend-capture rather than gamma.
- **Catalysts**: quarterly earnings (4 per fiscal year ending June), the monthly ADP National Employment Report (moves bonds/equities broadly, occasionally focuses attention on ADP itself), Fed-rate path (client-funds interest income), US employment trends.
- **Correlated names**: [[paychex]] (closest comp), Paycom, Dayforce, [[workday]].

## Valuation & How the Stock Trades

ADP trades at a premium-but-reasonable multiple (~23x trailing earnings per the fundamentals below) that reflects its quality-compounder profile: steady mid-single-digit revenue growth, double-digit EPS growth, best-in-class margins and a rare combination of recurring software economics with a rate-geared float kicker. The trailing P/E is a clean read here (unlike the loss-making/distorted-multiple names in its peer set), so the debate is whether to pay up for durable quality, not whether the earnings are real. Mechanically:

- **Defensive, low-beta quality** — it sits in dividend-growth and quality-factor ETFs and behaves defensively; it tends to lag in sharp risk-on rallies and outperform in drawdowns.
- **Dividend aristocrat** — 50+ consecutive annual increases; the dividend (yielding roughly 2% historically) plus buybacks is a central part of the total-return case, unlike the no-dividend growth names.
- **Rate-geared earnings** — float income means ADP's EPS and multiple respond to the short-rate path; higher-for-longer is a tailwind, aggressive cuts a headwind.
- **Modest IV / earnings drift** — good options liquidity in monthlies but modest implied volatility; typically traded for earnings drift and dividend capture rather than gamma.
- **Macro read-through** — the monthly ADP National Employment Report makes the company a macro touchstone; the print moves bonds and equities broadly and occasionally focuses attention on ADP itself.

## Notable History & Milestones

| Year | Milestone |
|---|---|
| 1949 | Founded by Henry Taub as Automatic Payrolls, Inc. in Paterson, New Jersey |
| 1961 | IPO; renamed Automatic Data Processing |
| 1970s–1990s | Becomes the dominant US payroll outsourcer; expands into broader HR and HCM services |
| 2007 | Spins off Broadridge Financial Solutions (securities processing) |
| 2014 | Spins off CDK Global (dealer-management systems), sharpening focus on HCM |
| 2017 | Pershing Square (Bill Ackman) launches an activist campaign pressing for faster margin gains |
| 2020s | Builds out cloud HCM (Workforce Now, RUN), AI-assisted service, and grows PEO (TotalSource); extends dividend-aristocrat streak |
| 2025 | FY2025 revenue +7% to $20.6B; adjusted EPS $10.01 (+9%); FY2026 guidance raised |
| 2026 | Q3 FY2026 guidance lifted (6–7% revenue, 10–11% adjusted EPS); own data flags a softening US labor market |

## Fundamentals

*Source: [[stockmarketapi-fundamentals-2026-05-10]] · period end 2025-06-30 · primary sec_edgar · completeness 100% · pulled 2026-06-10*

### Snapshot

| Metric | Latest | 5y avg | Note |
|---|---|---|---|
| PE ratio | 23.2x | — | compare to sector / index avg |
| Gross margin | — | — | trend matters — rising = pricing power |
| Operating margin | 25.8% | 24.3% | — |
| EBITDA margin | 28.7% | 27.3% | >20% strong; >27% Fred's 'excellent' tier |
| Net margin | 19.8% | 18.7% | — |
| ROE | 65.9% | 76.6% | API uses book equity — high values reflect leverage / buybacks |
| ROA | 7.6% | 6.2% | Fred's bar: ≥5% |
| Debt-to-equity | 0.64x | — | Fred: <1.0 healthy, >2.0 leveraged (sector-adjusted) |
| Liabilities-to-equity | 7.62x | — | broader leverage |
| Current ratio | 1.05x | — | Fred: >2.0 (N/A for retail / staples / banks) |
| Quick ratio | — | — | Fred: >1.0 |
| Interest coverage | 11.6x | — | Fred: <1.5 dangerous, >3.0 comfortable |
| EPS (diluted) | 9.98 | — | — |
| Dividend per share | 5.92 | — | — |
| Dividend yield (API) | 256.0% | 204.1% | API definition — see source page; not directly = market yield |
| Dividend payout | 58.80 | — | — |

### 5-period trend

| Period | EBITDA margin | Operating margin | ROE | D/E |
|---|---|---|---|---|
| 2025-06-30 (FY) | 28.7% | 25.8% | 65.9% | 0.64x |
| 2024-06-30 (FY) | 28.3% | 25.4% | 82.5% | 0.66x |
| 2023-06-30 (FY) | 27.7% | 24.6% | 97.2% | 0.85x |
| 2022-06-30 (FY) | 26.2% | 23.1% | 91.4% | 0.93x |
| 2021-06-30 (FY) | 25.8% | 22.4% | 45.8% | 0.53x |

### Fred-framework view

**Profile:** *Quality compounder* — passes 6/7 of Fred's hurdles.

| Bar | Result | Value |
|---|---|---|
| ROA ≥5% | ✓ | 6.2% |
| ROE ≥15% | ✓ | 76.6% |
| Net margin ≥10% | ✓ | 19.8% |
| EBITDA margin ≥20% | ✓ | 27.3% |
| D/E ≤1.0 (Industrials bar) | ✓ | 0.64x |
| Current ratio ≥2 | ✗ | 1.05x |
| Interest coverage ≥3x | ✓ | 11.65x |

- **Suits:** long-horizon compounder portfolios; investors who tolerate paying for quality
- **Watch for:** valuation risk if PE expansion stalls; concentration risk if held alongside other megacaps
- **Sector context:** Industrials — Fred's standard bars apply (D/E <1.0, current >2, interest coverage >3x).

## Related

- [[s-and-p-500]]
- [[industrials|Industrials]]
- [[technology]]
- [[financials]]
- [[economic-moat]]
- [[switching-costs]]
- [[allegion]]
- [[ametek]]
- [[a-o-smith]]
- [[axon-enterprise]]
- [[boeing]]
- [[paychex]]
- [[workday]]

## Sources

- (Source: [[stockmarketapi-sp500-2026-04-13]])
- [ADP Q4 FY2025 8-K exhibit (SEC)](https://www.sec.gov/Archives/edgar/data/0000008670/000000867025000026/q4fy25exhibit99.htm)
- [ADP Q3 FY2026 8-K exhibit (SEC)](https://www.sec.gov/Archives/edgar/data/0000008670/000000867026000016/q3fy26exhibit99.htm)
- [ADP Q4 2025 earnings call transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/04/21/adp-adp-q4-2025-earnings-call-transcript/)
- Verified via WebSearch, 2026-06-10
