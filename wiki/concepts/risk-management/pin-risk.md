---
title: "Pin Risk"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, risk-management, market-microstructure, derivatives]
aliases: ["Pin Risk", "Strike Pinning", "Pinning", "Pin", "Max Pain"]
related: ["[[expiration-laddering]]", "[[gamma-explosion]]", "[[zero-dte-options]]", "[[options-income]]", "[[short-strangle]]", "[[iron-condor]]", "[[covered-calls]]", "[[cash-secured-puts]]", "[[wheel-strategy]]", "[[managing-winners]]", "[[dealer-gamma-hedging]]", "[[market-makers]]", "[[settlement-process]]", "[[american-vs-european-options]]", "[[expected-shortfall]]"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[options-greeks]]", "[[options-expiration]]"]
difficulty: intermediate
---

**Pin risk** is the risk that an underlying closes *exactly at* (or extremely near) the strike of a short option position at expiration, leaving the trader uncertain whether the position will be exercised. The discomfort is not the option's value at expiration — by definition that is roughly zero — but the *post-close uncertainty*: an unhedged trader who believes a short call will expire worthless wakes up Saturday morning with an unwanted short stock position if the holder of the long call decides to exercise after the close. Strike pinning has a structural cause ([[dealer-gamma-hedging|dealer gamma hedging]]) and a structural cure (close before the bell, or use cash-settled instruments), and any [[options-income|income]] book trading physically settled options must handle it explicitly.

## Overview

The textbook model of options says: at expiration, an in-the-money option is exercised, an out-of-the-money option expires worthless, and an at-the-money option (S = K exactly) is a measure-zero event no one needs to plan for. Reality is messier on three fronts:

1. **At-the-money is not measure-zero in practice.** Liquid stocks pin to round-number strikes with surprising regularity, and the closing print can land within pennies of a strike often enough that "ATM at expiry" is a real, plannable event rather than a theoretical edge case. This pinning is itself a [[market-microstructure|microstructure]] phenomenon driven by dealer hedging flow.
2. **Exercise is a holder choice, not an automatic settlement.** [[american-vs-european-options|American-style]] options are exercised when the holder submits exercise instructions, which on the OCC's standard schedule can be done up to **90 minutes after the close** on expiration day. The short position has no information about exercise until the next trading session. The [[occ|OCC]] auto-exercises any option that is ITM by ≥$0.01 by default ("exercise by exception"), but the holder can override either direction — so being even $0.05 ITM does not guarantee exercise, and being $0.05 OTM does not guarantee non-exercise.
3. **The resulting overnight stock position has unhedged gap risk.** If a trader's short call gets assigned at $50 strike on a stock that closed Friday at $50.02, they wake up Monday with 100 shares short per contract — and any move in that stock between Friday's close and Monday's open is fully exposed.

Pin risk is not the small ATM mark-to-market loss; it is the structural mismatch between *what you thought you held* and *what you woke up holding*. The fix is operational, not financial: don't carry physically-settled short options with strikes anywhere near spot through expiration.

## Definition / Mechanism

**Pin risk** has two distinct components, often conflated:

### 1. Pinning (the spot phenomenon)

The market microstructure observation that liquid stocks tend to gravitate toward round-number strikes in the final hours of expiration day. The mechanism is [[dealer-gamma-hedging|dealer gamma hedging]]:

- Market makers are typically long gamma at strikes where retail and other client flow is heavily short premium (especially weekly and monthly expirations).
- A long-gamma dealer hedges by **buying low and selling high** — selling delta as the underlying rises through the strike, buying delta as it falls back.
- Aggregated across all dealers and all clients, this creates a mean-reverting force toward the strike with the most open interest as expiration approaches.
- The "max-pain" theory (the strike at which the most options expire worthless across all open interest) is a crude approximation of where this gravitational pull aims.

Pinning is a real, measurable phenomenon documented in academic literature ([[ni-pearson-poteshman|Ni, Pearson, and Poteshman 2005]] *Stock Price Clustering on Option Expiration Dates*, *Journal of Financial Economics*) and in practitioner data: in liquid optionable equities, the closing price on monthly expiration Fridays clusters at integer-multiple strikes (or $5 / $10 multiples for higher-priced names) at materially higher frequency than non-expiration days.

### 2. Pin risk (the position-level uncertainty)

The trader-level consequence of pinning: a short option whose strike is the pinning strike is in the worst possible state at expiration. It is neither comfortably ITM (clearly assigned, plan accordingly) nor comfortably OTM (clearly worthless, walk away). The post-close period — between the 4:00 pm equity close and the OCC's exercise cutoff — is a period of binary, uncontrollable risk:

- **If exercised**: the trader's account is delivered a stock position they did not want.
- **If not exercised**: the trader walks away clean.

The exposure is the *difference* between those two states, and that difference is the underlying's overnight gap multiplied by the contract multiplier. For a 100-share equity option, a $1 gap on Monday open is $100 per contract of pin-risk P&L the trader had no control over.

### Settlement style determines whether pin risk exists at all

The single most important fact about pin risk is that it is a property of **physically settled, American-style** options. Cash-settled and European-style instruments eliminate the exercise-decision ambiguity entirely.

| Instrument | Settlement | Exercise style | Pin risk? |
|---|---|---|---|
| [[spy\|SPY]], QQQ, IWM (ETF options) | Physical (deliver shares) | American | **Yes** — full pin risk |
| Single-name equities (AAPL, TSLA, …) | Physical (deliver shares) | American | **Yes** — full pin risk |
| [[spx-options\|SPX]], NDX, RUT (index options) | Cash | European | **No** — cash settles automatically |
| [[xsp\|XSP]] (mini-SPX) | Cash | European | **No** |
| Most futures options (ES, NQ) | Cash (on the future) / physical (into future) | American | Reduced — depends on contract |
| VIX options | Cash | European | **No** |

The practical takeaway is direct: an [[options-income]] book with no need for single-name exposure can make pin risk disappear by trading the cash-settled index complex (SPX instead of SPY, NDX instead of QQQ). This is mitigation #2 below, and it is the cleanest one.

## How It Works

### The exercise window

US equity options trading closes at 4:00 pm ET. Holders of long options have until **5:30 pm ET** (90 minutes later, OCC standard) to submit explicit exercise or non-exercise instructions to their broker. The broker then submits to the OCC, which clears overnight. For [[index-options|cash-settled index options]] like SPX, this window is a non-issue (cash settlement is automatic). For physically settled options on individual equities, ETFs, and most futures-options, the 90-minute window is when pin risk lives.

The holder's incentive structure during this window:

- A long ITM call has positive intrinsic value; the holder almost always exercises (or sells in the closing minutes, transferring the issue to whoever bought).
- A long OTM call has zero intrinsic value; the holder almost never exercises (paying strike to acquire stock worth less makes no sense).
- A long ATM call — strike within pennies of spot — is the genuinely ambiguous case. The holder sees post-close after-hours news, futures ticks, and any other information that emerges in the 90-minute window before deciding.

This last bullet is where pin risk lives. The holder might exercise based on post-close news (an upbeat earnings pre-announcement, a takeover rumour) and the short trader has zero ability to anticipate.

### Why dealers can't fix it

A market maker carrying a delta-hedged short position into expiration also faces pin risk on their inventory, but they can manage it with significantly more sophistication than a retail trader: scale-out of the position in the closing minutes, hold offsetting positions in different cycles, and so on. The retail trader has none of these tools and typically faces pin risk on a single concentrated position. The asymmetry is precisely what makes the discipline of *closing before the close* the canonical retail rule.

### The asymmetry of the bad outcome

The bad outcome of pin risk is asymmetric in a way that compounds the problem. Consider a [[short-strangle|short strangle]] trader pinned at the upper strike on a stock that closes at $100.01 against a $100 short call:

- **Best case** (option not exercised): trader walks away clean. P&L = full credit.
- **Worst case** (option exercised): trader receives -100 shares short at $100. Monday gap +5% on overnight news = -$500 unhedged loss per contract.

The expected value of the bad outcome is large enough that it dwarfs the credit collected on the strangle. A trader who runs into pin risk a few times a year erodes a meaningful fraction of annual income on these post-close gap events alone. This is why systematic [[options-income|income]] traders treat *avoiding pin risk* as an operational hard rule, not a "manage as it comes" tactic.

## Real-World Cases

### Routine pinning in mega-caps

[[apple|AAPL]], [[microsoft|MSFT]], [[tesla|TSLA]], [[nvidia|NVDA]], and [[spy|SPY]] all show pronounced pinning on monthly expiration days. AAPL, in particular, has closed within $0.50 of a $5 strike on more than 60% of monthly expirations in the post-2015 sample, materially more than the unconditional probability would predict. The Ni-Pearson-Poteshman work originally documented this effect on liquid US stocks; subsequent work by [[golez-jackwerth|Golez and Jackwerth]] (2012) extended it to index futures.

### High-profile pinning incidents

- **[[gamestop-saga|GameStop January 2021]]**: GME closed Friday January 22, 2021 at $65.01 after wild intraday volatility, pinning to the $65 strike where the largest weekly call open interest sat. Many short-call positions written earlier in the week as low-probability tails were caught at-the-money, and the following Monday's gap (open near $96) generated huge pin-risk losses for unhedged short-call writers.
- **[[tesla|Tesla]] earnings/expiry overlaps**: TSLA's habit of releasing significant news on or near expiration days has produced repeated pinning events at strikes that subsequently moved several percent overnight, generating exactly the asymmetric pin-risk loss profile.
- **Index futures options**: cash-settled SPX and ES futures options avoid the physical-settlement pin risk entirely, which is one reason institutional [[options-income]] books prefer them.

### A worked numerical example

A trader is short a single SPY $470 call expiring Friday with no offsetting position. SPY closes Friday at $470.04.

- The OCC's exercise-by-exception threshold is $0.01 ITM, so the call will auto-exercise unless the holder explicitly submits non-exercise.
- After-hours trading sees SPY drift down to $469.95 on light volume.
- The holder submits non-exercise (rationally — the call is now OTM in after-hours).
- Trader expected to be assigned, plans hedge accordingly with -100 SPY at $470.04.
- Monday open: SPY +1.8% on overnight macro news, opens at $478.50.
- Trader is **not short SPY** (the call expired worthless), but they had pre-positioned the short hedge on Friday afternoon.
- The pre-positioned -100 SPY hedge is now down -$8.46 per share = -$846.

The same trade with the opposite outcome (trader did *not* hedge, expecting non-exercise) and post-close +0.5% drift triggering exercise:

- Trader is now short -100 SPY at $470 acquired post-close.
- Monday open: SPY +1.8% gap to $478.50.
- Trader closes the short at the open: -$8.50 × 100 = -$850 loss.

In both cases the loss is roughly the same magnitude — and roughly equal to a *full week's* theta on the position the trader was running. Pin risk is not a small effect.

## Mitigation

The hierarchy of mitigations, ordered from cleanest to most reluctant. Use this table as the at-a-glance decision aid; the detail follows below.

| # | Mitigation | Eliminates pin risk? | Cost | Best for |
|---|---|---|---|---|
| 1 | Close before the bell | Yes (position gone) | Small extrinsic giveup (pennies) | Every retail trader; the default rule |
| 2 | Trade cash-settled instruments | Yes (no exercise decision) | Tax/granularity/selection tradeoffs | [[options-income]] books with no single-name need |
| 3 | Defined-risk structures ([[iron-condor]]) | No — but **caps** the loss | Reduced theta per contract | Books that must carry through expiry |
| 4 | Roll to a different expiry | Converts to duration risk | Small debit | Maintaining a structure with extrinsic left |
| 5 | Pre-hedge with the underlying | Partially | Directional bet during the window | Wheel traders who sometimes want assignment |
| 6 | Exercise-and-cover at the open | No — accepts assignment | Borrow/financing + gap exposure | Short puts with cash to take delivery |

### 1. Close before the close (the canonical rule)

Close any short option whose strike is within ~1% of spot before the closing bell on expiration day. This is the universally recommended retail approach; [[tastytrade]], [[itpm-trading-philosophy|ITPM]], and most published [[options-income|options-income]] curricula state it as a hard rule. The cost is a small premium giveup (the option's residual extrinsic value, often pennies); the benefit is total elimination of pin risk.

A common heuristic: **close any short option for which $|S - K| < 0.5 \times \text{ATR(20)}$ as the bell approaches**, where ATR is the 20-day average true range of the underlying. For low-vol stocks this is a tight band; for high-vol stocks the safe distance is much wider.

### 2. Trade cash-settled instruments

Cash-settled options ([[spx-options|SPX]], [[xsp]], [[ndx]], [[rut]], most index options globally) eliminate physical pin risk entirely. Settlement is in cash on the morning after expiration based on the official settlement print; there is no exercise decision and no resulting share position. For [[options-income]] books with no fundamental need for single-name exposure, switching from SPY to SPX (or QQQ to NDX) is the single cleanest mitigation. The cost is slightly different tax treatment (1256-contract, 60/40 treatment in the US for SPX), different position size granularity, and reduced selection — but pin risk goes away.

### 3. Trade defined-risk structures

A long wing protects against the worst case of pin risk. An [[iron-condor]] short call at $470 with a long call at $475 caps the maximum loss: in the worst-case pin-then-gap scenario, the long call is also assigned (or exercised by the trader), and the loss is capped at the wing width minus credit received. The cost is reduced theta per contract; the benefit is bounded pin-risk loss.

### 4. Roll out to a different expiry

If the short option is pinned on Friday afternoon and closing the position is unattractive (still has appreciable extrinsic, or the trader wants to maintain the structure), roll out to a future expiration. This converts pin risk into duration risk, which is far more manageable.

### 5. Pre-hedge with the underlying

For traders who must carry the position through expiry (e.g., wheel strategy practitioners who *want* assignment in some scenarios), pre-position a hedge in the underlying that flattens the post-exercise delta. The risk: the hedge is itself a directional bet between the close and the assignment notification.

### 6. Use exercise-and-cover at the open

A more aggressive approach: accept potential assignment, but plan to exercise-and-cover at Monday's open. Works for short puts where the trader has cash to take delivery; less viable for short calls (requires borrowing stock).

## Worked Example — Wheel-Strategy Trader

A trader runs a [[wheel-strategy|wheel]] on AAPL: sell weekly cash-secured puts at $0.20-$0.30 delta, get assigned on dips, sell covered calls against the assigned stock. Friday's expiration:

- AAPL spot: $185.40
- Short put strike: $185 (at-the-money)
- Trader holds 100% cash collateral; assignment is acceptable (this is part of the strategy).
- But unwanted: trader doesn't actually want to be assigned on this expiry — wanted the put to expire OTM.

Options:

1. **Close the put**: pay ~$0.40-$0.60 in extrinsic, walk away clean. Trader does this if the credit collected was meaningful and the assignment isn't desired.
2. **Roll the put**: close the $185 weekly put, open next-week's $182 put. Pays a small debit but converts pin risk to a higher-premium continuation trade.
3. **Accept the pin**: leave the put open. If AAPL closes $184.99, holder probably exercises (auto-exercise threshold), trader gets 100 shares at $185 = $18,500 cash deployed. Trader sells covered calls Monday morning. Risk: AAPL gaps -3% Monday on news → trader has $-555 unrealised loss before any covered-call premium.

The wheel-strategy practitioner's standard rule: **always close or roll any pinned position before the bell**. The strategy's edge is the [[variance-risk-premium]], not pin gambling. Accepting pin risk is a separate, uncompensated bet.

## Common Misuse / Limitations

1. **Confusing pin risk with assignment risk.** Assignment of a clearly-ITM short option is *expected* — the trader knows the position is being assigned and can plan. Pin risk is the *uncertain* assignment when the strike is at-the-money. They are different operational problems with different mitigations.
2. **Ignoring after-hours moves.** The 90-minute exercise window means after-hours news can flip the holder's decision. Traders who rely on the 4:00 pm print as the deciding factor can be wrong-footed by post-close moves on biotech approvals, earnings pre-announcements, or macro news.
3. **Trusting auto-exercise thresholds blindly.** The OCC's $0.01 threshold is a *default*, not a guarantee. Sophisticated holders override in either direction. A short option that's $0.05 OTM at the close can still be exercised; one that's $0.05 ITM can be allowed to expire. Plan for both states.
4. **Underestimating overnight gap risk.** The post-assignment overnight position is the actual exposure, not the expiration-day P&L. A 0.5% expected pin discrepancy plus a 2% expected overnight move = a 2.5% effective exposure on a position the trader thought was already closed.
5. **Forgetting weekend-and-holiday compounding.** Friday expirations carry both a weekend and any Monday holidays before the next session. A 3-day exposure on a "closed" position is a real number.
6. **Treating cash-settled and physical-settled identically.** SPX, NDX, XSP, RUT have no pin risk in the physical-settlement sense. SPY, QQQ, IWM, and individual equities all do. Mixing the two in a portfolio is fine, but the operational rules differ.
7. **Selling 0DTE without an exit plan.** [[zero-dte-options]] are pin risk all day on expiration day. The further the position goes ATM in the final hour, the more dangerous. A 0DTE income trader without a hard close-by-3:55 rule is running uncovered pin risk on every trade.

## Related

- [[expiration-laddering]] — diversifying across cycles is the strategic answer to pin risk concentration.
- [[gamma-explosion]] — the gamma side of expiration risk; pin risk is the assignment side.
- [[zero-dte-options]] — the highest-pin-risk exposure category.
- [[options-income]] — the strategy class most exposed to pin risk in routine operation.
- [[short-strangle]] / [[iron-condor]] / [[covered-calls]] / [[cash-secured-puts]] — the structures that face pin risk on each expiry.
- [[wheel-strategy]] — strategy where assignment is sometimes intentional but pin risk remains a discipline issue.
- [[managing-winners]] — the closing-before-expiry rule (often "close at 50% max profit" or "close 21 DTE") is itself a pin-risk mitigation.
- [[dealer-gamma-hedging]] — the structural cause of pinning.
- [[market-makers]] — who provides the liquidity that creates the pinning effect.
- [[settlement-process]] / [[american-vs-european-options]] — the institutional plumbing.
- [[expected-shortfall]] — the right risk metric for the fat-tailed pin-risk loss distribution.

## Sources

- Ni, S. X., Pearson, N. D., and Poteshman, A. M. (2005). *Stock Price Clustering on Option Expiration Dates*. *Journal of Financial Economics*, 78(1): 49-87. The foundational empirical study documenting strike pinning on monthly expirations.
- Golez, B., and Jackwerth, J. C. (2012). *Pinning in the S&P 500 Futures*. *Journal of Financial Economics*, 106(3): 566-585. Extends the pinning literature to index futures.
- [[occ]] Bylaws and Exercise Procedures — official documentation on the auto-exercise threshold and exercise windows.
- [[cboe]] / [[cme]] settlement procedure guides — institutional descriptions of physical vs cash settlement and the practical implications for traders.
- [[tastytrade]] research notes on closing-before-expiry as a standard income-trade discipline.
- [[itpm-trading-philosophy|ITPM]] curriculum on operational discipline at expiry.
