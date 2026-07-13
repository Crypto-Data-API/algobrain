---
title: "The Book of Alternative Data — Alexander Denev & Saeed Amen (2020)"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [education, book, machine-learning, alternative-data, nlp-sentiment-analysis, data-provider]
related:
  - "[[alternative-data]]"
  - "[[nlp-sentiment-analysis]]"
  - "[[machine-learning]]"
  - "[[feature-engineering-finance]]"
  - "[[ml-trading-pipeline]]"
  - "[[data-providers]]"
  - "[[alpha-vantage]]"
---

**The Book of Alternative Data: A Guide for Investors, Traders, and Risk Managers** by Alexander Denev and Saeed Amen (Wiley, 2020) is a leading reference on the rapidly growing [[alternative-data]] ecosystem. Alternative data is any information used by investors that falls outside traditional financial data (prices, fundamentals, filings). The book surveys the full landscape — [[nlp-sentiment-analysis|NLP]] on news and social media, satellite imagery, web scraping, credit-card transactions, app usage, geolocation/foot-traffic, and ESG data — and, more importantly, provides a disciplined framework for **evaluating** these datasets before spending money on them.

## Key Facts

| Field | Detail |
|-------|--------|
| **Authors** | Alexander Denev (risk-analytics expert) and Saeed Amen (quant; founder of Cuemacro; ex-Lehman, ex-Nomura) |
| **Published** | 2020 |
| **Publisher** | Wiley |
| **Full title** | *The Book of Alternative Data: A Guide for Investors, Traders, and Risk Managers* |
| **Scope** | Survey + evaluation framework across the major alternative-data categories |
| **Best-known contribution** | A structured framework for assessing dataset quality, coverage, history, uniqueness, and alpha decay |
| **Perspective** | Practitioner-grounded; honest about hype, cost, and edge erosion |
| **Companion concept page** | [[alternative-data]] |

## Core Thesis

In increasingly efficient markets, durable alpha comes from **information edges**, and [[alternative-data]] is the current frontier of such edges. But the value of any dataset is not its novelty — it is a function of measurable properties (quality, coverage, history length, uniqueness, timeliness) and a decaying half-life as adoption spreads. The book's organizing argument is therefore evaluative rather than evangelical: most "alternative" datasets are mediocre or already commoditized, and the discipline of *critically appraising a dataset* — and the legal, ethical, and operational costs of using it — matters more than chasing the latest exotic source.

## The Alternative-Data Evaluation Framework

For each data type the authors walk through a consistent appraisal: how the data is collected, what signal it provides, how to process it into tradeable features ([[feature-engineering-finance]]), what edge decay looks like, and real-world case studies. The recurring evaluation dimensions:

| Dimension | Question it answers |
|-----------|---------------------|
| Data quality | Is it clean, accurate, well-structured, and free of look-ahead bias? |
| Coverage | What fraction of the target universe (tickers, regions, sectors) does it span? |
| History length | Is there enough back-history to backtest robustly and avoid overfitting? |
| Uniqueness / scarcity | How many competitors already have it? (First-mover advantage is real and finite.) |
| Timeliness / frequency | How far ahead of official statistics or earnings does the signal arrive? |
| Cost & operational burden | Acquisition, storage, cleaning, and processing cost vs. expected alpha. |
| Legal & ethical risk | Privacy (PII), web-scraping terms, material non-public information concerns, ESG/compliance. |
| Alpha decay | How fast does the edge erode once the dataset is widely adopted (typically ~1–3 yr half-life)? |

## Chapter / Section Themes

- **What alternative data is and why it matters** — taxonomy, the data-vendor ecosystem, and the buyer/seller value chain.
- **Evaluating datasets** — the core framework above; building a structured scorecard for any vendor pitch.
- **[[nlp-sentiment-analysis|Natural language processing]]** — sentiment from news, social media, and earnings transcripts; entity extraction and event detection.
- **Satellite and geospatial imagery** — parking-lot car counts, oil-tanker and shipping movements, crop/agriculture monitoring.
- **Web-scraped data** — product reviews, pricing, job postings, and other public-web signals.
- **Transaction and consumer data** — credit-card panels and receipt data as near-real-time revenue proxies.
- **Mobile, app, and geolocation data** — downloads, MAUs, session metrics, and foot-traffic.
- **ESG data** — environmental/social/governance signals as both alpha and risk inputs.
- **Implementation and risk** — legal, privacy, and operational considerations; integrating features into a [[ml-trading-pipeline|pipeline]].

## Key Concepts and Takeaways

| Concept | Takeaway |
|---------|----------|
| Information edge | Alternative data is the frontier of alpha in efficient markets ([[alternative-data]]). |
| NLP sentiment | News/social/transcript sentiment is among the most established sources — quantifies qualitative info at scale ([[nlp-sentiment-analysis]]). |
| Satellite imagery | Real-time economic indicators (parking lots, tankers, crops) ahead of official statistics. |
| Web scraping | Reviews, pricing, and job postings reveal company trends invisible in filings. |
| Credit-card data | Near-real-time revenue estimates ~30–60 days ahead of quarterly earnings; high-conviction. |
| App / usage data | MAUs, sessions, and install/uninstall rates predict tech-company growth before earnings. |
| Geolocation | Mobile foot-traffic estimates store/restaurant/CRE performance at location level. |
| ESG | Increasingly an alpha and risk signal, not just compliance. |
| Alpha decay | Edges erode as adoption spreads; first movers win, with a ~1–3 yr half-life. |
| Evaluation first | Quality, coverage, and history length trump novelty — appraise before buying. |

## Criticisms and Limitations

- **Survey over implementation.** The book is more a landscape map and evaluation framework than a hands-on code/build guide; it contains limited end-to-end implementation detail.
- **Rapid obsolescence.** Published in 2020, several specific vendors, datasets, and price points are already dated; the *frameworks* age far better than the examples.
- **Vendor-showcase tone in places.** Some sections read as catalogues of providers, which can feel promotional rather than critically comparative.
- **Backtesting pitfalls under-emphasized.** Alternative data is especially prone to short histories, survivorship and selection bias, and look-ahead leakage — the book flags these but a practitioner needs deeper rigor (cross-reference [[ml-trading-pipeline]] and overfitting controls).
- **Cost/scale barrier glossed.** The economics that make most alternative data viable only for large, well-capitalized funds are acknowledged but not deeply quantified.

## Who Should Read This

Portfolio managers and quants deciding whether to invest in alternative data; systematic traders seeking signal sources beyond price and volume; data scientists moving into finance who need a map of what exists; and fund allocators assessing whether a manager's claimed "alternative-data edge" is genuine. Above all, anyone who has been pitched an alternative-data product and wants a rigorous framework for appraising it.

## How It Applies to AI Trading

Alternative data is the raw material that feeds an [[ml-trading-pipeline]] with features beyond price action. [[nlp-sentiment-analysis|NLP]] is the most accessible entry point — sentiment scores from news and social media that augment price-based features. The [[feature-engineering-finance]] surface expands dramatically once satellite-, web-, transaction-, and geolocation-derived features can sit alongside traditional inputs in the same [[machine-learning|ML]] model. The evaluation framework helps decide which [[data-providers]] are worth the cost and which "edges" are already commoditized. For traders using finviz, tradingview, or [[alpha-vantage]], the book contextualizes what they are missing and what more exotic data might add — while warning that the alpha half-life means the work of sourcing and validating new data never ends.

## Rating

**7/10** — The best available reference for understanding the alternative-data landscape and appraising datasets critically; the evaluation framework alone is worth the read. Marked down because the field evolves so fast that specific sources/vendors are already dated, the book is more survey than implementation guide, and some chapters lean promotional. The mental models, however, remain highly relevant even as individual datasets come and go.

## Related

- [[alternative-data]] — The concept page this book anchors
- [[nlp-sentiment-analysis]] — NLP on financial text, the most accessible technique
- [[machine-learning]] — The modeling layer that consumes alternative-data features
- [[feature-engineering-finance]] — Turning raw alternative data into model inputs
- [[ml-trading-pipeline]] — Alternative data as additional input features for ML models
- [[data-providers]] — Overview of data sources available to traders
- finviz / tradingview / [[alpha-vantage]] — Traditional data platforms for comparison

## Sources

General market knowledge; no specific wiki source ingested yet.
