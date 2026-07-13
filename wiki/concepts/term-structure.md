---
title: "Term Structure"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [bonds, volatility, derivatives, commodities, options]
aliases: ["Term Structure", "Term Structure of Interest Rates", "Curve Structure"]
related: ["[[yield-curve]]", "[[volatility-term-structure]]", "[[contango]]", "[[backwardation]]", "[[futures-curve-structure-analysis]]", "[[roll-yield]]", "[[interest-rates]]", "[[interest-rate-risk]]", "[[vix]]", "[[calendar-spread]]", "[[duration]]"]
domain: [bonds, derivatives]
prerequisites: ["[[interest-rates]]"]
difficulty: intermediate
---

Term structure is the relationship between the price (or rate, or implied volatility) of an instrument and its time to maturity, holding all else equal. Plotting that relationship across maturities produces a curve whose **shape** and **changes in shape** carry information that a single spot price cannot. The concept generalises across asset classes: the [[yield-curve|term structure of interest rates]], the [[volatility-term-structure|term structure of implied volatility]], and the [[futures-curve-structure-analysis|term structure of futures prices]] ([[contango]]/[[backwardation]]) are the three most-traded examples.

## The Three Major Term Structures

### Interest rates (the yield curve)
The [[yield-curve]] plots government-bond yields from overnight to 30 years. Its slope encodes growth and [[inflation]] expectations plus a term premium; **inversion** (short rates above long rates) is one of the most reliable recession lead indicators. See [[yield-curve]] for shapes (normal, flat, inverted, humped) and the [[2s10s]] spread. Modelled formally with [[interest-rate-models]] (Vasicek, CIR, Hull-White) and traded via [[duration]]-neutral steepeners and flatteners.

### Implied volatility (vol term structure)
The [[volatility-term-structure]] plots implied volatility by option expiry for a fixed underlying. Normally upward-sloping (longer-dated options price more uncertainty); it inverts into **backwardation** during stress, when near-dated panic bids exceed long-dated vol. The [[vix]] complex makes this directly tradeable — VIX futures are usually in contango, and the resulting [[roll-yield]] is the engine of the short-vol carry trade (and the cause of the 2018 "Volmageddon" blow-up).

### Futures (commodity / crypto curves)
A futures term structure in **[[contango]]** slopes upward (later contracts more expensive — storage cost, ample supply); in **[[backwardation]]** it slopes downward (tight supply, high [[convenience-yield]]). The shape determines [[roll-yield]]: long positions in contango bleed as they roll up the curve, while backwardation pays. Crypto perpetuals express the same idea through the funding rate.

### The three term structures compared

| Term structure | Y-axis | Normal shape | Inverted/stressed shape | What inversion signals | Primary trade |
|----------------|--------|--------------|--------------------------|------------------------|---------------|
| [[yield-curve\|Interest rates]] | Yield by maturity | Upward (long > short) | Short rate > long rate | Recession risk / late cycle | Steepeners, flatteners, [[duration]] bets |
| [[volatility-term-structure\|Implied volatility]] | IV by expiry | Upward ([[contango]]) | Near-dated > long-dated ([[backwardation]]) | Acute risk-off / panic | Short-vol carry, [[calendar-spread\|vol calendars]] |
| [[futures-curve-structure-analysis\|Futures / commodities]] | Futures price by delivery | [[contango]] (upward) | [[backwardation]] (downward) | Physical scarcity / high [[convenience-yield]] | Carry, roll trades, calendars |

The unifying idea is **cost of carry**: in each case the slope reflects the cost (or benefit) of holding the asset over time — financing and storage push the curve up; yield, scarcity, and demand for protection pull it down or invert it.

## What the Shape Tells You

- **Slope** — expectations of future rates/prices/vol plus a risk premium.
- **Curvature (the "belly")** — relative-value dislocations exploited by butterfly trades.
- **Level shifts vs twists** — a parallel shift means the whole curve moves; a twist (steepening/flattening) means the front and back diverge, the basis of curve trades.
- **Inversion** — almost always a stress or expectations signal (recession for rates, panic for vol, scarcity for commodities).

## Trading Relevance

- **Roll yield is structural P&L.** Any held futures or vol position earns or pays the slope of its term structure regardless of spot direction — the dominant return driver in commodity-index and short-vol strategies (see [[roll-yield]], [[calendar-spread]]).
- **Curve trades isolate shape from level.** Steepeners/flatteners (rates), [[calendar-spread]]s (vol/equity options) and futures roll trades are bets on the curve changing shape, with much of the directional risk hedged out.
- **Term structure as a regime signal.** Vol backwardation flags acute risk-off; yield-curve inversion flags late cycle; commodity backwardation flags physical tightness. These feed [[regime-detection]] and cross-asset overlays.
- **Calendar arbitrage.** Persistent kinks invite [[calendar-spread-arbitrage]] when the cost-of-carry relationship is violated.

## Worked Example: Roll Yield in a Contango Curve

Suppose front-month crude oil trades at **$80** and the contract one month out trades at **$81** — an upward-sloping ([[contango]]) curve, perhaps because storage is plentiful and there is no acute scarcity.

- A long futures holder who never wants delivery must, before expiry, sell the cheaper expiring contract near $80 and buy the more expensive next contract at $81 — paying up by **$1**, or about **1.25% per month**.
- If spot oil simply stays at $80 all year, the position still **bleeds ~1.25% each roll** purely from the curve shape — roughly 15% annualised of negative [[roll-yield]] before any directional move.
- This is the structural reason commodity-index investors underperform spot in persistent contango, and why a **short** position in the same curve *earns* the roll.
- In [[backwardation]] the arithmetic reverses: the holder rolls from a more expensive expiring contract into a cheaper deferred one, **earning** positive roll yield even with flat spot.

The same mechanic powers the short-VIX-futures carry trade: VIX futures usually sit in [[contango]] above spot VIX, so a short position collects the roll down the curve in calm markets — and suffers a violent loss when the curve snaps into [[backwardation]] during a spike (the 2018 "Volmageddon").

## Pitfalls and Risks

- **Roll yield is not a free lunch.** Carry strategies that harvest the curve (short vol, long backwardated commodities) tend to earn small, steady gains punctuated by rare, large losses precisely when the curve flips — a classic "picking up pennies in front of a steamroller" payoff. Size for the tail, not the average.
- **Curves are non-stationary.** A commodity that has been in backwardation for years can move into structural contango (or vice versa) as supply/demand or financing conditions change; do not assume the current regime persists.
- **Inversion is a signal, not a guarantee.** [[yield-curve]] inversion has preceded recessions historically but with long and variable lags and occasional false signals; trading it as a precise timing tool is dangerous.
- **Spot vs total return divergence.** Headline "the commodity is up X%" can mask a losing futures position once roll cost is included — always evaluate carry strategies on a total-return (rolled) basis.
- **Liquidity thins down the curve.** Back-month contracts and longer-dated options are far less liquid; curve trades that look clean on screen can be expensive to enter and exit.
- **Funding/financing assumptions matter.** Cost-of-carry pricing assumes a financing rate; when rates move sharply (see [[interest-rate-risk]]), the "fair" shape of the curve itself shifts.

## Related

- [[yield-curve]] — interest-rate term structure (its dedicated page)
- [[volatility-term-structure]] — implied-vol term structure
- [[contango]], [[backwardation]], [[futures-curve-structure-analysis]] — commodity/futures curves
- [[roll-yield]] — the carry generated by curve shape
- [[calendar-spread]], [[calendar-spread-arbitrage]] — trades on the curve
- [[interest-rate-models]], [[duration]] — modelling and risk
- [[interest-rate-risk]] — how rate moves reshape the cost-of-carry curve
- [[vix]] — the most-traded vol term-structure complex

## Sources

- Fabozzi, F. *Bond Markets, Analysis, and Strategies* — term structure of interest rates.
- Hull, J. *Options, Futures, and Other Derivatives* — futures cost-of-carry and implied-volatility term structure.
- Cochrane, J. and Piazzesi, M. "Bond Risk Premia" (American Economic Review, 2005).
