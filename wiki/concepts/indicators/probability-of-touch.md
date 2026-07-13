---
title: "Probability of Touch"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, indicators, probability, risk-management, position-sizing]
aliases: ["POT", "Probability of Touching", "Touch Probability", "P(Touch)"]
related: ["[[delta]]", "[[implied-volatility]]", "[[black-scholes-model]]", "[[options-greeks]]", "[[theta-targeting]]", "[[short-strangle]]", "[[iron-condor]]", "[[credit-spread]]", "[[managing-winners]]", "[[managing-losers]]", "[[rolling-options]]", "[[stop-loss-options]]", "[[volatility-skew]]", "[[options-premium-selling]]", "[[reflection-principle]]", "[[itm-probability]]", "[[probability-of-expiring]]"]
domain: [indicators, options, probability]
prerequisites: ["[[delta]]", "[[implied-volatility]]", "[[options-greeks]]"]
difficulty: intermediate
---

**Probability of Touch (POT)** is the probability that the underlying asset trades through a given strike — even momentarily — at any point before the option's expiration. It is a **path-dependent** statistic, distinct from the probability of *expiring* in or out of the money (which depends only on the terminal price). For a [[geometric-brownian-motion|geometric Brownian motion]] underlying, POT is approximately **2 × the probability of expiring beyond** the strike, a result that follows from the [[reflection-principle|reflection principle]] of Brownian motion and is the single most useful rule of thumb in short-premium options management.

## Overview

A short-premium trader who sells a 16-delta SPX put cares about two distinct probabilities:

1. *What is the probability this option finishes ITM?* — about 16%, since [[delta]] is a rough proxy for risk-neutral terminal probability.
2. *What is the probability the underlying will touch the strike at any point before expiry?* — about 32%, roughly twice the first number.

The 16% answer governs the **expected payoff at expiration**. The 32% answer governs the **probability of management interventions**: stop-outs, rolls, panic closes, gamma scalping by the dealer on the other side. For a trader running a managed book that closes at 50% of max profit or rolls when tested, POT is the more relevant probability because management decisions are triggered by *any* test, not only by terminal moneyness.

## Definition / Formula

For a geometric Brownian motion underlying with drift `mu`, volatility `sigma`, current price `S_0`, time-to-expiry `T`, and barrier `K` (with `K > S_0` for an up-touch or `K < S_0` for a down-touch), the probability of touching `K` before time `T` is:

```
POT(K) = N(d_minus) + (K / S_0)^(2 * mu_adj / sigma^2) * N(d_plus)
```

where:
- `d_minus = [ ln(S_0 / K) − mu_adj * T ] / (sigma * sqrt(T))`
- `d_plus = [ ln(K / S_0) + mu_adj * T ] / (sigma * sqrt(T))`
- `mu_adj = r − q − sigma^2 / 2` (the [[risk-neutral-measure|risk-neutral]] log-drift)
- `N(.)` is the cumulative standard normal

In the special case `mu_adj = 0` (zero drift, equivalent to a futures or forward), this collapses to the **reflection-principle result**:

```
POT ≈ 2 * P(S_T crosses K) = 2 * N(d2-style argument)
```

Most broker platforms ([[thinkorswim]], [[tastytrade-platform|tastytrade]], [[interactive-brokers]]) implement POT under the assumption `mu = 0` and report it as a single number on the option chain. The output is correct under [[black-scholes-model|BSM]] assumptions; it is wrong by the same amount BSM is wrong (no skew, no jumps, no stochastic vol — see "Common Misuse" below).

### The 2×POE rule of thumb

For practical purposes, traders use the approximation:

```
POT(K) ≈ 2 * POE(K)
```

where POE = "Probability of Expiring beyond K" ≈ |delta| of an option struck at K.

| Delta | POE (≈ delta) | POT (≈ 2× delta) |
|---|---|---|
| 5 | 5% | ~10% |
| 10 | 10% | ~20% |
| 16 | 16% | ~32% |
| 25 | 25% | ~50% |
| 30 | 30% | ~60% |
| 50 | 50% | ~100% (always touches at-the-money) |

Read the 16-delta row carefully: **the strike most short-premium traders use as their "safe" strike will be tested in roughly 1 in 3 trades**. This is not a malfunction; it is the path-vs-terminal distinction in action.

### Three probabilities, one position

Traders routinely conflate three distinct numbers reported by broker platforms. Keeping them separate is the single biggest conceptual upgrade in short-premium trading:

| Statistic | What it measures | Path or terminal | Rough proxy | Governs |
|---|---|---|---|---|
| [[delta]] | Risk-neutral terminal probability beyond strike (≈ POE) | Terminal | The Greek itself | Expected payoff at expiration |
| **POE / [[probability-of-expiring]]** | Probability the option expires ITM | Terminal | ≈ \|delta\| | Win/loss at expiry |
| **POT (this page)** | Probability the strike is touched at any time before expiry | Path | ≈ 2 × \|delta\| | Frequency of management interventions |
| [[probability-of-profit]] (POP) | Probability the *whole structure* is profitable at expiry (credit-adjusted) | Terminal | ≈ 1 − (POE adjusted for credit) | Expectancy framing of the trade |

The key relationships: **POP > POE** for a credit structure (the credit received pushes the breakeven beyond the strike), while **POT > POE** because touching is easier than finishing beyond. So for a single short option the ordering is typically `POP > 1−POE > ... ` on the favorable side and `POT ≈ 2×POE` on the test side. A 16-delta short put might show POP ≈ 84%, POE ≈ 16%, and POT ≈ 32% — three different lenses on the same strike. See [[probability-of-profit]] for how the credit shifts breakeven away from the raw strike.

## How It Works

### Why POT ≈ 2 × POE — the reflection principle

The intuition is geometric. For a driftless random walk, every path that ends **beyond** the barrier had to **touch** the barrier first. In addition, some paths touch the barrier and then bounce back to finish on the original side. By symmetry (the reflection principle), the number of "touch-and-bounce" paths exactly equals the number of "touch-and-stay-beyond" paths. So:

```
P(touch) = P(touch-and-stay-beyond) + P(touch-and-bounce-back)
        = P(end beyond) + P(end beyond)
        = 2 * P(end beyond)
```

The exact result requires zero drift and a continuous Brownian path — both of which fail in real markets — but the approximation holds well for short-dated equity options where drift is small relative to vol × sqrt(T) and gaps are infrequent.

### Connection to delta

[[delta]] under BSM is `N(d1)` for a call, where `d1` includes a `+sigma^2 / 2` adjustment that POE (`N(d2)`) does not. For at-the-money strikes with short tenors, `d1 ≈ d2` and delta is a clean proxy for POE. As tenors lengthen or implied vol rises, delta and POE diverge — by 1Y at 30 vol, ATM delta is ~58% but ATM POE is ~50%.

For the working trader on 30–60 DTE, the rough chain:

```
delta ≈ POE ≈ 0.5 * POT
```

is good enough for sizing decisions and the basis for the ubiquitous "16-delta strangle" framework: the trader is implicitly choosing 16% terminal-ITM probability and 32% touch probability for each leg.

### How brokers compute POT

Standard broker implementations:

- Use **BSM dynamics** with current implied vol from the surface.
- Set drift to zero or to `r − q` for index/dividend underlyings.
- Treat the strike as an absorbing-or-reflecting barrier and solve the closed-form formula above.
- Update in real time as IV and spot tick.

What they typically **do not** do:

- Account for [[volatility-skew|skew]] (out-of-the-money puts will be touched more often than the BSM-with-flat-vol number suggests).
- Account for jumps or earnings risk (POT is materially understated near binary events).
- Use realized-vol calibration (POT inherits any IV vs RV gap — see [[variance-risk-premium]]).

The first omission is the largest. On equity indices with steep negative skew, a 16-delta put has **higher actual touch probability** than its symmetric 16-delta call — the broker number does not show this.

## Worked Example

A trader sells a 45-DTE [[short-strangle|short strangle]] on SPX with strikes at the 16-delta points: short put at 4750, short call at 5300, with SPX at 5000 and IV at 16%.

**POE (terminal):**
- 16-delta put: ~16% probability SPX < 4750 at expiry
- 16-delta call: ~16% probability SPX > 5300 at expiry
- Probability *either* finishes ITM: ~30% (slightly less than 32% due to mild correlation)

**POT (path):**
- Put touch probability: ~32%
- Call touch probability: ~32%
- Probability *either* strike is touched during life: ~55-60% (less than the naive 64% sum because of correlation — touching one strike makes touching the other less likely conditional on the path)

**What this means in practice:**

1. ~16% of trades will require management on the put side at some point during the trade life. Same for the call side.
2. Combined, **more than half of strangles will get tested** on at least one side within their 45-day life.
3. A book selling 4 strangles per cycle should expect ~2 of them to face a management decision before expiry.
4. The standard cadence of "manage at 21 DTE or when tested" is therefore not a contingency plan — it is the *base case* for a meaningful fraction of the book.

A trader who has internalized POT will not be surprised when half their positions get tested. A trader who only thinks in delta-as-POE will be confused why their "85% probability of profit" trades are losing money 35% of the time on a mark-to-market basis even though most still expire profitable. The answer is gamma scalping by dealers and IV expansion during touches — the path is being monetized against the seller even when the terminal outcome is still favorable.

## Why POT Matters for Management Decisions

Management rules in short-premium playbooks are almost always **path-triggered**, not terminal-triggered:

- **Roll the tested side when short delta exceeds 30** — this trigger has a path-dependent probability ≈ POT, not POE.
- **Close the trade when the underlying touches the strike** — by definition triggered by POT.
- **Stop out at 2× credit received as a loss** — rough proxy for "the underlying has moved through the strike", another POT-trigger.
- **Take profit at 50% of max premium** — also path-triggered, but in the favorable direction.

Sizing the book on POE alone systematically underestimates how often the trader will be forced to act. A trader running 10 simultaneous strangles at 16-delta strikes can expect:

- ~3.2 trades per cycle to terminally lose on at least one side (16% × 2 sides − overlap).
- ~6 trades per cycle to face a management decision on at least one side (32% × 2 − overlap).

Capacity planning for adjustment liquidity, attention, and emotional bandwidth scales with POT, not POE.

POT also informs **strike selection**:

- 16-delta = 32% touch — the standard short-premium strike. Frequent management, but generous credits.
- 10-delta = 20% touch — less management, smaller credits, often poorer T/V ([[theta-targeting]]).
- 30-delta = 60% touch — high-touch strike used for [[short-straddle|short straddles]] and aggressive credit spreads. Requires active management discipline.
- 5-delta = 10% touch — the "set-and-forget" zone. Very rarely touched, but premium is so small that adverse moves wipe out many cycles of credit.

### Strike-selection decision table

| Goal | Target delta | Approx POT | Management cadence | Trade-off |
|---|---|---|---|---|
| Maximum credit, active management | 25–30 | 50–60% | Expect to manage most trades | Highest gamma/path risk |
| Balanced income ("16-delta book") | 16 | ~32% | ~1 in 3 tested | Industry default; generous T/V |
| Lower-touch, conservative | 10 | ~20% | ~1 in 5 tested | Thinner credits, weaker theta/vega |
| Set-and-forget tail seller | 5 | ~10% | Rarely managed | Tiny premium; one breach erases many cycles |

The right column is the discipline cost: a higher-POT strike does not mean a worse trade, but it does mean the trader must have the attention, capital, and emotional bandwidth to act on the tests that *will* arrive. Size the book to the management load implied by POT, not to the win rate implied by POE.

### How POT evolves through the trade

POT is not stationary. Three forces move it after entry:

| Driver | Effect on POT | Mechanism |
|---|---|---|
| Time passing (no move) | Falls | Less remaining path; fewer chances to touch (see [[theta]]) |
| [[implied-volatility|IV]] rising | Rises | Larger expected range over remaining life |
| Spot moving toward strike | Rises sharply | Barrier is closer; gamma accelerates |

A 45-DTE position that opened at 32% POT can sit at 80% POT a week later purely from an IV expansion, even with the underlying unchanged — the position has become materially more dangerous while looking unchanged on a price chart. Re-reading POT (not the entry POT) is what tells you the *current* risk.

## Common Misuse

- **Reading POT as "probability of loss."** A touch is not a loss — many touched positions still expire profitable. POT is a probability of *being tested*, not a probability of negative P&L.
- **Ignoring skew.** The flat-vol POT understates the touch probability of OTM puts on negatively skewed underlyings (equity indices). Realized OTM-put touch probabilities have historically run **20-40% higher** than BSM-implied POT on SPX over multi-decade samples.
- **Using POT around binary events.** Earnings, FOMC, CPI prints — anything with a discontinuous price process — produces POT that is wildly different from the BSM number. The broker shows you a number that doesn't include the announcement.
- **Confusing "touch" with "first hitting time."** Some platforms display *expected first hitting time* as a complement to POT. The two are different statistics; do not interpret one as the other.
- **Stacking POT across legs naively.** Touch probabilities on the two legs of a strangle are not independent; combined probability is **less than the sum**. On a short call + short put strangle, the joint touch probability is well-approximated by `1 − (1 − POT_call) × (1 − POT_put) × correlation_correction`, but the correlation correction is non-trivial.
- **Using static POT at trade entry as if it were stationary.** POT updates as time passes and as IV moves. A position that started at 32% POT can be at 80% POT a week later if vol expanded — the position has gotten *much* more dangerous even if the underlying hasn't moved.

## Related

- [[delta]] — the rough POE proxy that underlies the 2×POE shortcut
- [[probability-of-expiring]] — the terminal-probability sister statistic
- [[probability-of-profit]] — the credit-adjusted expectancy probability for the whole structure
- [[itm-probability]] — synonym used on some platforms
- [[theta]] — time decay that lowers POT as expiry approaches
- [[black-scholes-model]] — the dynamics under which POT has a closed form
- [[volatility-skew]] — what makes broker-reported POT systematically biased on equity indices
- [[implied-volatility]] — a key input; rising IV raises POT mechanically
- [[managing-winners]], [[managing-losers]] — playbooks triggered by touches
- [[rolling-options]] — the standard response when POT-driven management triggers
- [[reflection-principle]] — the mathematical basis for POT ≈ 2 × POE
- [[short-strangle]], [[iron-condor]], [[credit-spread]] — structures whose management cadence is POT-driven
- [[theta-targeting]] — the sizing framework in which POT informs strike selection
- [[options-premium-selling]] — the strategy class for which POT is the operational probability

## Sources

- Hull, J. *Options, Futures, and Other Derivatives*, ch. 26 — barrier options and first-hitting-time mathematics.
- [[book-option-volatility-and-pricing]] — Natenberg on path probabilities in BSM.
- [[tastytrade-research-pop-vs-pot]] — empirical comparison of probability-of-profit and probability-of-touch on liquid index options.
- Shreve, S. *Stochastic Calculus for Finance II*, ch. 7 — formal derivation of the reflection principle and first-passage distributions.
- CBOE / CFE option-chain documentation (POT calculation conventions in commercial platforms).
