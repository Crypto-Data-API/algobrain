---
title: "Auki Labs"
type: entity
created: 2026-04-09
updated: 2026-06-22
status: excellent
tags: [crypto, altcoins, defi, machine-learning]
aliases: ["AUKI", "Auki", "Posemesh"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.auki.com/"
related: ["[[crypto-markets]]", "[[base]]", "[[depin]]", "[[artificial-intelligence]]"]
---

# Auki Labs

**Auki Labs** (AUKI) is a [[depin|decentralized physical infrastructure network (DePIN)]] for **spatial computing and machine perception** — building what it calls the "real-world web," a way for robots and devices like smart glasses and phones to browse, navigate, and search physical locations. Its core protocol, the **posemesh**, is a collaborative, decentralized machine-perception network that gives robots and XR/AR devices a shared, persistent understanding of physical space. As of 2026-06-22 AUKI trades at **$0.00578705**, ranked **#714** by market cap (~$25.6M).

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AUKI |
| **Market Cap Rank** | #714 |
| **Market Cap** | ~$25.62M |
| **Current Price** | $0.00578705 |
| **24h Change** | +1.64% |
| **7d Change** | +2.40% |
| **Categories** | AI, Augmented Reality, Metaverse, DePIN, Robotics, Base / Peaq Ecosystem, Outlier Ventures Portfolio |
| **Website** | [https://www.auki.com/](https://www.auki.com/) |

---

## Overview

Auki Labs aims to make the physical world accessible to [[artificial-intelligence|AI]] by building the "real-world web" — infrastructure that lets robots and digital devices (smart glasses, phones) browse, navigate, and search physical locations. At its foundation is the **posemesh** protocol: a collaborative, decentralized machine-perception network that gives robots and XR devices a shared, persistent understanding of physical space, paired with a token economy for exchanging spatial data and compute. The thesis is that most economic activity remains tied to physical locations, so giving AI a spatial-reasoning layer over the real world is a large untapped market.

The network targets physical-AI applications such as warehouse/retail robotics, autonomous navigation, app-free augmented reality, and spatially aware smart glasses. Auki publicizes integrations with robotics vendors (e.g., Unitree, EngineAI, Padbot, Slamtec) and tracks on-chain activity via a public burn tracker on Dune ([dune.com/auki/stats](https://dune.com/auki/stats)). Auki has published an annual "State of the Auki Network" report summarizing demonstrations and adoption. *(Adoption, revenue, and integration claims originate from the project itself and are not independently verified here; treat them as marketing until corroborated by on-chain or third-party data.)*

---

## Architecture — How It Works

Auki's core is the **posemesh**, a decentralized, collaborative **machine-perception** network that gives devices a shared, persistent model of physical space — conceptually a decentralized "AR cloud" or spatial map that any participating robot or XR device can read from and write to.

1. **The localization / mapping problem.** For a robot, smart-glasses headset, or phone to act usefully in a room, it must answer "where am I, precisely, relative to the world?" — the *localization* problem. Doing this per-device, from scratch, is expensive and produces siloed maps. A *shared* spatial map lets many devices localize against the same coordinate frame and reuse each other's perception.
2. **The posemesh (decentralized spatial map).** The posemesh stores spatial anchors and machine-perception data in a decentralized, device-agnostic network. A device contributes localization/mapping data and, in return, can localize against the shared map — so the "pose" (position + orientation) of devices and objects is a network-level shared resource rather than a per-app silo. This is the source of Auki's "real-world web" framing: a queryable spatial layer over physical locations.
3. **Token-incentivized DePIN economy.** Node operators that contribute mapping/localization and compute resources earn rewards; devices and applications spend [[depin|DePIN]] credits (AUKI) to consume spatial data and machine-perception compute. A documented **burn** mechanism ties a token sink to network usage, tracked publicly on the project's Dune dashboard.

**Why decentralized?** A shared spatial map is naturally a *commons* — its value rises with the number of contributors and devices, and a neutral, open, token-incentivized network can in principle out-cooperate siloed proprietary AR-cloud services. The bet is that **physical AI** (humanoid/warehouse robots, smart glasses) scales and that those devices want a neutral spatial layer rather than each vendor's walled garden. *(Whether that adoption materializes — and is not captured by closed incumbents — is the central open question; see Risks.)*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.91B AUKI |
| **Total Supply** | 9.99B AUKI |
| **Max Supply** | 10.00B AUKI |
| **Fully Diluted Valuation** | $59.13M |
| **Market Cap / FDV Ratio** | 0.39 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0606 (2025-01-26) |
| **All-Time Low** | $0.00416096 (2026-02-05) |
| **24h Change (to 2026-06-22)** | +1.64% |
| **7d Change (to 2026-06-22)** | +2.40% |

AUKI sits roughly 90% below its January 2025 all-time high near $0.06, a deep multi-year drawdown common to early DePIN/metaverse-adjacent tokens. Into 2026-06-22 the token was modestly green over both 24h (+1.64%) and 7d (+2.40%), holding up better than peers (e.g. [[perle]]) during a market-wide **Extreme Fear** episode (Fear & Greed 21, [[bitcoin|BTC]] ~$64,508).

---

## Token Role & Mechanism

AUKI is the unit of account for the posemesh economy: devices and applications spend AUKI to access spatial data and machine-perception compute, while node operators that contribute mapping/localization and compute resources earn rewards. A documented **burn** mechanism ties token sink to network usage (tracked on the project's Dune dashboard). As with all [[depin|DePIN]] tokens, the long-run question is whether real usage-driven burns and demand outpace incentive emissions; a sub-$26M cap implies the market is pricing adoption as early and unproven.

### Value Accrual & Governance

- **Usage burn (the sink).** Spending AUKI to consume spatial data / machine-perception compute is burned (per the documented mechanism), so genuine network usage is deflationary — the cleanest value-accrual lever, and one that is *publicly observable* on the Dune burn tracker.
- **Operator rewards (the source).** Node operators earn AUKI for contributing mapping/localization and compute. The health question is whether usage-driven burns keep pace with these emissions.
- **Governance.** As the native token, AUKI is positioned to govern the posemesh economy as it decentralizes.

With ~39% of supply circulating (MC/FDV ≈ 0.39 — comparatively healthier than several peers in this batch) and a public burn dashboard, Auki offers more on-chain transparency than most early DePIN tokens; the open question is the *absolute level* of usage, which a sub-$26M cap implies is still early.

---

## Platform & Chain Information

**Native Chain:** Base

### Contract Addresses

| Chain | Address |
|---|---|
| Base | `0xf9569cfb8fd265e91aa478d86ae8c78b8af55df4` |
| Peaq | `0xf67db9d00401d9e883208882f5c100d7482b083d` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.auki.com/](https://www.auki.com/) |
| **Twitter** | [@Auki](https://twitter.com/Auki) |
| **Telegram** | [AukiNetwork](https://t.me/AukiNetwork) (14,765 members) |
| **Discord** | [https://discord.gg/auki](https://discord.gg/auki) |
| **GitHub** | [https://auki.gitbook.io/](https://auki.gitbook.io/) |
| **Whitepaper** | [https://auki.gitbook.io/](https://auki.gitbook.io/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | ~$89K (2026-04-09 snapshot — very thin) |
| **Market Cap Rank** | #714 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-06-22 |

---

## Competitive Position

Auki occupies an unusual intersection of [[depin|DePIN]], spatial computing/AR, and robotics infrastructure. Rather than competing with decentralized GPU-compute networks (Nosana, Akash, io.net), it competes conceptually with centralized **AR-cloud / spatial-anchor** services and proprietary robotics-mapping stacks — but as an open, token-incentivized, decentralized alternative.

| Competitor | Type | Model | Auki's contrast |
|---|---|---|---|
| **Niantic Lightship / Scaniverse** | Centralized AR cloud (VPS) | Proprietary visual-positioning map | Auki is open, token-incentivized, device-agnostic |
| **Google geospatial / ARCore** | Centralized geospatial AR | Maps-backed visual positioning | Auki is a neutral commons, not a single-vendor stack |
| **Proprietary robotics SLAM stacks** | Per-vendor mapping | Siloed, vendor-locked maps | Auki offers a *shared* posemesh across vendors |
| **[[depin\|DePIN]] compute peers (e.g. [[nosana\|Nosana]])** | GPU compute | Rent raw compute | Different layer — Auki sells *spatial perception*, not GPU time |

Auki's differentiator is **shared, device-agnostic spatial understanding** (the posemesh) that any robot or XR device can read and write to. The bet is on physical-AI / humanoid-robot and smart-glasses adoption; if that adoption is slow or captured by closed platforms, demand for a neutral decentralized layer stays small.

## How & Where It Trades

- **Spot venues.** The CoinGecko snapshot showed **no major centralized-exchange listings**; AUKI is deployed on [[base|Base]] (primary) and Peaq (see contract addresses), so liquidity is DEX-led and chain-fragmented.
- **Liquidity (very thin).** The Apr-2026 snapshot showed ~$89K 24h volume — extremely low even for this batch. AUKI is among the hardest names here to enter or exit at size without significant slippage.
- **Float / overhang.** ~39% of max supply circulates (3.91B of ~10B; MC/FDV ≈ 0.39), a comparatively healthier dilution profile than the ~0.10–0.24 peers in this batch, though future unlocks remain a factor.

## Narrative, Category & Catalysts

AUKI rides several overlapping narratives — **DePIN**, **spatial computing / AR**, and **robotics / physical AI** — and is in the Outlier Ventures portfolio. That breadth is a double-edged sword: it can catch multiple narrative rotations, but all three (AR/metaverse, robotics) have been hype-prone and volatile. Catalysts: verifiable growth in posemesh usage and burns (observable on Dune), marquee robotics/smart-glasses integrations that convert to paid usage, a CEX listing improving liquidity, or a physical-AI narrative rotation. The dominant de-rating risk is that physical-AI adoption is slow or captured by closed incumbents, leaving the neutral-layer demand thin.

## History & Timeline

- **2025-01-26** — AUKI all-time high of **$0.0606**.
- **2026-02-05** — AUKI all-time low of **$0.00416**.
- **2026-06-22** — Trades ~$0.00579 (~90% below ATH); +1.64% 24h / +2.40% 7d, holding up better than peers (e.g. [[perle]]) amid market-wide Extreme Fear (Fear & Greed 21, BTC ~$64,508).

---

## Risks

- **Narrative dependence** — exposed to AR/metaverse and robotics narratives, both of which have been volatile and prone to hype cycles.
- **Extreme low liquidity** — 24h volume in the tens of thousands of dollars makes AUKI very hard to enter/exit at size without large slippage.
- **Emissions vs. demand** — burns must be driven by genuine network usage to offset reward emissions; adoption metrics are largely project-reported.
- **Adoption / execution risk** — physical-AI and humanoid robotics are early; commercial traction may take years and may be captured by centralized incumbents.
- **Smart-contract / multi-chain risk** — deployed on [[base]] and Peaq, broadening attack surface.

---

## Trading Playbook

> *Educational context, not financial advice. AUKI is an extremely thin, high-beta small-cap.*

- **Regime awareness.** In the current **Established Bear Market / Extreme Fear** tape (Fear & Greed 21, BTC ~16% below its 200-day MA as of 2026-06-22), AR/robotics-DePIN small-caps are high-beta narrative plays. AUKI's modest green week is not durable strength — these names amplify the broader cycle.
- **Liquidity is the binding constraint.** With ~$89K daily volume in the snapshot and no major CEX listing, AUKI is one of the least liquid names in this batch; even small orders can move price and exits can be costly. Size accordingly; no perp to hedge.
- **Transparency advantage.** Unlike most peers, Auki publishes an on-chain burn tracker (Dune) — use it. Rising usage-driven burns are the most credible signal of real demand versus emission-funded activity.
- **Adoption-gated bull case.** The thesis depends on physical-AI / smart-glasses adoption converting to *paid* posemesh usage. Treat project-reported integration/adoption claims as marketing until corroborated on-chain or by third parties.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[base]]
- [[depin]]
- [[artificial-intelligence]]
- [[decentralized-compute]]
- [[nosana]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko). Project mechanics drawn from publicly stated Auki documentation and general market knowledge; adoption/revenue claims are project-reported and not independently verified. No specific wiki source ingested yet.
