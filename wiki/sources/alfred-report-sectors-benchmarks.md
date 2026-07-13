---
title: "Alfred Report — Sectors Benchmarks"
type: source
created: 2026-04-09
updated: 2026-06-12
status: good
tags: [alfred, fundamental-analysis, methodology]
aliases: ["Alfred sector benchmarks", "GICS benchmarks reference"]
source_type: data
source_author: "Alfred"
source_date: 2024-06-01
source_file: "r2://trader-wiki/reports/alfred-report-sectors-benchmarks.docx"
confidence: medium
claims_count: 5
related: ["[[alfred-report-methodology]]", "[[fred-sector-strategy]]", "[[valuation]]"]
---

Alfred's reference document for sector classification and fundamental benchmarks. Covers the GICS (Global Industry Classification Standard) framework and Alfred's default benchmark thresholds used when evaluating stocks across any sector.

## GICS Classification System

- [HIGH] GICS (Global Industry Classification Standard) — 11 sectors, 25 industry groups, 74 industries, 163 sub-industries. Developed in 1999 for S&P and MSCI indexes. (Source: [[alfred-report-sectors-benchmarks]])

### The 11 GICS Sectors

1. **Energy** — Oil, gas, consumable fuels, energy equipment and services
2. **Materials** — Chemicals, construction materials, containers/packaging, metals and mining, paper/forest products
3. **Industrials** — Capital goods, commercial/professional services, transportation
4. **Consumer Discretionary** — Automobiles, consumer durables/apparel, consumer services, media, retailing
5. **Consumer Staples** — Food/staples retailing, food/beverage/tobacco, household/personal products
6. **Health Care** — Health care equipment/services, pharmaceuticals/biotech/life sciences
7. **Financials** — Banks, diversified financials, insurance
8. **Information Technology** — Software/services, tech hardware/equipment, semiconductors
9. **Communication Services** — Telecom services, media/entertainment
10. **Utilities** — Electric utilities, gas utilities, multi-utilities, water utilities, independent power producers
11. **Real Estate** — Equity REITs, real estate management/development

- [HIGH] 11 GICS sectors listed with descriptions of constituent companies for each. (Source: [[alfred-report-sectors-benchmarks]])

## Alfred's Default Benchmarks

These are Alfred's baseline thresholds for evaluating any stock, before applying sector-specific adjustments:

| Metric | Benchmark |
|---|---|
| P/E | < 20.00 |
| Dividend Yield | > 3.80% |
| ROE | > 13.40% |
| D/E | < 0.50 |
| Current Ratio | > 2.00 |
| Quick Ratio | > 1.00 |
| Net Cover | > 2.00 |

- [HIGH] Alfred default benchmarks: P/E < 20.00, Div Yield > 3.80%, ROE > 13.40%, D/E < 0.50, Current Ratio > 2.00, Quick Ratio > 1.00, Net Cover > 2.00. (Source: [[alfred-report-sectors-benchmarks]])

## Benchmark Table Structure

The full benchmark table includes the following columns per sector:

| Column | Description |
|---|---|
| P/E | Price-to-Earnings ratio |
| Div Yield % | Dividend yield |
| EPS | Earnings per share |
| ROE | Return on equity |
| ROA | Return on assets |
| D/E | Debt-to-equity ratio |
| Current Ratio | Current assets / current liabilities |
| Quick Ratio | (Current assets - inventory) / current liabilities |
| Net Cover | Net tangible assets per share / share price |
| Price CAGR 5Y | 5-year price compound annual growth rate |
| Revenue CAGR 5Y | 5-year revenue CAGR |
| EBITDA CAGR 5Y | 5-year EBITDA CAGR |
| EPS CAGR 5Y | 5-year EPS CAGR |

- [HIGH] Benchmark table structure covers: P/E, Div Yield%, EPS, ROE, ROA, D/E, Current Ratio, Quick Ratio, Net Cover, Price CAGR 5Y, Revenue CAGR 5Y, EBITDA CAGR 5Y, EPS CAGR 5Y. (Source: [[alfred-report-sectors-benchmarks]])

## Sector-Specific Benchmarks

- [MEDIUM] Sector-specific benchmarks table is mostly unpopulated — only the default values are filled in. Sector-level benchmarks are intended to be populated over time as more sector reports are completed. (Source: [[alfred-report-sectors-benchmarks]])

## Pages Created/Updated

- [[alfred-report-methodology]]

## Sources

- Raw file: `r2://trader-wiki/reports/alfred-report-sectors-benchmarks.docx`
