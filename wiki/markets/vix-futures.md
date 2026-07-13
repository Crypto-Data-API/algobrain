---
title: "VIX Futures"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, volatility, futures, sp500]
aliases: ["VIX Futures", "VX Futures", "Volatility Futures", "CBOE VIX Futures"]
related: ["[[vix]]", "[[vix-calls]]", "[[long-vol-vs-short-vol]]", "[[xiv-velocity-shares]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[contango]]", "[[backwardation]]", "[[variance-swaps]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[short-vol]]", "[[span-margin]]", "[[term-structure]]", "[[vxx]]", "[[uvxy]]", "[[svxy]]", "[[roll-yield]]"]
---

**VIX futures** are listed, cash-settled futures contracts on the [[vix|CBOE Volatility Index]], traded on the CBOE Futures Exchange (CFE) under the ticker root **VX**. They are the only liquid, exchange-traded venue for taking direct positional exposure to expected forward S&P 500 implied volatility, and they sit at the center of the listed-vol ecosystem -- VIX options price off VX futures, and short-vol ETPs ([[xiv-velocity-shares|XIV]], [[svxy|SVXY]], [[uvxy|UVXY]], [[vxx|VXX]]) replicate weighted positions in the front two VX contracts.

## Overview

The CBOE launched VIX futures on March 26, 2004, six years before VIX options. The underlying is the VIX index (computed from a [[variance-swaps|variance-swap]]-style replication of 30-day SPX option implied vol), so each VX future represents a forward expectation of where the VIX index will fix at the contract's settlement -- not where SPX realized vol will print, and not where current spot VIX is.

VIX futures are critical because spot VIX is **not directly tradable**. The index is a calculated number; you cannot buy a "share" of VIX. VX futures are the closest thing to a tradable VIX, and every VIX-linked product (options, ETPs, structured products, [[vix-calls|VIX calls]] used for hedging) ultimately references them.

The dominant structural fact about VX futures is that they normally trade in **[[contango]]** -- longer-dated contracts price above shorter-dated, reflecting the market's expectation that vol will mean-revert upward from low spot levels. This produces a persistent **negative roll yield** for long holders and a persistent **positive carry** for short holders, which is the engine that powers the entire short-vol ETP complex (and that destroyed [[xiv-velocity-shares|XIV]] when the regime suddenly inverted).

## Contract Specs

| Specification | Value |
|---|---|
| **Exchange** | CBOE Futures Exchange (CFE), part of [[cboe-global-markets|Cboe]] |
| **Ticker root** | VX (monthly), VX01-VX05 (weekly contracts) |
| **Underlying** | CBOE Volatility Index (VIX) |
| **Contract multiplier** | $1,000 per VIX point |
| **Tick size** | 0.05 VIX points = $50 (front month: 0.01 = $10 in some venues) |
| **Trading hours** | Nearly 24-hour: 8:30am Sun - 3:15pm Fri CT (with brief halt) |
| **Last trading day** | Tuesday before final settlement (if monthly) |
| **Final settlement date** | Wednesday 30 days before next-month SPX option expiry (typically the third Wed) |
| **Settlement** | Cash-settled to a Special Opening Quotation (SOQ) of VIX from SPX option opening prints |
| **Position limits** | None on standard VX (notable in derivatives space) |
| **Margin** | [[span-margin|SPAN]]-based; initial margin typically $8,000-$15,000 in calm regimes, can spike 3-5x in stress |
| **Listed maturities** | 9 monthly contracts continuously, plus 6 weekly contracts (Wednesday expirations) |

A "Mini-VIX" (VXM) contract was launched in **August 2020** with a $100 multiplier (1/10 size of standard VX), targeting smaller and retail accounts. **Weekly VIX futures** were launched July 2015, providing finer-grained tenor exposure for short-dated vol trades and event hedging.

## How It Works

Settlement is the key conceptual quirk. A VX future settling on Wednesday `T` does **not** settle to that day's spot VIX. It settles to the **VIX SOQ**, computed from the opening prices of SPX options expiring 30 calendar days later (the following month's Wednesday-expiry SPX options). The point: a VX future is a forward on the *value* of the VIX index, which is itself a forward measure of vol over the *following* 30 days.

Practical consequences:

- A VX future at 18.50 with two weeks to expiry is saying: "the market expects that 30-day forward implied vol on SPX, measured by the VIX formula, will be 18.50 on the SOQ date."
- The future converges to spot VIX as expiry approaches (because the SOQ window collapses onto the current day).
- VX futures exhibit **declining sensitivity to spot VIX** as you go out the curve. A 5-point spike in spot VIX might move the front month 3 points, the second month 1.5 points, and the back month 0.5 points. This term-structure-driven beta is core to vol trading.

## Term Structure: Contango vs Backwardation

Roughly **80-85% of trading days** since 2004 have featured the VX curve in [[contango]] (longer dates above shorter). The remainder feature [[backwardation]] (shorter dates above longer), which is associated with vol spikes and crisis regimes.

The empirical regimes:

| Regime | Curve shape | Front-month roll cost (annualized) | What it implies |
|---|---|---|---|
| **Steep contango** | M2/M1 > 1.10 | -50% to -100% | Strong complacency; short-vol carry is fat |
| **Mild contango** | M2/M1 between 1.02 and 1.10 | -15% to -50% | Normal regime; baseline short-vol carry |
| **Flat** | M2/M1 between 0.99 and 1.02 | ~0% | Vol about to break; transition zone |
| **Backwardation** | M2/M1 < 0.99 | Positive (long-vol earns) | Crisis regime; short-vol funds bleeding |

Contango exists because spot VIX is mean-reverting, and when spot is below the long-run mean (~19), forwards drift back toward the mean as expiry approaches. The systematic "short the front, roll forward" trade has produced ~20-30% annualized historical Sharpe in calm years -- and total ruin in 1-day blow-ups, as discussed below.

## Roll Yield and the Short-Vol ETPs

Because the curve is normally upward-sloping, **a long-VX-futures position bleeds value as time passes**, even if spot VIX is unchanged. The front future "rolls down" the curve toward spot. The annualized cost depends on curve steepness, and during calm regimes it has been the single largest source of return in the entire vol complex.

Two products embodying the long-vol roll cost:

- **[[vxx|VXX]]** (Barclays / iPath) -- launched January 2009, replicates a constant-30-day-maturity weighted long position in the front two VX contracts. Loses roughly 60-80% per year in calm regimes due to roll cost. Has experienced multiple reverse splits (10:1, 4:1, 4:1...) to keep the share price tradable. The original ETN expired Jan 2019 and was replaced by VXXB (now VXX again).
- **[[uvxy|UVXY]]** (ProShares) -- 1.5x leveraged long version (originally 2x; reduced after February 2018). Loses 80-95% per year in calm regimes; has had multiple 1:5 and 1:10 reverse splits since launch in 2011.

And the mirror short-vol products:

- **[[xiv-velocity-shares|XIV]]** (Credit Suisse VelocityShares) -- short the same front-two-month basket. Returned ~600% in 2017. **Terminated February 5-6, 2018** ([[volmageddon]]) after losing 96% in a single overnight session.
- **[[svxy|SVXY]]** (ProShares) -- originally a -1x of the same basket. After [[volmageddon]] it was rewritten as **-0.5x** (half-leverage) to reduce blow-up risk. Has continued to trade since.

The collapse of XIV and the de-leveraging of SVXY is the seminal post-2018 product-design lesson: a -1x daily-rebalanced ETN on VX futures **cannot survive a +96% one-day move in the underlying basket**, which is exactly what happened on Feb 5, 2018.

## Sensitivities — How VX Futures Respond

Unlike an option, a VX future has no Greeks of its own — it is a linear forward — but its behavior is governed by a distinctive set of sensitivities that every VX trader must internalize:

- **Spot-VIX beta declines down the curve.** As noted under "How It Works," a 5-point spot-VIX spike might move the front month ~3 points, the second ~1.5, and the back ~0.5. The front contract is the most spot-sensitive and the most volatile; the back contract behaves like a slow-moving forward. This curve-dependent beta is the single most important risk parameter for sizing.
- **Roll-down drift.** In [[contango]], a long VX position loses value purely from the future drifting down the curve toward spot as expiry approaches, independent of any spot-VIX move. This is the [[roll-yield|roll yield]] — negative for longs, positive for shorts — and it is the dominant return source in calm regimes.
- **Convergence to the SOQ.** As expiry nears, the future converges to the VIX Special Opening Quotation, collapsing the gap between future and spot. Most of a contract's spot-sensitivity is concentrated in its final weeks.
- **Vol-of-vol ([[implied-volatility|VVIX]]) sensitivity.** VX futures reprice violently when the implied vol *of* VIX spikes — the largest one-day VX percentage moves in history have been VVIX-driven, not driven by SPX spot moves alone (see Risks).
- **No theta, no convexity.** Because the future is linear, it offers none of the convexity of [[vix-calls|VIX calls]] — which is precisely why VX-futures-long products make inferior tail hedges (linear bleed) while VIX options provide the convex payoff tail-hedgers actually want.

## Calendar and Spread Trading

Because the VX curve has a rich, regime-dependent shape, much VX trading is done as **calendar spreads** (long one expiry, short another) rather than outright longs or shorts:

| Structure | Construction | View expressed | Notes |
|---|---|---|---|
| **M1/M2 calendar** | Long front, short second (or reverse) | Slope of the near curve | Short-front/long-second is the classic contango-carry expression |
| **Roll spread** | Short front, long second | Harvest roll-down as front decays to spot | The mechanical trade the short-vol ETPs run continuously |
| **Backwardation reversal** | Long front, short back in a spike | Bet the curve normalizes back to contango | Mean-reversion trade after a vol shock |
| **VX vs SPX-realized** | VX long/short vs delta-hedged SPX options | [[variance-risk-premium\|VRP]] capture | The cleaner institutional VRP expression |
| **Term butterfly** | Long M1 + M3, short 2×M2 | Curvature of the term structure | Sophisticated curve-shape view |

Calendar structures isolate the *slope* of the curve and substantially reduce the outright spot-VIX directional risk, which is why professional vol desks trade the curve far more than they trade outright VX direction. The trade-off is that calendars are still exposed to non-parallel curve shifts — a spike can steepen or flatten the curve in ways that hurt a calendar that looked hedged on a parallel-shift basis. See [[term-structure]], [[contango]], [[backwardation]], and [[roll-yield]].

## Use Cases / Who Trades These

| Participant | Direction | Use |
|---|---|---|
| **Short-vol funds and ETPs** ([[svxy]], retail short-strangle accounts) | Short VX | Harvest [[variance-risk-premium]] and roll yield |
| **Tail-risk hedge funds** ([[universa-investments]], [[longtail-alpha]]) | Long VX (small) and long VIX calls | Crisis-alpha hedge to equity book |
| **Risk-parity / vol-targeting allocators** | Tactical short VX | Vol-targeting overlay |
| **Equity index option market-makers** | Hedging VIX options books | VX is the underlying for VIX options |
| **CTAs / momentum funds** | Long or short based on signal | Vol regime momentum |
| **Macro funds** | Long around known catalysts | Election, FOMC, geopolitical |
| **Bank exotic desks** | Vega offset for variance-swap and structured-product books | Recycling vega from autocallables and reverse convertibles |

The notional volume of VX futures has been a structural part of the SPX options ecosystem since the 2010s -- much of the listed [[variance-risk-premium]] is monetized via short VX rather than directly via short variance swaps, because of cleaner [[span-margin|margining]], central clearing, and tighter spreads.

## How Traders Use VX Futures — Playbook

| Goal | Typical expression | Key risk to manage |
|---|---|---|
| Harvest contango carry | Short front month, roll forward | Open-ended spike risk; size for stress, not calm |
| Hedge an equity book | Small long VX (or prefer [[vix-calls\|VIX calls]] for convexity) | Linear bleed in calm; cheaper to hedge via call spreads |
| Trade the curve, not direction | M1/M2 calendar spread | Non-parallel curve shifts |
| Bet on mean-reversion after a spike | Short VX in backwardation | Spike can extend before reverting |
| Vol-regime momentum (CTA-style) | Long or short on a trend signal | Whipsaw at regime transitions |
| Event hedge (FOMC, election) | Long [[vix-futures\|weekly VX]] into the catalyst | Roll/decay if the event passes quietly |

The recurring discipline across every short-VX use case is the same lesson Volmageddon and August 2024 taught: **size for the stress regime, because the calm regime that makes the carry attractive is exactly the regime that will not last.** Long-vol and tail-hedge users, conversely, should generally prefer convex [[vix-calls|VIX calls]] or call spreads to outright long futures, whose linear bleed makes them a poor standalone hedge.

## Related-Product Comparison

| Vehicle | Wrapper | Tax | Convexity | Best use |
|---|---|---|---|---|
| **VX futures** | Listed future | [[section-1256-contracts\|§1256]] | Linear (none) | Cleanest carry / curve trades; the underlying for everything else |
| **[[vix-calls\|VIX options]]** | Listed option | §1256 | Convex | Tail hedging; nonlinear vol bets |
| [[vxx\|VXX]] | ETN (long) | Equity | Linear bleed | Tactical long-vol; poor long-run hedge |
| [[uvxy\|UVXY]] | ETF (1.5x long) | Equity | Linear, amplified bleed | Short-term leveraged long-vol |
| [[svxy\|SVXY]] | ETF (-0.5x short) | Equity | Capped (de-levered) | Retail short-vol carry, post-2018 safer design |
| [[variance-swaps\|Variance swap]] | OTC | Varies | Convex (pure variance) | Institutional clean vol exposure |

VX futures sit at the center of this complex: they are simultaneously a tradable instrument in their own right, the **underlying that prices VIX options**, and the **basket the ETPs replicate**. Their linearity is both their strength (clean, transparent carry and curve trades) and their weakness (no convexity, so poor as a standalone tail hedge versus [[vix-calls|VIX calls]]). See [[long-vol-vs-short-vol]].

## Risks / Failure Modes

1. **Vol-of-vol spikes.** VX futures are highly sensitive to changes in implied vol of vol (VVIX). When VVIX spikes, both VX futures and VIX options reprice violently. The largest one-day VX percentage moves in history have come from VVIX shocks rather than from large spot SPX moves alone.
2. **Margin reprices instantly.** [[span-margin]] requirements for VX shorts can multiply 3-5x in a single session. Forced liquidation at the worst prices was a major contributor to losses in February 2018 and August 2024.
3. **Settlement basis (SOQ).** The SOQ is computed from the *opening* prints of SPX options on the settlement morning. In illiquid sessions, opening prints can be far from prior close, making the final settle hard to predict and creating last-day P&L gaps. The "VIX manipulation" allegations (2017-2018, multiple academic papers and a class-action lawsuit) center on this mechanism.
4. **Leverage from low margin.** SPAN lets traders run large notional VX positions on relatively thin margin in calm regimes, encouraging position sizes that cannot be carried through stress. This is the structural reason short-VX accounts blow up: the position is sized for the calm regime that will not last.
5. **Roll-yield cliff for long holders.** A 1% allocation to VXX bleeds ~80bps of NAV per year on average. As tail-hedge instruments, VIX-futures-long products are an inferior choice to [[vix-calls]] precisely because the bleed is linear rather than convex.
6. **Termination clauses on linked ETPs.** Many VX-linked ETNs (especially levered ones) have prospectus-level acceleration triggers (e.g., XIV's "80% intraday loss" clause). These trigger forced liquidation that then feeds back into VX futures pricing, a reflexive effect that amplified [[volmageddon]].

## Notable Events

- **March 26, 2004.** VX futures launch on CFE.
- **2008-2009 GFC.** First major test of the product. VX rises from ~22 to 80+ at peak. Short-VX strategies that existed at the time (mostly bank prop) experience years of losses; product survives, sets the stage for the post-2009 ETP boom.
- **January 29, 2009.** VXX ETN launches; long-VIX-futures exposure becomes accessible to retail.
- **November 2010.** XIV launches, allowing retail short-VIX-futures exposure.
- **August 2015 China devaluation.** VX front month rises ~80% over a few sessions; XIV loses ~50% peak-to-trough but survives. Foreshadows the 2018 mechanism.
- **July 2015.** Weekly VIX futures launched, expanding tenor granularity.
- **[[volmageddon|February 5-6, 2018]] (Volmageddon).** SPX falls 4.1% on Feb 5; spot VIX surges from 17 to 38 intraday. After-hours, VX futures gap an additional 90%+. XIV loses ~96% in the overnight session and is terminated by Credit Suisse on Feb 6. SVXY loses ~85% but survives (subsequently de-levered to -0.5x). UVXY 2x is reduced to 1.5x. Several short-vol hedge funds, most notably [[ljm-preservation-and-growth|LJM Preservation and Growth]], lose 50-80% in two days. The CFTC and SEC open inquiries into VIX settlement mechanics.
- **March 2020 (COVID crash).** Spot VIX prints 82.69 -- the highest in history. VX futures spike, but the term structure stays in steep backwardation only briefly; mean reversion is rapid as the Fed intervenes. Long-VIX-futures and VIX-call positions return 5-10x.
- **August 2020.** Mini-VIX (VXM) futures launch with $100 multiplier.
- **October 2021.** Credit Suisse de-lists XIV's successor product VXX (subsequently relaunched by Barclays).
- **[[vix-august-2024-spike|August 5, 2024]].** Yen-carry-unwind drives spot VIX from 16 to **65 intraday** -- the largest single-session percentage move in VIX history. VX futures gap 50-80% across the curve. Most short-strangle and short-VX retail accounts that survived 2018 and 2020 take heavy losses; survivors are concentrated in funds with explicit overlay protection. The move reverses within two weeks, illustrating the trap of "calm-regime sized" short-vol positions.

## Post-2018 Product Lineup Changes

The Volmageddon event triggered a structural reset in the listed vol product space:

- **XIV (-1x VIX futures)**: terminated Feb 2018, never relaunched
- **SVXY (-1x VIX futures)**: rewritten to **-0.5x** in February 2018; remains the largest listed inverse-VIX product
- **UVXY (2x VIX futures)**: reduced to **1.5x** in February 2018
- **VXX**: original 2009 ETN matured Jan 2019; relaunched as VXX in 2018 (same exposure)
- **Mini-VIX (VXM)**: launched August 2020 to broaden retail access at smaller size
- **Weekly VX**: launched July 2015, expanded coverage post-2018

The net effect: it became materially harder for retail to take large levered short-VIX-futures positions. The systemic short-vol crowding that fed Volmageddon has been partially regulated out -- although the [[vix-august-2024-spike|August 2024 episode]] showed that retail short-vol crowding has migrated into [[short-strangle|short strangles]] and [[zero-dte-options|0DTE]] structures rather than being eliminated.

## Related

- [[vix]] -- the underlying index
- [[vix-calls]] -- options on the underlying index, priced off VX futures
- [[long-vol-vs-short-vol]] -- VX futures as the listed-market expression of vol direction
- [[xiv-velocity-shares]], [[svxy]], [[uvxy]], [[vxx]] -- VIX-futures-linked ETPs
- [[volmageddon]] -- February 2018 short-VIX-futures blow-up
- [[vix-august-2024-spike]] -- August 2024 yen-carry-unwind vol shock
- [[contango]], [[backwardation]] -- term-structure regimes
- [[roll-yield]] -- the persistent return source for short VX
- [[variance-swaps]] -- OTC alternative for clean vol exposure
- [[variance-risk-premium]] -- the structural source of short-vol returns
- [[span-margin]] -- the margin methodology used for VX
- [[term-structure]] -- general framework for futures-curve trading
- [[short-vol]], [[long-vol]] -- the two sides
- [[zero-dte-options]] -- adjacent retail short-vol vehicle that absorbed flow post-2018
- [[vix-options]] -- listed options priced off VX futures
- [[vvix]] -- vol-of-vol; drives the largest VX moves
- [[calendar-spread]] -- VX is heavily traded as curve calendars
- [[section-1256-contracts]] -- §1256 tax treatment of VX futures
- [[tail-hedging]] -- where convex VIX calls beat linear long VX

## Sources

- CBOE / Cboe Global Markets. *VIX Futures Specifications* and *VIX Index Methodology White Paper* -- the authoritative spec and computation methodology.
- CBOE Futures Exchange. *Rule Book* (current edition) -- contains contract terms, position limits, settlement procedure.
- Whaley, R. (2009). "Understanding VIX." *Journal of Portfolio Management* -- foundational practitioner-academic reference.
- Mixon, S. (2013). "What Does Implied Volatility Skew Measure?" *Journal of Derivatives* -- background on VX-VIX-spot relationships.
- US Commodity Futures Trading Commission and Securities and Exchange Commission. *Joint Staff Report on the February 5, 2018 VIX Volatility Event* -- official post-mortem on Volmageddon and the SOQ settlement mechanics.
- Augustin, P., Brenner, M., Subrahmanyam, M., et al. (2018-2019 working papers). "Manipulation in the VIX?" -- academic literature on the VIX-SOQ settlement mechanism.
- Various brokerage research on the [[vix-august-2024-spike|August 2024 yen-carry-unwind episode]].
