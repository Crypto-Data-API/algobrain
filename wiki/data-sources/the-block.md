---
title: "The Block"
type: source
created: 2026-05-03
updated: 2026-06-12
status: good
tags: [data-provider, crypto, research, news]
aliases: ["The Block", "TheBlock", "TheBlock.co"]
source_type: data
source_url: "https://www.theblock.co"
source_author: "The Block"
confidence: high
related: ["[[crypto-data-sources]]", "[[messari]]", "[[coingecko]]", "[[dune-analytics]]"]
---

The Block is a crypto-native media and data company that combines news, long-form research, and a paid data terminal (The Block Pro) used by traders, analysts, and funds. Its dashboards span DEX volumes, stablecoin supply, derivatives open interest, prediction markets, and other on-chain and exchange-level metrics, making it a common cross-check alongside [[messari]], [[coingecko]], [[dune-analytics]], and [[defillama]].

## Background

- **Founded:** 2018 by Mike Dudas, originally as a crypto news outlet
- **Editorial focus:** Markets, regulation, infrastructure, and emerging crypto sectors
- **Ownership:** Acquired by Foresight Ventures (Forrest Bai) in 2023; the deal valued the publication and its data product as a unified asset
- **Controversy:** In December 2022, reporting tied to the [[ftx-collapse]] revealed that Alameda Research had loaned roughly $27M to The Block's parent company, with portions used by then-CEO Michael McCaffrey for personal real estate. McCaffrey resigned. Subsequent leadership emphasized editorial independence, but the episode is frequently cited when evaluating the publication's neutrality on FTX-related coverage
- **Positioning:** Crypto-focused, English-language, B2B-leaning -- the audience skews toward funds, traders, and protocol teams rather than retail

## Products

### The Block (free media)
- News articles, opinion, podcasts (e.g. *The Scoop*), and event coverage
- Free public dashboards summarizing high-level market metrics
- Useful as a daily news feed but not the main reason traders pay for The Block

### The Block Pro
- Subscription data terminal aimed at professional users
- Private research notes, expanded dashboards, custom data exports
- API access for some datasets (subject to plan)
- Email briefings and analyst calls

### The Block Research
- Long-form quarterly reports and ad hoc deep dives (sector reports on L2s, RWAs, DePIN, prediction markets, etc.)
- Often commissioned or sponsored, which is disclosed but worth noting when reading
- Reports tend to surface category data earlier than mainstream financial press

### Data Dashboards
- DEX volumes by protocol and chain
- Stablecoin supply, mint/burn flows, and dominance
- Derivatives -- futures and perp open interest, funding rates, options volume
- NFT marketplace volumes
- Prediction market activity, including [[polymarket]] and [[kalshi]] tracking
- Mining and staking metrics

## Trading Relevance

- **Prediction market monitoring:** The Block maintains regularly updated dashboards on [[polymarket]] volumes and resolution activity, and tracks [[kalshi]] event contract turnover. For traders running event-driven or arb strategies between centralized event markets and crypto-native ones, these dashboards are a quick way to size opportunity flow without writing custom Dune queries
- **DEX vs CEX rotation:** Tracking weekly DEX share of spot volume helps gauge when on-chain liquidity is gaining or losing ground -- a useful input for venue-selection and slippage modeling
- **Stablecoin flow:** Mint/burn data on USDT, USDC, DAI, and newer issuers acts as a proxy for fresh capital entering or leaving the system, and is often used as a risk-on/risk-off signal
- **Derivatives positioning:** Aggregated funding-rate and OI data makes it easier to spot crowded longs/shorts before squeezes -- complementary to exchange-native dashboards and to [[cryptoquant]]
- **Sector early-warning:** The Block Research is frequently early on emerging narratives (e.g., RWA, restaking, intent-based protocols, AI agents). For thematic traders, the reports are useful even when the data is later replicated on free platforms

## How It Compares

- **vs [[messari]]:** Messari leans heavier on token-by-token fundamentals, governance tracking, and standardized financial reports. The Block is stronger on sector-level dashboards, prediction markets, and editorial research
- **vs [[dune-analytics]]:** Dune is raw, customizable, SQL-driven on-chain data. The Block is curated and pre-packaged. Use Dune when you need a specific question answered; use The Block when you want a maintained dashboard on a standard metric
- **vs [[coingecko]] / CoinMarketCap:** Those are price-and-listing aggregators. The Block goes well beyond prices into research, derivatives, and on-chain flow data
- **vs [[defillama]]:** DefiLlama is free, open, and best-in-class for TVL and DEX data; The Block's DEX dashboards overlap heavily but sit behind a paywall and add editorial context

## Pricing

- **Free tier:** News, podcasts, and a subset of public dashboards
- **The Block Pro:** Paid subscription, typically priced in the several-hundred-USD-per-year range for individuals, with higher tiers for teams and enterprise data feeds. Refer to [theblock.co](https://www.theblock.co) for current pricing
- **Custom/Enterprise:** Bespoke data feeds and API access negotiated separately

## Limitations

- **Paywall:** The most useful dashboards and research sit behind The Block Pro, limiting access for small traders
- **Less customizable than Dune:** Dashboards are curated, not user-editable; if the cut you want is not on the page, you cannot reshape it
- **Update lag:** Some dashboards refresh daily rather than in real time, which is fine for positioning analysis but not for execution
- **Coverage skew:** Editorial focus has historically leaned toward US/EU and major-cap assets; emerging-market and long-tail coverage is thinner than crypto-native aggregators
- **Independence questions:** The Alameda funding episode and the Foresight Ventures acquisition both raise legitimate questions about coverage neutrality on related entities. Cross-check sensitive claims against [[messari]], on-chain data via [[dune-analytics]], or primary sources

## Related

- [[crypto-data-sources]] -- broader catalog of crypto data providers
- [[messari]] -- closest competitor on research and data
- [[dune-analytics]] -- raw, SQL-driven on-chain analytics
- [[defillama]] -- free TVL and DEX data
- [[coingecko]] -- price and listings aggregator
- [[polymarket]] -- a key dataset in The Block's prediction-market dashboards
- [[kalshi]] -- regulated US event-contract exchange tracked alongside Polymarket
- [[ftx-collapse]] -- context for the 2022 Alameda funding controversy

## Sources

- General knowledge -- The Block product structure, ownership history, and 2022 Alameda funding disclosures as widely reported in crypto press at the time of the [[ftx-collapse]]
- Publicly available information from theblock.co regarding products and dashboards
