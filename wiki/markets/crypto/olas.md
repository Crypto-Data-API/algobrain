---
title: "Olas (Autonolas)"
type: entity
created: 2026-04-11
updated: 2026-06-12
status: draft
tags: [crypto, ai-trading, agents, defi]
aliases: ["Autonolas", "OLAS", "Open Autonomy"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://olas.network/"
related: ["[[ai-agent-tokens]]", "[[ai-trading-agents]]", "[[defai]]", "[[eliza-framework]]", "[[decentralized-ai]]", "[[ai-agent-daos]]", "[[ai-prediction-markets]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Olas (Autonolas)

**Olas** (OLAS, formerly Autonolas) is a decentralized protocol and framework for building, owning, and operating **autonomous services** — long-running off-chain programs that act on behalf of users or DAOs. It is one of the longest-standing AI agent projects in crypto, predating the 2024 agent narrative by several years, and its "Open Autonomy" framework has been used by real prediction-market bots, DeFi trading bots, and consumer-facing agent apps.

## Architecture

Olas's core abstraction is the **autonomous service**: a set of off-chain agents running in a byzantine-fault-tolerant consensus, with a blockchain-anchored service registry that governs ownership, rewards, and upgrades.

- **Service registry** — on-chain contracts that record which services exist, who owns them, and how they're operated
- **Open Autonomy framework** — the Python-based software stack for building multi-agent services
- **OLAS emissions + bonding** — liquidity and developer incentives funded through bonding curves and token emissions

The distinctive property: Olas services are **multi-agent by construction**. A single autonomous service is a cluster of agents running consensus, so you get Byzantine-fault tolerance for free. This is closer to a distributed-systems view of AI agents than the single-LLM-in-a-loop view favored by [[eliza-framework|Eliza]] and newer frameworks.

## Key Integrations

Olas hosts several production autonomous services worth naming individually because they illustrate the range of the platform:

- **Pearl** — a consumer-facing "agent app store" that lets users run Olas agents on their own machines and earn
- **Babydegen** — a family of autonomous trading agents for DeFi yield optimization
- **Olas Predict** — prediction-market agents that autonomously trade on Polymarket and similar venues, using LLM-classified event outcomes
- **Agent Academy** — developer onboarding for building new services

## Tokenomics

OLAS uses a combination of protocol-owned liquidity (funded by bonding) and continuous emissions to developers of active services. Service developers can bond their service with the registry to receive OLAS rewards proportional to verified activity. The model favors long-lived, genuinely active services over short-lived launches — a structural contrast to agent-launchpad models like [[virtual-protocol|Virtuals]].

## Honest Assessment

Olas is the **technically most sophisticated** AI agent protocol in crypto by most objective measures: longest history, deepest framework, real production services with measurable usage. It is also the **least narratively successful** of the major AI agent tokens by a wide margin, and its market cap reflects this. The gap between "objective technical quality" and "market cap" is a recurring pattern in crypto — see the broader [[ai-narrative-arc|AI narrative arc]] discussion — and is not unique to Olas.

For a trader, Olas is interesting precisely because the gap is wide. If the AI agent narrative eventually rewards real product-market fit over launch hype, Olas is structurally positioned to benefit. If the narrative continues to reward whichever platform has the flashiest agent launches, Olas will continue to underperform. Both outcomes are plausible.

## See Also

- [[ai-agent-tokens]] — Full AI token landscape
- [[ai-agent-daos]] — Generalized concept
- [[eliza-framework]] — Contrasting agent-framework approach
- [[defai]] — DeFi + AI parent narrative
- [[decentralized-ai]] — Parent movement
- [[artificial-intelligence]] — AI section hub

## Sources

- Olas documentation at olas.network
