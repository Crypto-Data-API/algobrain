---
title: "Bonds Overview"
type: index
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [bonds, markets, index]
related: ["[[bond-market]]", "[[corporate-bonds]]", "[[treasury-bonds]]", "[[treasuries]]", "[[yield-curve]]", "[[duration]]", "[[credit-spread]]", "[[credit-risk]]", "[[interest-rate-risk]]", "[[lqd]]", "[[hyg]]"]
---

# Bonds Overview

Fixed-income markets -- government bonds, corporate debt, yield curves, and interest-rate dynamics. A **bond** is a tradable loan: the investor lends principal to a government or company and receives periodic interest (the coupon) plus repayment of principal at maturity. The [[bond-market]] is larger than the global equity market (an estimated $130+ trillion outstanding) and serves as the foundation of the financial system -- government-bond yields set the **risk-free rate** that prices every other asset.

## Why Bonds Matter for Every Trader

Understanding fixed-income basics -- coupon payments, [[duration]], [[credit-spread|credit spreads]], and the inverse relationship between bond prices and yields -- is essential even for equity and crypto traders, because interest-rate movements ripple across all markets. The [[yield-curve]] is one of the most-watched macro indicators: an inverted curve has preceded every US recession for the past ~50 years. Bonds also anchor [[portfolio-construction|portfolio construction]] as a diversifier and a source of income.

## Bond Vocabulary in One Paragraph

A bond's **face (par) value** is the principal repaid at **maturity**. The **coupon** is the fixed (or floating) annual interest, quoted as a percent of par. The **yield to maturity (YTM)** is the single discount rate that makes the present value of all coupons plus principal equal the current market **price** — it is the bond's internal rate of return if held to maturity, and it moves *inversely* to price. The **credit rating** (AAA down to D, from agencies like S&P, Moody's, Fitch) summarizes [[credit-risk|default risk]], and the [[credit-spread]] is the extra yield over a same-maturity Treasury that compensates for that risk.

## Types of Bonds

| Type | Issuer | Key risk | Notes |
|------|--------|----------|-------|
| **Treasury bills / notes / bonds** ([[treasuries]]) | US government | [[interest-rate-risk]] (≈no default risk) | Bills ≤1yr (zero-coupon), notes 2–10yr, bonds 20–30yr; set the [[risk-free-rate]] |
| **TIPS** | US government | Real-rate risk | Principal indexed to CPI — inflation protection |
| **Agency / MBS** | GSEs (Fannie, Freddie, Ginnie) | Prepayment + rate risk | Mortgage cash flows; negative convexity |
| **Municipal bonds** | US states / cities | Credit + rate risk | Often tax-exempt interest |
| **Investment-grade corporates** ([[corporate-bonds]]) | Companies rated BBB-/Baa3+ | Credit + rate risk | Tracked by ETFs like [[lqd]] |
| **High-yield ("junk")** | Companies rated BB+/Ba1 and below | Credit risk dominant | Higher coupon; tracked by [[hyg]] |
| **Sovereign / EM debt** | Foreign governments | Credit + currency risk | USD- or local-currency denominated |
| **Floating-rate notes** | Govt / corporate | Credit risk (low duration) | Coupon resets to a reference rate |
| **Convertibles** | Companies | Hybrid equity/credit | Bond that converts to equity |

Two cross-cutting dimensions organize the table: **maturity/duration** (how much [[interest-rate-risk]]) and **credit quality** (how much [[credit-risk]]). Treasuries are nearly pure rate risk; high-yield is mostly credit risk; investment-grade corporates carry a meaningful dose of both.

## Duration, Yield, and Credit Explained

- **Yield (price ↔ yield inverse).** A bond paying a \$50 coupon on \$1,000 par yields 5%. If market rates rise to 6%, new buyers demand the same 6%, so the old bond's price must *fall* (to roughly \$833 in the perpetual-bond limit) to lift its effective yield. This inverse mechanism is the engine of all bond price moves.
- **Duration (rate sensitivity).** Modified duration estimates the percentage price change for a 1-percentage-point change in yield: `ΔPrice% ≈ −Duration × Δyield`. A bond with duration 7 loses ~7% if yields rise 1%, and gains ~7% if they fall 1%. Longer maturity and lower coupon both raise duration. **Convexity** is the second-order correction that makes the real curve gentler than this linear estimate. See [[duration]].
- **Credit spread (default compensation).** The [[credit-spread]] is the yield gap over a matched Treasury. It *widens* in stress (recession fears, rising defaults) and *tightens* in calm. A 10-year IG corporate yielding 5.5% against a 4.2% Treasury carries a 130 bps spread. Spread widening can hurt a corporate bond even when Treasury yields are falling — the [[lqd]] page illustrates this rate-vs-credit decomposition.

### Worked example: a +1% rate shock

A portfolio holds \$1,000,000 of bonds with a portfolio duration of 6.5. If yields jump 1% (100 bps) across the curve, the first-order price impact is `−6.5 × 1% × \$1,000,000 = −\$65,000` (a ~6.5% drawdown), partly cushioned by positive convexity. This single calculation is why duration is the primary risk lever fixed-income managers control.

## Key Sub-Topics

| Page | What it covers |
|------|----------------|
| [[bond-market]] | Market structure: segments, primary vs secondary, how bonds trade, links to other assets |
| [[treasury-bonds]] | US government debt -- the "risk-free" benchmark (bills, notes, bonds) |
| [[corporate-bonds]] | Company debt -- investment grade vs high yield, ratings, default risk, bond structures |
| [[yield-curve]] | The term structure of rates and its power as a recession signal |
| [[duration]] | How sensitive a bond's price is to interest-rate changes |
| [[credit-spread]] | The yield premium over Treasuries that compensates for default risk |

## Core Mechanics in One Glance

- **Price ↔ yield are inverse** -- when yields rise, existing bond prices fall.
- **Duration = rate risk** -- a duration of 7 means ~7% price loss per +1% in yields.
- **Credit spread = default risk** -- widens in stress, tightens in calm.
- **Yield curve = the macro signal** -- inversion warns of recession.

## How Traders Use Bonds

- **The macro dashboard.** Even pure equity and crypto traders watch the 10-year Treasury yield, the [[yield-curve]] slope (2s10s), and IG/HY [[credit-spread|spreads]] as leading indicators of liquidity and risk appetite. Widening credit spreads frequently lead equity drawdowns.
- **Portfolio ballast.** A classic 60/40 stock/bond mix uses bonds as a diversifier; the historically negative stock-bond correlation can break down in inflation shocks (e.g. 2022), when both fell together.
- **Expressing rate views.** Traders go long duration (long-dated Treasuries or [[treasuries|TLT]]) to bet rates fall, or short duration to bet they rise, without single-name selection.
- **Carry and relative value.** Curve trades (steepeners/flatteners), credit-vs-rates trades (long [[lqd]] vs short Treasury futures to isolate spread), and IG-vs-HY trades ([[lqd]] vs [[hyg]]) decompose the bond market into independent risk factors.
- **Liquidity proxies.** Bond ETFs trade continuously while many underlying bonds trade rarely, so ETFs like [[lqd]] and [[hyg]] are watched for real-time price discovery during stress.

## Common Pitfalls and Risks

- **"Bonds are safe" is half-true.** Default-free Treasuries still carry [[interest-rate-risk]] — long-duration Treasuries fell ~30%+ in 2022. Safety from default is not safety from rate moves.
- **Ignoring duration.** Reaching for yield by extending maturity quietly piles on rate risk; a small yield pickup can be erased by a modest rate rise.
- **Reinvestment and call risk.** Falling rates reduce the yield on reinvested coupons; callable bonds get redeemed exactly when rates fall, capping upside.
- **Inflation erosion.** Fixed nominal coupons lose real value when inflation rises; only TIPS and floaters are structurally protected.
- **Liquidity illusion.** During stress, the underlying corporate bond market can freeze even while the ETF keeps trading — producing ETF/NAV basis dislocations (see the March 2020 episode on the [[lqd]] page).

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/markets/bonds"
WHERE type != "index"
SORT updated DESC
```

## Related

- [[bond-market]] — market structure and how bonds trade
- [[treasuries]] / [[treasury-bonds]] — the risk-free benchmark
- [[corporate-bonds]] — IG vs high-yield company debt
- [[yield-curve]] — the term structure and recession signal
- [[duration]] — interest-rate sensitivity
- [[credit-spread]] / [[credit-risk]] — default-risk compensation
- [[interest-rate-risk]] — the rate dimension shared by all bonds
- [[lqd]] / [[hyg]] — investment-grade and high-yield ETF proxies

## Sources

- General market knowledge; no specific wiki source ingested yet.
