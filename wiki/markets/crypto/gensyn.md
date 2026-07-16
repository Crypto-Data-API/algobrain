---
title: "Gensyn"
type: entity
created: 2026-04-11
updated: 2026-07-16
status: excellent
tags: [ai-trading, crypto, machine-learning]
aliases: ["AI", "AI (Gensyn)", "Gensyn Protocol"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.gensyn.ai/"
related: ["[[ai-agent-tokens]]", "[[akash-network]]", "[[artificial-intelligence]]", "[[crypto-markets]]", "[[decentralized-ai]]", "[[depin]]", "[[ethereum]]", "[[io-net]]", "[[machine-learning]]", "[[model-inference-vs-training]]", "[[prime-intellect]]", "[[tokenized-compute]]"]
---

# Gensyn

**Gensyn** (token ticker **AI**) is a decentralized protocol for **distributed machine-learning training** — stitching together heterogeneous GPU hardware from independent providers into a coordinated training run. Its core technical contribution is a verification system that lets the protocol trust that a remote worker actually performed the ML computation it claims to have performed, without re-executing the training itself. It sits at the [[tokenized-compute|tokenized-compute]] / [[depin|DePIN]] compute layer of [[decentralized-ai|decentralized AI]].

Gensyn sits alongside [[akash-network|Akash]], [[io-net|io.net]], [[aethir]], and [[prime-intellect]]. Unlike those projects, its focus is specifically on the **training** side of the training-versus-inference split — the harder problem from both a coordination and verification standpoint.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | AI |
| **Current Price** | $0.02640569 |
| **Market Cap** | $34.36M |
| **Market Cap Rank** | #591 |
| **24h Volume** | $6.39M |
| **24h Change** | +4.97% |
| **7d Change** | +1.82% |
| **24h Range** | $0.02428836 — $0.02687569 |
| **Fully Diluted Valuation** | $263.39M |
| **All-Time High** | $0.103372 (2026-04-29) |
| **All-Time Low** | $0.0218171 (2026-06-07) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: Gensyn's token now trades under the symbol **AI** and is live on CoinGecko (this updates earlier wiki content that described the token as pre-launch). The recency of the launch shows in the price path: an April 2026 ATH of $0.103 followed by a June 2026 ATL of $0.0218 — a ~79% drawdown in roughly six weeks, typical of a fresh, low-float AI token in an **Established Bear Market** with the Crypto Fear & Greed Index at **≈ 23 (extreme fear)** on 2026-06-21. AI has bounced ~21% off that June ATL and is roughly flat on the week, a tentative stabilization rather than a trend reversal.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.30B AI |
| **Total Supply** | 10.00B AI |
| **Max Supply** | 10.00B AI |
| **Fully Diluted Valuation** | ~$263.4M |
| **Market Cap / FDV** | ~0.13 |

Gensyn's **Market Cap / FDV is only ~0.13** — roughly 13% of the 10B max supply is circulating. This is a **severe unlock/dilution overhang**: VC, team, and ecosystem allocations (the project raised substantial funding, notably from a16z crypto) will unlock over the coming years, and the fully-diluted valuation (~$263M) is nearly **8x the current market cap** (~$34M). For a recently launched AI token in a bear market, low circulating float plus large scheduled emissions is the dominant price risk — every unlock cliff adds sell-side supply that demand must absorb. The ~$229M gap between cap and FDV is the implicit overhang buyers are underwriting. It is the **lowest float in this peer set** (vs. KGeN ~0.20, Seeker ~0.62, GoPlus ~0.44, KUB ~0.63), making AI especially sensitive to unlock schedules.

---

## Market Structure & Derivatives

### Spot liquidity

Gensyn's **AI** token is live and trades on centralized and decentralized venues with ~$6.4M of daily volume against a ~$34M cap (turnover ~19% of cap) — modest liquidity that is slippage-prone on size. Liquidity sits primarily on CEX AI-USDT pairs with on-chain depth on the token's home network. As a low-float name, order-book depth thins quickly away from mid, and unlock-driven supply events can overwhelm organic bids.

### Derivatives

As a newly listed, low-float token AI is **not** a flagship [[hyperliquid|Hyperliquid]] perp market; any perpetual-futures listings are early-stage with thin open interest, so funding and OI are not yet meaningful drivers. The practical consequence is that holders have **limited ability to hedge or short** directional risk, and the recent bounce off the ATL cannot be efficiently faded on-chain. Treat AI as a primarily spot instrument and verify the exact contract/ticker before trading, since "AI" is a heavily reused symbol and several unrelated/unofficial "GENSYN" tickers have historically circulated.

> **Caution:** Confirm you are trading the official Gensyn token. Symbol collisions ("AI") and prior fake "GENSYN" listings make ticker-only identification unsafe — verify by contract address and official channels.

---

## What Gensyn Is Actually Building

- **SwarmCompute** — Gensyn's peer-to-peer training protocol, where many independent GPUs contribute gradients to a shared training run.
- **Verification pipeline** — lightweight probabilistic checks that let the protocol detect workers who submit fabricated or low-quality gradients without re-executing the entire training step.
- **RL Swarm** — an open reinforcement-learning research environment built on top of the training substrate.

The design philosophy is that trustless distributed training — where anyone can contribute a GPU and be paid for honest work — requires a fundamentally different verification model from trustless inference, because training is an extremely long computation whose intermediate state is not independently checkable.

---

## Use Case, Narrative & Category

Gensyn is a **DePIN compute / decentralized-AI** protocol on the **training** side of the [[model-inference-vs-training|training-vs-inference]] split. The economic model: GPU owners earn the AI token for contributing verified training work; demand for the token is meant to track demand for decentralized training capacity. The narrative bet is that if decentralized training works at scale, it weakens a structural moat of centralized AI labs — the ability to concentrate tens of thousands of GPUs in one data center.

### Comparison to Peers

| Protocol | Focus | Token Status |
|----------|-------|--------------|
| [[akash-network\|Akash]] | General-purpose compute, inference-heavy | Live (AKT) |
| [[io-net\|io.net]] | Inference-focused GPU clusters | Live (IO) |
| [[gensyn\|Gensyn]] | Distributed training | Live (AI) |
| [[prime-intellect]] | Distributed training + RL research | Early / limited token |

### Valuation framing (qualitative)

Gensyn is a **pre-revenue infrastructure bet** priced on technology credibility and category narrative, not cash flows. Two valuation anchors matter: (1) **FDV vs. private-round marks** — at ~$263M FDV the token must hold against the valuations VCs (notably a16z crypto) entered at, and large blocks unlock into a market that may reprice those marks; (2) **share of the decentralized-AI-compute TAM** — bulls argue training is the larger, higher-value half of the [[model-inference-vs-training|inference-vs-training]] stack and that Gensyn is the most technically credible training-side protocol, justifying a premium to inference-led peers; bears note that distributed training over commodity interconnects has not yet demonstrated efficiency parity with centralized clusters, so the protocol's revenue is speculative. The combination of low float, ~8x FDV/MC, and an unproven verification model makes AI a high-variance expression of the decentralized-AI thesis rather than a stable infrastructure holding.

---

## Notable History

- Raised substantial venture funding (notably a16z crypto) prior to token launch, shaping a large, heavily-allocated token supply.
- **2026-04-29** — Token (AI) all-time high of $0.1034 shortly after launch.
- **2026-06-07** — All-time low of $0.0218, a ~79% drawdown from the ATH within ~6 weeks, amid the broad AI-token and bear-market repricing.

---

## Why It Matters

If decentralized training works at scale, it weakens one of the structural moats of centralized AI labs. Gensyn is among the most technically credible attempts to deliver this. Whether the protocol's verification assumptions hold under adversarial conditions, and whether distributed training can match the efficiency of centralized training with fast interconnects, are the two questions that determine whether this thesis is a bet or a structural inevitability.

---

## Risks

- **Severe unlock/dilution overhang** — only ~13% of supply circulating; FDV ~8x market cap means years of scheduled emissions weigh on price, the dominant risk for this name.
- **Recent-launch volatility** — a ~79% drawdown from ATH to ATL in six weeks shows how violently low-float AI tokens reprice.
- **Unproven technical assumptions** — the verification model and distributed-training efficiency vs. centralized clusters are still being battle-tested adversarially.
- **Ticker/identity risk** — symbol "AI" and prior fake "GENSYN" listings make misidentification a real hazard; verify by contract.
- **Hype-cycle + bear-market beta** — decentralized-AI/DePIN-compute is a high-beta narrative subsector; the Established Bear Market and extreme-fear (F&G ≈ 23) regime amplify downside.
- **Thin liquidity & no hedge** — ~$6.4M daily volume moves price on size, and the absence of a deep perp market leaves holders unable to hedge directional risk.

---

## See Also

- [[tokenized-compute]] — Parent concept
- [[decentralized-ai]] — Parent movement
- [[depin]] — DePIN compute category
- [[prime-intellect]] — Adjacent distributed-training project
- [[model-inference-vs-training]] — Why training is the harder side of the stack
- [[ai-agent-tokens]] — Full AI token landscape
- [[artificial-intelligence]] — AI section hub
- [[crypto-fear-and-greed-index]]

---

## Sources

- Gensyn documentation at gensyn.ai
- Market data as of 2026-06-21 via cryptodataapi.com / CoinGecko top-1000 markets snapshot.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | AI |
| **Market Cap Rank** | #572 |
| **Market Cap** | $34.32M |
| **Current Price** | $0.0263 |
| **Categories** | Artificial Intelligence (AI), Smart Contract Platform, Binance Alpha Spotlight |
| **Website** | [https://www.gensyn.ai/](https://www.gensyn.ai/) |

---

## Overview

Gensyn, the Network for Machine Intelligence, is an open infrastructure layer for AI. It provides the foundational infrastructure AI needs to operate at scale, including compute, data, and information exchange, by enabling both humans and machines to participate in open digital markets. Built with native support for AI communication, identification, and verification, Gensyn serves as the economic backbone for continual learning over new decentralised AI models and applications, without centralised control.

Gensyn is backed by a16z crypto, CoinFund, Galaxy Digital, Eden Block, Maven 11, and more. For more information, visit http://gensyn.ai

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 1.30B AI |
| **Total Supply** | 10.00B AI |
| **Max Supply** | 10.00B AI |
| **Fully Diluted Valuation** | $263.05M |
| **Market Cap / FDV Ratio** | 0.13 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.1034 (2026-04-29) |
| **Current vs ATH** | -75.12% |
| **All-Time Low** | $0.0205 (2026-06-25) |
| **Current vs ATL** | +25.29% |
| **24h Change** | +11.90% |
| **7d Change** | -0.20% |
| **30d Change** | +4.14% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x4d7078ddd6ccfed2f85db5b7d3ff16828d378d48` |
| Gensyn | `0x4e742319f6b0fec4afa504fc8ed3ceab0fb751a2` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | AIGENSYN/USDT | N/A |
| Kraken | AI/USD | N/A |
| Upbit | AI/KRW | N/A |
| Bitget | AI/USDT | N/A |
| KuCoin | AI/USDT | N/A |
| Crypto.com Exchange | AIGENSYN/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V3 (Ethereum) | 0X4D7078DDD6CCFED2F85DB5B7D3FF16828D378D48/0XA0B86991C6218B36C1D19D4A2E9EB0CE3606EB48 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.gensyn.ai/](https://www.gensyn.ai/) |
| **Twitter** | [@gensynai](https://twitter.com/gensynai) |
| **Discord** | [https://discord.com/invite/gensyn](https://discord.com/invite/gensyn) |
| **Whitepaper** | [https://docs.gensyn.ai/litepaper](https://docs.gensyn.ai/litepaper) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $17.09M |
| **Market Cap Rank** | #572 |
| **24h Range** | $0.0235 — $0.0264 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
