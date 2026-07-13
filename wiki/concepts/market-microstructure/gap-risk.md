---
title: "Gap Risk"
type: concept
created: 2026-05-07
updated: 2026-06-11
status: good
tags: [market-microstructure, risk-management, options, volatility, derivatives]
aliases: ["Gap Risk", "Overnight Gap Risk", "Jump Risk"]
related: ["[[long-vol-vs-short-vol]]", "[[tail-risk-hedging]]", "[[short-strangle]]", "[[options-premium-selling]]", "[[volmageddon]]", "[[vix-august-2024-spike]]", "[[covid-crash]]", "[[circuit-breakers]]", "[[liquidity-provider]]", "[[portfolio-margin]]", "[[options-stress-testing]]", "[[ergodicity]]"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]"]
difficulty: intermediate
---

Gap risk is the risk that an instrument's price jumps from one level to another with **no opportunity to trade at intermediate prices** — across an overnight close, a weekend, an exchange halt, an earnings release, or a news shock. It is the single most important reason that standard continuous-time risk models systematically underestimate the tails of options-selling, levered-ETF, and futures portfolios. For short-vol books in particular, gap risk converts a "0.10-delta" short put — which a continuous-trading model says has roughly a 10% chance of finishing in the money — into a position that can lose 5-30x its credit on a single overnight move.

## Overview

Most textbook option pricing — Black-Scholes, the Greeks, Value-at-Risk, portfolio-margin stress scenarios as originally specified — assumes the underlying price follows a **continuous diffusion**. Under that assumption, a hedger can in principle [[delta-hedging|delta-hedge]] continuously, large moves are accumulated from many small ones, and tail probabilities are Gaussian. The world does not work this way. Markets close. Earnings happen after hours. News breaks on weekends. Exchanges halt. Prices on reopening reflect a discrete jump from one level to another, and during that jump no hedging, stop-loss, or rolling action is possible.

Gap risk is the umbrella term for the family of exposures that emerge from this **discreteness of trading**:

- **Overnight gap risk** — the equity market closes at 4:00 PM ET and reopens at 9:30 AM ET. Anything that moves SPX between those times — Asian session, European session, futures-session news, [[fomc|Fed]] minutes leak, geopolitics — shows up as a jump on the cash open.
- **Weekend gap risk** — 65 hours between Friday close and Monday open. Most weekend news (sovereign defaults, banking-system announcements, geopolitical events) is digested into Monday's open.
- **Halt gap risk** — single-name halts (LULD, news pending, regulatory) and market-wide [[circuit-breakers]] freeze trading. The reopen is a discrete auction at a level that may be far from the halt price.
- **Earnings gap risk** — single-name post-earnings moves average ~6% in absolute value for S&P 500 names, and tails are far heavier than implied. The position-holder cannot hedge between the close and the print.
- **Session-boundary gap risk in futures and crypto** — even nominally 24-hour markets have low-liquidity windows (Sunday open in [[bitcoin]], CME futures maintenance, Asian holiday closures) where the order book is thin and a single sweep produces a discrete jump.

The defining feature of all five is that the **price path between two observable prices is unobservable and untradeable**. Continuous-time models assume the path; reality skips it.

## Mechanism / How It Works

Three mechanisms generate gaps, often in combination:

### 1. Information arrives during a closure

The most common cause. Earnings, regulatory decisions (FDA, antitrust, central bank), geopolitical events, and macro data all arrive on schedules that intersect with closures. The market's first opportunity to reprice is the next session. The reopening price reflects the cumulative information impact, compressed into a single tick.

The mathematical consequence: the variance of the overnight return is not a small fraction of the daytime variance scaled by the time interval. It is often *larger* per unit time, because information is concentrated rather than diffuse. Empirically the overnight return distribution has fatter tails than the intraday return distribution at every horizon.

### 2. Liquidity withdraws around the boundary

In the minutes before close and the minutes after open, [[liquidity-provider|market makers]] widen quotes and shrink size. They face inventory risk overnight (cannot hedge if news breaks) and [[adverse-selection]] risk on the open (informed flow trades the open). The result is that even orderly news produces a jump in the marked price simply because the bid-ask widens and trades print at the new midpoint.

### 3. Forced flows compound the move

Margin-called short-vol books, levered-ETF rebalancing flows, and stop-loss cascades concentrate at the open. The first trades of the session set the price for everyone — including positions whose stop-losses were specified intraday but cannot fire until trading resumes. This is the gap-through-strikes phenomenon: the underlying gaps past one strike, then through the next, then through the next, while the [[short-strangle|short-strangle]] holder sits frozen until the cash open.

### Why standard risk models miss it

A typical Reg-T or even portfolio-margin stress test shocks the underlying ±15% with implied vol +50% and looks at the resulting P&L. This is fine for a single shock day but undercounts gap risk in two ways:

- **Stress sequence ignored.** The model evaluates "spot -15%" as a single event, not as "spot gaps -8% on Friday close, then -7% more on Monday open through a halt-and-reopen, with IV spiking from 15 to 55 in the same window." Position-margin reprices in real time and forces liquidation between the two legs.
- **Continuous-hedging fiction.** The model implicitly assumes the trader can rebalance Greeks at the stressed level. In a real gap, the trader rebalances *after* the gap, into a wider market, often with the broker liquidating positions before they can act.

The empirical fix is to stress with **explicit jump scenarios**: SPX -8% gap-down open, single-name -30% earnings gap, VIX +25 points overnight. See [[options-stress-testing]].

## Examples / Real-World Cases

### August 5, 2024 — VIX overnight gap

The yen-carry-unwind shock produced the largest single-day VIX spike in history (see [[vix-august-2024-spike]]). VIX closed Friday Aug 2 at ~23. By the Monday Aug 5 cash open, VIX futures and the cash index opened with a gap that took VIX past 50 within 30 minutes; the intraday print briefly touched 65. Short-strangle accounts that were 0.16-delta-short on Friday found themselves multiple standard deviations short on the open, with no opportunity to roll, hedge, or buy back wings between Friday close and Monday open. Many retail accounts sustained 40-80% drawdowns on a single session, and the loss was almost entirely front-loaded into the first 30 minutes of trading.

### COVID gap-down opens — March 2020

SPX gapped down 7%+ on the Monday open of March 9, 2020 (oil-war news over the weekend) and again on March 16 (Fed weekend emergency cut + lockdown announcements). [[circuit-breakers]] halted trading for 15 minutes after each gap. Short-put books with strikes 5-7% below the prior close found themselves through-the-money before any trade could execute, and the level-1 circuit breaker prevented hedging during the freeze. This was the canonical demonstration that **halts are not protective for short-premium positions** — they freeze the loss in place rather than capping it.

### NVDA earnings — August 2024

NVDA reported earnings after the close. The stock printed an after-hours move of ~7%, then drifted further before the cash open. Holders of short strangles or short puts on NVDA that were sized "0.20-delta-short" the prior day had essentially no opportunity to react: the AH session is illiquid, options markets are largely closed, and the underlying repriced through any reasonable strike before cash hours resumed. Earnings gaps are systematic — for the median S&P 500 name, the [[implied-move|implied earnings move]] embedded in the [[straddle]] underprices the realized tail by 10-30% on average over multi-decade samples.

### LULD and single-name halts

A single name halts via the Limit Up-Limit Down rule for unusual moves (5-10% in 5 minutes for tier-1 names). The reopening auction is a discrete event. Holders of options on the halted name cannot trade the option (options exchanges halt with the underlying) and cannot delta-hedge with stock. When the auction reopens, the option marks to a new spot at a new IV, both of which jumped. For small accounts running [[short-strangle]] positions on volatile single names (TSLA, GME, biotech), a single halt-driven gap has produced 100% account losses.

### Crypto weekend gaps

[[bitcoin]] trades 24/7, but liquidity is thinnest on Sunday afternoon UTC. Multiple historical flash crashes (March 12, 2020; May 19, 2021; the 2022 LUNA collapse) printed the bulk of their move during low-liquidity weekend windows. Levered-perpetual short books that were "well-collateralized" Friday found themselves liquidated by the time North American traders woke up Monday.

## Implications

### For options sellers

Short-premium positions — naked puts, [[short-strangle]], iron condors with wide wings, [[options-premium-selling|put-credit spreads]] — have **negative gamma** and **negative skew**, both of which compound through gaps. The [[delta]] and [[gamma]] reported by the broker reflect the diffusion model; the realized payoff in a gap reflects the *terminal* spot position, which can be many strikes through the short leg. Three practical rules:

- **Defined-risk structures only beyond a stress threshold.** Iron condors and put spreads cap the gap loss; naked positions do not. A blow-up-resistant book runs almost entirely defined-risk.
- **Wing distance set by gap-percentile, not by IV-percentile.** A 1-sigma move under Black-Scholes is not the relevant size; the realized 99th-percentile overnight move is. For SPX this is roughly -7%; for single names, -15% to -30% on earnings.
- **No naked positions across earnings, FOMC, or major data prints.** Closing premium-selling positions before a known catalyst is the cheapest insurance available; the [[implied-volatility]] crush after the print is rarely worth the gap exposure.

See [[long-vol-vs-short-vol]] for the asymmetry between gap-vulnerable and gap-immune books.

### For levered ETFs

Daily-rebalanced 2x and 3x ETFs (TQQQ, SOXL, SPXU) experience gap risk at the *fund* level: their daily reset means a -8% gap in the underlying produces a -16% to -24% mark on the fund. Decay accumulates because the fund must rebalance into the gapped move (buy at the bottom for inverse funds, sell at the bottom for long funds), realizing the gap as a permanent loss rather than a path-dependent fluctuation. Holders sized to "the underlying can drop 8% in a day" without modeling the levered fund's reset are routinely surprised.

### For futures and margin

Futures positions reprice continuously in the overnight session, but margin calls and forced liquidations cluster at session boundaries. A futures position sized to 10% of account on Friday can be margin-called Monday morning at a level that no Friday risk model would have flagged. [[portfolio-margin]] for futures uses SPAN scenarios, but SPAN is only as good as its scenario grid — it does not enumerate every possible gap-then-vol-spike combination.

### For risk modelling

Gap risk is the principal reason **historical-simulation [[var]]** outperforms parametric VaR for short-vol books: empirical history contains gaps; Gaussian assumptions do not. Better still are **scenario-based stress tests** that explicitly model gap-then-stress sequences. See [[options-stress-testing]] and [[ergodicity]] for the deeper argument: time-average returns of strategies exposed to gaps are far below their ensemble-average returns, because gaps disproportionately contribute to the rare paths that destroy compounding.

## Common Misconceptions

1. **"My broker will close the position before it gets bad."** Brokers liquidate at the prevailing market when margin breaches occur. In a gap-and-halt sequence, the prevailing market is the post-gap, post-halt reopen. The broker cannot liquidate during the gap or the halt; you eat the move and then eat the spread.
2. **"Stop-losses protect me overnight."** Stop orders rest on the exchange, which is closed. They activate at the open at whatever price the open prints, which can be far from the stop level. Stops are gap-vulnerable, not gap-protective.
3. **"Earnings IV crush makes selling premium across the print profitable."** On average, the IV crush is *priced into* the [[implied-move]] — i.e., the [[straddle]] price embeds it. The realized variance of single-name post-earnings returns has a fat right tail in absolute size, and the negative-skew of premium selling means a single 3-sigma earnings gap erases a year of theta.
4. **"Implied vol already prices gap risk."** Partially. Implied vol prices the *expected* magnitude of moves under the market's distribution assumption, but the 99th-percentile gap is consistently underpriced relative to its frequency in equity options — this is a major component of the [[variance-risk-premium]] but also of why short-premium tail losses are systematic.
5. **"Hedging continuously eliminates gap risk."** No. Hedging continuously eliminates gamma risk only between trading sessions. Across a closure, the hedge is frozen at its prior level.

## Related

- [[long-vol-vs-short-vol]] — gap risk is the structural edge of long-vol books and the structural curse of short-vol books
- [[tail-risk-hedging]] — explicit construction designed around gap immunity
- [[options-premium-selling]] — strategy most exposed to gap risk
- [[short-strangle]] — canonical structure that gaps through strikes
- [[options-stress-testing]] — how to model gap scenarios explicitly
- [[circuit-breakers]] — the halt mechanism that freezes (rather than caps) gap losses
- [[liquidity-provider]] — the agents whose withdrawal at session boundaries widens gaps
- [[volmageddon]] — Feb 2018, gap-driven termination of XIV
- [[vix-august-2024-spike]] — Aug 2024, largest VIX overnight gap in history
- [[covid-crash]] — multiple gap-down opens through circuit breakers
- [[ergodicity]] — why time-average return diverges from expected return when gaps exist
- [[implied-move]] — the market's pricing of expected gap magnitude

## Sources

- Spitznagel, Mark. *Safe Haven: Investing for Financial Storms* (2021) — extended treatment of gap and crash risk in geometric-mean compounding ([[safe-haven-spitznagel]]).
- Taleb, Nassim Nicholas. *Dynamic Hedging* (1997) — original practitioner treatment of jump risk and the failure of continuous-hedging assumptions.
- Carr, Peter and Wu, Liuren. "Variance Risk Premiums" (2009) — empirical decomposition of the VRP, including the jump component.
- [[volmageddon|Feb 2018 vol shock]], [[vix-august-2024-spike|Aug 2024]], [[covid-crash|March 2020]] — direct historical evidence.
- CBOE LULD and Market-Wide Circuit Breaker rules — exchange documentation on halt mechanics.
