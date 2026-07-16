---
title: "Oasis"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, perpetual-futures, funding-rate, open-interest, liquidations, derivatives, defi, altcoins]
aliases: ["Oasis Network", "ROSE"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://oasisprotocol.org/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[mina-protocol]]", "[[privacy-coins]]", "[[proof-of-stake]]", "[[zero-knowledge-proofs]]", "[[binance]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[funding-rate-harvest]]", "[[liquidation-cascade-fade]]"]
---

# Oasis

**Oasis** (ticker **ROSE**, formerly "Oasis Network") is a [[proof-of-stake]] [[layer-1]] purpose-built for **confidential computing** — privacy-preserving smart contracts at scale, placing it in the [[privacy-coins|privacy-blockchain]] category. Its flagship runtime, **Sapphire**, is marketed as the first confidential EVM, where contract state and inputs can be kept encrypted even from validators via trusted-execution-environment (TEE)–backed compute. Oasis separates **consensus** (a settlement layer secured by [[proof-of-stake]]) from **ParaTimes** (parallel runtime environments for computation), and offers cross-chain privacy tooling (the Oasis Privacy Layer) so EVM dApps on other chains can tap confidential execution.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | ROSE |
| **Market Cap Rank** | #439 |
| **Market Cap** | $51.96M |
| **Current Price** | $0.0066718 |
| **24h Change** | +2.46% |
| **7d Change** | +4.12% |
| **24h Volume** | $2.60M |
| **Circulating Supply** | ~7.79B ROSE |
| **Fully Diluted Valuation** | ~$66.72M |
| **All-Time High** | $0.597 (2022-01-15) — now -98.9% |
| **All-Time Low** | $0.00600 (2026-06-10) — now +11.2% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. ROSE trades roughly 11% above its all-time low (~$0.0060, set just days earlier on 2026-06-10) and about 99% below its January-2022 all-time high of $0.597. Its +4.12% 7-day and +2.46% 24h moves are among the few positive prints in this peer group, though on light ~$2.6M volume.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~7.79B ROSE |
| **Total Supply** | 10.00B ROSE |
| **Max Supply** | 10.00B ROSE |
| **Fully Diluted Valuation (FDV)** | ~$66.72M |
| **Market Cap / FDV** | ~0.78 |

ROSE is the network's gas, staking, and governance token, with a hard cap of 10B. Circulating supply is ~78% of max, so remaining dilution from staking rewards and unlocked allocations is moderate but not negligible — at full dilution the market cap would rise ~28% from current levels purely from supply growth, a mild structural headwind versus fully-circulating peers like [[dusk-network|DUSK]]. Validators and delegators **stake ROSE** on the consensus layer to secure the chain and earn staking rewards; rewards are funded from a fixed reward schedule rather than open-ended inflation, given the capped supply.

---

## How & Where It Trades

**Spot venues.** ROSE is listed on [[binance]] (ROSE/USDT), Bitget, and KuCoin, among others. The asset carries a BNB Smart Chain contract (`0xf006...bd4a`) and is tagged in the [[bnb]] Chain ecosystem.

**Derivatives.** ROSE perpetuals are available on major centralized derivatives venues. The wiki's prior snapshot did **not** record a ROSE perp on [[hyperliquid]], so do not assume one exists — verify the live venue list before trading derivatives. With a ~$51M market cap and only ~$2.3M daily volume (the thinnest in this peer group), liquidity is shallow and slippage/funding swings can be severe.

---

## Technology & Consensus

Oasis uses a **two-layer architecture**:

- **Consensus layer** — a [[proof-of-stake]] (Tendermint/Cosmos-SDK–based) settlement layer that orders blocks and secures the network.
- **ParaTime layer** — parallel runtimes that execute computation off the consensus critical path. The key runtimes are **Sapphire** (confidential EVM) and **Emerald** (standard EVM), with **Cipher** for confidential WASM contracts.

Confidentiality is delivered through **trusted execution environments (TEEs)**: contract execution happens inside hardware enclaves so that even node operators cannot see the plaintext state or inputs. This TEE-based model contrasts with [[zero-knowledge-proofs|zk]]-based privacy chains — it is faster and EVM-compatible but introduces a hardware-trust assumption. The Oasis Privacy Layer extends this confidentiality cross-chain to EVM dApps elsewhere, and Runtime Offchain Logic (ROFL) brings verifiable off-chain compute on-chain.

---

## Use Case, Narrative & Category

Oasis sits in the **privacy / confidential-computing L1** category ([[privacy-coins]]) alongside Secret Network, [[mina-protocol]] (zk-privacy), and others. Its narrative leans on confidential DeFi, on-chain data privacy, and — increasingly — **confidential AI / verifiable compute** (running models or agents over private user data). Tagged categories include Smart Contract Platform, Layer 1 (L1), Proof of Stake (PoS), Privacy Blockchain, Privacy Infrastructure, BNB Chain Ecosystem, Coinbase 50 Index, plus VC-portfolio tags (a16z, Pantera, Polychain, Blockchain Capital, Binance Labs/YZi).

---

## Valuation Framing (qualitative)

- **MC/FDV ~0.78:** ~22% of supply is still to enter circulation, a moderate but real dilution overhang. At today's price, fully diluted value is ~$67M versus a ~$52M live cap.
- **Near the floor:** ROSE printed its all-time low ($0.0060) on 2026-06-10, only ~11% below the current price. A name trading this close to its cycle low with a multi-year operating history and tier-1 VC backing (a16z, Pantera, Polychain) is the kind of "deep value, deep skepticism" setup that re-rates only on a clear adoption catalyst.
- **No earnings anchor:** like all infra L1s, ROSE has no cash-flow valuation; the bull case rests on confidential-compute / confidential-AI demand actually arriving. The bear case is that TEE-based privacy demand never materializes at scale, leaving a well-funded chain with thin usage.
- **Catalyst dependence:** a credible "confidential AI" flagship application (private inference over sensitive data) is the most plausible re-rating trigger; absent that, ROSE trades as bear-market beta on a privacy narrative.

---

## Peer Comparison

ROSE against other privacy and small/mid-cap infrastructure L1s in this cohort (data as of 2026-06-21):

| Token | Ticker | Price | Market Cap | Rank | 7d % | MC/FDV | Privacy tech |
|---|---|---|---|---|---|---|---|
| **Oasis** | ROSE | $0.0066718 | $52.0M | #439 | +4.12% | 0.78 | TEE / confidential EVM |
| [[dusk-network]] | DUSK | $0.085452 | $50.4M | #449 | -5.68% | 1.00 | ZK compliance / confidential SC |
| [[nervos-network]] | CKB | $0.00104816 | $51.3M | #443 | -8.58% | 0.98 | PoW (privacy not core) |
| [[theta-token\|Theta]] | THETA | $0.15476 | $154.8M | #206 | -3.34% | 1.00 | n/a (DePIN/compute) |
| [[mina-protocol]] | MINA | — | — | — | — | — | ZK / succinct blockchain |

Among the sub-$60M privacy/infra names, ROSE is one of only two with a *positive* 7-day return in an extreme-fear tape, distinguishing its TEE-based confidential-compute approach from [[dusk-network|DUSK's]] ZK-compliance angle and [[zero-knowledge-proofs|zk]]-based [[mina-protocol]].

---

## Notable History

- The Oasis Network mainnet launched in 2020, backed by a16z, Binance Labs, Polychain, and others.
- ROSE printed its all-time high of **$0.597 on 2022-01-15** during the prior bull cycle.
- It has since fallen ~99%, reaching a fresh all-time low of **$0.00600 on 2026-06-10**.
- As of 2026-06-21 it trades at ~$0.0067, about 11% off the low, with a rare positive 7-day return (+4.12%) in an otherwise weak peer group.

---

## Risks

- **TEE / hardware-trust assumption.** Confidentiality relies on the integrity of hardware enclaves; side-channel or microarchitectural attacks against TEEs are an ongoing research concern and represent a distinct risk versus pure-cryptographic (zk) privacy.
- **Adoption gap.** Confidential-computing demand on-chain has been slow to materialize; the value case depends on usage that remains limited.
- **Privacy / regulatory scrutiny.** Privacy-focused chains face heightened regulatory attention.
- **Competition.** Crowded privacy-and-AI narrative with both zk-based and TEE-based rivals.
- **Liquidity / sentiment.** Low volume (~$2.6M/day), down ~99% from ATH, sitting only ~11% above a fresh all-time low under an extreme-fear macro regime.

---

## Trading Profile

**Venues & liquidity.** ROSE is tradable on [[binance]] — both spot (ROSE/USDT) and a USD-margined [[perpetual-futures|perpetual]] contract carrying [[funding-rate|funding]], [[open-interest]], and [[liquidations|liquidation]] data. It is **not** listed on [[hyperliquid]], so Binance is the primary leveraged venue and effectively the single source of truth for ROSE derivatives flow. This concentration matters: with a sub-$60M cap and only ~$1.6–2.6M daily spot volume, the perp orderbook is thin, funding can swing sharply, and any leveraged size must be scaled to a shallow book. Position sizing should assume meaningful slippage on entries/exits and avoid market orders of size; venue concentration also means a single exchange's funding print and liquidation map drive most of the tradable signal.

**Applicable strategies.**
- [[funding-rate-harvest]] — a low-cap privacy L1 with a single leveraged venue tends to produce persistent funding skews that can be harvested delta-neutral (long spot / short perp).
- [[crowded-long-funding-fade]] — narrative-driven pops (confidential-AI headlines) on a thin ROSE perp often over-extend into positive funding, setting up a fade.
- [[liquidation-cascade-fade]] — shallow Binance ROSE liquidity makes stop-runs and liquidation flushes sharp and mean-reverting, a classic fade near cycle lows.
- [[breakout-and-retest]] — with ROSE pinned just above a fresh all-time low, a confirmed break of that range and retest offers a defined-risk directional entry.
- [[volatility-breakout]] — low-volume compression on a beaten-down name can resolve in violent expansion, suiting ATR/range-expansion triggers.
- [[oi-confirmed-trend]] — using Binance [[open-interest]] to confirm whether a ROSE move is fresh positioning or a squeeze filters false breakouts on this illiquid perp.

**Volatility & regime character.** ROSE is a small-cap (rank ~469) privacy / confidential-computing infrastructure L1 — high-beta to BTC/ETH risk appetite and to the broader privacy-and-AI narrative rather than to fundamentals. Trading ~99% below its 2022 ATH and near its all-time low, it behaves as deep-bear-market beta: quiet, low-volume drift punctuated by narrative-driven spikes. Not a memecoin, but reflexivity is elevated by thin liquidity, so realized volatility clusters and gaps are common. Correlation to majors is high on down moves; upside decoupling requires a coin-specific catalyst.

**Risk flags.**
- **Venue concentration.** Binance is effectively the only meaningful leveraged venue; a listing/rules change or delisting there would sharply impair tradability.
- **Thin liquidity.** ~$1.6–2.6M daily volume is among the thinnest in its peer group — slippage, funding whipsaws, and liquidation cascades are amplified.
- **Emissions / dilution.** MC/FDV ~0.78–0.79 leaves ~21–22% of supply still to enter circulation from staking rewards and unlocks — a structural supply headwind.
- **Narrative dependence.** Price hinges on the confidential-compute / confidential-AI thesis actually delivering; absent a catalyst it drifts as bear-market beta.
- **Regulatory.** As a privacy-focused chain, ROSE faces heightened regulatory scrutiny that can trigger venue or jurisdictional restrictions.

---

## Getting the Data (CryptoDataAPI)

Verified [[cryptodataapi|CryptoDataAPI]] endpoints for Binance spot + USD-M perp (auth via `X-API-Key`).

**Live data:**
- `GET /api/v1/market-data/ticker/price?symbol=ROSEUSDT` — current Binance spot price
- `GET /api/v1/market-data/ticker/24hr?symbol=ROSEUSDT` — 24h ticker stats
- `GET /api/v1/derivatives/summary?coin=ROSE` — Binance funding/OI snapshot
- `GET /api/v1/derivatives/funding-rates?coin=ROSE` — cross-exchange funding

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=ROSEUSDT&interval=1d&limit=200` — Binance spot OHLCV
- `GET /api/v1/derivatives/binance/funding-rates?symbol=ROSEUSDT` — Binance perp funding history
- `GET /api/v1/backtesting/klines` — deep kline archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/summary?coin=ROSE"
```

Auth: `X-API-Key` header. Catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

---

## See Also

- [[crypto-markets]]
- [[bnb]]
- [[layer-1]]
- [[proof-of-stake]]
- [[privacy-coins]]
- [[zero-knowledge-proofs]]
- [[mina-protocol]]
- [[dusk-network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.
- General market knowledge; no specific wiki source ingested yet.

