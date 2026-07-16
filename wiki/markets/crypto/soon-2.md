---
title: "SOON"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, layer-2]
aliases: ["SOON"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://soo.network/"
related: ["[[crypto-markets]]", "[[layer-2]]", "[[modular-blockchains]]", "[[solana]]"]
---

# SOON

**SOON** (ticker **SOON**) is a rollup stack that brings the **Solana Virtual Machine (SVM)** to other base layers as a Layer-2. The team pioneered **Decoupled SVM**, which lets SVM rollups be deployed across different L1s with native fraud proofs, reduced data-availability cost, and horizontal scaling. SOON's pitch is "high-performance SVM execution for every L1" — bringing [[solana|Solana]]-grade throughput to chains that don't natively run the SVM.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | SOON |
| **Current Price** | $0.161502 |
| **Market Cap** | $54.88M |
| **Market Cap Rank** | #421 |
| **Fully Diluted Valuation** | $161.77M |
| **24h Volume** | $5.75M |
| **24h Change** | +1.87% |
| **7d Change** | -6.41% |
| **All-Time High** | $4.30 (2025-11-14) |
| **All-Time Low** | $0.101005 (2026-04-10) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

SOON trades roughly 96% below its November 2025 all-time high of $4.30, though it sits above its April 2026 all-time low of ~$0.10. The backdrop is extreme fear (Crypto Fear & Greed Index of 22, established bear market — see [[fear-and-greed-index]]). The market-cap/FDV ratio of 0.34 flags meaningful locked supply still to enter circulation.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~339.8M SOON |
| **Total Supply** | ~1.00B SOON |
| **Max Supply** | Uncapped (no fixed max) |
| **Market Cap / FDV** | 0.34 |

**Dilution overhang is significant.** Only ~340M of a ~1B total supply (~34%) circulates, leaving ~660M tokens (team, investors, ecosystem) to vest. There is no fixed max supply, so issuance is not hard-capped. The gap between the $55M market cap and $162M FDV quantifies the unlock overhang — a recent-launch profile where scheduled unlocks add structural sell pressure over the coming years.

### Value accrual & governance

SOON the token captures value as the **fee/gas and incentive asset** of the SOON network and, where deployed, of the SVM rollups built with its stack — a Rollups-as-a-Service (RaaS) economic model where the framework can take fees from chains spun up on it. Channels: **transaction fees** on SOON-powered rollups, **staking/sequencing** participation, **governance** over the protocol and ecosystem treasury, and **incentives** (airdrops, points, ecosystem grants) that drove early distribution. The structural tension is acute here: with only ~34% of supply circulating, **no fixed max supply**, and ~660M tokens still to vest, emission and unlocks are the dominant near-term supply force. Durable value accrual requires fee revenue from real SVM-rollup deployments to scale faster than that supply enters the market — an unproven bar for a recent-launch RaaS token in a bear tape.

---

## How & Where It Trades

**Centralized exchanges (spot):** SOON is listed on Kraken (SOON/USD), Upbit (SOON/BTC), Bitget (SOON/USDT), and KuCoin (SOON/USDT). It was a Binance Alpha Spotlight project. Note the Upbit pair quotes against BTC rather than KRW.

**Derivatives:** No major Hyperliquid perp is tracked for SOON in the current snapshot; CEX perp coverage is limited relative to spot. Traders should verify live perp availability and funding before attempting leveraged or hedged positions, as small-cap L2 tokens can see volatile funding around unlocks.

---

## Technology

SOON's core innovation is **Decoupled SVM** — separating the Solana execution environment from Solana's own L1 so it can run as a rollup atop any base chain:

- **SVM execution as an L2** — apps get Solana's high-throughput, parallel-execution runtime while settling to a separate base layer (e.g., Ethereum or other L1s for DA/settlement), a [[modular-blockchains|modular]] design.
- **Native fraud proofs** — optimistic-style verification adapted to the SVM, rather than relying on a trusted operator.
- **Reduced DA cost / horizontal scaling** — multiple SVM rollups can be spun up and interconnected.
- **Super Adoption Stack (SAS)** — native interoperability among SOON chains and with Solana (SOL) and TON, including a SOL×TON bridge with a Telegram mini-app for user acquisition.

This positions SOON as SVM-flavored Rollups-as-a-Service, distinct from EVM-centric L2s and from Solana itself (which is a monolithic L1).

### How the rollup model actually works

To be precise about the stack: a SOON rollup runs the **SVM as its execution environment** (so apps get Solana-style parallel execution and tooling), but **settles and posts data to a separate base layer** — Ethereum or another L1 for [[data-availability|data availability]] and settlement. The "Decoupled SVM" idea is that the SVM is lifted out of Solana's monolithic design (where execution, consensus and DA are bundled) and run as a modular rollup component. Verification is described as **native fraud proofs** — an optimistic-rollup posture where state is assumed valid and a challenge window lets honest parties dispute invalid transitions, adapted to the SVM rather than the EVM. As with all optimistic rollups, the live trust assumptions to verify are the **sequencer** (typically centralized at first, controlling ordering) and whether the **fraud-proof mechanism is actually live and permissionless** — until it is, security leans on the operator. This is a fundamentally different and lighter trust model than a [[bsquared-network|BTC-L2 bridge]], but the standard rollup caveats (sequencer centralization, challenge-window latency, DA-layer dependency) apply.

---

## Comparison vs competitor chains

SOON competes in **SVM scaling / Rollups-as-a-Service** — a narrower field than general L2s.

| Project | Model | Execution | Differentiator vs SOON |
|---|---|---|---|
| **SOON** | Decoupled-SVM optimistic rollup / RaaS | SVM on any base L1 | SVM-everywhere via native fraud proofs; SOL×TON bridge + SAS |
| **Eclipse** | SVM L2 (settles to Ethereum) | SVM | SVM execution + Ethereum settlement + Celestia DA; well-funded peer |
| **MagicBlock** | SVM "ephemeral rollups" on Solana | SVM | Real-time/gaming ephemeral rollups *within* Solana, not on other L1s |
| **[[solana\|Solana]] (SOL)** | Monolithic L1 | SVM | The incumbent — already high-throughput; the "is SVM-L2 even needed?" bear case |
| **[[arbitrum\|Arbitrum]] Orbit / OP Stack** | EVM RaaS | EVM | The dominant RaaS frameworks — but EVM, not SVM |

The competitive crux: SOON's whole thesis is that demand exists to run the SVM *outside* Solana. Its direct SVM rivals (Eclipse, MagicBlock) attack the same niche from different angles, while [[solana|Solana]] itself is the looming "fast enough already" objection and the EVM RaaS giants own the broader rollup-factory market.

---

## Use Case, Narrative & Category

SOON is an **SVM-everywhere / high-performance L2** narrative play: the thesis that Solana's execution model is superior for many apps and that demand exists to run it outside the Solana L1. CoinGecko categories include Infrastructure, Smart Contract Platform, Layer 2, Cross-chain Communication, BNB Chain Ecosystem, and Base Ecosystem. The bull case is SVM adoption spreading to other ecosystems via SOON rollups; the bear case is that Solana's own L1 is "fast enough" and SVM-L2 demand stays thin.

### Catalysts

Plausible **positive catalysts**: real SVM rollups going live on SOON with meaningful TVL/activity, a fee-bearing RaaS revenue story, renewed SVM/modular narrative rotation, SOL×TON bridge traction via the Telegram mini-app, and additional CEX listings. **Negative catalysts**: scheduled unlocks from the ~660M locked supply (no fixed max) hitting thin liquidity, Solana L1 capacity improvements undercutting the "SVM-elsewhere" thesis, and competition from Eclipse/MagicBlock capturing the SVM-rollup niche first.

---

## Notable History

- **Token launch late 2025**; SOON peaked at ~$4.30 on 2025-11-14 during its listing/airdrop momentum.
- Featured as a Binance Alpha Spotlight project; launched the first SOL×TON bridge with a Telegram mini-app.
- Suffered a ~96% drawdown, bottoming near $0.10 on 2026-04-10 amid the broader bear market.

---

## Risks

- **Unlock/dilution overhang** — only ~34% of supply circulates, with ~660M tokens to vest and no fixed max supply.
- **Competition** — competes with Solana's own L1 (which is already high-throughput), other SVM rollup efforts (Eclipse, MagicBlock), and EVM-centric RaaS providers.
- **Demand uncertainty** — whether teams want SVM execution *outside* Solana at scale is unproven.
- **No liquid derivatives** — limited perp coverage constrains hedging and leverage.
- **Narrative dependence** — tied to the SVM / modular-L2 narrative cycle.
- **Macro/regime** — extreme-fear sentiment (F&G 22) and an established bear market weigh on small-cap L2 tokens.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

Context as of 2026-06-23: market-wide **Extreme Fear** (F&G 21), transitional **bottoming/accumulation** regime, BTC ~16% below its 200-day MA.

- **Character:** SOON has somewhat better liquidity than the thinnest names in this section (~$5.75M/24h, multiple CEX listings, Binance Alpha exposure) but carries a heavy unlock overhang (~34% float, no fixed max) and is down ~96% from its Nov-2025 ATH while sitting above its April-2026 low.
- **Default stance:** the dominant near-term force is supply (vesting), not demand. In Extreme Fear, buying ahead of unlocks is poor risk/reward; default to patience and let the unlock calendar inform timing.
- **If positioning:** treat unlock dates as scheduled risk events to fade or avoid; prefer scaling in on weakness post-unlock rather than into strength. No liquid perp means limited hedging — size accordingly.
- **Invalidation / view change:** a broad regime flip out of Extreme Fear *plus* evidence the RaaS thesis is monetizing (live SVM rollups, fees, TVL). Absent real adoption data, this remains a narrative bet whose chart is governed by vesting.

---

## See Also

- [[solana]] — source of the SVM execution environment
- [[layer-2]] — the L2 category SOON occupies
- [[modular-blockchains]] — the architecture thesis
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`)
- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SOON |
| **Market Cap Rank** | #401 |
| **Market Cap** | $55.71M |
| **Current Price** | $0.1640 |
| **Categories** | Infrastructure, Smart Contract Platform, Layer 2 (L2), Cross-chain Communication, Binance Alpha Spotlight, Base Native |
| **Website** | [https://soo.network/](https://soo.network/) |

---

## Overview

SOON stack is the most efficient rollup stack delivering high performance to every L1, powered by SVM. SOON team pioneered Decoupled SVM, which allows SVM rollups to be spun up across different L1s with native fraud proofs, reduced DA cost and horizontal scaling capacity. 

SOON's SAS (Super Adoption Stack) creates a native interop among all SOON chains as well as with SOL &amp; TON. We launched the first SOL x TON bridge with native TG mini app. Devs can access users without leaving the SOON ecosystem, making it a more effective user acquisition tool at a fraction of the cost of TVL game.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 339.79M SOON |
| **Total Supply** | 1.00B SOON |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $164.57M |
| **Market Cap / FDV Ratio** | 0.34 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $4.30 (2025-11-14) |
| **Current vs ATH** | -96.19% |
| **All-Time Low** | $0.1010 (2026-04-10) |
| **Current vs ATL** | +62.34% |
| **24h Change** | -0.66% |
| **7d Change** | -2.03% |
| **30d Change** | -3.16% |
| **1y Change** | +12.95% |

---

## Platform & Chain Information

**Native Chain:** Solana

### Contract Addresses

| Chain | Address |
|---|---|
| Solana | `4eDf52YYzL6i6gbZ6FXqrLUPXbtP61f1gPSFM66M4XHe` |
| Binance Smart Chain | `0xb9e1fd5a02d3a33b25a14d661414e6ed6954a721` |
| Base | `0xb9e1fd5a02d3a33b25a14d661414e6ed6954a721` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | SOON/USD | N/A |
| Upbit | SOON/KRW | N/A |
| Bitget | SOON/USDT | N/A |
| KuCoin | SOON/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://soo.network/](https://soo.network/) |
| **Twitter** | [@soon_svm](https://twitter.com/soon_svm) |
| **Discord** | [https://discord.gg/soon-svm](https://discord.gg/soon-svm) |
| **GitHub** | [https://github.com/soonlabs/](https://github.com/soonlabs/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $4.48M |
| **Market Cap Rank** | #401 |
| **24h Range** | $0.1633 — $0.1675 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---
