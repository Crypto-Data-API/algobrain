---
title: "TLT (iShares 20+ Year Treasury Bond ETF)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [stocks, bonds, treasuries, etf, options, derivatives]
aliases: ["TLT ETF", "iShares 20+ Year Treasury Bond ETF", "Long Bond ETF"]
related: ["[[spy]]", "[[ief]]", "[[options-concentration-risk]]", "[[treasuries]]", "[[duration]]", "[[vix-futures]]", "[[move-index]]"]
---

TLT is the iShares 20+ Year Treasury Bond ETF, issued by [[blackrock|BlackRock]] under the iShares brand. It tracks the ICE U.S. Treasury 20+ Year Bond Index, holding a weighted basket of US Treasury securities with remaining maturities greater than twenty years. TLT is the standard listed instrument for expressing views on the long end of the US yield curve and the most heavily traded long-duration Treasury vehicle in the world.

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | TLT |
| **Underlying** | ICE U.S. Treasury 20+ Year Bond Index |
| **Issuer** | BlackRock (iShares) |
| **Structure** | Open-end ETF |
| **Inception** | July 22, 2002 |
| **Expense ratio** | 0.15% |
| **AUM** | approximately $50-60B (as of early 2026) |
| **Avg daily volume** | approx 30-50M shares/day |
| **Effective duration** | ~16-17 years |
| **Options liquidity** | Very deep — among the most liquid bond ETF options |
| **Dividend** | Monthly distribution, yield tracks long-bond coupon |

## What It Holds

TLT holds a market-value-weighted basket of US Treasury bonds with remaining maturity greater than twenty years — the longest-maturity bucket of the [[treasuries|Treasury]] curve. There is no credit risk (these are direct US government obligations); the entire return and risk profile is driven by **interest-rate** movements at the long end. Because TLT only holds the 20+ year bucket, it is the purest listed expression of long-end [[duration]]. As bonds age below the 20-year threshold they roll out of the index, keeping the fund's maturity (and thus its very long duration) roughly constant over time.

## How Price Moves Inverse to Yields

Bond prices and yields move inversely: when long-end Treasury yields rise, the fixed coupons of existing long bonds become less attractive, so their prices fall — and TLT falls with them. When yields fall (e.g. in a recession scare or a dovish [[interest-rates|Fed]] pivot), long-bond prices rise and TLT rallies. Because TLT holds only very long-maturity bonds, a given change in yield produces an outsized change in price. This is why TLT trades almost mechanically off the [[interest-rates|long-end interest-rate]] outlook — inflation prints, Fed guidance, and Treasury supply/auction dynamics are its primary fundamental drivers, not earnings or growth.

## Duration and Rate Sensitivity

TLT's effective duration sits around 16-17 years, making it one of the most rate-sensitive listed instruments retail traders can access. Approximate price moves per 100bp shift in 20yr+ Treasury yields:

- +100bp yield rise → roughly -15% to -17% price move
- -100bp yield fall → roughly +15% to +17% price move

This convexity makes TLT a high-beta vehicle for any rates view. The 2022 drawdown (Fed hiking cycle) saw TLT lose nearly 50% from its 2020 highs — comparable to a major equity bear market — purely from duration mechanics.

### Convexity

Duration is only the first-order (linear) sensitivity; **convexity** is the second-order curvature. Because TLT's duration is so long, its convexity is meaningful: price gains from falling yields are slightly larger than the equivalent price losses from rising yields (the price-yield curve bows favorably for the holder). In practice this means the simple "duration × yield change" rule understates the upside of a big rally and overstates the downside of a big sell-off — but only modestly. For day-to-day moves, the ~16-17 year duration is the dominant driver.

## Portfolio Hedge / 60-40 Ballast Role

Long-duration Treasuries are the classic equity hedge and the "ballast" leg of a [[60-40-portfolio|60/40 portfolio]]. The thesis: in a growth scare or risk-off shock, investors flee to the safety of US Treasuries, yields fall, and long-bond prices rise — offsetting equity losses. TLT is the most direct retail vehicle for that ballast because its long duration delivers the largest price response per unit of yield decline. The relationship rests on the [[stock-bond-correlation|stock-bond correlation]] being negative — which holds in deflationary/growth-scare regimes but **breaks in inflationary regimes** (see 2022 below), the central caveat for anyone using TLT as a hedge.

## The 2022 Drawdown and Rate-Cycle Behavior

2022 is the defining cautionary episode. As the Fed hiked aggressively to fight inflation, both stocks and long bonds fell together — TLT lost roughly half its value from its 2020 highs while equities also fell, so the bond "ballast" failed exactly when 60/40 holders needed it. The lesson: TLT only hedges equities when the [[stock-bond-correlation|stock-bond correlation]] is negative (deflationary growth scares), not when the shock is an inflation/rate shock that hits both asset classes. The correlation reasserted itself in the 2023-2024 recession scares (when TLT rallied on risk-off), illustrating that TLT's hedge value is regime-dependent. Across the rate cycle, TLT behaves like a leveraged bet on the long-end yield path: brutal in a hiking cycle, powerful in a cutting cycle.

## Options on TLT

TLT hosts the deepest options market of any bond ETF:

- **Weekly expirations** available
- **Strike granularity** — $1 increments near ATM
- **American-style**, physical settlement
- **IV regime** — TLT realized vol typically runs 12-18% annualized in normal regimes, 20-30%+ during rate-policy stress (2022, 2023 SVB)
- **Skew** — modest put skew; less pronounced than equity index skew because rate moves are more symmetric

TLT options IV correlates strongly with the [[move-index|MOVE index]] (Treasury implied vol), making TLT options a retail-accessible proxy for trading rate vol.

## Peer / Related Comparison

The Treasury-ETF complex spans the curve from ultra-short to ultra-long. TLT sits at the long-end extreme; the rest of the family trades off the same rate driver with progressively different durations.

| ETF | Curve segment | Approx duration | Role vs TLT |
|---|---|---|---|
| **TLT** | 20+ year | ~16-17 yr | The long-end benchmark; deepest options market |
| [[ief]] | 7-10 year | ~7.5-8 yr | Intermediate "belly"; ~half TLT's duration; the standard curve-trade counterpart |
| SHY | 1-3 year | ~1.8 yr | Short end; minimal rate sensitivity, near-cash |
| IEI | 3-7 year | ~4.5 yr | Lower belly; calmer than IEF |
| TLH | 10-20 year | ~11-12 yr | Sits between IEF and TLT on duration |
| GOVT | Broad (all maturities) | ~6 yr | Whole-curve Treasury exposure in one fund |
| EDV | STRIPS, 20-30 yr | ~24 yr | Zero-coupon long Treasuries — even more duration/convexity than TLT |
| ZROZ | STRIPS, 25+ yr | ~27 yr | The most extreme listed Treasury duration; a leveraged-feeling rate bet |

[[tlt|TLT]] vs [[ief|IEF]] is the canonical retail curve trade (long-end vs belly); EDV/ZROZ are for traders who want *more* duration than TLT, while SHY/IEI/GOVT step down the risk for those who want less.

## Trading Uses

- **Directional rates view** — long TLT to express a view that long yields fall (recession, dovish Fed); short TLT for the reverse
- **Equity hedge** — historically, TLT has offered negative correlation to [[spy|SPY]] during risk-off events; this relationship broke in 2022 when both fell together but reasserted in 2023-2024 recession scares
- **Vol overlay** — short TLT premium provides exposure to rate vol, which is a different vol regime than equity vol
- **Curve trades** — TLT vs [[ief|IEF]] (7-10yr) expresses curve steepening/flattening views
- **Carry trade** — owning TLT collects coupon income while market-makers in short-dated TLT options harvest premium

## How It Trades vs Equities

TLT's relationship to equities is the heart of its portfolio role and is governed by the [[stock-bond-correlation|stock-bond correlation]]:

- In **deflationary / growth-scare** regimes, equities fall and Treasuries rally (negative correlation) — TLT is a genuine hedge for [[spy|SPY]]/[[qqq|QQQ]].
- In **inflationary / rate-shock** regimes (2022), both fall together (positive correlation) — TLT amplifies rather than offsets equity losses.
- The shared macro driver is the [[interest-rates|rate cycle]]: rising real rates pressure both long bonds and equity valuations (especially long-duration growth/tech), which is why TLT and [[qqq|QQQ]] can sell off together when real yields spike.

This regime dependence is the single most important thing to understand before using TLT as portfolio ballast.

## Concentration Risk Angle

[[options-concentration-risk]] explicitly recommends rate vol as one of the key asset classes for diversifying a short premium book. A trader running short premium across [[spy]], [[qqq]], [[xlk]], and single-name tech is 100% loaded on equity vol — a single VIX spike hits every line item simultaneously.

Adding short premium on TLT introduces a vol regime that is *correlated but distinct*:

- TLT vol is driven by Fed policy expectations, inflation prints, and Treasury supply dynamics
- Equity vol is driven by earnings, growth expectations, and risk appetite
- The two share a macro driver (rate cycle) but diverge meaningfully day-to-day

TLT short premium typically harvests 2-4 vol points of [[volatility-risk-premium|VRP]] (similar magnitude to equity index VRP), but the realized correlation between TLT VRP P&L and SPY VRP P&L is meaningfully below 1, providing genuine diversification at the book level.

## Key Relationships

- **TLT vs IEF**: TLT has roughly 2x the duration of [[ief|IEF]]; the ratio is the standard curve trade
- **TLT vs SPY**: traditionally negative correlation (-0.3 to -0.5 in normal regimes); broke in 2022 (both fell together as Fed hiked into inflation)
- **TLT vs DXY**: complex; rising real rates often strengthen the [[us-dollar|dollar]] and pressure TLT simultaneously
- **TLT vs MOVE**: TLT realized vol tracks the [[move-index|MOVE index]]; spikes in MOVE coincide with TLT IV expansion

## Risks

- **Duration risk** — the dominant risk; a sustained rise in long-end yields drives large drawdowns (2022 saw ~50% from the highs).
- **Inflation regime risk** — TLT's hedge value fails in inflationary shocks, exactly when 60/40 holders rely on it.
- **Rate-vol risk** — sharp [[move-index|MOVE]] spikes whipsaw both the shares and options.
- **Supply / fiscal risk** — heavy Treasury issuance and term-premium repricing can push long yields up independent of the Fed.
- **No credit risk** — these are US government bonds, so default risk is not a factor; the risk is entirely rate-driven.
- **Negative-correlation breakdown** — the stock-bond hedge is regime-dependent and not guaranteed.

## Sources

- BlackRock iShares official fund documentation
- ICE U.S. Treasury 20+ Year Bond Index methodology
- CBOE options volume statistics

## Related

- [[ief]] — 7-10yr Treasury ETF, the intermediate-duration counterpart
- [[treasuries]] — underlying asset class
- [[bonds]] — the broader fixed-income context
- [[duration]] — the mechanic driving TLT's price sensitivity
- [[interest-rates]] — the macro driver of TLT's price
- [[stock-bond-correlation]] — governs TLT's value as an equity hedge
- [[60-40-portfolio]] — TLT as the bond-ballast leg
- [[move-index]] — Treasury implied vol benchmark
- [[options-concentration-risk]] — TLT as the rate-vol diversifier
- [[spy]] — equity counterpart for risk-on/risk-off pair trades
- [[vix-futures]] — equity vol benchmark; TLT options are the rate-vol analog
