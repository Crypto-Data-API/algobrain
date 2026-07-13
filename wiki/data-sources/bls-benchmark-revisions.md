---
title: "BLS Nonfarm Payrolls and Benchmark Revisions"
type: source
created: 2026-05-05
updated: 2026-06-12
status: good
tags: [data-provider, employment, macro, free-data-sources, fundamental-analysis]
aliases: ["BLS Benchmark Revisions", "Nonfarm Payrolls", "NFP", "BLS Employment Situation", "QCEW Benchmark"]
source_type: data
source_url: "https://www.bls.gov/"
confidence: high
related: ["[[employment]]", "[[recession]]", "[[macro-data-sources]]", "[[fundamental-data-sources]]", "[[free-data-sources]]", "[[data-sources-overview]]", "[[2026-03-bls-900k-jobs-revision]]", "[[service-sector-multiplier]]", "[[ai-layoff-trap]]", "[[wage-compression-vs-job-loss]]", "[[ibkr-forecast-trader]]"]
---

# BLS Nonfarm Payrolls and Benchmark Revisions

The U.S. **Bureau of Labor Statistics (BLS)** publishes the monthly Employment Situation report — the headline **nonfarm payrolls (NFP)** print — and the **annual benchmark revisions** that retroactively re-base prior-year payroll counts against the more accurate Quarterly Census of Employment and Wages (QCEW). For traders monitoring an [[ai-layoff-trap|AI-driven labor cascade]], the benchmark revisions are arguably more important than the headline NFP itself, because they correct directional signal that the monthly establishment survey misses for many months. (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])

## What It Tracks

| Release | Frequency | What it is |
|---------|-----------|------------|
| **Employment Situation Summary** ("the jobs report") | First Friday of each month, 8:30 AM ET | Headline NFP change, unemployment rate, average hourly earnings, hours worked, labor-force participation |
| **JOLTS** (Job Openings and Labor Turnover) | Monthly, lagged | Openings, hires, quits, layoffs |
| **QCEW** | Quarterly, ~6 months lag | Near-census of UI-covered employment; the benchmark for monthly estimates |
| **Annual benchmark revision** | Released with February jobs report; preliminary estimate the prior August | Re-bases NFP history to QCEW; revises 12-21 months of prior data |

## Why It Matters for AI-Recession Analysis

The headline NFP print is the most-traded macro release in the world, but it is built from a sample-based **establishment survey** that misses business birth/death dynamics in real time. When the labor market is turning, the establishment survey is systematically wrong in the same direction for months, then corrected in one large revision.

The **February 2026 benchmark revision erased ~900,000 jobs from 2025 figures — the largest in over a decade.** (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]]) See [[2026-03-bls-900k-jobs-revision]] for the dated event note. Implications:

- The labor market in 2025 was materially weaker than the monthly headlines suggested while traders were positioning.
- Any AI-displacement narrative built on monthly NFP "still strong" prints in 2025 was mismeasuring the baseline.
- [[service-sector-multiplier|Service-sector multiplier effects]] from initial tech layoffs may be operating against a smaller, weaker labor base than reported, amplifying downside.

For an AI-recession watcher, the practical rule is: **monthly NFP tells you what is reported; the benchmark revision tells you what was real.** Treat the establishment survey as a leading sentiment indicator and the QCEW-anchored revision as ground truth.

## Access

| Detail | Value |
|--------|-------|
| **Provider** | U.S. Bureau of Labor Statistics |
| **URL** | [bls.gov](https://www.bls.gov/) |
| **Cost** | Free |
| **API** | BLS Public Data API (free, registration optional, higher quotas with API key) — [bls.gov/developers/](https://www.bls.gov/developers/) |
| **Bulk download** | Flat files via `bls.gov/data/` and FRED mirrors |
| **Mirror** | Federal Reserve Economic Data ([[fred-data|FRED]]) republishes most BLS series with charting and graphs |

Most traders consume BLS data via FRED, Bloomberg, or broker macro calendars rather than directly from the BLS website, but the original release is canonical.

## Key Series for AI-Displacement Tracking

- **CES (Current Employment Statistics)** — establishment survey; total nonfarm and sectoral payrolls. Track **information**, **professional and business services**, and **financial activities** for white-collar AI exposure; **construction** and **trade/transport/utilities** for the inverse (skilled trades) signal.
- **CPS (Current Population Survey)** — household survey; unemployment rate, labor-force participation. Diverges from CES in ways that flag turning points.
- **JOLTS** — quits rate is a leading indicator of labor-market tightness; layoffs/discharges rate is the direct AI-displacement print.
- **QCEW** — by-county, by-industry near-census. Slow but authoritative; the basis for benchmark revisions and for [[citrini-research|Citrini-style]] regional analyses.
- **OEWS (Occupational Employment and Wage Statistics)** — annual occupation-level wages; useful for tracking the [[skilled-trades-wage-boom]] and [[wage-compression-vs-job-loss]].

## Gotchas / Caveats

- **Establishment-survey bias near turning points.** The birth/death model assumes business formation/closure follows historical patterns. In a rapid AI-displacement regime, this assumption breaks and NFP overstates employment.
- **Revisions are not symmetric in market reaction.** Markets typically trade the headline; benchmark revisions are read but rarely re-priced into asset prices in proportion to their size. This is itself an opportunity.
- **Seasonal adjustment can mask trend.** Watch both seasonally adjusted (SA) and not-seasonally-adjusted (NSA) series.
- **Federal-employment noise.** The federal-government workforce has lost ~327K workers since Oct 2024 (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]]); strip it out when isolating AI-driven private-sector displacement.
- **AI-attributed layoffs are not a BLS series.** Track them via TechNode, layoffs.fyi, and corporate filings; BLS aggregates them into broader sector totals.
- **Preliminary benchmark estimate.** A preliminary benchmark is published in August and revised in the February release. Do not treat the August preliminary as final.

## Use Cases

- **Validate or fade AI-recession narratives.** If monthly NFP stays "strong" but the August preliminary benchmark forecasts a large negative revision, the labor market is weaker than the tape implies — bias toward [[recession]] hedges via [[ibkr-forecast-trader]].
- **Sector rotation timing.** Watch the divergence between **information** payrolls (declining) and **construction** payrolls (rising) for the [[capital-vs-labor-asymmetry|capital-vs-labor]] AI signature.
- **Calibrate [[service-sector-multiplier]].** Tech-job loss → 3-5x service-job loss with 2-4 quarter lag. Use BLS sectoral data to verify the multiplier is firing.
- **Detect [[wage-compression-vs-job-loss]].** Combine CES average hourly earnings with CPS unemployment: stable unemployment + falling real wages is the AI-displacement signature, not classical recession.

## Related

- [[employment]]
- [[recession]]
- [[2026-03-bls-900k-jobs-revision]]
- [[service-sector-multiplier]]
- [[wage-compression-vs-job-loss]]
- [[ai-layoff-trap]]
- [[macro-data-sources]]
- [[fundamental-data-sources]]
- [[free-data-sources]]
- [[data-sources-overview]]
- [[ibkr-forecast-trader]]

## Sources

- (Source: [[2026-04-22-gap-finder-possible-ai-fueled-global-job-loss-reces]])
- Bureau of Labor Statistics — [bls.gov](https://www.bls.gov/)
- BLS Public Data API documentation — [bls.gov/developers/](https://www.bls.gov/developers/)
