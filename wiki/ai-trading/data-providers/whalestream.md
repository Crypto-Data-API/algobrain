---
title: "WhaleStream"
type: entity
created: 2026-05-06
updated: 2026-06-10
status: good
tags: [data-provider, options, stocks]
aliases: ["Whale Stream", "WhaleStream.com"]
entity_type: company
website: https://www.whalestream.com
related:
  - "[[unusual-whales]]"
  - "[[optionstrat]]"
  - "[[opra]]"
  - "[[polygon-io]]"
  - "[[spotgamma]]"
  - "[[gamma-squeeze]]"
  - "[[0dte-trading]]"
---

# WhaleStream

Web-based options flow analytics platform that scans the entire US options market in real time, filters out retail noise, and surfaces large institutional ("whale") trades. WhaleStream consumes [[opra|OPRA]] data, applies its own filtering algorithm to highlight notable orders, and presents them in a feed designed for discretionary flow-based traders. It positions itself as a lower-cost alternative to [[unusual-whales]], with a retail subscription listed at $69/month (or $690/year) as of June 2026. For traders, WhaleStream's value is as a curated institutional-positioning signal: a real-time feed of large sweeps and blocks used to seed directional ideas, confirm momentum, and read sentiment into catalysts.

## Overview

WhaleStream's premise is that institutional options activity leaves visible footprints in the tape: outsized contract sizes, sweeps across multiple exchanges, far out-of-the-money bets with short-dated expiries, and unusual volume relative to open interest. By filtering OPRA's full-market feed in real time, WhaleStream attempts to separate signal from the millions of small retail orders that dominate raw flow data. The output is a curated stream of "whale" trades that traders use to infer where and when institutions are positioning -- both for directional ideas and for reading sentiment around catalysts like earnings, [[fomc-meetings|Fed meetings]], or macro events.

Dark pool data on the platform is delayed by 15 minutes, consistent with FINRA's reporting rules for off-exchange equity prints. Lit options flow is real time.

## Pricing

Pricing verified on whalestream.com as of June 2026:

- **Subscription**: **$69/month** or **$690/year** (annual saves ~17%, roughly two months free)
- **Trial**: 7-day trial available
- The platform also publishes free public market-data pages (e.g. daily "top options flow" summaries), which serve as a limited preview of the paid feed

Earlier retail tiers were advertised around ~$50/mo; the listed price has since consolidated at $69/mo. Direct competitor pricing reference: [[unusual-whales]] entry-level plans start around $48-75/mo and scale to several hundred per month for institutional features. WhaleStream's retail tier is broadly comparable but with a different feature mix.

## What You Get / Key Features

- **Real-time options flow feed**: tickers, strikes, expiries, premium paid, side (bid/ask), sweep flag, and exchange detail
- **Whale filter**: proprietary algorithm tags trades likely to be institutional based on size, premium, and order routing
- **Dark pool prints**: delayed 15 minutes; useful as a confirmation layer alongside options activity
- **Watchlists and alerts**: notification when flow exceeds size or premium thresholds on user-selected tickers
- **Historical flow lookup**: review past whale trades on a ticker to see how prior positioning resolved
- **Sweep vs block tagging**: distinguishes urgency-driven sweeps (multi-exchange, taking liquidity) from negotiated blocks
- **Sector and index dashboards**: aggregate flow by sector or index component to spot rotation
- **OPRA-sourced**: full market coverage, not a sampled feed

## Use Cases / Who Uses It

- Discretionary options traders looking for directional ideas seeded by institutional positioning
- [[0dte-trading|0DTE]] traders monitoring same-day call/put sweeps for momentum confirmation
- Swing traders front-running or fading large bets on earnings, M&A, or macro catalysts
- Traders watching for [[gamma-squeeze]] setups via concentrated short-dated call buying
- Retail traders priced out of [[bloomberg-terminal|Bloomberg]] or institutional flow services who still want a curated tape
- Anyone using flow as one input alongside [[spotgamma|GEX analytics]], [[unusual-whales]], or chart-based signals

## Strengths and Limitations

**Strengths**

- Lower price point than most institutional flow services
- OPRA-sourced full-market coverage rather than sampled or partial feeds
- Real-time lit flow with minimal latency for the retail tier
- Web-based, no terminal install required

**Limitations**

- Dark pool data is 15 minutes delayed (a regulatory limit, not a vendor choice -- but worth noting vs services that present "live" dark pool prints which are by definition delayed too)
- Whale-detection heuristics are proprietary and not fully transparent; some flagged trades are still hedges or spreads, not directional bets
- Smaller community and ecosystem than [[unusual-whales]]; fewer third-party integrations
- Does not replace deeper analytics like [[spotgamma|gamma exposure]] modeling or [[optionstrat|payoff analysis]]
- Like all flow services, it shows what was traded -- not why -- and reading hedges as directional bets is a common error

## Status (June 2026)

WhaleStream is an active, live product as of June 2026: the site publishes current pricing ($69/mo / $690/yr), a 7-day trial, and public market-data pages with daily options-flow summaries dated through June 2026. The product is described as a web-based application combining real-time options flow with dark pool and equity print monitoring. No acquisition, rename, or shutdown has been reported.

## Related

- [[unusual-whales]] -- closest competitor in the retail options flow space
- [[optionstrat]] -- options strategy builder commonly used alongside flow services
- [[spotgamma]] -- complementary gamma exposure analytics
- [[opra]] -- the underlying market data feed
- [[polygon-io]] -- raw OPRA data API for traders building their own flow tools
- [[options-greeks]]
- [[gamma-squeeze]]
- [[0dte-trading]]
- [[dark-pools]]

## Sources

- WhaleStream official site and pricing -- https://www.whalestream.com (verified live with current pricing, June 2026)
- WhaleStream public market-data pages -- https://www.whalestream.com/market-data/top-options-flow
- Bullish Bears, "WhaleStream Review" -- https://bullishbears.com/whalestream-review/
- The European Business Review, "WhaleStream Review: A Comprehensive Look at the Trading Platform" -- https://www.europeanbusinessreview.com/whalestream-review-a-comprehensive-look-at-the-trading-platform-revolutionising-retail-investing/
- Status, pricing, and product description verified via Perplexity (sonar, high search context), 2026-06-10.
