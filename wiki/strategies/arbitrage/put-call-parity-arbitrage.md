---
title: "Put-Call Parity Arbitrage"
type: strategy
created: 2026-04-24
updated: 2026-06-21
status: excellent
tags: [arbitrage, options, derivatives, quantitative, volatility]
aliases: ["Conversion Arbitrage", "Reversal Arbitrage", "Box Spread", "Jelly Roll"]
strategy_type: quantitative
timeframe: intraday
markets: [options, stocks]
complexity: advanced
backtest_status: untested
edge_source: [structural, analytical]
edge_mechanism: "Market makers and retail flow occasionally misprice the synthetic-versus-cash relationship, especially around dividends, hard-to-borrow stocks, and expiry, allowing a locked box of four instruments to earn a return above the risk-free rate."
data_required: [options-chain, equity-borrow-rates, dividend-calendar, risk-free-curve]
min_capital_usd: 100000
capacity_usd: 50000000
crowding_risk: high
expected_sharpe: 0.5
expected_max_drawdown: 0.03
breakeven_cost_bps: 5
decay_evidence: "Opportunities shrank dramatically after electronic market-making arrived in 2000s. Remaining edge concentrated in hard-to-borrow names and dividend capture windows."
related: ["[[arbitrage]]", "[[volatility-arbitrage]]", "[[options-strategies]]", "[[box-spread]]", "[[edge-taxonomy]]", "[[put-call-parity]]", "[[conversion-reversal-arbitrage]]", "[[limits-to-arbitrage]]"]
---

# Put-Call Parity Arbitrage

Put-call parity is a no-arbitrage identity linking a European call, a European put, the underlying stock, and a risk-free bond: **C - P = S - K*e^(-rT) - D**, where C and P are the call and put prices at strike K, S is the spot price, r is the risk-free rate, T is time to expiry, and D is the present value of dividends paid before expiry. When this identity is violated, a trader can lock in a risk-free profit by buying the cheap side and selling the rich side -- a trade known as a **conversion** (long stock + long put + short call) or a **reversal** (short stock + short put + long call). See [[put-call-parity]] for the underlying identity and [[conversion-reversal-arbitrage]] for the mechanics of the locked-box construction.

In modern, liquid markets the identity holds within pennies, and the remaining mispricings are arbitraged by electronic market makers in microseconds. Persistent violations tend to cluster around **dividend capture windows, hard-to-borrow stocks** (where the shorting leg carries a real cost not reflected in listed option prices), **locate fees on meme stocks**, and pre-listing/post-listing of new expiries. The jelly roll -- a calendar spread of two conversion/reversal pairs at different expiries -- isolates the interest-rate and dividend term structure and is a workhorse of options market-making desks. This page is the canonical reference for the classic options no-arbitrage family: the parity identity itself, the conversion and reversal trades that enforce it, and the box spread / jelly roll structures built on top.

## The Parity Identity and Its Synthetic Equivalences

Put-call parity is not a strategy so much as a *constraint* that the strategy enforces. Rearranging the identity exposes a set of synthetic equivalences -- each instrument can be replicated by a combination of the other three. A desk treats these as interchangeable building blocks; the arbitrage exists only when the market prices the same payoff two different ways.

| Synthetic position | Equivalent replication | Use case |
|---|---|---|
| Synthetic long stock | long call + short put (same K, T) | Get long exposure without borrowing/financing the share |
| Synthetic short stock | short call + long put | Get short exposure when stock is hard to borrow |
| Synthetic long call | long stock + long put | Recreate upside with downside protection |
| Synthetic long put | short stock + long call | Recreate downside hedge synthetically |
| Synthetic bond (financing) | long stock + long put + short call (= conversion) | Lend at the implied box rate |
| Synthetic borrow | short stock + short put + long call (= reversal) | Borrow at the implied box rate |
| Box spread | conversion at K1 + reversal at K2 | Pure synthetic loan/deposit between two strikes |
| Jelly roll | conversion/reversal at T1 vs same at T2 | Isolate the interest-rate + dividend term structure |

The **box spread** deserves special mention: a long box (bull call spread + bear put spread, or equivalently a conversion at one strike plus a reversal at another) has a payoff at expiry of exactly `K2 - K1` regardless of where the stock lands. It is therefore a synthetic zero-coupon bond, and its market price implies a financing rate. Boxes are how professionals lend or borrow cash *through the options market*, sometimes at rates cheaper than their broker's margin loan -- the infamous 2018 retail box-spread blow-ups occurred when traders sold "risk-free" boxes on European-style index options without understanding that they had effectively borrowed at an uncapped rate.

## Edge Source

**Structural** and **analytical**. The structural component comes from the fact that the four instruments -- call, put, stock, bond -- trade in different venues with different frictions (borrow costs, dividend timing, early-exercise risk on American options, settlement). The analytical component is the correct modelling of those frictions: a desk that prices dividends, borrow, and hard-to-borrow specials accurately can identify when a listed option chain is out of line with the correctly-adjusted parity relationship. See [[edge-taxonomy]].

## Why This Edge Exists

Retail option traders, dealer hedging flow, and dividend-motivated buy-writers transact in the listed options chain without simultaneously enforcing the parity relationship. When a stock goes ex-dividend, American-style calls have early-exercise optionality that European parity does not price; when a stock becomes hard to borrow, the synthetic short (short call + long put + short stock) is the only way to get short exposure and the put side gets bid up. The counterparty on a conversion is typically a dividend-capture buyer who accidentally overpaid for the call, or a directional retail bettor who lifted an offer without checking the synthetic. See [[failure-modes]].

The deeper reason violations *persist* at all rather than instantly collapsing is the set of [[limits-to-arbitrage]] that apply specifically to the four-leg box: (i) the short-sale constraint and recall risk on the stock leg, which Ofek, Richardson & Whitelaw (2004) show is the dominant driver of residuals in hard-to-borrow names; (ii) the capital intensity of holding a near-zero-return position to expiry, which crowds out all but the cheapest balance sheets; and (iii) early-exercise and pin uncertainty on American options, which makes the "risk-free" box genuinely path-dependent in the last week. The edge is the residual after all three frictions are correctly priced -- not the raw quoted dislocation.

## Null Hypothesis

Under no-edge conditions, parity holds exactly after adjusting for (i) the forward dividend stream, (ii) the borrow/locate cost of the stock, (iii) early-exercise value for American options, and (iv) financing at the correct funding curve (not just T-bill). If you run a conversion/reversal scanner and find that apparent mispricings are always within the bid-ask spread plus borrow plus early-exercise value, there is no edge -- you are measuring transaction cost, not alpha.

## Rules

### Entry

1. **Scan the full options chain** for each underlying where both calls and puts are listed at the same strike and expiry.
2. **Compute the implied parity residual**: `residual = C - P - (S - K*e^(-rT) - D)`. Include current borrow cost for hard-to-borrow names.
3. **Check both directions**:
   - Residual > threshold + costs -> **Conversion**: long stock, long put, short call.
   - Residual < -threshold - costs -> **Reversal**: short stock, short put, long call.
4. **Threshold** = round-trip exchange + clearing fees + half the bid-ask on each leg + a buffer for early-exercise risk on American options.
5. **Execute all four legs as a single package order** (conversion/reversal spread order type on CBOE, ISE, etc.). Do NOT leg in.
6. **Hold to expiry** in most cases -- the position is self-liquidating when options settle.

### Exit

1. **Passive expiry**: the strike price pins the payoff; stock is called away (conversion) or put back (reversal).
2. **Early unwind**: if the mispricing reverses before expiry, close the box for a smaller-but-faster profit.
3. **Early exercise defense**: if short an American call going into a dividend and parity has tightened, exercise your long put or close early to avoid assignment risk.

### Position Sizing

Size by the lesser of (a) your margin capacity given the borrow and locate cost, (b) option open interest at the strike, and (c) maximum desk concentration limits. Risk-free in theory, but capital-intensive: a $1M conversion might earn $500 over two weeks.

## Implementation Pseudocode

```python
for chain in option_chains_today:
    for (strike, expiry) in chain.common_strikes_puts_and_calls():
        C = chain.call(strike, expiry).mid
        P = chain.put(strike, expiry).mid
        S = chain.spot
        T = year_fraction(today, expiry)
        r = funding_curve.rate(T)
        D = dividends.pv_between(today, expiry, r)
        borrow_cost = borrow_curve.rate(chain.symbol) * T

        # American early exercise premium via binomial tree
        eep_call = american_early_exercise_premium(C, S, K=strike, T, r, D)

        residual = (C - P) - (S - strike * exp(-r*T) - D)
        adj_residual = residual - borrow_cost - eep_call

        cost = fees + 0.5 * sum(bid_ask_spreads)

        if adj_residual > cost:      # conversion: buy stock, buy put, sell call
            place_conversion_spread(chain.symbol, strike, expiry, size)
        elif adj_residual < -cost:   # reversal
            place_reversal_spread(chain.symbol, strike, expiry, size)
```

## Indicators / Data Used

- Real-time options chain with NBBO quotes for calls and puts across all strikes
- Equity **borrow/locate rates** from prime broker -- critical for hard-to-borrow and meme names
- Risk-free curve (OIS/SOFR, not T-bill) at each expiry
- American early-exercise premium from a binomial or trinomial tree
- Pin risk assessment near expiry: if stock closes exactly at strike, the assignment outcome is uncertain

## Example Trade

**July 2021, AMC Entertainment ($AMC) during the meme-stock squeeze** (illustrative quotes reconstructing the documented setup). Borrow rates on AMC spiked to over 20% annualized, but the listed options chain continued to quote calls and puts at the same strike with a parity residual implying only the risk-free rate. A desk that correctly priced the 20% borrow cost could sell the overpriced synthetic (long call + short put) to anyone trying to get short exposure through options, and simultaneously short the stock and collect the rich borrow rebate.

- Strike 40 Sep-21 call: $6.50 bid
- Strike 40 Sep-21 put: $4.20 ask
- Spot AMC: $42.00
- Implied parity residual: C - P = $2.30, but S - K*e^(-rT) = $42 - $39.95 = $2.05. Residual = $0.25 rich on the call side.
- Conversion: buy 100 shares at $42.00, buy 1 put at $4.20, sell 1 call at $6.50. Net debit = $42.00 + $4.20 - $6.50 = $39.70.
- At expiry, if stock > $40, shares are called away at $40 -> receive $40; put expires worthless. Profit = $40 - $39.70 = $0.30 per share, or **$30 per contract**, locked in, two months.
- On 10,000 contracts across many names, this becomes meaningful, and in hard-to-borrow cases the spread was dramatically wider.

## Performance Characteristics

- **Return profile**: typically 10-50 bps above risk-free rate per opportunity, with volatility near zero when the box holds to expiry.
- **Sharpe**: can appear very high (>5) on paper but is capital-intensive -- realized Sharpe after haircuts and concentration limits is more like 0.3-1.0.
- **Drawdowns**: near-zero in normal regimes; risk events include early assignment on short calls around dividends, borrow recalls on hard-to-borrow shorts, and clearinghouse margin changes.
- **Best conditions**: high retail flow into options (meme stocks, earnings season, dividend weeks), elevated borrow, new expiry listings before market makers adjust.
- **Worst conditions**: calm, highly-liquid single-name equity options where electronic market makers enforce parity to the penny.

### Cost-aware residual decomposition (illustrative)

The reason naive scanners overstate the edge is that the *raw* residual must survive a stack of frictions before any of it is profit. The table below is an illustrative decomposition of a quoted residual (not a backtest result) showing how a deceptively large headline number collapses:

| Component | Effect on a quoted 30 bp residual | Notes |
|---|---|---|
| Headline quoted residual | +30 bp | What a naive `C - P - (S - Ke^-rT - D)` scan reports |
| Half bid-ask on 4 legs | -12 to -20 bp | Mid-price quotes are not executable; you cross the spread |
| Exchange + clearing fees (4 legs) | -2 to -5 bp | Per-contract OCC/exchange fees, multiplied by four legs |
| Borrow/locate carry (if hard-to-borrow) | -5 to -200+ bp | Can flip the entire trade negative on specials |
| Early-exercise premium (American calls pre-div) | -1 to -10 bp | Value the binomial tree assigns to optional early exercise |
| Pin-risk / assignment uncertainty buffer | -1 to -5 bp | Insurance against ambiguous expiry outcome |
| **Net realizable edge** | **often <5 bp, sometimes negative** | This is the number that must clear `breakeven_cost_bps` |

The discipline is to size off the **net** column, never the headline. Most quoted "violations" are simply transaction-cost artifacts -- exactly the null hypothesis above.

## Capacity Limits

Capacity is constrained by (i) stock borrow availability for reversals, (ii) option open interest and volume at a given strike, and (iii) margin capital. A desk can typically deploy $10-50M in conversion/reversal positions at any time; beyond that, the act of putting on the trade moves the residual away and kills the opportunity. Hard-to-borrow names have microscopic capacity -- often <$1M per name -- because that is how much stock can actually be shorted.

## What Kills This Strategy

1. **Electronic market makers** (Citadel, Susquehanna, Optiver) who run the same scanner at lower latency and tighter spreads. See [[market-efficiency]] and [[failure-modes]].
2. **Borrow rate spikes** that make a previously-profitable reversal turn into a loss if the borrow is recalled.
3. **Early assignment on short American calls** just before ex-dividend, converting a locked box into an uncovered short against a dividend payment.
4. **Pin risk** at expiry: if the stock closes near the strike, it is ambiguous whether the short call is assigned, leaving overnight directional exposure.
5. **Regulatory/clearinghouse changes** -- e.g. after 2021 meme-stock events, DTCC margin requirements on options positions spiked unpredictably.

## Kill Criteria

- Rolling 30-day average net edge per conversion < fees + 2 bps
- Any unexpected early-assignment loss > 3x expected per-trade profit
- Borrow recall events > 1 per quarter
- Regulatory margin change increasing capital requirement by >25% without corresponding return increase

## Advantages

- Truly market-neutral -- no directional exposure
- Mathematically verifiable edge: the identity either holds or it does not
- Self-liquidating at expiry with no discretionary exit
- Works in any market regime -- does not depend on volatility direction or trend
- Forms the foundation of almost all professional options market-making

## Disadvantages

- Capital-intensive: huge notional to capture small absolute returns
- Highly competitive: dominated by exchange market makers with colocation
- Early-exercise and pin risk are real and hard to model perfectly
- Borrow costs and dividends must be tracked in real time
- Complex operational setup: four-legged orders, prime-broker locate desks, options-clearing margin
- Tail risk of assignment, recall, and regulatory change is asymmetric to the tiny per-trade profit

## Sources

- Hans Stoll (1969), *The Relationship Between Put and Call Option Prices*, Journal of Finance — the original put-call parity paper
- Ofek, Richardson & Whitelaw (2004), *Limited Arbitrage and Short Sales Restrictions: Evidence from the Options Markets*, Journal of Financial Economics — documents persistent parity violations in hard-to-borrow names
- John Hull, *Options, Futures, and Other Derivatives* — parity derivation, American early-exercise treatment
- Sheldon Natenberg, *Option Volatility and Pricing* — conversions, reversals, boxes, jelly rolls from the market-maker's seat
- See [[options-strategies]] and [[arbitrage]] for foundational wiki context.

## Related

- [[arbitrage]] -- parent concept
- [[put-call-parity]] -- the no-arbitrage identity this strategy enforces
- [[conversion-reversal-arbitrage]] -- the locked-box construction in detail
- [[volatility-arbitrage]] -- trades the same chain but on IV, not parity
- [[box-spread]] -- the four-legged construction used to earn synthetic financing
- [[options-strategies]] -- broader options playbook
- [[limits-to-arbitrage]] -- why parity violations persist at all
- [[edge-taxonomy]], [[failure-modes]] -- methodology
