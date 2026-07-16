---
title: "Liquidity Mining"
type: concept
created: 2026-04-15
updated: 2026-07-16
status: excellent
tags: [crypto, defi, liquidity, yield]
aliases: ["LM", "Liquidity Mining"]
related: ["[[airdrop]]", "[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[liquidity-pools]]", "[[liquidity-providers]]", "[[yield-farming]]"]
domain: [defi]
difficulty: intermediate
entity_type: protocol
headquarters: "Decentralized"
website: "https://leisuremeta.io/"
---

Liquidity mining is the practice by which a [[defi|DeFi]] protocol distributes its own (usually newly minted) **governance tokens** to users who supply liquidity, in order to bootstrap usage and deposits. An LP not only earns ordinary [[liquidity-pools|pool]] trading fees but also receives a stream of incentive tokens on top, often pushing advertised yields well above what fee income alone would justify. Liquidity mining was the spark of "DeFi Summer" in 2020 and remains the dominant go-to-market tactic for new protocols -- and a textbook case of how token emissions can manufacture impressive-looking yields that mask a transfer of value rather than its creation.

## Overview

The model was crystallized by **Compound** in June 2020, when it began distributing its COMP governance token to both lenders and borrowers. Yields spiked, capital flooded in, and total value locked (TVL) across DeFi exploded from under $1B to over $10B within months. Every subsequent protocol -- SushiSwap, Curve, Yearn, and countless forks -- adopted the playbook: emit a token, point it at the desired behavior (usually liquidity provision), and watch deposits arrive.

The mechanics are simple: a protocol allocates a fixed schedule of token emissions and directs them to specific pools. Users who stake their [[liquidity-providers|LP]] tokens in the protocol's "farm" earn a pro-rata share of those emissions. The effect is to **subsidize liquidity** -- the protocol prints a claim on its own future governance/cashflow and pays it to early supporters in exchange for capital and bootstrapped network effects.

### Where it fits

Liquidity mining sits on top of the base DeFi liquidity stack — it is an *incentive layer*, not a market structure:

| Layer | Page | Role |
|---|---|---|
| Market mechanism | [[automated-market-maker]] | The pricing curve (x·y=k) that quotes trades |
| Venue | [[liquidity-pools]] | The reserves traders swap against |
| Supplier | [[liquidity-providers]] | Who deposits the capital and bears risk |
| **Incentive** | **Liquidity mining** | Protocol-emitted tokens layered on top of fee income |
| User strategy | [[yield-farming]] | Chasing the best risk-adjusted yield across all of the above |

### Worked example (qualitative)

An LP deposits an ETH/USDC pair into a pool. From swap fees alone the position might yield ~5% APY. The protocol runs a liquidity-mining program that emits its governance token to that pool, advertising an extra "30% APY" in rewards — a **35% total** headline. But that 30% is paid in the protocol's own token, whose price is falling as emissions inflate supply. After accounting for token-price decay, [[impermanent-loss|impermanent loss]] on the volatile pair, and gas to harvest and sell, the *realized* return can be a small fraction of the headline — sometimes negative versus simply holding ETH and USDC. The headline yield measured a transfer of newly minted tokens, not value created.

## Liquidity Mining vs. Yield Farming

The terms overlap and are often used interchangeably, but there is a useful distinction:

| Term | Perspective |
|------|-------------|
| **Liquidity mining** | The *protocol's* program -- the act of emitting tokens to reward liquidity providers |
| **[[yield-farming|Yield farming]]** | The *user's* strategy -- chasing the highest risk-adjusted yield across protocols, of which liquidity-mining rewards are one input |

In short: liquidity mining is what the protocol does; yield farming is what the user does with it (often hopping between farms, recursively staking LP tokens, and stacking incentives).

## Mercenary Capital and Emissions Decay

Two structural problems define the economics of liquidity mining:

**Mercenary capital.** Liquidity attracted purely by token rewards is disloyal -- it chases the highest emissions and leaves the instant they drop or a better farm appears. This is "mercenary" liquidity. The classic demonstration was the **2020 "vampire attack"** by SushiSwap, which used aggressive SUSHI emissions to lure roughly $1B in liquidity away from Uniswap in days; much of it left again once the incentive math changed.

**Emissions decay.** High advertised APYs are paid in the protocol's own inflating token. As emissions continue, supply grows, the token price typically falls, and the real yield collapses -- a reflexive death spiral: lower token price → lower APY → liquidity exits → less usage → further price decline. Many "food coin" farms of 2020-2021 followed exactly this arc to near-zero.

The industry's response has been mechanisms to make liquidity **sticky** and align it with long-term protocol health:

- **veTokenomics (vote-escrow)** -- pioneered by Curve (veCRV): users lock tokens for up to 4 years to earn boosted rewards and direct emissions, trading liquidity for governance power. This spawned the "**Curve Wars**," in which protocols (Convex, et al.) competed to accumulate veCRV to steer emissions toward their own pools.
- **Protocol-owned liquidity (POL)** -- popularized by OlympusDAO (the "(3,3)" bonding model): the protocol buys its *own* liquidity instead of renting it, so it cannot walk away. Olympus's subsequent collapse illustrated the model's fragility.
- **Real-yield narratives (post-2022)** -- a shift toward distributing *actual protocol revenue* (fees) rather than pure inflationary emissions, marketed as sustainable yield.

## Trading and Market Relevance

- **Bootstrapping** -- liquidity mining remains the fastest way for a new AMM, lending market, or perp DEX to acquire the deep [[liquidity-pools|liquidity]] needed for tight [[slippage]] and credible launch metrics.
- **Yield strategy input** -- mining rewards are a core component of DeFi [[yield-farming|farming]] strategies; sophisticated farmers model emission schedules, token-price beta, and exit timing.
- **[[airdrop|Airdrop]] adjacency** -- liquidity mining is frequently combined with, or a precursor to, retroactive airdrops; "points programs" that promise a future token for current liquidity are a modern, emission-deferred variant.
- **Signal for sell pressure** -- large, ongoing emissions imply continuous structural selling as farmers harvest and dump rewards, a headwind for the token's price.

## Risks

- **[[impermanent-loss|Impermanent loss]]** -- the underlying LP risk persists; rewards can be erased by divergence loss on volatile pairs.
- **Token-price collapse** -- rewards paid in an inflating, illiquid token can be worth far less by the time they are sold; quoted APYs are gross and forward-optimistic.
- **Mercenary flight / liquidity cliffs** -- when emissions end or drop, liquidity can evaporate overnight, widening spreads and stranding remaining LPs.
- **[[smart-contract-risk|Smart-contract and rug risk]]** -- farm contracts, especially in unaudited forks, have been exploited or deliberately back-doored countless times.
- **Ponzi dynamics** -- where the only source of "yield" is new token issuance with no underlying revenue, returns depend entirely on inflows from later participants.

## Related

- [[yield-farming]] -- the user-side strategy that consumes mining rewards
- [[liquidity-providers]] -- who liquidity mining pays
- [[liquidity-pools]] -- the venues being incentivized
- [[defi]] -- the broader ecosystem
- [[airdrop]] -- a related, retroactive form of token distribution
- [[impermanent-loss]] -- the persistent underlying LP risk

## Sources

- General market knowledge; no specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LM |
| **Market Cap Rank** | #2228 |
| **Market Cap** | $1.99M |
| **Current Price** | $0.00055695 |
| **Categories** | Smart Contract Platform, Layer 1 (L1) |
| **Website** | [https://leisuremeta.io/](https://leisuremeta.io/) |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 3.57B LM |
| **Total Supply** | 4.67B LM |
| **Max Supply** | 5.00B LM |
| **Fully Diluted Valuation** | $2.60M |
| **Market Cap / FDV Ratio** | 0.76 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $1.39 (2023-02-23) |
| **Current vs ATH** | -99.96% |
| **All-Time Low** | $0.00055354 (2026-07-16) |
| **Current vs ATL** | +0.73% |
| **24h Change** | -1.82% |
| **7d Change** | -4.05% |
| **30d Change** | -25.05% |
| **1y Change** | -79.30% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc064f4f215b6a1e4e7f39bd8530c4de0fc43ee9d` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://leisuremeta.io/](https://leisuremeta.io/) |
| **Twitter** | [@LeisureMeta_LM](https://twitter.com/LeisureMeta_LM) |
| **Telegram** | [LeisureMeta_Official](https://t.me/LeisureMeta_Official) (10,569 members) |
| **Discord** | [https://discord.gg/leisuremetaofficial](https://discord.gg/leisuremetaofficial) |
| **GitHub** | [https://github.com/leisuremeta](https://github.com/leisuremeta) |
| **Whitepaper** | [https://github.com/leisuremeta/whitepaper/blob/main/LM_WP_v3.1_Eng.pdf](https://github.com/leisuremeta/whitepaper/blob/main/LM_WP_v3.1_Eng.pdf) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $43,649.00 |
| **Market Cap Rank** | #2228 |
| **24h Range** | $0.00055354 — $0.00057710 |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
