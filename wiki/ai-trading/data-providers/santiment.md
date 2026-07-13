---
title: "Santiment"
type: entity
created: 2026-04-06
updated: 2026-04-06
status: good
tags: [data-provider, crypto, sentiment]
entity_type: company
website: https://santiment.net
related:
  - "[[glassnode]]"
  - "[[nansen]]"
  - "[[laevitas]]"
---

# Santiment

## Overview

Crypto analytics platform combining social sentiment analysis, on-chain metrics, and development activity tracking into a single product. Santiment's core differentiator is its social data engine: it scrapes Twitter, Reddit, Telegram, Discord, and other platforms to build real-time sentiment scores for thousands of crypto tokens. The thesis is that extreme sentiment -- whether euphoria or fear -- is a contrarian indicator. When everyone is screaming "to the moon," the top is likely in. When despair dominates, accumulation opportunities emerge. Beyond sentiment, Santiment also provides on-chain metrics and a unique development activity tracker that measures actual GitHub commit activity for crypto projects.

## Pricing

- **Free (Sanbase)**: basic charts, limited metrics, 3-month historical data
- **Pro**: ~$50/mo -- full metric access, API, 2+ years history, alerts
- **Business**: ~$300/mo -- custom integrations, advanced API, bulk data, team features
- SAN token can be staked for discounted access

## What You Get (vs Free)

- Full social sentiment data with granular time resolution (free shows aggregated daily only)
- Complete on-chain metrics library: network activity, holder distribution, whale tracking
- Development activity scores for 2,000+ crypto projects (unique to Santiment)
- API access (SanAPI) for pulling data into quantitative models and trading bots
- Custom alerts on sentiment spikes, whale movements, and development changes
- Historical data going back years for [[backtesting]] sentiment-based strategies

## Alpha Edge

- **Sentiment extremes predict reversals**: Santiment's social volume and weighted sentiment metrics have strong historical correlation with local tops and bottoms. A spike in social volume combined with extreme positive sentiment frequently marks a local top for altcoins
- **Development activity as fundamental signal**: projects with consistently high developer activity tend to outperform long-term. Conversely, declining development activity is an early warning sign before price declines. This metric is unavailable from most other providers
- **Whale accumulation signals**: tracking large holder (whale) balance changes reveals institutional positioning before it shows up in price
- **Network Realized Profit/Loss**: aggregate on-chain profit-taking or loss realization across all holders -- similar to [[glassnode]]'s SOPR but with Santiment's own methodology
- **Social divergence**: when price rises but social sentiment stays flat or negative, it suggests sustainable appreciation rather than hype-driven pumps

## Key Features

- **Sanbase**: web dashboard with interactive charts for all social, on-chain, and development metrics
- **Social Trends**: real-time tracking of trending topics, emerging narratives, and sentiment shifts across crypto social media
- **Development Activity**: GitHub-based scoring of actual coding activity (not vanity metrics like stars/forks)
- **Whale Tracking**: monitoring large holder balance changes and wallet behavior
- **SanAPI**: GraphQL API for programmatic access to all metrics
- **Alerts**: custom notifications for sentiment spikes, whale movements, and social volume anomalies
- **Insights**: community-driven research and analysis platform

## Who Uses It

- Crypto traders using sentiment as a contrarian indicator for entries and exits
- Long-term investors evaluating project health through development activity metrics
- Quantitative researchers building multi-factor crypto models incorporating social data
- Fund managers monitoring narrative shifts and emerging trends in real time
- Content creators and analysts sourcing data for crypto market commentary
- Anyone who has experienced the pain of buying a token at peak social hype and wants data to avoid it next time

Complements [[glassnode]] (deep Bitcoin on-chain focus) and [[nansen]] (wallet-level intelligence) with a unique emphasis on social and development signals.
