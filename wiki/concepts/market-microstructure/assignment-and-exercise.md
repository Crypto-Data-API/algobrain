---
title: "Assignment and Exercise"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: good
tags: [options, derivatives, market-microstructure]
aliases: ["Option Exercise", "Option Assignment", "Early Exercise", "Pin Risk", "Exercise and Assignment"]
domain: [market-microstructure]
prerequisites: ["[[options]]", "[[call-options]]", "[[put-options]]", "[[moneyness]]"]
difficulty: intermediate
related: ["[[options]]", "[[american-vs-european-options]]", "[[moneyness]]", "[[covered-call]]", "[[cash-secured-put]]", "[[put-call-parity]]", "[[theta]]", "[[dividends]]"]
---

Exercise is the act of converting an option contract into a position in the underlying asset. Assignment is what happens to the option seller (writer) when the buyer exercises — the seller is obligated to fulfill the contract. Understanding exercise and assignment mechanics is critical for avoiding unexpected stock positions, managing dividend risk, and making rational decisions about whether to exercise, hold, or close an option position.

## Basic Mechanics

### Exercise

| Action | Call Exercise | Put Exercise |
|--------|-------------|-------------|
| What the buyer gets | Buys 100 shares at the strike price | Sells 100 shares at the strike price |
| When it makes sense | Stock price > strike (ITM) | Stock price < strike (ITM) |
| Cash requirement | Strike × 100 (to buy shares) | Must own 100 shares (or go short) |

### Assignment

| Action | Short Call Assignment | Short Put Assignment |
|--------|----------------------|---------------------|
| What the seller must do | Sell 100 shares at the strike price | Buy 100 shares at the strike price |
| Effect if holding stock | Shares called away (covered call) | Stock purchased at strike |
| Effect if no stock | Short 100 shares created | Long 100 shares purchased |
| Cash requirement | Deliver shares (or margin for short) | Strike × 100 (to buy shares) |

### The Process

1. The option holder submits an exercise notice to their broker
2. The OCC (Options Clearing Corporation) randomly assigns the exercise to a seller
3. Assignment is typically processed overnight — the stock position appears the next morning
4. For American-style options, this can happen any day before expiration
5. For European-style options (SPX, index options), this only happens at expiration

## Automatic Exercise at Expiration

The OCC automatically exercises options that are **$0.01 or more in-the-money** at expiration. This is called "exercise by exception." Key details:

- Options expire at 4:00 PM ET on expiration Friday (standard equity options)
- SPX and index options settle based on the opening price the morning after expiration (AM settlement) or the closing price (PM settlement) depending on the contract
- **Do-not-exercise instructions**: You can submit a DNE instruction to your broker if you hold an ITM option and do NOT want to exercise (rare, but relevant when exercise costs exceed the option's intrinsic value due to commissions or margin implications)
- After-hours moves can turn an OTM option ITM (or vice versa) between 4:00 PM and the exercise cutoff — this is a source of **pin risk**

## Early Exercise (American Options)

American-style options (most single-stock options) can be exercised any time before expiration. Early exercise is only rational in specific situations:

### When Early Exercise Makes Sense

**Long calls — almost never**, except:
- **Deep ITM calls on stocks about to go ex-dividend**: If the dividend exceeds the remaining time value of the call, exercising early to capture the dividend is optimal. The rule of thumb: exercise if the dividend > put price at the same strike (this follows from [[put-call-parity]])
- When the remaining time value is less than the cost of carry (rare in low interest rate environments)

**Long puts — more common**:
- **Deep ITM puts**: When the put is so deep ITM that its time value approaches zero, exercising early converts the put into cash (short stock at the strike). The cash earns interest, which may exceed the forgone time value. This is more common when interest rates are high.
- When borrow costs for the underlying stock are very high (the short stock position earns the borrow rebate)

### Early Assignment Risk for Sellers

If you are short an American-style option, you face early assignment risk. The highest-risk scenarios:

1. **Short calls on dividend-paying stocks**: Just before the ex-dividend date, call holders may exercise to capture the dividend. If you are short a deep ITM call, assignment the night before ex-div is likely.

2. **Short deep ITM puts**: When interest rates are high, put holders exercise deep ITM puts early to receive the strike price in cash and earn interest.

3. **Short ITM options near expiration**: As time value approaches zero, there is no cost to the holder of exercising, so early exercise becomes more common.

**What to do**: Monitor short option positions for early exercise risk. If the time value of your short option drops below the dividend (for calls) or below the interest on the strike (for puts), consider closing the position before assignment occurs.

## Pin Risk

Pin risk occurs when the underlying price is very close to a strike price at expiration. The option may be slightly ITM and auto-exercised, slightly OTM and expire worthless, or fluctuate between the two in the final minutes/after-hours.

### Why Pin Risk Matters

- **For option sellers**: You don't know if your short option will be exercised until the next morning. You might wake up with an unexpected stock position that gaps against you overnight.
- **For spread holders**: If only one leg of your spread is exercised, you may be left with a naked stock position. Example: a short call spread where the short call is assigned but the long call expires worthless — you're now short 100 shares with no hedge.
- **For market makers**: Pin risk is a major source of overnight exposure, which is why heavy hedging activity occurs near strikes with large open interest at expiration.

### Managing Pin Risk

1. **Close positions before expiration**: The simplest solution — close any options near the money before the final hour of trading
2. **Exercise your long leg**: If you hold a spread and the short leg is at risk of assignment, exercise the long leg to offset
3. **Monitor after-hours trading**: Stock moves after 4:00 PM can change the exercise outcome
4. **Avoid holding near-ATM short options into expiration**: Close or roll early

## Cash vs. Physical Settlement

| Settlement Type | How It Works | Common In |
|----------------|-------------|-----------|
| **Physical delivery** | Actual shares change hands (buy/sell 100 shares per contract) | Single-stock equity options |
| **Cash settlement** | Difference between strike and settlement price paid in cash | Index options (SPX, NDX, RUT), VIX options |

Cash-settled options eliminate assignment risk entirely — there is no stock position created. This is one advantage of trading SPX options over SPY options.

## The Dividend Play

A common retail options scenario involves [[covered-call]] writers and dividends:

1. You own stock and sell a covered call
2. The stock approaches ex-dividend with the call deep ITM
3. The call buyer exercises the night before ex-div
4. Your stock is called away at the strike price
5. You do NOT receive the dividend (because you no longer own the stock on ex-div morning)

To avoid this, monitor the time value of short calls approaching ex-dividend dates. If time value < dividend, consider buying back the call or rolling it.

## Spread-Related Assignment Scenarios

### Vertical Spread Assignment

If you hold a short vertical spread and the short leg is assigned:

- **Short put spread**: Assignment = you buy stock at the short put strike. You still hold the long put as protection. You can exercise the long put to close the position, sell the stock, or hold it.
- **Short call spread**: Assignment = you sell stock short at the short call strike. You still hold the long call as protection.

The key risk: **margin**. Even though your long leg provides defined risk, the stock position created by assignment may require margin overnight before you can exercise your long leg the next morning. Ensure your account has sufficient margin for potential assignment scenarios.

### Iron Condor / Iron Butterfly Assignment

If only one short leg of an [[iron-condor]] or [[iron-butterfly]] is assigned, you end up with a stock position plus the remaining spread legs. This is usually resolved by closing the stock position and the remaining options the next morning, but overnight gap risk exists.

## Options Approval Levels

Most brokers require graduated options approval:

| Level | Allowed Strategies | Typical Requirements |
|-------|-------------------|---------------------|
| **Level 1** | Covered calls, cash-secured puts | Stock ownership or full cash collateral |
| **Level 2** | Long calls, long puts | Basic options knowledge |
| **Level 3** | Spreads (debit and credit) | Options experience, margin account |
| **Level 4** | Naked puts, strangles | Significant experience, high account value |
| **Level 5** | Naked calls | Extensive experience (highest risk) |

## Related

- [[options]] — foundational options concepts
- [[american-vs-european-options]] — exercise style determines assignment risk
- [[moneyness]] — exercise decisions depend on ITM/OTM status
- [[covered-call]] — assignment risk management for call writers
- [[cash-secured-put]] — assignment is the intended outcome
- [[put-call-parity]] — explains when early exercise is rational
- [[theta]] — time value determines whether exercise is optimal
- [[iron-condor]] — managing assignment risk in multi-leg positions

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg's treatment of early exercise, dividend-related exercise, and assignment risk
- [[book-options-futures-other-derivatives]] — Hull's formal analysis of optimal early exercise boundaries
