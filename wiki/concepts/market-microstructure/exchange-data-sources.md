---
title: "Exchange Data Sources"
type: concept
created: 2026-04-09
updated: 2026-04-09
status: good
tags: [exchange, data-provider, regulation, fundamental-analysis]
aliases: ["Official Exchange Data", "EDGAR", "ASX Data"]
domain: [market-microstructure, fundamental-analysis]
difficulty: intermediate
related: ["[[sec]]"]
---

Master reference of official data sources for major stock exchanges and their regulatory filing systems. These are the authoritative, free (or low-cost) endpoints for company filings, tickers, announcements, and bulk data downloads.

## Australia — ASX

The ASX (Australian Securities Exchange) requires companies to submit half-yearly and annual reports. Financial year ends June 30. Annual reports due end of October; half-yearly reports due end of February.

| Resource | URL |
|----------|-----|
| **Company Directory** (includes CSV download) | https://www.asx.com.au/markets/trade-our-cash-market/directory |
| **Ticker Announcements Search** (search by year) | https://www.asx.com.au/markets/trade-our-cash-market/historical-announcements |
| **Company Code & Name Changes** | https://www.asx.com.au/markets/market-resources/asx-codes-and-descriptors/asx-code-changes |
| **Reporting Dates** | https://www.asx.com.au/markets/trade-our-cash-market/announcements/important-information-about-market-announcements |
| **Dividend Search** (results not comprehensive) | https://www.asx.com.au/markets/trade-our-cash-market/dividend-search |
| **Listing Requirements** | https://www.asx.com.au/listings/how-to-list/listing-requirements |
| **Data Catalogues for Sale** (historical + live feeds, expensive) | https://www.asxdatasphere.com.au/s/catalogue |

**ASX Reporting Schedule:**

| Report | Deadline |
|--------|----------|
| Annual report | End of October 30th |
| Half-yearly report | End of February (released throughout Feb) |
| Quarterly (mining, oil, gas — some required) | Quarterly |

**ASX Listing Requirements:**
- 20% of shares in free float for trading
- $1 million in profit over 3 years
- $4 million in assets OR $15 million market cap
- Minimum of 300 investors holding $2,000+ each
- Half-yearly and yearly reports must be submitted

**ASX Trading Hours:** 10:00 AM – 4:00 PM Sydney time (AEST/AEDT).

**Scale:** ASX total market cap is ~AUD $1.5 trillion — tiny compared to ~$45 trillion across US exchanges (NYSE + NASDAQ combined).

## USA — SEC / EDGAR

US-listed companies on NYSE and NASDAQ report to the [[sec|SEC]] through the EDGAR (Electronic Data Gathering, Analysis, and Retrieval) system. Standard financial year ends December 30.

| Filing | Description | Deadline |
|--------|-------------|----------|
| **10-K** | Annual report | 90 days after FY end (end of March) |
| **10-Q** | Quarterly report | 45 days after quarter end |
| **8-K** | Major events report | Promptly |

Additional filings include: annual meeting statements, insider transactions, beneficial ownership transactions, and earnings statements (can be reported through 8-K forms).

### EDGAR Data Access

| Resource | URL |
|----------|-----|
| **EDGAR Data Documentation** | https://www.sec.gov/os/accessing-edgar-data |
| **Company Tickers (CIK codes) — JSON** | https://www.sec.gov/files/company_tickers.json |
| **Company Search Pages** (substitute CIK) | https://www.sec.gov/edgar/browse/?CIK=0001018724 |
| **SEC API Documentation (bulk ZIP downloads)** | https://www.sec.gov/edgar/sec-api-documentation |
| **Daily Archives (ZIP)** | https://www.sec.gov/Archives/edgar/Feed/ |
| **Full Indexes (ZIP)** | https://www.sec.gov/Archives/edgar/full-index/ |
| **Single Company Submissions (JSON)** (substitute CIK) | https://data.sec.gov/submissions/CIK0001018724.json |
| **Company Financial Facts (XBRL JSON)** (substitute CIK) | https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json |
| **SEC Forms List** | https://www.sec.gov/forms |

Note: There is also a daily bulk ZIP for company and submissions data. Many XBRL endpoints have deprecated fields.

### EDGAR RSS Feeds

| Resource | URL |
|----------|-----|
| **RSS Feeds Overview** | https://www.sec.gov/about/sec-rss |
| **Latest Filings (browse-edgar)** | https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent |
| **Example: AMZN 10-K/10-Q RSS** | https://data.sec.gov/rss?cik=1018724&type=10-K,10-Q,10-KT,10-QT,NT%2010-K,NT%2010-Q,NTN%2010K,NTN%2010Q&count=40 |

RSS feeds are available for company-specific filing searches — useful for automated monitoring of specific tickers.

## Europe

Various exchanges with varying regulatory frameworks. Major venues:

- **Euronext** — Paris, Amsterdam, Brussels, Dublin, Lisbon, Milan, Oslo
- **Deutsche Börse / Xetra** — Frankfurt
- **SIX Swiss Exchange** — Zurich

Data sources to be documented.

## United Kingdom — LSE

The London Stock Exchange (LON) is one of the oldest exchanges in the world.

Data sources to be documented.

## India — NSE / BSE


Data sources to be documented.

## Asia — HKEX

The Hong Kong Stock Exchange (HKG) is a major gateway for international investment into mainland China.

Data sources to be documented.

## Market Size Comparison

| Exchange | Approximate Total Market Cap |
|----------|------------------------------|
| NYSE | ~$28 trillion |
| NASDAQ | ~$25 trillion |
| NYSE + NASDAQ combined | ~$45+ trillion |
| London Stock Exchange | ~$3.5 trillion |
| Hong Kong Stock Exchange | ~$4 trillion |
| ASX | ~AUD $1.5 trillion (~$1 trillion USD) |

## Related

- [[sec]]
- [[fundamental-analysis-overview]]
