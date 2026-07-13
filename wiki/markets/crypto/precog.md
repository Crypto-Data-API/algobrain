---
title: "Precog (SN55)"
type: entity
created: 2026-04-19
updated: 2026-06-12
status: draft
tags: [crypto, bittensor, crypto-forecasting, prediction-markets]
aliases: ["SN55", "Precog"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://precog.ai/"
related: ["[[bittensor]]", "[[bittensor-subnets]]", "[[dtao]]", "[[proprietary-trading-network]]", "[[sp500-oracle-subnet]]", "[[bettensor]]", "[[infinite-games-subnet]]", "[[sportstensor]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Precog (SN55)

**Precog** (SN55) is a Bittensor subnet for cryptocurrency price forecasting. Miners submit probability distributions over BTC, ETH, and altcoin prices at short horizons (5min, 15min, 1h, 4h, 24h); validators score realized calibration and accuracy. The subnet produces a continuously-updated crypto-price forecasting feed.

## How It Works

At each evaluation tick, miners submit forward price distributions for each covered asset. Validators compute pinball loss or CRPS against realized prices at the forecast horizon. Top miners earn emission share; the consensus distribution is published as a decentralized price-forecast feed.

## Trading Relevance

**Directly tradable**: crypto traders can consume Precog's consensus forecasts as a short-horizon signal input, benchmark proprietary models against them, or run arbitrage against less-informed markets. The subnet is the crypto-price sibling of SN28 [[sp500-oracle-subnet|S&P Oracle]] (equity) and SN8 [[proprietary-trading-network|Taoshi PTN]] (multi-asset signals).

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]]
- [[proprietary-trading-network]] (SN8), [[sp500-oracle-subnet]] (SN28) -- sibling financial subnets
- [[bettensor]] (SN30), [[infinite-games-subnet]] (SN6), [[sportstensor]] (SN41) -- broader prediction-market family

## Sources

- precog.ai
- taostats.io
