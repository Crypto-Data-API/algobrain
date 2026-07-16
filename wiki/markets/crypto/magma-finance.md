---
title: "Magma Finance"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [automated-market-maker, crypto, defi]
aliases: ["MAGMA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://magmafinance.io/"
related: ["[[automated-market-maker]]", "[[cetus-protocol]]", "[[crypto-markets]]", "[[decentralized-finance]]", "[[impermanent-loss]]", "[[liquidity]]", "[[sui]]", "[[uniswap]]"]
---

# Magma Finance

**Magma Finance** (MAGMA) is a decentralized finance (DeFi) protocol and **automated market maker (AMM)** / decentralized exchange built on the **[[sui|Sui]]** blockchain. It provides on-chain spot swaps and (concentrated) liquidity provision, and was featured via Binance Alpha Spotlight, giving it ecosystem visibility within Sui DeFi.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | MAGMA |
| **Market Cap Rank** | #322 |
| **Market Cap** | ~$77.2M |
| **Current Price** | $0.4070 |
| **24h Change** | -2.75% |
| **7d Change** | +20.01% |
| **Circulating Supply** | 190.0M MAGMA |
| **Total Supply** | 1.00B MAGMA |
| **Max Supply** | 1.00B MAGMA |
| **All-Time High** | $0.5683 (≈ -28.4% from current) |
| **All-Time Low** | $0.0698 (≈ +482.7% from current) |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

**Dilution flag:** Only 19% of the 1B max supply circulates (MC ≈ $77.2M vs. **FDV ≈ $407M**, MC/FDV ≈ 0.19). ~810M MAGMA remains uncirculated — emissions/unlocks are a significant overhang.

---

## Technology / What It Does

Magma Finance is a [[sui|Sui]]-native AMM/DEX:

- **AMM swaps** — constant-function / concentrated-liquidity market making for spot token swaps on Sui, using Sui's object-centric, parallel-execution Move-based architecture for low-latency, low-fee trading.
- **Liquidity provision** — users supply token pairs to earn trading fees and (typically) MAGMA incentive emissions; concentrated-liquidity designs let LPs target price ranges for higher capital efficiency.
- **Ecosystem role** — as a core DEX/AMM on Sui, Magma is part of the chain's base [[liquidity|liquidity]] layer that other Sui dApps route through.

Verify the exact AMM model (full-range vs. concentrated, ve-style emissions, etc.) against current project docs before relying on specifics.

### Architecture deep-dive

Magma is built on [[sui|Sui]], whose [[move-language|Move]]-based, object-centric model and parallel transaction execution are well suited to a high-throughput DEX. The architecture follows the modern **concentrated-liquidity AMM (CLMM)** pattern pioneered by [[uniswap|Uniswap V3]] and brought to Sui by protocols like Cetus:

- **Concentrated liquidity** — instead of spreading capital uniformly across the entire price curve (the [[uniswap|Uniswap V2]]/constant-product model), LPs allocate liquidity to specific price ranges ("ticks"). Capital sitting near the trading price earns disproportionately more fees, improving **capital efficiency** by orders of magnitude — at the cost of higher [[impermanent-loss|impermanent-loss]] sensitivity and active range management when price moves out of the chosen band.
- **Object-centric pools** — on Sui, each liquidity position is typically represented as an on-chain object (often an NFT-like position), enabling parallel, low-fee settlement and composability with other Sui dApps.
- **Routing & aggregation** — as a base DEX, Magma's pools serve as routable liquidity for Sui aggregators and dApps, so volume can arrive both directly and via third-party routers.
- **Incentive layer** — LPs earn swap fees plus MAGMA emissions; many Sui CLMMs layer a **ve(3,3)-style** vote-escrow model on top (lock the token, direct emissions to chosen pools, earn fees/bribes). Confirm whether Magma uses a ve-model against current docs before relying on it.

The practical takeaway: Magma competes on **capital efficiency and Sui-native liquidity depth**, and its LP economics hinge on the balance between swap-fee revenue and MAGMA emission dilution.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | 190.0M MAGMA |
| **Total Supply** | 1.00B MAGMA |
| **Max Supply** | 1.00B MAGMA |
| **FDV** | ~$407M |
| **MC / FDV** | ~0.19 |

A clean 1B max supply with 19% circulating. The token most likely funds liquidity-mining incentives, so emissions are intrinsic to the model — track the emission schedule, as it is the primary dilution lever and a driver of LP yield.

### Value accrual & governance

A DEX token's value rests on **fee capture and emission control**. In a ve(3,3)-style design (common for the category), MAGMA holders lock the token to (1) **direct emissions** to the pools they choose, (2) **earn a share of trading fees and bribes** from those pools, and (3) **govern** protocol parameters. This aligns long-term lockers with protocol revenue but makes the token reflexive: emissions attract liquidity → liquidity attracts volume → volume generates fees → fees support the token. The chain breaks if emissions outpace genuine fee revenue. With ~81% of supply uncirculated, the **emission schedule is the dominant valuation variable**: it both dilutes holders and bootstraps the liquidity that justifies the token. Verify the live fee-distribution and lock mechanics against current docs.

---

## Comparison vs Sui / DEX Peers

| DEX | Chain | Token | Model | Notes |
|---|---|---|---|---|
| **Magma Finance** | [[sui\|Sui]] | MAGMA | CLMM (concentrated liquidity) | Binance Alpha Spotlight; ~19% float |
| **[[cetus-protocol\|Cetus]]** | Sui (+ [[aptos\|Aptos]]) | CETUS | CLMM / leading Sui DEX | Largest Sui DEX by TVL/volume; suffered a major 2025 exploit |
| **[[uniswap\|Uniswap]]** | [[ethereum\|Ethereum]] + L2s | UNI | V3 CLMM / V4 hooks | Category-defining CLMM; deepest liquidity overall |
| **[[aerodrome\|Aerodrome]]** | [[base\|Base]] | AERO | ve(3,3) Slipstream CLMM | Dominant Base DEX; reference ve(3,3) economics |

Magma's challenge is that **Cetus is the entrenched Sui DEX leader**, so Magma must win liquidity and routing share on its home chain while the broader CLMM playbook is well-trodden elsewhere. Its differentiation is narrower than incumbents'; relative outperformance tends to come from Sui-specific catalysts and incentive campaigns rather than a durable structural moat.

---

## How / Where It Trades

- **Venues:** Trades on its own Sui AMM (native liquidity) and on centralized exchanges — CoinGecko lists a Bitget MAGMA/USDT market.
- **Liquidity — moderate-to-thin:** 24h volume ~$3.06M against ~$77.2M market cap (~4% turnover) — healthier than most peers in this batch, but still small-cap; size trades carefully.
- **Perps:** No major perpetual-futures listing evident in this snapshot; primarily spot.

---

## Narrative / Category

MAGMA rides the **Sui DeFi** and **DEX/AMM** narratives, amplified by **Binance Alpha Spotlight** exposure. In the 2026-06-21 snapshot its +20% 7-day move (well above its peer batch) made it a relative outperformer — typical of rotation into ecosystem-DEX tokens during Sui-specific catalysts. As of **2026-06-23** the broad tape sits in **Extreme Fear** (Fear & Greed = 21) with a long-horizon **Bottoming / Accumulation** read, so a single token's strength against that backdrop is notable but fragile. Note it still trades ~28% below its ATH.

**Catalysts:** Sui ecosystem TVL growth, new incentive/points campaigns, aggregator integrations that route volume through Magma's pools, a fee-switch/ve-lock activation, and broad DeFi-DEX rotation. **Headwinds:** Cetus's incumbency, emissions dilution, and the risk-off macro regime.

---

## History / Timeline

- **2026-04-09** — MAGMA appears in the CoinGecko top-1000 snapshot used to seed this page ([[sui|Sui]]-native AMM/DEX, rank ~#322).
- **2026-06-21** — Market snapshot: ~$77.2M cap, price $0.4070, **+20.01% over 7 days** (relative outperformer); ~$3.06M 24h volume.
- **2026-06-23** — Macro regime read: Extreme Fear (F&G 21), long-horizon Bottoming/Accumulation.

> Only dated events confirmed in ingested snapshots/sources are listed. Project milestones (launch, audits, listings) are not independently verified here.

---

## Risks

- **Dilution overhang** — ~81% of max supply uncirculated; incentive emissions can pressure price.
- **Ecosystem dependence** — value tracks Sui DeFi adoption and TVL; a Sui slowdown hits MAGMA directly.
- **DEX competition** — Sui hosts multiple AMMs/DEXes (e.g., Cetus and others); fee/liquidity share is contestable.
- **Small-cap volatility** — sharp moves in both directions; the +20% week can reverse quickly.
- **Smart-contract risk** — AMM/[[move-language|Move]] contracts require audits and have historically been exploit targets in Sui DeFi (notably the large 2025 [[cetus-protocol|Cetus]] exploit), underscoring real CLMM smart-contract risk on Sui.
- **Incumbent-competition risk** — [[cetus-protocol|Cetus]] is the entrenched Sui DEX leader; Magma must take liquidity/routing share rather than create it.

> *This page is informational, not investment advice. Small-cap DEX tokens with large uncirculated supply are highly volatile.*

---

## Trading Playbook (Bear / Extreme-Fear, Bottoming Regime)

Context: 2026-06-23 — **Extreme Fear** (F&G 21), long-horizon **Bottoming / Accumulation**.

- **Respect the dilution clock.** ~81% uncirculated supply means emissions/unlocks are the dominant medium-term pressure. A +20% week in Extreme Fear can be incentive-campaign-driven and reverse fast; do not chase strength without a durable catalyst.
- **LP vs. hold are different trades.** As an LP you earn fees + emissions but take [[impermanent-loss|IL]] and emission-dilution risk; as a holder you are long the reflexive emissions-vs-fees flywheel. Know which exposure you want.
- **Track real fees, not just price.** The healthy signal is **swap-fee revenue rising relative to emissions** — that is what converts a mercenary-liquidity DEX into a sustainable one. Falling volume with high emissions is the failure pattern.
- **Liquidity / no leverage:** ~$3M daily volume is healthier than peers but still small-cap; size carefully and avoid leverage on a token prone to sharp two-way moves.
- **Invalidation:** Sui TVL contraction, loss of routing share to Cetus, or volume collapsing while emissions continue.

---

## See Also

- [[crypto-markets]]
- [[sui]]
- [[decentralized-finance]]
- [[automated-market-maker]]
- [[liquidity]]
- [[cetus-protocol]]
- [[uniswap]]
- [[impermanent-loss]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Project site: magmafinance.io (project self-description).
- General market knowledge; no specific wiki source ingested yet.

