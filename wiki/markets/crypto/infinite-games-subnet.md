---
title: "Infinite Games (SN6)"
type: entity
created: 2026-04-19
updated: 2026-07-16
status: draft
tags: [ai-trading, bittensor, crypto, prediction-markets]
aliases: ["Infinite Games", "SN6"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://infinitegames.xyz/"
related: ["[[bettensor]]", "[[bittensor-subnets]]", "[[bittensor]]", "[[crypto-markets]]", "[[dtao]]", "[[precog]]", "[[prediction-markets]]", "[[sportstensor]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Infinite Games (SN6)

**Infinite Games** (SN6) is a Bittensor subnet running AI-driven prediction markets and forecasting. The subnet hosts resolvable questions (binary, categorical, and continuous) across sports, finance, politics, and crypto; miners submit probabilistic forecasts; validators score calibration and accuracy against ground-truth outcomes.

## How It Works

Each question has a resolution date and a ground-truth source (official result, price oracle, or trusted verifier). Miners submit probability distributions at question open and update them up to the close. Validators compute Brier scores or log-loss scores against the realized outcome. High-scoring miners capture more emissions; losing miners are diluted out of the alpha pool over time.

## Trading Relevance

SN6 output is a **directly consumable forecasting feed**. A trader who subscribes to the subnet's top-ranked miner forecasts effectively has a consensus-weighted prediction over everything the subnet covers. Overlaps with SN30 [[bettensor|BetTensor]] (more betting-focused), SN41 [[sportstensor]] (sports-only), and SN55 [[precog]] (crypto-price-focused). Each subnet optimizes its reward function for a different slice of the prediction-market universe.

## History

SN6 was originally the **Masa** subnet before Masa migrated to SN42. The SN6 slot was subsequently taken over by the Infinite Games team, which pivoted the subnet to prediction markets.

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]] -- protocol context
- [[bettensor]], [[precog]], [[sportstensor]] -- sibling prediction-market subnets
- [[masa-subnet]] -- the Masa team, now at SN42
- [[prediction-markets]], [[event-driven-trading]] -- trading concepts

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

## See Also

- [[crypto-markets]]

---
