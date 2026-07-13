---
title: "SPX Options"
type: market
created: 2026-05-06
updated: 2026-06-19
status: excellent
tags: [options, derivatives, sp500, indicators, stocks]
aliases: ["SPX", "S&P 500 Index Options", "Cboe SPX Options"]
domain: [derivatives, options]
difficulty: intermediate
related: ["[[index-options]]", "[[options]]", "[[spy-options]]", "[[xsp-options]]", "[[ndx-options]]", "[[rut-options]]", "[[section-1256-contracts]]", "[[am-vs-pm-settlement]]", "[[cash-vs-physical-settlement]]", "[[american-vs-european-options]]", "[[weekly-options]]", "[[0dte-trading]]", "[[vix]]", "[[volatility-skew]]", "[[itpm-trade-construction-playbook]]", "[[options-portfolio-construction]]"]
---

SPX options are Cboe-listed, cash-settled, European-style [[index-options]] on the [[sp500|S&P 500 Index]]. They carry a $100 contract multiplier — so a single SPX contract is roughly 10x the notional of a comparable [[spy-options|SPY]] option — and they qualify as [[section-1256-contracts|Section 1256 contracts]] under US tax law, giving them a 60/40 long-term/short-term capital gains treatment regardless of holding period. Because settlement is in cash and exercise is European-style, sellers carry no early-assignment risk and no risk of unwanted stock delivery, which makes SPX the preferred index-options vehicle for active and institutional traders, including [[itpm|ITPM]]-style portfolios. SPX is also the reference index for the [[vix|VIX]] volatility index.

## Overview

SPX options trade exclusively at the Cboe and reference the S&P 500 Index level (e.g., SPX = 5000 means a single contract has $500,000 of notional exposure at $100 multiplier). They are the deepest, most liquid index options product in the world, with daily volume regularly running in the millions of contracts. Two related products extend the franchise: traditional monthly SPX options ("AM-settled") and SPXW weeklies ("PM-settled"), which together cover essentially every trading day with [[0dte-trading|0DTE]] expirations now available daily.

Three structural features distinguish SPX from equity-style options:

1. **Cash settlement** — at expiration, the holder of an in-the-money option receives the intrinsic value in cash; no shares of any kind are delivered (see [[cash-vs-physical-settlement]]).
2. **European exercise** — exercise can occur only at expiration. Sellers cannot be assigned early (see [[american-vs-european-options]]).
3. **Section 1256 tax treatment** — 60% of any gain is taxed as long-term and 40% as short-term, regardless of how long the position was held.

## Specifications

| Spec | Value |
|---|---|
| Underlying | S&P 500 Index (SPX) |
| Multiplier | $100 |
| Exercise style | European |
| Settlement | Cash |
| Strike intervals | $5 standard; $1 near-the-money on weeklies |
| Tick size | $0.05 below $3.00 premium; $0.10 above |
| Trading hours | Regular: 9:30am–4:15pm ET; Extended (Globex): 8:15pm prior day → 9:15am ET, plus a global trading session — about 24 hours longer than SPY each week |
| Symbol | SPX (AM-settled monthlies), SPXW (PM-settled weeklies including 0DTE) |
| Tax treatment | [[section-1256-contracts|Section 1256]] (60/40) |

## Tax Treatment (Section 1256)

SPX options are "broad-based stock index options" under IRC Section 1256, which means:

- **60/40 split** — every realized gain or loss is treated as 60% long-term capital gain/loss and 40% short-term, regardless of holding period. A scalp held for two minutes still gets the 60/40 treatment.
- **Mark-to-market at year-end** — open positions on Dec 31 are treated as if closed at fair market value on that date. This eliminates the need to track holding periods across years.
- **Loss carryback** — Section 1256 losses can be carried back up to 3 years (against prior Section 1256 gains only) on Form 6781, a feature unavailable to standard equity option losses.
- **No wash-sale concerns under §1091** in the same way as equities — though dealer/anti-abuse rules can still apply in edge cases (see [[wash-sale-rules-options]]).

For an active SPX trader in the top federal bracket, the 60/40 blended rate is roughly 26.8% federal vs ~37% short-term — a meaningful structural edge that compounds over a portfolio's life. See [[section-1256-contracts]] for full mechanics.

## Settlement Mechanics

Two distinct settlement regimes coexist:

- **AM settlement (monthly SPX)** — the traditional 3rd-Friday monthly contract settles to the **Special Opening Quotation (SOQ)**, calculated from the opening prints of all 500 component stocks on expiration Friday morning. Final trading occurs the prior afternoon. Because S&P 500 components open at staggered times, the SOQ can differ materially from Thursday's close, creating overnight gap risk.
- **PM settlement (SPXW weeklies and 0DTE)** — settles to the official 4:00pm ET closing print of the SPX Index. Trading on the expiration day continues until 4:00pm.

This AM/PM distinction matters for any spread that straddles both styles — see [[am-vs-pm-settlement]] for the full discussion and case studies.

## Liquidity Profile

- **Volume** — routinely 2–4 million contracts/day, with 0DTE alone now over 40% of total SPX volume.
- **Bid/ask spreads** — penny-equivalent (after multiplier) at the most liquid strikes; widening on far OTM wings and back-month expirations.
- **Open interest** — concentrated around round-number strikes and key technical levels; analyzed via [[max-pain]] and [[gamma-exposure]] frameworks.
- **Strike density** — $5 intervals across the chain; $1 increments are increasingly available near-the-money on weeklies.
- **Quote sizes** — typically large (50–500 contracts) at the inside on near-the-money strikes; market makers compete heavily.

## Greeks and Volatility-Surface Behavior

SPX is the deepest, cleanest [[options-greeks|Greeks]] laboratory in the listed market because cash settlement and European exercise strip away the dividend-driven and early-exercise distortions that complicate equity options:

- **Delta** — behaves along the textbook Black-Scholes-Merton curve with no ex-dividend early-exercise kink. Institutional books frequently aggregate exposure in *delta-equivalent index points* so SPX, [[ndx-options|NDX]], and [[rut-options|RUT]] positions net to a single number.
- **Gamma** — short-dated SPX options (weeklies and [[0dte-trading|0DTE]]) carry enormous gamma. Dealer net-gamma positioning in SPX has become a tracked market-structure variable: when dealers are long gamma they dampen intraday moves; when short, they amplify them. The 0DTE boom intensified this feedback loop. See [[gamma-exposure]].
- **Theta** — the decay engine behind SPX [[options-premium-selling|premium selling]]; accelerates non-linearly into expiry, which is why short-dated structures harvest the bulk of decay in the final days.
- **Vega** — SPX is the primary listed instrument for broad-market [[implied-volatility|implied-vol]] exposure, and SPX option prices are literally what the [[vix|VIX]] is computed from. Long calendars are long vega; short strangles are short vega and harvest the [[volatility-risk-premium]].

### The SPX volatility surface

- **Steep negative [[volatility-skew|skew]] (the "smirk")** — SPX puts trade at materially higher implied vol than equidistant calls, the most stable feature of the surface. Index crashes are correlated, crash-protection demand is one-directional and persistent, and the skew has never normalized since the 1987 crash. The skew itself is tradable via risk reversals and put-spread collars.
- **Term structure of implied vol** — upward-sloping in calm regimes (mean-reversion expectation), inverting in stress. This is the equity-option analog of the [[vix|VIX]] futures curve and is traded via calendars and diagonals.
- **Volatility-of-volatility** — the SPX surface itself moves; its second-moment behavior is tracked by [[vvix|VVIX]] and matters for hedging long-dated vega.

Mastery of the full surface — skew and term structure, not just at-the-money vol — is what distinguishes a structural SPX book from naive directional trading.

## Term Structure

SPX implied vol has a pronounced term structure that drives a large share of institutional positioning:

| Regime | Term-structure shape | Typical structure response |
|---|---|---|
| Calm / low-vol | Upward-sloping (near vol < far vol) | Sell near-dated theta; long calendars to be long vega cheaply |
| Stress / spike | Inverted (near vol > far vol) | Near-dated premium rich; sell short-dated, hedge tails |
| Event-driven (FOMC, CPI, earnings clusters) | Local "kink" around the event date | Calendars and diagonals isolate the event-vol bump |

Because every SPX expiry references the *same* underlying index, an SPX calendar is a **pure same-underlying time spread** — unlike [[vix-options|VIX calendars]], whose legs reference different futures. This makes SPX calendars and diagonals the canonical clean way to trade the [[implied-volatility]] term structure. See [[calendar-spread]] and [[vix-term-structure]] for the contrast.

## Common Spread Structures

| Structure | Construction | View | Notes |
|---|---|---|---|
| [[short-strangle\|Short strangle]] | Sell OTM put + OTM call (e.g. 16-delta) | Range-bound / short vol | Undefined risk; harvests [[volatility-risk-premium\|VRP]]; portfolio-margin efficient |
| [[iron-condor\|Iron condor]] | Short strangle + protective wings | Range-bound, defined risk | Capped loss; dominant 0DTE structure |
| [[short-straddle\|Short straddle]] | Sell ATM put + ATM call | Strong short-vol / pin bet | Highest theta and gamma |
| Put credit spread | Short higher put, long lower put | Mildly bullish / short vol | Popular defined-risk 0DTE trade |
| [[calendar-spread\|Calendar]] | Sell near, buy far (same strike) | Long vega / term-structure | Pure same-underlying time spread |
| [[itpm-ratio-calendar-spread\|Ratio calendar]] | Asymmetric near/far quantities | Term-structure + skew | ITPM staple |
| Put-spread collar | Long put spread financed by short call | Tail hedge for long book | Net-cheap downside protection |

Defined-risk variants dominate retail and 0DTE flow because they cap the [[notional-shock|notional shock]] of a single ~$500K contract; undefined-risk strangles and straddles dominate institutional books where [[options-buying-power-reduction|portfolio margin]] makes them capital-efficient. See [[itpm-trade-construction-playbook]].

## ITPM Use Cases

[[itpm|ITPM]]-style portfolios use SPX options for several reasons that follow directly from the spec sheet:

- **Macro hedges** — buying OTM SPX puts as catastrophe insurance for a long [[long-short-equity]] book. Cash settlement means the hedge pays cash exactly when needed; no shares to liquidate, no overnight gap risk from physical delivery.
- **Vol selling / premium harvest** — selling [[short-strangle|strangles]], [[iron-condor|iron condors]], and [[short-straddle|straddles]] on SPX captures the [[volatility-risk-premium]] without early-assignment risk. See [[itpm-ratio-calendar-spread]].
- **Calendar and diagonal spreads** — exploit the term structure of [[implied-volatility]] without dividend-risk complications that affect equity options.
- **Capital-efficient size** — one SPX contract replaces ~10 SPY contracts, reducing per-contract commissions and operational complexity for portfolio-scale hedges.
- **Tax-aware sizing** — Section 1256 treatment means the after-tax Sharpe of an SPX premium-selling strategy can exceed the equivalent SPY strategy by several hundred basis points annually.

## Typical Strategies

SPX is the workhorse for index-level options structures. The most common are:

- **Premium harvesting** — [[short-strangle|short strangles]], [[short-straddle|straddles]], and [[iron-condor|iron condors]] sold to capture the [[volatility-risk-premium]]; European exercise removes early-assignment risk entirely.
- **Tail hedging** — long OTM puts or [[put-spread|put spreads]] as portfolio catastrophe insurance; cash settlement delivers liquidity exactly when an equity book is under stress.
- **0DTE intraday** — same-day [[0dte-trading|0DTE]] credit spreads and iron condors on SPXW, now the largest single slice of SPX volume.
- **Calendar / diagonal spreads** — exploiting the [[implied-volatility]] term structure without the dividend-timing complications that affect [[spy-options|SPY]] equity options.
- **Skew and dispersion** — expressing views on SPX [[volatility-skew]] or trading SPX vol against [[ndx-options|NDX]] / [[rut-options|RUT]] in a [[dispersion-trading]] frame.

## SPX vs SPY Comparison

| Dimension | SPX | [[spy-options|SPY]] |
|---|---|---|
| Underlying | S&P 500 Index | SPDR S&P 500 ETF |
| Notional per contract | ~$500,000 (at SPX 5000) | ~$50,000 (at SPY 500) |
| Exercise | European | American |
| Settlement | Cash | Physical (100 shares) |
| Tax | Section 1256 (60/40) | Standard equity |
| Early assignment risk | None | Yes (esp. ex-dividend) |
| Tick size | $0.05 / $0.10 | $0.01 (penny pilot) |
| Strike intervals | $5 (most), $1 (some weeklies) | $1 broadly |
| Dividend risk | None (index, not ETF) | Yes (quarterly distributions) |
| IRA/small account | Capital-intensive | More accessible |
| Trading hours | Extended (~24hrs longer/week) | Standard |

For ITPM-style portfolios trading at meaningful size with active premium-selling, SPX is the default. For sub-$25K accounts or IRAs that need single-contract granularity, SPY (or [[xsp-options|XSP]]) is more appropriate.

## Risks

- **Notional shock** — at $100 multiplier on a 5000-level index, every 1-point SPX move is $100 per contract. Position sizing errors are unforgiving.
- **AM-settle gap risk** — overnight news between Thursday close and Friday SOQ can move settlement materially.
- **Liquidity collapse on stress days** — bid/ask spreads on far OTM wings widen sharply during volatility spikes, exactly when hedges need to be monetized.
- **Pricing tick floors** — the $0.05 tick below $3 creates a wider effective spread vs SPY's penny pricing, eroding edge on small-premium tactics like cheap OTM scalps.
- **Section 1256 mark-to-market** — open positions on Dec 31 generate taxable events even without closing, complicating tax planning for long-dated structures.

## Historical Context

SPX options launched on the Cboe in **1987**, evolving from the earlier OEX (S&P 100) options that pioneered cash-settled index options in 1983. SPX is now the deepest options market in the world and has been reshaped by several structural episodes:

- **October 1987 (Black Monday)** — the first crash to stress listed index options; the episode entrenched the steep SPX put [[volatility-skew|skew]] that persists to this day, as crash-protection demand never normalized afterward. See [[1987-crash]].
- **2003 — VIX recast on the SPX option strip** — the modern [[vix|VIX]] is computed directly from out-of-the-money SPX option prices, making SPX implied vol itself a tracked, tradable object via [[vix-options|VIX options]] and [[vix-futures|VIX futures]].
- **August 24, 2015 — the SOQ flash-crash morning** — staggered component openings produced an SPX Special Opening Quotation roughly 5% below the prior close, settling AM puts far deeper ITM than Thursday's close implied. The canonical cautionary tale for AM-settlement gap risk. See [[am-vs-pm-settlement]].
- **2022–2025 — the 0DTE era** — daily SPX expirations drove same-day options to over 40% of total SPX volume, transforming intraday dealer-[[gamma-exposure|gamma]] dynamics and creating an entirely new short-dated retail and systematic flow. See [[0dte-trading]].

## Related

- [[index-options]] — overview of the cash-settled index-options franchise
- [[options]] — options fundamentals
- [[spy-options]] — physically-settled American-style cousin
- [[xsp-options]] — 1/10 size SPX with same tax treatment
- [[ndx-options]] — Nasdaq-100 index-options sibling
- [[rut-options]] — Russell 2000 index-options sibling
- [[section-1256-contracts]] — tax framework
- [[am-vs-pm-settlement]] — settlement mechanics
- [[cash-vs-physical-settlement]] — settlement type comparison
- [[weekly-options]] — SPXW mechanics
- [[0dte-trading]] — same-day expiration strategies
- [[american-vs-european-options]] — exercise style
- [[vix]] — implied volatility on SPX
- [[volatility-skew]] — SPX skew structure
- [[max-pain]] — open-interest-based pinning analysis
- [[itpm-trade-construction-playbook]]
- [[options-portfolio-construction]]
- [[options-position-sizing]]
- [[options-greeks]] — delta/gamma/theta/vega vocabulary
- [[gamma-exposure]] — dealer-gamma market structure
- [[implied-volatility]] — the surface SPX options trade
- [[calendar-spread]] — pure same-underlying term-structure trade
- [[short-strangle]], [[iron-condor]], [[short-straddle]] — canonical structures
- [[volatility-risk-premium]], [[variance-risk-premium]] — the structural edge
- [[options-buying-power-reduction]] — portfolio-margin efficiency
- [[vix-options]], [[vix-futures]] — vol products referencing SPX
- [[1987-crash]] — the event that entrenched SPX put skew

## Sources

- Cboe SPX product specifications (cboe.com/tradable_products/sp_500/spx_options)
- IRC Section 1256 — Internal Revenue Code
- Cboe Special Opening Quotation methodology
