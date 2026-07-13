---
title: "Implied Earnings Move"
type: concept
created: 2026-05-06
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, indicators, earnings]
aliases: ["Implied Earnings Move", "Expected Move", "Implied Move", "Straddle-Implied Move"]
domain: [options, indicators]
difficulty: intermediate
related: ["[[iv-crush]]", "[[implied-volatility]]", "[[iv-rank-and-iv-percentile]]", "[[volatility-surface]]", "[[volatility-skew]]", "[[options-greeks]]", "[[earnings-volatility-trading]]", "[[earnings-plays]]", "[[earnings-calendar]]", "[[variance-risk-premium]]", "[[market-chameleon]]", "[[spotgamma]]", "[[optionstrat]]"]
---

The implied earnings move is a forward-looking estimate of the percentage move the options market is pricing into a stock between the close before its earnings announcement and the open (or close) after. It is derived from the prices of [[options-pricing|options]] -- most commonly the at-the-money straddle on the first expiration following earnings -- and represents the market's consensus expected absolute return at the event. The implied move is the natural benchmark against which to evaluate an earnings options trade: if you expect the stock to move more than the implied, long premium is favored; if less, short premium is favored.

## Overview

When a company announces earnings, options markets typically price in elevated implied volatility for the expirations that span the event. The cheapest way to extract the market's "event premium" is to look at the at-the-money (ATM) straddle on the nearest post-earnings expiration. Because that straddle pays the absolute move from the strike, its price approximately equals the market-expected absolute move plus a baseline cost from non-event volatility and time value.

A more careful term-structure decomposition isolates the event-only contribution by comparing the IV of the front (event-spanning) expiration with that of a later (non-event) expiration. Vendors such as [[market-chameleon|Market Chameleon]], [[spotgamma|SpotGamma]], and [[optionstrat|OptionStrat]] publish implied earnings moves daily for thousands of names, including history of past implied vs. realized.

The implied earnings move is closely tied to [[iv-crush|IV crush]]: the same event premium that creates the implied move is precisely what evaporates when uncertainty resolves at the announcement. Across large samples, implied earnings moves systematically *overstate* the average realized absolute move because of the [[variance-risk-premium|volatility risk premium]] -- options sellers are paid for bearing event risk.

### Quick reference

| Property | Value |
|---|---|
| What it measures | the market's priced expected **absolute** move over the event window |
| Primary source | ATM straddle on the first post-earnings expiration |
| Quick formula | `(ATM call + ATM put) / spot` |
| Convention caveat | straddle ≈ *expected absolute* move ≈ 0.8× the 1σ move (×≈1.25 to convert) |
| Cleaner measure | term-structure decomposition (front vs back IV) isolates the event-only jump |
| Direction of bias | implied **>** realized on average (the [[variance-risk-premium]]) |
| Key companion concept | [[iv-crush]] — the collapse of this premium at the announcement |
| It is NOT | a forecast — it is a *price*, set by supply/demand for event optionality |

## How it works / Calculation

### Quick straddle approximation

The simplest formula uses the ATM straddle price on the first expiration after earnings:

```
implied_move ≈ (ATM call price + ATM put price) / stock_price
```

This works because the straddle is delta-neutral and approximately pays the absolute move from the strike. The expression gives a percent move; multiply by the stock price to get a dollar move.

For example, if AAPL is at $190.00 and the nearest post-earnings ATM straddle (a $190 call + $190 put) trades for $9.50:

```
implied_move ≈ 9.50 / 190.00 = 5.0%
```

So the market is pricing a roughly +/- 5.0% move at earnings.

### Accounting for one standard deviation vs. expected absolute move

The straddle approximation actually corresponds to roughly the **expected absolute move** under a lognormal model (which is `sigma * sqrt(2/pi)` of the standard deviation). Some publishers report instead the **one-standard-deviation move** implied by IV. The two differ by a factor of about `sqrt(pi/2) ≈ 1.25`. Always check the convention a vendor uses.

### Term-structure decomposition (more precise)

Let:

- `IV_front` = IV of the first expiration *spanning* the earnings event (`T_front` days)
- `IV_back` = IV of the next expiration that does not contain a fresh event (`T_back` days)

If we model total variance as the sum of baseline variance over the period plus an event jump variance `J^2`:

```
IV_front^2 * T_front = baseline_var * T_front + J^2
IV_back^2  * T_back  = baseline_var * T_back
```

Solving:

```
baseline_var = IV_back^2
J^2 = T_front * (IV_front^2 - IV_back^2)
implied_event_move ≈ sqrt(J^2 / 252)   # one-day-equivalent event std dev
```

This event-only implied move is the "clean" earnings number, with non-event vol stripped out. It is what serious volatility traders compare across earnings cycles.

### Pseudocode

```python
import math

def implied_event_move(iv_front, t_front_days, iv_back, t_back_days):
    """
    iv_front, iv_back: annualized IVs (decimal)
    t_*_days: calendar days to expiration
    Returns the event-only implied 1-day std dev (decimal).
    """
    var_front = iv_front**2 * (t_front_days / 365)
    var_back  = iv_back**2  * (t_back_days  / 365)
    # baseline variance per day, calibrated on the back month
    baseline_per_day = var_back / t_back_days
    baseline_in_front = baseline_per_day * t_front_days
    event_var = max(var_front - baseline_in_front, 0.0)
    return math.sqrt(event_var)

def straddle_implied_move(call_mid, put_mid, spot):
    return (call_mid + put_mid) / spot
```

## Practical use / Trading applications

### Comparing implied vs. historical realized moves

The single most common use case: pull a stock's last 8-12 earnings-day realized absolute moves from a vendor like [[market-chameleon|Market Chameleon]] or [[optionstrat|OptionStrat]], compute the average, and compare to today's implied move.

| Setup | Read |
|---|---|
| Implied move >> historical average | Market is over-pricing the event -- favor short premium ([[iron-condor|iron condors]], short [[strangle|strangles]]) |
| Implied move ≈ historical average | Fair priced -- no edge from this lens alone |
| Implied move << historical average | Market is under-pricing the event -- favor long premium (long [[straddle|straddles]], long calls/puts) |

This is the core of the [[earnings-volatility-trading|earnings volatility trading]] strategy and one of the most studied relationships in options retail education.

#### Structure selection from the implied-vs-realized read

The read above maps onto concrete structures. The right choice also depends on whether you have a directional view and how much tail risk you can bear:

| View | Best vol bias | Defined-risk structure | Undefined-risk structure | Notes |
|---|---|---|---|---|
| Implied >> realized, neutral | short vol | [[iron-condor]] / [[iron-fly]] | short [[strangle]] / [[straddle]] | the [[variance-risk-premium]] tailwind plus [[iv-crush]] both work for you |
| Implied >> realized, want IV exposure pre-event | long vol, but theta-friendly | [[calendar-spread]] (event between expiries) | — | rare way to be long the event while harvesting term-structure differential |
| Implied << realized, neutral | long vol | long [[straddle]] / [[strangle]] | — | must clear both the implied move AND the post-event [[iv-crush]] |
| Implied ≈ realized | no vol edge | trade direction only, or stand aside | — | no edge from this lens; needs a separate catalyst |
| Bullish + implied rich | short vol w/ tilt | [[short-put-spread]] | [[cash-secured-puts]] | directional credit; tail capped by the long wing |

The single dominant fact: because of the [[variance-risk-premium]], the *base-rate* edge points to **short premium**, but the [[#Tail events break the average|tail]] is what makes naive short-vol-into-earnings dangerous. Defined-risk structures ([[iron-condor]], [[iron-fly]], [[short-put-spread]]) exist precisely to bound that tail.

### Strike selection for credit-spread earnings plays

When constructing an [[iron-butterfly|iron butterfly]] or [[iron-condor|iron condor]] over earnings, the implied move directly informs strike placement:

- Place short strikes *outside* the implied move if you want a higher probability of profit (lower credit).
- Place short strikes *at* the implied move boundaries to maximize credit but accept ~30-40% historical loss rate from the long tail of event distributions.

### Position sizing for long-vol bets

Buying premium into earnings is statistically negative-expectancy on average due to the [[variance-risk-premium|variance risk premium]] and [[iv-crush|IV crush]]. The implied move sets the bar: a pre-earnings long straddle only profits if the stock moves more than the implied move *after* IV crush. Many traders insist on multiple confirming signals (low [[iv-rank-and-iv-percentile|IV rank]], wide skew, fundamental catalysts) before paying that premium.

### As an input to expected-value calculations

```
EV_long_straddle = P(|move| > implied) * E[payoff | beat implied] - straddle_cost
```

Vendors like [[optionstrat|OptionStrat]] surface this directly via their "earnings calculator" features.

## Limitations / What can go wrong

### Volatility risk premium drags long-vol returns

On average across the universe of US single-name earnings, **realized moves are smaller than implied moves**. Studies (Goldman Sachs derivatives research, Susquehanna SIG notes, academic options literature) typically find the implied/realized ratio above 1.0 -- meaning naive long-straddle-into-earnings strategies lose money. The implied move is not a forecast; it is a price.

### Tail events break the average

The aggregate edge to short-premium hides large left-tail losses. A handful of earnings prints (NFLX 2022, META 2022, NVDA various) produced moves well in excess of the implied, wiping out years of accumulated short-premium credits in a single trade. The implied move tells you the market's expectation; it does not constrain what the stock can actually do.

### Skew and binary outcomes

For names with binary catalysts (small biotech around FDA decisions; small-caps with going-concern risk), the lognormal assumption underlying the straddle approximation breaks down. The realized distribution is bimodal, and the "implied move" loses its standard interpretation. Use the term-structure or risk-reversal decomposition with care.

### Stale or bad quotes around earnings

After-hours liquidity is poor. Mid-prices computed from wide bid-ask spreads in low-volume names give noisy implied-move estimates. Always confirm with at least two strikes around ATM and check that the chain is liquid.

### Implied move is for a *specific window*

The straddle-implied move is the move expected by the **expiration of that straddle**, not strictly by the earnings event. If the front expiration is a week or more after earnings, you are buying not just the event but also the post-event drift. The term-structure decomposition above corrects for this.

### Changes in expected timing

If a company shifts its earnings date, the IV curve repositions overnight. Holding an implied-move-based trade through a date change can produce sharp, unexpected MTM swings.

### Pitfalls at a glance

| Pitfall | Symptom | Mitigation |
|---|---|---|
| [[variance-risk-premium]] drag | naive long-straddle loses on average | bias toward short premium; size for the tail |
| Tail events (NFLX/META/NVDA-style) | one print erases many credits | use defined-risk ([[iron-condor]], [[short-put-spread]]); cap per-name size |
| Binary / bimodal names | straddle approximation breaks | risk-reversal / term-structure decomposition; treat as event, not vol |
| Stale after-hours quotes | noisy implied-move read | confirm 2+ strikes; require liquid chain |
| Window mismatch | straddle expires well after the event | term-structure decomposition strips post-event drift |
| Date changes | overnight IV-curve reposition | avoid carrying event trades across unconfirmed dates |

## Examples

### NVDA Q4 FY24 earnings (February 21, 2024)

Going into the report, [[market-chameleon|Market Chameleon]] published an implied move around 11% based on the post-earnings weekly straddle. NVDA's 8-quarter average historical earnings move was roughly 8%. The setup looked rich (implied > historical), favoring short premium. The actual move on February 22, 2024 was approximately +16% -- a significant outlier. Short-iron-condor positions priced inside the implied move took maximum loss; long-straddle positions priced for the implied move profited substantially.

This is a textbook example of why the average is not the trade -- variance-risk-premium edge is paid for, in tail blowouts.

### Worked example -- AAPL straddle implied move

Suppose AAPL is at $190.00 the day before earnings. The next-Friday $190 straddle (which expires after earnings) is quoted:

- $190 call: bid $4.55 / ask $4.65, mid $4.60
- $190 put: bid $4.80 / ask $4.90, mid $4.85
- Straddle mid: $9.45

```
implied_move = 9.45 / 190.00 = 4.97%
implied_dollar_move = +/- $9.45
```

If AAPL's last 8 earnings moves averaged 3.4% absolute, the market is implying a richer move than history -- a short-premium tilt. A trader might sell the $200/$180 strangle to express this view, or sell the $182/$199 iron condor, with strikes set near the historical-average move boundaries.

### Term-structure event move

Suppose for a stock the front weekly (7 calendar days) IV is 95% and the back monthly (35 calendar days) IV is 45%.

```
var_front = 0.95^2 * (7/365)  = 0.01731
var_back  = 0.45^2 * (35/365) = 0.01940
baseline_per_day = 0.01940 / 35 = 0.000554
baseline_in_front = 0.000554 * 7 = 0.00388
event_var = 0.01731 - 0.00388 = 0.01343
event_std = sqrt(0.01343) = 0.116 = 11.6%
```

The event-only implied 1-day move is roughly 11.6%, materially larger than the naive front-weekly 1-day vol read of ~5% -- the term-structure decomposition exposes the embedded earnings premium.

## Related

- [[iv-crush]] -- the IV collapse that follows earnings; the other side of the implied-move coin
- [[implied-volatility]]
- [[iv-rank-and-iv-percentile]]
- [[volatility-surface]]
- [[volatility-skew]]
- [[volatility-smile]]
- [[options-greeks]]
- [[earnings-volatility-trading]] -- the strategy page
- [[earnings-plays]]
- [[earnings-calendar]]
- [[variance-risk-premium]]
- [[market-chameleon]]
- [[spotgamma]]
- [[optionstrat]]
- [[straddle]] / [[strangle]] / [[iron-condor]] / [[iron-butterfly]]
- [[iron-fly]] -- the ATM defined-risk structure most directly priced off the implied move
- [[short-put-spread]] -- the directional defined-risk short-premium earnings play
- [[calendar-spread]] -- the term-structure (event-between-expiries) earnings structure
- [[options-premium-selling]] -- the parent short-vol strategy that harvests the event premium
- [[theta]] / [[vega]] / [[gamma]] -- the Greeks that move hardest across an earnings event

## Sources

- CBOE Options Institute educational materials on event-implied volatility
- Market Chameleon -- daily implied vs. historical earnings move data
- OptionStrat earnings move calculator documentation
- Goldman Sachs Derivatives Research, recurring "Earnings Season Volatility" notes
- Euan Sinclair, *Volatility Trading* (Wiley) -- chapter on event vol decomposition
- SpotGamma daily institutional notes on event-implied moves
