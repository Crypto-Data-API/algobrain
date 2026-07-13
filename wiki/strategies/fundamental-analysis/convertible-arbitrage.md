---
title: "Convertible Arbitrage"
type: strategy
created: 2026-04-06
updated: 2026-06-21
status: excellent
tags: [stocks, bonds, convertible-bonds, arbitrage, hedging, delta-hedging, gamma, credit-risk, hedge-fund, volatility]
aliases: ["Convertible Bond Arbitrage", "CB Arb", "Convert Arb"]
strategy_type: fundamental
timeframe: position|long-term
markets: [stocks, bonds]
complexity: advanced
backtest_status: untested
edge_source: [analytical, structural, risk-bearing]
edge_mechanism: "Issuers and natural holders sell embedded equity volatility too cheaply; the arbitrageur buys it via the convertible, hedges the stock with delta, and harvests the gap between implied and realized vol plus coupon and convergence, bearing credit and liquidity risk in return."
data_required: [convertible-terms, ohlcv-daily, options-implied-vol, credit-spreads, borrow-rates]
min_capital_usd: 1000000
capacity_usd: 5000000000
crowding_risk: medium
related: ["[[yield-curve-trading]]", "[[long-short-equity]]", "[[volatility-arbitrage]]", "[[delta-hedging]]", "[[merger-arbitrage]]", "[[convertible-bonds]]", "[[gamma]]", "[[implied-volatility]]", "[[credit-spread]]"]
---

# Convertible Arbitrage

Convertible arbitrage is a classic hedge-fund relative-value strategy: buy a [[convertible-bonds|convertible bond]] and short the underlying equity to isolate and capture the mispricing of the bond's embedded equity call option. Because a convertible can be exchanged for a fixed number of shares, it behaves like a straight bond plus a long call -- it carries [[gamma]] (convexity), credit exposure, and rate exposure. The arbitrageur buys the cheap embedded option (long [[gamma]], long credit, long carry), neutralizes directional stock risk with [[delta-hedging]], and monetizes the volatility premium, coupon, and convergence to fair value. The strategy was central to funds like Citadel, D.E. Shaw, and Millennium through the 2000s.

## Overview

A convertible's value is driven by stock price, equity [[implied-volatility|volatility]], [[credit-spread|credit spreads]], and interest rates. The arbitrage thesis: convertibles are frequently **underpriced** relative to a fair model value because issuers sell them to raise cheap financing and natural holders (income funds) under-price the embedded optionality -- so the embedded option's [[implied-volatility]] often sits *below* the stock's realized/expected volatility. By going long the bond and short the [[delta-hedging|delta]]-equivalent shares, the position is market-neutral and profits from: (a) **gamma scalping** the dynamic hedge, (b) **coupon** carry, (c) **convergence** of price to model value, and (d) credit-spread tightening -- regardless of whether the stock rises or falls.

## Edge source

Per [[edge-taxonomy]], convert arb combines:

- **Analytical** -- correctly modeling the convertible (delta, [[gamma]], vega, rho, credit-adjusted option value) and the dynamic hedge.
- **Structural** -- a niche, under-covered asset class with motivated issuers and price-insensitive natural holders, creating persistent cheapness of the embedded option.
- **Risk-bearing** -- the arbitrageur is paid to warehouse **credit risk** and **liquidity risk** (the strategy's signature tail), which is the core reason the embedded volatility is sold cheap.

## Why this edge exists

Three counterparties supply the edge. **Issuers** sell convertibles for cheap, low-coupon financing and to monetize their own equity volatility -- they are happy to sell the embedded call below fair value. **Natural holders** (income-oriented convertible and balanced funds) buy for yield and conversion upside but systematically under-value the optionality and rarely delta-hedge, so they leave volatility on the table. **Forced sellers** in stress (2008, March 2020) dump convertibles for liquidity, deepening the discount. The arbitrageur is the marginal sophisticated buyer who hedges out the directional risk and is *paid* (via cheap implied vol + spread) to hold the credit and liquidity risk others are shedding. The "loser keeps losing" because the structural supply (issuance, income-fund demand for yield) recurs every cycle -- though crowding_risk is **medium** because the trade de-rates violently when leveraged arbs all delever at once.

## Null hypothesis

Under no edge, the convertible is fairly priced: embedded [[implied-volatility]] equals expected realized volatility, the credit spread fairly compensates default risk, and after [[delta-hedging]] the position earns only its financing-adjusted carry. In that world, [[gamma]] scalping P&L over the life of the trade exactly offsets the (theta) cost of holding the option, coupon merely covers financing and borrow, and there is no convergence because price already equals model. The edge is real only if **implied < realized vol** persistently and/or the bond trades below model value net of borrow, financing, and [[credit-spread]] risk.

## Rules

- **Screen** the convertible universe for bonds where embedded [[implied-volatility]] < stock's realized/expected vol, or trading below model value (e.g., post-issuance overhang, forced selling).
- **Buy** the convertible (long coupon, long credit, long [[gamma]]).
- **Short** delta-equivalent shares: shares = delta × conversion ratio × bonds held -- neutralizing directional equity exposure.
- **Delta-hedge dynamically:** as the stock moves, delta changes (that is [[gamma]]); rebalance the short -- **add shorts as the stock rises, cover as it falls** -- mechanically selling high and buying low to extract gamma.
- **Hedge ancillary risks:** [[credit-spread]] risk via CDS where available; interest-rate risk via Treasury futures/swaps; manage [[short-selling|borrow]] cost/availability.

## Implementation pseudocode

```python
bond = convertible(issuer="XYZ", face=5_000_000, coupon=0.03, conv_ratio=20)
buy(bond)

def target_short_shares():
    return bond.delta * bond.conv_ratio * bond.units   # delta-equivalent

short(stock(bond.issuer), target_short_shares())

while position_open:
    if abs(current_short - target_short_shares()) > rebal_band:
        rebalance_short(target_short_shares())   # gamma scalp: sell high / buy low
    accrue(coupon)                               # carry
    pay(borrow_cost + financing)                 # costs that eat the edge
    optionally hedge_credit(CDS)                 # cap default tail
    optionally hedge_rates(treasury_futures)
```

## Indicators / data used

[[convertible-bonds|Convertible]] terms (coupon, conversion ratio/price, call/put schedule, maturity), stock price ([[ohlcv-daily]]) and realized vol, [[options-implied-vol|option-implied vol]] for the embedded option, [[credit-spread|credit spreads]]/CDS, [[short-selling|stock borrow]] rates and availability, and interest-rate curve for rho.

## Example trade

A fund finds a 5-year XYZ Corp convertible at **$980 / $1,000 face**, 3% coupon, convertible into 20 shares (conversion price $50). Stock is $45, delta 0.40. The fund buys **$5M face** and shorts **40,000 shares** (= 0.40 × 20 × 5,000 bonds) at $45 (~$1.8M short). Over 6 months: (a) coupon pays **$75,000**; (b) [[delta-hedging|dynamic hedging]] as the stock oscillates $40-$50 [[gamma]]-scalps **$60,000**; (c) the bond converges toward model value, gaining **$40,000**. Gross: **$175,000 on ~$3.2M net capital (≈5.5% / 6mo, ≈11% annualized)** -- profitable whether the stock rose or fell. *(Illustrative round numbers.)* Against this, subtract stock-borrow cost, financing/leverage cost, and rebalancing [[slippage]] -- and note the unmodeled tail: if XYZ's credit gapped wider or it defaulted, the bond could fall far more than the short hedge recovers.

## Performance characteristics

Convert arb's return profile is **steady positive carry punctuated by sharp credit/liquidity tail losses** -- a short-volatility-of-liquidity profile. Gross returns on unlevered capital are modest, so funds typically run **3-6x leverage**, which is exactly what turns 2008-style dislocations into double-digit drawdowns as forced delevering compresses prices for everyone at once. Frame qualitatively: positive in calm, dispersed markets; dangerous in credit crunches.

| Cost / friction | Effect | Notes |
|-----------------|--------|-------|
| **Stock borrow** | Direct drag; can spike or vanish | Hard-to-borrow names raise cost and risk a squeeze/forced buy-in |
| **Financing / leverage** | Amplifies both return and drawdown | 3-6x typical; margin can be pulled in stress |
| **Rebalancing [[slippage]]** | Each delta-hedge crosses the spread | More gamma scalping = more trades = more cost |
| **[[credit-spread]] widening** | Mark-to-market loss on the long bond | The signature tail; partially hedgeable via CDS |
| **Liquidity / [[market-impact]]** | Convertibles are illiquid; exits costly in stress | 2008 / Mar-2020 were devastating |
| **CDS / rate hedges** | Cost of hedging credit and rho | Reduces tail but costs carry |

## Capacity limits

Bounded by the size of the **convertible issuance universe** and stock-borrow availability rather than equity-market depth. Global convertible outstanding is large but finite and varies by cycle; capacity_usd is an order-of-magnitude estimate for the strategy in aggregate. A single fund's capacity is limited by how much of an issue it can hold without dominating the (often thin) secondary market and by borrow on the underlying. Issuance droughts shrink the opportunity set; issuance booms (e.g., low-rate windows) expand it.

## What kills this strategy

See [[failure-modes]]. The realistic killers:

- **Credit event / default** -- the long bond falls more than the short hedge recovers; the dominant tail.
- **Liquidity crunch + forced delevering** -- leveraged arbs sell into a no-bid market simultaneously (2008, March 2020).
- **Borrow squeeze** -- the stock becomes hard/impossible to short, breaking the hedge or forcing a costly buy-in.
- **Implied ≥ realized vol** -- if the embedded option is no longer cheap, the core edge evaporates.
- **Shrinking universe** -- low issuance reduces opportunities; crowding compresses cheapness.

## Kill criteria

See [[when-to-retire-a-strategy]]. Reduce/exit when:

- Issuer credit deteriorates beyond a set CDS/spread threshold and cannot be hedged economically.
- Stock borrow cost exceeds the trade's expected gamma + coupon + convergence return.
- Embedded [[implied-volatility]] rises to or above expected realized vol (no edge).
- Book-level leverage or drawdown breaches risk limits amid widening credit spreads.

## Advantages

- **Market-neutral** -- [[delta-hedging]] removes stock-direction exposure; profit from volatility.
- **Multiple return sources** -- coupon, [[gamma]] scalping, [[credit-spread]] tightening, convergence.
- **Structural mispricing** -- under-covered niche with motivated issuers and natural holders.
- **Downside cushion** -- the straight-bond floor limits downside above the conversion region.

## Disadvantages

- **Credit/default risk** -- the convertible can lose far more than the hedge protects.
- **Liquidity risk** -- illiquid bonds; brutal in market stress.
- **Borrow cost/availability** -- shorting can be costly or impossible.
- **Modeling complexity** -- simultaneous equity, credit, rate, and vol risk.
- **Leverage dependency** -- modest unlevered returns push funds to 3-6x, amplifying tails.
- **Shrinking universe** -- issuance cycles cap the opportunity set.

## Sources

General hedge-fund and convertible-securities knowledge (embedded-option valuation, delta/gamma hedging, the 2008 convert-arb dislocation); no specific wiki source ingested yet. See [[volatility-arbitrage]] and [[delta-hedging]] for the option-mechanics foundation and [[credit-spread]] for the credit leg.

## Related

- [[convertible-bonds]] -- the instrument and its embedded option
- [[delta-hedging]] -- the dynamic equity hedge at the strategy's core
- [[gamma]] -- the convexity that generates hedging profits
- [[implied-volatility]] / [[volatility-arbitrage]] -- the vol-mispricing thesis
- [[credit-spread]] -- the credit risk borne and (sometimes) hedged
- [[short-selling]] -- borrow cost/availability for the equity hedge
- [[long-short-equity]] -- hedged-equity cousin without the fixed-income leg
- [[merger-arbitrage]] -- another event-driven hedge-fund relative-value strategy
- [[yield-curve-trading]] -- fixed-income relative value requiring duration management
- [[edge-taxonomy]] -- analytical + structural + risk-bearing edges
- [[transaction-costs]] / [[slippage]] / [[market-impact]] -- the cost overlay
