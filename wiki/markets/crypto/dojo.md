---
title: "Dojo (SN52)"
type: entity
created: 2026-04-19
updated: 2026-06-12
status: draft
tags: [crypto, bittensor, ai, rlhf, data-labeling]
aliases: ["SN52", "Dojo"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://dojo.network/"
related: ["[[bittensor]]", "[[bittensor-subnets]]", "[[dtao]]", "[[coldint]]", "[[templar]]", "[[iota-2]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Dojo (SN52)

**Dojo** (SN52) is a Bittensor subnet that crowdsources RLHF-style data labeling and preference annotation. Human miners provide preference rankings and structured feedback on AI outputs; validators score annotation quality and consistency. The subnet produces labeled datasets that are useful for fine-tuning and alignment work.

## How It Works

Tasks are presented to human labelers (the "miners" in this subnet's unusual configuration). Labelers rank model outputs, answer questions, or provide structured feedback. Validators cross-check labeler consistency against expert references and internal agreement metrics.

## Trading Relevance

Training-data infrastructure exposure. Dojo's output (high-quality preference data) feeds into the other training subnets (Templar, IOTA, Coldint) -- making it structurally complementary to the pretraining and fine-tuning stack.

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]]
- [[templar]] (SN3), [[iota-2]] (SN9), [[coldint]] (SN29) -- downstream training subnets that consume labeled data

## Sources

- dojo.network
- taostats.io
