---
title: Contango
type: concept
created: 2026-04-06
updated: 2026-07-01
status: excellent
tags: [futures, derivatives, commodities, volatility]
aliases: ["contango market", "futures premium", "Contango"]
domain: [market-microstructure]
prerequisites: ["[[futures-overview]]", "[[spot-price]]", "[[cost-of-carry]]"]
difficulty: intermediate
related:
  - "[[backwardation]]"
  - "[[spot-price]]"
  - "[[speculation]]"
  - "[[roll-yield]]"
  - "[[cost-of-carry]]"
  - "[[convenience-yield]]"
  - "[[storage-economics]]"
  - "[[commodity-curve-rolls]]"
---

# Contango

Contango is a market condition where the futures price of a commodity or asset is higher than the current [[spot-price]], creating an upward-sloping term structure across expiration dates.

## Why Contango Occurs

- **[[storage-economics|Storage costs]]** - Physical [[commodities]] (oil, gold, grain) incur storage, insurance, and financing costs that are priced into futures
- **[[cost-of-carry]]** - The theoretical futures price equals [[spot-price]] plus the cost of holding the asset until delivery: F = S x e^(r+c-y)t where r=risk-free rate, c=storage, y=[[convenience-yield]]
- **Supply/demand expectations** - Markets may price in expected future scarcity or [[inflation]]
- **Low [[convenience-yield]]** - When inventories are ample, the benefit of holding physical commodity is low, allowing storage costs to dominate the curve

## Impact on Traders

- **Negative [[roll-yield]]** - Traders holding long futures positions must periodically "roll" from expiring contracts to later ones. In contango, each roll means buying a more expensive contract, creating a drag on returns. The [[commodity-curve-rolls|commodity curve roll anomaly]] (Erb & Harvey) documents this systematic drag.
- **ETF decay** - Commodity ETFs that hold futures (e.g., USO for [[crude-oil|oil]]) suffer persistent losses in contango markets as they continuously roll contracts at a premium.
- **[[cash-and-carry]] arbitrage** - Traders can buy the [[spot-price|spot]] asset, sell the futures, and earn the spread (if [[storage-economics|storage]] is feasible). This is the fundamental [[basis-trading|basis trade]] in [[commodities]].

## Trading Relevance

Understanding contango is essential for anyone trading commodity futures or futures-based ETFs/ETPs. The persistent contango in oil futures has historically eroded the value of long-only oil ETFs, making them poor long-term holdings compared to spot exposure. In crypto, perpetual futures in contango create funding rate payments from longs to shorts.

## Worked Example (hypothetical)

The numbers below are illustrative, not historical, and ignore taxes and bid-ask costs.

Suppose crude oil spot is $80.00 and the futures curve is in contango:

| Contract | Price |
|----------|-------|
| Front month (expires in 1 month) | $80.40 |
| Second month | $80.80 |
| Third month | $81.20 |

The curve rises ~$0.40 per month (~0.5%). A futures-based ETF holding the front month must **roll** before expiry: it sells the $80.40 contract and buys the $80.80 contract. If spot is unchanged when the front month converges to $80.00 at expiry, the fund has effectively "bought high, sold low" by $0.40 on each roll.

- **Roll drag per month:** ~0.5% of position value.
- **Annualised drag if contango persists:** roughly 0.5% x 12 ≈ 6% before any change in spot.

So even if oil's spot price is flat for a year, the ETF can lose ~6% purely to [[roll-yield|negative roll yield]]. This is why a long-only futures ETF can fall while the underlying commodity's spot price is unchanged — the gap between spot return and ETF return is the roll drag. The opposite happens in [[backwardation]], where rolling into cheaper deferred contracts adds a positive roll yield.

## How to Interpret the Curve

- **Steepness matters more than direction alone.** A 0.5%/month contango is a meaningful drag; a 0.05%/month contango is negligible. Traders look at the annualised roll yield, not just whether the curve slopes up.
- **Contango is "normal" for storable commodities.** For assets with real [[storage-economics|storage costs]] and no [[convenience-yield]] benefit (e.g. ample-inventory crude, natural gas in shoulder season), an upward-sloping curve is the default state implied by [[cost-of-carry]] — it does not by itself signal a bearish view.
- **Super-contango signals stress.** An unusually steep curve (e.g. the 2020 oil glut) reflects a market desperate to defer delivery because physical storage is full — a genuine fundamental signal, not just carry.

## Limitations and Nuances

- **Contango is not a forecast.** A higher futures price does not mean the market "expects" the spot price to rise; under [[cost-of-carry]] it mostly reflects storage and financing, and the futures price typically converges *down* to spot at expiry.
- **Roll drag is not guaranteed loss.** If spot rises faster than the roll drag, a long futures position still profits; contango only describes the *carry* component, not the *spot* component, of total return.
- **Curve shape changes.** Markets flip between contango and [[backwardation]] as inventories and [[convenience-yield]] shift, so a backtest that assumes permanent contango can mislead.
- **Equity-index and financial futures** sit in mild contango from the [[cost-of-carry|carry]] of interest rates minus [[dividends]]; the storage-cost intuition that dominates physical commodities does not apply.

## Opposite

The inverse condition is [[backwardation]], where futures trade below spot.

## Related

- [[backwardation]]
- [[roll-yield]]
- [[cost-of-carry]]
- [[convenience-yield]]
- [[storage-economics]]
- [[commodity-curve-rolls]]
- [[basis-trading]]
- [[cash-and-carry]]
- [[futures-curve-structure-analysis]]

## Sources

- Hull, J. C. *Options, Futures, and Other Derivatives* (chapter on forward and futures prices / cost of carry).
- Erb, C. & Harvey, C. (2006). "The Strategic and Tactical Value of Commodity Futures." *Financial Analysts Journal* (roll yield and curve drag).
- CME Group, "Understanding Contango and Backwardation" (educational materials).
