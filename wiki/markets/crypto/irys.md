---
title: "Irys"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, data-provider]
aliases: ["IRYS"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://irys.xyz/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[bnb]]", "[[depin]]", "[[arweave]]", "[[filecoin]]"]
---

# Irys

**Irys** (ticker **IRYS**) is a Layer 1 "programmable datachain" that unifies on-chain data storage and smart-contract execution in a single network. Where traditional smart-contract chains handle transactions but lack native primitives for working with data at scale — and traditional storage chains lack execution — Irys aims to serve both, making stored data programmable through **IrysVM**, its native EVM execution layer. The IRYS token is the network's gas/fee and staking asset, with token deployments on [[ethereum]] and [[bnb]] (BNB Chain). Irys is the rebrand/evolution of **Bundlr Network**, which began as an [[arweave|Arweave]] data-upload scaling layer before pivoting to its own datachain.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | IRYS |
| **Price** | $0.01687909 |
| **Market Cap** | $33,749,270 |
| **Market Cap Rank** | #597 |
| **24h Volume** | $2,907,791 |
| **24h Change** | -1.03% |
| **7d Change** | -2.44% |
| **Circulating Supply** | 2.00B IRYS |
| **Total Supply** | 10.00B IRYS |
| **Max Supply** | Uncapped |
| **Fully Diluted Valuation** | ~$168.79M |
| **Market Cap / FDV** | ~0.20 |
| **All-Time High** | $0.084374 (2026-01-24) — now ~-80.0% |
| **All-Time Low** | $0.01652714 — now ~+2.1% |

> *Market data as of 2026-06-20 (cryptodataapi.com / CoinGecko).*

Context: IRYS is trading within ~2% of its all-time low and is essentially flat-to-down on the week, consistent with the broader backdrop of **extreme fear** ([[fear-and-greed-index|Fear & Greed]] = 21 on 2026-06-23) and a longer-horizon **Bottoming / Accumulation** regime.

---

## Architecture / how it works

Irys merges two layers that are usually separate — **storage** and **execution** — into one programmable datachain:

- **IrysVM (execution).** A native EVM execution layer means smart contracts can read, reference, and act on stored data directly, rather than treating storage as an off-chain blob the chain cannot see. This is the core differentiator versus "dumb" blob storage: data is **programmable**.
- **Storage layer.** Users choose **term storage** (temporary, duration-based pricing) or **permanent storage** (one-time payment for perpetual retention) — the permanent option is conceptually similar to [[arweave|Arweave]]'s pay-once-store-forever model, but coupled with on-chain execution.
- **Validators & data partitions.** Validators stake IRYS and **prove continuous maintenance of assigned data partitions**, which lets the network scale storage capacity horizontally as more validators join and demand grows. Proof-of-storage-style mechanics tie security to actually holding the data, not just to token weight.
- **Multi-revenue economics.** Network economics combine storage fees, execution fees, and programmable-data transaction fees, intended to keep pricing at-or-near cost while remaining sustainable.
- **Token reach.** IRYS token contracts live on [[ethereum]] and [[bnb]] (BNB Chain) for distribution and trading, while the datachain itself is the L1.

The thesis: AI, gaming, and consumer apps increasingly need cheap, verifiable, and *executable* data — not just storage — so a chain that natively unifies the two captures a workload neither pure-storage nor general-purpose L1s serve well.

---

## Tokenomics & Supply

- **Circulating:** ~2.0B IRYS against a total of 10.0B — only ~20% in circulation, so the market-cap-to-FDV ratio is a low ~0.20. This is a **large future-unlock overhang** and the primary structural risk.
- **No fixed max supply** recorded; storage and execution economics rely on a multi-revenue model (storage fees + execution fees + programmable-data transactions) intended to keep at-cost pricing sustainable.
- **Utility:** IRYS pays for all storage and execution fees and is used for validator staking; validators prove continuous maintenance of assigned data partitions, allowing horizontal scaling as demand grows.
- **Storage model:** users choose term storage (temporary, duration-based) or permanent storage (one-time payment for perpetual retention) — a design comparable to [[arweave]]'s pay-once-store-forever model but coupled with on-chain execution.

---

## Value accrual / governance

IRYS accrues value through **fee demand and staking**: every storage upload, execution call, and programmable-data transaction is paid in IRYS, and validators must stake the token (and provably maintain data) to earn. The more real storage and execution demand the datachain attracts, the more IRYS is consumed and locked. The counterweight is the low ~0.20 MC/FDV: with ~80% of total supply still to enter circulation, fee-driven demand has to outrun a steady stream of unlocks before token holders see durable value capture. Until usage scales, the unlock schedule is the dominant force on price.

---

## Comparison vs competitors

| Project | Token | Core thesis | Execution layer? | Notes |
|---|---|---|---|---|
| **Irys** | IRYS | Programmable datachain (storage + EVM) | **Yes — IrysVM** | ex-Bundlr; ~20% circulating; near ATL |
| **[[arweave]]** | AR | Permanent "pay once, store forever" storage | No (storage only; AO is separate) | Incumbent permaweb; Irys was once a Bundlr layer on it |
| **[[filecoin]]** | FIL | Decentralized storage marketplace | No (FVM added later, limited) | Largest DePIN storage network by capacity |
| **Walrus** | WAL | Blob storage on Sui | No (relies on Sui execution) | Newer high-throughput blob storage |

Irys's distinctive claim is the **unified storage + native execution** (IrysVM) — competitors are storage-first and bolt on (or rely on a separate) execution. The trade-off: Arweave and Filecoin are far larger, more battle-tested, and more liquid, so Irys must prove a durable cost or capability edge to win developer mindshare.

---

## How & Where It Trades

- **Spot (CEX):** Bitget (IRYS/USDT) and KuCoin (IRYS/USDT) are the primary listed venues.
- **On-chain:** token contracts live on [[ethereum]] and [[bnb]] (BNB Chain); the project also ran a Binance Wallet IDO for early distribution.
- **Derivatives / Hyperliquid:** no perpetual-futures market or funding/open-interest data is recorded for IRYS in this snapshot — treat it as a spot-only small-cap unless a venue is confirmed at trade time. **No perp.**
- **Liquidity profile:** ~$2.9M of 24h volume on a ~$33.7M cap (turnover ~8.6%) — adequate for small positions but susceptible to slippage on size. Combined with the large unlock overhang, this makes IRYS a **low-float / high-future-supply** profile where new unlocks meeting a thin book is a recurring downside catalyst.

---

## Use Case, Narrative & Category — catalysts

Irys targets the **decentralized data / [[depin]]-adjacent storage** narrative with a twist: programmable, on-chain data. By merging storage with an EVM execution layer (IrysVM), Irys positions itself between pure storage networks ([[arweave]], [[filecoin]]) and general-purpose L1s. Aggregator categories include Layer 1 (L1), Ethereum Ecosystem, BNB Chain Ecosystem, and Binance Wallet IDO.

**Potential catalysts:** mainnet/datachain usage milestones (real storage + execution demand); flagship AI or gaming apps building on IrysVM; a top-tier spot listing or perp launch to deepen liquidity; a broader DePIN/decentralized-storage narrative rotation. The chief headwind to any rally is the unlock schedule.

---

## History / timeline

- **Origin:** Irys is the evolution of **Bundlr Network**, which began as an Arweave data-upload scaling layer before pivoting to its own programmable datachain (exact rebrand date not in source data and not invented here).
- **2026-01-24:** all-time high of $0.084374.
- **2026-06-20:** trading at $0.01687909, roughly -80% from ATH and only ~2% above its all-time low — near cycle lows amid extreme-fear market conditions.

---

## Risks

- **Severe supply overhang:** ~80% of total supply is not yet circulating; scheduled unlocks are a major dilution risk and weigh on the low MC/FDV.
- **Near all-time lows:** price is ~2% off ATL; momentum and sentiment are negative, and the asset has high beta to a bear market.
- **Competition:** the data-storage / programmable-data space is crowded ([[arweave]], [[filecoin]], and newer datachains like Walrus); Irys must prove a durable cost or capability edge.
- **Liquidity:** limited venue coverage and modest volume increase execution risk; no perp to hedge.
- **Early stage / adoption:** the value of the network depends on real storage and execution demand materializing.
- **Macro / regime risk:** Extreme Fear ([[fear-and-greed-index|Fear & Greed]] = 21, 2026-06-23) in a bottoming regime; high-beta micro-cap.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

- **Unlock-aware sizing.** With only ~20% circulating, treat scheduled unlocks as recurring supply shocks — avoid sizing as if the float is stable.
- **Near-ATL context.** Price is ~2% above its all-time low; in a bottoming regime this can mark an accumulation zone, but "near ATL" is not itself a signal — require a demand catalyst and base-building before adding.
- **No hedge.** No perp recorded — manage downside with position size and stops, not derivatives.
- **Liquidity is workable but thin.** ~8.6% turnover allows small entries/exits; scale out into volume spikes rather than expecting depth.
- **Bear default:** watch-list / starter-size; the unlock overhang argues for patience and catalyst confirmation over early conviction sizing.

---

## See Also

- [[crypto-markets]]
- [[ethereum]]
- [[depin]]
- [[arweave]]
- [[filecoin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-20 (cryptodataapi.com / CoinGecko top-markets dataset).
- Macro framing: market snapshot 2026-06-23 (Fear & Greed 21, Extreme Fear; bottoming/accumulation regime).
- General market knowledge; no specific wiki source ingested yet.
