---
title: "LQD (iShares Investment Grade Corporate Bond ETF)"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [bonds, fixed-income, risk-management]
aliases: ["LQD", "lqd", "iShares iBoxx $ Investment Grade Corporate Bond ETF"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[corporate-bonds]]", "[[etf]]"]
difficulty: intermediate
related: ["[[corporate-bonds]]", "[[credit-spread]]", "[[credit-risk]]", "[[interest-rate-risk]]", "[[duration]]", "[[hyg]]", "[[etf]]", "[[credit-cycle]]", "[[treasuries]]", "[[bonds-overview]]", "[[yield-curve]]"]
---

LQD is the ticker for the **iShares iBoxx $ Investment Grade Corporate Bond ETF**, one of the largest and most liquid exchange-traded funds tracking US investment-grade (IG) corporate debt. Launched by [[blackrock|BlackRock]]'s iShares in 2002 and tracking the Markit iBoxx USD Liquid Investment Grade Index, it holds a diversified basket of dollar-denominated, investment-grade corporate bonds and is widely used as a benchmark instrument for IG credit exposure. See [[bonds-overview]] for where IG corporates sit in the broader fixed-income landscape.

> **Data note:** specific figures below (number of holdings, duration, expense ratio, yield) drift over time and across the rate cycle. Treat them as qualitative/illustrative; consult the current iShares fact sheet for live values.

## Snapshot

| Attribute | Description |
|-----------|-------------|
| Issuer | [[blackrock|BlackRock]] / iShares |
| Inception | 2002 |
| Underlying index | Markit iBoxx USD Liquid Investment Grade Index |
| Asset class | US investment-grade [[corporate-bonds]] (rated BBB-/Baa3 and above) |
| Replication | Physical (holds the underlying bonds) |
| Distributions | Monthly |
| Primary risks | [[interest-rate-risk]] (long duration) + [[credit-risk]] / [[credit-spread]] |
| High-yield analogue | [[hyg]] |
| Rate-only analogue | Treasury ETFs (e.g. IEF, [[treasuries|TLT]]) |

## What It Holds

- **Holdings:** a broad basket (historically on the order of a couple thousand) of investment-grade corporate bonds (rated BBB-/Baa3 and above), spanning financials, industrials, utilities, healthcare, and technology issuers — heavily diversified across issuers to dilute single-name [[credit-risk|default risk]].
- **Effective duration:** historically long, around 8 years — meaning LQD carries substantial [[interest-rate-risk]] in addition to credit risk. As a first-order estimate, a 100 bp rise in rates implies roughly an 8% price decline, all else equal (see [[duration]] for the `ΔPrice% ≈ −Duration × Δyield` rule).
- **Structure:** monthly distributions; physically replicated (holds the bonds) with an authorized-participant creation/redemption mechanism that keeps the share price tethered to net asset value ([[etf|NAV]]) in normal conditions.

## Two Risk Factors in One Instrument

LQD's price is driven by two largely independent factors:

1. **Rate risk** — as a long-duration bond fund, LQD falls when Treasury yields rise. In 2022 it posted one of its worst drawdowns ever almost entirely on duration, not credit.
2. **Credit-spread risk** — the [[credit-spread]] (yield over Treasuries) widens in risk-off regimes, pushing LQD down independently of rates. LQD vs an equal-duration Treasury ETF (e.g. IEF) isolates the pure credit-spread move.

Pairing LQD with high-yield ([[hyg|HYG]]) and [[treasuries|Treasuries]] lets traders decompose any bond-market move into rate vs. IG-spread vs. high-yield-spread components.

### Worked example: decomposing a move

Suppose over a quarter LQD falls 5%. By comparing to an equal-duration Treasury ETF you might find Treasury yields rose enough to explain a 3% decline (pure [[duration]]/rate effect), leaving 2% attributable to IG [[credit-spread]] widening. If [[hyg]] fell 9% over the same window, the high-yield spread widened far more than IG — a classic [[risk-off]] signal of credit-market stress concentrated in lower-quality issuers. This rate-vs-IG-spread-vs-HY-spread breakdown is the everyday analytical use of these three instruments together.

## Trading Relevance

- **Credit barometer.** LQD's price and its option-implied volatility are watched as a real-time gauge of IG credit-market stress; widening spreads tend to lead equity drawdowns in the [[credit-cycle]].
- **March 2020 case study.** During the COVID liquidity crisis LQD traded at a steep discount to its net asset value as the underlying bond market froze — the dislocation was a key trigger for the Federal Reserve's unprecedented decision to buy corporate-bond ETFs directly, after which the discount collapsed. This episode is the canonical example of ETF/NAV basis risk in fixed income.
- **Hedging and expression.** Liquid options and a borrow market make LQD a vehicle for hedging IG portfolios, expressing duration views without single-name selection, and running rate-vs-credit relative-value trades (long LQD / short Treasury futures to strip out duration and isolate spread).
- **Liquidity proxy.** Because the ETF trades continuously while many constituent bonds trade rarely, LQD often provides price discovery for the underlying IG market during stress — a feature and a risk.

## How Traders Use LQD

- **Core IG allocation.** Long-term investors use LQD as a one-ticket way to hold diversified investment-grade credit, earning a yield premium over [[treasuries]] in exchange for credit and rate risk.
- **Macro credit gauge.** Watching LQD's price, its [[credit-spread|spread]] over Treasuries, and its option-implied volatility provides a real-time read on IG credit conditions — an input to broader [[risk-on|risk-on/risk-off]] positioning.
- **Relative-value expression.** Long LQD / short Treasury futures strips out [[duration]] to isolate the credit-spread view; LQD vs [[hyg]] expresses an IG-vs-high-yield quality preference.
- **Hedging.** Liquid LQD options and a borrow market let managers hedge an IG bond book or take a tactical short against credit deterioration without selling individual bonds.

## Common Pitfalls and Risks

- **It is not a Treasury substitute.** LQD carries genuine [[credit-risk]]; in a recession both rates *and* spreads can move against it, and defaults can impair specific holdings.
- **Long-duration sting.** With ~8-year duration, LQD is highly exposed to rising rates — the 2022 drawdown was driven almost entirely by duration, not credit. Investors reaching for its yield often underestimate this.
- **NAV/basis risk in stress.** As March 2020 showed, the ETF can trade at a meaningful discount to NAV when the underlying bond market is illiquid; the continuously-traded price can move faster than the (stale) NAV.
- **Yield ≠ return.** The distribution yield is not a guaranteed total return; price losses from rising rates or widening spreads can swamp coupon income in a bad year.
- **Concentration in financials.** IG corporate indices are heavily weighted toward bank and financial issuers, adding sector-correlated risk during financial-system stress.

## Related

- [[corporate-bonds]] — the underlying asset class
- [[credit-spread]] / [[credit-risk]] — the credit risk factor LQD carries
- [[interest-rate-risk]], [[duration]] — the rate-risk dimension
- [[treasuries]] — the rate-only comparison instrument
- [[hyg]] — the high-yield analogue
- [[etf]] — instrument structure and NAV mechanics
- [[credit-cycle]] — regime that drives spreads
- [[bonds-overview]] — the fixed-income hub page

## Sources

- iShares (BlackRock) LQD fund fact sheet and prospectus — holdings, duration, index methodology
- Markit iBoxx USD Liquid Investment Grade Index methodology
- Federal Reserve Secondary Market Corporate Credit Facility (2020) — ETF purchases including LQD
