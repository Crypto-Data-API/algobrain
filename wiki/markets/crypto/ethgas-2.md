---
title: "ETHGas"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto, defi, derivatives, ethereum]
aliases: ["ETHGas", "GWEI"]
entity_type: protocol
headquarters: "Decentralized (ETHGas protocol)"
website: "https://www.ethgas.com/"
related: ["[[bnb]]", "[[crypto-markets]]", "[[derivatives]]", "[[ethereum]]", "[[mev]]"]
---

# ETHGas

**ETHGas** (ticker **GWEI**) is a blockspace-infrastructure protocol that turns Ethereum blockspace into tradable, composable units — enabling real-time block production (pre-confirmations) and a futures/forward market for **gas**. The goal is a crypto-native commodities market for blockspace, with GWEI as the ecosystem token. It is a [[derivatives|derivatives]] / DeFi infrastructure play built around [[ethereum|Ethereum]] block construction.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Metric | Value |
|---|---|
| **Ticker** | GWEI |
| **Price** | $0.1059 |
| **Market-cap rank** | #161 |
| **Market cap** | ~$222.5M |
| **Fully diluted valuation** | ~$1.06B |
| **24h volume** | ~$2.44M |
| **24h change** | -0.49% |
| **7d change** | -37.7% |
| **Circulating supply** | ~2.10B GWEI |
| **Total supply** | 10.0B GWEI |
| **Max supply** | 10.0B GWEI |
| **All-time high** | $0.2156 (2026-06-13), now -50.9% |
| **All-time low** | $0.01668 (2026-01-21), now +535% |

**Supply / valuation note:** This token carries a **large dilution overhang**. Circulating supply (~2.10B) is only ~21% of the 10.0B max; market cap (~$222.5M) is roughly one-fifth of FDV (~$1.06B), so an MC/FDV of ~0.21 means ~7.9B GWEI (~79% of supply) is still to unlock. The -37.7% 7d move and -50.9% from a very recent ATH (2026-06-13) underline how exposed the price is to unlock pressure and momentum reversal. The macro backdrop as of 2026-06-23 is **Extreme Fear** ([[fear-and-greed-index|Fear & Greed]] = 21) within a longer-horizon bottoming/accumulation regime.

---

## Architecture & mechanism (how it works)

ETHGas restructures **gas as a financial primitive** and blockspace as a tradable commodity:

- **Blockspace as a commodity.** The protocol decomposes Ethereum blockspace into tradable, composable units so block production can be sold/purchased ahead of time — separating the *right to include transactions* from the moment of block creation.
- **Pre-confirmations / real-time blocks.** By selling blockspace in advance, ETHGas enables sub-second **pre-confirmations** rather than waiting the ~12s Ethereum block interval — useful for latency-sensitive apps (DEX trading, intent settlement). It ships a **commit-boost / preconf module** for validators so they can opt into selling preconfs.
- **Gas futures & yield curve.** A futures/forward market for gas lets builders and users **hedge gas costs** and, in aggregate, forms a native Ethereum gas "yield curve" — a term structure of expected blockspace prices.
- **Open Gas Initiative.** Gas abstraction that shifts gas volatility/cost away from end users toward protocols, improving UX.
- **Validator/builder dependence.** The system only works if validators and builders participate in selling blockspace — it sits squarely in the [[mev]] / proposer-builder-separation (PBS) stack and depends on that supply side showing up.
- **Chains.** GWEI is issued on [[ethereum|Ethereum]] (`0x2798b1cc5a993085e8a9d46e80499f1b63f42204`) with a [[bnb|BNB Chain]] deployment as well.

See [[derivatives]] for the financial-primitive framing and [[mev]] for the block-construction context.

---

## Tokenomics & Supply

- **Max / total supply:** 10.0B GWEI (fixed).
- **Circulating:** ~2.10B (~21% of cap) — heavy future emissions/unlocks remain.
- MC/FDV ~0.21 signals the market is pricing only the circulating slice; future unlocks are the **dominant tokenomics risk**.
- Token is positioned as the ecosystem/utility asset for the blockspace marketplace.

---

## Value accrual / governance

GWEI is the **utility/ecosystem asset** for the blockspace marketplace — it is intended to coordinate and capture value from gas-futures trading, preconf sales, and the broader Open Gas economy, and to underpin governance of the protocol. The value question is whether marketplace activity (preconf demand, gas-hedging volume, validator participation) generates enough token demand to outweigh the ~79% of supply still to unlock. With a ~$1.06B FDV against only ~$222M market cap, the market is heavily discounting future unlocks; realized usage of the blockspace market is the swing factor for whether GWEI accrues durable value or bleeds against emissions.

---

## Comparison vs competitors

| Project | Token | Core thesis | Niche | Notes |
|---|---|---|---|---|
| **ETHGas** | GWEI | Blockspace commodity market + gas futures + preconfs | Gas/blockspace markets | High FDV, ~21% float; very recent ATH |
| **Espresso Systems** | (ESP) | Shared sequencing / preconfirmations across rollups | Sequencing/preconfs | Preconf + cross-rollup ordering |
| **Flashbots / MEV-Boost** | — | PBS infrastructure, MEV auctions | MEV / block building | Dominant block-building middleware (largely non-token) |
| **[[ethereum]]** (native) | ETH | Base fee market (EIP-1559) | Fee market | The incumbent gas-pricing mechanism ETHGas builds atop |

ETHGas's differentiation is making **gas itself a tradable, hedgeable asset class** with a forward curve, layered on top of preconfirmations — going further than pure sequencing/preconf players (Espresso) or non-tokenized PBS infrastructure (Flashbots). The flip side: it must win validator/builder adoption against an active, crowded research field, and Ethereum's own fee-market and PBS roadmap could reshape the opportunity.

---

## How & Where It Trades

- **Centralized:** Listed on Kraken (GWEI/USD), Bitget (GWEI/USDT) and KuCoin (GWEI/USDT) per the snapshot.
- **Decentralized:** Uniswap V3 on Ethereum (GWEI/USDT pool).
- **Derivatives:** no verified GWEI perpetual-futures market is recorded in this snapshot; treat as spot unless a perp venue is confirmed at trade time. **No perp recorded.**
- **Liquidity profile:** Moderate for the cohort — 24h volume ~$2.44M against ~$222M market cap. Spread across several CEXs plus Uniswap, but still small in absolute terms; large orders will move price. The **low float (~21%) plus large pending unlocks** means concentrated emissions into thin books is a recurring downside catalyst.

---

## Narrative / category & catalysts

GWEI sits in the **Ethereum infrastructure / blockspace markets / pre-confirmations** narrative — part of the broader push around proposer-builder separation, [[mev]], and making blockspace a tradable commodity. It overlaps with the "based / preconf" rollup discourse and with DeFi derivatives (a gas futures market). The thesis is ambitious: turn gas into an asset class with its own forward curve. Execution and validator adoption are the swing factors.

**Potential catalysts:** measurable validator/builder participation and preconf throughput; real gas-hedging volume on the futures market; integrations with rollups and latency-sensitive apps; favorable Ethereum-roadmap developments around preconfs/PBS. The chief headwinds are unlock pressure and the risk that a competing preconf/blockspace standard wins.

---

## History / timeline

- **2026-01-21:** all-time low of $0.01668.
- **2026-06-13:** all-time high of $0.2156 — a very recent peak.
- **2026-06-21:** $0.1059, down 37.7% on the week and ~-50.9% from the 2026-06-13 ATH, reflecting unlock pressure and momentum reversal.

---

## Risks

- **Dilution.** ~79% of supply still to unlock; emissions are a structural headwind (already -37.7% over 7 days). FDV (~$1.06B) dwarfs market cap (~$222M).
- **Adoption / technical risk.** The model depends on validator and builder participation in selling blockspace and on preconf demand actually materializing.
- **Competition.** Pre-confirmation and blockspace-market designs are an active, crowded research area (Espresso, Flashbots-adjacent efforts); competing standards could win.
- **Ethereum-roadmap risk.** Protocol-level changes to block construction, PBS, or fee markets could reshape or undercut the product.
- **Liquidity risk.** Volume is modest; concentrated unlocks into thin books are a downside catalyst; no perp to hedge.
- **Momentum risk.** Down ~51% from a very recent (2026-06-13) ATH — late-comers are underwater and overhead supply is heavy.
- **Macro backdrop.** As of 2026-06-23 crypto Fear & Greed reads 21 (Extreme Fear); high-FDV, low-float infrastructure tokens are among the most exposed to risk-off de-rating.

---

## Trading playbook (bear / Extreme-Fear, bottoming regime)

- **High-FDV / low-float caution.** A ~$1.06B FDV on a ~21% float is the textbook unlock-overhang setup — every unlock tranche is a potential supply shock. Size for that, not for the headline market cap.
- **Respect the recent ATH break.** Down ~51% from a 2026-06-13 high with -37.7% on the week signals momentum reversal; chasing into heavy overhead supply is dangerous. Prefer base-building confirmation.
- **No hedge.** No verified perp recorded — manage downside with position size and stops, not derivatives; check for a perp listing at trade time.
- **Catalyst-gated.** The bull trigger is real validator/preconf adoption and gas-futures volume. In a bottoming regime the narrative can rally, but require usage evidence plus turnover before adding.
- **Bear default:** watch-list / starter-size until unlock pressure abates and adoption metrics improve.

---

## Related

- [[ethereum]]
- [[derivatives]]
- [[mev]]
- [[bnb]]
- [[crypto-markets]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Project documentation: ETHGas (https://www.ethgas.com/).
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko top-1000).
- Macro framing: market snapshot 2026-06-23 (Fear & Greed 21, Extreme Fear; bottoming/accumulation regime).
- General market knowledge; no specific wiki source ingested yet.

## See Also

- [[crypto-markets]]
- [[ethereum]]

---
