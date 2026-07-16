---
title: "SingularityNET"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-agent-tokens, ai-trading, crypto, machine-learning]
aliases: ["AGIX", "SNET", "SingularityNET"]
entity_type: protocol
founded: 2017
headquarters: "Decentralized"
website: "https://singularitynet.io/"
related: ["[[ai-agent-tokens]]", "[[artificial-intelligence]]", "[[crypto-markets]]", "[[decentralized-ai]]", "[[ethereum]]", "[[ocean-protocol]]"]
---

# SingularityNET

**SingularityNET** (AGIX) is a decentralized marketplace and protocol for [[artificial-intelligence|AI]] services, where developers can publish AI/ML algorithms as on-chain "agents" that anyone can discover, call, and pay for using the network's token. Co-founded by AI researcher Ben Goertzel, the project's long-term ambition is to build a decentralized network of interacting AI agents as a path toward artificial general intelligence (AGI). It ranks **#840** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

As of 2026-06-22, AGIX trades at **$0.080426** with a market cap of about **$19.53M** (rank **#840**). The token was down **-1.92%** over 24 hours and a notable **-12.79%** over the trailing 7 days — **materially weaker than peers** — amid a risk-off regime ([[bitcoin|BTC]] near $64,508, with the Crypto [[fear-and-greed-index|Fear & Greed Index]] at 21, "Extreme Fear") and the ongoing token-merger transition described below. The pronounced 7-day drawdown is consistent with migration-related uncertainty and illiquidity in the legacy AGIX ticker as supply converts to the unified ASI token.

> **Token-merger context (ASI Alliance):** In 2024, SingularityNET (AGIX), Fetch.ai (FET), and [[ocean-protocol|Ocean Protocol]] (OCEAN) announced the **Artificial Superintelligence (ASI) Alliance** and agreed to merge their tokens into a single unified token (FET, rebranded **ASI**) at fixed conversion ratios — AGIX and OCEAN holders convert to ASI at predefined rates. The goal is to pool decentralized-AI liquidity, talent, and compute. Because migration rolls out in phases and exchange/wallet support differs, the **AGIX ticker can continue to be quoted and traded on some venues during/after migration**. The figures above reflect the AGIX ticker as quoted on 2026-06-22; holders should verify the official, current conversion/migration status directly with the projects before acting, since legacy and merged tokens can coexist and price independently during the transition.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AGIX |
| **Market Cap Rank** | #840 |
| **Market Cap** | $19,529,193 |
| **Current Price** | $0.080426 |
| **24h Change** | -1.92% |
| **7d Change** | -12.79% |
| **Genesis Date** | 2017-12-21 |
| **Merger** | Part of the ASI Alliance (Fetch.ai + SingularityNET + Ocean) token unification |
| **Categories** | Artificial Intelligence (AI), AI Agents, Cardano Ecosystem, Ethereum Ecosystem |
| **Website** | [https://singularitynet.io/](https://singularitynet.io/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

SingularityNET is a decentralized marketplace for [[artificial-intelligence|AI]] services. Its thesis is that there is a gap between the researchers and academics who build AI tools and the businesses that want to consume them, and that most organizations need more customized, composable AI than any single vendor provides. SingularityNET lets developers wrap AI/[[machine-learning|ML]] models as network "agents," advertise them in a marketplace, and get paid per call, while consumers can chain multiple agents together to solve larger problems.

The project's long-term vision (associated with co-founder Ben Goertzel and the OpenCog lineage) is a self-organizing network of interacting AI agents that can route work to whichever agent performs a sub-task best — a substrate the team frames as a route toward decentralized AGI. The widely publicized humanoid robot **Sophia** (Hanson Robotics) has been used as a flagship demonstration of multi-agent AI coordination. See also [[decentralized-ai]] and [[ai-agent-tokens]].

---

## Architecture and Mechanism

- **AI service marketplace** — developers register AI agents (e.g., NLP, vision, generative, analytics services) on-chain; the network handles discovery, calling, and metered micropayment.
- **Agent composition** — a coordinating agent can subcontract sub-tasks to specialized agents and pay them in the network token, enabling complex AI pipelines from simple parts.
- **Token role** — the network token (historically AGI, then AGIX, migrating to ASI) is the medium of exchange for AI services, a staking asset, and the [[governance-token|governance]] asset for the SingularityNET ecosystem and its associated DAO/funding programs (e.g., Deep Funding).
- **Multi-chain** — SingularityNET has operated across Ethereum and Cardano, and the ASI merger consolidates token economics across the alliance.

### Ecosystem and Spin-outs

SingularityNET is the hub of a broader constellation of AI-focused projects, several of which have their own tokens and roadmaps:

- **Deep Funding** — a community-governed grants program that crowdsources and funds AI development on the network, allocating treasury resources to teams building agents and tooling. It is SingularityNET's principal mechanism for directing capital toward useful AI services rather than pure speculation.
- **OpenCog Hyperon** — the open-source AGI research framework (descended from the OpenCog lineage) that underpins the project's long-term cognitive-architecture ambitions.
- **Spin-out tokens** — the ecosystem has incubated specialised projects such as **NuNet** (decentralized compute), **SingularityDAO** (DeFi/portfolio management), **Rejuve** (longevity), and **HyperCycle** (AI micro-ledger infrastructure), illustrating a hub-and-spoke model where SingularityNET seeds vertical AI applications.

### Value Accrual

The network token (AGI → AGIX → ASI) is meant to capture value as the **medium of exchange for metered AI-service calls**, plus staking and governance utility. In practice, paid on-chain demand for AI services has historically been small relative to AGIX's market capitalization, so the token has traded predominantly on the **decentralized-AI narrative** and on the AGI vision associated with co-founder Ben Goertzel, rather than on realised service revenue. The ASI merger redirects long-term value accrual into the unified token's economics, which holders should evaluate at the consolidated level rather than via legacy AGIX alone.

---

## History

- **2017** — SingularityNET founded by Ben Goertzel and team; ICO conducted, raising significant capital during the 2017 boom. AGI token launched.
- **2019** — Phase II expansion; deeper ties to the OpenCog AGI research lineage and to Cardano for scalability.
- **2021–2023** — AGI token redenominated to **AGIX**; ecosystem programs (Deep Funding) launched to crowdsource AI development.
- **2024 — ASI Alliance** — SingularityNET joined Fetch.ai and [[ocean-protocol|Ocean Protocol]] to form the Artificial Superintelligence Alliance, merging AGIX (and OCEAN) into a unified token (FET → ASI) at fixed ratios. Migration proceeded in phases; legacy AGIX quotes have persisted on some venues during transition.

---

## Worked Example: Composing AI Agents on the Marketplace

Suppose a small business wants an automated pipeline that ingests customer-support voicemails and returns a sentiment-tagged summary:

1. **Discover** — it browses the SingularityNET marketplace and selects three published **agents**: a *speech-to-text* agent, a *summarization* agent, and a *sentiment-analysis* agent, each registered by independent developers.
2. **Orchestrate** — a coordinating agent chains them: voicemail → text (agent A) → summary (agent B) → sentiment label (agent C).
3. **Meter & pay** — each sub-call is metered and the developers are paid per invocation in the network token. The business never has to host any model itself; the developers earn recurring micropayments for their specialised models.

This composition-of-specialists pattern — routing each sub-task to whichever agent does it best and settling payment automatically — is the core product idea and the practical seed of the project's "network of interacting AI agents" AGI thesis.

---

## ASI Alliance Member Comparison

The three legacy tokens converging into the unified **ASI** token occupy distinct niches in the decentralized-AI stack:

| Project | Token (legacy) | Role in the AI stack | Core product |
|---|---|---|---|
| **Fetch.ai** | FET (→ becomes **ASI**) | **Agents & compute** — autonomous economic agents and infrastructure | Agentverse / agent framework, the surviving unified token |
| **SingularityNET** | AGIX (→ ASI) | **AI services marketplace** — publish/call AI models as agents | SingularityNET marketplace, Deep Funding, OpenCog Hyperon |
| **[[ocean-protocol\|Ocean Protocol]]** | OCEAN (→ ASI) | **Data layer** — the fuel for AI training and inference | Ocean Market, Compute-to-Data, Predictoor |

The merger's logic is vertical integration of decentralized AI: **data (Ocean) + services/models (SingularityNET) + agents/compute (Fetch.ai)** under one liquid token. The trade-off is the loss of independent token-level exposure to each sub-thesis plus the operational complexity (and the kind of legacy-ticker illiquidity visible in AGIX's -12.79% 7-day move) inherent in a phased, multi-asset, multi-chain migration.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 245.73M AGIX |
| **Total Supply** | 442.50M AGIX |
| **Max Supply** | 2.00B AGIX |
| **Fully Diluted Valuation** | $46.47M |
| **Market Cap / FDV Ratio** | 0.56 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.46 (2024-03-10) |
| **Current vs ATH** | -92.81% |
| **All-Time Low** | $0.00747159 (2020-03-13) |
| **Current vs ATL** | +1305.79% |
| **24h Change** | -3.01% |
| **7d Change** | -0.85% |
| **30d Change** | +63.15% |
| **1y Change** | -36.59% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x5b7533812759b45c2b44c19e320ba2cd2681b542` |
| Sora | `0x005e152271f8816d76221c7a0b5c6cafcb54fdfb6954dd8812f0158bfeac900d` |
| Cardano | `f43a62fdc3965df486de8a0d32fe800963589c41b38946602a0dc53541474958` |

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0X5B7533812759B45C2B44C19E320BA2CD2681B542/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |
| Uniswap V3 (Ethereum) | 0X5B7533812759B45C2B44C19E320BA2CD2681B542/0XAEA46A60368A7BD060EEC7DF8CBA43B7EF41AD85 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://singularitynet.io/](https://singularitynet.io/) |
| **Twitter** | [@SingularityNET](https://twitter.com/SingularityNET) |
| **Reddit** | [https://www.reddit.com/r/SingularityNetsub/](https://www.reddit.com/r/SingularityNetsub/) |
| **Telegram** | [singularitynet](https://t.me/singularitynet) (10,371 members) |
| **Discord** | [https://discord.gg/snet](https://discord.gg/snet) |
| **GitHub** | [https://github.com/singnet/singnet](https://github.com/singnet/singnet) |
| **Whitepaper** | [https://public.singularitynet.io/whitepaper.pdf](https://public.singularitynet.io/whitepaper.pdf) |

---

## Risks

- **Token-migration / coexistence risk** — AGIX is converting to the unified ASI token. Legacy and merged tokens can trade at the same time at different prices; the recent 7d underperformance (-12.79%, materially worse than the BTC tape) coincides with transition uncertainty and thin legacy-ticker liquidity. **Confirm official conversion ratios, deadlines, and supported venues directly with the projects before acting.**
- **Adoption / utility risk** — paid demand for on-chain AI services has historically been modest relative to the token's market value; much of the valuation reflects narrative rather than metered usage.
- **Narrative-dependence / volatility risk** — AGIX is a high-beta [[ai-agent-tokens|AI token]]; sentiment toward decentralized AI can swing sharply, and the asset is sensitive to broad [[bitcoin|BTC]]-led moves.
- **Liquidity / small-cap risk** — at ~$20M market cap (rank ~#832), AGIX is small and volatile.
- **Execution risk** — the AGI ambition is extremely long-horizon and unproven; competition from centralized AI providers is intense.
- **General crypto risk** — smart-contract bugs, regulatory uncertainty, and bear-market drawdowns.

*Nothing here is investment advice; figures are point-in-time snapshots that can change rapidly.*

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[artificial-intelligence]]
- [[decentralized-ai]]
- [[ai-agent-tokens]]
- [[ocean-protocol]]
- [[machine-learning]]
- [[governance-token]]
- [[cardano]]
- [[fear-and-greed-index]]
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge (incl. publicly announced ASI Alliance token merger); no specific narrative wiki source ingested yet.

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2,395.55 |
| **Market Cap Rank** | #908 |
| **24h Range** | $0.0686 — $0.0711 |
| **Last Updated** | 2026-07-16 |

---
