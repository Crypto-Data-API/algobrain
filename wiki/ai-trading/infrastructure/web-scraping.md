---
title: "Web Scraping"
type: concept
created: 2026-04-15
updated: 2026-06-12
status: good
tags: [data-provider, algorithmic, quantitative]
aliases: ["Web Scraping", "Web Scraper", "Screen Scraping"]
domain: [algorithmic]
difficulty: intermediate
related: ["[[alternative-data]]", "[[python]]", "[[sentiment-analysis]]", "[[natural-language-processing-finance]]", "[[ai-data-providers-overview]]", "[[nlp-sentiment-analysis]]", "[[the-book-of-alternative-data]]"]
---

Web scraping is the automated extraction of data from websites — programmatically fetching pages and parsing their content into structured datasets. In trading it is a primary technique for building [[alternative-data|alternative-data]] pipelines: harvesting information that is publicly visible but not packaged into a clean API or commercial feed, then converting it into tradable signals. Examples range from scraping e-commerce product prices and review counts, to job-posting boards, to regulatory filing portals, to social-media sentiment.

## How It Works

A scraping pipeline typically has four stages:

1. **Fetch** — request pages over HTTP. For static HTML, lightweight clients (Python `requests`, `httpx`) suffice. For JavaScript-rendered pages, a headless browser is needed (Selenium, Playwright, Puppeteer).
2. **Parse** — extract fields from the HTML/JSON using parsers (BeautifulSoup, lxml, parsel) or CSS/XPath selectors. APIs hidden behind the page (XHR/JSON endpoints) are often the cleanest target.
3. **Clean & normalize** — deduplicate, type-cast, timestamp, and store (CSV/Parquet/database). [[pandas]] is the standard tool.
4. **Schedule & monitor** — run on a cron/scheduler, with retries, rate-limiting, proxy rotation, and alerting when a site's layout changes and breaks selectors.

Frameworks like **Scrapy** combine these stages into a single asynchronous crawler. Anti-bot measures (Cloudflare, CAPTCHAs, rate limits, fingerprinting) are a constant arms race; serious operations rotate residential/datacenter proxies and randomize request patterns.

## Trading / Finance Relevance

Web scraping is the workhorse of the do-it-yourself alternative-data desk. Common signal sources:

- **E-commerce / pricing** — scraping product prices, stock-outs, and review velocity to nowcast a retailer's revenue ahead of earnings.
- **Job postings** — counting open roles by company/department as a leading indicator of expansion or contraction (a well-documented alt-data signal).
- **App store / web traffic** — download ranks and ratings as demand proxies for consumer-software names.
- **Regulatory & filings** — scraping SEC EDGAR, FDA action calendars, patent offices, court dockets, and government tender portals for event-driven signals.
- **Social & news sentiment** — harvesting Reddit, X/Twitter, StockTwits, and news headlines to feed [[nlp-sentiment-analysis|sentiment]] and [[natural-language-processing-finance|NLP]] models.
- **Crypto on-chain / DEX** — scraping block explorers, DEX dashboards, and forums where structured APIs are thin.

The edge from scraped data is typically **informational** and **decay-prone**: it works until the data is commercialized into a packaged feed and the crowd arbitrages it away. The classic alt-data lifecycle — see [[the-book-of-alternative-data]] — is that a scraped signal is most valuable when you are one of few who have it.

## Risks and Legal Considerations

- **Terms of service / legality** — many sites prohibit scraping in their ToS. US case law (e.g. *hiQ v. LinkedIn*) has generally protected scraping of *publicly accessible* data, but the picture is unsettled and jurisdiction-dependent; scraping behind logins or paywalls carries materially more legal risk. Always assess the specific site and seek counsel for any institutional deployment.
- **Material non-public information** — scraping must never capture MNPI; firms need compliance review of any alt-data source.
- **Data quality / fragility** — scrapers silently break when site layouts change, producing stale or wrong data that can poison a live signal. Monitoring and validation are essential.
- **Rate limits / IP bans** — aggressive scraping gets blocked; respectful crawl rates and proxy hygiene matter.
- **Reproducibility** — scraped historical data is hard to reconstruct point-in-time, creating look-ahead-bias risk in backtests.

## Build vs Buy

For widely-used datasets (web traffic, card transactions, satellite imagery), commercial vendors now package what firms once scraped — often with better coverage, point-in-time integrity, and legal indemnification. Scraping is most justified for **niche, idiosyncratic, or short-shelf-life** signals where no vendor exists, or where the cost of a vendor feed is disproportionate to a single strategy's capacity. See [[ai-data-providers-overview]] for the broader provider landscape.

## Related

- [[alternative-data]] — the broader category scraping feeds
- [[python]] — the dominant scraping toolchain (requests, Scrapy, Playwright, pandas)
- [[natural-language-processing-finance]], [[nlp-sentiment-analysis]] — what scraped text often feeds
- [[ai-data-providers-overview]] — packaged-feed alternatives to scraping
- [[the-book-of-alternative-data]] — reference on the alt-data lifecycle

## Sources

- Alexander Denev & Saeed Amen, *The Book of Alternative Data* (Wiley, 2020) — see [[the-book-of-alternative-data]].
- *hiQ Labs v. LinkedIn* (US 9th Circuit) — public-data scraping case law.
