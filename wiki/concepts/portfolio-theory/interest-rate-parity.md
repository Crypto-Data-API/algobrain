---
title: "Interest Rate Parity"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [forex, arbitrage, macro, derivatives]
aliases: ["Interest Rate Parity", "IRP", "Covered Interest Rate Parity", "Uncovered Interest Rate Parity", "CIP", "UIP", "interest-rate-parity"]
domain: [portfolio-theory, macro]
prerequisites: ["[[interest-rates]]", "[[forex]]", "[[arbitrage]]"]
difficulty: intermediate
related: ["[[interest-rates]]", "[[forex]]", "[[arbitrage]]", "[[carry-trade]]", "[[forward-contract]]", "[[purchasing-power-parity]]", "[[cross-currency-basis]]", "[[no-arbitrage]]"]
---

Interest rate parity (IRP) is the no-arbitrage condition linking the spot exchange rate, the forward exchange rate, and the interest rates of two currencies. In its strict (covered) form it says the forward premium or discount of one currency against another must exactly offset the interest-rate differential between them -- otherwise a riskless arbitrage exists. IRP is the foundation of FX forward pricing, the theoretical anchor for the [[carry-trade]], and a lens on global funding stress.

## Covered Interest Rate Parity (CIP)

CIP uses a forward contract to lock in (cover) the future exchange rate, removing currency risk. The condition is:

```
F / S = (1 + i_d) / (1 + i_f)
```

where `S` is the spot rate (units of domestic currency per unit of foreign), `F` the forward rate for the same horizon, `i_d` the domestic interest rate, and `i_f` the foreign rate (both for the matching tenor). Rearranged, the **forward premium** approximately equals the interest-rate differential:

```
(F − S) / S ≈ i_d − i_f
```

The currency with the *higher* interest rate trades at a *forward discount*; the lower-rate currency at a forward premium. If this fails, an investor can borrow the cheap currency, convert spot, lend in the high-rate currency, and lock the reconversion forward for a riskless profit -- the arbitrage that enforces CIP. Because it is a pure no-arbitrage relationship, CIP held almost exactly pre-2008.

### The CIP basis (post-2008 breakdown)

Since the 2008 crisis, CIP has visibly *failed* -- a persistent [[cross-currency-basis|cross-currency basis]] (often tens of basis points, blowing out in stress) reflects the cost of balance-sheet, dollar-funding scarcity, regulatory constraints (Basel III leverage ratios), and dealer reluctance to arbitrage. The basis widens sharply in crises (2008, March 2020) as everyone scrambles for dollars, making it a real-time gauge of global USD funding stress.

## Uncovered Interest Rate Parity (UIP)

UIP drops the forward hedge and instead asserts that the *expected* change in the spot rate offsets the interest differential:

```
E[ΔS] / S ≈ i_d − i_f
```

i.e. high-interest-rate currencies are expected to *depreciate* by roughly their rate advantage, so expected returns are equalised across currencies. UIP is a statement about expectations, not a no-arbitrage condition, and it is empirically *false* over most horizons -- the famous **forward premium puzzle** (Fama, 1984): high-rate currencies have historically tended to *appreciate or hold*, not depreciate, on average. That empirical failure is precisely what the [[carry-trade]] monetises.

## Trading and Portfolio Relevance

- **FX forward / swap pricing.** CIP is the formula dealers use to quote FX forwards and FX swaps; forward points are mechanically derived from the rate differential.
- **The carry trade.** Because UIP fails, borrowing low-yield currencies (historically JPY, CHF, EUR) to fund high-yield currencies (AUD, NZD, EM) has been profitable on average -- harvesting the interest differential the market does not "give back" via depreciation. The risk is sharp, correlated drawdowns when carry unwinds (e.g. the August 2024 yen-carry unwind), giving carry its characteristic negative-skew, "picking up pennies in front of a steamroller" return profile.
- **Hedging cost.** A portfolio manager hedging foreign-currency assets pays or earns the CIP-implied forward points; the rate differential *is* the currency-hedging carry, a material drag or boost on hedged international allocations.
- **Funding-stress signal.** The cross-currency basis is a watched indicator of dollar funding tightness and counterparty stress.

## Relationship to Other Parity Conditions

IRP concerns the *financial* (interest/exchange-rate) linkage; [[purchasing-power-parity]] concerns the *goods-price* linkage (exchange rates should equalise the price of a basket of goods). Together with the Fisher relation they form the set of international parity conditions in open-economy macro -- all approximate, all useful as anchors, all violated to exploitable degrees in practice.

## Related

- [[interest-rates]] -- the differential that drives the forward premium
- [[forex]] -- the market where IRP is enforced
- [[arbitrage]] -- the mechanism that enforces covered parity
- [[carry-trade]] -- the strategy that monetises the failure of uncovered parity
- [[forward-contract]] -- the instrument that "covers" the exchange-rate risk
- [[cross-currency-basis]] -- the measured deviation from covered parity
- [[purchasing-power-parity]] -- the goods-market parity counterpart

## Sources

- Keynes, J.M. *A Tract on Monetary Reform* (1923) -- early statement of covered interest parity.
- Fama, E. (1984) "Forward and Spot Exchange Rates," *Journal of Monetary Economics* -- the forward premium puzzle.
- Du, W., Tepper, A., Verdelhan, A. (2018) "Deviations from Covered Interest Rate Parity," *Journal of Finance* -- post-2008 CIP basis.
- Borio, C. et al. (2016) "Covered interest parity lost: understanding the cross-currency basis," *BIS Quarterly Review*.
- Mark, N. *International Macroeconomics and Finance* -- textbook treatment of parity conditions.
