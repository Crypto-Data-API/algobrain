---
title: "News and Sentiment Sources"
type: reference
created: 2026-04-10
updated: 2026-06-20
status: excellent
tags: [data, news, sentiment, nlp]
aliases: ["News Data", "Sentiment Data", "News Providers", "Sentiment Providers"]
related: ["[[data-sources-overview]]", "[[alternative-data-providers]]", "[[sentiment-analysis]]", "[[news-trading]]"]
---

# News and Sentiment Sources

Vendors and APIs that provide structured news, entity-tagged events, and sentiment scores for use in trading strategies. The challenge with news data is *timing*: most news data products timestamp by ingestion (when the vendor saw it), not by publication (when it actually went out). For event-driven strategies, the difference is everything.

## Provider Reference Table

A consolidated view of the providers detailed below. Cost tiers are relative (verify current pricing with each vendor); "entity tagging" and "sentiment" indicate whether the product ships structured tags/scores or just raw text.

| Provider | Category | Cost tier | Entity tagging | Sentiment | Best for |
|---|---|---|---|---|---|
| Bloomberg (BN/NSE) | Institutional news | Very high | Yes | Yes (terminal) | Earliest timestamps, deep tagging |
| Reuters / Refinitiv | Institutional news | Very high | Yes | Yes (NewsScope) | Broad coverage, alt sourcing |
| Dow Jones / Factiva | Institutional news | High | Partial | Partial | Business, M&A, earnings |
| RavenPack | Sentiment analytics | Institutional | Yes | Yes | Event-driven, earnings-drift |
| Refinitiv MarketPsych | Sentiment indices | Institutional | Yes | Yes | Macro/security mood research |
| Brain Sentiment | Sentiment factor | Mid-high | Yes | Yes | Explicit-methodology factors |
| Predata | Geopolitical risk | Institutional | Theme-level | Indirect | Country/geo-risk monitoring |
| StockTwits | Social sentiment | Free + paid | Ticker-level | Self-reported | Stock-specific retail signal |
| Twitter (X) API | Social stream | Paid (tiered) | DIY | DIY | Real-time event detection |
| Reddit (PRAW) | Social forum | Free (rate-limited) | DIY | DIY | WSB / niche community signal |
| NewsAPI | Aggregator | Free + paid | No | No | Prototyping, broad aggregation |
| GDELT | Open event DB | Free | Auto (noisy) | Tone score | Geopolitical, long-tail country |
| Google News RSS | Aggregator | Free | No | No | Cheap query-based feeds |
| NewsCatcher | Structured news API | Mid | Some | Some | Affordable structured news |
| Estimize | Earnings estimates | Free + paid | Ticker-level | n/a | Crowdsourced surprise prediction |
| Earnings Whisper | Whisper estimates | Free + paid | Ticker-level | n/a | Informal consensus vs sell-side |
| Refinitiv I/B/E/S | Analyst estimates | Institutional | Ticker-level | n/a | Sell-side consensus (see fundamental-data-sources) |
| Wall Street Horizon | Corporate calendar | Institutional | Ticker-level | n/a | Clean event calendars |
| SEC EDGAR | Regulatory filings | Free | CIK-level | n/a | 8-K/10-K/13F/Form 4, authoritative |

## Institutional News Vendors

### Bloomberg (BN, NSE)

The institutional standard. Bloomberg News + the broader Bloomberg news feed (BN) which aggregates wire services and tags by ticker, sector, and event type.

**Pros:** Earliest timestamps in the industry, deep entity tagging, integrated with the terminal, decades of history.

**Cons:** Expensive (terminal cost), API access (BLP) is proprietary, redistribution restricted.

### Reuters (Refinitiv)

Reuters News plus Refinitiv NewsScope.

**Pros:** Comparable to Bloomberg in coverage and quality, often slightly different sourcing.

**Cons:** Expensive, institutional only.

### Dow Jones Newswires / Factiva

Wall Street Journal parent company's news service. Strong in business news.

**Pros:** Quality business journalism, strong M&A and earnings coverage.

**Cons:** Expensive.

## Specialized Sentiment Vendors

### RavenPack

The leading systematic news analytics vendor for trading.

**Pros:** Real-time entity tagging, sentiment scores, event types, novelty scoring, used widely in systematic equity strategies. Deep historical archive.

**Cons:** Institutional pricing.

**Best for:** Event-driven and earnings-drift strategies that need timestamped sentiment with entity links.

### Refinitiv MarketPsych

Sentiment indices on macro themes, market moods, individual securities.

**Pros:** Long history, academic-friendly licensing for research.

**Cons:** Methodology is partially black-box.

### Bloomberg News Sentiment

Built into the terminal. Sentiment scores derived from Bloomberg News and external feeds.

### Brain Sentiment Indicator

Academic-style sentiment factor with explicit methodology.

### Predata

Geopolitical risk modeling from web activity (Wikipedia traffic, government website traffic, etc.).

**Use for:** Geopolitical event prediction, country risk monitoring.

## Social Media Sentiment

### StockTwits API

Free + paid tiers. Stock-specific social platform with bullish/bearish self-reporting.

**Pros:** Stock-specific signal, easy to access, decent historical depth.

**Cons:** Heavy retail bias, prone to manipulation, short-term noise.

### Twitter (X) API

Free tier is essentially unusable as of 2024-2026. Paid tiers ($100-$5000/month) provide varying levels of access. The "firehose" (full real-time stream) is enterprise-only.

**Use for:** Real-time event detection, sentiment, breaking news. Much harder than it was in the 2015-2022 period.

### Reddit

Public data dumps via PushShift (now restricted) or PRAW with rate limits. Some paid third-party aggregators exist.

**Use for:** WSB-style retail sentiment, niche community signals.

### Sentiment Aggregators
- **Augmento** — crypto-focused social sentiment
- **The TIE** — crypto sentiment
- **Sprinklr** / **Brandwatch** / **Talkwalker** — enterprise social listening (expensive)

## Free / Cheap News Sources

### NewsAPI

Range: free + paid tiers ($449+/month for commercial use).

**Pros:** Aggregates many news sources via single API.

**Cons:** Free tier is limited, no entity tagging, no sentiment.

### GDELT Project

Free. Global Database of Events, Language, and Tone — automatically extracts events from world news in many languages.

**Pros:** Free, broad coverage, includes geocoding and event types.

**Cons:** Noisy, requires significant cleaning, lower precision than commercial vendors.

**Use for:** Geopolitical monitoring, event detection at country level, long-tail country coverage.

### Google News RSS

Free. RSS feeds for any search query.

**Pros:** Free, easy.

**Cons:** No structured tagging, rate limits, intermittent reliability.

### NewsCatcher API

Range: $50-$500/month.

**Pros:** Affordable structured news API.

**Cons:** Coverage and quality vary by source.

### News API of the Day

Various smaller commercial APIs at low cost. Quality varies.

## Earnings Calendars and Estimates

### Estimize

Free and paid. Crowdsourced earnings estimates, often more accurate than sell-side consensus on certain names.

**Use for:** Earnings drift research, surprise prediction.

### Earnings Whisper

Tracks "whisper" estimates (informal consensus distinct from formal sell-side estimates).

### Refinitiv I/B/E/S

Institutional standard for sell-side analyst estimates. See fundamental-data-sources.

### Wall Street Horizon

Range: institutional. Comprehensive corporate event calendar including earnings, dividends, splits, conferences, regulatory deadlines.

**Use for:** Event-driven strategies that need a clean calendar of corporate events.

## Government / Regulatory News

### SEC EDGAR (Free)

Real-time filings (8-K, 10-K, 10-Q, 13F, Form 4). The authoritative source.

**Use for:** Material event detection, insider tracking, ownership changes.

### Bloomberg Government / GovTrack / FactSquared

Legislative tracking, regulatory news, congressional agendas.

### Federal Register (Free)

US federal regulations and notices. Real-time RSS available.

## Common News-Data Pitfalls

### 1. Ingestion vs. Publication Timestamps

The biggest pitfall in news data backtesting. Most vendors timestamp by *when they ingested* the article, which can be seconds to minutes after the actual publication. For strategies that trade on news, this lag is usually too large to matter accurately. Always check whether your vendor provides publication timestamps.

### 2. Entity Tagging Errors

Auto-tagging by NLP is imperfect. "Apple" might refer to AAPL or to a fruit. "Goldman" might mean Goldman Sachs or someone's last name. Vendors vary in their tagging accuracy.

### 3. Sentiment Calibration Drift

Sentiment models are trained on historical data and lose accuracy over time as language evolves. A 2015-trained model evaluating 2025 news is not the same as a 2025-trained model.

### 4. Source Mix Changes

Vendors add and remove sources over time. A backtest that's "real-time enough" in early periods may have artificially clean data in later periods (when more sources came online), creating a spurious trend.

### 5. Republished News

Wire services get republished. The same story may appear multiple times with different timestamps. Naive count-of-articles features will overcount.

### 6. Embargoed and Pre-Released News

Some news is embargoed until a specific time. If a vendor accidentally includes pre-embargo content, you have lookahead.

## How Trading and AI Systems Consume These Sources

Different consumers want different shapes of the same underlying data:

| Consumer | What they ingest | Latency need | Typical use |
|---|---|---|---|
| Latency-sensitive event traders | Machine-readable headlines with publication timestamps | Sub-second | Trade the print on earnings, M&A, macro |
| Systematic equity factor models | Daily entity-tagged sentiment + novelty scores | End-of-day | Earnings-drift, earnings-revision, sentiment factors |
| Discretionary research desks | Searchable archive + alerts | Minutes | Context, thesis-building |
| LLM / NLP pipelines | Raw text → embeddings → classification | Batch or streaming | FinBERT/finance-LLM scoring, summarization, entity linking |
| Macro / geo-risk monitors | Theme- and country-level aggregates (GDELT, Predata) | Daily | Country risk, regime monitoring |

For AI systems specifically, the dominant pattern is: ingest raw text → deduplicate → entity-link to tickers → score with a finance-tuned model ([[sentiment-analysis|FinBERT or similar]]) → store with **both** ingestion and publication timestamps. The model layer is only as good as the timestamp hygiene beneath it — a state-of-the-art classifier on look-ahead-contaminated timestamps still produces a worthless backtest. See [[news-trading]] for strategy-side considerations.

## Data-Quality Caveats — Summary

| Caveat | Impact | Mitigation |
|---|---|---|
| Ingestion vs publication timestamps | Look-ahead / latency error | Insist on publication timestamps; store both |
| Entity-tagging errors | Wrong-ticker signals | Validate tagger; maintain a disambiguation map |
| Sentiment calibration drift | Model decays as language evolves | Retrain/recalibrate periodically |
| Source-mix changes | Spurious trends in backtests | Hold source set constant or flag changes |
| Republished wire stories | Overcounted article-volume features | Fuzzy-match deduplication |
| Embargoed / pre-released news | Look-ahead bias | Filter pre-embargo content |

## Building a News Data Pipeline

For research that needs custom news handling:

1. **Source ingestion** — RSS feeds, API polls, web scraping
2. **Deduplication** — fuzzy matching to collapse republications
3. **Entity linking** — map mentions to ticker symbols / canonical IDs
4. **Sentiment scoring** — apply a model (FinBERT, Llama-3-finance, custom)
5. **Storage** — append-only with both ingestion and publication timestamps
6. **Retrieval** — by ticker, by date, by event type

This is 1-3 months of engineering. Worth doing if news is core to your strategy; not worth doing if you only need news as one feature among many.

## Recommended Stack

### Personal research, no budget
GDELT + Google News + NewsAPI free tier + StockTwits free + SEC EDGAR. Suitable for prototyping; not for production.

### Serious retail
NewsCatcher or NewsAPI paid + StockTwits paid + Estimize. ~$200-$500/month.

### Institutional
RavenPack + Bloomberg News + Wall Street Horizon + custom NLP infrastructure.

## Sources

- Vendor websites and product documentation (Bloomberg, Reuters/Refinitiv, RavenPack, GDELT, SEC EDGAR, etc. — verify current pricing and capabilities)
- [[sentiment-analysis]] — concept page
- [[news-trading]] — strategies that use news
- General market knowledge; no specific wiki source ingested yet.

## Related

- [[data-sources-overview]]
- [[alternative-data-providers]]
- [[sentiment-analysis]]
- [[news-trading]]
