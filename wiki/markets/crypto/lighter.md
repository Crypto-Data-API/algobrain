---
title: "Lighter"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives]
aliases: ["LIT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://lighter.xyz/"
related: ["[[crypto-markets]]", "[[decentralized-exchange]]", "[[dydx-chain]]", "[[ethereum]]", "[[funding-rate]]", "[[hyperliquid]]", "[[perp-dex-aggregation]]", "[[perpetual-futures]]", "[[zk-rollup]]"]
---

# Lighter

**Lighter** (LIT) is a high-performance [[decentralized-exchange|DEX]] for [[perpetual-futures|perpetual futures]], built as a [[zk-rollup|zk-rollup]] with verifiable order matching and liquidations. It markets itself as the first exchange to offer *provable* (cryptographically verifiable) order matching and liquidation while delivering CEX-grade latency, settling on [[ethereum|Ethereum]]. The LIT token is the protocol's governance and incentive asset; Lighter is one of the new wave of perp DEXs competing directly with [[hyperliquid|Hyperliquid]] and [[dydx-chain|dYdX]].

---

## Market Data

| Field | Detail |
|---|---|
| **Ticker** | LIT |
| **Market Cap Rank** | #120 |
| **Market Cap** | $381.64M |
| **Current Price** | $1.53 |
| **24h Change** | -2.51% |
| **7d Change** | -6.11% |
| **24h Volume** | $24.24M |
| **Circulating Supply** | 250.00M LIT |
| **Total / Max Supply** | 1.00B LIT |
| **Fully Diluted Valuation** | ~$1.53B |
| **All-Time High** | $7.86 — now ~-80.5% |
| **All-Time Low** | $0.780945 — now ~+96% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

Context: despite the broad market sitting in **extreme fear** (Fear & Greed = 23) and an **Established Bear Market** regime as of 2026-06-21, LIT holds a relatively high rank (#120) and strong daily turnover (~$24M, ~6% of market cap), reflecting active speculative interest in the perp-DEX narrative. The token is down ~6% on the week but still trades nearly 2x its all-time low.

---

## Technology & Protocol

Lighter's differentiator is **verifiable execution via a ZK architecture**:

- **Provable matching & liquidations** — order matching, cancellation sequencing, and liquidations are executed in a way that can be cryptographically proven on [[ethereum|Ethereum]] via [[zk-rollup|zero-knowledge]] proofs. This addresses the trust gap where users must otherwise rely on an operator's good faith for fair sequencing and liquidation — a recurring concern with off-chain "trusted sequencer" perp venues.
- **CEX-grade latency** — the rollup design targets the speed sophisticated traders expect, while inheriting Ethereum settlement security.
- **MEV resistance** — provable, deterministic sequencing limits the operator's ability to reorder or front-run flow, appealing to market makers and high-frequency participants.
- **Order-book model** — Lighter runs a transparent CLOB rather than an AMM, positioning it alongside [[dydx-chain|dYdX]] and [[hyperliquid|Hyperliquid]] rather than pool-based perp DEXs.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 250.00M LIT |
| **Total Supply** | 1.00B LIT |
| **Max Supply** | 1.00B LIT |
| **Market Cap / FDV** | ~0.25 |

Only **~25% of max supply circulates**, so LIT carries **substantial future dilution / unlock overhang** — its fully-diluted valuation is roughly 4x its current market cap (**~$1.53B FDV vs ~$382M cap**). This **low float / high FDV** structure is a key trading consideration: token unlocks and emissions can pressure price even if protocol fundamentals improve. It contrasts sharply with incumbents like dYdX (~84% float), making LIT far more exposed to vesting cliffs.

---

## Market Structure & Derivatives

**Spot venues (CEX):** LIT trades on Bitget, KuCoin, Crypto.com Exchange, and other centralized exchanges, mostly against USDT/USD.

**On-chain spot:** Available on Uniswap V3 (Ethereum) against WETH.

**The protocol's own venue:** Lighter is itself a perp DEX. Its differentiator is **verifiable matching** — order matching and liquidations are executed in a way that can be cryptographically proven (ZK), addressing the trust gap where users must otherwise rely on an operator's good faith for sequencing and liquidation fairness. This targets sophisticated traders who care about MEV resistance and provable fair execution, similar in spirit to a transparent CLOB.

**Derivatives on LIT itself:** LIT is listed as a perpetual on [[hyperliquid|Hyperliquid]] (LIT-PERP). Given the low circulating float and high FDV, the LIT perp can see pronounced [[funding-rate|funding-rate]] swings and open-interest spikes — speculative longs/shorts around unlock events and listing momentum make funding a useful sentiment signal. Thin float means the perp is sensitive to liquidation cascades on sharp moves.

---

## Use Case / Narrative / Category

Lighter is part of the **next-generation perp-DEX** cohort betting that decentralized derivatives volume keeps migrating on-chain. Its narrative leans on **technical credibility** — verifiable matching/liquidations and CEX-level performance — to differentiate from AMM-based and operator-trusted competitors. The bull case is capturing perp volume from CEXs and incumbents; the token thesis depends on fee capture and incentive design accruing value to LIT holders. It is a frequently-cited name in [[perp-dex-aggregation|perp-DEX]] discussions alongside Hyperliquid and dYdX.

---

## Valuation Framing (qualitative)

LIT's ~$382M market cap masks a **~$1.53B fully-diluted valuation** — the single most important number for the token. At ~25% float, the market is effectively pricing four future LIT for every one circulating, so even strong protocol growth can be offset by unlock-driven supply. On a relative basis LIT is *richer* than dYdX (which has a real USDC fee link and much higher float at a smaller cap), so a buyer is paying up for the ZK-verifiable-execution narrative and momentum. The valuation case rests on Lighter winning durable perp volume and translating fees into token value before vesting dilutes holders.

---

## Peer Comparison

| Token | Architecture | MC Rank | Market Cap | MC/FDV | Edge / Risk |
|---|---|---|---|---|---|
| **Lighter (LIT)** | ZK-rollup, verifiable matching | #120 | ~$382M | **~0.25** | Provable execution; heavy unlock overhang |
| [[hyperliquid\|Hyperliquid (HYPE)]] | Own L1 order book | top-tier | multi-$B | high | Volume leader; deep liquidity |
| [[dydx-chain\|dYdX (DYDX)]] | Cosmos appchain CLOB | #268 | ~$101M | ~0.84 | USDC fee link; high float |
| GMX | Oracle/AMM perps | mid-cap | $100Ms | high | Pool-backed, no order book |

---

## Notable History

- A relatively new entrant; the LIT token reached an all-time high around **$7.86** before retracing ~80% through the 2026 bear market.
- Positioned alongside Hyperliquid and dYdX in the competitive perp-DEX landscape, emphasizing ZK-verifiable execution.
- Currently trades ~96% above its all-time low (~$0.78), having found a floor in the recent drawdown.

---

## Risks

- **Dilution overhang:** With only ~25% of supply circulating, scheduled unlocks/emissions are a persistent downside risk; FDV is ~4x market cap.
- **Intense competition:** The perp-DEX space is crowded (Hyperliquid, dYdX, GMX, others); winning durable volume share is uncertain.
- **Bear-market beta:** As a higher-volatility DeFi token, LIT is highly exposed to the current extreme-fear / Established Bear Market backdrop.
- **Unproven longevity:** As a newer protocol, it lacks the multi-cycle track record of older DeFi names; smart-contract and operational risks are elevated.
- **Token value capture:** Like many DEX governance tokens, value accrual to LIT holders is not guaranteed even if the protocol succeeds.

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[hyperliquid]]
- [[dydx-chain]]
- [[perpetual-futures]]
- [[perp-dex-aggregation]]
- [[funding-rate]]
- [[decentralized-exchange]]
- [[zk-rollup]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — historical snapshot context
- Market data as of 2026-06-21 from the crypto-loop CoinGecko markets snapshot (cryptodataapi.com / CoinGecko).
- General market knowledge; no specific wiki source ingested yet for protocol mechanics.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LIT |
| **Market Cap Rank** | #1600 |
| **Market Cap** | $4.83M |
| **Current Price** | $0.1069 |
| **Categories** | Binance Launchpool |
| **Website** | [https://www.litentry.com/](https://www.litentry.com/) |

---

## Overview

Litentry is a privacy-preserving decentralized identity aggregation oracle, built on the Substrate framework and tailored for Polkadot, EVM-based platforms, and other multi-chain ecosystems. It leverages Trusted Execution Environments (TEE), verifiable credentials, and customizable score computation to usher in a new era of digital identity. Its flagship product, the IdentityHub, is transforming how identities are managed and authenticated across blockchains. Its self-sovereign user-centric approach to identity, bridging both Web2 and Web3, offers a robust suite for user activity and identity data management. With tools like the IdentityHub and unique staking mechanisms, Litentry is committed to establishing a unified, privacy-centric decentralized identity infrastructure, redefining interoperability and utility for users and projects in the decentralized space.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 45.17M LIT |
| **Total Supply** | 100.00M LIT |
| **Max Supply** | 100.00M LIT |
| **Fully Diluted Valuation** | $10.69M |
| **Market Cap / FDV Ratio** | 0.45 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $13.31 (2021-02-16) |
| **Current vs ATH** | -99.20% |
| **All-Time Low** | $0.0556 (2026-05-28) |
| **Current vs ATL** | +92.23% |
| **24h Change** | +3.01% |
| **7d Change** | -0.71% |
| **30d Change** | +44.43% |
| **1y Change** | -66.63% |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xb59490ab09a0f526cc7305822ac65f2ab12f9723` |
| Binance Smart Chain | `0xb59490ab09a0f526cc7305822ac65f2ab12f9723` |

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Kraken | LIT/USD | N/A |

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | 0XB59490AB09A0F526CC7305822AC65F2AB12F9723/0XC02AAA39B223FE8D0A0E5C4F27EAD9083C756CC2 | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.litentry.com/](https://www.litentry.com/) |
| **Twitter** | [@litentry](https://twitter.com/litentry) |
| **Telegram** | [litentry](https://t.me/litentry) (18 members) |
| **Discord** | [https://discord.gg/litentry](https://discord.gg/litentry) |
| **GitHub** | [https://github.com/litentry](https://github.com/litentry) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $16,603.61 |
| **Market Cap Rank** | #1600 |
| **24h Range** | $0.1008 — $0.1163 |
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
