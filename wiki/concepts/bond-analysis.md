---
title: "Bond Analysis"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [bonds, fundamental-analysis, valuation, derivatives]
aliases: ["Bond Analysis", "bond-analysis", "fixed income analysis", "bond valuation"]
related: ["[[bonds]]", "[[duration]]", "[[yield-curve]]", "[[credit-cycle]]", "[[interest-rates]]", "[[corporate-bonds]]", "[[treasury-bonds]]", "[[convexity]]"]
domain: [fundamental-analysis]
prerequisites: ["[[bonds]]", "[[interest-rates]]"]
difficulty: intermediate
---

**Bond analysis** is the discipline of valuing fixed-income securities and measuring their sensitivity to interest-rate and credit risk. Where equity analysis centres on growth and earnings, bond analysis centres on *yield*, *cash-flow certainty*, *interest-rate sensitivity*, and *default risk*. Its core outputs are a fair price/yield, a measure of duration and convexity, and a credit assessment of the issuer.

## Yield Measures

A bond's price and yield move inversely, so analysts work primarily in yield terms. The main measures, in increasing order of usefulness:

- **Current yield** — annual coupon ÷ current price. A crude income measure that ignores capital gain/loss to maturity.
- **Yield to maturity (YTM)** — the single discount rate that sets the present value of all coupons plus principal equal to the current market price. YTM is the bond's internal rate of return assuming it is held to maturity and all coupons are reinvested at the same rate. It is the standard quote for comparing bonds.
- **Yield to call (YTC)** / **yield to worst (YTW)** — for callable bonds, the yield assuming the issuer redeems early; YTW is the lowest of YTM and all YTC scenarios, the conservative figure.
- **Spread measures** — for non-Treasuries, the **option-adjusted spread (OAS)** or **Z-spread** over the [[treasury-bonds|Treasury]] curve isolates the compensation for credit and liquidity risk after stripping out the risk-free term structure.

## Valuation

A bond is priced as the present value of its cash flows discounted at the appropriate rate(s):

`Price = Σ [ Coupon_t / (1 + y)^t ] + [ Face / (1 + y)^n ]`

In practice each cash flow is discounted at the corresponding point on the spot/zero curve rather than a single YTM. A bond trades at a **premium** when its coupon exceeds prevailing yields, at a **discount** when below, and at **par** when equal.

## Interest-Rate Risk: Duration and Convexity

The central risk measures of bond analysis:

- **[[duration]]** (modified duration) — the approximate percentage change in price for a 1% change in yield. A bond with modified duration 7 falls ~7% if yields rise 1%. Duration rises with maturity and falls with coupon size. **Macaulay duration** is the weighted-average time to receive cash flows; **DV01** expresses the same sensitivity in dollars per basis point.
- **[[convexity]]** — the curvature of the price/yield relationship. Duration is a linear approximation; convexity corrects it for large yield moves. Positive convexity (most option-free bonds) means prices rise more when yields fall than they fall when yields rise — a favourable asymmetry. Callable and mortgage-backed bonds can exhibit *negative* convexity.

Duration is the single most important number a bond trader manages, because it converts a view on [[interest-rates|rates]] into a precise position-sizing and hedging input.

## Credit Analysis

For anything other than risk-free government debt, the analyst must assess **default risk**:

- **Ratings** — agency grades (e.g. AAA down to D from S&P/Fitch, Aaa to C from Moody's) split the universe into *investment grade* and *high yield* ("junk").
- **Fundamental credit metrics** — leverage (debt/EBITDA), interest-coverage ratios, free-cash-flow generation, and covenant quality, analogous to equity fundamental analysis but focused on the firm's ability to *service and repay debt* rather than grow.
- **Credit spreads and [[credit-default-swaps|CDS]]** — market-implied default risk; widening spreads signal deteriorating credit and risk-off conditions (see [[credit-cycle]]).

## Trading Relevance

- **Rate views become duration trades.** A trader expecting yields to fall buys duration (long longer-dated bonds); expecting a rise, shortens duration or sells. Duration and DV01 size the trade and let it be hedged against parallel curve shifts.
- **Curve and relative-value trades.** Bond analysis underpins yield-curve trades (steepeners/flatteners), butterflies, and credit relative-value (long undervalued vs. short overvalued issuers), where the [[spread]] rather than the outright yield is the position.
- **Credit-cycle positioning.** Spread levels and rating trends locate the market within the [[credit-cycle]]; widening high-yield spreads are a leading risk-off signal that bond analysts watch as an early warning for equities too.
- **Carry and roll-down.** Much fixed-income return is *carry* (earning the coupon/yield) plus *roll-down* (a bond's price appreciating as it ages down a positively sloped curve) — both quantified directly from the yield curve and the bond's cash-flow profile.

## Related

- [[bonds]] — the underlying instruments
- [[duration]] — the core interest-rate sensitivity measure
- [[convexity]] — the second-order correction to duration
- [[yield-curve]] — the term structure used to discount and to find relative value
- [[interest-rates]] — the primary driver of bond prices
- [[credit-cycle]] — where credit spreads sit in the macro cycle
- [[corporate-bonds]] — the main subject of credit analysis
- [[treasury-bonds]] — the risk-free benchmark for spread measurement
- [[credit-default-swaps]] — market-implied default risk

## Sources

- Frank J. Fabozzi, *Bond Markets, Analysis, and Strategies* — standard reference on yield measures, valuation, duration/convexity, and credit analysis.
- John C. Hull, *Options, Futures, and Other Derivatives* — term structure, duration, and DV01 hedging.
- CFA Institute curriculum, Fixed Income readings — YTM/YTW, spot-curve valuation, OAS, and credit-risk fundamentals.
