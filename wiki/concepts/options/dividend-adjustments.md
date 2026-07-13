---
title: "Dividend Adjustments in Options"
type: concept
created: 2026-05-03
updated: 2026-06-11
status: good
tags: [options, derivatives, dividends, risk-management]
aliases: ["Dividend Risk", "Ex-Dividend Risk", "Dividend Adjustments in Options"]
domain: [options, risk-management]
prerequisites: ["[[options]]", "[[options-pricing]]", "[[assignment]]"]
difficulty: intermediate
related: ["[[options]]", "[[options-pricing]]", "[[assignment]]", "[[covered-calls]]", "[[cash-secured-puts]]", "[[credit-spreads]]", "[[iron-condors]]", "[[early-exercise]]", "[[put-call-parity]]", "[[implied-volatility]]"]
---

Dividends affect [[options]] in two distinct ways: they shift the forward price used in [[options-pricing|pricing models]] (making calls cheaper and puts more expensive on dividend-paying stocks), and they create early-exercise risk on deep ITM short calls the day before ex-dividend. Most retail traders ignore both effects until they wake up to an unexpected assignment notice the morning of ex-dividend on a covered call they "shouldn't" have lost.

## How Dividends Shift Option Prices

The forward price of a stock is:

> F = S − PV(D)

where S is the spot price, D is the expected dividend before expiry, and PV(D) is its present value. Options price off the forward, not the spot. The implications:

- **Calls become cheaper** on dividend-paying stocks, because the forward price (which the call is effectively "exercised against") is lower than spot.
- **Puts become more expensive** on dividend-paying stocks, by the same logic — the forward is below spot, so the put is closer to ITM than spot would suggest.
- The relationship is enforced by [[put-call-parity]]: C − P = S − K·e^(−rT) − PV(D). The dividend term sits inside parity and the market arbitrages it.

For a $100 stock paying a $1.00 quarterly dividend in 30 days, with the option expiring in 60 days, PV(D) ≈ $1.00. The forward at 60 days is roughly $99. A 100-strike call on this stock prices about $0.50-$0.80 cheaper than an identical option on a non-dividend-paying $100 stock; the matching put prices about $0.50-$0.80 richer.

## Why Options Are NOT Adjusted for Ordinary Dividends

This is the common retail surprise: when a stock pays its regular quarterly dividend and the share price drops by the dividend amount on ex-date, **options contracts are not adjusted**. The strike stays the same, the multiplier stays at 100, and the deliverable stays at 100 shares. The option simply prices the dividend in via the forward; ex-date is a non-event from the contract's perspective.

The OCC adjusts contracts only for **special or extraordinary dividends**, which by rule are typically **cash distributions greater than 10% of the stock price** or any non-cash distribution (stock split, spinoff, return of capital). For these:

- Strike is reduced by the special dividend amount
- The deliverable may be modified to include the dividend in cash
- A new "non-standard" symbol is often issued (e.g., AAPL1 instead of AAPL)

A regular $0.96/year Apple dividend on a $200 stock (~0.5%) is far below threshold and is not adjusted. A one-time $5 special dividend on the same stock would clear the 10% test if the stock were $40 but not at $200, so even mid-sized specials often go un-adjusted. Always check the OCC memo when a special dividend is announced.

## The Real Trap: Early Exercise on Deep ITM Short Calls

This is where retail traders running [[covered-calls]] or call-side credit spreads get hurt. The setup:

- The trader is short a call (covered or as part of a spread).
- The underlying is paying a dividend tomorrow (ex-date).
- The call is **deep ITM** — its price is mostly intrinsic with very little extrinsic (time) value left.

A rational long-call holder will exercise their call early if and only if the dividend they capture by being long the stock on ex-date exceeds the extrinsic value they forfeit by exercising:

> **Early exercise is rational when: Dividend > Remaining extrinsic value of the call**

If they exercise tonight, they get the stock at the strike, hold through ex-date, and capture the dividend. The extrinsic value of the call is what they give up. If the dividend is larger, they pull the trigger.

The signal a short-call holder needs to monitor: on the day before ex-date, look at the bid/mid of the corresponding put at the same strike — that's roughly the call's extrinsic value (per put-call parity for ATM-to-ITM strikes). Compare to the dividend. If the put is worth less than the dividend, the call is at high risk of early exercise.

### Worked Example: Short $100 Call into a $0.75 Dividend

Stock at $108 the day before ex-date. Trader is short the $100 call (8 points ITM), 14 DTE.

- Call bid/ask: $8.55 / $8.65 (mid $8.60)
- Intrinsic: $108 − $100 = $8.00
- Extrinsic: $8.60 − $8.00 = **$0.60**
- Tomorrow's dividend: **$0.75**

A rational long-call holder exercises tonight: by giving up $0.60 of extrinsic and exercising at $100, they'll own stock through ex-date and pocket $0.75 of dividend — a net $0.15 per share gain over holding the option through ex-date and watching it lose $0.75 of intrinsic the next morning. The short-call holder is assigned overnight, has their shares called away at $100, and **does not receive the dividend** (the new long-stock holder does).

Compare to a $90 call on the same name: extrinsic might be $0.05 with intrinsic of $18 — almost certainly assigned. A $115 call: extrinsic $1.10 with intrinsic $0 — never assigned for the dividend (it's already OTM and there's still time value to lose).

The danger zone for short calls is **strikes 1-5% below spot, with extrinsic less than the dividend, in the day or two before ex-date.**

## Effect on Common Strategies

### Covered Calls

The most common retail dividend-assignment story. Trader sells a call against 100 shares for monthly income, the call goes ITM, ex-date approaches, the call's extrinsic drops below the dividend, and the trader is assigned. They lose:

- The dividend (which goes to the new stock owner)
- Any unrealized gains above the strike on their shares
- The basis they had in those shares

What they keep: the original premium and the strike. The trade still works mathematically — they sold a call and got assigned — but the dividend they expected to collect goes to whoever exercised the call against them.

### Iron Condors / Credit Spreads on Dividend Payers

Less commonly discussed but real: in a call credit spread, the *short* call can be early-exercised for a dividend, leaving the trader with a synthetic short stock position (short 100 shares + long deep ITM call). This is a margin event — overnight margin requirements jump and the long-call leg may need to be exercised manually to close. For [[iron-condors]] on dividend-paying single names, this risk argues for either:

- Closing the entire condor before ex-date when the call side is breached
- Sticking to non-dividend-paying underlyings (most index ETFs, growth stocks)
- Using SPX/NDX index options, which are European-style and cannot be exercised early at all

### Cash-Secured Puts

[[Cash-secured-puts|Cash-secured puts]] face the *opposite* concern: short puts on dividend stocks can be assigned early when the put is deep ITM and the dividend is small (because the put holder wants to capture the time value before the stock drops on ex-date). However, this is much rarer than the call case — it's usually only rational when interest rates are very low and the put is European-equivalent in moneyness.

## Practical Mitigation Checklist

For any short call position on a dividend-paying underlying:

1. **Mark ex-date in the trade journal at entry.** Don't get surprised.
2. **The day before ex-date, check the corresponding put price at the short strike.** If the put is worth less than the dividend, plan to roll or close the same day.
3. **Roll up-and-out** to a higher strike or later expiration if you want to keep the position. Rolling regenerates extrinsic value, raising it above the dividend and removing the early-exercise incentive.
4. **Close before ex-date** if you don't want to manage the assignment risk. Buy back the call, take the P&L, and re-enter after ex-date if desired.
5. **Avoid selling calls inside 1-3% of spot on dividend payers in the 1-2 weeks before ex-date** unless you actively want to be called away.
6. **For systematic premium-sellers**, prefer non-dividend ETFs (QQQ pays a small dividend; SPY pays quarterly; IWM pays small) or use index options (SPX, NDX, RUT) which are European-style cash-settled and have no early-exercise risk at all.
7. **Cross-check with dividend calendar tools** — tastytrade, thinkorswim, and most brokers flag upcoming ex-dates on the option chain.

## Special-Dividend Adjustment Example

In November 2012, Costco (COST) declared a $7 special dividend on a ~$100 stock — a 7% payout, *below* the OCC's 10% threshold. The OCC did not adjust contracts. Holders of November ITM calls who didn't exercise before ex-date watched the stock drop ~$7 and their calls lose ~$7 of intrinsic value with no offsetting compensation. The lesson: even with a publicized special dividend, if it's below the OCC threshold, the option contract treats it like an ordinary dividend and the early-exercise math applies.

In contrast, Microsoft's $3-per-share special dividend in 2004 (on a ~$30 stock, ~10% payout) *was* adjusted by the OCC, with strike prices reduced by $3.

## Related

- [[options]] — overview of contracts
- [[options-pricing]] — the model that incorporates the dividend term in the forward
- [[assignment]] — the broader mechanism of which dividend assignment is one trigger
- [[covered-calls]] — the strategy most exposed to dividend-related early assignment
- [[cash-secured-puts]] — the inverse case, much rarer
- [[credit-spreads]] — short-call leg can be assigned on dividend payers
- [[iron-condors]] — same risk on the call wing for single-name dividend stocks
- [[early-exercise]] — the broader phenomenon of which dividend exercise is the most common case
- [[put-call-parity]] — the no-arbitrage relationship that determines the dividend's effect on prices
- [[implied-volatility]] — extracted from option prices *after* removing the dividend forward effect

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
