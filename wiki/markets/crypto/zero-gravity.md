---
title: "0G (Zero Gravity)"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, machine-learning, hyperliquid, perpetual-futures, funding-rate, open-interest, derivatives, altcoins]
aliases: ["0G", "0G Labs", "0g-labs", "Zero Gravity"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.0gfoundation.ai/"
related: ["[[ai-agent-tokens]]", "[[artificial-intelligence]]", "[[bnb]]", "[[celestia]]", "[[crypto-markets]]", "[[decentralized-ai]]", "[[modular-blockchains]]", "[[ocean-protocol]]", "[[on-chain-inference]]", "[[tokenized-compute]]", "[[hyperliquid]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[hl-vs-cex-funding-divergence]]", "[[funding-rate-harvest]]"]
---

# 0G (Zero Gravity)

**0G** (ticker **0G**; also "0G Labs," "Zero Gravity") is a [[modular-blockchains|modular]] Layer 1 focused specifically on the data-availability and storage needs of **decentralized AI workloads** — training datasets, model weights, inference logs, and the large-object storage that current monolithic blockchains cannot economically support. It positions itself as "the first AI-focused modular blockchain" and sits at the intersection of the data layer of [[decentralized-ai|decentralized AI]] and the broader [[on-chain-inference|on-chain inference]] stack.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | 0G |
| **Current Price** | $0.266981 |
| **Market Cap** | $56.95M |
| **Market Cap Rank** | #412 |
| **Fully Diluted Valuation** | ~$267.0M (price × total supply) |
| **24h Volume** | $7.61M |
| **24h Change** | -0.46% |
| **7d Change** | -9.77% |
| **Circulating Supply** | ~213.2M 0G |
| **All-Time High** | $7.05 (2025-09-23) |
| **All-Time Low** | $0.264938 (2026-06-20) |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

0G trades roughly **96% below** its September 2025 all-time high of $7.05 and printed a fresh all-time low on 2026-06-20 — it is making new lows *today*. The 7-day change of -9.77% is among the weakest of this cohort, consistent with the extreme-fear backdrop ([[fear-and-greed-index|Crypto Fear & Greed Index]] of 23, established bear market). The market-cap/FDV ratio of **0.21** signals heavy locked supply still to come — turnover is high (~13% of cap daily) as the float churns near capitulation lows.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~213.2M 0G |
| **Total Supply** | 1.00B 0G |
| **Max Supply** | Uncapped (no fixed max) |
| **Market Cap / FDV** | 0.21 |

**Dilution overhang is large.** Only ~213M of a 1B total supply (~21%) circulates, leaving ~787M tokens (team, investors, ecosystem, foundation) to vest. The token also has **no fixed max supply**, so beyond scheduled unlocks there is ongoing inflationary issuance to fund storage/DA/compute incentives. The 0.21 mcap/FDV is one of the lowest in this group — a recent-launch profile where unlock-driven sell pressure can persist for years.

---

## Architecture

0G is a modular stack with three main components:

- **0G Storage** — a permissionless storage layer optimized for large files (model weights, datasets) rather than small frequent writes
- **0G DA (Data Availability)** — a data-availability layer intended to serve rollups and AI-specific compute chains, analogous to [[celestia|Celestia]] or EigenDA but with AI-workload optimizations
- **0G Compute** — a forthcoming compute layer for model training and inference coordinated by the same protocol

The bet is that AI workloads need a fundamentally different data substrate than DeFi workloads — terabyte datasets, gigabyte model checkpoints, high-throughput read patterns for inference — and that building this as a modular AI-native stack beats retrofitting it onto general-purpose blockchains.

---

## Technology / Where It Fits in the Modular & Decentralized-AI Stack

| Layer | 0G's Contribution | Competing Approaches |
|-------|---------------------|----------------------|
| Storage | 0G Storage (AI-optimized) | Filecoin, Arweave, Walrus |
| DA | 0G DA | [[celestia|Celestia]], EigenDA, Avail |
| Compute | 0G Compute (planned) | [[akash-network|Akash]], [[io-net|io.net]], [[gensyn]] |

The novelty is combining all three in a single [[modular-blockchains|modular]] stack targeted at AI. If decentralized AI matters, and if AI workloads need AI-specific infrastructure, 0G is a natural beneficiary. If AI workloads can run adequately on general-purpose modular chains, 0G is redundant. See [[tokenized-compute]] for the broader economic-model context.

---

## How & Where It Trades

**Centralized exchanges (spot):** 0G has strong tier-1 coverage — Binance (0G/USDT), Kraken (0G/USD), Upbit (0G/KRW), Bitget (0G/USDT), and KuCoin (0G/USDT). It launched via a Binance HODLer Airdrop and was a Binance Alpha Spotlight asset.

**Derivatives:** 0G has a perpetual futures market on [[hyperliquid|Hyperliquid]] (0G-PERP) in addition to major CEX perps, so directional, funding, and basis trades are available. Given the token is making fresh all-time lows, check live funding and open interest carefully before sizing — perp funding can swing hard around unlocks and capitulation.

---

## Use Case, Narrative & Category

0G is a **decentralized-AI infrastructure** narrative play, combining the [[modular-blockchains|modular-blockchain]] and "AI needs its own data layer" theses. CoinGecko categories include Artificial Intelligence (AI), Infrastructure, [[layer-1|Layer 1]], AI Framework, BNB Chain Ecosystem, and Ethereum Ecosystem. The bull case is AI workloads genuinely requiring blockchain-native, AI-optimized storage and [[data-availability|DA]]; the bear case is that the "infra for decentralized AI" category is crowded and real demand lags narrative valuations.

---

## Valuation Framing (qualitative)

- **MC/FDV 0.21 — the key risk number.** Only ~21% of supply circulates; the ~$57M cap masks a ~$267M FDV. As ~787M locked tokens vest, fully-diluted dilution can suppress price for years even if usage grows. This is the opposite of the [[tezos|Tezos]]/[[conflux-token|Conflux]] profile (those are ~fully diluted).
- **Pre-revenue infra bet** — 0G Storage/DA are live but real paid AI-workload demand is nascent; valuation is positioning-driven, not fee-driven.
- **High turnover at lows** — ~13% of cap traded in 24h while making fresh ATLs signals active price discovery / capitulation, not accumulation.
- **Optionality** — if decentralized-AI demand inflects and 0G captures AI-specific [[data-availability|DA]]/storage share, the low circulating cap gives high beta; but the uncapped supply and unlock schedule cap how much of that accrues to current holders.

---

## Peer Comparison (decentralized-AI / DA infrastructure, 2026-06-20)

| Asset | Price | Market Cap | Rank | MC/FDV | Niche |
|---|---|---|---|---|---|
| **0G (0G)** | $0.266981 | $56.95M | #412 | 0.21 | AI-native modular L1 (storage + DA + compute) |
| [[celestia\|Celestia (TIA)]] | — | (mid-cap) | — | low-mod | General-purpose [[data-availability\|DA]] layer |
| [[akash-network\|Akash (AKT)]] | — | (small/mid-cap) | — | high | Decentralized GPU/compute marketplace |
| [[render-network\|Render (RNDR)]] | — | (mid-cap) | — | high | Decentralized GPU rendering / compute |
| [[filecoin\|Filecoin (FIL)]] | — | (mid-cap) | — | mod | Decentralized storage |

> 0G is the smallest-cap and least-diluted-on-paper but highest-FDV-overhang name here: it spans storage + DA + compute, competing with all four peers at once — broad surface area, but no single moat yet.

---

## Honest Assessment

0G is early-stage and the thesis is as much about positioning as about current traction. The team and investors are credible, the modular architecture is well-designed on paper, and the AI-specific framing is a defensible wedge against general-purpose modular chains. But the category of "infrastructure for decentralized AI" is crowded, and the real demand for AI-specific blockchain infrastructure is far lower than narrative market caps imply. Treat 0G as a long-dated bet on AI workloads genuinely needing blockchain-native storage and DA — not as a near-term revenue story.

---

## Notable History

- **Token / mainnet era 2025**; 0G peaked at ~$7.05 on 2025-09-23 amid the AI-infrastructure narrative and its Binance listing/airdrop.
- Launched via a Binance HODLer Airdrop; featured as a Binance Alpha Spotlight project.
- Endured a ~96% drawdown into 2026, making a new all-time low on 2026-06-20 — actively in price discovery to the downside.

---

## Risks

- **Heavy unlock/dilution overhang** — only ~21% of supply circulates and there is no fixed max supply, so unlocks plus ongoing inflation create sustained sell pressure.
- **Crowded category** — competes across three fronts (storage vs Filecoin/Arweave/Walrus; DA vs Celestia/EigenDA/Avail; compute vs Akash/io.net/Gensyn).
- **Demand uncertainty** — real demand for AI-specific blockchain storage/DA is far below narrative-implied valuations.
- **Active downtrend** — making fresh all-time lows; no technical floor established yet.
- **Narrative dependence** — tightly coupled to the decentralized-AI cycle.
- **Macro/regime** — extreme-fear sentiment ([[fear-and-greed-index|F&G]] 23) and an established bear market amplify drawdowns in early-stage AI tokens.

---

## Trading Profile

**Venues & liquidity.** 0G trades on **both** [[hyperliquid|Hyperliquid]] (0G-PERP, up to ~40-50x leverage) and Binance (spot plus a USD-margined perpetual), giving it a genuine **two-venue derivatives market** on top of broad tier-1 spot coverage (Kraken, Upbit, Bitget, KuCoin). The dual-venue perp footprint means depth is deeper and funding is more contested than a single-venue alt: an on-chain Hyperliquid book and a CEX book quote the same risk, so mispricings compress quickly but also open recurring cross-venue funding/basis windows. Practically, this supports larger size and tighter execution than a rank ~518 token would otherwise allow — but the token is in active price discovery near all-time lows, so use limit orders, scale into size, and check live L2 depth and funding before committing; thin patches and gap risk still appear around unlocks and capitulation.

**Applicable strategies.**
- [[hl-vs-cex-funding-divergence]] — 0G runs on both a Hyperliquid perp and a Binance USD-margined perp, so the two funding streams diverge and can be captured directly.
- [[funding-rate-harvest]] — deep two-venue perp interest on a small-cap AI token produces sharp, harvestable funding swings, especially around unlocks and capitulation.
- [[cash-and-carry]] — Binance spot plus perps on both venues let you hold spot 0G against a short perp to farm basis/funding when it dislocates.
- [[liquidation-cascade-fade]] — a high-beta token near ATLs with up to ~50x leverage produces frequent long-liquidation flushes that overshoot and mean-revert.
- [[oi-price-exhaustion]] — rising open interest into a price grind toward fresh lows flags crowded positioning ripe for a squeeze either direction.
- [[narrative-trading]] — 0G is tightly bound to the decentralized-AI/modular-infra narrative; catalyst and sentiment shifts drive most of its directional moves.

**Volatility & regime character.** 0G is a **high-beta, early-stage AI-infrastructure / modular-L1 token** — small circulating cap (~21% of supply), uncapped issuance, and ~96% drawdown from its ATH make it far more volatile than large-cap crypto. It trades with high positive beta to BTC/ETH risk-on/risk-off regimes and amplifies moves in the broader AI/DeAI narrative basket ([[celestia]], compute/DA peers). In extreme-fear regimes it tends to underperform majors; in AI-narrative pumps it can outperform sharply given the low float.

**Risk flags.**
- **Unlock/dilution overhang** — only ~21% of supply circulates, no fixed max supply, and ongoing inflation; scheduled unlocks are a recurring downside catalyst and can whipsaw perp funding.
- **Narrative dependence** — price is tightly coupled to the decentralized-AI cycle; a narrative rotation removes the primary bid.
- **Price-discovery / no floor** — actively making fresh all-time lows with no established technical support; gap and cascade risk are elevated.
- **Perp funding dislocations** — dual-venue perps mean funding can swing hard and diverge across Hyperliquid vs CEX around unlocks and liquidations; monitor before sizing.
- **Liquidity fragility at the tails** — headline depth is solid across two venues, but a rank ~518 token can thin out fast in stress, so cross-venue arbs carry execution/slippage risk.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/summary?coin=0G` — all-in-one perp data (mark, funding, OI)
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=0G` — L2 order-book depth
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=0G&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=0G&limit=100` — funding history
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=0G"
```

Auth: `X-API-Key` header. Endpoint catalog: [[cryptodataapi-hyperliquid]]. See also [[cryptodataapi]].

---

## See Also

- [[decentralized-ai]] — Parent movement
- [[modular-blockchains]] — the architecture thesis
- [[celestia]] — competing/peer DA layer
- [[tokenized-compute]] — Adjacent economic-model layer
- [[on-chain-inference]] — Adjacent consumption layer
- [[ai-agent-tokens]] — Broader AI token landscape
- [[artificial-intelligence]] — AI section hub
- [[hyperliquid]] — venue for 0G perpetual futures
- [[crypto-markets]]
- [[bnb]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 — cryptodataapi.com / CoinGecko markets feed (`raw/data/crypto-loop/coingecko-markets.json`)

