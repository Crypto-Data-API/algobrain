---
title: "Synthetic Positions"
type: concept
created: 2026-04-13
updated: 2026-04-13
status: good
tags: [options, derivatives, arbitrage, pricing]
aliases: ["Synthetic Stock", "Synthetic Long", "Synthetic Short", "Conversion", "Reversal"]
domain: [market-microstructure, risk-management]
prerequisites: ["[[options]]", "[[put-call-parity]]", "[[call-options]]", "[[put-options]]"]
difficulty: intermediate
related: ["[[put-call-parity]]", "[[options]]", "[[box-spread]]", "[[risk-reversal]]", "[[delta-neutral]]", "[[volatility-arbitrage]]"]
---

A synthetic position replicates the risk/reward profile of one instrument using a combination of other instruments. In options, synthetic positions arise directly from [[put-call-parity]] — since C - P = S - PV(K), any one component can be constructed from the other three. Understanding synthetics is essential for recognizing equivalent positions, finding cheaper execution, and understanding how market makers enforce pricing relationships.

## Core Synthetic Equivalences

All synthetics use the **same strike price and expiration** for both the call and put.

### Synthetic Stock

| Synthetic | Construction | Equivalent To |
|-----------|-------------|---------------|
| **Synthetic long stock** | Long call + short put | Long 100 shares |
| **Synthetic short stock** | Short call + long put | Short 100 shares |

A synthetic long stock has the same delta (+1.0), the same unlimited upside, and the same unlimited downside as owning shares. The only differences are:
- No voting rights or dividends (though dividends are priced into the options)
- Capital efficiency — the synthetic requires less capital than buying shares outright
- Defined expiration — the position expires, unlike stock ownership

### Synthetic Options

| Synthetic | Construction | Equivalent To |
|-----------|-------------|---------------|
| **Synthetic long call** | Long stock + long put | Long call |
| **Synthetic long put** | Short stock + long call | Long put |
| **Synthetic short call** | Short stock + short put | Short call (covered) |
| **Synthetic short put** | Long stock + short call | Short put (covered call) |

These equivalences reveal important relationships:
- A **[[covered-call]]** (long stock + short call) is synthetically identical to a **short put** at the same strike. They have the same risk profile and P&L.
- A **[[protective-put]]** (long stock + long put) is synthetically identical to a **long call**. Both have unlimited upside and defined downside.

## Conversions and Reversals

Conversions and reversals are the arbitrage trades that **enforce** put-call parity.

### Conversion

```
Long stock + Long put + Short call = Risk-free position
```

A conversion locks in a guaranteed payoff equal to the strike price at expiration. If the combined cost is less than PV(K), the trader earns a risk-free profit. Market makers execute conversions when calls are "too expensive" relative to puts.

### Reversal

```
Short stock + Short put + Long call = Risk-free position
```

The mirror image — a reversal locks in the same guaranteed payoff from the short side. Executed when puts are "too expensive" relative to calls.

### Economics

In practice, conversions and reversals are not pure arbitrage — they involve:
- **Borrow costs**: Shorting stock requires paying the borrow fee
- **Dividend risk**: Unexpected special dividends or dividend cuts change the economics
- **Early exercise risk**: For American options, the short option leg can be assigned early (especially short calls before ex-dividend dates)
- **Margin requirements**: Capital is tied up for the duration

The implied interest rate from a conversion/reversal often differs from the risk-free rate, reflecting these frictions. This difference is called the **carry** or **jelly roll** cost.

## Why Synthetics Matter

### 1. Capital Efficiency

A synthetic long stock using ATM options on a $200 stock might cost $5 net (call premium minus put premium received), controlling $20,000 of notional exposure. This is dramatically more capital-efficient than buying 100 shares, which is why the [[itpm]] methodology uses options as stock replacements.

### 2. Recognizing Equivalent Positions

Understanding synthetics prevents traders from holding redundant or offsetting positions without realizing it:

| If You Hold... | You Actually Have... |
|----------------|---------------------|
| Long stock + short call + long put (same strike) | A risk-free position (conversion) — no market exposure |
| Long call + short put (same strike) | Synthetic long stock — same risk as owning shares |
| Covered call (long stock + short call) | Synthetic short put — short vol, defined upside |
| Married put (long stock + long put) | Synthetic long call — long vol, defined downside |

### 3. Execution and Liquidity

Sometimes the synthetic version of a position is cheaper or more liquid than the direct version:
- Deep ITM options may have wide bid-ask spreads. A synthetic (using ATM options) can achieve the same delta exposure more cheaply.
- In markets where shorting stock is expensive or restricted, a synthetic short (short call + long put) provides equivalent exposure without borrowing shares.
- Options on hard-to-borrow stocks often embed the borrow cost — the put becomes relatively expensive and the call cheap, reflecting the cost of carrying a short position.

### 4. Identifying Mispricings

Professional traders compare the cost of a position against its synthetic equivalent. If long stock costs $100 but synthetic long stock (long call + short put) can be assembled for a net debit equivalent to $99.50, the synthetic is cheaper — either an arbitrage opportunity or a reflection of hidden costs (dividends, borrow, early exercise).

## Advanced Synthetic Structures

### Jelly Roll

A jelly roll combines a synthetic long stock at one expiration with a synthetic short stock at another expiration (same strike). It isolates the interest rate and dividend components between two dates — effectively a forward-starting loan.

```
Long call (Dec) + Short put (Dec) + Short call (Mar) + Long put (Mar) = Jelly Roll
```

### Synthetic Straddle

```
Long 100 shares + Long 2 puts = Synthetic long straddle
```

Or equivalently: delta-hedge a long straddle position. This is the basis of [[gamma-scalping]] — hold a synthetic straddle and continuously rehedge delta to harvest gamma.

### Risk Reversal as Directional Synthetic

A [[risk-reversal]] (short OTM put + long OTM call, or vice versa) is a partial synthetic — it captures directional exposure while giving up the strike-to-strike range. Unlike a full synthetic at a single strike, a risk reversal has a dead zone between the two strikes where neither option has value.

## Common Misconceptions

- **"A covered call is a conservative strategy"** — It is synthetically identical to a naked short put. The risk profile (unlimited downside, capped upside) is the same. The "conservative" label comes from the psychological comfort of owning the stock, not from the actual risk.
- **"Synthetics always cost the same as the real thing"** — In theory yes, but in practice dividends, borrow costs, bid-ask spreads, and early exercise risk create small differences. These differences are trading opportunities for market makers.
- **"You can create a synthetic with different strikes"** — True synthetics require the same strike and expiration. Using different strikes creates spread-like positions (risk reversals, collars) that approximate but don't replicate the underlying.

## Related

- [[put-call-parity]] — the mathematical foundation for all synthetic relationships
- [[covered-call]] — synthetically equivalent to a short put
- [[protective-put]] — synthetically equivalent to a long call
- [[risk-reversal]] — partial synthetic with OTM options
- [[box-spread]] — combines two synthetics to create a risk-free loan
- [[gamma-scalping]] — uses synthetic straddles for volatility trading
- [[delta-neutral]] — synthetics are the building blocks of delta-neutral portfolios
- [[options]] — overview of options concepts

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg's comprehensive treatment of synthetic positions, conversions, reversals, and their role in market making
- [[book-options-futures-other-derivatives]] — Hull's formal derivation of synthetic equivalences from put-call parity
