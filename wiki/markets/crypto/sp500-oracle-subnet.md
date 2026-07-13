---
title: "S&P 500 Oracle (SN28)"
type: entity
created: 2026-04-19
updated: 2026-06-12
status: draft
tags: [crypto, bittensor, financial-oracle, trading]
aliases: ["SN28", "S&P 500 Oracle", "Foundry SN28"]
entity_type: protocol
headquarters: "Decentralized"
website: ""
related: ["[[bittensor]]", "[[bittensor-subnets]]", "[[dtao]]", "[[proprietary-trading-network]]", "[[synth-2]]", "[[precog]]", "[[oracle-feed]]", "[[chainlink]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# S&P 500 Oracle (SN28)

**S&P 500 Oracle** (SN28) is a Bittensor subnet that produces near-real-time, high-frequency price predictions and oracle feeds for the S&P 500 index and its constituents. Miners submit forecasts at short horizons (seconds-to-minutes); validators score realized accuracy. The subnet functions as a decentralized financial oracle, comparable in spirit to [[chainlink]] for price data but with a prediction/forecasting rather than pure price-reporting angle.

## How It Works

At each evaluation tick, miners submit a distribution over the target price at a specific forward horizon. Validators score miners on realized outcomes using calibration metrics (pinball loss, continuous ranked probability score). The subnet's top-scoring miners are aggregated into a consensus forecast consumable by validators and external applications.

## Trading Relevance

**Directly tradable.** SN28 is one of the clearest "financial oracle subnets" on Bittensor. Use cases:

- Consume SN28 forecasts as inputs to intraday equity / index futures strategies.
- Benchmark internal quant models against the SN28 consensus.
- Cross-check conventional sentiment and flow indicators against SN28's probability feeds.

Alpha-28 valuation is driven by whether the oracle attracts paying consumers (trading desks, DeFi applications needing S&P oracles, synthetic-asset protocols).

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]]
- [[proprietary-trading-network]] (SN8) -- signals rather than price oracle
- [[synth-2]] (SN50) -- synthetic financial data complement
- [[precog]] (SN55) -- crypto-price forecasting sibling
- [[oracle-feed]], [[chainlink]] -- non-Bittensor comparisons

## Sources

- taostats.io
- Foundry team (SN28 operator)
