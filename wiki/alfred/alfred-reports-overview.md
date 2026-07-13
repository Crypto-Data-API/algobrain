---
title: "Alfred Investment Reports"
type: index
created: 2026-04-09
updated: 2026-04-09
status: good
tags: [alfred, fundamental-analysis, stocks, index]
related: ["[[alfred]]", "[[alfred-report-methodology]]", "[[alfred-fundamental-analysis]]", "[[fred-mcnaught]]", "[[sam-deering]]"]
---

Index of all Alfred stock investment reports. For how these reports are structured, see [[alfred-report-methodology]]. For metric formulas, see [[alfred-fundamental-analysis]].

## Company Reports — Verdict Summary

| Company | Ticker | Report Type | Date | Valuation | Owner | Non-Owner | Risk |
|---------|--------|-------------|------|-----------|-------|-----------|------|
| [[close-the-loop]] | CLG:ASX | Full Report | 15 May 2024 | UNDERVALUED | BUY | BUY | MEDIUM |
| [[macquarie-technology]] | MAQ:ASX | Full Report | 28 May 2024 | OVERPRICED | HOLD | WATCHLIST | — |
| [[northern-star]] | NST:ASX | Full Report | 8 May 2024 | FULLY PRICED | HOLD | WAIT | — |
| [[snowflake]] | SNOW:NYSE | Full Report | 25 Jun 2024 | OVERVALUED | — | — | — |
| [[boss-energy]] | BOE:ASX | 1-Pager | 5 Jun 2024 | — | — | — | — |
| [[csl-limited]] | CSL:ASX | 1-Pager | 7 Jun 2024 | — | — | — | — |
| [[dicker-data]] | DDR:ASX | 1-Pager | 5 Jun 2024 | — | — | — | — |
| [[nextdc]] | NXT:ASX | 1-Pager | 1 Jun 2024 | — | — | — | — |
| [[origin-energy]] | ORG:ASX | 1-Pager | 2 Jun 2024 | — | — | — | — |
| [[paladin-energy]] | PDN:ASX | 1-Pager | 5 Jun 2024 | — | — | — | — |

## Sector & Commodity Reports

| Report | Date | Key Finding |
|--------|------|-------------|
| [[alfred-report-gold-commodity|Gold Commodity]] | 23 May 2024 | 7.78% CAGR over 10Y, beating inflation. +553% AUD over 20Y. Future looks bright. |
| [[alfred-report-uranium-commodity|Uranium Commodity]] | 6 Jun 2024 | 25.33% CAGR 5Y. Supply squeeze. Third price boom possible with catalyst. |
| [[alfred-report-asx-gold-sector|ASX Gold Sub-Industry]] | 8 May 2024 | 17 stocks, top-heavy. NST 35% of sector. PRU strongest fundamentals. |
| [[alfred-report-sectors-benchmarks|Sectors Benchmarks]] | Jun 2024 | GICS classification + Alfred default benchmark thresholds. |

## All Report Source Summaries

```dataview
TABLE source_date as "Date", confidence, claims_count as "Claims"
FROM "wiki/sources"
WHERE contains(file.name, "alfred-report")
SORT source_date DESC
```

## Companies Analyzed

```dataview
TABLE status, updated, tags
FROM "wiki/entities/companies"
WHERE contains(related, "alfred-report")
SORT title ASC
```

## Related

- [[alfred]] — Alfred AI assistant
- [[alfred-report-methodology]] — How reports are structured
- [[alfred-fundamental-analysis]] — Metric formulas and worked example
