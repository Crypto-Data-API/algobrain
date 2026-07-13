---
title: "Assignment"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives]
aliases: ["Assignment", "Options Assignment", "Exercise and Assignment", "Early Assignment"]
domain: [derivatives]
prerequisites: ["[[options]]", "[[options-pricing]]"]
difficulty: intermediate
related: ["[[options]]", "[[covered-calls]]", "[[cash-secured-puts]]", "[[options-pricing]]", "[[theta]]", "[[occ]]", "[[pin-risk]]"]
---

Assignment is the process by which a short [[options|option]] holder is obligated to fulfill the terms of the contract when the option buyer exercises their right. For a short call, assignment means the seller must deliver (sell) shares of the underlying at the strike price. For a short put, assignment means the seller must buy shares at the strike price. Assignment is the mechanism through which options obligations become actual stock transactions.

## How Assignment Works Mechanically

When an option holder exercises, the Options Clearing Corporation (OCC) randomly assigns the exercise notice to a broker with a matching short position, who then assigns it to a client account (typically at random). Assignment can occur on any business day for **American-style** options (which can be exercised at any time before expiration), but only at expiration for **European-style** options. Most equity and ETF options in the US are American-style; index options (e.g., SPX) are typically European-style and cash-settled, meaning assignment results in a cash transfer rather than stock delivery.

### What you owe when assigned

| You are short a... | On assignment you must... | At what price |
|--------------------|---------------------------|---------------|
| **Call** | Deliver (sell) 100 shares per contract | The strike price |
| **Put** | Buy 100 shares per contract | The strike price |

Worked example — short put: you sold one **$45-strike put** for a $1.50 premium ($150 collected). At expiration the stock is at **$42**, so the put is $3 in-the-money and you are assigned. You must buy 100 shares at $45 ($4,500 cash out) even though the market price is $42. Your effective cost basis is $45 − $1.50 premium = **$43.50/share**, a paper loss of $1.50/share versus the $42 market — exactly the [[cash-secured-puts|cash-secured put]] outcome, which is why sellers keep the strike's worth of cash on hand.

Worked example — short call: you wrote one **$55-strike covered call** for $1.00 against 100 shares bought at $50. The stock rallies to $60 and you are assigned: you deliver your 100 shares at $55. Your total proceeds are the $55 strike + $1.00 premium = **$56/share**, a fine outcome — but you forgo the move above $55. This is the planned, "happy" assignment of a [[covered-calls|covered call]].

## Early Assignment Risk

Early assignment -- being assigned before expiration -- is the primary concern for short option sellers. It occurs most commonly in two scenarios. First, short calls on stocks approaching an **ex-dividend date**: if the remaining time value of the call is less than the dividend amount, it becomes rational for the call holder to exercise early to capture the dividend. [[covered-calls|Covered call]] sellers should be particularly aware of this risk when writing calls on dividend-paying stocks. Second, **deep in-the-money puts** may be exercised early when the remaining time value is minimal and the put holder wants to free up capital. The general rule is that early assignment risk is negligible when the option has significant time value remaining, since exercising would forfeit that time value.

## Pin Risk

A special hazard at expiration is **pin risk**: when the underlying closes very close to the strike, the short seller does not know with certainty whether they will be assigned. An option that is fractionally in-the-money at the close is subject to automatic exercise by the OCC (the "exercise-by-exception" threshold for equity options is $0.01 in-the-money), but the holder can also submit a contrary instruction, and after-hours moves can flip the economics. A trader who assumes they will *not* be assigned can wake up Monday holding (or short) a stock position that gaps against them over the weekend. The standard mitigation is to close near-the-money short options before the close on expiration day rather than letting them expire.

## Managing Assignment

For strategies like [[covered-calls]] and [[cash-secured-puts]], assignment is a planned outcome rather than a catastrophe -- the seller has the underlying shares (covered call) or sufficient cash (cash-secured put) to fulfill the obligation. For naked or spread positions, unexpected assignment can create unwanted stock positions and margin issues. Notably, with a vertical spread, getting assigned on the short leg before expiry while the long leg remains unexercised leaves the trader with a directional stock position plus financing/margin demands until they exercise the long leg or close out. Traders managing short options positions should monitor their options' proximity to being in-the-money, upcoming dividends (see ex-dividend-date), and the remaining [[theta|time value]] to anticipate and manage assignment risk.

## Trading Relevance

Assignment risk is the structural cost embedded in any short-premium strategy. Because assignment is random within a broker's pool of short positions, it cannot be predicted account-by-account, only managed probabilistically — keep significant time value in short options, avoid carrying short calls through ex-dividend dates when the dividend exceeds the call's remaining extrinsic value, and treat near-the-money expiration as a position to be actively closed rather than passively held. For income strategies, every assignment is a transaction-cost event (commissions on the resulting stock trade plus the unwind), so the frequency of assignment directly erodes net yield.

## How Traders Manage Assignment Risk

A practical checklist for anyone running short-premium strategies:

| Situation | Risk | Mitigation |
|-----------|------|------------|
| Short call, dividend approaching | Early assignment to capture the dividend | Compare remaining extrinsic value vs. dividend; roll or close before ex-dividend-date if extrinsic < dividend |
| Deep ITM short put | Early exercise to free up capital | Roll down/out before extrinsic value disappears |
| Near-the-money at expiration | [[pin-risk]] — assigned or not? | Close the short before the bell; do not gamble on the close |
| Short leg of a vertical spread assigned | Naked stock position + margin call | Exercise the long leg or close the whole position promptly |
| High [[implied-volatility|IV]] / wide bid-ask | Assignment plus costly unwind | Trade liquid underlyings; size positions for the cash/shares to deliver |

**Rule of thumb:** as long as a short option retains meaningful **extrinsic ([[theta|time]]) value**, early assignment is unlikely, because the exerciser would be throwing that value away. Assignment risk spikes precisely when extrinsic value approaches zero — deep ITM, near expiration, or just before an ex-dividend date.

## Common Pitfalls

- **Assuming OTM means safe at the close.** After-hours moves can push a near-the-money option ITM and trigger exercise-by-exception over the weekend.
- **Forgetting the long leg of a spread.** Being assigned on the short leg alone converts a defined-risk spread into an undefined directional stock position until you act.
- **Holding short calls through dividends.** This is the single most common avoidable early-assignment event.
- **Ignoring style/settlement.** Treating a European cash-settled index option like an American equity option, or vice versa, leads to nasty surprises.

## Related

- [[options]] -- the instruments that can result in assignment
- [[covered-calls]] -- strategy where assignment is a defined, acceptable outcome
- [[cash-secured-puts]] -- strategy that accepts assignment as a way to acquire stock at a target price
- [[options-pricing]] -- understanding time value is key to predicting assignment risk
- [[theta]] -- remaining time value determines whether early exercise is rational

## Sources

- Options Clearing Corporation (OCC), *Characteristics and Risks of Standardized Options* (the "options disclosure document") — official source on exercise/assignment mechanics and exercise-by-exception.
- Sheldon Natenberg, *Option Volatility and Pricing* (2nd ed., 2014) — early-exercise economics for dividends and deep ITM options.
- CBOE, "Expiration, Exercise and Assignment" educational materials.
