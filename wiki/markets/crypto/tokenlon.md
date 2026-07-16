---
title: "Tokenlon"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, decentralized-exchange, defi]
aliases: ["LON"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://tokenlon.im/"
related: ["[[arbitrum]]", "[[automated-market-maker]]", "[[crypto-markets]]", "[[decentralized-exchange]]", "[[defi]]", "[[ethereum]]", "[[governance-token]]", "[[slippage]]", "[[uniswap]]"]
---

# Tokenlon

**Tokenlon** (LON) is a [[decentralized-exchange|decentralized exchange]] and trade aggregator that originated from the **imToken** crypto wallet, one of the most widely used self-custody wallets in Asia. Tokenlon lets users swap tokens directly from their wallet using an off-chain request-for-quote (RFQ) model backed by professional market makers, settling trades on-chain on [[ethereum|Ethereum]] (and later other networks). **LON** is the protocol's utility and [[governance-token|governance token]], used to align ecosystem stakeholders and incentivize participation.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).* LON: $0.184417, rank #757, market cap $22,764,695, 24h -1.28%, 7d -3.70%. Market backdrop: Fear & Greed Index at 21 (Extreme Fear).

As of 2026-06-22, LON traded at **$0.184417**, ranked **#757** by market capitalization with a market cap of approximately **$22.76M**. The token was soft over the short term — **-1.28% over 24 hours** and **-3.70% over the trailing 7 days** — a relatively contained reading against an "Extreme Fear" market backdrop (Fear & Greed 21, [[bitcoin]] under pressure). LON remains far below its January 2021 all-time high near $9.81, reflecting the broad de-rating of older [[defi]] tokens.

---

## What Tokenlon Does

Tokenlon is a [[decentralized-exchange]] and DEX aggregator embedded in the imToken wallet experience. Rather than relying solely on an on-chain [[automated-market-maker|AMM]] pool, Tokenlon historically pioneered an **RFQ (request-for-quote)** design: when a user requests a swap, professional market makers compete to provide a quote off-chain, and the winning quote is settled on-chain. This hybrid model can deliver tighter pricing and reduced slippage on larger trades versus a pure constant-product AMM, while keeping custody with the user.

Its origin inside imToken gave Tokenlon distribution to a large mobile-first, self-custody user base, particularly in Asian markets — a meaningful differentiator in the crowded DEX landscape.

---

## Mechanism and Architecture

- **RFQ / professional market makers** — off-chain quoting by market makers, on-chain settlement. This reduces failed transactions and front-running exposure relative to fully on-chain order matching, and improves execution for size.
- **Aggregation** — Tokenlon also routes across liquidity sources to find better execution, functioning as an aggregator in addition to its own RFQ liquidity.
- **Wallet-native UX** — deep integration with imToken means swaps happen within a familiar self-custody wallet rather than a separate dApp interface, lowering friction for retail users.
- **Multi-chain reach** — beyond Ethereum, LON and Tokenlon liquidity have extended into ecosystems such as [[arbitrum|Arbitrum]].

### RFQ vs AMM: why it matters

An [[automated-market-maker|AMM]] like [[uniswap|Uniswap]] prices every swap along a constant-product curve, so larger orders walk the curve and incur **[[slippage|slippage]]** proportional to trade size relative to pool depth. An **RFQ** model instead asks professional market makers for a firm quote for the full size: the maker prices the whole order at once using their own inventory and off-chain hedging, then commits to settle on-chain. For larger trades this can deliver a single, tighter price with no curve-walking, and because the quote is signed off-chain the user is shielded from on-chain front-running between quote and settlement. The trade-off is reliance on maker participation and quote competitiveness rather than always-available passive pool liquidity.

### Illustrative swap flow

1. User requests a swap (e.g., 50,000 USDC → ETH) inside the imToken wallet.
2. Tokenlon's system solicits quotes from connected professional market makers (and may compare against aggregated on-chain routes).
3. The best signed quote is returned to the user with a fixed price and short validity window.
4. The user signs; the trade settles on-chain via Tokenlon's settlement contract. If no maker beats available on-chain liquidity, the aggregator can route to that instead. *(Illustrative; exact routing logic per protocol docs.)*

---

## Token Role: LON

LON is the Tokenlon ecosystem's utility and [[governance-token|governance token]]. Its intended roles include:

- **Governance** — participation in decisions about protocol parameters and direction.
- **Staking / fee sharing** — staking LON (historically into mechanisms such as a buyback-and-stake model) to earn a share of protocol trading-fee revenue and align holders with platform usage.
- **Ecosystem incentives** — rewarding liquidity provision and active usage to bootstrap and retain volume.

LON has a relatively high market-cap-to-FDV ratio (most supply already circulating), which limits future dilution overhang compared with many newer DeFi tokens — a notable structural difference from heavily-emitting peers.

### Value accrual & governance

- **Buyback-and-stake** — historically Tokenlon directed a portion of protocol trading-fee revenue into **buying back LON** and rewarding stakers, so LON value accrual is tied to platform trading volume rather than to inflationary emissions. When swap volume is high, more fees flow to stakers; when volume is thin (as in a bear market), the value-accrual loop weakens.
- **veToken-style alignment** — staking mechanisms reward longer-term lockers with a larger share of distributed rewards and governance weight, aligning holders with sustained usage.
- **Governance scope** — LON holders participate in decisions on fee parameters, treasury allocation, supported chains, and ecosystem incentives.

---

## History & Notable Events

- **2017–2019** — Tokenlon launches as an in-wallet swap feature inside **imToken**, one of the most-used self-custody wallets in Asia, initially built around 0x-protocol order relaying.
- **2020–2021** — Tokenlon evolves into a standalone DEX/aggregator with its RFQ market-maker model; the **LON** token launches in 2021 with a community distribution, reaching an all-time high near **$9.81** in the January 2021 DeFi run-up.
- **2022 onward** — Like most older DeFi tokens, LON de-rates sharply through the bear market; the protocol extends to additional chains (Arbitrum) and continues operating as a wallet-native swap venue, but token liquidity and volume remain thin.

---

## Competitive Position

Tokenlon competes in the DEX and DEX-aggregator space against [[uniswap|Uniswap]], 1inch, CowSwap, and other RFQ/aggregation venues. Its edge is distribution (imToken integration) and an RFQ model suited to larger, lower-slippage trades. The headwinds are the same facing all older DeFi tokens: liquidity has consolidated around a handful of dominant DEXs, and trading volume on the LON token itself has been thin (its on-chain spot pairs show modest daily turnover), which can make price discovery noisy and exit liquidity limited.

### Comparison vs DEX / aggregator peers

| Venue | Model | Native liquidity | Distribution edge | Token | Best-fit trade |
|---|---|---|---|---|---|
| **Tokenlon** | RFQ + aggregation | Professional market makers | imToken wallet integration (Asia) | LON | Larger size, low slippage, in-wallet |
| [[uniswap\|Uniswap]] | Constant-product [[automated-market-maker\|AMM]] | Passive LP pools | Brand, deepest pools, ubiquity | UNI | Always-on, long-tail tokens |
| 1inch | Pure aggregator | Routes across DEXs | Best-execution routing | 1INCH | Splitting across many pools |
| CowSwap | Batch auction + solvers | Solver-sourced + CoW matching | MEV protection, coincidence-of-wants | COW | MEV-sensitive, surplus capture |

Tokenlon's RFQ niche overlaps most with CowSwap's solver model (both source firm prices off-chain) but its real differentiator remains native imToken distribution rather than standalone protocol pull.

---

## Risks

- **Thin token liquidity** — LON's traded volume has been low, so the token is susceptible to slippage and sharp moves on relatively small flow.
- **Micro-cap status** — at ~$22.9M (rank #757), it is a small-cap asset with concentrated risk.
- **Competitive pressure** — DEX/aggregator market share is dominated by a few leaders; sustaining relevance requires continued differentiation.
- **Smart-contract risk** — as with any [[defi]] protocol, contract bugs or exploits can cause losses; verify audit status independently.
- **Dependence on market makers** — the RFQ model relies on professional market makers providing competitive quotes; reduced market-maker participation degrades execution quality.

> **Data disclaimer:** Figures above are point-in-time market snapshots (2026-06-22) and qualitative descriptions of mechanism. Volume, TVL, and staking-yield details are not independently verified here and should be confirmed against official documentation before any decision.

---

## Platform & Chain Information

**Native Chain:** [[ethereum|Ethereum]]

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0x0000000000095413afc295d19edeb1ad7b71c952` |
| Arbitrum One | `0x55678cd083fcdc2947a0df635c93c838c89454a3` |

---

## Tokenomics

| Metric | Value |
|---|---|
| **Max Supply** | 200.00M LON |
| **Market Cap / FDV** | High (most supply circulating) |

*Note: exact circulating supply and FDV change with each snapshot; re-verify at source.*

---

## Exchange Listings

### Decentralized Exchanges

| Exchange | Pair | Type |
|---|---|---|
| Uniswap V2 (Ethereum) | LON / WETH | Spot |
| Sushiswap | LON / USDT | Spot |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://tokenlon.im/](https://tokenlon.im/) |
| **Twitter** | [@tokenlon](https://twitter.com/tokenlon) |
| **Discord** | [https://discord.gg/nPmsMrG](https://discord.gg/nPmsMrG) |

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
- [[decentralized-exchange]]
- [[automated-market-maker]]
- [[uniswap]]
- [[slippage]]
- [[defi]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko snapshot).
- General market knowledge; no additional specific wiki source ingested yet.

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | LON |
| **Market Cap Rank** | #787 |
| **Market Cap** | $21.64M |
| **Current Price** | $0.1753 |
| **Categories** | Decentralized Exchange (DEX), Exchange-based Tokens, Decentralized Finance (DeFi) |
| **Website** | [https://tokenlon.im/](https://tokenlon.im/) |

---

## Overview

LON is a utility token issued by the Tokenlon DEX, used to align all ecosystem stakeholders and incentivize participation and expansion of the ecosystem.

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $9.81 (2021-01-30) |
| **Current vs ATH** | -98.21% |
| **All-Time Low** | $0.0669 (2026-01-24) |
| **Current vs ATL** | +161.93% |
| **24h Change** | +0.50% |
| **7d Change** | +1.85% |
| **30d Change** | -9.52% |
| **1y Change** | -76.64% |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $13,404.97 |
| **Market Cap Rank** | #787 |
| **24h Range** | $0.1731 — $0.1832 |
| **CoinGecko Sentiment** | 100% positive |
| **Last Updated** | 2026-07-16 |

---
