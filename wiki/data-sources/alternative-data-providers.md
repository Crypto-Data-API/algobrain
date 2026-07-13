---
title: "Alternative Data Providers"
type: reference
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [data, alternative-data, alpha]
aliases: ["Alt Data", "Alternative Data Vendors"]
related: ["[[data-sources-overview]]", "[[alternative-data]]", "[[alternative-data-alpha]]", "[[edge-taxonomy]]", "[[paid-data-providers]]", "[[free-data-sources]]", "[[crypto-data-sources]]", "[[informational-edge]]"]
---

# Alternative Data Providers

Vendors that supply non-traditional data — satellite imagery, credit card transactions, web traffic, app usage, sentiment, weather — for use as predictive signals in trading strategies. Alternative data is the canonical source of *informational edge* (see [[edge-taxonomy]]). The good ones are expensive, opaque, and often capacity-limited; the cheap ones are usually too well-known to provide alpha. This page is a reference catalogue of providers by category; see fundamental-data-sources for financial-statement data and [[crypto-data-sources]] for on-chain alt data. All cost figures below are public-domain rough ranges that change frequently — confirm current pricing directly with each vendor.

## Category Overview

| Category | What it measures | Primary signal use | Typical cost band | Decay stage |
|---|---|---|---|---|
| Satellite imagery | Physical activity (cars, tanks, ports, crops) | Earnings & commodity-inventory prediction | $5K-$50K+/mo per product | Mature for classic uses; edge in newer proxies |
| Card / debit transactions | Consumer spend by merchant | Revenue forecasting for consumer names | $20K-$200K+/yr | Mostly priced in; residual in long-tail names |
| Web traffic / search | Site visits, app installs, search interest | E-commerce & app-driven company tracking | Free (Google Trends) to $10K+/mo | Mixed |
| Web scraping | Job posts, prices, reviews, filings | Hiring proxy, pricing intelligence | $10K+/yr or DIY engineering | Depends on freshness |
| Sentiment / news NLP | Entity-tagged news & social sentiment | Event-driven & drift strategies | $100/mo to institutional | Fast decay (minutes) |
| Weather | Forecasts & historical climate | Ag commodities, power demand, retail | Free (NOAA) to $50K+/mo | Stable (physical) |
| Shipping / logistics | Vessel & flight movements, commodity flows | Commodity-flow & supply-chain signals | $2K-$50K+/mo | Mixed |
| Geolocation / foot traffic | Aggregated device pings by venue | Retail & real-estate revenue | $5K-$50K+/mo | Mature |
| Government / regulatory | Legislation, filings, political trades | Policy & event monitoring | Free to enterprise | Niche |
| Social media analytics | Brand/social listening, firehose | Sentiment & trend detection | Varies widely | Fast decay |
| Crypto-specific | On-chain, social, dev activity | Crypto positioning & flow | See [[crypto-data-sources]] | Varies |

## Categories

### Satellite Imagery

Images of physical locations — parking lots, factories, ports, oil tanks, mines, agricultural land.

- **Orbital Insight** — counted-cars-per-parking-lot, oil tank fill levels, port traffic. The original.
- **RS Metrics** — similar use cases, retail and metals focus.
- **Planet Labs** — daily imagery of the entire Earth's land surface; raw imagery rather than pre-tagged signals.
- **Maxar** — high-resolution imagery, broader B2B applications.
- **SpaceKnow** — manufacturing and construction activity from satellite + machine learning.

**Use cases:** earnings prediction (count cars at Walmart parking lots), commodity inventory tracking (oil tank fill), agricultural yield forecasting, geopolitical event monitoring.

**Cost:** $5K-$50K+/month per data product. Often per-symbol pricing.

**Decay:** parking-lot counting was pure alpha in 2014, mostly priced in by 2020. Newer applications (port congestion, China industrial proxies) still have edge.

### Credit Card / Debit Card Transactions

Aggregated and anonymized consumer transaction data, used to forecast company-level revenue.

- **Yodlee / Envestnet** — consumer banking aggregation, large panels.
- **SecondMeasure (Bloomberg Second Measure)** — consumer transaction panel.
- **Earnest Analytics** — card spend with company tagging.
- **Facteus** — debit card aggregation.

**Use cases:** revenue forecasting for consumer-facing companies, especially e-commerce, subscription, restaurants, retail.

**Cost:** $20K-$200K+/year for institutional licenses.

**Decay:** the major panels have been used since the mid-2010s. Modest residual edge remains, mostly in long-tail names not covered by sell-side analysts.

### Web Traffic / Search

App downloads, website traffic, search trends.

- **SimilarWeb** — website traffic estimation, app rankings.
- **Sensor Tower** / **Apptopia** / **Data.ai (formerly App Annie)** — mobile app downloads, revenue, usage estimates.
- **Google Trends** (free) — search interest by query and region.
- **SEMrush** — search engine ranking and SEO data.

**Use cases:** track e-commerce companies, app-driven companies (Uber, DoorDash, Airbnb), advertising spend predictions.

**Cost:** SimilarWeb / Sensor Tower etc. are $1K-$10K+/month for institutional access. Google Trends is free.

### Web Scraping

Custom-collected data — job postings, prices, reviews, news, regulatory filings, public records.

- **Thinknum** — pre-aggregated alt data from web sources (job postings, store counts, etc.).
- **Quandl Web Data** (now Nasdaq Data Link) — various scraped datasets.
- **DIY** — running your own scrapers is often cheaper and more flexible than buying.

**Use cases:** job postings as a hiring proxy (LinkedIn data), pricing intelligence, review sentiment, regulatory filings parsing.

**Cost:** Thinknum is $10K+/year. DIY is the cost of engineering and proxies.

### Sentiment and News Analytics

NLP-tagged news and social media.

- **RavenPack** — entity-tagged news with sentiment scores, real-time. Institutional standard.
- **Bloomberg News Sentiment** — built into the terminal.
- **Refinitiv MarketPsych** — sentiment indices on market themes.
- **Predata** — geopolitical risk from web activity.
- **StockTwits / Twitter sentiment vendors** (Augmento, etc.) — retail sentiment from social.
- **Brain Sentiment Indicator** (BSI) — academic-style sentiment factor.

**Use cases:** earnings drift trading, event-driven strategies, crisis detection.

**Cost:** RavenPack institutional pricing; consumer-grade sentiment tools $100-$1000/month.

**Decay:** sentiment alpha decays fast. Headline-grade NLP signals from major vendors are now mostly priced in within minutes.

### Weather

- **NOAA** (free) — historical and forecast US weather
- **DTN / Maxar Weather Desk** — commercial weather forecasts and historical
- **AccuWeather** — paid forecasts and historical
- **Speedwell Weather** — derivatives and energy-focused weather data

**Use cases:** weather derivatives trading, agricultural commodities, electricity demand forecasting, retail (snow boots in winter).

### Shipping and Logistics

- **MarineTraffic** / **VesselValue** — AIS ship tracking and valuations.
- **Kpler** — commodity flows by vessel (oil, LNG, coal, grains).
- **Vortexa** — energy commodity tracking from satellite + AIS.
- **FlightAware** / **OAG** — flight tracking and capacity.

**Use cases:** commodity flow prediction, OPEC compliance monitoring, supply chain disruption, airline capacity.

**Cost:** $2K-$50K+/month.

### Geolocation / Foot Traffic

Cell phone location pings aggregated by venue.

- **Placer.ai** — foot traffic by retail location.
- **SafeGraph** — points of interest plus visit data.
- **Veraset** — anonymized location panel.
- **Advan Research** — institutional foot traffic.

**Use cases:** retail revenue prediction, real estate, restaurants.

**Cost:** $5K-$50K+/month.

### Government and Regulatory

- **GovTrack** / **Bloomberg Government** — legislative tracking
- **FactSquared** — politician trade tracking (PELOSI tracker fame)
- **Gravity Research** — regulatory monitoring
- **Open Secrets** (free) — campaign finance and lobbying

### Social Media Analytics

- **Brandwatch** / **Talkwalker** / **Sprinklr** — enterprise social listening
- **Sprout Social** — smaller business
- **Twitter API** (paid tiers) — direct firehose access at high cost
- **Reddit data dumps** — historical reddit data (free but bulky)
- **tickertags** — founded 2015 by [[chris-camillo]]; mapped ~350K product/brand tags to ~8K tickers using social mention frequency. Acquired by [[m-science]] (a [[jefferies-financial-group|Jefferies]] subsidiary) in 2018; standalone product wound down ~2020, technology absorbed into M Science institutional research. Historically significant as an early productization of [[social-arbitrage]].

### Crypto-Specific Alt Data

- **Glassnode** / **Nansen** / **Arkham** — see [[crypto-data-sources]]
- **Santiment** — social and developer activity for crypto projects
- **The TIE** — crypto sentiment

## How Trading and AI Systems Consume Alt Data

Alt data is rarely traded off raw. It passes through a pipeline before it becomes a position, and most of the engineering value (and most of the failure modes) live in this pipeline:

| Stage | What happens | Common pitfall |
|---|---|---|
| **Ingestion** | Vendor feed (API, S3/SFTP drop, file) lands in storage | Schema drift between vendor versions silently breaks features |
| **Entity mapping** | Map vendor entities (merchants, brands, domains) to tradable tickers | Mis-mapping or ticker changes (M&A, re-listings) corrupt the panel |
| **Point-in-time alignment** | Stamp each datapoint with the date it was *actually available* | Using delivery-snapshot instead of as-of date injects lookahead — see [[lookahead-bias]] |
| **Normalisation** | Deseasonalise, panel-balance, control for coverage changes | Methodology changes by the vendor mimic a real signal |
| **Feature construction** | Turn raw data into a factor (YoY growth, surprise vs. consensus) | Over-fitting transformations to the backtest window |
| **Signal blending** | Combine with price/fundamental factors; orthogonalise vs. known factors | Redundancy with public data leaves no residual alpha |
| **Execution sizing** | Translate signal into capacity-constrained position | Edge exists only below the strategy's capital — see Capacity below |

**For systematic/quant funds**, alt data is most often consumed as a *factor*: regressed against forward returns with strict PIT alignment, orthogonalised against known style factors, and blended into a multi-signal model. The single highest-value check is whether the alt-data factor carries *residual* alpha after controlling for price, value, momentum, and the publicly available version of the same information.

**For discretionary/fundamental desks**, alt data is consumed as a *nowcast* — e.g. card-spend panels to estimate a consumer company's quarter ahead of the print, or foot-traffic to sanity-check a retail thesis. Here the value is forming a differentiated view before consensus, not a fully automated signal.

**For AI / LLM-based systems** (including agentic research pipelines), unstructured alt data — news, filings, reviews, transcripts, social — is increasingly consumed via NLP/LLM extraction: entity-tagging, sentiment scoring, event classification, and summarisation feed structured features downstream. The caveats compound: model hallucination, prompt-sensitivity, and the fact that headline-grade sentiment is already arbitraged within minutes (see Sentiment decay above) mean LLM-derived sentiment is best used for *coverage and structuring* of long-tail unstructured data rather than as a standalone fast signal. Adversarial verification and PIT discipline matter even more when an LLM sits in the loop.

## Data-Quality Caveats

Independent of category, these caveats recur and should be treated as a checklist before paying for any provider:

- **Survivorship and coverage drift** — panels that silently add or drop merchants/venues over time create artificial trends; demand a stable, documented methodology.
- **Panel representativeness** — a card panel skewed toward one demographic or bank does not generalise to total revenue; the bias can be stable (tolerable) or drifting (dangerous).
- **Restated / snapshot data** — many vendors expose only a current snapshot, not the as-of value; that is lookahead bias in disguise. See [[lookahead-bias]].
- **Latency vs. decision frequency** — real-time data adds nothing to a daily-rebalanced strategy; pay only for the latency you can actually act on.
- **Crowding** — vendors' public "trusted by" client logos reveal who else holds the data; widely-held data is, by construction, closer to priced-in.
- **Legal / ToS exposure** — scraped data may breach source-platform terms; location and card data raise privacy and de-identification questions; never ingest anything that could constitute material non-public information.

## How to Evaluate Alternative Data

A useful framework before paying for any alt data product:

### 1. Coverage and Latency
- How many tickers does it cover?
- What's the lag from underlying event to data delivery?
- Is the panel stable over time, or has the methodology changed?

### 2. Backtestability
- Is there point-in-time history?
- How long is the history?
- Can the vendor demonstrate the data was available *as of* each historical date, or is it a current snapshot reconstructed?

### 3. Capacity / Crowding
- How many other clients use this product?
- Has the underlying signal decayed?
- Is the vendor's customer list public? (Many vendors publish "trusted by" logos that reveal who else has the data.)

### 4. Cost vs. Edge
- What's the licensing cost?
- What capacity does the strategy support?
- Does the alt data signal hold up after transaction costs?

### 5. Legal and Ethical
- Does the data collection comply with the terms of service of the source platforms?
- Is the data anonymized and de-identified?
- Does the vendor have material non-public information (insider issues)?

## The Alpha-Decay Story

Alternative data has a brutal alpha-decay cycle:

1. **Years 1-2 after vendor launches:** small number of clients, real informational edge, potential Sharpe of 1-2 from alone using this single data source
2. **Years 3-5:** more clients, signal partially priced in, Sharpe drops to 0.5-1
3. **Years 5-10:** widely subscribed, signal mostly priced in within hours, residual Sharpe < 0.5
4. **Year 10+:** the data is table stakes; not having it puts you behind, but having it doesn't put you ahead

Most major alt-data products are now in stage 3 or 4. The frontier moves to newer, weirder, less-covered data sources — and the cycle repeats.

## When Alt Data Doesn't Pay

Many strategies fail to extract alpha from alt data even when the data is real, because:

1. **The signal is correlated with publicly available data** — if web traffic correlates with announced revenue and the announcement comes out before you can act, the alt data adds nothing
2. **The decision frequency doesn't match the data frequency** — daily-decision strategies don't benefit from real-time alt data
3. **The capacity is too small** — the edge exists but only at sub-million-dollar position sizes
4. **The execution costs eat the edge** — most alt-data-derived strategies trade many small positions, and slippage adds up

A good test: take the alt data, regress it against the *next-period stock return* with proper PIT alignment, and see if the residual alpha (after controlling for known factors) is non-zero. If not, the alt data is correlated with already-known signals — buying it adds cost without alpha.

## Sources

- [[alternative-data-alpha]] — strategies built on alt data
- [[alternative-data]] — concept page
- [[edge-taxonomy]] — alt data as informational edge
- General market knowledge; no specific wiki source ingested yet. Vendor names and cost ranges are public-domain reference points that change frequently — confirm current details with each provider.

## Related

- [[data-sources-overview]]
- [[paid-data-providers]]
- [[free-data-sources]]
- [[informational-edge]]
- [[crypto-data-sources]]
- [[lookahead-bias]]
- [[edge-taxonomy]]
