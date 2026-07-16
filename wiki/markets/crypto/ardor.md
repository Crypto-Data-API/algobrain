---
title: "Ardor"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [altcoins, crypto]
aliases: ["ARDR", "Ardor Platform"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized"
website: "https://www.ardorplatform.org/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[proof-of-stake]]", "[[smart-contracts]]", "[[binance]]", "[[donchian-channel-breakout]]", "[[crypto-beta-rotation]]"]
---

# Ardor

**Ardor** (ARDR) is a [[proof-of-stake|proof-of-stake]] [[layer-1]] blockchain-as-a-service (BaaS) platform built and maintained by **Jelurida**, the team behind the pioneering Nxt blockchain. Its defining feature is a "parent-child chain" architecture: a single security/forging parent chain (Ardor) anchors many lightweight, customizable **child chains** that businesses can launch without operating their own validator set. Ardor ranks **#687** by market capitalization.

> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

At the snapshot date ARDR traded at **$0.02682192** with a market cap of **$26,780,785** (rank #691), down **2.07%** over 24 hours and down a notable **8.95%** over the trailing 7 days — a heavier slide than most peers in this cohort, set against a broad-market risk-off backdrop (Fear & Greed Index 21 / "Extreme Fear").

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | ARDR |
| **Market Cap Rank** | #691 |
| **Market Cap** | $26,780,785 |
| **Current Price** | $0.02682192 |
| **24h Change** | -2.07% |
| **7d Change** | -8.95% |
| **Genesis Date** | 2018-01-01 (Nxt genesis 2013) |
| **Consensus** | [[proof-of-stake|Forging Proof-of-Stake]] |
| **Categories** | Infrastructure, BaaS, [[smart-contracts|Smart Contract Platform]] |
| **Website** | [https://www.ardorplatform.org/](https://www.ardorplatform.org/) |
> *Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).*

---

## Overview

Ardor is a [[layer-1]] blockchain-as-a-service (BaaS) platform developed by **Jelurida**, a Swiss-registered company that also stewards the original Nxt blockchain. It lets businesses and institutions leverage blockchain without building custom infrastructure: a single main (parent) chain handles security, consensus and decentralization, while customizable **child chains** come ready to use for various business applications. Ardor is the second-generation evolution of Nxt, designed to address blockchain bloat, scalability and customization.

### Parent–child chain architecture

The signature design decision is the separation of security from application logic:

- **Parent chain (Ardor / ARDR)** — provides consensus and security via [[proof-of-stake|forging proof-of-stake]]. ARDR holders forge blocks and secure the entire ecosystem. The parent chain stores only block-header-level data, which keeps the chain lean.
- **Child chains** — independent transactional chains that inherit the parent's security. Each child chain can have its own native token used for transaction fees, so projects are not forced to make users hold ARDR to transact.

This solves a long-standing pain point of the original Nxt model: because Nxt's forgers are paid from transaction fees, fees had to be paid in NXT, meaning any custom currency built on Nxt still required users to hold NXT — diluting the new token's utility. Ardor's child chains let each project denominate fees in its own token while ARDR forgers are compensated via a "bundling/exchange" mechanism that converts child-chain fees back to ARDR.

### Ignis and other child chains

To demonstrate Ardor's capabilities, Jelurida launched **Ignis** as the first public child chain — a feature-complete child implementing the full Nxt feature set (asset exchange, marketplace, messaging, voting, account control, etc.). The Ignis token sale (ICO) raised roughly $15 million for development. Subsequent child chains (e.g. enterprise and permissioned deployments) have followed. Ardor child chains can host equity-trading platforms, digital file transfer, supply-chain tracking, voting and tokenized-asset use cases.

### Blockchain "pruning"

A core scalability claim is that Ardor child-chain transaction data can be **pruned** from the parent chain after being aggregated, reducing on-chain bloat over time. Note that pruning trades full historical data availability for storage efficiency — a design trade-off worth understanding before relying on the chain for permanent record-keeping.

### Consensus mechanics — forging proof-of-stake

Ardor inherits Nxt's **"forging"** [[proof-of-stake|Proof-of-Stake]] model, one of the earliest pure-PoS designs in crypto (Nxt, launched 2013, predates most PoS chains). There is **no mining and no inflationary block subsidy**: the entire ARDR supply was created at the Nxt genesis and migrated to Ardor at the 2018 snapshot. Forgers — accounts with staked ARDR — are selected to produce the next block with probability proportional to their balance, and they are compensated from **transaction fees** rather than newly minted coins. This makes ARDR a **fixed-supply, fee-funded** chain, structurally different from inflationary PoS L1s.

Because each child chain can denominate its own fees, Ardor uses a **bundling** mechanism: "bundlers" collect child-chain transactions, pay the parent-chain ARDR fee on their behalf, and recoup the cost in the child token — decoupling end-user token requirements from the security token while still routing economic value back to ARDR forgers.

### Built-in feature set (no smart-contract VM required)

Unlike EVM chains, Ardor (via Nxt's heritage and the Ignis child) ships a **fixed library of built-in transaction types** rather than a general-purpose [[smart-contracts|smart-contract]] virtual machine: a decentralized asset exchange, a data/marketplace system, encrypted messaging, account control (multi-sig / phasing), voting, aliasing, and a "Lightweight Contracts" framework (off-chain Java contracts triggered by on-chain events). This trades the open-ended flexibility of Solidity for a curated, audited primitive set — fewer footguns, but less composability.

| Metric | Value |
|---|---|
| **Circulating Supply** | 998.47M ARDR |
| **Total Supply** | 998.47M ARDR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $43.73M |
| **Market Cap / FDV Ratio** | 1.00 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $2.04 (2018-01-13) |
| **Current vs ATH** | ~-98.7% |
| **All-Time Low** | $0.00874500 (2016-12-06) |
| **24h Change** | -2.07% |
| **7d Change** | -8.95% |

ARDR peaked during the January 2018 ICO mania and, like most 2017-era altcoins, has spent the years since trading at a small fraction of its all-time high. The current 7-day decline of -8.95% is steeper than the broader top-1000 cohort, consistent with thin liquidity amplifying moves during an "Extreme Fear" market regime (Fear & Greed 21 on 2026-06-22).

---

## Token Role

| Function | Description |
|---|---|
| **Consensus / forging** | ARDR is staked ("forged") to secure the parent chain and validate blocks. |
| **Fee settlement** | Child-chain transaction fees are ultimately converted to ARDR to reward forgers. |
| **Network security anchor** | The economic weight behind every child chain is ARDR's stake. |

ARDR has a fixed supply (~998M, created at the 2013 Nxt genesis and migrated to Ardor in 2018) with no inflationary block reward — forgers earn from transaction fees rather than newly minted coins.

---

## History

- **2013** — **Nxt** launches as one of the first 100%-[[proof-of-stake|proof-of-stake]] blockchains, with its full ~1B coin supply created at genesis; it pioneers built-in features (asset exchange, marketplace, messaging) instead of a scripting VM.
- **2016** — **Jelurida** is formed as the Swiss-registered steward of the Nxt codebase, holding the IP and leading development.
- **2017** — Jelurida announces **Ardor** as Nxt's second-generation successor and runs the **Ignis ICO** (the first child chain), raising ~$15M; ARDR is distributed to NXT holders via snapshot.
- **1 January 2018** — Ardor mainnet goes live; the parent-child architecture separates security (ARDR parent) from application chains (Ignis and later children).
- **2018–present** — additional child chains (including enterprise/permissioned deployments) and interoperability work; development remains concentrated in Jelurida, and broader market mind-share has shifted toward EVM L1/L2 ecosystems.

---

## Governance

- **Single-steward model:** Ardor is developed and maintained primarily by **Jelurida**, which owns the codebase IP. This concentrates roadmap and ecosystem direction in one company — efficient for coherence, but a centralization and key-person risk.
- **On-chain voting primitives:** The protocol exposes a built-in **voting system** and **account-control / phasing** (conditional, multi-party approval) features that child chains can use for governance and treasury actions, but these do not constitute decentralized control over the base protocol itself.
- **No inflation-funded treasury:** Because there is no block subsidy, the protocol has no native emission-funded treasury; development funding has historically come from the ICO proceeds and Jelurida's commercial activity.

---

## Ardor vs. Peer BaaS / Platform Chains

| Dimension | Ardor (ARDR) | Nxt (NXT) | [[stratis]] (STRAX) | [[ethereum|Ethereum]] (ETH) |
|---|---|---|---|---|
| **Consensus** | Forging [[proof-of-stake|PoS]] | Forging [[proof-of-stake|PoS]] | [[proof-of-stake|PoS]] (UTXO) | PoS (post-Merge) |
| **Supply model** | Fixed (no inflation) | Fixed (no inflation) | Inflationary staking | Low net issuance |
| **Programmability** | Built-in features + Lightweight Contracts | Built-in features | C# smart contracts | Full EVM |
| **Architecture** | Parent + pruned child chains | Single chain | Mainchain + sidechains | Single chain + L2s |
| **Steward** | Jelurida | Jelurida | Stratis Group (UK) | Foundation + diffuse |
| **Multi-token fees** | Yes (per child chain) | No (fees in NXT) | No | No (gas in ETH) |
| **Origin** | 2018 (Nxt lineage 2013) | 2013 | 2016 | 2015 |

Ardor's genuinely differentiated features are its **parent-child chain separation**, **child-chain pruning**, and **multi-token fee** model — it directly solved Nxt's "everyone must hold NXT to transact" problem. The trade-off versus EVM platforms is the lack of open-ended smart-contract composability and a much smaller developer ecosystem.

---

## Platform & Chain Information

**Native Chain:** Own [[layer-1]] blockchain (Ardor parent chain + child chains)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | ARDR/USDT | N/A |
| Upbit | ARDR/KRW | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://www.ardorplatform.org/](https://www.ardorplatform.org/) |
| **Twitter** | [@ArdorPlatform](https://twitter.com/ArdorPlatform) |
| **Reddit** | [https://www.reddit.com/r/Ardor/](https://www.reddit.com/r/Ardor/) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 11 |
| **GitHub Forks** | 5 |
| **Commits (4 weeks)** | 1 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **Price (2026-06-22)** | $0.02682192 |
| **Market Cap (2026-06-22)** | $26,780,785 |
| **Market Cap Rank** | #691 |
| **24h Change** | -2.07% |
| **7d Change** | -8.95% |
| **Last Updated** | 2026-06-22 |
| **Historical (2026-04-09)** | 24h volume $106,408; rank #645; 24h range $0.0438–$0.0448 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Risks & Considerations

- **Maturity vs. momentum** — Ardor is technically mature but has limited recent mind-share; the 2018-era BaaS narrative has been overtaken by EVM L1/L2 ecosystems. Adoption of child chains has been modest relative to competing smart-contract platforms.
- **Liquidity / depth** — low 24h turnover means prices can move sharply on small flows, as the -8.95% weekly drop (2026-06-22) illustrates.
- **Concentration & governance** — the network is steered by a single development company (Jelurida); roadmap and ecosystem growth depend heavily on it.
- **Narrative risk** — the parent-child architecture is genuinely differentiated, but the broader market has gravitated toward [[smart-contracts|general-purpose smart-contract]] platforms and rollups, leaving Ardor a niche.
- *Not investment advice — figures are point-in-time and small-cap altcoins are high-volatility, low-liquidity instruments.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & liquidity

Tradable on Binance SPOT only — no liquid perpetual venue, so leverage/short access is limited and this is a spot-primary asset. Perp funding/basis/liquidation strategies do NOT apply. With a single deep venue plus KRW liquidity on Upbit, order flow is concentrated and 24h turnover is thin for a rank ~812 name; this means slippage rises quickly on size, so execution should lean on limit/[[vwap-trading|VWAP-style]] passive fills, smaller clip sizes, and avoiding market orders during low-volume windows. The absence of a perp market also removes cheap directional shorting, so bearish or hedged expressions are hard to size and positioning is effectively long-or-flat spot.

### Applicable strategies

- [[breakout-and-retest]] — thin ARDR spot tends to gap on catalyst then retest; entering on the confirmed retest filters the frequent false breaks in illiquid conditions.
- [[donchian-channel-breakout]] — a channel breakout system captures the rare multi-week trending legs in a range-bound, low-float name while sitting flat through chop.
- [[range-mean-reversion]] — most of the time ARDR oscillates in a low-volume range, favoring fading extremes back toward the mid.
- [[dca-strategy]] — spot-only, fixed-supply infra token suits scheduled accumulation that averages through illiquid drawdowns rather than timing entries.
- [[crypto-beta-rotation]] — as a high-beta small-cap L1, ARDR is best held tactically when the broad alt regime is risk-on and rotated out during risk-off.
- [[atr-trailing-stop]] — volatile, gap-prone moves make an ATR-based trailing stop essential for locking gains and capping downside on spot positions.

### Volatility & regime character

Small-cap ([~$27M, rank ~812]) infrastructure / BaaS [[layer-1]] token with fixed supply and no inflation. It behaves as a high-beta altcoin: sharp, liquidity-amplified moves that trail broad crypto sentiment and correlate strongly with BTC/ETH risk-on/risk-off regimes, typically underperforming in "Extreme Fear" drawdowns. Not a memecoin — moves are driven by market beta and thin depth rather than reflexive social hype. Long stretches of low-volume ranging punctuated by infrequent volatility expansions.

### Risk flags

- **Liquidity / venue concentration** — spot-only, concentrated on Binance (plus Upbit KRW); thin depth amplifies slippage and gap risk, and there is no perp venue for hedging or shorting.
- **Narrative dependence** — the 2018-era BaaS narrative has been overtaken by EVM L1/L2 ecosystems, leaving ARDR a niche with limited mind-share and modest child-chain adoption.
- **Key-person / governance concentration** — steered by a single steward (Jelurida), concentrating roadmap and ecosystem risk.
- **Low developer activity** — minimal recent commit cadence signals limited ongoing catalyst flow.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] Binance-spot endpoints (auth via `X-API-Key`). No perp/funding endpoints apply — no liquid perp venue.

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ARDRUSDT` — current price
- `GET /api/v1/market-data/ticker/24hr?symbol=ARDRUSDT` — 24h ticker stats (volume, range, change)

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ARDRUSDT&interval=1d&limit=1000` — OHLCV klines
- `GET /api/v1/market-data/volume-history?days=90` — daily volume + buy ratio
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ARDRUSDT&interval=1d&limit=1000"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[proof-of-stake]]
- [[smart-contracts]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-22 (cryptodataapi.com / CoinGecko).
- General market knowledge; no additional specific wiki source ingested yet.

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 998.47M ARDR |
| **Total Supply** | 998.47M ARDR |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $20.34M |
| **Market Cap / FDV Ratio** | 1.00 |

---
