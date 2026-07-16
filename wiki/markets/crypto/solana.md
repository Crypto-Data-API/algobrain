---
title: "Solana"
type: entity
created: 2026-04-06
updated: 2026-07-16
status: review
tags: [crypto, defi, markets, solana, hyperliquid, perpetual-futures, funding-rate, derivatives, open-interest, liquidations]
aliases: ["SOL"]
entity_type: protocol
founded: 2020
headquarters: "Decentralized"
website: "https://solana.com"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[defi]]", "[[ethereum]]", "[[proof-of-stake]]", "[[staking]]", "[[hyperliquid]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[cryptodataapi]]"]
---

# Solana

**Solana** (SOL) is a high-performance Layer 1 [[blockchain]] designed for speed and low transaction costs. Founded by **Anatoly Yakovenko** and launched on mainnet in March 2020, Solana differentiates itself from [[ethereum|Ethereum]] through its **Proof of History (PoH)** mechanism layered on [[proof-of-stake]], enabling theoretical throughput of ~65,000 transactions per second (TPS) at a fraction of a cent per transaction.

After nearly being left for dead following the [[ftx|FTX]] collapse in November 2022 -- which cratered SOL from ~$35 to under $10 due to deep FTX/Alameda ties -- Solana staged one of the most remarkable comebacks in crypto history. Surging [[defi]] activity, a vibrant meme-coin culture, and genuine developer momentum propelled SOL back into the top tier of cryptoassets.

---

## Market Data

| Metric | Value |
|---|---|
| **Rank** | #7 |
| **Price** | $71.52 |
| **Market Cap** | $41.50 billion |
| **24h Volume** | $1.90 billion |
| **24h Change** | +4.53% |
| **7d Change** | +6.18% |
| **Circulating Supply** | 580,291,391 SOL |
| **Total Supply** | 628,690,500 SOL |
| **Max Supply** | None (uncapped; disinflationary issuance schedule) |
| **Fully Diluted Valuation** | $44.96 billion |
| **All-Time High** | $293.31 (2025-01-19) — currently -75.6% |
| **All-Time Low** | $0.5008 (2020-05-11) — currently +14,181% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

**Macro backdrop (2026-06-20):** [[crypto-market-sentiment|Fear & Greed]] = **22 (Extreme Fear)**; **Established Bear Market**. SOL is the deepest-drawdown major here (~-76% from its Jan 2025 ATH), consistent with its high beta — yet it printed the strongest 24h/7d bounce of the six flagships (+4.5%/+6.2%), a reminder that high-beta names lead both legs of a move.

---

## Key Facts

| Field | Detail |
|---|---|
| **Ticker** | SOL |
| **Creator** | Anatoly Yakovenko (Solana Labs) |
| **Mainnet Launch** | March 2020 |
| **Consensus** | Proof of History (PoH) + [[proof-of-stake|Proof of Stake]] |
| **Throughput** | ~65,000 TPS theoretical; ~2,000-4,000 TPS realized |
| **Block Time** | ~400 milliseconds |
| **Transaction Cost** | Typically < $0.01 |
| **Staking Yield** | ~6-8% APR |
| **Website** | [solana.com](https://solana.com) |

---

## Technology & Consensus

### Proof of History

Solana's core innovation is **Proof of History (PoH)** -- a cryptographic clock that creates a verifiable ordering of events without all validators communicating about timing. Instead of consensus on *when* transactions occurred, PoH pre-orders them using a verifiable delay function (recursive SHA-256 hashing). This lets validators process transactions in parallel rather than sequentially, dramatically increasing throughput.

Supporting innovations:

| Component | Role |
|---|---|
| **Tower BFT** | PoH-optimized Byzantine Fault Tolerance consensus |
| **Gulf Stream** | Mempool-less transaction forwarding |
| **Turbine** | Block propagation (sharded to peers) |
| **Sealevel** | Parallel smart-contract runtime (multi-core) |
| **Firedancer** | Independent high-performance validator client (Jump Crypto) improving resilience & throughput |

### Monolithic vs. Modular

Solana takes a **monolithic** approach: one chain handles execution, consensus, and data availability together. This contrasts with [[ethereum|Ethereum's]] **modular** strategy of outsourcing execution to [[arbitrum|L2 rollups]].

| Approach | Solana (monolithic) | Ethereum (modular) |
|---|---|---|
| **Scaling** | Single optimized chain | L1 + L2 rollups |
| **Composability** | Native; all apps on one chain | Fragmented across L2s |
| **Hardware** | High (powerful validators) | Lower per layer |
| **Decentralization** | Fewer, more powerful validators | More validators across layers |
| **UX** | Simple; no bridging | Bridging between L2s |

This debate directly impacts SOL/ETH relative-value trades. Solana's historical weakness has been **network outages** (multiple in 2022); reliability has improved markedly since, aided by the **Firedancer** client.

---

## Tokenomics & Supply Schedule

- **No hard cap.** SOL launched with ~8% annual inflation, decaying ~15% per year toward a long-run ~1.5% terminal rate.
- **Net issuance offsets:** ~50% of transaction fees are **burned**, and a large share of priority fees + MEV tips accrue to stakers. Periods of intense meme-coin/priority-fee demand sharply raise validator revenue and can make real (net) issuance very low.
- **Staking:** ~60-70% of SOL is typically staked (high participation) at ~6-8% APR. High staking ratio reduces liquid float; liquid staking (JitoSOL, mSOL) re-mobilizes it across [[defi]].
- **Circulating vs total:** circulating (580.3M) is below total supply (628.7M); FDV ($44.96B) exceeds market cap ($41.50B), so modest residual unlock/emission overhang exists.

---

## Ecosystem & Use Cases

| Protocol | Category | Significance |
|---|---|---|
| **Jupiter** | DEX aggregator | Largest swap venue on Solana; routes the majority of spot flow |
| **Raydium** | AMM / DEX | Core liquidity venue and launchpad |
| **pump.fun** | Token launchpad | Engine of the meme-coin boom; major fee generator |
| **Marinade / Jito** | Liquid staking | mSOL / JitoSOL (JitoSOL adds MEV rewards) |
| **Drift** | Perp DEX | On-chain derivatives |
| **Kamino** | Lending / vaults | Leading Solana money market |
| **Tensor** | NFT marketplace | Leading Solana NFT venue |

### Meme-Coin Culture & Payments

Solana became the epicenter of the 2023-2024 **meme-coin boom**, with near-zero fees enabling rapid token creation (pump.fun). This drove massive transaction volume and onboarded users, but is a double-edged sword: it inflates usage metrics and fee revenue while attracting regulatory and reputational scrutiny. Beyond memes, Solana has pushed into **payments/RWA** -- e.g., Visa's USDC settlement on Solana and equity tokenization by firms like Galaxy Digital.

---

## Market Structure & Derivatives

| Characteristic | Detail |
|---|---|
| **Rank** | #7 |
| **Liquidity** | High; among the most liquid altcoins |
| **Volatility** | Significantly higher than [[bitcoin\|BTC]]/[[ethereum\|ETH]]; 10-20% daily moves possible |
| **Beta to BTC** | High; ~1.5-2.5x BTC moves |
| **Primary spot pairs** | SOL/USDT ([[binance]]), SOL/USD ([[coinbase]], Kraken) |
| **Primary perp** | SOL-PERP ([[hyperliquid]]) + all major CEX perp venues; on-chain via Drift |

### Spot Solana ETFs

US spot **SOL ETFs** progressed through 2025-2026 under the SEC's new generic listing standards, with multiple issuers filing (and some staking-enabled structures proposed). A spot SOL ETF -- especially one with pass-through staking yield -- is a standing catalyst that would mirror the institutional access [[bitcoin-etfs|BTC ETFs]] unlocked in 2024. In the current Extreme-Fear regime, alt-ETF flows tend to be muted. *(Flow magnitudes vary daily and are not quoted here to avoid stale figures.)*

### Funding, OI & Basis

SOL [[funding-rate|funding rates]] can be **extreme** during trending markets (meme-driven euphoria), creating rich [[basis-trade|basis]]/[[arbitrage]] opportunities and elevated [[liquidation]] risk on crowded [[perpetual-futures|perps]]. SOL-PERP ranks among the top markets on [[hyperliquid]] by volume; [[open-interest]] surges into meme cycles are a classic over-leverage warning.

---

## On-chain & Valuation Frameworks

| Metric | What it measures | Trading use |
|---|---|---|
| **Real economic value (REV)** | Total fees + tips + MEV paid | Proxy for genuine demand/usage |
| **DEX volume (Jupiter)** | On-chain swap throughput | Leading indicator for SOL momentum |
| **Active addresses / new tokens** | Network adoption & meme activity | Sentiment gauge |
| **Staking ratio** | % of supply staked | Liquid-float scarcity + yield benchmark |
| **Net issuance (after burn)** | Effective inflation | Supply-pressure input |
| **MVRV / cost basis** | Aggregate cost basis vs price | Cyclical value zones (as for BTC/ETH) |

---

## Trading Playbook

- **High-beta directional vehicle** — SOL amplifies broad-market moves; a way to express crypto-beta without explicit [[leverage]].
- **SOL/ETH ratio** — the monolithic-vs-modular relative-value trade; rising SOL/ETH = market favoring Solana's design.
- **Meme-cycle sentiment** — surging pump.fun launches and DEX volume often precede/accompany SOL rallies; collapsing meme volume warns of distribution.
- **Funding extremes** — fade blowout positive [[funding-rate]]; respect [[liquidation]] clusters given SOL's volatility.
- **ETF catalyst** — spot SOL ETF (esp. staked) approval is a structural re-rating event.
- **Regime sizing** — deepest drawdown of the majors; in a bear/extreme-fear regime, size for outsized volatility in both directions.

---

## History & Cycles

| Date | Event |
|---|---|
| Mar 2020 | Mainnet beta launch |
| 2021 | DeFi/NFT boom; SOL to ~$260 (Nov 2021) |
| 2022 | Multiple network outages; [[ftx\|FTX]] collapse craters SOL below $10 |
| 2023 | Recovery begins; developer activity rebounds |
| 2024 | Meme-coin boom (pump.fun); SOL reclaims top tier |
| Jan 2025 | All-time high $293.31 |
| 2025-26 | Firedancer rollout; SOL ETF filings progress |
| Jun 2026 | $71.52 — deep bear drawdown (~-76% from ATH) |

### FTX Connection & Recovery

[[ftx|FTX]]/Alameda were among SOL's largest holders and backers; their November 2022 collapse forced liquidation that cratered the price below $10, while a wave of 2022 outages compounded the credibility crisis. The subsequent recovery — fewer outages, real developer activity, the meme wave, and contrarian buying — powered SOL from ~$10 back to a $293 ATH, forging a fiercely loyal community. This collapse-and-resurrection arc defines Solana's market identity.

---

## Competitive Positioning

| Asset | Rank | Mkt Cap | Consensus | Core thesis |
|---|---|---|---|---|
| **Solana (SOL)** | #7 | $41.5B | PoH + [[proof-of-stake\|PoS]] | Monolithic high-throughput L1 |
| [[bitcoin\|Bitcoin (BTC)]] | #1 | $1.27T | [[proof-of-work]] | Digital gold |
| [[ethereum\|Ethereum (ETH)]] | #2 | $208B | [[proof-of-stake]] | Modular settlement + L2s |
| [[cardano\|Cardano (ADA)]] | #18 | $6.1B | Ouroboros [[proof-of-stake\|PoS]] | Research-driven L1 |
| [[polkadot\|Polkadot (DOT)]] | #51 | $1.63B | NPoS | Layer-0 multichain |

> Peer market data as of 2026-06-20 (CoinGecko). SOL is the primary "ETH killer" beneficiary of the high-throughput / consumer-app narrative.

---

## Regulatory

- **US**: SOL was named as an alleged unregistered security in past SEC enforcement actions against exchanges -- a litigation overhang that has eased as spot SOL ETF filings advanced under the SEC's newer listing framework.
- **Staking**: staking-as-a-service and staked-ETF structures are the key regulatory frontier (as with [[ethereum|ETH]]).
- **Meme coins**: pump.fun-style launches draw consumer-protection scrutiny.

---

## Risks

- **Reliability** — historical outage track record; resilience improved but not eliminated.
- **High beta** — outsized drawdowns in risk-off (deepest of the majors currently).
- **Centralization** — fewer, higher-spec validators; client diversity improving via Firedancer.
- **Meme dependence** — a large share of fees/activity ties to speculative meme cycles that can evaporate.
- **Unlock/emission** — FDV > market cap; residual supply overhang.
- **Funding/liquidation** — extreme perp funding and [[liquidation]] cascades in trending markets.

> **Risk warning:** Crypto assets are highly volatile and speculative. Nothing here is investment advice. SOL's high beta means the largest drawdowns among the majors in the current Extreme-Fear / bear regime.

---

## Related

- [[ethereum]] -- Primary competitor; the modular alternative (SOL/ETH ratio)
- [[bitcoin]] -- Market leader setting the macro tone
- [[cardano]] / [[polkadot]] -- Other L1 peers
- [[defi]] -- Growing Solana DeFi ecosystem
- [[ftx]] -- The collapse that nearly destroyed Solana
- [[proof-of-stake]] / [[staking]] -- Consensus and yield
- [[bitcoin-etfs]] -- Template for the pending SOL ETF
- [[hyperliquid]] -- DEX where SOL-PERP is a top market
- [[binance]] / [[coinbase]] -- Largest CEX venues
- [[perpetual-futures]] / [[funding-rate]] / [[open-interest]] / [[basis-trade]] -- Derivatives toolkit
- [[crypto-markets]] -- Market landscape overview

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]]) — original auto-generated entity data
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko (`raw/data/crypto-loop/coingecko-markets.json`); macro backdrop from `raw/data/crypto-loop/_digest.md` (Fear & Greed = 22; Established Bear Market)

## Overview

Solana is a high-performance Layer 1 blockchain designed for mass adoption by providing a fast, secure, and low-cost environment for decentralized applications. It distinguishes itself by scaling globally without the use of complex sharding or multiple layers, instead maintaining a single, unified ledger to avoid liquidity fragmentation. This architecture allows it to process thousands of transactions per second with sub-second finality, often at a cost of less than a penny per transaction.

The network operates on a unique hybrid model that combines Proof of Stake with an innovation called Proof of History, which functions as a decentralized clock to timestamp transactions. This system reduces the need for constant node communication, allowing the Sealevel engine to run non-conflicting smart contracts in parallel across multiple CPU cores. Further efficiency is gained through the Gulf Stream protocol, which reduces confirmation times by forwarding transactions to validators before the current block is finished.

Founded in 2017 by Anatoly Yakovenko, Solana is now supported by the Switzerland-based Solana Foundation and significant institutional investors like Andreessen Horowitz and Polychain Capital. The platform’s native token, SOL, serves as the primary currency for paying transaction fees, participating in network governance, and securing the system through staking. 

Solana has also seen significant institutional adoption ranging from spot Solana ETFs to major partnerships including Visa's 2025 launch of USDC settlement on the network and the tokenization of public equity by firms like Galaxy Digital.

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 582.41M SOL |
| **Total Supply** | 630.36M SOL |
| **Max Supply** | Unlimited |
| **Fully Diluted Valuation** | $47.97B |
| **Market Cap / FDV Ratio** | 0.92 |

---

## Price History

| Metric | Value |
|---|---|
| **All-Time High** | $293.31 (2025-01-19) |
| **Current vs ATH** | -74.05% |
| **All-Time Low** | $0.5008 (2020-05-11) |
| **Current vs ATL** | +15096.99% |
| **24h Change** | -1.57% |
| **7d Change** | -2.47% |
| **30d Change** | +1.62% |
| **1y Change** | -53.95% |

---

## Platform & Chain Information

**Native Chain:** Own blockchain (Layer 1)

---

## Exchange Listings

### Centralized Exchanges

| Exchange | Pair | Trust Score |
|---|---|---|
| Binance | SOL/USDT | N/A |
| Kraken | SOL/USD | N/A |
| Bitget | SOL/USDT | N/A |
| KuCoin | SOL/USDT | N/A |
| Crypto.com Exchange | SOL/USD | N/A |

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://solana.com/](https://solana.com/) |
| **Reddit** | [https://www.reddit.com/r/solana](https://www.reddit.com/r/solana) |
| **GitHub** | [https://github.com/solana-labs/solana](https://github.com/solana-labs/solana) |
| **Whitepaper** | [https://solana.com/solana-whitepaper.pdf](https://solana.com/solana-whitepaper.pdf) |

---

## Developer Activity

| Metric | Value |
|---|---|
| **GitHub Stars** | 11,071 |
| **GitHub Forks** | 3,516 |
| **Commits (4 weeks)** | 171 |
| **Pull Requests Merged** | 23,614 |
| **Contributors** | 411 |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $2.00B |
| **Market Cap Rank** | #7 |
| **24h Range** | $75.75 — $78.80 |
| **CoinGecko Sentiment** | 82% positive |
| **Last Updated** | 2026-07-16 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Trading Profile

### Venues & Liquidity

SOL is one of the most liquid altcoins and is tradable across the two venues this wiki focuses on:

| Venue | Product | Notes |
|---|---|---|
| **[[binance]]** | Spot (SOL/USDT) | Deepest CEX spot book for SOL; primary price discovery for the pair |
| **[[binance]]** | USDⓈ-M Perp (SOLUSDT) | Deep [[perpetual-futures\|perp]] liquidity; high leverage available; 8-hour [[funding-rate\|funding]] intervals |
| **[[hyperliquid]]** | SOL-PERP | Consistently a **top-5 market** on Hyperliquid by volume (~$215M/24h in the Apr 2026 snapshot); ~10-20x leverage tier; **1-hour** funding intervals |

The Binance-spot + Binance-perp + Hyperliquid-perp triangle makes SOL a clean candidate for cross-venue funding and basis work, and its depth lets directional traders size meaningfully without dominating the book.

### Applicable Strategies

- **[[crypto-beta-rotation]]** — SOL is the archetypal high-beta L1 (~1.5-2.5x BTC); a natural leg to lever up in risk-on regimes and de-beta / hedge when the macro correlation turns risk-off.
- **[[oi-confirmed-trend]]** — momentum/trend on the SOL perp, filtered by rising [[open-interest]] to separate conviction moves from mean-reverting retail chases (ideal for a high-beta name that trends hard in both directions).
- **[[cash-and-carry]]** — buy SOL spot, short the dated/perp future to harvest the [[basis-trade|basis]] when leveraged longs bid SOL futures into contango during meme/euphoria cycles.
- **[[hl-vs-cex-funding-divergence]]** — SOL-PERP trades on both Hyperliquid (1h funding) and Binance (8h funding); the differing funding cadences and retail bases open persistent cross-venue funding spreads to arbitrage.
- **[[crowded-long-funding-fade]]** — SOL [[funding-rate|funding]] blows out positive in euphoric runs; fading crowded longs collects the carry and positions for the mean-reversion / long-squeeze.
- **[[liquidation-cascade-fade]]** — SOL's outsized [[volatility]] produces sharp [[liquidation]] cascades that overshoot fair value; a fade/reversal setup provides liquidity into the flush.

### Volatility & Regime Character

- **High-beta L1** — daily moves of 10-20% are possible; empirically amplifies BTC/ETH moves ~1.5-2.5x, so SOL leads both legs of a broad move (it printed the strongest 24h/7d bounce of the six flagships even while sitting at the deepest drawdown, ~-76% from its Jan-2025 ATH).
- **BTC/ETH-correlated** — trades as crypto-beta; the SOL/ETH ratio is a monolithic-vs-modular relative-value expression rather than an idiosyncratic bet.
- **Narrative-driven** — ecosystem/meme cycles (pump.fun launches, Jupiter DEX volume), the SOL-ETF catalyst, and REV/fee demand drive regime shifts more than for the majors, making sentiment/regime gating especially valuable.

### Risk Flags

- **Network outage history** — multiple full outages in 2022; reliability has improved markedly (Firedancer client), but tail-risk of a halt remains a live consideration for leveraged perp positions.
- **Unlock / inflation overhang** — uncapped supply with disinflationary issuance; FDV ($44.96B) > market cap ($41.50B), so residual emission/unlock supply pressure persists.
- **Ecosystem concentration** — a large share of fees/activity ties to speculative meme cycles (pump.fun); collapsing meme volume can rapidly deflate usage metrics and sentiment.
- **Funding / liquidation risk** — extreme perp funding and crowded [[open-interest]] into meme cycles precede violent [[liquidation]] cascades on both Binance and Hyperliquid perps.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=SOL` — cross-exchange funding (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=SOL` — cross-exchange [[open-interest]]
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=SOLUSDT` — Binance top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=SOL` — all-in-one derivatives overview (markdown format available)
- `GET /api/v1/hyperliquid/summary?coin=SOL` — all-in-one Hyperliquid perp data
- `GET /api/v1/hyperliquid/l2-book?coin=SOL` — L2 order-book snapshot
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange [[liquidation|liquidations]]

**Historical / backtesting data:**
- `GET /api/v1/hyperliquid/candles?coin=SOL&interval=1h&limit=1000` — Hyperliquid OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=SOL&limit=100` — current + historical HL funding
- `GET /api/v1/derivatives/binance/funding-rates?symbol=SOLUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — OHLCV archive for forward-return labels
- `GET /api/v1/backtesting/funding` — funding archive

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=SOL"
```

Auth: `X-API-Key` header. Full endpoint catalogs: [[cryptodataapi-derivatives]], [[cryptodataapi-hyperliquid]].

---

## See Also

- [[crypto-markets]]

---
