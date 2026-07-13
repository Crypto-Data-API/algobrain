---
title: "Janction"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, ai-trading, machine-learning]
aliases: ["JCT"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.janction.ai/home"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[bnb]]", "[[depin]]", "[[ai-crypto]]", "[[jasmycoin]]", "[[render-network]]", "[[akash-network]]"]
---

# Janction

**Janction** (JCT) is a **[[depin|DePIN (Decentralized Physical Infrastructure Network)]]** project focused on decentralized compute for AI. It runs a resource-sharing marketplace where participants rent and lease GPU/compute power, storage, and related resources to serve AI products and workloads. JCT is a multi-chain token deployed on [[ethereum|Ethereum]] and [[bnb|BNB Chain]], is associated with the **[[jasmycoin|JasmyCoin (JASMY)]] / Jasmy "Data Democracy"** ecosystem, and was featured via Binance Alpha Spotlight.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | JCT |
| **Market Cap Rank** | #405 |
| **Market Cap** | ~$58.9M |
| **Current Price** | $0.005128 |
| **24h Change** | -6.31% |
| **7d Change** | -26.31% |
| **Circulating Supply** | ~11.49B JCT |
| **Total Supply** | 50.00B JCT |
| **Max Supply** | 50.00B JCT |
| **All-Time High** | $0.01058 (≈ -51.5% from current) |
| **All-Time Low** | $0.001059 (≈ +384.0% from current) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Dilution flag:** Only 23% of the 50B max supply circulates (MC ≈ $58.9M vs. **FDV ≈ $256M**, MC/FDV ≈ 0.23). ~38.5B JCT remains uncirculated — a heavy emissions/unlock overhang typical of DePIN compute-reward models.

---

## Technology / What It Does

Janction is an AI-compute DePIN:

- **Compute marketplace** — a decentralized two-sided market matching providers of GPU/compute, storage, and image resources with AI developers who need them, intended to undercut centralized cloud pricing.
- **AI-product serving** — positioned to host/serve inference and other AI workloads on the open web.
- **Token incentives** — JCT is used to reward resource providers and pay for usage, the standard DePIN flywheel of bootstrapping supply with token emissions before organic demand.

The project spans Ethereum and BNB Chain. As with most DePIN-compute tokens, the key open question is the ratio of real paid usage to subsidized/incentivized activity — verify utilization metrics before treating revenue claims as proven.

### Architecture deep-dive

Janction is positioned as an **AI-compute Layer-2 / DePIN network** that aggregates idle GPU and compute resources into a permissionless marketplace. The general design pattern (verify specifics against current project docs) has these components:

- **Provider (supply) side** — operators run a node client that contributes GPU/CPU, storage, and bandwidth. The network verifies contributed work and pays providers in JCT, the standard DePIN mechanism for bootstrapping physical supply with token emissions before organic demand arrives.
- **Consumer (demand) side** — AI developers submit inference/training/serving workloads and pay in JCT (or a stable unit) for metered compute, with the network acting as an orchestration and settlement layer between distributed providers and the workload.
- **Verification & settlement** — decentralized compute networks must prove that off-chain work was actually performed (proof-of-compute / proof-of-sampling style attestation) so that providers cannot claim rewards for work they did not do; this verification layer is the hard technical problem of the category.
- **Ecosystem ties** — Janction is associated with the **[[jasmycoin|Jasmy]]** ecosystem (the "Data Democracy" / IoT-data project), positioning it as the compute layer alongside Jasmy's data-sovereignty narrative. Multi-chain deployment ([[ethereum|Ethereum]] + [[bnb|BNB Chain]]) widens listing and liquidity reach.

The defining strategic question for any AI-DePIN is **demand quality**: networks are easy to bootstrap on the supply side with emissions but hard to fill with *paying* AI workloads that compete with hyperscaler cloud on reliability, latency, and SLAs. Treat advertised "compute capacity" as a supply metric, not a revenue metric.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~11.49B JCT |
| **Total Supply** | 50.00B JCT |
| **Max Supply** | 50.00B JCT |
| **FDV** | ~$256M |
| **MC / FDV** | ~0.23 |

A large 50B max supply (hence the sub-cent price) with ~23% circulating. DePIN designs typically emit tokens continuously to subsidize compute providers, so ongoing inflation is structural — the emission curve is the dominant tokenomics variable.

### Value accrual & governance

JCT's value case is the classic DePIN flywheel: token utility (paying for compute, rewarding providers) and, if implemented, fee capture or burn from real usage. The token may also carry governance over network parameters and the provider-reward schedule. The critical caveat is that **emissions are front-loaded** — with ~77% of supply still to be released largely to subsidize providers, JCT must convert subsidized supply growth into genuine paid demand fast enough to absorb the new tokens, or price decays structurally. Until paid-usage metrics are demonstrated, JCT's value is primarily reflexive (incentive-driven) rather than cash-flow-backed.

---

## Comparison vs AI-Compute / DePIN Peers

| Project | Focus | Token | Niche | Notes |
|---|---|---|---|---|
| **Janction** | Decentralized GPU/compute for AI | JCT | AI-DePIN L2, Jasmy ecosystem | ~23% float; Binance Alpha Spotlight |
| **[[render-network\|Render]]** | Decentralized GPU rendering / AI compute | RENDER | GPU rendering pioneer, now AI inference | Largest/most established GPU-DePIN |
| **[[akash-network\|Akash]]** | Decentralized cloud (GPU + general compute) | AKT | "Supercloud" spot market for compute | [[cosmos]]-based; live GPU marketplace |
| **[[ionet\|io.net]]** | Aggregated GPU clusters for ML | IO | DePIN GPU aggregation on [[solana\|Solana]] | Large advertised GPU supply |

Janction is a **late, smaller entrant** in a category already led by Render, Akash, and io.net — all of which have more mature marketplaces, larger supply networks, and stronger brand recognition. Its potential edge is the [[jasmycoin|Jasmy]] ecosystem association and a focused AI-serving pitch, but it competes for the same scarce paying-demand pool as much larger rivals.

---

## How / Where It Trades

- **Venues:** Trades on centralized exchanges — CoinGecko lists Bitget JCT/USDT and KuCoin JCT/USDT markets.
- **Liquidity — moderate-to-thin:** 24h volume ~$2.96M against ~$58.9M market cap (~5% turnover) — reasonable for the rank but still small-cap.
- **Perps:** No major perpetual-futures listing evident in this snapshot; primarily spot on CEXes.

---

## Narrative / Category

JCT sits squarely in the **AI + DePIN** narrative — decentralized GPU/compute for AI, one of the cycle's most-hyped themes — with **Binance Alpha Spotlight** exposure and a tie to the [[jasmycoin|Jasmy]] ecosystem. In the 2026-06-21 snapshot momentum had rolled over hard: **-26% over 7 days** and -6% on the day, the weakest 7-day performance in its peer batch, consistent with a risk-off backdrop and a cooling AI-token rotation. As of **2026-06-23**, the broader tape remains in **Extreme Fear** (Fear & Greed = 21) with a long-horizon **Bottoming / Accumulation** read — a regime in which high-beta, heavily diluted AI-DePIN micro-caps are typically among the last to recover. It trades roughly halfway between its ATH and ATL.

**Catalysts to watch:** demonstrable paid-usage / utilization metrics (the category's missing proof), new GPU-provider growth, AI-DePIN theme rotation, additional exchange listings, and any concrete Jasmy-ecosystem integration. **Headwinds:** emissions overhang, dominance of larger DePIN rivals, and the risk-off regime.

---

## History / Timeline

- **2026-04-09** — JCT appears in the CoinGecko top-1000 snapshot used to seed this page (rank ~#405, multi-chain [[ethereum|Ethereum]]/[[bnb|BNB]] deployment).
- **2026-06-21** — Market snapshot: ~$58.9M cap, price $0.005128, down -26.31% over 7 days amid broad risk-off conditions.
- **2026-06-23** — Macro regime read: Extreme Fear (F&G 21), long-horizon Bottoming/Accumulation.

> Only dated events confirmed in ingested snapshots/sources are listed. Project-history milestones (mainnet, listings, partnerships) are not independently verified here and should be confirmed against official sources before use.

---

## Risks

- **Sharp negative momentum** — -26% in a week signals active distribution / narrative cooling.
- **Heavy dilution** — ~77% of max supply uncirculated; DePIN emissions add persistent sell pressure.
- **Demand-vs-subsidy risk** — DePIN compute networks often have far more incentivized supply than paying demand; sustainability is unproven.
- **Intense competition** — the decentralized-compute space is crowded (multiple AI-DePIN tokens compete for the same workloads).
- **Small-cap / liquidity risk** — rank #405 with modest volume; vulnerable in risk-off regimes.
- **Established-rival risk** — Render, Akash, and io.net hold larger, more mature compute marketplaces and brand; Janction must take share from incumbents.

> *This page is informational, not investment advice. Heavily diluted small-cap AI/DePIN tokens are highly volatile and can lose most of their value rapidly.*

---

## Trading Playbook (Bear / Extreme-Fear, Bottoming Regime)

Context: 2026-06-23 — **Extreme Fear** (F&G 21), long-horizon **Bottoming / Accumulation**.

- **Dilution-aware sizing.** With ~77% of supply uncirculated and continuous provider emissions, the *structural* sell pressure means JCT needs accelerating real demand just to hold price. In a bottoming regime, this makes it a low-conviction hold absent a usage catalyst — momentum/distribution (-26% week) confirms the downtrend was still active at the last snapshot.
- **Wait for the turn, not the dip.** High-beta AI-DePIN micro-caps tend to bottom *after* BTC/majors and rally late; do not anchor to "halfway between ATH and ATL" as fair value. Prefer evidence of trend reversal (stabilizing price, rising volume, real utilization data) over catching the falling knife.
- **Liquidity / no leverage:** spot CEX liquidity (Bitget, KuCoin) is modest; size for the thin book and avoid leverage on a token in active distribution.
- **Edge is demand-proof.** The single most valuable signal is verified *paying* compute usage vs. subsidized supply. Until that exists, treat JCT as pure theme-rotation beta.
- **Invalidation:** continued lower-lows on rising volume, or evidence that activity is overwhelmingly emissions-subsidized, argue against any allocation.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[bnb]]
- [[depin]]
- [[ai-crypto]]
- [[jasmycoin]]
- [[render-network]]
- [[akash-network]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Project site & docs: janction.ai, docs.janction.io (project self-description).
- General market knowledge; no specific wiki source ingested yet.
