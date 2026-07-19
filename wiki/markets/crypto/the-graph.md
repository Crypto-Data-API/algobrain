---
title: "The Graph"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [ai-trading, crypto, data-provider, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["GRT", "Graph Protocol"]
entity_type: protocol
founded: 2018
headquarters: "Decentralized (developed by Edge & Node, San Francisco)"
website: "https://thegraph.com/"
related: ["[[arbitrum]]", "[[chainlink]]", "[[crypto-markets]]", "[[ethereum]]", "[[narrative-trading]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]", "[[defai]]", "[[ai-trading-agents]]", "[[on-chain-inference]]", "[[nansen]]", "[[glassnode]]", "[[arkham-intelligence]]"]
---

# The Graph

**The Graph** (GRT) is the dominant decentralized indexing protocol for blockchain data — often called "the Google of Web3" — letting developers query on-chain data via GraphQL subgraphs instead of running their own indexing servers. For traders it matters as the longest-running pure-play **data-infrastructure token** and, since 2025, as a member of the AI-agent/data narrative basket: most major DeFi front-ends (Uniswap, Aave, etc.) depend on its query layer.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | GRT (ERC-20, native to [[ethereum]]; protocol contracts on [[arbitrum]]) |
| **Sector** | Data infrastructure / [[indexing]], [[depin\|DePIN]], AI-agent data tooling |
| **Market Cap Rank** | #171 |
| **Market Cap** | $209.26M |
| **Fully Diluted Valuation** | $209.27M |
| **Current Price** | $0.01937798 |
| **24h Volume** | $12.94M |
| **24h Change** | -0.03% |
| **7d Change** | -2.12% |
| **All-Time High** | $2.84 (2021-02-12) |
| **All-Time Low** | $0.01847949 (2026-06-10) |
| **Launched** | Mainnet December 2020 (project founded 2018, built by Edge & Node) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

GRT trades at ~$0.0194, essentially flat on the day and down ~2% on the week, hovering just above a **fresh all-time low** ($0.01848, printed 2026-06-10) and ~99% below the February 2021 ATH of $2.84. The backdrop is **extreme fear** ([[crypto-fear-and-greed-index|Fear & Greed Index]] ≈ 23) inside an **"Established Bear Market"** regime. The near-1.0 market-cap/FDV ratio (cap ≈ FDV) means GRT is fully diluted — there is no large locked-supply overhang, so price weakness reflects demand, not unlocks.

---

## Overview

The Graph is an indexing protocol and global API for organizing blockchain data and making it accessible with GraphQL. Developers publish **subgraphs** (open APIs); the network makes it possible to build serverless dApps that run entirely on public infrastructure.

GRT is the work token coordinating three roles: **Indexers** (node operators who stake GRT and earn query fees + indexing rewards), **Delegators** (who delegate GRT to indexers for a share of rewards), and **Curators** (who signal GRT on useful subgraphs). Protocol operations migrated to [[arbitrum]] in 2023 to cut gas costs.

### Key developments 2025–2026

- **Token API beta (March 2025)** — real-time token balances, transfers, and pricing across chains, positioning The Graph against centralized providers like Alchemy and Covalent.
- **GRC-20 / Geo knowledge graphs (Feb–Mar 2025)** — a proposed standard for composable decentralized knowledge graphs (first GRC-20 hackathon ran Feb 3 – Mar 9, 2025 with a 150,000 GRT bounty), aimed squarely at the AI-agent data market.
- **Substreams Foundational Stores (October 2025)** — pre-processed, fork-aware streaming blockchain data for high-performance analytics.
- **Horizon upgrade (December 2025)** — the largest protocol upgrade since launch, transforming The Graph from a subgraph-only indexer into a modular, multi-service data platform.
- **Chainlink CCIP integration (announced 2025-2026)** — cross-chain GRT transfers across Arbitrum, Base, and Solana, a prerequisite for cross-chain staking. (See [[chainlink]].)

Despite the protocol shipping aggressively, the token has badly lagged: GRT fell ~67% in the year to April 2026 and kept setting fresh all-time lows through 2026 (ATL $0.01848 on 2026-06-10) — a textbook example of the **fundamentals-price divergence** common in infrastructure tokens whose fee capture is small relative to FDV. With the float fully diluted (cap ≈ FDV), there is no unlock overhang to blame; the weakness is a demand and fee-capture story.

---

## Trading Relevance

- **Where it trades**: deep spot liquidity on Binance (GRT/USDT), Coinbase, Kraken (GRT/USD), Upbit (GRT/KRW), Bitget, KuCoin; perps on Binance and most major derivatives venues. DEX liquidity on Uniswap v3.
- **Narrative basket**: AI/data-infrastructure and DePIN baskets (see [[narrative-trading]]). GRT historically trades as a high-beta laggard within AI baskets — it rallies late and hard when the AI narrative rotates into "picks and shovels" plays.
- **Catalysts to watch**: Horizon adoption metrics (query fees, new data services), Token API revenue, CCIP-enabled Solana expansion, and any AI-agent platform standardizing on GRC-20.
- **Bear case / structure**: near-fully-diluted supply with ongoing ~3% issuance to indexers creates persistent sell pressure; query-fee burn remains small. Price at all-time lows means delisting/index-removal risk is non-trivial for a former top-50 asset.

---

## Peer Comparison — Decentralized Data / Indexing Infrastructure

| Project | Token | Niche | Notes |
|---|---|---|---|
| **The Graph** | GRT | Decentralized [[indexing]] / GraphQL subgraphs | Longest-running pure-play; "Google of Web3"; pivoting to AI-agent data (GRC-20, Token API) |
| [[chainlink\|Chainlink]] | LINK | Oracles + CCIP cross-chain | Adjacent data-infra leader; partners with The Graph on cross-chain GRT |
| Pyth Network | PYTH | Low-latency price oracles | Competes for the market-data layer, esp. on [[solana\|Solana]] |
| Covalent / Alchemy / Infura | (CXT / private) | Centralized & semi-decentralized RPC + data APIs | The Graph's commercial competition for the indexing/API market |

The Graph's structural edge is that it is **decentralized and protocol-owned** rather than a SaaS vendor, but its commercial rivals (Alchemy, Infura) offer turnkey APIs that many teams prefer — the central tension in the GRT thesis.

---

## Valuation Framing (qualitative)

- **Fully-diluted, low-multiple infra token:** cap ≈ FDV (~$209M) with no large unlock overhang, so GRT screens cheap on a price basis — but query-fee revenue captured by the token is small relative to that cap, the classic infra-token **fee-capture gap**.
- **Optionality on AI/data narrative:** GRT is a high-beta laggard in the AI-data and [[depin|DePIN]] baskets (see [[narrative-trading]]); if AI agents standardize on decentralized knowledge graphs (GRC-20) or the Token API monetizes, fee capture could re-rate the token.
- **Issuance drag:** ongoing ~3% indexer-reward issuance is a structural headwind unless query-fee burn scales to offset it.
- **Distinct from locked peers:** unlike [[spark-2|SPK]] or [[huma-finance|HUMA]] (heavy locked supply), GRT's weakness is pure demand/fundamentals, not dilution — a cleaner (if still bearish) setup.

---

## Snapshot Data (2026-04-09, CoinGecko — historical archive)

> The tables below are an **archived** April 2026 point-in-time capture, retained for reference only. For current figures see the **Market Data** block at the top of this page.

### Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 10.78B GRT |
| **Total Supply** | 10.80B GRT |
| **Max Supply** | 10.80B GRT |
| **Fully Diluted Valuation** | $257.25M |
| **Market Cap / FDV Ratio** | 1.00 |

### Price History

| Metric | Value (2026-04-09) |
|---|---|
| **All-Time High** | $2.84 (2021-02-12) |
| **All-Time Low** | $0.0232 (2026-03-29) — since broken; new ATL $0.01848 on 2026-06-10 |
| **1y Change** | -66.81% |
| **Market Cap** | $256.68M (rank #147) |
| **24h Volume** | $12.81M |

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xc944e90c64b2c07662a292be6244bdf05cda44a7` |
| Arbitrum One | `0x9623063377ad1b27544c965ccd7342f7ea7e88c7` |
| Polygon PoS | `0x5fe2b58c013d7601147dcdd68c143a77499f5531` |
| Avalanche | `0x8a0cac13c7da965a312f08ea4229c37869e85cb9` |
| Harmony Shard 0 | `0x002fa662f2e09de7c306d2bab0085ee9509488ff` |
| Near Protocol | `c944e90c64b2c07662a292be6244bdf05cda44a7.factory.bridge.near` |
| Energi | `0x771513ba693d457df3678c951c448701f2eaaad5` |
| Sora | `0x00d1fb79bbd1005a678fbf2de9256b3afe260e8eead49bb07bd3a566f9fe8355` |

### Social & Developer

| Platform | Link / Metric |
|---|---|
| **Twitter** | [@graphprotocol](https://twitter.com/graphprotocol) |
| **GitHub** | [graphprotocol/graph-node](https://github.com/graphprotocol/graph-node) — 3,123 stars, 123 contributors (Apr 2026) |
| **Docs** | [https://thegraph.com/docs/en/](https://thegraph.com/docs/en/) |

---

## Related

- [[crypto-markets]]
- [[ethereum]]
- [[arbitrum]]
- [[chainlink]]
- [[indexing]]
- [[depin]]
- [[narrative-trading]]
- [[ai-trading-overview]]
- [[crypto-fear-and-greed-index]]

---

## Sources

- CoinGecko, The Graph page snapshot 2026-04-09 (Source: [[coingecko-top-1000-2026-04-09]])
- CoinMarketCap — The Graph: https://coinmarketcap.com/currencies/the-graph/ (price ~$0.0202, cap ~$218.8M, rank #127, retrieved 2026-06-10)
- CoinGecko — The Graph: https://www.coingecko.com/en/coins/the-graph (cap ~$218.4M, rank #166, retrieved 2026-06-10)
- The Graph blog — GRC-20 Hackathon Recap: https://thegraph.com/blog/grc-20-hackathon-recap/
- Messari — State of The Graph Q1–Q3 2025: https://messari.io/report/state-of-the-graph-q2-2025
- BlockEden — "The Graph's Quiet Takeover: data layer for AI agents" (Feb 2026): https://blockeden.xyz/blog/2026/02/05/the-graph-depin-evolution-trillion-queries-ai-agents-indexing/
- Perplexity verification, 2026-06-10 (market cap ~$214M, CoinGecko rank ~#165-166)

## Trading Profile

### Venues & liquidity

GRT is tradable on [[binance]] as both **spot** (GRT/USDT) and a **USD-margined perpetual** ([[perpetual-futures]]) carrying [[funding-rate|funding]], [[open-interest]], and [[liquidations]] data. It is **NOT listed on Hyperliquid**, so Binance is the primary — and effectively the only deep — leveraged venue. With market-cap rank ~174 and modest 24h volume, order books thin out quickly beyond small clip sizes; leverage concentration on a single perp venue means funding, OI, and liquidation flows on Binance dominate price discovery. Practically, size positions to Binance depth, expect slippage on large market orders, and treat cross-venue basis/arb as constrained by the absence of a second major perp venue.

### Applicable strategies

- [[funding-rate-harvest]] — collect Binance perp funding on GRT when the single-venue perp sits in persistent positive-carry regimes, hedged against spot.
- [[crowded-long-funding-fade]] — fade over-leveraged longs when GRT funding spikes during AI/data-narrative pumps, a recurring pattern for a high-beta laggard.
- [[liquidation-cascade-fade]] — GRT's thin single-venue book makes it prone to sharp forced-liquidation wicks near all-time lows that mean-revert.
- [[narrative-trading]] — GRT is a late, high-beta mover in AI-agent and [[depin|DePIN]] baskets; trade rotation into "data infrastructure" plays.
- [[rsi-mean-reversion]] — persistent downtrend near ATL produces oversold-bounce setups suited to bounded mean-reversion entries.
- [[oi-confirmed-trend]] — use Binance open-interest confirmation to validate breakouts/breakdowns given how much of GRT's leverage sits on one venue.

### Volatility & regime character

Small/mid-cap altcoin with high beta to BTC/ETH risk sentiment and elevated reflexivity inside AI-data/DePIN narrative baskets. As an infrastructure/DeFi-adjacent token (indexing layer for major DeFi front-ends) it lacks memecoin-style froth but rallies late and hard when "picks and shovels" narratives rotate. Fully diluted supply (cap ≈ FDV) means moves reflect demand and fee-capture sentiment rather than unlock mechanics; character is a grinding-downtrend-with-sharp-relief-bounce profile.

### Risk flags

- **Venue concentration**: leveraged exposure is concentrated on Binance (no Hyperliquid, no second major perp venue), so liquidity and funding are single-venue dependent.
- **Thin liquidity / delisting risk**: rank ~174 with price at all-time lows raises index-removal/delisting risk for a former top-50 asset.
- **Emissions drag**: ongoing ~3% indexer-reward issuance is a structural sell-pressure headwind unless query-fee burn scales.
- **Narrative dependence**: upside is heavily contingent on the AI-agent/data-infrastructure narrative re-rating fee capture.

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=GRTUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=GRTUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=GRT` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=GRT` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=GRTUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=GRTUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=GRT"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
