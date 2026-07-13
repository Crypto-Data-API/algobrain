---
title: "Vana"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, machine-learning, ai-trading, data-provider]
aliases: ["VANA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.vana.org/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[decentralized-ai]]", "[[ocean-protocol]]", "[[ai-agent-tokens]]", "[[artificial-intelligence]]", "[[data-daos]]"]
---

# Vana

**Vana** (ticker **VANA**) is an EVM-compatible Layer 1 that lets individuals aggregate, tokenize, and monetize their personal data through Data Liquidity Pools (DLPs) — essentially [[data-daos|Data DAOs]] where users contribute data (chat logs, social history, fitness tracking, purchase records) and receive proportional ownership of the resulting tokenized dataset. It sits at the **data layer** of [[decentralized-ai|decentralized AI]] and is the most technically distinctive attempt to solve the problem of "user-owned training data" in the post-ChatGPT era.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | VANA |
| **Current Price** | $1.15 |
| **Market Cap** | $35.56M |
| **Market Cap Rank** | #572 |
| **Fully Diluted Valuation** | ~$138.0M |
| **24h Volume** | $2.14M |
| **24h Change** | +2.69% |
| **7d Change** | +2.83% |
| **Circulating Supply** | 30.80M VANA |
| **All-Time High** | $35.23 (2024-12-17), -96.7% |
| **All-Time Low** | $1.03 (2026-06-06) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

VANA trades roughly 97% below its December 2024 all-time high of $35.23 and is hovering just above the all-time low of $1.03 set on 2026-06-06. The backdrop is an extreme-fear market (Crypto Fear & Greed Index of ~23, established bear market — see [[fear-and-greed-index]]). The very low market-cap/FDV ratio of ~0.26 is the dominant near-term risk: most of the supply has not yet entered circulation, so ~$2.1M of daily turnover sits against a large pending unlock.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 30.80M VANA |
| **Total Supply** | 120.00M VANA |
| **Max Supply** | 120.00M VANA |
| **Market Cap / FDV** | 0.26 |

**Dilution overhang is severe.** Only ~30.8M of 120M tokens (26%) circulate, so ~89M VANA (74% of max supply) — team, investor, foundation, and ecosystem allocations — remains to unlock. At today's price that locked supply is worth ~$102M against a $35M circulating cap, meaning future unlocks can dwarf the current float. This is the classic "low-float / high-FDV" structure of a recent VC-backed launch and is the single biggest structural headwind to price.

---

## How Vana Fits into Decentralized AI

The core insight behind Vana is that AI model quality is bottlenecked by data, and most of the world's interesting training data is owned by platforms (Google, Meta, OpenAI) rather than by the users who generated it. Vana's DLP model tries to flip this: if users can contribute their data to a shared pool, retain fractional ownership via a tradeable token, and collectively sell access to AI buyers, then the value of the data accrues back to its creators rather than to the platforms.

This is a genuinely novel design compared to [[ocean-protocol|Ocean Protocol]] (which focuses on data marketplaces for business-grade datasets) and [[grass]] (which tokenizes bandwidth rather than the data itself). Vana's **Proof-of-Contribution** system is the mechanism that makes DLPs economically coherent: contributed data is validated for quality, contributors earn VANA-denominated rewards proportional to quality, and DLP creators earn fees from data sales.

---

## Technology

Vana is an EVM-compatible Layer 1 with two protocol-level primitives:

- **Data Liquidity Pools (DLPs)** — on-chain pools where users contribute private datasets that are validated and tokenized; DLP tokens represent fractional ownership and a claim on data-sale revenue.
- **Proof-of-Contribution (PoC)** — the validation mechanism that scores contributed data for quality and authenticity before rewarding contributors, preventing spam/low-quality submissions from diluting a pool.

Incentive structure: data contributors, validators, and DLP creators are all rewarded in $VANA, aligning the network around producing high-quality, sellable datasets. Architecturally Vana is its own L1 but maintains broad cross-ecosystem reach, with the token bridged across Ethereum, Base, BNB Chain, Polygon, Arbitrum, and Optimism.

---

## How & Where It Trades

**Centralized exchanges (spot):** VANA is listed on Binance (VANA/USDT), Upbit (VANA/KRW), Bitget (VANA/USDT), and KuCoin (VANA/USDT) — a solid tier-1 footprint for a sub-$600 rank token.

**Derivatives:** No major Hyperliquid perp is tracked for VANA in the current snapshot; derivatives exposure is limited relative to spot. Traders relying on hedging or leverage should confirm live CEX perp availability before sizing, as small-cap AI tokens can see funding/OI spikes around unlock and narrative events.

**DEX (spot):** Uniswap V3 on Ethereum provides on-chain liquidity (VANA/WETH).

---

## Valuation Framing (qualitative)

VANA is best understood as a **pre-revenue option on the data-ownership thesis**, not a cash-flow asset. Three lenses:

- **MC/FDV (~0.26)** — the single most important number. ~74% of supply is uncirculated, so today's ~$36M cap understates the eventual diluted base (~$138M FDV). Any spot strength has to absorb a multi-year unlock schedule.
- **vs. revenue** — DLP data-sale revenue is the fundamental that should eventually back the token, but it is currently small; the cap is narrative- and beta-driven, not a multiple of recurring data sales.
- **vs. comparable AI-data peers** — see table below. VANA carries a higher dilution overhang than near-fully-circulating peers, which is why low-float dynamics dominate its short-term price action.

The honest read: this is a long-dated venture-style bet where price discovery is driven by the AI cycle and unlock cadence far more than by usage.

---

## Peer Comparison

| Token | Rank | Price | Market cap | MC/FDV | Sub-niche |
|---|---|---|---|---|---|
| **VANA** | #572 | $1.15 | ~$36M | ~0.26 | User-owned data L1 (Data DAOs) |
| [[ocean-protocol\|OCEAN]] | mid-cap | — | — | high | Data marketplace |
| [[grass\|GRASS]] | mid-cap | — | — | low-float | Bandwidth/data scraping |
| [[neo\|NEO]] | #204 | $2.21 | ~$156M | ~0.71 | Legacy smart-economy L1 |

Among the decentralized-AI cohort, VANA is the most distinctive on design (Proof-of-Contribution + DLPs) but also the most exposed to unlock-driven supply pressure.

---

## Trading Thesis and Honest Assessment

Vana is a long-dated bet on **user-owned data becoming economically competitive with platform-owned data** for AI training. The tailwinds are real (regulatory pressure on platform data practices, growing user awareness, synthetic-data quality plateaus) but the timelines are long and adoption depends on AI buyers actually paying for DLP data at prices that make contributor incentives work. The closest historical analog is "data unions" — an idea that has existed in various forms for a decade without breaking through commercially. Vana could finally provide the incentive alignment this idea has always lacked, or it could repeat the pattern of slow adoption.

Token price in the near term is dominated by the [[ai-narrative-arc|AI narrative cycle]], airdrop/investor unlock schedules, and Layer 1 beta — not by DLP revenue, which remains small. Structural success (DLP revenue becoming meaningful) is a multi-year question.

---

## Use Case, Narrative & Category

VANA is a **decentralized-AI / data-ownership** narrative token. CoinGecko categories include Artificial Intelligence (AI), Smart Contract Platform, Layer 1, and the portfolios of Paradigm, Coinbase Ventures, DeFiance, and Polychain. The bull case is data unions finally finding product-market fit with AI buyers; the bear case is that adoption stays slow while heavy unlocks pressure the token.

---

## Notable History

- **Mainnet / token launch late 2024**; VANA peaked at ~$35.23 on 2024-12-17 during peak AI-token enthusiasm.
- Backed by prominent funds (Paradigm, Coinbase Ventures, Polychain, DeFiance).
- Suffered a ~97% drawdown through 2025–2026, setting a fresh all-time low of $1.03 on 2026-06-06 amid the bear market and ongoing unlock pressure.

---

## Risks

- **Severe unlock/dilution overhang** — only 26% of supply circulates; ~74% remains to unlock, a persistent structural sell-pressure source.
- **Demand-side uncertainty** — DLP revenue depends on AI buyers actually paying for user-contributed data at scale, which is unproven.
- **Narrative dependence** — price is driven by the AI token cycle far more than by fundamentals today.
- **Competition** — Ocean Protocol, Grass, and other data/AI-infrastructure projects compete for the same thesis and capital.
- **Early-stage execution** — L1 maturity, validator decentralization, and data-quality enforcement (PoC) are still being proven.
- **Macro/regime** — extreme-fear sentiment (F&G ~23) and an established bear market weigh on all early-stage AI tokens.

---

## See Also

- [[decentralized-ai]] — Parent movement
- [[data-daos]] — the DLP / Data DAO primitive
- [[ocean-protocol]] — Adjacent data-marketplace approach
- [[grass]] — Bandwidth tokenization peer
- [[ai-agent-tokens]] — Broader AI token landscape
- [[artificial-intelligence]] — AI section hub
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`)
