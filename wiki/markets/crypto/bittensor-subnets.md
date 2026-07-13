---
title: "Bittensor Subnets"
type: concept
created: 2026-04-09
updated: 2026-04-19
status: good
tags: [crypto, ai-trading, machine-learning, defi]
aliases: ["Bittensor Subnets", "TAO Subnets"]
domain: [market-microstructure]
difficulty: advanced
related: ["[[bittensor]]", "[[dtao]]", "[[tao]]", "[[ai-agent-tokens]]", "[[defai]]", "[[artificial-intelligence]]", "[[decentralized-ai]]", "[[tokenized-compute]]", "[[ai-narrative-arc]]", "[[on-chain-inference]]", "[[bittensor-subnet-rotation]]", "[[alpha-token-arbitrage]]", "[[tao-validator-delegation]]"]
---

# Bittensor Subnets

**Subnets** are the core organizational unit of the [[bittensor|Bittensor]] network. Each subnet is a specialized marketplace where miners compete to provide AI/ML services and validators evaluate their outputs. TAO token emissions are distributed across subnets based on performance, creating a decentralized incentive market for artificial intelligence.

## How Subnets Work

Each subnet has three participants:

1. **Subnet owner**: Defines the task, evaluation criteria, and incentive structure
2. **Miners**: Compete to produce the best outputs for the subnet's task (predictions, text, data, computation)
3. **Validators**: Evaluate miner outputs and assign scores that determine TAO emissions distribution

The Bittensor root network allocates TAO emissions across subnets based on validator consensus about which subnets are producing the most valuable work.

## dTAO: The February 2025 Economic Upgrade

In February 2025 Bittensor migrated from **root-validator-voted** emissions to a **market-based allocation** mechanism known as [[dtao|dTAO]]. Each subnet now issues its own **alpha token** via a bonding curve denominated in TAO, and block emissions are allocated across subnets in proportion to the TAO-denominated market cap of each subnet's alpha pool.

This is the single most important context for trading anything subnet-related. The short version:

- Every subnet has an **alpha token** (alpha-1, alpha-8, alpha-64, etc.) with a bonding curve.
- Staking TAO into a subnet buys alpha tokens at the curve price; unstaking sells them back.
- Subnets with larger alpha market caps receive larger shares of each block's TAO emissions.
- Alpha tokens are therefore a **liquid retail instrument** for betting on individual AI subnets.

See [[dtao]] for the full mechanics.

## Notable Subnets (Post-dTAO Landscape)

The table below covers the most notable subnets as of April 2026. For category-wide coverage see [[bittensor#Subnets]]. For individual subnet pages, click through.

| Subnet | Name | Focus | Trading Relevance |
|---|---|---|---|
| **SN1** | [[apex-5\|Apex]] | LLM inference | LLM capability proxy |
| **SN3** | [[templar]] | Distributed LLM pretraining | Training infrastructure bet |
| **SN4** | [[targon]] | LLM inference | Inference demand |
| **SN5** | [[openkaito]] | AI-native search | Search/data infrastructure |
| **SN6** | [[infinite-games-subnet\|Infinite Games]] | Prediction-market AI | Prediction-market alpha |
| **SN8** | [[proprietary-trading-network\|Taoshi PTN]] | Trading signal network | **Direct: miners submit trade signals; signals can be subscribed** |
| **SN9** | [[iota-2\|IOTA]] | Distributed pretraining | Training infrastructure |
| **SN10** | [[sturdy-subnet\|Sturdy]] | DeFi yield optimization | **Direct: DeFi yield discovery** |
| **SN11** | [[dippy]] | Roleplay / character LLMs | Consumer AI |
| **SN13** | [[data-universe-subnet\|Data Universe]] | Social data scraping (X, Reddit) | **Direct: alternative data feed** |
| **SN17** | [[404-gen]] | 3D asset generation | Games / 3D AI |
| **SN18** | [[cortex-subnet\|Cortex]] | LLM inference API | Inference demand |
| **SN19** | [[nineteen-ai\|Nineteen]] | Image generation / multimodal | Consumer AI |
| **SN20** | [[bitagent-subnet\|BitAgent]] | Autonomous AI agents | Agent-economy exposure |
| **SN21** | [[omron-subnet\|Omron]] | Verifiable ML / zkML | Infrastructure for on-chain AI |
| **SN24** | [[omega-labs]] | Any-to-any multimodal | Multimodal research |
| **SN28** | [[sp500-oracle-subnet\|S&P 500 Oracle]] | Financial price oracle | **Direct: tradable financial oracle** |
| **SN29** | [[coldint]] | Distributed fine-tuning | Training |
| **SN30** | [[bettensor]] | AI-powered prediction markets | **Direct: prediction-market alpha** |
| **SN32** | [[its-ai-subnet\|It's AI]] | AI-text detection | Moderation tooling |
| **SN34** | [[bitmind]] | Deepfake detection | Trust/safety infrastructure |
| **SN38** | [[distributed-training-subnet\|Distributed Training]] | Training network | Infrastructure |
| **SN39** | [[w-ai-parked\|Basilica]] | Decentralized compute | Infrastructure / GPU marketplace |
| **SN41** | [[sportstensor]] | Sports data + predictions | **Direct: sports-betting alpha** |
| **SN42** | [[masa-subnet\|Masa]] | Real-time decentralized data | Alternative data feed |
| **SN44** | [[score]] | Audio / music scoring | Creative AI |
| **SN50** | [[synth-2\|Synth]] | Synthetic financial data | **Direct: training data for quant models** |
| **SN51** | [[celium]] | Decentralized GPU marketplace | Infrastructure / compute |
| **SN52** | [[dojo]] | RLHF data labeling | Training-data infrastructure |
| **SN53** | [[efficient-frontier-subnet\|Efficient Frontier]] | Quant portfolio optimization | **Direct: portfolio signals** |
| **SN55** | [[precog]] | Crypto price forecasting | **Direct: tradable crypto predictions** |
| **SN56** | [[gradients]] | AutoML fine-tuning | Training tooling |
| **SN62** | [[ridges-ai\|Ridges AI]] | AI software engineer | Coding agent |
| **SN64** | [[chutes]] | Serverless GPU inference | **Compute infrastructure; one of the largest alpha caps** |
| **SN68** | [[nova-3\|NOVA]] | Small-molecule drug discovery | Science-AI |
| **SN75** | [[hippius]] | Decentralized storage | Infrastructure |
| **SN81** | [[patrol-tao-com\|Patrol]] | On-chain data intelligence | Data infrastructure |
| **SN85** | [[vidaio]] | Video AI / upscaling | Media AI |
| **SN93** | [[bitcast]] | Creator-monetization AI | Consumer AI |
| **SN120** | [[affine]] | Reasoning benchmark | Evaluation infrastructure |

Subnets marked **Direct:** have explicit, present-day trading relevance -- they either produce tradable signals / data, or their domain is prediction markets / financial oracles.

## Why Subnets Matter

Bittensor's subnet architecture is unique in crypto because it creates **genuine economic incentives for AI quality**, reinforced by dTAO making emission share a market-driven variable. Unlike most AI tokens where the token is disconnected from the technology, TAO emissions flow to miners who produce the best AI outputs, and alpha tokens let retail traders bet on specific subnet futures. Practical implications:

- Subnet performance metrics are a live, tradable proxy for the state of decentralized AI capability.
- Alpha tokens give retail direct exposure to specific AI verticals without running infrastructure.
- Compute / data subnets (SN51 Celium, SN64 Chutes, SN39 Basilica, SN13 Data Universe, SN42 Masa) have captured outsized emission share post-dTAO because their revenue is measurable.

## Trading Relevance

Subnet-level trading has three dimensions post-dTAO:

1. **Direct alpha-token speculation** -- buy alpha-N if you believe subnet N will gain emission share. See [[alpha-token-arbitrage]].
2. **Consumption of subnet output** -- SN8 Taoshi signals, SN28 S&P oracle, SN50 Synth synthetic data, SN41 Sportstensor, SN55 Precog, SN10 Sturdy DeFi yield, SN53 Efficient Frontier are consumable APIs a trading shop can plug into.
3. **Structural rotation** -- rotate staked TAO between subnets tracking emission-share momentum. See [[bittensor-subnet-rotation]]. Validators can also be delegated to for combined dividend+alpha yield. See [[tao-validator-delegation]].

## Post-2024 Reset and the Shift Toward Verifiable Output

Bittensor did not escape the broader 2025 AI token reset. Like most AI-narrative tokens, TAO was caught in the sector-wide drawdown covered in [[ai-narrative-arc#Phase 3b The 2025 AI Token Reset numeric scale|Phase 3b]] of the AI narrative arc — collectively AI tokens lost approximately 75% year-over-year by Q4 2025, and eight of the top ten AI-category tokens posted losses exceeding 70% over that window (Source: [[2026-04-11-perplexity-ai-crypto-gaps]]).

The more interesting development for Bittensor was not the price action but the **narrative restructure** that followed. By early 2026, the surviving AI×crypto projects — Bittensor among them — had visibly shifted their marketing and roadmap emphasis away from agent-autonomy hype and toward **verifiable outputs, measurable compute utilization, and institutional-grade evaluation frameworks**. Several practical effects:

- **Subnet quality became the headline metric**, not subnet count. Projects that launched dozens of subnets with minimal validator scrutiny were penalized by TAO holders; projects with a smaller number of high-quality, measurable subnets saw relative outperformance
- **Integration with verifiable inference infrastructure** (see [[on-chain-inference]], [[statistical-proof-of-execution]], and [[restaking-and-ai]]) became a credible story for how subnet outputs could become usable by on-chain DeFi consumers, rather than just existing as off-chain API services
- **Tokenomic restructures** across the broader AI category focused on tying emissions to real usage fees rather than to raw participation metrics — a trend that eventually pressured Bittensor's own incentive design as well

For a trader, the cleanest framing is that Bittensor is now in the **post-speculation infrastructure phase** of its lifecycle: the narrative valuation has unwound, the technology is real, and the question is whether subnet output quality translates into real-world integration and fee revenue over the next 1–3 years. This is a different question from the 2024 "will AI agents take over crypto" framing that drove TAO's original multi-thousand-dollar peaks.

## See Also

- [[bittensor]] — TAO token and network overview
- [[ai-agent-tokens]] — Broader AI token landscape
- [[defai]] — DeFi + AI convergence
- [[decentralized-ai]] — Parent movement
- [[tokenized-compute]] — Adjacent economic-model framing
- [[ai-narrative-arc]] — The 2024–2026 cycle including Bittensor's reset
- [[on-chain-inference]] — Adjacent integration target
- [[artificial-intelligence]] — AI section hub
