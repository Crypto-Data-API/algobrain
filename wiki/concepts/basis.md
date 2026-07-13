---
title: "Basis"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [futures, derivatives, market-microstructure, arbitrage]
aliases: ["Basis", "Futures Basis", "Cash-Futures Basis"]
domain: [market-microstructure]
prerequisites: ["[[futures]]", "[[cost-of-carry]]"]
difficulty: intermediate
related: ["[[futures]]", "[[contango]]", "[[backwardation]]", "[[funding-rate]]", "[[arbitrage]]", "[[cost-of-carry]]", "[[hedging]]", "[[perpetual-swaps]]", "[[basis-trade]]"]
---

The basis is the difference between the spot (cash) price of an asset and its [[futures]] price. It is commonly expressed as **basis = spot price - futures price**. When the futures price exceeds the spot price (negative basis under this convention), the market is in [[contango]]; when spot exceeds futures (positive basis), the market is in [[backwardation]]. The basis converges to zero at futures expiration, since the futures contract settles to the spot price.

> **Sign-convention warning:** many commodity desks and data feeds quote basis the *opposite* way — **futures − spot** — so a "positive basis" can mean either condition depending on the source. Always confirm the convention before trading; this page uses **spot − futures** throughout.

## The two sign conventions

| Convention | Formula | Contango (futures > spot) | Backwardation (futures < spot) |
|---|---|---|---|
| This page (cash basis) | spot − futures | **negative** basis | **positive** basis |
| Common commodity desk | futures − spot | positive | negative |

Because both are in wide use, professionals usually just say "the curve is in [[contango]]/[[backwardation]]" to avoid ambiguity, and reserve "basis" for a specific cash-vs-contract spread when hedging.

## Cost of Carry Model

In theory, the futures price reflects the spot price plus the cost of carrying the underlying asset to the delivery date. This cost of carry includes storage costs, insurance, financing (interest rates), and minus any income the asset generates (dividends, convenience yield). For financial futures like equity index futures, the basis is primarily driven by the risk-free interest rate minus the dividend yield. When actual basis diverges from the theoretical cost-of-carry, it can create [[arbitrage]] opportunities -- known as **cash-and-carry arbitrage** (buy spot, sell futures) or **reverse cash-and-carry** (sell spot, buy futures).

The general fair-value relationship is:

```
Fair futures price  F = S × e^((r + u − y) × T)

  S = spot price          r = risk-free financing rate
  u = storage/carry cost   y = income or convenience yield (dividends, lease rate)
  T = time to expiry (years)
```

For equity index futures this simplifies to **F = S × e^((r − d) × T)**, where d is the dividend yield. The carry components push the curve into [[contango]] or [[backwardation]]:

| Carry component | Pushes curve toward | Asset class where it dominates |
|---|---|---|
| High financing rate (r) | Contango | Equity index, financials |
| High storage cost (u) | Contango | Crude oil, natural gas, grains |
| High dividend / income yield (y) | Backwardation | Equity index (high payers) |
| High convenience yield | Backwardation | Commodities in tight supply |

### Worked example: cash-and-carry on an index future

Suppose an index trades at **S = $5,000**, the financing rate is **r = 5%**, the dividend yield is **d = 2%**, and the future expires in **T = 0.5 years**.

- Fair value = $5,000 × e^((0.05 − 0.02) × 0.5) = $5,000 × e^0.015 ≈ **$5,075.6**.
- If the future actually trades at **$5,110** (rich by ~$34), an arbitrageur runs **cash-and-carry**: buy the index basket for $5,000 (financed at 5%), sell the future at $5,110, collect $50 of dividends over the half-year, and lock in the convergence. Net of ~$125 financing cost and the $50 dividend, the ~$110 contract premium leaves a near-riskless profit until the rich basis is arbitraged away.
- If instead the future trades **cheap** (say $5,040), the **reverse** trade applies: short the basket, invest the proceeds at 5%, buy the future.

In practice these gaps are tiny and fleeting because index arbitrage desks compete them away; the residual basis is the market's read on real-world financing and dividend expectations.

## Basis Risk

Basis risk arises when a hedge using futures does not perfectly offset the underlying exposure, because the basis changes unpredictably. For example, a farmer hedging wheat with CBOT wheat futures faces basis risk because local cash wheat prices may not move in lockstep with the futures contract. Basis risk is a key consideration in any hedging program and is the reason that hedging reduces but does not eliminate all price risk. The less correlated the hedge instrument is with the underlying exposure, the greater the basis risk.

The common sources of basis risk are worth naming because each is mitigated differently:

| Source of basis risk | Description | Mitigation |
|---|---|---|
| Asset (quality) mismatch | Hedge instrument differs in grade/type from the exposure (e.g. local cash wheat vs CBOT contract) | Choose the most correlated contract; cross-hedge ratio |
| Location mismatch | Spot in one delivery point, future in another | Use a contract with nearby delivery; adjust for transport |
| Calendar (maturity) mismatch | Hedge expires before/after the exposure ends | Roll the hedge; stack-and-roll |
| Quantity mismatch | Standardized contract size ≠ exposure size | Accept rounding; use mini/micro contracts |

A producer who is **long the physical and short futures is effectively long the basis**: they gain when the basis strengthens (spot rises relative to futures) and lose when it weakens — which is why "trading the basis" is itself a recognized commercial activity for merchants and elevators.

## Crypto Perpetual Basis and Funding Rates

In cryptocurrency markets, perpetual swap contracts have no expiration date, so basis convergence does not happen naturally. Instead, exchanges use a [[funding-rate]] mechanism to tether the perpetual price to the spot price. When the perpetual trades above spot (positive funding), longs pay shorts; when below spot, shorts pay longs. The annualized basis on crypto perpetual swaps can range from near-zero in quiet markets to 30-50%+ during euphoric bull markets, creating opportunities for **basis trading** (buy spot, short perpetual, collect funding). This is a popular market-neutral strategy in [[crypto]] markets.

## Trading Relevance

The basis is the central state variable for three distinct activities. For **hedgers**, it converts price risk into the smaller (but non-zero) basis risk — a producer who is long the physical and short futures is effectively long the basis, and profits when the basis strengthens. For **cash-and-carry arbitrageurs**, the gap between actual and theoretical (cost-of-carry) basis defines a near-riskless return if it exceeds funding and storage costs. For **crypto basis traders**, the annualized perpetual basis (funding) is harvested directly as a market-neutral carry yield. Watching the basis is also a sentiment gauge: a sharply rising equity-index basis or crypto funding signals leveraged-long crowding, and a collapse or inversion (backwardation) often coincides with deleveraging or supply stress in commodities. Note that "basis" is sometimes quoted with the opposite sign convention (futures minus spot); always confirm which convention a data feed uses before trading on it.

### Who uses the basis, and how

| Participant | What the basis is to them | Action |
|---|---|---|
| Producer / merchant | Commercial P&L driver | Hedge with futures; trade the local basis |
| Index-arb desk | A mispricing signal | Cash-and-carry / reverse when it breaks fair value |
| [[basis-trade\|Treasury basis trader]] | Cash bond vs futures spread | Leveraged long cash / short futures (repo-funded) |
| Crypto carry trader | Funding yield | Long spot, short [[perpetual-swaps\|perp]]; collect funding |
| Macro / sentiment reader | Positioning gauge | Read funding / index basis for crowding & stress |

A note on the **[[basis-trade|Treasury basis trade]]**: leveraged funds exploit the small spread between cash Treasuries and Treasury futures, financing the cash leg in [[repo|repo]] at very high leverage. The trade is profitable in calm markets but is a recognized systemic-risk concern — a funding-market shock can force rapid unwinds (as flagged around the March 2020 "dash for cash"), illustrating that "near-riskless" basis trades carry significant liquidity and funding risk.

## Common pitfalls

- **Sign-convention confusion** — reading "positive basis" as the wrong market state because the data feed uses futures − spot. Confirm first.
- **"Riskless" is never riskless** — cash-and-carry and the Treasury basis trade depend on stable financing; a [[repo|repo]] or funding squeeze can blow up a position that converges perfectly in theory.
- **Carry costs underestimated** — storage, insurance, financing, and transaction costs can swallow an apparent arbitrage; only the *net* edge matters.
- **Roll cost in [[contango]]** — long futures (or futures-based ETFs) bleed value each roll in steep contango ([[roll-yield|negative roll yield]]); a flat spot can still produce losses.
- **Convergence isn't always smooth** — physical-delivery quirks, squeezes, and limit moves can keep the basis dislocated right into expiry.
- **Crypto funding regime shifts** — perpetual funding can flip from richly positive to deeply negative fast, turning a carry harvest into a cost.

## Related

- [[futures]] -- the derivative contracts whose pricing defines the basis
- [[contango]] -- market condition where futures trade above spot
- [[backwardation]] -- market condition where futures trade below spot
- [[cost-of-carry]] -- the model that prices the theoretical basis
- [[funding-rate]] -- mechanism that controls basis in crypto perpetual swaps
- [[hedging]] -- the activity whose residual risk is basis risk
- [[arbitrage]] -- strategies that exploit basis mispricing
- [[basis-trade]] -- the leveraged cash-vs-futures Treasury trade
- [[perpetual-swaps]] -- crypto contracts whose basis is set by funding
- [[roll-yield]] -- P&L from rolling futures along the curve
- [[repo]] -- the financing market that underpins carry trades
- [[convenience-yield]] -- the carry term that drives commodity backwardation

## Sources

- John C. Hull, *Options, Futures, and Other Derivatives* (10th ed.) — cost-of-carry pricing, basis risk, and hedging chapters.
- CME Group, "Understanding Basis" educational materials (agricultural and financial futures).
- Robert McDonald, *Derivatives Markets* (3rd ed.) — cash-and-carry and reverse cash-and-carry arbitrage.
