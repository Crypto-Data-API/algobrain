---
title: "IEF (iShares 7-10 Year Treasury Bond ETF)"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [stocks, bonds, treasuries, etf, options, derivatives]
aliases: ["IEF ETF", "iShares 7-10 Year Treasury Bond ETF", "Intermediate Treasury ETF"]
related: ["[[tlt]]", "[[spy]]", "[[options-concentration-risk]]", "[[treasuries]]", "[[duration]]", "[[move-index]]"]
---

IEF is the iShares 7-10 Year Treasury Bond ETF, issued by [[blackrock|BlackRock]] under the iShares brand. It tracks the ICE U.S. Treasury 7-10 Year Bond Index, holding US Treasuries with remaining maturities between seven and ten years. IEF is the listed proxy for the intermediate belly of the Treasury curve — the segment most directly tied to the 10-year yield, which serves as the global benchmark risk-free rate.

## Key Facts

| Metric | Value |
|--------|-------|
| **Ticker** | IEF |
| **Underlying** | ICE U.S. Treasury 7-10 Year Bond Index |
| **Issuer** | BlackRock (iShares) |
| **Structure** | Open-end ETF |
| **Inception** | July 22, 2002 |
| **Expense ratio** | 0.15% |
| **AUM** | approximately $30-35B (as of early 2026) |
| **Avg daily volume** | approx 8-15M shares/day |
| **Effective duration** | ~7.5-8 years |
| **Options liquidity** | Moderate; far less deep than [[tlt|TLT]] |
| **Dividend** | Monthly distribution |

## What It Holds

IEF holds a market-value-weighted basket of US [[treasuries|Treasury]] notes with remaining maturity between seven and ten years — the intermediate "belly" of the curve. Like all Treasury ETFs it carries no credit risk; its return and risk are driven entirely by [[interest-rates|interest-rate]] moves, specifically in the segment anchored to the **10-year yield**, the global benchmark risk-free rate. As notes age below the seven-year threshold they roll out of the index, keeping the fund's maturity and duration roughly constant. Because it targets the belly rather than the long end, IEF tracks the 10-year more cleanly than [[tlt|TLT]] tracks any single point on the curve.

## How Price Moves Inverse to Yields

As with all bonds, IEF's price moves inversely to yields: when 10-year Treasury yields rise, the prices of the intermediate notes IEF holds fall, and IEF falls with them; when yields fall (recession scare, dovish [[interest-rates|Fed]]), IEF rallies. Because IEF's duration (~7.5-8 years) is roughly half [[tlt|TLT]]'s, the price response to a given yield move is about half as large — IEF is the calmer, cleaner expression of the same rate driver, without the convexity whipsaws of the long bond.

## Duration and Rate Sensitivity

IEF's effective duration sits near 7.5-8 years, roughly half that of [[tlt|TLT]]. Approximate price moves per 100bp shift in 10-year yields:

- +100bp yield rise → roughly -7% to -8% price move
- -100bp yield fall → roughly +7% to +8% price move

The reduced duration makes IEF a calmer instrument than TLT, with realized vol typically 8-12% annualized versus TLT's 15-20%. For traders who want rate exposure without the convexity whipsaws of the long bond, IEF is the standard choice.

### Convexity

IEF has positive convexity like any vanilla bond fund, but because its duration is moderate, the second-order curvature is small relative to [[tlt|TLT]]'s. In practice the simple "duration × yield change" approximation is quite accurate for IEF across normal yield moves — there is far less of the asymmetric "rally faster than it sells off" behavior that the very-long-duration funds (TLT, EDV, ZROZ) exhibit. This makes IEF a more linear, predictable rate instrument.

## IEF vs TLT

| Feature | IEF | TLT |
|---------|-----|-----|
| **Duration** | ~7.5-8yr | ~16-17yr |
| **Realized vol** | 8-12% | 15-20% |
| **Options liquidity** | Moderate | Very deep |
| **Curve segment** | Intermediate (10yr proxy) | Long end (20yr+ proxy) |
| **Best for** | Cleaner rate view, lower vol | High-conviction directional, vol trading |

The IEF/TLT ratio is the canonical retail-accessible curve trade: long IEF / short TLT bets on a steepening curve (10yr falls relative to 20yr+); the reverse bets on flattening or inversion.

## Peer / Related Comparison

IEF sits in the middle of the Treasury-ETF complex — more duration than the short-end funds, far less than the long bond. All trade off the same [[interest-rates|rate]] driver with progressively different durations.

| ETF | Curve segment | Approx duration | Role vs IEF |
|---|---|---|---|
| **IEF** | 7-10 year | ~7.5-8 yr | The intermediate "belly"; cleanest 10-year proxy |
| [[tlt]] | 20+ year | ~16-17 yr | Long end; ~2x IEF's duration; the standard curve-trade counterpart |
| SHY | 1-3 year | ~1.8 yr | Short end; near-cash, minimal rate sensitivity |
| IEI | 3-7 year | ~4.5 yr | Lower belly; a step down in duration from IEF |
| TLH | 10-20 year | ~11-12 yr | Sits between IEF and TLT on the curve |
| GOVT | Broad (all maturities) | ~6 yr | Whole-curve Treasury exposure in one fund |
| EDV | STRIPS, 20-30 yr | ~24 yr | Zero-coupon long Treasuries — far more duration/convexity |
| ZROZ | STRIPS, 25+ yr | ~27 yr | The most extreme listed Treasury duration |

[[ief|IEF]] vs [[tlt|TLT]] is the canonical retail curve trade (belly vs long-end). IEI/SHY step down to lower duration for those who want less rate risk than IEF; TLH/EDV/ZROZ step up for those who want more.

## Portfolio Hedge / 60-40 Ballast Role

IEF is a natural "40% bonds" sleeve in a modernized [[60-40-portfolio|60/40 portfolio]]: it provides Treasury ballast against equity drawdowns with materially less interest-rate risk than [[tlt|TLT]]. Many practitioners prefer intermediate Treasuries to the long bond for ballast precisely because the lower duration reduces the catastrophic-drawdown risk that hit long-bond holders in 2022, while still delivering a flight-to-quality rally in genuine growth scares. As with TLT, the hedge value depends on the [[stock-bond-correlation|stock-bond correlation]] being negative — it works in deflationary/growth-scare regimes and weakens in inflationary/rate-shock regimes.

## The 2022 Drawdown and Rate-Cycle Behavior

IEF also fell in 2022 as the Fed hiked aggressively, but its drawdown was far milder than [[tlt|TLT]]'s because its duration is roughly half — the ~7.5-8 year duration translated a sharp rise in yields into a single-digit-to-mid-teens decline rather than TLT's ~50%-from-the-highs collapse. This is the practical argument for IEF as 60/40 ballast: it still failed to hedge equities in the 2022 inflation shock (both fell together, the [[stock-bond-correlation|correlation flipped positive]]), but it did far less damage. Across the rate cycle IEF behaves like a lower-octane version of TLT: it rallies on Fed-cut pricing in recession scares (as in 2023-2024) and sells off in hiking cycles, with about half the amplitude.

## Options on IEF

IEF options exist but are far less liquid than TLT options. Bid-ask spreads are wider, strike granularity is coarser, and 0DTE products are not available. For most retail vol overlays, [[tlt|TLT]] is the preferred vehicle for actively traded rate-vol structures; IEF is more often used buy-and-hold for portfolio duration matching.

## Trading Uses

- **Pure rate view** — IEF gives a cleaner expression of 10yr yield direction without the convexity noise of TLT
- **Curve steepener/flattener** — long IEF / short TLT, or vice versa, expresses curve shape views
- **60/40 portfolio sleeve** — IEF is the standard "40% bonds" component in modernized 60/40 retail portfolios; serves as ballast against [[spy|SPY]] drawdowns
- **Macro pair trade** — long IEF / short SPY expresses recession / risk-off positioning
- **Defensive rotation** — when growth expectations weaken, intermediate Treasuries rally as the market prices Fed cuts

## How It Trades vs Equities

IEF's relationship to equities is governed by the [[stock-bond-correlation|stock-bond correlation]], the same regime-dependent dynamic as [[tlt|TLT]] but with smaller absolute moves:

- In **deflationary / growth-scare** regimes, equities fall and intermediate Treasuries rally (negative correlation) — IEF is a milder hedge for [[spy|SPY]]/[[qqq|QQQ]].
- In **inflationary / rate-shock** regimes (2022), both fell together (positive correlation), though IEF's lower duration limited the damage.
- The shared driver is the [[interest-rates|rate cycle]]: rising real yields pressure both intermediate Treasuries and equity valuations, especially long-duration growth/tech ([[qqq|QQQ]]).

Because of its lower duration, IEF is the gentler ballast — less hedging power in a deflationary scare, but less downside risk in a rate shock.

## Concentration Risk Angle

[[options-concentration-risk]] flags rate vol as a key diversifier for short premium books concentrated in equity vol. While [[tlt|TLT]] is the more common short-premium vehicle (better liquidity), IEF serves the same role for traders who prefer the lower-duration, lower-vol exposure profile.

A short premium book that is 100% equity-loaded (SPY, QQQ, single-name) shares one fundamental driver: equity risk premium and equity implied vol. Adding even a modest IEF or TLT short premium sleeve introduces a different macro factor — Fed reaction function and inflation expectations — with imperfect correlation to equity vol regimes.

For a smaller account where TLT options' notional sizing is too large, IEF's lower share price and tighter realized vol can make position sizing easier. The vol regime exposure is structurally similar.

## Key Relationships

- **IEF vs TLT**: roughly 0.85+ correlated daily; the IEF/TLT spread is a curve trade
- **IEF vs SPY**: typically negative correlation in risk-off regimes; broke in 2022
- **IEF vs DXY**: similar dynamic to TLT — rising real rates pressure both bonds and equity multiples
- **IEF vs MOVE**: tracks rate vol but with smaller absolute price moves than TLT

## Risks

- **Duration risk** — the dominant risk, though roughly half [[tlt|TLT]]'s; a sustained rise in 10-year yields drives drawdowns.
- **Inflation regime risk** — IEF's hedge value weakens in inflationary shocks (2022), when both stocks and bonds fall.
- **Rate-vol risk** — [[move-index|MOVE]] spikes move IEF, though less violently than TLT.
- **Supply / fiscal risk** — heavy Treasury issuance and term-premium repricing can lift intermediate yields.
- **No credit risk** — US government bonds carry no default risk; the risk is entirely rate-driven.
- **Negative-correlation breakdown** — the equity hedge is regime-dependent and not guaranteed.

## Sources

- BlackRock iShares official fund documentation
- ICE U.S. Treasury 7-10 Year Bond Index methodology
- CBOE options market data

## Related

- [[tlt]] — long-end Treasury ETF, the duration-leveraged counterpart
- [[treasuries]] — underlying asset class
- [[bonds]] — the broader fixed-income context
- [[duration]] — the mechanic driving IEF's rate sensitivity
- [[interest-rates]] — the macro driver of IEF's price
- [[stock-bond-correlation]] — governs IEF's value as an equity hedge
- [[60-40-portfolio]] — IEF as the bond-ballast leg
- [[options-concentration-risk]] — IEF as a rate-vol diversifier
- [[move-index]] — Treasury implied vol benchmark
- [[spy]] — equity counterpart for risk-on/risk-off pair trades
