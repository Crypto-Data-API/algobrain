---
title: "US Treasury Bonds"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [bonds, risk-management, treasuries]
domain: [portfolio-theory]
prerequisites: ["[[bonds]]", "[[interest-rates]]"]
difficulty: intermediate
aliases: ["Treasuries", "US Treasuries", "T-Bonds", "Treasury Bonds"]
related: ["[[us-debt]]", "[[interest-rates]]", "[[us-dollar]]", "[[market-crashes]]", "[[bonds]]", "[[interest-rate-risk]]", "[[yield-curve]]", "[[federal-reserve]]", "[[duration]]"]
---

US Treasury bonds are debt securities issued by the United States government, traditionally considered the global risk-free benchmark for fixed income. Fred discusses Treasuries as a potential trigger for the next major [[market-crashes|market crash]]: if bond prices collapse due to loss of confidence in US creditworthiness, [[interest-rates]] spike uncontrollably, crushing equity valuations and the broader economy. The US Treasury market is the largest and most liquid bond market in the world (exceeding $27 trillion outstanding), and its stability underpins the entire global financial system. Fred monitors the relationship between [[us-debt]] levels, Treasury yields, and the [[us-dollar]] as interconnected macro risk factors that could cascade into a systemic crisis.

## Types of Treasury Securities

The US Treasury issues several categories of debt, distinguished primarily by maturity:

| Security | Maturity | Coupon | Notes |
|---|---|---|---|
| **Treasury Bills (T-Bills)** | 4 weeks to 1 year | Zero-coupon (sold at discount) | Used as the "risk-free rate" for short-term pricing |
| **Treasury Notes (T-Notes)** | 2 to 10 years | Semi-annual fixed coupon | The 10-year note is the most-watched benchmark globally |
| **Treasury Bonds (T-Bonds)** | 20 to 30 years | Semi-annual fixed coupon | Longest-duration standard issue |
| **TIPS** | 5, 10, or 30 years | Semi-annual (inflation-adjusted principal) | Principal adjusts with CPI; protects against inflation |
| **I-Bonds** | 30 years (redeemable after 1 year) | Fixed + inflation-adjusted rate | Purchased directly from Treasury; $10K annual limit |
| **FRNs** | 2 years | Floating (13-week bill rate + spread) | Coupon resets weekly; minimal [[interest-rate-risk]] |

A related instrument is the **STRIP** (Separate Trading of Registered Interest and Principal Securities): dealers can split a coupon-bearing note or bond into its individual cash flows, each trading as a zero-coupon bond. STRIPS have the longest possible [[duration]] for a given maturity and are favored by liability-matching investors (pension funds, insurers) who want a single dated cash flow.

## How Treasuries Are Issued: Auctions

The Treasury raises cash through regularly scheduled **auctions** conducted via [[treasurydirect|TreasuryDirect]] and the primary-dealer system. Bidders submit either **competitive bids** (specifying the yield they will accept, used by institutions) or **non-competitive bids** (accepting whatever yield clears, used by retail and capped at $10 million). The auction is a *single-price* (Dutch) auction: every winning bidder pays the highest accepted yield (the "stop-out" or "high yield"), so aggressive bidders are not penalized for bidding too low a yield.

Auction health is read through three metrics that trading desks watch in real time:

| Metric | What it measures | Bullish read (strong demand) |
|---|---|---|
| **Bid-to-cover ratio** | Total bids submitted ÷ amount sold | High ratio (e.g. > 2.5) = oversubscribed |
| **Tail** | Stop-out yield minus the pre-auction "when-issued" yield | Negative or zero tail = strong |
| **Indirect/direct bidder share** | Portion taken by foreign central banks (indirect) vs. domestic non-dealers (direct) | High indirect = healthy foreign appetite |

A "tailing" auction (stop-out well above the when-issued level) signals weak demand and often pressures the broader bond market for the rest of the session. The 35% per-bidder limit on a single auction is the rule [[salomon-brothers|Salomon Brothers]] famously violated in the [[1991-salomon-treasury-auction-scandal|1991 Treasury auction scandal]].

## The Yield Curve

The [[yield-curve]] plots Treasury yields across all maturities and is one of the most important indicators in macro-finance. Under normal conditions, longer maturities offer higher yields to compensate for greater [[interest-rate-risk]] and uncertainty (upward-sloping curve). An **inverted yield curve** -- where short-term rates exceed long-term rates -- has preceded every US recession since the 1960s, typically by 12-18 months. A **flat curve** suggests the market is uncertain about growth and rate direction. The [[federal-reserve|Federal Reserve]] directly controls short-term rates via the fed funds rate, while long-term rates are set by market supply and demand, making the curve a reflection of both monetary policy and market expectations.

## Role in Financial Markets

Treasury yields serve as the foundation for pricing virtually every financial instrument. Corporate bond yields are quoted as a spread over Treasuries of equivalent maturity. Mortgage rates are benchmarked to the 10-year note. The DCF discount rate, equity risk premiums, and WACC calculations all begin with the risk-free rate. When Treasury yields move, the repricing ripples across stocks, real estate, and credit markets globally. During periods of market stress, investors flee to Treasuries as a safe haven ("flight to quality"), pushing bond prices up and yields down. This inverse relationship between Treasury prices and yields is central to understanding [[interest-rate-risk]].

## Monetary Policy Transmission

The [[federal-reserve|Federal Reserve]] uses Treasuries as the primary vehicle for monetary policy. Open market operations (buying/selling Treasuries) inject or drain reserves from the banking system. During quantitative easing (QE), the Fed purchased trillions of dollars in Treasuries to push long-term yields lower and stimulate the economy. During quantitative tightening (QT), the Fed allows its Treasury holdings to mature without reinvestment, reducing the money supply and putting upward pressure on yields. The scale of Fed intervention in the Treasury market has grown dramatically since the 2008 financial crisis, raising questions about whether market-determined price discovery still functions normally in the world's most important bond market.

## Duration and the Price-Yield Mechanics

Treasury prices move inversely to yields, and the *magnitude* of that move is governed by **duration**. Two terms matter:

- **Macaulay duration** — the weighted-average time to receive the bond's cash flows, expressed in years.
- **Modified duration** — the percentage price change for a 1% (100 bp) change in yield: `%ΔPrice ≈ −ModifiedDuration × Δyield`.
- **Convexity** — the second-order correction: as yields fall, prices rise *more* than duration alone predicts, and as yields rise, prices fall *less*. Convexity is a benefit to the bondholder and grows with maturity and lower coupons.

### Worked example: a 1% rate shock

Consider a hypothetical 10-year T-note with a modified duration of ~8.5. If yields rise by 1 percentage point:

`%ΔPrice ≈ −8.5 × 1.0% ≈ −8.5%`

The note loses roughly 8.5% of its market value, partially offset by a small positive convexity term. A 30-year bond (duration ~17–19) would lose roughly twice as much, while a 3-month T-bill (duration ~0.25) loses well under 1%. This is why moving "down the curve" into bills is the standard defensive move when rising rates are expected, and why long Treasuries are a high-octane way to express a recession/rate-cut view. The 2022 bond bear market — when 10-year yields roughly doubled — inflicted double-digit losses on long-duration funds precisely through this mechanism.

## How Traders and Allocators Use Treasuries

| Use case | Instrument / expression | Rationale |
|---|---|---|
| **Risk-free benchmark** | T-bill / SOFR-adjacent rate | Discount rate for DCF, starting point for WACC and the [[risk-free-rate]] |
| **Safe-haven / flight-to-quality** | Long notes & bonds, futures | Bid up in crises; classic equity-drawdown hedge (pre-2022) |
| **Macro rate view** | Move along the curve; extend/shorten [[duration]] | Long duration for cuts/recession, short for hikes |
| **Curve view** | Steepeners / flatteners (e.g. 2s10s) | Trade the *shape* without taking outright level risk |
| **Inflation view** | TIPS vs. nominals (breakeven trade) | The nominal–TIPS yield gap is the market's inflation expectation |
| **Carry / financing** | Repo market, on-the-run/off-the-run basis | [[on-off-the-run-treasury-arbitrage|Relative-value]] trades; the playbook of [[salomon-brothers]] and [[ltcm|LTCM]] |
| **Leverage / hedging** | Treasury futures (ZT, ZF, ZN, ZB, UB) | Capital-efficient duration; the "basis trade" links cash and futures |

The most-watched single number in global finance is the **10-year Treasury yield**, which anchors mortgage rates, corporate-bond spreads, and equity valuations. The **2s10s spread** (10-year minus 2-year) is the canonical recession gauge.

## Risks and Pitfalls

Treasuries are free of *credit* risk in nominal terms (the US can always print the dollars it owes) but are far from riskless overall:

- **Interest-rate / duration risk** — the dominant risk. Long bonds can lose 20%+ when yields rise sharply, as 2022 demonstrated.
- **Inflation risk** — nominal Treasuries pay back fixed dollars; high inflation erodes real value. TIPS hedge this; nominals do not.
- **Reinvestment risk** — coupons and maturing principal may have to be reinvested at lower yields.
- **Stock-bond correlation regime risk** — the negative equity-bond correlation that made the 60/40 portfolio work for two decades flipped *positive* in 2022, when both fell together under the inflation shock. Allocators can no longer assume Treasuries will rally when equities fall.
- **Supply / fiscal risk** — ballooning [[us-debt]] means ever-larger auctions; a weak auction or a downgrade (S&P 2011, Fitch 2023) can lift the term premium. This is the channel through which Fred's "Treasury crisis" thesis operates.
- **Liquidity-event risk** — even the deepest market can seize, as in the March 2020 "dash for cash" when Treasuries sold off alongside risk assets until the Fed intervened.

## Related

- [[bonds]] — broader overview of fixed-income instruments
- [[interest-rate-risk]] — the risk that rate changes affect bond prices
- [[yield-curve]] — the term structure of Treasury rates
- [[us-debt]] — the growing national debt that Treasuries fund
- [[federal-reserve]] — the central bank that manages monetary policy via Treasuries

## Portfolio Relevance

In multi-asset portfolios, Treasuries traditionally serve three roles: the **risk-free anchor** for asset pricing, a **diversifier** whose returns were negatively correlated with equities for most of 1998-2021 (the classic 60/40 ballast), and a **liquidity reserve** that can be sold in a crisis to rebalance into cheap risk assets. That stock-bond correlation flipped positive in 2022 when both fell together under the inflation shock -- a regime that undermined the diversification case and forced allocators to reconsider whether long Treasuries still hedge equity drawdowns or merely add [[interest-rate-risk]]. Duration is the key control variable: a 10-year note has roughly 8-9 years of duration, meaning a 1% yield rise produces an ~8-9% price loss, while T-bills carry near-zero duration. Practitioners express macro views by moving along the curve (shortening duration when they expect rising rates, extending when they expect cuts or recession) and by trading curve shape (steepeners/flatteners) rather than outright level.

## Sources

- US Department of the Treasury, *TreasuryDirect* — security types, auction mechanics, and outstanding balances.
- Federal Reserve, *Selected Interest Rates (H.15)* and FRED — historical Treasury yields and the yield curve.
- Estrella, A. and Mishkin, F. S. (1996). *"The Yield Curve as a Predictor of U.S. Recessions."* Federal Reserve Bank of New York, *Current Issues in Economics and Finance* 2 (7). (yield-curve inversion as recession signal)
- Ilmanen, A. (2011). *Expected Returns.* Wiley. (term premium, duration, and the role of bonds in portfolios)
