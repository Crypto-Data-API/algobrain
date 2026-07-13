---
title: "SEC EDGAR"
type: source
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [data-provider, fundamental-analysis, stocks, regulation, technology]
aliases: ["EDGAR", "SEC EDGAR", "data.sec.gov", "EDGAR Full-Text Search"]
source_type: data
source_url: "https://www.sec.gov/edgar"
confidence: high
related:
  - "[[sec]]"
  - "[[fundamental-data-sources]]"
  - "[[free-data-sources]]"
  - "[[fundamental-analysis]]"
  - "[[information-arbitrage]]"
  - "[[event-driven]]"
  - "[[data-sources-overview]]"
---

EDGAR (Electronic Data Gathering, Analysis, and Retrieval) is the U.S. [[sec|SEC]]'s system for receiving and publicly disseminating company filings — 10-Ks, 10-Qs, 8-Ks, proxy statements, Form 4 insider trades, 13F holdings, S-1 prospectuses, and more. It is the canonical, free, primary-source repository of U.S. corporate disclosure, and its machine-readable APIs make it a foundational data feed for fundamental, event-driven, and information-arbitrage strategies.

## What It Provides

- **Filing archive**: full public filing history with indexes back to **1994 Q3**; raw documents plus structured exhibits.
- **Full-Text Search (EFTS)**: search the body text of filings since 2001 (UI at efts.sec.gov / sec.gov/cgi-bin/srqsb). Useful for finding every filer mentioning a term (e.g., a product, a counterparty, "going concern").
- **REST APIs on `data.sec.gov`** (free, JSON):
  - `/submissions/CIK##########.json` — a company's full filing history.
  - `/api/xbrl/companyfacts/CIK##########.json` — all XBRL-tagged financial facts for one company.
  - `/api/xbrl/companyconcept/...` — a single concept (e.g., `RevenueFromContractWithCustomerExcludingAssessedTax`) over time.
  - `/api/xbrl/frames/...` — one concept across **all** filers for a given period (cross-sectional fundamentals).
- **Real-time disclosure**: 8-Ks and Form 4 insider transactions are public within minutes of acceptance — the basis for many event-driven and insider-flow signals.

## Access and Limits (2026)

- **Free**, no API key required.
- **Rate limit**: max **10 requests/second**.
- **User-Agent required**: requests must send a declared `User-Agent` header identifying the requester with contact info (e.g., `Sam Research sam@example.com`); requests without it are blocked.
- Data is delivered as raw HTML/text/XBRL — expect to parse. XBRL frames provide the cleanest path to structured numbers.

## Trading Use-Cases

- **Fundamental analysis at scale** — pull standardized XBRL facts across the universe via the `frames` API to build screens, factor models, and quality/value metrics ([[fundamental-analysis]], [[fundamental-data-sources]]).
- **Event-driven** — monitor 8-Ks for material events, M&A, guidance changes, auditor resignations ([[event-driven]]).
- **Insider-flow signals** — Form 4 cluster buying/selling.
- **13F replication / smart-money tracking** — parse institutional holdings each quarter.
- **NLP / text mining** — risk-factor and MD&A language change detection over time; full-text search for thematic exposure. This is a classic source of [[information-arbitrage]] when others read filings slowly.

## Alternatives and Wrappers

- **sec-api.io, edgartools (Python), python-edgar, sec-edgar-downloader** — wrappers that handle pagination, rate limiting, and XBRL parsing.
- **Financial Modeling Prep, Intrinio, Sharadar/Quandl** — pre-cleaned fundamentals derived from EDGAR, saving the parsing work (see [[paid-data-providers]]).
- EDGAR remains the free ground truth; paid vendors mostly add cleaning, point-in-time correctness, and normalization on top.

## Related

- [[sec]] — the regulator that operates EDGAR
- [[fundamental-data-sources]] — fundamentals catalog
- [[free-data-sources]] — where EDGAR sits among free feeds
- [[fundamental-analysis]] — the discipline EDGAR feeds
- [[event-driven]] — 8-K / Form 4 driven strategies
- [[information-arbitrage]] — reading filings faster/deeper than the market

## Sources

- SEC, "Accessing EDGAR Data" (sec.gov/search-filings/edgar-search-assistance), accessed via web research June 2026
- SEC data.sec.gov API documentation
