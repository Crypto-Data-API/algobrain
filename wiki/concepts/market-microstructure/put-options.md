---
title: Put Options
type: concept
created: 2026-04-06
updated: 2026-05-03
status: good
tags:
  - options
  - derivatives
  - market-microstructure
  - risk-management
aliases:
  - put
  - puts
  - put-option
related:
  - "[[options]]"
  - "[[call-options]]"
  - "[[strike-price]]"
  - "[[options-greeks]]"
  - "[[put-call-parity]]"
  - "[[protective-puts]]"
  - "[[cash-secured-puts]]"
  - "[[bear-put-spread]]"
  - "[[implied-volatility]]"
---

# Put Options

A put option gives the holder the right, but not the obligation, to sell an underlying asset at a specified [[strike-price]] before expiration. See [[options]] for a full overview of options trading and [[call-options]] for the bullish counterpart.

## Payoff Structure

The payoff of a long put at expiration is: **max(strike price - underlying price, 0) - premium paid**. Maximum profit is achieved when the underlying falls to zero (strike price - premium paid). Maximum loss is limited to the premium paid.

For a short (written) put, the payoff is the inverse: maximum profit equals premium received, but the seller can lose up to (strike - 0) per share if the underlying collapses, less premium collected. This asymmetry — limited upside, large downside — is why naked put selling is treated as a margin-intensive activity.

## Anatomy of a Put Contract

A standard equity put contract in the US has the following components:

| Component | Description |
|-----------|-------------|
| **Underlying** | The asset the put references (a stock, ETF, index, future) |
| **Strike price** | Price at which the holder can sell the underlying — see [[strike-price]] |
| **Expiration date** | Date the contract expires (third Friday of month for monthlies; weeklies, dailies also exist) |
| **Premium** | The price paid by the buyer to the seller, quoted per share |
| **Multiplier** | Almost always **100** for US equity options — one contract controls 100 shares |
| **Exercise style** | [[american-options]] (exercise any time before expiry) vs [[european-options]] (only at expiry) |
| **Settlement** | Physical (deliver shares) for stock options; cash-settled for index options like SPX |

US-listed equity and ETF puts are American-style; index puts (SPX, NDX) are European-style and cash-settled. The distinction matters for early-exercise risk on short puts (especially around dividends and deep ITM cases).

## Put Pricing Components

A put's premium is decomposed into two pieces:

- **Intrinsic value** = max(K - S, 0), where K is strike and S is the underlying price. This is what the put is worth if exercised right now.
- **Extrinsic value** (time value) = Premium - Intrinsic value. This captures everything else — time to expiration, [[implied-volatility]], interest rates, dividends.

A $100-strike put when stock = $95 has $5 of intrinsic value. If the put trades at $7, the remaining $2 is extrinsic. As expiration approaches, extrinsic value decays toward zero (theta decay) — the put eventually settles to pure intrinsic value at expiry.

Out-of-the-money (OTM) puts (K < S) have **zero intrinsic value** — their entire premium is time value, which is why they decay aggressively in the final weeks.

## Greeks for Puts

The [[options-greeks]] describe how a put's price changes with respect to various inputs. For a long put:

| Greek | Sign | Meaning |
|-------|------|---------|
| [[delta]] | Negative (0 to -1) | Change in put price per $1 move in underlying. ATM ~ -0.50, deep ITM approaches -1.00, deep OTM approaches 0 |
| [[gamma]] | Positive | Rate of change of delta. Peaks at-the-money, especially near expiration |
| [[theta]] | Negative | Time decay — long puts lose extrinsic value daily, accelerating in last 30 DTE |
| [[vega]] | Positive | Sensitivity to [[implied-volatility]]. A long put gains when IV rises |
| **Rho** | Negative | Sensitivity to interest rates. Higher rates reduce put value |

**Worked example.** Stock = $98, $100-strike put, 30 DTE, IV = 30%, risk-free rate = 5%. Approximate Greeks:

- Premium ≈ $3.20 ($2.00 intrinsic + $1.20 extrinsic)
- Delta ≈ -0.55 (slightly ITM)
- Gamma ≈ 0.04 (each $1 drop in stock adds 0.04 to |delta|)
- Theta ≈ -0.05 (loses ~$5 per contract per day)
- Vega ≈ 0.11 (gains ~$11 per contract per 1-vol-point IV bump)

If the stock drops $2 to $96 the next day with IV unchanged, the put gains roughly $1.10 from delta plus $0.04 from gamma (delta becomes more negative as the stock falls), minus $0.05 from theta — finishing around $4.29.

## Long vs Short Puts

**Long put.** Buyer pays premium, gains the right to sell at K. Profitable when the underlying falls below K - premium. Limited risk (premium), large potential profit. Used for bearish speculation and hedging.

**Short put.** Seller collects premium, accepts obligation to buy at K if assigned. Profitable when underlying stays above K - premium. Risk reward is inverted: limited profit (premium) and large potential loss. Two main flavors:

- **Cash-secured put** ([[cash-secured-puts]]) — seller posts full strike × 100 in cash. Risk is owning the stock at K; widely used by investors who want to be paid to wait for a pullback.
- **Naked put** — seller posts only [[margin]]. Higher capital efficiency, but margin can balloon if IV spikes or the stock collapses. Not suitable for retail except via spreads.

Short puts have a positive delta (they gain as the stock rises), are short gamma (delta becomes more negative as the stock falls — bad), short vega (hurt by rising IV), and positive theta (gain from time decay).

## Put Strategies Catalog

Puts are building blocks for a wide range of structures:

| Strategy | Construction | View |
|----------|--------------|------|
| **Long put** | Buy 1 put | Bearish, defined risk |
| **Married put / [[protective-puts]]** | Long stock + long put | Hedged long, floor on losses |
| **[[cash-secured-puts]]** | Short put + cash | Mildly bullish, income |
| **[[bear-put-spread]]** | Long higher-strike put + short lower-strike put | Bearish, defined risk and reward |
| **[[put-spread]] (credit)** | Short higher-strike put + long lower-strike put | Bullish, premium collection |
| **[[short-strangle]]** | Short OTM put + short OTM call | Range-bound, short volatility |
| **[[iron-condors]]** | Bull put spread + bear call spread | Range-bound, defined risk |
| **Collar** | Long stock + long put + short call | Hedged long with capped upside |

Each maps to a different [[probability-of-profit]] profile and a different exposure to delta, vega, and theta.

## Put-Call Parity

Puts and calls are not independent instruments — they are bound by [[put-call-parity]], a no-arbitrage identity for European options on a non-dividend-paying stock:

```
C - P = S - K * e^(-rT)
```

Where C is the call price, P is the put price, S is spot, K is strike, r is the risk-free rate, T is time to expiration. This means every put can be replicated synthetically by a long call, short stock, and a bond — and conversely a long put + long stock = long call + cash. Market makers enforce parity through arbitrage, which is why ATM put and call IVs trade close together (deviations show up in [[volatility-skew]]).

## When Puts Lose Value Fast

Long puts can decay rapidly even when the directional thesis is right. Common traps:

- **IV crush.** When [[implied-volatility]] drops (post-earnings, post-event), vega losses can wipe out delta gains. Buying puts before earnings frequently loses money even if the stock falls — see [[earnings-volatility-trading]].
- **Theta acceleration.** Time decay is non-linear — extrinsic value decays roughly with the square root of time. The last 30 days lose half the remaining time value, the last 7 days the bulk of that.
- **Rallies through strike.** OTM puts with a 0.20 delta lose value 20¢ on every $1 the stock rises, plus theta. A 5% rally over a week often takes a 30 DTE OTM put to near zero.
- **Skew compression.** Crash-protection bids push OTM put IV above ATM (positive [[volatility-skew]]). When fear fades, that skew flattens, costing OTM put holders even with stable spot.

## Common Retail Mistakes

- **Lottery-ticket OTM puts.** Buying very far OTM puts hoping for a crash. Win rates are very low; the few wins rarely cover the losses (see [[probability-of-profit]]).
- **Holding through earnings.** IV is bid up before earnings and crashes after. Long premium positions usually lose unless the move dwarfs the implied move.
- **Ignoring assignment risk on short puts.** American-style puts can be exercised early, especially deep ITM near ex-dividend dates. See [[assignment]].
- **Over-sizing cash-secured puts.** Selling 10 contracts on a $50 stock requires $50,000 in collateral and a willingness to own $50K of the stock. A 30% drop is a real-money loss, not a paper one.
- **Rolling losers indefinitely.** Rolling a short put down-and-out to avoid assignment can mask a thesis that has broken. Eventually the position size and duration explode.

## Real-World Use Cases

- **Portfolio hedging.** A long-only US equity book can be hedged with SPY or SPX puts. A common rule of thumb: 2-5% of portfolio value spent on 3-6 month, 10-15% OTM puts. See [[protective-puts]].
- **Income generation.** Selling [[cash-secured-puts]] on quality stocks at strikes you'd be happy to own. Premium collected becomes the discount to your effective entry price.
- **Pre-earnings hedges.** Long stock holders buying short-dated puts to protect against earnings miss. Cost of insurance is high (elevated IV) but bounded.
- **Tail risk overlays.** Funds like Universa pursue convex tail-hedge strategies built around far-OTM index puts, designed to lose small amounts continuously and pay off massively in crashes.
- **Volatility expression.** Long puts express both a bearish view AND a long-vol view. To isolate volatility from direction, traders use straddles or delta-hedged puts.

## Advantages

- **Asymmetric payoff** — limited downside (premium), large upside on a crash
- **Capital efficient** — controls 100 shares of exposure for a fraction of stock cost
- **Flexible expression** — direction, volatility, time, or skew can be isolated by strike/expiry choice
- **Defined-risk hedging** — protective puts cap portfolio drawdowns without forcing share sales
- **Income generation** — short puts (cash-secured or in spreads) monetize time decay and elevated IV

## Disadvantages

- **Time decay** is a constant headwind for long premium — even a correct directional call can lose money
- **Wide bid-ask spreads** in less liquid names dramatically increase transaction cost
- **Pin risk** near expiration can produce surprise assignments on shorts when stock closes very near strike
- **Tax treatment** is generally short-term capital gains in the US, regardless of holding period
- **IV mean reversion** — buying puts after a sharp selloff often means paying peak IV, with vega losses if volatility normalizes
- **Liquidity cliffs** — far-dated and far-OTM contracts can trap holders unable to exit at fair value

## Worked Hedging Example

A $1M long-only US equity portfolio, 0.95 correlated to SPY at $500. To hedge ~10% downside over 3 months:

- **SPY notional to hedge** = $1M × 0.95 = $950K → 19 SPY contracts (each = 100 × $500 = $50K)
- Buy 19 SPY $475 puts (5% OTM) with 90 DTE. IV ~18%, premium ~$8.50 → total cost ≈ $16,150 (1.6% of book)
- If SPY falls 15% to $425, puts pay (475 - 425) × 100 × 19 = $95,000 — roughly half the equity-portfolio drawdown
- If SPY rallies, max loss is the $16K premium — a known, budgetable cost of insurance

This is the canonical [[protective-puts]] structure scaled to a real book; refinements include rolling, monetizing skew via put spreads, or adding a short call to fund the hedge (collar).

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]]) — gap analysis covering put-option mechanics, Greeks, retail mistakes, and portfolio uses

## Related

- [[options]]
- [[call-options]]
- [[strike-price]]
- [[options-greeks]]
- [[delta]]
- [[gamma]]
- [[theta]]
- [[vega]]
- [[implied-volatility]]
- [[put-call-parity]]
- [[protective-puts]]
- [[cash-secured-puts]]
- [[bear-put-spread]]
- [[put-spread]]
- [[short-strangle]]
- [[iron-condors]]
- [[volatility-skew]]
- [[assignment]]
- [[american-options]]
- [[european-options]]
- [[probability-of-profit]]
- [[earnings-volatility-trading]]
- [[married-put]]
- [[calls-vs-puts]]
