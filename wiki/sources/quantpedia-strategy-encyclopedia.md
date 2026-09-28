---
title: "Quantpedia — Encyclopedia of Quantitative Trading Strategies (free-tier harvest, 2026-09-28)"
type: source
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [strategy-development, quantitative, anomalies, backtesting, crypto, forex, commodities, futures]
aliases: ["Quantpedia strategy encyclopedia", "Quantpedia free strategies"]
source_type: data
source_url: "https://quantpedia.com/strategies/"
source_author: "Quantpedia (Radovan Vojtko et al.)"
source_date: 2026-09-28
confidence: medium
claims_count: 24
related: ["[[quantpedia]]", "[[external-strategy-sources]]", "[[alpha-decay]]", "[[data-snooping-and-p-hacking]]", "[[bitcoin-overnight-seasonality]]", "[[crypto-rebalancing-premium]]", "[[bitcoin-max-min-breakout]]", "[[commodity-skewness-strategy]]", "[[volume-oi-conditioned-reversal]]", "[[currency-value-ppp]]", "[[dollar-carry-trade]]"]
---

# Quantpedia — Encyclopedia of Quantitative Trading Strategies

A harvest (2026-09-28) of the free-tier strategy entries on [[quantpedia|Quantpedia]] (quantpedia.com), restricted to entries relevant to this wiki's scope: cryptocurrencies, currencies, commodities, and multi-asset futures. Quantpedia summarises academic papers into standardised strategy cards (rules, backtest period, headline return/volatility/Sharpe/max drawdown, source paper). Entry pages were fetched directly; the free list page was fetched as rendered on the harvest date.

> **Confidence: MEDIUM overall.** Quantpedia is a secondary source: each card paraphrases a paper (or a sell-side index) and reports the *paper's* in-sample, pre-cost statistics. The underlying papers range from peer-reviewed journals (HIGH) to Quantpedia's own working papers and bank research notes (MEDIUM). None of the performance figures below are net of costs, and most predate the [[alpha-decay|McLean–Pontiff publication decay]] window. Treat every number as "the source claims", not as expected live performance.

## Provenance

| | |
|---|---|
| **Publisher** | Quantpedia (Bratislava, Slovakia) |
| **Access** | Free tier (sign-up) for ~65-70 strategies; Premium/Pro for 900+ |
| **Fetched** | 2026-09-28 (strategy cards, pricing page, crypto research hub, blog) |
| **Nature** | Curated summaries of academic/industry research |
| **Independence** | Quantpedia authors some of the underlying papers themselves (Vojtko, Padyšák, Hanicová, Dujava, Ďurian) |

## Claims extracted

### About the platform

1. `[HIGH]` Quantpedia's free tier exposes roughly 65-70 strategy cards; the list fetched on 2026-09-28 contained ~80 entries, overwhelmingly equities. (Direct observation.)
2. `[MEDIUM]` Paid tiers (Prime, Premium, Pro) unlock "900+" strategies, 1,000+ linked papers, and — Pro only — ~800 out-of-sample backtests with Python code, API access and portfolio modelling across 200+ ETFs and ~40 cryptocurrencies. (Pricing page, 2026-09-28.)
3. `[MEDIUM]` Third-party sources quote Premium at ~$449 (3 months), ~$599 (12 months), ~$1,199 (3 years); pricing was not visible on the fetched page, so figures may be stale.
4. `[HIGH]` Each strategy card reports: rebalancing period, markets traded, backtest period, annualised return, volatility, Sharpe, max drawdown, complexity, and the source paper plus related papers. (Direct observation.)
5. `[HIGH]` Only two of the ~80 free cards on 2026-09-28 were crypto-specific (#0701 rebalancing premium, #0753 overnight Bitcoin seasonality); most crypto research sits in the blog or Premium tier.

### Crypto entries

6. `[MEDIUM]` **Overnight seasonality in Bitcoin (#0753)** — long BTC 22:00-00:00 UTC every day; source claims ~33% p.a., 20.9% vol, Sharpe 1.58, max DD −34% over 2015-2021 on Gemini data, pre-cost. Source: Padyšák & Vojtko (2022), "Seasonality, Trend-following, and Mean reversion in Bitcoin". → [[bitcoin-overnight-seasonality]]
7. `[MEDIUM]` The proposed mechanism is that 22:00-00:00 UTC is when most major equity venues (US, Europe, Asia-Pacific) are closed, leaving BTC as one of the few liquid venues for flow.
8. `[MEDIUM]` **Rebalancing premium in cryptocurrencies (#0701)** — long a daily-rebalanced equal-weight basket of 27 coins, short 70% of a buy-and-hold equal-weight basket; source claims 7.65% p.a., 2.6% vol, Sharpe 2.93 over 2018-2021, while the card also lists max DD −99.99% (an internal inconsistency on the card). Source: Hanicová & Vojtko (2021). → [[crypto-rebalancing-premium]]
9. `[MEDIUM]` **Bitcoin MAX/MIN strategies** (blog, 2024-09-12, Beluská) — buying BTC at a new 10-day high (trend) and at a new 10-day low (reversion) both worked in-sample (2015-02/2022); out-of-sample 2022-2024 the MAX leg held up while the MIN leg underperformed materially. → [[bitcoin-max-min-breakout]]
10. `[MEDIUM]` The same 2024 study found no robust day-of-week pattern in BTC; apparent strong days were judged random.

### FX entries

11. `[HIGH]` **FX carry (#0005)** — long 3 highest-rate, short 3 lowest-rate currencies from a 10-20 G-currency universe, monthly; card cites the Deutsche Bank carry index 1989-2009: 7.27% p.a., 9.6% vol, Sharpe 0.29, max DD −32%. → note on [[carry-trade]]
12. `[HIGH]` **Currency momentum (#0008)** — long 3 / short 3 by 12-month return vs USD; DB index 1989-2009: 7.61% p.a., Sharpe 0.30, max DD −46%; Menkhoff et al. find up to 10% p.a. winner-loser spread 1976-2010; card notes deteriorating out-of-sample alpha. → note on [[currency-momentum]]
13. `[MEDIUM]` **Currency value / PPP (#0009)** — long 3 most undervalued, short 3 most overvalued vs OECD PPP (CPI-adjusted monthly); DB 1989-2009: 7.82% p.a., 9.3% vol, Sharpe 0.36, max DD −39%; card flags deteriorating out-of-sample alpha. → [[currency-value-ppp]]
14. `[HIGH]` **Dollar carry (#0129)** — long USD vs a 10-currency developed basket when the 3-month T-bill exceeds the basket's average forward discount, short otherwise; 1983-2009: 5.6% p.a., 8.5% vol, Sharpe 0.66, max DD −32%. Source: Lustig, Roussanov & Verdelhan (2009/2014), "Countercyclical Currency Risk Premia". → [[dollar-carry-trade]]

### Commodity and futures entries

15. `[HIGH]` **Term structure effect (#0022)** — long top-20% roll-yield commodities, short bottom-20%, monthly; 1979-2004: 11.7% p.a., 23.8% vol, Sharpe 0.49, max DD −78%. Source: Fuertes, Miffre & Rallis (2008). → note on [[commodity-carry-strategy]]
16. `[HIGH]` **Momentum effect in commodities (#0021)** — listed at 14.6% p.a. (card headline); cross-sectional commodity momentum. → note on [[commodity-momentum]]
17. `[MEDIUM]` **Skewness effect in commodities (#0281)** — long 3 lowest-skew, short 3 highest-skew of 22 futures by 12-month skewness, monthly; 1990-2022: 9.51% p.a., 11.6% vol, Sharpe 0.82, max DD −17.5%. Source: Dujava & Vojtko (2023); related Fernandez-Perez et al. → [[commodity-skewness-strategy]]
18. `[MEDIUM]` **Return asymmetry in commodity futures (#0664)** — ranks 22 futures by an asymmetry measure (IE) on 260 daily returns, long bottom 7 / short top 7; 1991-2021: 4.36% p.a., 7.5% vol, Sharpe 0.58, max DD −47.6%; correlation with the skewness strategy ~0.46. Source: Ďurian & Padyšák (2020). → variant on [[commodity-skewness-strategy]]
19. `[HIGH]` **Short-term reversal with futures (#0071)** — weekly contrarian on 24 US futures, restricted to contracts with rising volume and falling open interest; 1983-2000: 29.6% p.a., 31.4% vol, Sharpe 0.82, max DD −58.7%. Source: Wang & Yu (2004), "Trading Activity and Price Reversals in Futures Markets". → [[volume-oi-conditioned-reversal]]
20. `[HIGH]` **Time-series momentum (#0118)** — long assets with positive 12-month excess return, short negative, volatility-scaled; 1965-2009 across 58 futures: Sharpe 1.31 (card), max DD −34%. Source: Moskowitz, Ooi & Pedersen (2012). → note on [[time-series-momentum]]
21. `[MEDIUM]` **WTI/Brent spread (#0100)** — fade deviations of the spread from its 20-day SMA; 1995-2004 claim 9.9% p.a., Sharpe 0.88, max DD −69%, with "slightly negative" out-of-sample performance. Source: Evans, Dunis & Laws. → note on [[geographic-spread-trading]]

### Cross-cutting

22. `[HIGH]` Several cards (currency momentum, currency value, WTI/Brent) explicitly flag deteriorating out-of-sample alpha — consistent with the publication-decay evidence on [[alpha-decay]].
23. `[MEDIUM]` Headline performance figures on cards are not cost-adjusted; high-turnover entries (weekly futures reversal, daily crypto rebalancing, daily 2-hour BTC window) are the most exposed to cost erosion.
24. `[LOW]` Quantpedia's crypto research hub also lists studies on BTC futures-expiration effects, exchange reserves, Google Trends and news as predictors — not harvested here (Premium or blog-only).

## Pages this source contributed to

- Created: [[quantpedia]], [[bitcoin-overnight-seasonality]], [[crypto-rebalancing-premium]], [[bitcoin-max-min-breakout]], [[commodity-skewness-strategy]], [[volume-oi-conditioned-reversal]], [[currency-value-ppp]], [[dollar-carry-trade]]
- Updated with variant notes: [[carry-trade]], [[currency-momentum]], [[commodity-carry-strategy]], [[commodity-momentum]], [[time-series-momentum]], [[geographic-spread-trading]], [[wti-brent-spread]], [[short-term-reversal]], [[rebalancing]]

## Related

- [[quantpedia]] · [[external-strategy-sources]] · [[crypto-idea-generation]] · [[alpha-decay]] · [[data-snooping-and-p-hacking]] · [[research-checklist]]
