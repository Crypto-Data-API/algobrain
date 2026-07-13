---
title: "Options Trading Pitfalls"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, risk-management, derivatives, behavioral-finance, education]
aliases: ["Options Pitfalls", "Common Options Mistakes", "Options Trader Mistakes"]
domain: [risk-management, derivatives, options]
prerequisites: ["[[options-greeks]]", "[[implied-volatility]]", "[[american-vs-european-options]]"]
difficulty: intermediate
related: ["[[iv-crush]]", "[[pin-risk]]", "[[assignment-risk]]", "[[options-trader-psychology]]", "[[delta-hedging]]", "[[gamma-scalping]]", "[[volatility-risk-premium-decay]]", "[[long-straddle]]", "[[short-volatility-strategies]]", "[[iron-condors]]", "[[wheel-strategy]]", "[[covered-calls]]", "[[cash-secured-puts]]", "[[managing-winners]]", "[[options-premium-selling]]", "[[options-portfolio-construction]]", "[[behavioral-finance]]"]
---

**Options trading pitfalls** are the recurring failure modes that destroy retail and intermediate options accounts: the structural traps embedded in the product that catch traders who treat options like leveraged stock. Most options-specific losses do not come from being wrong on direction. They come from being right on direction but wrong on [[implied-volatility|implied vol]], on [[theta-decay|theta]], on [[assignment-risk|assignment]], or on position sizing. This page enumerates the ten most common pitfalls, the mechanism behind each, a real-world reference point, and how professional traders structurally avoid them. (Source: [[2026-04-22-gap-finder-stock-options-trading-pitfalls-tradesta]])

## Overview

Options are a non-linear, time-decaying, [[vega|vega]]-sensitive instrument. Each of those three properties — non-linearity, decay, and vol sensitivity — generates its own family of mistakes. The pitfalls below are organized roughly in order of frequency and account-destruction severity.

The recurring pattern: a trader who has succeeded with stocks (or with one or two lucky options trades) imports stock-style intuitions into options and gets blown up by a Greek they did not size for. Almost every entry below maps to "ignored a Greek that mattered."

## Pitfalls Catalog (Summary Table)

The full catalog of ten pitfalls, the Greek or mechanic each one violates, the root cause, and the one-line fix. Each row links to its detailed section below.

| # | Pitfall | Greek / mechanic | Root cause | One-line fix |
|---|---------|------------------|------------|--------------|
| 1 | [[#1 Overleverage and Undersizing\|Overleverage / undersizing]] | Delta, gamma, vega notional | Sizing in contracts not risk | Cap single trade at 1-3% of equity at *max loss* |
| 2 | [[#2 IV Crush on Long Premium Around Earnings\|IV crush around earnings]] | [[vega]] / [[iv-crush]] | Buying inflated pre-event IV | Use vega-neutral spreads or skip long premium |
| 3 | [[#3 Assignment Surprises American-Style\|Assignment surprises]] | Early exercise ([[assignment-risk]]) | American-style + dividend/borrow | Scan short calls pre-ex-div; use cash-settled |
| 4 | [[#4 Pin Risk at Expiration\|Pin risk]] | Expiration exercise ([[pin-risk]]) | ATM short into the close | Close strikes within ~1% of spot a day early |
| 5 | [[#5 Buying OTM Lottery Tickets\|OTM lottery tickets]] | Negative expected value | [[lottery-stock-anomaly\|Lottery bias]] | Buy longer-dated, less-OTM; cap as entertainment |
| 6 | [[#6 Doubling Down on Short Premium Losers Negative Gamma Blowups\|Doubling down short premium]] | Negative [[gamma]] | Loss-aversion; "roll for credit" | Predefine *exit* (close at 2x credit lost) |
| 7 | [[#7 Wide Bid-Ask Spreads in Illiquid Options\|Illiquid wide spreads]] | Transaction cost | Ignoring liquidity | Filter: spread ≤5% mid, OI ≥500 |
| 8 | [[#8 Holding Through Earnings Unintentionally\|Unintended earnings hold]] | [[vega]] ramp + gap | No earnings-calendar check | "No earnings within DTE" hard filter |
| 9 | [[#9 Theta Decay Misunderstanding Selling 90 DTE for Safety\|Theta misunderstanding (90+ DTE)]] | [[theta-decay\|theta]] vs [[vega]] | Confusing premium with risk-adj return | Default 30-45 DTE for short premium |
| 10 | [[#10 Naked Options with Undefined Risk\|Naked undefined risk]] | Unbounded loss | Chasing higher credit | Always define risk with protective wings |

## 1. Overleverage and Undersizing

**What it is.** Buying or selling options sized in *contracts* rather than in *notional risk*. A retail trader who would never put 80% of their account into one stock thinks nothing of putting 80% into one weekly call.

**Why it happens.** Options dollar-prices look small. A $2.50 call looks like 1/40th the cost of $100 stock — but its 50-delta means it carries the same directional risk as 50 shares of stock per contract, and the embedded gamma and vega multiply the path-dependent damage on adverse moves.

**Real-world magnitude.** Robinhood's 2020-2021 options expansion produced multiple documented cases of accounts losing 80%+ in a single week from oversized weekly calls. The aggregate retail loss on AMC short calls alone in mid-2021 (during the [[meme-stock-rally|meme-stock rally]]) ran into tens of millions; small accounts got vaporized. The 2018 [[xiv-implosion|XIV unwind]] is the institutional version of the same mistake.

**How to avoid.** Size positions by *vega-adjusted notional risk* and worst-case loss, not by contract count. Cap any single options trade at 1-3% of account equity at *maximum loss*, not at premium paid. See [[options-portfolio-construction]] and [[risk-management]].

## 2. IV Crush on Long Premium Around Earnings

**What it is.** Buying calls or puts (or [[long-straddle|long straddles]]) before earnings, being directionally correct on the print, and *still losing money* because [[implied-volatility|IV]] crushes 30-50% the moment the announcement hits.

**Why it happens.** Pre-earnings IV inflates because the market prices the binary information event into the option. Once the print resolves uncertainty, [[vega]] collapses. A $5.00 ATM straddle bought the afternoon of an earnings report routinely opens the next morning at $2.00-$2.50 even when the stock moves the implied move.

**Real-world magnitude.** Empirically, the "long straddle into earnings" trade has historically lost money on average across S&P names — the [[variance-risk-premium|variance risk premium]] is positive precisely *because* IV crush systematically over-rewards short premium and punishes long. Documented in repeated academic work on the [[volatility-risk-premium-decay]].

**How to avoid.** If you must take an earnings directional bet, use *spreads* (vertical or diagonal) that are vega-balanced or vega-negative. If you have no vol view, do not buy long premium ahead of a known event. See [[iv-crush]] and earnings-iv-crush.

## 3. Assignment Surprises (American-Style)

**What it is.** A short option holder gets surprise-exercised by the long counterparty before expiration, often around a dividend or a hard-to-borrow event, and wakes up with an unwanted stock position they did not hedge for.

**Why it happens.** Equity and ETF options are [[american-vs-european-options|American-style]]: the long can exercise any time, and does so when the option's remaining extrinsic value is less than the dividend (for ITM short calls) or the borrow rebate (for ITM short puts). See [[assignment-risk]] for the full mechanic.

**Real-world magnitude.** Robinhood's 2020 Alex Kearns suicide is the most extreme documented case: a 20-year-old saw a -$730k notional balance after one leg of a bull put spread was assigned overnight, despite the position's actual max loss being a fraction of that. Less catastrophically, dividend-driven early assignments on SPY, JPM, and high-dividend names happen in *every* dividend cycle.

**How to avoid.** Scan all short calls before ex-dividend dates. Close any deep-ITM short whose remaining extrinsic is less than the next dividend. Index ETFs/XSP/SPX (cash-settled European) eliminate this risk entirely.

## 4. Pin Risk at Expiration

**What it is.** The underlying closes within pennies of a short strike on expiration day. The trader does not know whether the position will be exercised, and discovers Monday morning whether they own a stock position they did not want.

**Why it happens.** [[american-vs-european-options|American-style]] options can be exercised up to 90 minutes after the equity close on expiration day. ATM short options leave the trader's exercise outcome in the long holder's hands. See [[pin-risk]] and [[options-pinning]].

**Real-world magnitude.** GME during 2021 saw multiple Friday closes pinning to round-number strikes (e.g., $400 on 2021-01-29) that left short-call writers with surprise overnight short-stock positions in a stock that opened with double-digit gaps the following week. Standard occurrence around every monthly OPEX for liquid names.

**How to avoid.** Close any physically-settled short option with a strike within ~1% of spot at least one trading day before expiration. Use cash-settled index options for expiration-day positions.

## 5. Buying OTM "Lottery Tickets"

**What it is.** Buying far-out-of-the-money short-dated calls (or puts) for $0.05-$0.20, hoping for a 10-50x payoff on a tail move that almost never materializes.

**Why it happens.** Cognitive bias toward [[lottery-ticket-bias|lottery-shaped payoffs]]. The expected value is reliably negative — these options are priced *with* a fat-tail premium that more than offsets the actual tail probability — but the occasional 50x winner is salient and memorable.

**Real-world magnitude.** Multiple academic studies (e.g., Bali, Cakici, Whitelaw 2011) document that the cheapest, most lottery-shaped securities have the *worst* average returns. Retail-favored 5-delta weekly calls in single names typically expire worthless 90%+ of the time, and the average outcome is a 100% loss of premium.

**How to avoid.** If you want positive convexity, buy *longer-dated*, *less-OTM* options where vega and gamma actually compensate you for time. Treat sub-$0.20 weekly OTM premium as entertainment spending capped at <0.25% of account equity. See [[options-trader-psychology]].

## 6. Doubling Down on Short Premium Losers (Negative Gamma Blowups)

**What it is.** A short [[short-strangle|strangle]] or [[iron-condors|iron condor]] starts losing as the underlying breaches a strike. The trader "rolls for credit" — moving the tested strike further out and selling more contracts — instead of taking the loss. The position is now *larger and shorter gamma* into a continuing trend, and the next leg compounds.

**Why it happens.** Loss-realization aversion plus the comforting illusion that "rolling for a credit" means the trade is still profitable. It is not — the credit is dwarfed by the increased risk. See [[options-trader-psychology]].

**Real-world magnitude.** The classic case is James Cordier / OptionSellers.com: $150M+ AUM short-strangle book on natural gas that blew up in November 2018 when nat gas spiked ~50% in a week. Account holders received margin calls *exceeding* their entire balances. Smaller but structurally identical blowups happen quarterly to retail short-premium traders during VIX spikes (Aug 2024, March 2020, Feb 2018).

**How to avoid.** Predefine *exit* criteria, not roll criteria. Short-premium positions should have a hard "close at 2x credit lost" rule and never be sized so that a single test of the strike is account-threatening. See [[managing-winners]] and [[short-volatility-strategies]].

## 7. Wide Bid-Ask Spreads in Illiquid Options

**What it is.** Trading options on names with low open interest, where bid-ask spreads are 10-30% of the option's mid price. The trader pays the spread on entry and again on exit, and any "edge" the strategy claimed is gone before the underlying moves.

**Why it happens.** Newer traders look at premium and Greeks but not at *liquidity*. A 0.40-bid 0.60-ask quote on a $0.50 mid means a 40% round-trip slippage cost, dwarfing any reasonable edge.

**Real-world magnitude.** On small-cap stocks (sub-$1B market cap), it is common for weekly options to quote $0.05 wide on a $0.30 mid — 33% round-trip cost. Even on liquid mega-caps, far-OTM weeklies near expiration routinely show 10-15% spread costs.

**How to avoid.** Filter the universe to options with (a) bid-ask spread ≤5% of mid, (b) open interest ≥500 contracts, (c) daily volume ≥100 contracts on the specific strike. Trade SPY, QQQ, and the ~50 most liquid single names, not the long tail.

## 8. Holding Through Earnings Unintentionally

**What it is.** A trader holds a short premium position (covered call, credit spread, iron condor) on a name they did not realize had an earnings release inside the position's expiration window. The pre-earnings IV ramp drives the position into a mark-to-market loss; the post-earnings move can break the position entirely.

**Why it happens.** No earnings-calendar awareness in the entry workflow. The trader screens for IV rank, picks a strike, and never checks the earnings-calendar.

**Real-world magnitude.** Common on names like NFLX, NVDA, TSLA which routinely move 5-15% on earnings — far outside typical iron condor wings. A $100-wide iron condor on NVDA going into a 12% earnings move is a max-loss event by definition.

**How to avoid.** Build "no earnings within DTE" as a hard filter into the entry workflow. If trading earnings is the *intent*, do it deliberately with appropriate structure. See earnings-volatility and earnings-calendar.

## 9. Theta Decay Misunderstanding (Selling 90+ DTE for "Safety")

**What it is.** A trader sells longer-dated options thinking the wider time buffer makes the position safer. In reality, 90+ DTE short premium has poor theta-per-day, far higher *vega* exposure, and ties up margin for months — accumulating risk faster than it accumulates premium.

**Why it happens.** Confusing nominal premium ($X collected) with risk-adjusted return. A 90-DTE put might collect $3.00 of premium versus $0.80 for a 30-DTE — but it has 3x the vega and only collects extrinsic at the slow back-end of the theta curve.

**Real-world magnitude.** Studies of short-premium return-on-capital consistently show the 30-45 DTE range optimizes theta-per-day-per-margin. Going to 90+ DTE typically halves the theta yield while doubling the vega risk. See [[volatility-risk-premium-decay]] and [[theta-targeting]].

**How to avoid.** Default to 30-45 DTE for short premium. Use longer expirations only when explicitly trading vol term structure or hedging a longer-horizon thesis. Manage winners at 50% of max profit; the back half of theta decay is not worth the residual gamma/vega risk.

## 10. Naked Options with Undefined Risk

**What it is.** Selling [[short-strangle|short strangles]], naked short calls, or naked short puts without protective wings — exposing the account to theoretically unlimited loss (for short calls) or strike-times-100 loss (for short puts) on a single adverse move.

**Why it happens.** The defined-risk version (iron condor, credit spread) collects less premium. Traders rationalize that "the strikes are far OTM so it'll never happen" and prefer the higher credit. Until it happens.

**Real-world magnitude.** Beyond OptionSellers.com (above), Karen Supertrader / Karen Bruton's $190M short-strangle fund unwound in 2014-2016 with allegations of mismarking to hide losses; SEC settlement followed. The pattern is consistent: years of credit collection followed by a single quarter that erases the entire P&L plus principal.

**How to avoid.** Always define risk with wings. The premium reduction from buying a far-OTM long leg (1-3 strikes wider) is small relative to the catastrophic-tail protection. If the strategy is not profitable as a defined-risk structure, it was not profitable as an undefined one — you were just collecting an insurance premium without holding capital for the claim.

## Worked Example (Qualitative): How Three Pitfalls Compound

A retail trader is bullish on a $50 stock reporting earnings in three days. They buy 20 contracts of the $55 weekly call for $0.40 each ($800 total), reasoning "if it pops I make 10x."

- **Pitfall 1 (overleverage):** $800 is 16% of their $5,000 account, sized by premium paid rather than by the realistic-loss expectation. Almost all of that $800 is at risk because the option is far OTM and short-dated.
- **Pitfall 2 (IV crush):** Earnings IV is inflated to ~120%. The trader is paying a fat-tail premium *on top of* an event-inflated vol level.
- **Pitfall 5 (OTM lottery ticket):** A 5-delta weekly call needs a ~12% up-move in three days just to reach the strike, and more to be profitable -- a tail outcome priced against them.

**Outcome.** Earnings print is *mildly* good; the stock rises 4% to $52. The trader was directionally right -- but the call is still OTM, and post-print [[iv-crush|IV collapses]] from 120% to 45%. The $0.40 call is now worth $0.06. The position loses 85% despite a correct directional call. Every individual mistake was survivable; stacked together they were near-certain loss. The professional version of this trade -- if taken at all -- is a *defined, less-OTM, vega-aware* structure sized at <1% of equity, entered with full knowledge of the implied-earnings-move.

## Professional Pre-Trade Checklist

The structural counter to these pitfalls is a fixed pre-trade checklist. Most blowups are a checklist item that was skipped.

| Check | Question | Pitfall it defuses |
|-------|----------|--------------------|
| Sizing | Is max loss ≤1-3% of equity? | 1 |
| Vol regime | Is IV rich or cheap; is there an event inside DTE? | 2, 8 |
| Calendar | Earnings or ex-dividend before expiration? | 2, 3, 8 |
| Style | American (assignment/pin risk) or European cash-settled? | 3, 4 |
| Liquidity | Spread ≤5% of mid, OI ≥500, volume ≥100? | 7 |
| Structure | Is risk *defined* (wings in place)? | 6, 10 |
| DTE | Is 30-45 DTE appropriate for the thesis? | 9 |
| Exit | Are profit-take and stop-out levels predefined? | 6, 10 |

## Cross-Cutting Themes

Several pitfalls share root causes worth naming explicitly:

- **Greek illiteracy.** Pitfalls 1, 2, 6, 9 all stem from sizing in dollars or contracts rather than in [[options-greeks|Greeks]]. The fix is portfolio-level Greeks reporting on every position.
- **Liquidity blindness.** Pitfalls 3, 4, 7 are amplified by trading illiquid underlyings. A liquidity filter solves much of the surface area.
- **Behavioral.** Pitfalls 5, 6, 10 are at root [[options-trader-psychology|behavioral]]. Position sizing rules and predefined exits are the operational counter to behavioral biases.
- **Calendar awareness.** Pitfalls 2, 3, 8 are calendar-driven (earnings, ex-dividend, expiration). A weekly calendar review eliminates most of these.

## Related

- [[iv-crush]] — the volatility-collapse mechanic behind pitfall #2
- [[pin-risk]] — the expiration-day mechanic behind pitfall #4
- [[assignment-risk]] — the early-exercise mechanic behind pitfall #3
- [[options-trader-psychology]] — the behavioral substrate behind several pitfalls
- [[delta-hedging]], [[gamma-scalping]] — the professional flip side of pitfall #6
- [[volatility-risk-premium-decay]] — why short premium tends to win on average
- [[options-portfolio-construction]] — the sizing framework that defuses pitfalls 1, 6, 10
- [[lottery-stock-anomaly]] — the equity analogue of pitfall #5 (overpaying for positive skew)
- [[risk-management]] — the universal principles these pitfalls violate

## Sources

- [[2026-04-22-gap-finder-stock-options-trading-pitfalls-tradesta]] — gap-analysis source identifying these as wiki coverage gaps
