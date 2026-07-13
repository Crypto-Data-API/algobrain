---
title: "Put-Call Parity"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: good
tags: [options, derivatives, arbitrage, pricing]
aliases: ["Put Call Parity", "PCP", "put-call-parity"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[options]]", "[[call-options]]", "[[put-options]]"]
difficulty: intermediate
related: ["[[options]]", "[[black-scholes]]", "[[synthetic-positions]]", "[[volatility-arbitrage]]", "[[american-vs-european-options]]"]
---

Put-call parity is the fundamental no-arbitrage relationship linking the prices of European [[call-options|calls]], [[put-options|puts]], the [[strike-price|strike price]], and the underlying asset. It is the single most important equation in options theory — every pricing model must satisfy it, and violations create risk-free arbitrage opportunities that market makers exploit instantly.

## The Equation

For European options on a non-dividend-paying stock:

```
C - P = S - K × e^(-rT)
```

Where:
- **C** = call price
- **P** = put price  
- **S** = current stock price
- **K** = strike price (same for both options)
- **r** = risk-free interest rate
- **T** = time to expiration (in years)
- **e^(-rT)** = discount factor (present value of strike)

In plain English: **a long call minus a long put at the same strike equals a forward position on the stock**. The difference between call and put prices must equal the difference between the stock price and the present value of the strike.

## Intuition

Consider two portfolios:

| Portfolio | Components | Payoff at Expiration |
|-----------|-----------|---------------------|
| **A** | Long call + cash equal to PV(K) | max(S_T - K, 0) + K = max(S_T, K) |
| **B** | Long put + long stock | max(K - S_T, 0) + S_T = max(S_T, K) |

Both portfolios produce identical payoffs in every scenario. By the law of one price, they must cost the same today. Rearranging gives the parity equation.

## Why It Matters

### 1. Arbitrage Enforcement

If put-call parity is violated, traders can lock in risk-free profit:

- **Call "too expensive"** (C - P > S - PV(K)): Sell the call, buy the put, buy the stock, borrow PV(K). Guaranteed profit at expiration.
- **Put "too expensive"** (C - P < S - PV(K)): Buy the call, sell the put, short the stock, lend PV(K). Guaranteed profit at expiration.

These are called **conversion** and **reversal** arbitrage, respectively. Market makers monitor parity continuously, and deviations are typically small (a few cents) and short-lived.

### 2. Synthetic Positions

Put-call parity implies that any option position can be replicated using the other option plus the underlying stock. See [[synthetic-positions]] for the full taxonomy:

| Synthetic Position | Construction |
|-------------------|-------------|
| Synthetic long stock | Long call + short put (same strike) |
| Synthetic short stock | Short call + long put (same strike) |
| Synthetic long call | Long stock + long put |
| Synthetic long put | Short stock + long call |

### 3. Pricing Consistency

The [[black-scholes]] model and all valid pricing models must satisfy put-call parity. If a model prices calls correctly but violates parity for puts, the model is broken. Traders use parity as a sanity check on any pricing output.

### 4. Implied Forward Price

Rearranging parity gives the market's implied forward price:

```
F = S × e^(rT) = K + (C - P) × e^(rT)
```

This is how market makers extract the forward price from option prices — useful for detecting dividend expectations, borrow costs, and supply/demand imbalances.

## Dividends and American Options

### Discrete Dividends

For stocks paying a known dividend D before expiration:

```
C - P = S - PV(D) - K × e^(-rT)
```

The stock price is reduced by the present value of expected dividends. This adjustment is critical for accurately pricing options around ex-dividend dates.

### American Options

Put-call parity holds as an **inequality** for American options:

```
S - K ≤ C - P ≤ S - K × e^(-rT)
```

The inequality arises because American puts may be optimally exercised early (converting time value to intrinsic value), particularly deep ITM puts or puts on dividend-paying stocks near ex-dividend dates. American calls on non-dividend-paying stocks are never optimally exercised early, so their pricing is equivalent to European calls.

## Practical Applications

### Detecting Mispricings

Professional traders scan for parity violations across thousands of option chains. Even small deviations (after accounting for bid-ask spreads, borrow costs, and transaction fees) can be profitable at scale. The tightness of put-call parity is a measure of market efficiency — wider deviations occur in less liquid options.

### Understanding Skew Through Parity

Since put-call parity links calls and puts mechanically, the [[implied-volatility]] skew for puts must be consistent with the skew for calls at the same strike. If OTM put IV rises (higher demand for downside protection), the corresponding OTM call IV at the same strike adjusts to maintain parity. This is why traders often quote skew in terms of risk-reversals (the IV difference between OTM calls and OTM puts).

### Box Spreads as Parity Trades

A [[box-spread]] (bull call spread + bear put spread at the same strikes) is a direct application of put-call parity. The box payoff is always equal to the width of the strikes at expiration, so its fair value is the present value of that width. Box spreads are used to:
- Borrow or lend money at implied interest rates
- Detect parity violations
- Execute risk-free financing

## Common Misconceptions

- **"Calls and puts with the same strike should cost the same"** — Wrong. Parity says C - P = S - PV(K), not C = P. They are equal only when S = PV(K), which rarely occurs.
- **"Parity doesn't work in practice"** — It works extremely well. Apparent violations are almost always explained by dividends, borrow costs, bid-ask spreads, or American exercise features.
- **"Parity only applies to Black-Scholes"** — Put-call parity is model-independent. It holds regardless of the assumed volatility process, jump dynamics, or distribution of returns.

## Related

- [[synthetic-positions]] — constructing equivalent positions using parity
- [[black-scholes]] — the pricing model that must satisfy parity
- [[box-spread]] — direct arbitrage application of parity
- [[options]] — overview of options concepts
- [[american-vs-european-options]] — how exercise style affects parity
- [[volatility-arbitrage]] — exploiting IV vs RV, built on parity relationships
- [[conversion-reversal-arbitrage]] — the specific trades that enforce parity

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg's treatment of put-call parity, synthetic positions, and conversion/reversal arbitrage
- [[book-options-futures-other-derivatives]] — Hull's formal derivation with dividend and American option extensions
