---
title: "The Book of Alternative Data — Alexander Denev & Saeed Amen (2020)"
type: source
created: 2026-04-07
updated: 2026-04-07
status: good
tags: [book, machine-learning, alternative-data, nlp-sentiment-analysis, data-provider]
aliases: ["The Book of Alternative Data", "Denev Amen Alternative Data"]
related: ["[[nlp-sentiment-analysis]]", "[[feature-engineering-finance]]", "[[ml-trading-pipeline]]", "[[finviz]]", "[[tradingview]]", "[[alpha-vantage]]", "[[data-providers]]", "[[the-book-of-alternative-data]]"]
source_type: book
source_author: "Alexander Denev, Saeed Amen"
source_date: 2020
confidence: high
claims_count: 10
---

The definitive practitioner guide to the alternative data ecosystem for investment management, authored by Alexander Denev (risk analytics expert) and Saeed Amen (former quant at Lehman Brothers and Nomura, founder of Cuemacro). The book surveys the full landscape of non-traditional data sources used by investors — NLP for text analysis, satellite imagery, web scraping, credit card transactions, app usage data, geolocation/foot traffic, and ESG data — providing evaluation frameworks for assessing data quality, signal strength, alpha decay, and cost-effectiveness. The authors bring practitioner credibility and critical perspective to a field often dominated by vendor hype.

## Key Claims

1. [HIGH] **Alternative data provides information advantages unavailable from traditional price/fundamental data**: Traditional financial data (prices, volumes, financial statements, SEC filings) is available to all market participants simultaneously. Alternative data — satellite imagery, credit card transactions, social media sentiment, web scraping — provides information asymmetries that can generate alpha in otherwise efficient markets. The growth of alternative data is the current frontier of information-based competitive advantage. (Source: Denev, Amen)

2. [HIGH] **NLP applied to news, social media, and earnings transcripts generates sentiment-based trading signals**: Natural language processing techniques quantify the sentiment, topics, and entities in financial text at a speed and scale impossible for human analysts. Sentiment scores derived from news flow, social media (Twitter, Reddit), and earnings call transcripts have been shown to predict short-term price movements, particularly around event windows (earnings, Fed announcements). (Source: Denev, Amen)

3. [HIGH] **Satellite imagery provides real-time economic indicators before official data releases**: Satellite imagery analysis — counting cars in retail parking lots, monitoring oil storage tank levels via shadow analysis, tracking shipping vessel movements, assessing crop health via multispectral imaging — produces economic indicators that lead official government statistics by weeks or months. This temporal advantage translates directly into trading alpha. (Source: Denev, Amen)

4. [HIGH] **Web scraping of product reviews, job postings, and pricing data reveals company-level trends**: Systematic web scraping produces company-level intelligence: declining product review scores signal quality problems before they appear in financials, accelerating job postings reveal expansion plans, and competitive pricing data shows market positioning shifts. These signals provide fundamental insights at a higher frequency than quarterly financial reports. (Source: Denev, Amen)

5. [HIGH] **Credit card transaction data provides near-real-time revenue estimates ahead of quarterly earnings**: Aggregated, anonymized credit card transaction data from payment processors provides revenue estimates for consumer-facing companies 30-60 days before official quarterly earnings reports. This is one of the highest-conviction alternative data sources, with multiple academic studies and practitioner case studies demonstrating its predictive power for earnings surprises. (Source: Denev, Amen)

6. [HIGH] **App download and usage data predicts technology company growth trajectories**: Monthly active users, daily active users, session duration, install/uninstall rates, and app store rankings provide granular growth metrics for technology companies. These metrics are available at weekly or daily frequency, far ahead of the quarterly KPIs reported in earnings releases. Anomalies in app usage patterns (sudden declines, viral growth) generate tradeable signals. (Source: Denev, Amen)

7. [HIGH] **Geolocation/foot traffic data from mobile phones estimates retail store performance**: Aggregated, anonymized GPS data from mobile phone location services estimates foot traffic at individual retail locations, restaurants, and commercial properties. Year-over-year traffic changes at the store level predict same-store sales growth, enabling company-level revenue estimates from location-level data aggregation. (Source: Denev, Amen)

8. [MEDIUM] **ESG data is increasingly a source of alpha and risk management**: Environmental, social, and governance (ESG) data — carbon emissions, labor practices, board diversity, regulatory compliance — is transitioning from a compliance/values screening tool to a source of alpha. Companies with improving ESG scores tend to outperform on a risk-adjusted basis, possibly because ESG improvements proxy for management quality and operational efficiency. The evidence is growing but not yet conclusive. (Source: Denev, Amen)

9. [HIGH] **The alternative data market is growing rapidly — first movers gain edge that erodes as data becomes commoditized**: Alternative data edges have a finite half-life. When a dataset is new and few investors use it, the information advantage is large. As the dataset becomes widely available and adopted, alpha decays — typically over 1-3 years. This creates a continuous race for newer, more unique data sources. The economics favor large firms that can afford to buy and process data early. (Source: Denev, Amen)

10. [HIGH] **Data quality, coverage, and history length are the primary evaluation criteria for alternative datasets**: The authors' evaluation framework assesses alternative datasets on: data quality (accuracy, completeness, consistency), coverage (what fraction of the investable universe is covered), history length (how many years of backfill are available for backtesting), timeliness (latency from event to data availability), uniqueness (how many competitors have the same data), and cost. Datasets failing on quality, coverage, or history are not worth pursuing regardless of theoretical alpha. (Source: Denev, Amen)

## Concepts Referenced

- [[nlp-sentiment-analysis]], [[alternative-data]]
- [[feature-engineering-finance]], [[ml-trading-pipeline]]
- [[data-providers]], [[finviz]]
- [[tradingview]], [[alpha-vantage]]
- [[esg-investing]], [[web-scraping]]

## Pages Backed

- [[nlp-sentiment-analysis]] — NLP for financial text as the most established alternative data technique
- [[feature-engineering-finance]] — alternative data features (satellite, NLP, transaction) for ML models
- [[ml-trading-pipeline]] — alternative data as additional feature inputs for ML-based trading systems
- [[data-providers]] — framework for evaluating alternative data vendors and sources
