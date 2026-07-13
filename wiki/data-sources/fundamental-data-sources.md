---
title: "Fundamental Data Sources"
type: reference
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [data, fundamentals, point-in-time]
aliases: ["Financial Statement Data", "Compustat Alternatives"]
related: ["[[data-sources-overview]]", "[[paid-data-providers]]", "[[free-data-sources]]", "[[lookahead-bias]]", "[[alternative-data-providers]]", "[[survivorship-bias]]", "[[financial-statement-analysis]]", "[[earnings-revision]]"]
---

# Fundamental Data Sources

Where to get company financial statement data — income statements, balance sheets, cash flow statements, ratios, analyst estimates — at the quality required for honest backtesting. The single biggest pitfall in fundamental data is the difference between *as-reported* (what was filed at the time) and *as-restated* (what the books say today after corrections). Strategies that use restated data have a built-in lookahead bias that destroys backtest validity.

## What "Point-in-Time" Means

A point-in-time fundamental dataset records, for each company and each historical date:

- The most recent financial statement *that had been filed by that date*
- The exact figures *as they were originally filed*
- Any subsequent restatement, with the date the restatement became known

A non-point-in-time dataset (the more common kind) only stores the latest version of each financial statement, applied retroactively. Backtests run on non-PIT data implicitly assume the market knew the restated numbers in real time, which it didn't. This creates systematic lookahead bias.

The bias is *largest* for fundamental factor strategies: value, quality, accruals, accounting red flags. These strategies depend on small differences in financial ratios, and restatements often change exactly those ratios. A restated EPS revision can move the entire bottom decile of the value sort.

## Provider Comparison

The single most important column is **Point-in-Time (PIT)** — whether the dataset records figures as-of each historical date. Anything marked "No" is unsafe for fundamental backtests. Cost figures are public-domain rough ranges that change frequently; confirm current pricing with each vendor.

| Provider | PIT | Coverage | Cost band | Best for |
|---|---|---|---|---|
| **Compustat (S&P Global)** | Yes | Global, deep history (late 1980s) | ~$10K-$50K+/yr (free via WRDS for academics) | Academic & institutional factor research |
| **S&P Capital IQ** | Yes | Global + private cos, M&A, ownership | Institutional | Ownership/transaction-rich research |
| **FactSet Fundamentals** | Yes | Comparable to Compustat | Institutional | FactSet-integrated workflows |
| **Refinitiv Worldscope / Datastream** | Yes | Best non-US (EU/Asia/EM) | Institutional | Global / EM fundamentals |
| **Sharadar SF1 (Nasdaq Data Link)** | Yes (As-Reported / MRR / Restated) | US listed, back to 1998 | ~$150-$400/mo | Retail/individual PIT quants |
| **SEC EDGAR (direct)** | Yes (by definition) | All US filers; XBRL since ~2009 | Free (+ engineering) | DIY PIT when budget is $0 |
| **Stockanalysis / Macrotrends / Simply Wall St** | No | US + some intl | Free-$30/mo | Human research only, not backtests |
| **Yahoo Finance (`yfinance`)** | No | Broad | Free | Prototyping only |
| **IEX Cloud / Tiingo** | Partial / No | Limited fundamentals | Cheap | Light apps, not full PIT |

### Estimates, Ownership, and Insider Data

| Provider | Domain | PIT / timestamping | Notes |
|---|---|---|---|
| **IBES / I/B/E/S (Refinitiv)** | Analyst earnings estimates | Timestamped (accuracy varies) | Standard for revision & drift research |
| **FactSet Estimates (StreetAccount)** | Analyst estimates | Timestamped | Comparable to IBES |
| **Refinitiv StarMine** | Adjusted estimates + analyst scoring | Timestamped | Proprietary analyst-quality scoring |
| **Visible Alpha** | Segment-level estimates & KPIs | Timestamped | Granular beyond headline EPS/revenue |
| **WhaleWisdom / Fintel / 13F.info** | 13F institutional holdings | 45-day reporting lag | Free/cheap; no shorts or derivatives |
| **S&P Capital IQ Ownership** | Comprehensive ownership | Varies | Includes non-US filings |
| **SEC Form 4 (EDGAR)** | Insider buys/sells | Filed within 2 business days | Free, authoritative |
| **OpenInsider / InsiderInsights** | Insider aggregators | Near-real-time | Free (OpenInsider) / paid scoring |

## The Sources

### Compustat (S&P Global) — The Standard

Range: institutional pricing, ~$10K-$50K+/year. Available free to academics through WRDS (Wharton Research Data Services).

**Pros:** The academic and institutional gold standard. Point-in-time fundamentals from the late 1980s, restated history available, broad global coverage, integrates with CRSP for prices.

**Cons:** Expensive, institutional licensing, no redistribution. Some quirks in how restatements are recorded require expertise to handle correctly.

**Best for:** Academic factor research and any institutional strategy where decades of clean PIT fundamentals matter.

### S&P Capital IQ

Range: institutional pricing. Broader than Compustat in some dimensions (private companies, M&A history, ownership).

**Pros:** Includes private companies, more granular industry classification, ownership and transaction history.

**Cons:** Expensive, complex licensing.

### FactSet Fundamentals

Range: institutional. Comparable to Compustat with some methodological differences.

**Pros:** Strong PIT capabilities, integrates with FactSet Workstation.

**Cons:** Expensive.

### Refinitiv Worldscope / Datastream

Range: institutional. Strong global (especially non-US) fundamentals coverage.

**Pros:** Best-in-class for European, Asian, and emerging markets fundamentals.

**Cons:** Expensive, schema is complex.

### Sharadar (via Nasdaq Data Link / Quandl)

Range: ~$150-$400/month for the SF1 fundamentals dataset.

**Pros:** **Point-in-time fundamentals at retail prices.** Includes the As-Reported, Most Recently Reported, and Restated versions of each datapoint, properly time-stamped. Coverage of US listed companies back to 1998.

**Cons:** US-only, smaller coverage than Compustat, less metadata. Some series start later.

**Best for:** **Retail quants who need PIT fundamentals on a budget.** The single best value-for-money fundamental data source for individual researchers as of 2024-2026.

### SEC EDGAR (Direct)

Free. The SEC's filing system contains every 10-K, 10-Q, 8-K, and 13F filed by US public companies, structured in XBRL since around 2009.

**Pros:** Free, authoritative (it *is* the source), point-in-time by definition, includes every filing.

**Cons:** XBRL parsing is painful, schema changes over time, restatements appear as separate filings with relationships to originals, no convenience layer.

**Tools that make EDGAR easier:**
- `python-edgar` library
- `sec-edgar-downloader`
- The SEC's own bulk download facilities
- `simfin` (slightly normalized via a third party)

**Best for:** When you absolutely need PIT and can't afford Sharadar or Compustat. Budget 1-2 months of engineering to build a usable layer.

### Stockanalysis.com / Simply Wall St / Macrotrends / WisesheetS

Range: free or cheap subscriptions ($10-$30/month).

**Pros:** Easy to use, decent coverage, includes some historical data.

**Cons:** **Not point-in-time.** These are aggregators of restated data with simple frontends. Useful for human research, dangerous for quant backtests.

### Yahoo Finance Fundamentals

Free via `yfinance`.

**Pros:** Free.

**Cons:** Not point-in-time, often missing fields, restatements applied silently, occasional errors.

**Use for:** Prototyping only.

### IEX Cloud / Tiingo Fundamentals

Range: cheap. Limited coverage of fundamentals.

**Pros:** Real APIs at low cost.

**Cons:** Not full PIT, limited history, may aggregate from other sources.

## Estimates and Analyst Data

### IBES / I/B/E/S (Refinitiv)

The standard for analyst earnings estimates. Includes consensus and individual broker estimates with timestamps.

**Pros:** Deep history of consensus revisions, broker-level detail, used in academic research.

**Cons:** Institutional pricing. Timestamping accuracy varies (broker release date vs. database insertion date).

**Best for:** Earnings revision strategies, post-earnings drift research.

### FactSet Estimates (StreetAccount)

Comparable to IBES.

### Refinitiv StarMine

Adjusted estimates with proprietary scoring of analyst quality.

### Visible Alpha

Newer entrant focused on detailed segment-level estimates and KPIs (not just headline EPS/revenue). Used for granular fundamental analysis.

## Ownership and 13F Data

### WhaleWisdom / Fintel / 13F.info

Free or cheap access to 13F filings — quarterly holdings of institutional investors with > $100M AUM.

**Pros:** Free or cheap, easy to query.

**Cons:** Limited to 13F-required filers, 45-day reporting lag, doesn't include shorts or derivatives.

**Use for:** [[smart-money-orderflow-combo|Smart-money]] tracking, fund overlap analysis, late-stage idea generation.

### S&P Capital IQ Ownership

Comprehensive ownership data including non-US filings.

## Insider Trading

### SEC Form 4 (via EDGAR)

Insider buys and sells, filed within 2 business days of the trade. Free direct from SEC.

### Aggregators
- OpenInsider (free, easy to browse)
- InsiderInsights (paid, scoring of insider activity)

## How Trading and AI Systems Consume Fundamental Data

Fundamental data feeds three broadly different consumers, each with different quality requirements:

- **Systematic factor strategies** consume PIT fundamentals as *features* — value (P/E, P/B, EV/EBITDA), quality (ROIC, margins, accruals), and accounting red-flag scores — aligned to the *filing date*, not the period end, and combined with point-in-time prices (e.g. CRSP alongside Compustat). For these strategies PIT is non-negotiable: a non-PIT source quietly converts a real backtest into a fiction (see [[lookahead-bias]]).
- **Discretionary fundamental analysis** consumes the same statements through a human or dashboard lens — trend analysis, peer comparison, ratio decomposition (see [[financial-statement-analysis]]). Restated convenience aggregators (Macrotrends, Stockanalysis) are acceptable here because a human is interpreting, not backtesting.
- **AI / LLM-based research pipelines** increasingly extract structured facts from unstructured filings (10-K/10-Q/8-K) using NLP/LLM parsing — pulling segment data, risk-factor changes, management-tone shifts, and KPI mentions that are not in the headline financials. The discipline that matters: parse from the *original filing as of its filing date* (EDGAR is PIT by construction), verify extracted numbers against the structured XBRL where possible, and treat model output as a draft to be checked, not ground truth. An LLM reading a restated convenience source inherits that source's lookahead bias.

The data-quality bar rises as you move from human research toward automated backtesting: a source that is "fine for a human" can be "fatal for a quant." When in doubt, prefer the filing-date-stamped PIT source and reconcile against EDGAR.

## Common Pitfalls in Fundamental Data

1. **Using restated data in backtests** — covered above. The single biggest source of fundamental backtest bias.

2. **Aligning by period end vs. filing date** — a Q4 with period-end Dec 31 isn't filed until February-March. Strategies that align by period end have weeks of lookahead.

3. **Missing reporting jurisdictions** — many providers are weak on non-US fundamentals. Multi-region strategies need to confirm coverage explicitly.

4. **Currency conversion** — multinational companies report in different currencies; conversion to USD can introduce errors. Compare apples-to-apples (constant currency) when possible.

5. **GAAP vs. non-GAAP** — companies report both; analysts often use non-GAAP. Datasets vary in which they store and how they label.

6. **Restatement chains** — a single financial period may be restated multiple times. Some PIT datasets only track the *latest* restatement; the most rigorous track every revision.

7. **Survivorship in fundamentals** — bankrupt companies stop reporting. If your fundamental dataset only includes "currently reporting" companies, you have survivorship bias even if your price universe doesn't.

## Recommended Stack by Budget

**$0/month:** SEC EDGAR direct (with engineering investment) + Yahoo for fast prototyping. Accept that production backtests need an upgrade.

**$150-$400/month:** Sharadar SF1 via Nasdaq Data Link. The minimum for serious retail PIT fundamentals research.

**$1K-$5K/month:** Sharadar + a curated alt-data add-on or analyst estimates.

**Institutional:** Compustat (via WRDS or direct) + IBES + FactSet/Capital IQ for ownership + alternative data layer.

## Sources

- [[book-quantitative-trading-ernest-chan]] — Chan on point-in-time data
- WRDS documentation (https://wrds-www.wharton.upenn.edu/) — academic standard tutorials
- [[lookahead-bias]] — why point-in-time is non-negotiable
- [[survivorship-bias]] — applies to fundamentals as well as prices

## Related

- [[data-sources-overview]]
- [[free-data-sources]]
- [[paid-data-providers]]
- [[alternative-data-providers]] — the non-financial-statement data complement
- [[lookahead-bias]]
- [[survivorship-bias]]
- [[financial-statement-analysis]]
- [[earnings-revision]]
