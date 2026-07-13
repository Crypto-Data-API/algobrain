---
title: "Conversion & Reversal Arbitrage"
type: strategy
created: 2026-04-15
updated: 2026-06-20
status: excellent
tags: [arbitrage, options, technical-analysis, market-microstructure]
aliases: ["Conversion Reversal Arbitrage", "Conversion Arbitrage", "Reversal Arbitrage", "Synthetic Arbitrage"]
strategy_type: quantitative
timeframe: intraday|swing
markets: [stocks, options]
complexity: advanced
backtest_status: untested
edge_source: [structural]
edge_mechanism: "Exploits violations of put-call parity — temporary mispricings between options and their synthetic equivalents"
related: ["[[put-call-parity]]", "[[box-spread]]", "[[volatility-arbitrage]]", "[[arbitrage-overview]]", "[[options-overview]]", "[[delta-neutral]]", "[[dividend-arbitrage]]", "[[arbitrage-parameter-cheatsheet]]", "[[leg-risk]]"]
---

# Conversion & Reversal Arbitrage

Conversion and reversal arbitrage exploit violations of [[put-call-parity]] — the fundamental pricing relationship between calls, puts, and the underlying asset. When the relationship breaks (even briefly), an arbitrageur locks in a risk-free profit by constructing a synthetic position that replicates the mispriced instrument.

These are among the **purest forms of options arbitrage** — in theory, completely risk-free. In practice, early exercise risk, borrow costs, dividend timing, and pin risk introduce residual risks that must be managed.

## Edge source

Per [[edge-taxonomy]], this is a pure **structural** edge — arguably the most structural in the entire strategy catalog. There is no forecast, no behavioral mispricing to exploit, and no risk premium being harvested. The "edge" is simply that the no-arbitrage condition [[put-call-parity]] must hold, and when transient supply/demand imbalances in one leg push the synthetic price away from the cash-plus-financing price, an arbitrageur can lock the difference. The profit is bounded above by the size of the parity violation, which is itself bounded by how far a competitive market lets prices drift before someone closes it.

## Why this edge exists (and why it is thin)

- **Who is on the other side**: whoever created the imbalance — a large directional buyer of one option lifting offers, a forced unwind dumping a leg, a market maker temporarily skewing quotes to manage inventory, or a retail order routed at a stale price. They are not "losing" in a behavioral sense; they are paying for immediacy or liquidity, and the conversion/reversal desk supplies it.
- **Why it persists at all**: the arbitrage requires capital, balance-sheet (margin on stock + options), borrow access for reversals, and the operational ability to execute multiple legs near-simultaneously. These barriers mean the edge is never *fully* competed away — but they also mean it is captured almost entirely by market makers and proprietary desks running it continuously and at scale.
- **Why the edge is structurally thin**: because the relationship is mechanical and continuously monitored by hundreds of automated systems, violations are tiny (typically **0.01-0.10% of notional**, see Performance Characteristics) and fleeting. The thinness is not a flaw in the strategy — it is the *signature* of a true structural arbitrage. A "fat" parity violation would mean either a calculation error (mismodeled dividend, rate, or borrow) or a real residual risk (impending early exercise, hard-to-borrow recall) that makes the trade not actually riskless. **If it looks too good, you are missing a cost.**

## Null hypothesis

Under a frictionless, no-arbitrage market, [[put-call-parity]] holds *exactly* at all times and expected profit from conversions/reversals is **zero** — the synthetic and the real position always cost the same. Any observed profit must therefore come from one of: (1) a real, transient violation net of *all* frictions, or (2) an un-modeled cost masquerading as profit. The discriminating test is brutal: after fully loading bid-ask on every leg, commissions, borrow/financing, dividend risk, and early-exercise probability, does positive expectancy survive? For all but the most efficient operators with the lowest cost base, the honest answer at retail scale is **no** — which is why this is a market-maker strategy, not a retail one.

## The Put-Call Parity Relationship

For European-style options:
```
Call - Put = Stock - PV(Strike) - PV(Dividends)
```

Or equivalently:
```
C - P = S - K × e^(-rT) - D × e^(-r×t_d)
```

Where: C = call price, P = put price, S = stock price, K = strike price, r = risk-free rate, T = time to expiry, D = dividend, t_d = time to ex-dividend date.

When this equation doesn't hold, a conversion or reversal captures the difference.

## Strategy Mechanics

### Conversion (Synthetic Short = Real Long)

A conversion profits when the synthetic short (long put + short call at the same strike) is **more expensive** than shorting the stock:

| Leg | Position | Purpose |
|---|---|---|
| 1. **Buy stock** | Long 100 shares | Real long exposure |
| 2. **Buy put** | Long 1 put (same strike, same expiry) | Downside protection |
| 3. **Sell call** | Short 1 call (same strike, same expiry) | Upside cap |

**Result:** Delta-neutral position. The combined position has zero directional exposure. Profit = any deviation from put-call parity.

**Profit formula:**
```
profit = (call_bid - put_ask) - (stock_ask - strike × e^(-rT)) - dividends - borrow_cost
```

If this is positive, the conversion is profitable.

### Reversal (Synthetic Long = Real Short)

A reversal is the mirror image — profits when the synthetic long (long call + short put) is **cheaper** than buying the stock:

| Leg | Position | Purpose |
|---|---|---|
| 1. **Short stock** | Short 100 shares | Real short exposure |
| 2. **Buy call** | Long 1 call (same strike, same expiry) | Upside protection |
| 3. **Sell put** | Short 1 put (same strike, same expiry) | Downside obligation |

**Profit formula:**
```
profit = (stock_bid - strike × e^(-rT)) - (call_ask - put_bid) - dividends + short_rebate - borrow_cost
```

## Carry and Financing — Where the Real Economics Live

The headline "parity violation" is only the gross spread. The realized P/L is a **carry trade** dressed as an arbitrage: the position is held to expiry, and over that holding period interest, dividends, and borrow accrue. Decomposing the carry is the entire game, because the carry terms are usually *larger* than the parity violation itself.

| Carry component | Conversion (long stock) | Reversal (short stock) | Notes |
|---|---|---|---|
| **Interest on strike** | you forgo interest by tying up cash in stock | you *earn* interest on short-sale proceeds | scales with [[interest-rate-options\|rate]] × T |
| **Dividends** | you *receive* dividends on long stock | you *pay* dividends on the short | the dominant single-name risk |
| **Borrow cost** | none (you own the stock) | you *pay* the borrow fee | kills reversals on HTB names |
| **Financing of options** | net option debit/credit carries | net option debit/credit carries | small for ATM |

The clean way to see this: a conversion is a **synthetic short position financed by owning the stock**, and a reversal is a **synthetic long financed by shorting the stock**. The options legs lock the price; the cash-and-stock leg generates (or consumes) carry. This is why a reversal on a high-yielding general-collateral name with a steep rate curve can be profitable even when the raw parity spread looks neutral — the interest earned on short proceeds *is* the trade. Conversely, a reversal on a [[dividend-arbitrage|dividend-paying]] or hard-to-borrow name can show a "violation" that vanishes once carry is loaded.

## Relationship to the Box Spread

A [[box-spread]] is the cleanest way to understand what conversions and reversals actually trade. **A box spread = a conversion at strike K1 + a reversal at strike K2** (or equivalently a bull call spread + a bear put spread on the same strikes). Because all stock exposure cancels between the two synthetics, a box has **no directional risk and no stock leg at all** — it is a pure lending/borrowing instrument whose payoff at expiry equals the strike width. Its implied yield *is* the market's synthetic financing rate.

| Instrument | Stock leg? | Directional risk | What it isolates |
|---|---|---|---|
| Conversion | yes (long) | none | parity violation + carry, one strike |
| Reversal | yes (short) | none | parity violation + carry, one strike |
| [[box-spread\|Box spread]] | no | none | the synthetic risk-free rate (lending/borrowing) |

The famous failure mode here is the **short box blow-up**: traders who sold European-style index boxes as a cheap way to borrow (the 2019 "infinity squeeze" / Robinhood box-spread losses) discovered that *American-style* boxes carry early-assignment risk and that a box is not riskless if its components can be exercised against you. This is the same early-exercise risk that makes single-name conversions/reversals not truly riskless — see Risks below.

## Rules

### Entry

1. **Screen for put-call parity violations:** Scan options chains for strikes where the synthetic and real position prices diverge by more than transaction costs. Focus on liquid underlyings with tight bid-ask spreads
2. **Calculate theoretical parity value:** Include risk-free rate, dividends, and borrow cost in the calculation. Use bid-ask prices (not mid) for realistic fill assumptions
3. **Minimum edge required:** The violation must exceed:
   ```
   min_edge = options_spread_cost + stock_spread_cost + commissions + borrow_cost + dividend_risk_buffer
   ```
   Typically 0.05-0.15% of the stock price for liquid names
4. **Execute legs simultaneously** or near-simultaneously. See [[execution-sequencing]] — execute the harder leg (options, especially the illiquid strike) first

### Exit

Hold until expiration. The position converges to its theoretical value at expiry (options expire, stock position closes against assignment/exercise). There is no active exit decision — the profit is locked in at entry.

**Exception:** Exit early if borrow becomes unavailable (recall risk) or if early exercise changes the economics.

### Position Sizing

- ≤ 5% of portfolio per position (single name concentration)
- Account for full margin requirement (long stock + short call requires margin capacity)
- Factor in borrow availability for reversals (short stock leg)

## Risks

### 1. Early Exercise Risk (American Options)

The most significant risk. American-style options (most US equity options) can be exercised early by the counterparty, breaking the arb:

| Scenario | Risk | When It Happens |
|---|---|---|
| **Deep ITM call exercised early** | Your short call is assigned; you deliver shares but lose interest on the strike price for the remaining time | Call holder exercises to capture dividend |
| **Deep ITM put exercised early** | Your short put is assigned; you must buy shares at the strike | Put holder exercises when carry cost exceeds time value |
| **Dividend-related exercise** | Call holders exercise the day before ex-dividend to capture the dividend | When dividend > remaining time value of the call |

**Mitigation:** Avoid options with upcoming dividends where the call time value is less than the dividend amount. Monitor for early exercise signals (very low time value, approaching ex-date).

### 2. Borrow Cost and Availability

For reversals (short stock), borrow cost directly eats into profit:
- **General collateral (GC) stocks:** Borrow rate < 1% annualized. Manageable
- **Hard-to-borrow (HTB) stocks:** Borrow rate 5-50%+ annualized. Can destroy the arb entirely
- **Recall risk:** Lender can demand shares back, forcing you to close the short at a potentially adverse time

**Mitigation:** Only run reversals on GC stocks. Check borrow availability and rate before entry. Lock in term borrow if possible.

### 3. Pin Risk

At expiration, if the stock is **exactly at the strike price**, the options may or may not be exercised/assigned. This creates uncertainty:
- Your short call might be assigned (you deliver shares) or not
- Your long put might be worth exercising or not
- If one side is exercised and the other isn't, you end up with an unhedged position over the weekend

**Mitigation:** Close positions before expiry if the stock is within 1-2% of the strike. The cost of closing early is usually less than the risk of uncertain assignment.

### 4. Dividend Timing Risk

Dividends affect put-call parity. If the dividend amount or timing changes after you enter the trade, the expected parity value shifts:
- **Surprise special dividend:** Can make a conversion less profitable or a reversal more profitable
- **Dividend cut:** Opposite effect

**Mitigation:** Avoid positions spanning earnings announcements or known dividend decision dates. Use confirmed forward dividend estimates, not trailing.

## Indicators Used

- [[put-call-parity]] — the theoretical relationship being exploited
- **Implied volatility skew** — skew can indicate where parity violations are most likely
- **Borrow rate** — critical input for reversal profitability
- **Dividend schedule** — ex-dividend dates and amounts
- **Risk-free rate** — treasury yield for the matching maturity
- **Options bid-ask spread** — wider spreads reduce or eliminate arb profit

## Example Trade

**Setup (hypothetical):**
- Stock XYZ: $100.00
- 60-day ATM options (Strike $100)
- Call bid: $4.50, Call ask: $4.60
- Put bid: $4.20, Put ask: $4.30
- Risk-free rate: 5% (60-day PV factor: 0.9918)
- No dividends expected
- Borrow rate: 0.5% annualized

**Theoretical put-call parity:**
```
C - P = S - K × e^(-rT) = 100 - 100 × 0.9918 = $0.82
```

**Market implies:**
```
C - P = 4.50 - 4.30 = $0.20 (using bid for C, ask for P — worst case for conversion)
```

**Discrepancy:** Theoretical $0.82, market $0.20. The call is cheap relative to the put (or the put is expensive).

**Reversal trade (synthetic long is cheap):**
1. Short 100 shares at $100.00 (receive $10,000)
2. Buy 1 call at $4.60 (pay $460)
3. Sell 1 put at $4.20 (receive $420)
4. Net debit on options: $40
5. Interest earned on short proceeds (60 days): $10,000 × 5% × 60/365 = $82.19
6. Borrow cost (60 days): $10,000 × 0.5% × 60/365 = $8.22
7. **Locked-in profit:** $82.19 - $40.00 - $8.22 - commissions ≈ $28-30

**At expiry:** Regardless of where XYZ closes, the three positions cancel out, and you keep the locked-in profit. If XYZ rises, call gains offset short stock loss. If XYZ falls, short stock gains offset put assignment.

## Performance Characteristics

| Metric | Value |
|---|---|
| Expected return per trade | 0.01-0.10% of notional (very thin margins) |
| Win rate | ~99% (mechanical, near-riskless) |
| Max loss scenario | Early exercise + adverse move before re-hedging |
| Typical holding period | Until expiration (1-90 days) |
| Capital efficiency | Low — requires full margin on stock + options |
| Capacity | Moderate — limited by option OI and borrow availability |
| Crowding | High — market makers run these continuously |

## What Kills This Strategy

1. **Borrow cost spike:** If borrow rate increases after entry, reversal profit erodes or goes negative
2. **Dividend surprise:** Unexpected dividend changes parity value
3. **Early exercise:** American option holder exercises, breaking the hedge
4. **Spread widening:** Options spreads widen, making entry/exit more expensive
5. **Interest rate change:** Risk-free rate moves, shifting theoretical parity (usually minor for short-dated)
6. **Competition / latency:** Faster, lower-cost market makers fill the violation before you can — at retail latency the opportunity is gone by the time it appears on a screen.

## Kill criteria

Numerical conditions for standing down (see [[when-to-retire-a-strategy]]):

- **Net edge after all frictions < expected early-exercise loss** → the trade is not riskless; do not take it. (The single most important gate.)
- **Borrow rate on a reversal name > the interest earned on short proceeds** → carry has gone negative; skip.
- **Realized fill slippage > 50% of the modeled parity violation over a rolling 20 trades** → execution is no longer competitive; the desk is being adversely selected.
- **Any single-name dividend or borrow surprise produces a loss exceeding the cumulative profit of the prior month** → the residual risks dominate the thin edge; retire the name from the universe.
- **Average gross violation captured < commissions + 2× modeled bid-ask** → the cost base is too high for this venue/size.

## Advantages

- **Near-riskless when correctly modeled** — delta-neutral by construction; P/L is locked at entry and does not depend on the underlying's direction.
- **Mechanical and scalable** for an operator with low costs and good borrow access — no forecasting, no discretion.
- **Self-limiting downside** — the worst realistic case (early exercise + adverse re-hedge) is small relative to notional, not catastrophic, *provided* the dividend/borrow gates are respected.
- **Complementary to a market-making book** — the legs hedge inventory and the carry is captured as a by-product of providing liquidity.

## Disadvantages

- **Vanishingly thin margins** (0.01-0.10% of notional) — only economic at very low cost base and meaningful size; uneconomic for almost all retail accounts.
- **Capital- and balance-sheet-intensive** — requires full margin on stock plus options for tiny returns; capital efficiency is poor versus other uses of the same buying power.
- **Borrow-dependent** for reversals — HTB names, recall risk, and rate spikes can turn a locked profit negative after entry.
- **Early-exercise and pin risk** make the "riskless" label aspirational on American-style single-name options.
- **Crowded and latency-sensitive** — dominated by automated market makers; a manual trader is structurally disadvantaged.

## Relationship to Other Options Arbs

| Strategy | Relationship |
|---|---|
| [[box-spread]] | A box spread = conversion + reversal at different strikes. Locks in risk-free rate |
| [[dividend-arbitrage]] | Uses similar put-call parity logic but specifically targets dividend capture |
| [[volatility-arbitrage]] | Different mechanism — trades IV vs RV, not parity violations |

## Related

- [[put-call-parity]] — the pricing identity being arbitraged
- [[box-spread]] — conversion + reversal combined; the synthetic-rate instrument
- [[dividend-arbitrage]] — adjacent put-call-parity play targeting dividends
- [[volatility-arbitrage]] — different mechanism (IV vs RV), not parity
- [[arbitrage-overview]] — the broader arbitrage family
- [[options-overview]] — options market context
- [[delta-neutral]] — the position's directional stance
- [[leg-risk]] — execution risk across the multiple legs
- [[execution-sequencing]] — fill the hard leg first
- [[arbitrage-parameter-cheatsheet]] — quick-reference inputs (rates, borrow, dividends)
- [[interest-rate-options]] — rate sensitivity of the carry
- [[edge-taxonomy]] — structural-edge classification
- [[when-to-retire-a-strategy]] — kill-criteria framework

## Sources

- General market knowledge; no specific wiki source ingested yet.
