---
title: "Carry Trade / Basis Regime"
type: concept
created: 2026-06-03
updated: 2026-06-11
status: good
tags: [crypto, derivatives, market-regime, market-microstructure, arbitrage, leverage]
aliases: ["Basis Regime", "Carry Trade Regime", "Futures Basis Regime", "Basis Health"]
domain: [market-microstructure, derivatives]
difficulty: advanced
related: ["[[crypto-market-regime-taxonomy]]", "[[derivatives-native-regime]]", "[[liquidity-depth-regime]]", "[[basis]]", "[[basis-trading]]", "[[funding-rate-arbitrage]]", "[[funding-rate]]", "[[2025-10-crypto-liquidation-cascade]]", "[[hyperliquid]]"]
---

The **Carry Trade / Basis regime** is basket #8 of the 14-basket crypto regime taxonomy (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). Its central claim is that the futures [[basis]] — the spread between perpetual or dated-futures price and spot — is not merely a funding signal but a *regime in its own right, and specifically a fragility gauge*. The mechanics of how basis arises and how it is harvested are covered elsewhere: see [[basis]] and [[basis-trading]] for the cash-and-carry spread, and [[funding-rate-arbitrage]] for the delta-neutral perp/spot trade. This page does something different — it reads **basis health as a state of the system**. The framework's key observation is that *basis collapse historically precedes the clearest cascade warnings*: a persistently positive [[funding-rate]] paired with record open interest is fragility forming, and the basis is the dial that shows it building and breaking. See [[crypto-market-regime-taxonomy]] for the full basket map.

## Sub-Regimes

Each sub-state below is a reading of basis *health*, not a basis mechanic. Follow the links out for how the carry itself works. The four bands below (<3% / 3–6% / 6–8% elevated / 8%+) are the framework's illustrative cut points, not hard lines; the **direction of travel** (is the basis firming or bleeding?) matters more than the exact number, and the 6–8% zone is the transitional "elevated" band where a healthy carry is tipping into crowded.

### High Basis (8%+ APR) — bias: Fragile, reduce size
- **Signal**: Annualized basis sustained at ~8%+ APR — or rising through the ~6–8% elevated zone toward it (framework heuristics, Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). The [[basis-trading|cash-and-carry]] is crowded; leveraged longs are paying up to be long and carry traders are piling into the spread.
- **Bias**: Fragility forming. A rich basis looks like a juicy carry but is also a measure of how much leverage is stacked on one side — the more attractive the carry, the more crowded and brittle the positioning.
- **What to trade**: Reduce directional size and watch for the unwind. The carry is harvestable but treat it as a *late-cycle* condition; the entry is crowded and the exit is the cascade.

### Healthy Basis (3–6%) — bias: Constructive long
- **Signal**: Annualized basis in the ~3–6% band (framework heuristic, Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) — positive enough to reflect genuine demand, not so rich that it signals crowding.
- **Bias**: Sustainable accumulation. The framework flags this as the *best long environment*: leverage is being added at a pace the market can support, not a blow-off.
- **What to trade**: Constructive long bias, and carry harvest via [[funding-rate-arbitrage]] is viable here because the spread is being replenished by real flow rather than reflexive leverage. This is the regime to *be in*, not to fade.

### Basis Collapse / Inversion — bias: Defensive, fade the flush
- **Signal**: Basis compresses hard or flips into backwardation (perp/futures below spot). Carry traders are exiting, fear is extreme, and the spread that financed the longs has evaporated.
- **Bias**: Cascade likely. The unwind of a crowded carry *is* the forced-selling event — the [[2025-10-crypto-liquidation-cascade|October 2025 cascade]] is the canonical example of basis collapse coinciding with a self-amplifying flush.
- **What to trade**: Defensive — cut leverage and protect the book. Tactically, look for the over-shoot flush to fade once forced selling and carry-unwind exhaust, mirroring the cascade-fade logic in [[derivatives-native-regime]].

### Flat / Marginal Basis (<3%) — bias: Low-conviction range
- **Signal**: Basis grinding below ~3% APR (framework heuristic, Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) with no persistent direction. Institutional cash-and-carry capital is sidelined because the spread does not clear its hurdle rate.
- **Bias**: Range-bound fragility. Without the carry bid, the market lacks the structural buyer that a healthy basis provides; price drifts and chops.
- **What to trade**: Low-conviction, range tactics — fade extremes of the range rather than press direction. Wait for the basis to firm into the *Healthy* band before adding directional risk.

## Basis as a Fragility Gauge

The regime framing rests on a single mechanism. A high, crowded basis means leveraged longs are *financing the carry*: they are long perp/futures (or long spot and short the rich future), and the spread is the cost or yield that keeps them in the position. While the basis stays rich, the carry pays and the leverage is comfortable. But the same richness measures how much leverage has accumulated on one side of the book. When the basis collapses, that financing reverses: longs unwind, the carry trade is closed in size, and the resulting forced selling *is* the cascade. The basis does not predict the cascade from the outside — it is the dial on the very pressure that becomes the cascade.

This basket is the **basis leg of the fragility triad**. The full stack — crowded basis (this basket) + persistent funding/record OI ([[derivatives-native-regime]]) + OI outrunning book depth ([[liquidity-depth-regime]]) — and why their *alignment* (not any single dial) is the pre-cascade signature, is stated canonically in [[crypto-market-regime-taxonomy#The Fragility Triad (canonical)|the taxonomy]]. This page covers only the basis dial.

## Detection Signals

Read basis health from four primary signals:

1. **Annualized basis** — perpetual basis (perp vs spot, expressed as an annualized rate via funding) and dated-futures basis (calendar future vs spot). The level relative to the ~8% / 3–6% / <4% bands (framework heuristics, Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) sets the sub-state. See [[basis]].
2. **Funding level and persistence** — for perps, the [[funding-rate]] *is* the basis; sustained positive funding is a rich perpetual basis. Persistence matters more than a single print.
3. **Open interest alongside basis** — a rich basis on rising OI is leverage building (fragile); a rich basis bleeding OI is the carry already unwinding.
4. **Term structure** — contango (futures above spot) confirms a healthy/rich carry; backwardation (futures below spot) is the inversion that flags collapse.

**Hyperliquid structural edge**: [[hyperliquid|Hyperliquid]]'s on-chain funding and OI are transparent in real time rather than reconstructed from a CEX's partial feeds, which makes basis-health tracking precise — perpetual basis and the OI behind it can be read directly per coin. See [[hyperliquid]].

## Relationship to Other Regimes

This basket is a **fragility detector, not a directional backdrop** — it sits alongside [[derivatives-native-regime]] (funding/OI) and [[liquidity-depth-regime]] (OI vs depth) as the third leg of the pre-cascade signature. The carry that this basket measures is the same leverage those baskets watch for failure, so the three overlap heavily.

Basis collapse rarely happens in a vacuum: it usually *coincides with* a trigger from another regime — a [[security-black-swan-regime|security shock / black swan]] that scares carry traders out, or a [[crypto-macro-correlation-regime|macro risk-off]] event that pulls the bid. Those regimes supply the catalyst; the crowded basis supplies the fuel.

## Pitfalls

- **Treating high basis as a pure long signal.** A rich basis reflects demand, but it is *also* a fragility reading — the richer and more crowded the carry, the closer the unwind. Do not read 8%+ APR as "bullish" without reading it as "crowded."
- **Assuming the carry is risk-free.** Cash-and-carry and [[funding-rate-arbitrage]] are *not* riskless: auto-deleveraging (ADL) can force-close the perp leg mid-cascade, a stablecoin or wrapped-asset depeg can break the spot leg, and venue/counterparty risk sits underneath both. The carry yield is compensation for exactly these tail risks.
- **Expecting the unwind on your schedule.** A crowded basis can stay crowded far longer than it "should." Richness is a *condition*, not a timing trigger — wait for the basis to actually roll over (compression, OI bleed, term-structure inversion) before positioning for collapse.

## Sources

- (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]) — defines the 14-basket taxonomy and the basis-health bands (8%+ / 3–6% / <4% APR) used here.

## Related

- [[crypto-market-regime-taxonomy]] — hub for all 14 baskets
- [[derivatives-native-regime]] — funding/OI fragility, overlapping carry leverage
- [[liquidity-depth-regime]] — depth side of the fragility equation
- [[basis]] · [[basis-trading]] — the basis spread and cash-and-carry mechanics
- [[funding-rate-arbitrage]] · [[funding-rate]] — delta-neutral carry harvest and the perpetual basis
- [[2025-10-crypto-liquidation-cascade]] — canonical basis-collapse cascade
- [[hyperliquid]] — transparent on-chain funding/OI for precise basis-health tracking
