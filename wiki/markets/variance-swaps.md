---
title: "Variance Swaps"
type: market
created: 2026-05-07
updated: 2026-06-19
status: excellent
tags: [options, derivatives, volatility, futures]
aliases: ["Variance Swap", "Var Swap", "Realized Variance Swap"]
related: ["[[long-vol-vs-short-vol]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[realized-volatility]]", "[[vix]]", "[[vix-futures]]", "[[volatility-swap]]", "[[log-contract]]", "[[carr-madan-replication]]", "[[gamma]]", "[[vega]]", "[[volmageddon]]", "[[vix-august-2024-spike]]"]
---

A **variance swap** is an over-the-counter (OTC) forward contract on the realized variance of an underlying asset. The buyer pays a fixed strike (the "variance strike", quoted as a vol number squared) and receives the realized variance over the contract life, multiplied by a notional vega. Variance swaps are the cleanest pure-vol instrument available -- they have no path-dependence, no [[delta-hedge|delta hedging]] required, and unlike a [[straddle]] or [[strangle]] their payoff is independent of where spot finishes.

## Overview

Variance swaps emerged in the mid-1990s as the institutional answer to the question: "how do I take a directional bet on volatility itself, without the path-dependent slippage of a [[delta-hedged-options|delta-hedged option]]?" A vanilla option's vol exposure changes constantly as spot moves and time passes. By contrast, a variance swap pays out exactly the difference between *realized* annualized variance and the *strike* variance set at trade inception, multiplied by the variance notional. That makes them the cleanest expression of a [[vega]] view, and the canonical instrument for trading the [[variance-risk-premium]].

Variance swaps grew rapidly through 2000-2007, became core hedging tools for dispersion, correlation, and tail-risk desks, then suffered a structural setback after the [[gfc|2008 GFC]] when several large dealer short-variance books incurred outsized losses. The market today is smaller and more conservatively traded, with most flow concentrated in single-name dispersion books, [[forward-variance-swap|forward var]] used by vol funds, and the construction of vol indices such as the [[vix|VIX]] -- which is itself, mechanically, a one-month variance swap on the SPX.

## Contract Mechanics

A variance swap is defined by a small number of parameters:

| Parameter | Typical value | Notes |
|---|---|---|
| **Underlying** | SPX, SX5E, single-stock, FX pair | Equity index variance is the deepest market |
| **Tenor** | 1m, 3m, 6m, 1y, 2y | 3m and 1y are the most liquid |
| **Variance strike (K_var)** | Quoted as a vol number, e.g. "18.5" | Squared internally: K_var = 18.5^2 = 342.25 |
| **Variance notional (N_var)** | $/variance point | Often quoted via vega notional N_vega = 2 * K_var * N_var |
| **Sampling** | Daily close-to-close log returns | Calendar days vs business days conventions vary |
| **Annualization factor** | 252 (business) or 365 | Specified in confirm |

The realized variance over the life of the swap is computed as:

```
RV = (252 / N) * sum_{i=1..N} ln(S_i / S_{i-1})^2
```

where `N` is the number of daily returns observed. The buyer's payoff at maturity is:

```
Payoff = N_var * (RV - K_var^2)
```

quoted in dollars per variance point. The vega notional `N_vega = 2 * K_var * N_var` gives an intuitive $-per-vol-point sensitivity at inception (because the derivative of variance with respect to vol is `2 * vol`).

Most contracts include a **variance cap** -- typically `2.5 * K_var` or `(2.5 * K_var)^2` in variance terms -- that limits the maximum payout. Caps were nearly universal post-2008 after several uncapped books blew through their risk limits during volatile sessions.

## Pricing and Replication

The defining theoretical insight of variance swaps is that their payoff can be replicated **statically** using a portfolio of European options of all strikes. This is the [[carr-madan-replication|Carr-Madan log-contract result]] (Carr & Madan, 1998; formalized in [[demeterfi-derman-kamal-zou-1999|Demeterfi, Derman, Kamal, Zou 1999]] -- the canonical Goldman Sachs primer).

The intuition: realized variance over a continuous path is mathematically equivalent to `-2 * E[ln(S_T / S_0)]` plus a known drift term. The function `ln(S)` can be replicated using a continuum of out-of-the-money puts and calls, weighted as `1 / K^2`. Concretely, the fair variance strike is:

```
K_var^2 = (2 / T) * [ integral_{0}^{F} (1/K^2) * P(K) dK
                    + integral_{F}^{inf} (1/K^2) * C(K) dK ]
```

where `F` is the forward, `P(K)` and `C(K)` are OTM put and call prices. In practice dealers replicate using a discrete grid of listed strikes, accepting a small basis from the continuous formula.

Two practical consequences:

1. **The variance strike is determined by the entire smile**, not just at-the-money implied vol. A steep [[volatility-skew|skew]] raises the variance strike above the ATM IV.
2. **Hedging a variance swap requires owning a strip of options and dynamically delta-hedging each one.** A short-variance position is therefore short a strip of OTM puts -- which is why dealer books became so dangerous in 2008 when crash risk was repriced.

## Variance Swap vs Volatility Swap

A **volatility swap** pays `N_vol * (sqrt(RV) - K_vol)` -- that is, realized vol rather than realized variance. Despite sounding cleaner, vol swaps cannot be statically replicated; they require dynamic hedging and are usually quoted off variance swaps.

The relationship between the two strikes is the **convexity adjustment**:

```
K_var ≈ K_vol + 0.5 * vol-of-vol^2 * T / K_vol
```

(intuitively: variance is a convex function of vol, so by [[jensens-inequality|Jensen's inequality]] the variance strike sits above the squared vol strike). The convexity adjustment is small in calm regimes and large when vol-of-vol is high. In practice traders quote vol-swap fair value as `K_var - convexity adjustment`, with the adjustment estimated from historical or implied vol-of-vol.

## Greek Exposures: Why a Variance Swap Behaves Like a Static Option Strip

Although a variance swap has no spot exposure at inception, the static replication (a strip of OTM options weighted `1/K^2`, dynamically delta-hedged) embeds the classic option Greeks. Understanding them is essential to running a variance book:

| Greek | Variance swap behaviour | Practical consequence |
|---|---|---|
| **Delta** | Zero at inception by construction; the replicating strip is delta-hedged continuously | A pure variance swap is **direction-neutral** — its P&L depends only on how much spot moves, not where it ends |
| **Vega** | Constant in *variance* terms; in *vol* terms it equals `N_vega = 2 * K_var * N_var` and decays linearly to zero at maturity | A long variance swap is **long vega**, but the vega is "fair" across the whole smile, not just ATM |
| **Gamma** | The strip is **constant-cash-gamma** (dollar-gamma independent of spot) — this is the defining property that makes the payoff equal to realized variance | The buyer is paid for every squared return regardless of strike; this is why variance, not vol, is replicable |
| **Theta** | The accrued variance offsets time decay; the position bleeds the strike `K_var^2` per unit time and collects realized `RV` | Long var "pays theta" only when realized vol < implied — i.e. the [[variance-risk-premium]] is the structural cost |
| **Vanna / Volga** | Embedded via the smile weighting; a steep [[volatility-skew|skew]] feeds into the strike but the *position* itself is first-order skew-neutral | Skew changes reprice the entry strike, not the floating leg |

The `1/K^2` weighting is the crucial detail: it produces **uniform sensitivity to log-returns across all spot levels**, which is what makes dollar-gamma constant and the payoff path-independent. A single ATM [[straddle]], by contrast, has gamma that peaks at the strike and collapses as spot moves away — which is precisely the path-dependence variance swaps were designed to eliminate.

## Vol-of-Vol and the Convexity of Realized Variance

Because variance is the *square* of volatility, a long variance swap is implicitly **long vol-of-vol** (long the volatility of volatility). The payoff is convex in realized vol: a move from 20 to 40 vol quadruples variance, while a move from 20 to 10 only quarters it. This asymmetry means:

- Long-variance positions benefit disproportionately from **vol spikes** relative to the symmetric loss from vol declines — a built-in positive convexity that makes variance swaps attractive crisis-alpha vehicles (see [[tail-risk-hedging]]).
- Short-variance positions carry the mirror-image **negative convexity**: bounded gains in calm regimes, unbounded losses (absent a cap) in spikes. This is the structural reason short-variance books are so dangerous and why the 2008 losses were so severe relative to the vega notional carried.
- The convexity is the economic source of the **variance-vs-volatility-swap spread** (the convexity adjustment in the prior section): variance always trades at a premium to the squared vol-swap strike, and that premium widens with expected vol-of-vol.

## Term Structure and Forward Variance

Variance is **additive across time**, which gives variance swaps a clean term structure that bond and rates traders find intuitive. Total variance over `[0, T2]` equals variance over `[0, T1]` plus forward variance over `[T1, T2]`:

```
T2 * K_var(0,T2)^2  =  T1 * K_var(0,T1)^2  +  (T2 - T1) * FwdVar(T1,T2)
```

A **[[forward-variance-swap|forward variance swap]]** isolates the variance accruing over a future window `[T1, T2]`. Traders construct it by going long the far-dated total-variance swap and short the near-dated one, scaled by tenor. Forward variance is the natural instrument for:

- **Term-structure trades** — betting that the variance curve is too steep or too flat (analogous to a steepener/flattener on the [[yield-curve|rates curve]]).
- **Event isolation** — buying forward variance that spans an earnings date, central-bank meeting, or election while avoiding the carry cost of the nearer window.
- **Roll-down harvesting** — when the variance term structure is in contango (typical in calm regimes), forward variance rolls down toward lower spot variance, a structural short-vol carry that vol funds like [[capstone-investment-advisors|Capstone]] exploit.

The variance term structure usually mirrors the [[vix-futures]] curve: **contango in calm markets** (forward variance > spot variance, reflecting the [[variance-risk-premium]]) and **backwardation in stress** (spot variance spikes above forward, reflecting mean-reversion expectations).

## Dispersion Trading

Dispersion is the single largest institutional use of variance swaps today. The trade is **short index variance, long a basket of single-name variance** (or the reverse), and it is fundamentally a bet on **correlation**:

```
Index variance  ≈  Σ w_i^2 * (single-name variance_i)  +  cross-correlation terms
```

Because index variance is suppressed when constituents are *uncorrelated* (diversification cancels idiosyncratic moves), selling index variance and buying single-name variance is **short implied correlation**. The trade profits when realized correlation comes in below the implied correlation embedded in index-vs-single-name vol spreads — historically a persistent premium, since index puts are structurally bid by hedgers (the [[variance-risk-premium]] is concentrated at the index level).

Dispersion via variance swaps is cleaner than via [[straddle]] baskets because the path-independence removes the need to continuously rebalance deltas across dozens of names. The implied-correlation level can be read directly off the ratio of index variance strike to the weighted single-name variance strikes. Dispersion books were among the worst-hit in 2008 (correlation went to ~1 in the crash, the opposite of the short-correlation bet) and again in March 2020.

## Connection to the VIX

The [[vix|CBOE VIX index]] is, mechanically, a 30-day variance swap fair-strike on the SPX, expressed as an annualized vol number. The VIX formula is the discrete-strike version of the Carr-Madan replication, computed twice daily off SPX listed options of all strikes. Owning a [[variance-swap]] on SPX with 30-day tenor and a strike equal to current VIX is approximately equivalent to a vega-neutral position relative to the VIX index itself.

This connection makes variance swaps the natural arbitrage instrument against [[vix-futures]]: dealers who run short-VIX-futures inventory frequently hedge with long-variance-swap positions, and vice versa.

## Use Cases / Who Trades These

| Participant | Direction | Motive |
|---|---|---|
| **Dedicated vol funds** ([[capstone-investment-advisors]], [[parallax-volatility-advisers]]) | Long vol | Express directional vol view; hedge equity book |
| **Dispersion desks** | Long single-name var, short index var | Bet on idiosyncratic risk vs correlation |
| **Bank exotic-option desks** | Short var (gamma seller) | Recycle vega received from selling structured products |
| **Risk-parity allocators** | Long var as crisis-alpha overlay | Convex hedge to equity book |
| **Pension / insurance** | Long var for [[tail-risk-hedging]] | Bounded-cost alternative to put protection |
| **CTA / macro funds** | Tactical long/short var | Trade vol regime shifts |

The buyer is typically anyone running a [[long-vol|long-vol]] book or hedging a structurally short-vol exposure. The seller is typically a bank desk recycling vega absorbed from structured products (autocallables, reverse convertibles, [[short-strangle|short strangles]] sold to retail wrappers), or a [[short-vol|short-vol]] hedge fund harvesting the [[variance-risk-premium]].

## Comparison to Related Volatility Instruments

| Instrument | Exposure | Path-dependent? | Listed/Cleared? | Replicable statically? | Best for |
|---|---|---|---|---|---|
| **Variance swap** | Realized variance vs strike | No | Mostly OTC, ISDA | Yes (option strip) | Clean pure-vol view; dispersion; term-structure trades |
| **[[volatility-swap|Volatility swap]]** | Realized vol vs strike | No (but needs dynamic hedge) | OTC | No (needs convexity adj.) | Linear-in-vol payoff; less convex than var |
| **[[vix-futures|VIX futures]]** | Forward 30-day implied variance | No | Listed, cleared (CFE) | N/A | Liquid, low-friction vol exposure; term-structure roll |
| **VIX options** | Options on forward implied variance | Yes | Listed, cleared | N/A | Convex bets on vol-of-vol; tail hedges |
| **[[delta-hedged-options|Delta-hedged option]]** | Gamma/theta on one strike | **Yes** (gamma peaks at strike) | Listed | N/A | Localized vol view near one strike |
| **[[straddle]] / [[strangle]]** | Vol + residual direction | **Yes** | Listed | N/A | Cheap, simple, but path- and pin-sensitive |
| **[[forward-variance-swap|Forward variance swap]]** | Variance over a future window | No | OTC | Yes (calendar of var swaps) | Term-structure and event-isolation trades |

The variance swap's edge over every alternative is **exact path-independence with no delta management** — you are paid precisely for realized variance regardless of the route spot takes. Its disadvantages are **OTC counterparty risk** (vs listed [[vix-futures]]), **non-standard documentation**, and the **dangerous convexity** that has to be capped.

## Risks / Failure Modes

Variance swaps are conceptually clean but operationally dangerous when sold without a cap:

1. **Convex payoff in realized variance.** A move from 15 to 60 vol is a 16x increase in variance. A short-variance position uncapped can lose far more than the vega notional suggests -- the 2008 short-var carnage was driven by this convexity.
2. **Path-independence cuts both ways.** Unlike a [[delta-hedged-options|delta-hedged option]], the seller cannot reduce exposure by hedging spot. Variance keeps accumulating as long as the asset moves.
3. **Jump risk and cap basis.** Capped contracts pay max `2.5 * K_var` realized; if a single overnight gap pushes variance above the cap, the buyer is left with uncapped downside on the rest of the tenor while the dealer is fully off-risk.
4. **Replication basis.** Real dealer hedges use a finite grid of listed strikes. In a tail event, the unlisted-deep-OTM-put portion of the replication is missing, and the dealer is short more variance than the model assumes.
5. **Counterparty risk** (pre-clearing). Variance swaps are OTC; in 2008 several long-variance positions had counterparty exposure to failing dealers. Post-Dodd-Frank, central clearing has reduced but not eliminated this.
6. **Liquidity in stress.** Bid-ask on variance swaps widens 5-10x in vol shocks; getting flat is expensive.

## Notable Events

- **2008 GFC.** Large bank short-variance books incurred losses estimated in the multi-billion-dollar range as realized variance on equity indices spiked 4-5x. Several desks were closed or repurposed. After 2008, almost all new variance swap trades are capped, and dealer risk limits on net short-variance exposure were tightened across the industry.
- **August 2015 (China devaluation).** Realized variance on SPX briefly spiked, caused mark-to-market losses on dealer short-var inventory; dealers rotated short-var hedges into [[vix-futures]] instead.
- **[[volmageddon|February 2018]].** While the headline blow-up was [[xiv-velocity-shares|XIV]] and [[ljm-preservation-and-growth|LJM]] in the [[vix-futures]] complex, the underlying vol-of-vol shock also widened bid-ask on variance swaps and forced several dealer desks to mark down their short-var inventory.
- **March 2020 (COVID crash).** Realized variance on SPX hit ~70-vol annualized over the worst month -- the largest realized-vs-implied gap on record. Long-variance positions returned multiples of premium. Capped contracts hit caps; uncapped variance is now nearly extinct in the dealer market.
- **[[vix-august-2024-spike|August 2024 spike]].** Yen carry unwind drove realized-variance spike; long-variance positions saw rapid markups, but the move reversed within two weeks, illustrating how short-tenor variance is highly sensitive to single sessions.

## Post-2008 Evolution

Several structural changes have reshaped the market since 2008:

- **Caps are universal.** Almost every new variance swap is capped at `2.5 * K_var`. Uncapped variance is rare and priced at a significant premium to the capped equivalent.
- **Listed alternatives.** [[vix-futures]] and VIX options provide listed, cleared, lower-friction exposure for many use cases. The variance swap market has consolidated toward institutional users who specifically need the path-independence.
- **Regulatory clearing pressure.** Dodd-Frank and EMIR pushed many derivatives toward central clearing; variance swaps remain mostly bilateral due to non-standard sampling conventions, but documentation has standardized via ISDA.
- **Forward-variance products** ([[forward-variance-swap]]) for term-structure trades have become a niche but liquid corner of the market, used heavily by [[capstone-investment-advisors|Capstone]] and similar vol funds.
- **The [[variance-risk-premium]] trade itself has crowded** since the early 2010s; expected returns to systematic short-variance strategies have compressed from ~5-7% per year (pre-2008) to ~2-4% per year (post-2018), a regime shift that punishes naive short-variance harvesting.

## Related

- [[long-vol-vs-short-vol]] -- variance swaps as a clean expression of the vol-side bet
- [[variance-risk-premium]] -- the structural premium that variance buyers pay and sellers earn
- [[implied-volatility]] -- relationship between IV and variance strike
- [[realized-volatility]] -- the floating leg of the swap
- [[vix]] -- variance swap on SPX, expressed as a vol number
- [[vix-futures]] -- listed alternative for vol exposure
- [[volatility-swap]] -- linear-in-vol cousin requiring convexity adjustment
- [[log-contract]] -- the static-replication primitive
- [[carr-madan-replication]] -- the formal replication theorem
- [[tail-risk-hedging]] -- variance swaps as crisis-alpha vehicle
- [[gamma]], [[vega]] -- the Greek exposures variance swaps embed
- [[volmageddon]], [[vix-august-2024-spike]] -- events that repriced variance
- [[capstone-investment-advisors]] -- canonical institutional variance trader

## Sources

- Demeterfi, K., Derman, E., Kamal, M., Zou, J. (1999). *More Than You Ever Wanted to Know About Volatility Swaps*. Goldman Sachs Quantitative Strategies Research Notes -- the canonical practitioner primer on variance swap pricing, replication, and the vol-swap convexity adjustment.
- Carr, P., Madan, D. (1998). "Towards a Theory of Volatility Trading." *Volatility: New Estimation Techniques for Pricing Derivatives* (R. Jarrow ed.) -- the static-replication theorem that underlies the variance swap formula and the VIX index.
- Carr, P., Wu, L. (2009). "Variance Risk Premiums." *Review of Financial Studies* -- canonical empirical measurement of the variance risk premium across equity indices.
- CBOE. *VIX White Paper* (current edition) -- spells out the discrete-strike variance-swap formula used to compute the VIX.
- Bossu, S. (2014). *Advanced Equity Derivatives: Volatility and Correlation*. Wiley -- modern textbook treatment including post-2008 market structure.
