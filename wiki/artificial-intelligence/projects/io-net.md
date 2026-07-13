---
title: "io.net"
type: entity
created: 2026-04-09
updated: 2026-06-10
status: good
tags: [crypto, ai-trading, machine-learning]
aliases: ["io.net", "IO", "Internet of GPUs"]
entity_type: protocol
founded: 2022
headquarters: "Decentralized"
website: "https://io.net"
related: ["[[nvidia-ai]]", "[[model-inference-vs-training]]", "[[akash-network]]", "[[render-token]]", "[[aethir]]", "[[ai-agent-tokens]]", "[[solana]]", "[[artificial-intelligence]]"]
---

# io.net

**io.net** is a [[solana|Solana]]-based decentralized GPU compute network (DePIN) that aggregates underutilized GPUs from data centers, crypto miners, and consumer hardware into clusters for AI/ML workloads. Founded in 2022 by Ahmad Shadid (originally as infrastructure for a quant-trading system), it aims to undercut AWS/GCP/Azure pricing for AI [[model-inference-vs-training|training and inference]]. Its IO token is also a cautionary case study in DePIN token performance: down ~97% from its June 2024 launch-day high by mid-2026.

## Key Facts (as of June 2026)

| Field | Detail |
|---|---|
| **Token** | IO (Solana SPL; listed on Binance June 11, 2024) |
| **Price / Market cap (June 2026)** | ~$0.16-0.17; market cap ~$55M; FDV ~$128M |
| **Supply** | ~346M circulating of 800M max |
| **All-time high** | $6.44 on June 12, 2024 (CoinMarketCap) — i.e., −97% to June 2026 |
| **Hardware offered** | NVIDIA H100/H200 clusters, plus consumer-grade GPUs |
| **Funding** | $30M Series A (March 2024) led by Hack VC; backers incl. Multicoin, Solana Labs, OKX/Aptos ecosystems |

## History and Governance

- **2022** — founded by Ahmad Shadid; pivoted from powering an in-house quant fund to a general GPU marketplace
- **March 2024** — $30M Series A at reported ~$1B valuation
- **June 2024** — IO token generation event and Binance listing; days later, **Shadid stepped down as CEO** amid controversy over inflated/spoofed GPU-supply counts (fake "GPU metadata" exposed by researchers); COO **Tory Green** took over
- **2024-2026** — network refocused on verified enterprise-grade supply (H100/H200 clusters), an inference API ("io.intelligence"), and partnerships across the Solana DePIN ecosystem; token price nonetheless ground down with the broader DePIN/AI-token sector

## How It Works

- GPU owners connect hardware to the network and earn IO for verified uptime and jobs
- Users rent clusters for AI training, inference, or rendering at rates below hyperscaler pricing
- The network orchestrates distributed workloads across available GPUs (Ray-based clustering)
- Payment in IO or USDC; block rewards subsidize supply-side growth (disinflationary emission schedule)

## Competitive Landscape

| Network | Focus | Differentiator |
|---------|-------|---------------|
| **io.net** | GPU clustering for ML | Large aggregated GPU supply, Solana-native |
| [[akash-network|Akash]] | General cloud compute | Kubernetes-based, broadest workloads |
| [[render-token|Render]] | GPU rendering + AI | Creator-focused, Hollywood-grade |
| [[aethir|Aethir]] | Enterprise GPU cloud | Enterprise partnerships, gaming |
| [[nvidia-ai|NVIDIA]] (centralized) | GPU hardware | Hardware monopoly, CUDA ecosystem |

## Trading Relevance

- IO trades as a high-beta proxy for the DePIN/AI-compute narrative; it correlates with [[ai-agent-tokens|AI-token]] sentiment and, loosely, NVDA
- **Token-launch lesson**: IO's −97% drawdown from its day-one high illustrates the structural pattern of high-FDV, low-float 2024 launches — unlock schedules and emissions overwhelmed demand
- The supply-spoofing scandal (June 2024) is a canonical due-diligence case: verify DePIN supply metrics independently before trading the narrative
- GPU utilization and pricing on decentralized networks provide a free signal of marginal AI compute demand vs the [[nvidia-ai|NVIDIA]]/hyperscaler complex
- The decentralized compute thesis still depends on breaking NVIDIA's CUDA moat — unproven as of 2026

## Related

- [[nvidia-ai]] — Centralized GPU hardware provider
- [[model-inference-vs-training]] — The compute economics io.net addresses
- [[akash-network]], [[render-token]], [[aethir]] — Competing networks
- [[ai-agent-tokens]] — Broader AI token landscape
- [[solana]] — Host chain
- [[artificial-intelligence]] — AI section hub

## Sources

- io.net official site and docs: https://io.net
- CoinMarketCap, io.net (price, supply, ATH): https://coinmarketcap.com/currencies/io-net/
- Kraken, IO price page: https://www.kraken.com/prices/io.net
- CoinDesk/The Block coverage of Ahmad Shadid's resignation and GPU-count controversy (June 2024)
- Verified via Perplexity (sonar), 2026-06-10 (price ~$0.16, mcap ~$55M, FDV ~$128M)
