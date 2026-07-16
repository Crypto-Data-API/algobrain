---
title: "Rain"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, options]
aliases: ["RAIN", "Rain Protocol (rain.one)"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://rain.one"
related: ["[[arbitrum]]", "[[crypto-markets]]", "[[polymarket]]", "[[predictions]]", "[[solana]]"]
---

# Rain

**Rain** (RAIN) is a decentralized prediction-markets and options protocol on [[arbitrum|Arbitrum]] that positions itself as the "Uniswap of prediction markets" — infrastructure for permissionless public and private markets rather than a single app. For traders it is the dominant **on-chain prediction-market token** play of the 2025–2026 cycle (a sector led off-chain by [[polymarket|Polymarket]] and Kalshi, neither of which has a token), reaching the top 30 by market cap in early 2026.

> **Disambiguation**: not to be confused with the older "Rain Protocol" smart-contract tooling project (rainprotocol.one) or the Bahrain-based Rain exchange.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | RAIN |
| **Market Cap Rank** | Top 30-40 (as of June 2026, approximate; #30 at April 2026 snapshot) |
| **Market Cap** | ~$3.8B at April 2026 snapshot; FDV roughly 2.4x higher — significant unlock overhang |
| **Chain / Sector** | Arbitrum One (cross-chain deposits from Ethereum, Base, BNB Chain); sectors: prediction markets, options, GambleFi |
| **Categories** | Gambling (GambleFi), Decentralized Finance (DeFi), Options, Prediction Markets, Arbitrum Ecosystem |
| **Website** | [https://rain.one](https://rain.one) |

---

## Overview

Rain is a decentralized options protocol built on Arbitrum. It enables anyone to create and trade custom markets without restrictions, offering a permissionless framework for prediction and options trading. Public markets are resolved using Olympus AI’s oracle agent, while private markets allow creators to act as resolvers. The protocol supports secondary trading, account abstraction for smoother user experience, and a deflationary token model where 2.5% of trading volume is allocated to buy and burn the $RAIN token. Governance of the protocol is carried out by token holders through a DAO.

Rain is the first protocol to offer **private, invitation-only prediction markets** alongside permissionless public markets. Market resolution uses an AI-powered oracle (referred to as Delphi / Olympus AI's oracle agent in protocol docs) with a built-in dispute layer. Cross-chain deposits are supported from Ethereum, Base and BNB Chain. The deflationary mechanic — **2.5% of every market's trading volume is used to buy back and burn RAIN** — ties token scarcity directly to platform volume.

---

## Architecture / How It Works

Rain is best understood as **prediction-market *infrastructure*** rather than a single front-end app — the self-styled "Uniswap of prediction markets." Anyone can spin up a market; Rain provides the rails (creation, liquidity, resolution, settlement) that those markets run on.

- **Permissionless market creation.** Any user can create a market on any question without gatekeeper approval — the permissionless analogue to [[polymarket|Polymarket]]'s curated listing process. This is the supply-side scaling bet: instead of a team listing markets, the crowd does.
- **Public vs private markets.** *Public* markets are open and resolved via the protocol's AI oracle. *Private* (invitation-only) markets let the **creator act as the resolver** — useful for closed groups, fantasy/sports pools, or bespoke bets, but it concentrates resolution trust in one party. The public/private split is Rain's headline differentiator.
- **AI oracle resolution + dispute layer.** Public-market outcomes are settled by an AI oracle agent (Delphi / "Olympus AI's oracle agent" in the docs) that ingests real-world data to determine the result, with a **dispute mechanism** that lets participants challenge a resolution. The integrity of the whole protocol rests here: a wrong, gamed, or stalled resolution is the single most damaging failure mode for a prediction market (the same class of risk Polymarket has faced in contested resolutions like the "did the candidate wear a suit" dispute).
- **Liquidity / matching (V2 roadmap).** V2 targets **automated market makers + on-chain order books** so markets have continuous liquidity rather than relying purely on counterparty matching — important for the long-tail markets that permissionless creation generates.
- **Account abstraction & cross-chain deposits.** AA smooths UX (gasless/streamlined flows), and deposits are accepted cross-chain from [[ethereum|Ethereum]], Base and [[bnb|BNB Chain]] into the [[arbitrum|Arbitrum]] execution layer — lowering the friction of getting capital into markets.
- **Buy-and-burn flywheel.** **2.5% of every market's trading volume** is routed to buy back and burn RAIN. This is the core value-accrual mechanic: token scarcity scales with platform volume, so the bull thesis is explicitly "volume → burn → supply down." It also means the token is reflexively tied to usage — strong in a volume boom, weak when activity dries up.

---

## Value Accrual & Governance

- **Value accrual = buy-and-burn.** RAIN does not pay a direct dividend; instead the **2.5%-of-volume buyback-and-burn** is the deflationary value-accrual channel. Holders benefit indirectly: more platform volume → more RAIN bought and destroyed → lower supply. The mechanic is clean but **reflexive** — it rewards holders precisely when the protocol is busy and does nothing (while emissions/unlocks continue) when it is quiet.
- **Governance.** The protocol is governed by RAIN holders through a **DAO** — parameter changes, treasury, listings policy, and resolution rules fall under token-holder governance. As with most young DAO tokens, real decentralisation of resolution and treasury control is the thing to verify; early-stage governance is typically team-led in practice.
- **Supply caveat.** With **MC/FDV ≈ 0.42**, more than half the 1.15T max supply is still to enter circulation. Burns must outpace emissions/unlocks for the deflation thesis to hold on a net basis — otherwise the "deflationary" framing is gross, not net.

---

## 2025–2026 Developments

- **Token launch and run** — RAIN's all-time low was September 2025 ($0.0022) and its all-time high February 2026 ($0.0109), a ~5x in five months as prediction markets became a leading crypto narrative.
- **$200M ecosystem commitment** — announced via a partnership with Nasdaq-listed Enlivex, plus a **$100M protocol liquidity expansion** (Crypto Reporter, 2026).
- **Version 2 roadmap** — permissionless market creation, automated market makers, on-chain order books, AI-assisted market resolution, and public + private markets, timed ahead of the **2026 FIFA World Cup**, which the team is targeting as its flagship volume event.
- **Listings** — spot listings on [[kraken|Kraken]] and KuCoin (notable for a token this young).

### Dated timeline (verified anchors)

| Date | Event |
|---|---|
| **2025-09-14** | All-time low **$0.00222** recorded — effectively the post-launch base. |
| **2026-02-09** | All-time high **$0.0109** — ~5x off the low as the prediction-market narrative peaked. |
| **2026-04-09** | CoinGecko snapshot: ~#30 by market cap, ~$3.8B cap, ~$14.8M/24h volume. |
| **2026 (announced)** | $200M ecosystem commitment (Enlivex partnership) + $100M liquidity expansion; V2 + World Cup growth strategy (Crypto Reporter). |

*Editorial/partnership items above are sourced to the citations below; price anchors are from the 2026-04-09 CoinGecko snapshot and are historical reference only.*

---

## Comparison Table

| Protocol | Token? | Model | Resolution | vs Rain |
|---|---|---|---|---|
| **Rain** | **RAIN** | On-chain, permissionless public + private markets ([[arbitrum\|Arbitrum]]) | AI oracle + dispute layer | The investable on-chain token expression; private markets are its unique angle |
| **[[polymarket\|Polymarket]]** | No token | Curated, centrally listed markets (Polygon, USDC) | UMA optimistic oracle | The off-chain volume leader; no token, so RAIN is the "tokenised proxy" trade, not a direct competitor for capital |
| **Kalshi** | No token | Regulated US exchange (CFTC) | Exchange/operator | Fully regulated, fiat, no crypto token; appeals to compliance-sensitive flow |
| **Azuro** | AZUR | On-chain prediction/betting liquidity layer | Oracle-based | Closest on-chain *infrastructure* peer; liquidity-layer framing similar to Rain |

The strategic read: the **demand side** (Polymarket, Kalshi) proved prediction markets are a real, large category — but neither monetises via a token. Rain's pitch is to be the **on-chain, tokenised, permissionless** layer that captures that demand where Polymarket/Kalshi can't (or won't) — and to give traders the only liquid token in the basket.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 478.35B RAIN |
| **Total Supply** | 1.15T RAIN |
| **Max Supply** | 1.15T RAIN |
| **Fully Diluted Valuation** | $9.09B |
| **Market Cap / FDV Ratio** | 0.42 |

---

## Price History (snapshot: 2026-04-09, CoinGecko — historical reference only)

| Metric | Value |
|---|---|
| **All-Time High** | $0.0109 (2026-02-09) |
| **Current vs ATH** | -27.47% |
| **All-Time Low** | $0.00222126 (2025-09-14) |
| **Current vs ATL** | +255.97% |
| **24h Change** | +4.23% |
| **7d Change** | +0.55% |
| **30d Change** | -12.08% |
| **1y Change** | +0.00% |

---

## Platform & Chain Information

**Native Chain:** Arbitrum One

### Contract Addresses

| Chain | Address |
|---|---|
| Arbitrum One | `0x25118290e6a5f4139381d072181157035864099d` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | RAIN/EUR | N/A |
| KuCoin | RAIN/USDT | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://rain.one](https://rain.one) |
| **Twitter** | [@rain__protocol](https://twitter.com/rain__protocol) |
| **Telegram** | [+9y2TtrFRYEA2OGFk](https://t.me/+9y2TtrFRYEA2OGFk) (16,018 members) |
| **Whitepaper** | [https://whitepaper.rain.one](https://whitepaper.rain.one) |

---

## Trading Characteristics (snapshot: 2026-04-09 — stale; see Trading Relevance below)

| Characteristic | Detail |
|---|---|
| **24h Volume** | $14.79M |
| **Market Cap Rank** | #30 (April 2026) |
| **24h Range** | $0.00736572 — $0.00805895 |
| **CoinGecko Sentiment** | 50% positive |
| **Last Updated** | 2026-04-09 |

---

## Trading Relevance

- **Where it trades**: spot on [[kraken|Kraken]] (RAIN/EUR) and KuCoin (RAIN/USDT); thinner CEX coverage than peers of its market cap, so liquidity/slippage risk is elevated relative to rank.
- **Narrative basket**: the **prediction-markets basket** — the on-chain tokenized answer to [[polymarket|Polymarket]] and Kalshi (see [[predictions]]); also overlaps GambleFi and the [[arbitrum|Arbitrum]] ecosystem basket.
- **Catalysts**: V2 launch, 2026 FIFA World Cup volume (the explicit growth strategy), burn-rate prints (2.5% of volume), and new exchange/perp listings.
- **Key risks**: **MC/FDV of 0.42** means more than half of supply is yet to circulate — unlock-driven sell pressure is the structural short thesis; volume (~$15M/day at snapshot) is thin versus a ~$3.8B cap, flagging reflexivity/valuation risk; oracle-resolution disputes are a protocol-specific tail risk; 50% sentiment shows a genuinely contested market.

---

## Risks (structured)

- **Unlock overhang (structural).** MC/FDV ≈ 0.42 — >50% of the 1.15T max supply still uncirculated. The buyback-and-burn must net against ongoing emissions; until it does, scheduled unlocks are the clearest sell-pressure / short thesis. See [[token-unlocks]].
- **Oracle / resolution risk (protocol-specific tail).** An AI oracle resolving real-world events is a novel, partially unproven mechanism. A wrong, manipulated, or stalled resolution — or a dispute layer that fails under load — directly destroys user trust. In private markets the **creator is the resolver**, concentrating counterparty/integrity risk.
- **Valuation / reflexivity.** A ~$3.8B (snapshot) cap on ~$15M/day volume is a thin-float, narrative-rich profile: price can fall fast if the prediction-market narrative cools, and the burn flywheel reverses (low volume → little burn → no scarcity support).
- **Venue / liquidity risk.** Thinner CEX coverage than peers of its rank (spot on [[kraken|Kraken]] EUR and KuCoin); elevated slippage relative to market-cap rank. See [[liquidity]], [[slippage]].
- **Execution/roadmap risk.** The bull case leans on V2 (AMMs, order books) shipping and the **2026 FIFA World Cup** delivering the flagship volume event. Delivery slippage or a disappointing World Cup turnout undercuts the catalyst thesis.
- **Smart-contract & cross-chain risk.** Standard [[smart-contract-risk]] plus cross-chain deposit/bridge exposure from Ethereum/Base/BNB into Arbitrum.
- **Regulatory risk.** Prediction/GambleFi markets sit in a contested regulatory zone (Kalshi/Polymarket have both faced US scrutiny); a permissionless, tokenised version carries more, not less, regulatory tail risk.

---

## Trading Playbook (bear / Extreme-Fear, bottoming regime)

Framing only — not advice. Against the 2026-06-23 macro backdrop (Fear & Greed 21, market-health 29/100, *Bottoming / Accumulation* long-horizon regime):

- **Thesis token, event-gated.** RAIN is the cleanest liquid way to express the on-chain prediction-market narrative, but it is **catalyst-dependent**: the V2 launch and the **2026 FIFA World Cup** are the explicit volume events. In a risk-off tape, the rational stance is to *stage* exposure into those catalysts rather than chase.
- **Respect the unlock calendar.** Before sizing, check the vesting/unlock schedule against the >50% uncirculated supply — rallies into unlocks are suspect, and unlock dates are natural short windows.
- **Watch the burn print as a fundamental tape.** The 2.5%-of-volume burn is an on-chain proxy for real usage; rising burn into rising price is a healthier signal than price moving on narrative alone.
- **Liquidity discipline.** With only Kraken/KuCoin spot and thin depth, use limit orders, size for slippage, and assume you cannot exit a large position cleanly in a stress move.
- **Invalidation.** A failed/disputed high-profile resolution, a missed V2 window, or a weak World Cup volume showing would each break the core thesis — treat them as hard exits, not dips.

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Related

- [[crypto-markets]]
- [[arbitrum]] — host chain
- [[polymarket]] — off-chain prediction-market leader (no token)
- [[predictions]] — prediction markets overview
- [[ethereum]] — settlement layer for cross-chain deposits

---

## Sources

- CoinGecko top-1000 snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- [Rain — official site](https://www.rain.one/) and [RAIN Token White Paper v2.0](https://whitepaper.rain.one/)
- [Crypto Reporter — RAIN Highlights $200M Ecosystem Commitment, $100M Liquidity Expansion, World Cup Strategy Ahead of V2 (2026)](https://www.crypto-reporter.com/newsfeed/rain-highlights-200m-ecosystem-commitment-100m-liquidity-expansion-and-world-cup-growth-strategy-ahead-of-version-2-launch-127486/)
- [Atomic Wallet Academy — What Is Rain Protocol? Prediction Market Infrastructure on Arbitrum](https://atomicwallet.io/academy/articles/what-is-rain-protocol)
- [BingX Learn — What Is Rain (RAIN) Crypto Prediction Protocol](https://bingx.com/en/learn/article/what-is-rain-protocol-crypto-prediction-market-how-does-it-work)
- Verified via Perplexity (sonar) and web search, 2026-06-10.

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $0.0132 (2026-02-16) |
| **Current vs ATH** | -67.90% |
| **All-Time Low** | $0.00335087 (2026-06-30) |
| **Current vs ATL** | +26.10% |
| **24h Change** | -7.89% |
| **7d Change** | -6.34% |
| **30d Change** | -12.23% |
| **1y Change** | +0.00% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $19,669.72 |
| **Market Cap Rank** | #1682 |
| **24h Range** | $0.00414348 — $0.00463148 |
| **Last Updated** | 2026-07-16 |

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## See Also

- [[crypto-markets]]
- [[solana]]

---
