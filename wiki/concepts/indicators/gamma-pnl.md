---
title: "Gamma P&L"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, risk-management, indicators, volatility]
aliases: ["Gamma P&L", "Gamma Pnl", "Gamma Component", "Realized Gamma"]
related: ["[[gamma]]", "[[delta]]", "[[theta]]", "[[vega]]", "[[options-greeks]]", "[[second-order-greeks]]", "[[options-risk-budgeting]]", "[[gamma-scalping]]", "[[realized-volatility]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[volatility-risk-premium]]", "[[short-strangle]]", "[[iron-condor]]", "[[delta-neutral]]", "[[volga]]"]
domain: [risk-management, derivatives]
prerequisites: ["[[gamma]]", "[[delta]]", "[[options-greeks]]"]
difficulty: advanced
---

**Gamma P&L** is the realized profit-or-loss component attributable to [[gamma]] alone over a holding period, after stripping out the linear delta P&L. For a delta-hedged book it is the *only* P&L from spot moves — and it is always positive for long-gamma positions and always negative for short-gamma positions, regardless of the direction of the move. Gamma P&L is the mechanism by which the difference between [[realized-volatility]] and [[implied-volatility]] is *monetized*: a long-gamma trader who delta-hedges captures (RV − IV) per unit of gamma, while their short-gamma counterparty pays it.

## Overview

[[gamma|Gamma]] is the second derivative of option price with respect to spot. By Taylor expansion, the option's price change for a spot move of ΔS is approximately:

```
ΔC ≈ Δ × ΔS + 0.5 × Γ × (ΔS)² + Vega × Δσ + Θ × Δt + ...
```

The first term is the **delta P&L** — linear in the move. The second term is the **gamma P&L** — quadratic in the move. The remaining terms capture vega, theta, and higher-order effects.

The full daily P&L attribution for an options book decomposes into these lines:

| P&L line | Greek term | Driver | Sign behaviour |
|---|---|---|---|
| Delta P&L | Δ × ΔS | Direction of the move | Linear; vanishes on a delta-hedged book |
| **Gamma P&L** | ½ Γ (ΔS)² | *Magnitude* of the move (squared) | Always +ve for long Γ, −ve for short Γ; sign of ΔS irrelevant |
| Vega P&L | Vega × Δσ | Change in [[implied-volatility]] | +ve for long [[vega]] when IV rises |
| Theta P&L | Θ × Δt | Passage of time | Long-Γ pays Θ; short-Γ collects Θ |
| Vanna P&L | [[vanna]] × ΔS × Δσ | Spot–vol cross-move | Material when IV moves *with* spot |
| Volga P&L | [[volga]] × (Δσ)² | Convexity in vol | Material in [[volatility-spike|vol spikes]] |

Gamma and theta are the two lines that are *mechanically linked* on a delta-hedged book: you pay theta to own gamma (long) or collect theta to be short it (short). The whole [[gamma-scalping]] trade is a bet that realized gamma P&L will exceed paid theta.

For a *delta-hedged* portfolio (delta = 0 immediately after each rebalance), the linear term vanishes between hedges. What remains, summed over the path, is the realized gamma component — the integral of (1/2)Γ(ΔS)² over each step.

This is the engine of [[gamma-scalping|gamma scalping]]: a long-gamma trader rebalances delta-to-zero repeatedly. Each rebalance locks in a small gain proportional to the squared move just realized. Cumulated over many small moves, this stream of (ΔS)² captures pay equal to the realized variance of the underlying. The cost is theta, which approximately equals the implied variance — so the net P&L is proportional to (RV² − IV²), the [[variance-risk-premium]].

## Definition / Formula

For a single discrete move ΔS, gamma P&L is:

```
Gamma P&L ≈ 0.5 × Γ × (ΔS)²
```

Where:
- **Γ** = portfolio gamma at the start of the interval (P&L per $1² of squared move)
- **ΔS** = absolute change in the underlying over the interval (in dollars)
- **(ΔS)²** = the squared move; always non-negative

Gamma P&L is **strictly non-negative for long Γ** and **strictly non-positive for short Γ**. The sign of ΔS doesn't matter — only its magnitude. A 1% up-move and a 1% down-move produce identical gamma P&L.

### Per-period and continuous form

For a series of N rebalanced sub-intervals over a holding period:

```
Gamma P&L_total ≈ 0.5 × Σᵢ Γᵢ × (ΔSᵢ)²
```

In the continuous-time, delta-hedged limit (Black-Scholes world), the Gamma P&L per unit time relates to realized variance:

```
dGamma P&L = 0.5 × Γ × S² × σ_RV² × dt
```

while the theta cost over the same interval is:

```
Theta cost = -0.5 × Γ × S² × σ_IV² × dt   (the gamma-theta identity)
```

Net carry per unit time (delta-hedged) is therefore:

```
Net P&L per dt = 0.5 × Γ × S² × (σ_RV² − σ_IV²) × dt
```

This is the precise mathematical statement of "long-gamma traders earn the [[variance-risk-premium]] when realized vol exceeds implied vol." See [[gamma-scalping]] for the full derivation.

### Re-expressed in percentage terms

Using ΔS = S × r, where r is the percentage return:

```
Gamma P&L ≈ 0.5 × Γ × S² × r²
```

The factor Γ × S² is sometimes called **dollar gamma** — P&L per (1% move)² is dollar gamma × 0.0001 × 0.5. Many platforms (TOS, IBKR) report dollar gamma natively because it is directly comparable to dollar P&L.

### Sign and interpretation table

The single most important property of gamma P&L is that its sign depends only on the *position*, never on the direction of the move:

| Position | Γ sign | Pays/collects Θ | Gamma P&L on any move | Wants RV vs IV | Canonical structure |
|---|---|---|---|---|---|
| Long options (net) | + | Pays Θ | Always positive | RV > IV | Long straddle, long [[gamma-scalping]] book |
| Short options (net) | − | Collects Θ | Always negative | RV < IV | [[short-strangle]], [[iron-condor]] |
| [[delta-neutral]] long-Γ | + | Pays Θ | Positive, ∝ realized variance | RV > IV | Dealer hedging long inventory |
| Delta-neutral short-Γ | − | Collects Θ | Negative, ∝ realized variance | RV < IV | Premium-selling overlay |

A useful mnemonic: **long gamma is long realized volatility; short gamma is short realized volatility.** The [[variance-risk-premium]] is the expected payout of that bet.

## Why It Matters (for risk-budgeted books)

Inside [[options-risk-budgeting]], gamma P&L is one of the four primary lines in the daily P&L attribution (delta, gamma, vega, theta). It is also the primary mechanism behind several risk realities:

1. **Short-gamma books bleed on every move.** A net-flat delta short-strangle book has Γ = -200 dollar gamma. Any 1% move in the underlying produces gamma P&L of 0.5 × -200 × 100² × 0.0001 = -$100. A 2% move produces -$400. The loss scales with the *square* of the move — moderate moves are an annoyance, large moves are catastrophic. This is the core reason short-vol books die in [[volatility-spike|vol spikes]].

2. **Long-gamma books need realized vol to break even.** A long straddle with Γ = +150 dollar gamma costs ~$80 of theta per day. To break even on theta from gamma alone, the day's move must satisfy 0.5 × 150 × 100² × r² ≥ 80, i.e. |r| ≥ 1.03%. If realized vol is below ~1%/day (i.e., <16% annualized), the position bleeds; above it, it earns.

3. **P&L attribution catches model errors.** A daily report that decomposes total P&L into Δ × ΔS + 0.5Γ(ΔS)² + Vega × ΔIV + Θ should explain ~80%+ of P&L. If gamma P&L explains far less than expected, either Γ is mismeasured (often because IV moved alongside spot — see [[vanna]]) or higher-order Greeks (volga, vanna, charm) are material. See the residual diagnostic in [[options-risk-budgeting]].

4. **Capacity and slippage planning.** Gamma P&L assumes you can rebalance delta at zero cost. In reality, rebalancing incurs slippage proportional to the size of the delta change. For high-gamma books, the rebalance cost can eat a meaningful fraction of theoretical gamma P&L — particularly in fast-moving, wide-spread regimes. This is why dealers reduce hedging frequency in stress.

5. **The dealer-flow narrative.** Aggregate market-maker gamma P&L drives the "[[gamma-exposure-trading|GEX]]" narrative: when dealers are long gamma, their hedging buys dips and sells rallies (stabilizing); when short, they sell dips and buy rallies (destabilizing). Gamma P&L is the literal P&L line being defended — dealers hedge to neutralize the gamma component because the alternative is unbounded losses on large moves.

## Hedging Frequency and the Capture Trade-off

Continuous-time gamma P&L is an idealization. Real traders rebalance at discrete intervals, and the choice of interval is a trade-off between *capturing* the realized variance and *paying* transaction costs to do so.

| Rebalance discipline | Variance captured | Transaction cost | Best regime |
|---|---|---|---|
| Continuous (theoretical) | 100% of RV | Infinite (impossible) | N/A — limit case |
| Time-based (e.g. hourly) | High; tracks RV closely | Moderate, predictable | Steady, mean-reverting tape |
| Time-based (daily) | Captures close-to-close variance only; misses intraday chop | Low | Slow-moving, low-cost markets |
| Delta-band (rehedge when |Δ| > threshold) | Tunable; captures the moves that matter | Activity-dependent; spikes in fast markets | Trending or jumpy markets |
| Move-based (rehedge on N-bp move) | Captures large moves, ignores noise | Concentrated in volatile windows | Event-driven, gap-prone names |

The gap between continuous-time and discrete-hedged gamma P&L is the **hedging error** — itself a random variable with mean roughly zero but non-trivial variance. Hedging more often shrinks the error but raises costs; the optimal band balances the two (the classic Leland / Whalley-Wilmott result). See [[gamma-scalping]] for the full treatment.

## P&L Attribution as a Diagnostic

A daily attribution report is the practical home of gamma P&L. The residual line — actual P&L minus the sum of the Greek-explained lines — is a model-quality signal:

| Residual size | Likely cause | Action |
|---|---|---|
| Near zero | Greeks well-measured; book behaving | None |
| Small, persistent same-sign | Stale or mis-signed Γ; missing carry | Re-measure Γ; check dividend/borrow carry |
| Large on big-move days | Higher-order Greeks ([[second-order-greeks|speed, color]]) material; Γ not constant along path | Re-price at path of spots, not start-of-day Γ |
| Large when IV moved with spot | [[vanna]] / [[volga]] cross-terms uncaptured | Add spot-vol cross-terms to attribution |

A book whose gamma P&L line consistently explains ~80%+ of spot-driven P&L is well-understood; one whose residual dominates is being run blind. See the residual diagnostic in [[options-risk-budgeting]].

## Worked Example

*(All figures below are illustrative — chosen for clean arithmetic, not drawn from a specific trade.)*

A short-premium book, 1 SPX iron condor, 30 DTE, sized to a 1-sigma wing:

- Net Γ = -2.5 (per SPX point²)
- Net Θ = +$50/day
- SPX at 5,000

The book is **delta-hedged daily** to zero. Below is one day where SPX moves +50 points (1% move):

**Step 1 — gamma P&L.**
ΔS = 50 points. Γ = -2.5.
Gamma P&L = 0.5 × (-2.5) × 50² = **-$3,125** (loss).

In the Taylor expansion this is the dominant term for a delta-hedged book.

**Step 2 — theta P&L.**
Time decay = +$50 (one day passed).

**Step 3 — vega P&L.**
Suppose IV unchanged for simplicity. Vega P&L = $0.

**Step 4 — net day's P&L.**
Total = -3,125 + 50 + 0 = **-$3,075**.

This is the canonical short-gamma pattern: the trader collects $50/day in theta to take **-0.5 × 2.5 × (ΔS)²** of risk on every realized move. Thirty days of $50 theta = $1,500. A *single* 1% adverse move erases ~2 months of theta income. A 2% move (gamma P&L = -$12,500) wipes out 8 months.

### The other side — a long-gamma scalper

The dealer on the other side of this trade is long the iron condor wings (long Γ = +2.5, short Θ = -$50/day). On the same 1% move, delta-hedged:

- Gamma P&L = +0.5 × 2.5 × 50² = **+$3,125**
- Theta P&L = -$50
- Net = +$3,075

This is the [[gamma-scalping]] mechanism: the dealer captures (RV − IV) profits realized as gamma P&L. Over a long horizon, if the option was sold at IV = 16% and SPX realizes RV = 22%, the dealer's cumulative gamma P&L exceeds cumulative theta cost — they earn the difference. If RV < IV, the trader on the short side wins the premium.

### Compound 1% moves over a month

Suppose the same short-Γ position experiences 20 trading days of 1% absolute moves (signs irrelevant — gamma P&L only cares about magnitude):

- 20 days × -$3,125 gamma P&L = -$62,500
- 20 days × +$50 theta = +$1,000
- Net = **-$61,500**

Realized vol of 1%/day ≈ 16% annualized. If the iron condor was sold at IV = 12%, the trader was structurally underpaid for the realized variance and the position is a steady loser. The variance gap (RV² − IV²) ≈ 0.0256 - 0.0144 = 0.0112 fully explains the ~$60k loss given the dollar gamma profile.

## Common Misuse / Pitfalls

1. **Forgetting that gamma P&L is path-dependent.** Two paths with the same start and end point produce different gamma P&L if their *realized variance* differs. A flat day with no rebalances yields zero gamma P&L; a chop day with the same close yields material gamma P&L. The integral of (ΔS)² over the path matters, not the start-to-end change.

2. **Confusing delta P&L with gamma P&L.** A long-call holder who does *not* delta-hedge captures the delta P&L (linear in the move) plus the gamma P&L (quadratic). The total is the option's price change. Gamma P&L only equals total spot-driven P&L *after* delta is hedged out.

3. **Ignoring the rebalance interval.** Continuous-time gamma P&L assumes infinite rebalances. In practice, traders hedge at discrete intervals (daily, hourly, by delta-band). Discrete hedging captures less than the continuous-time variance — the difference is the *hedging error*, which is itself a source of variance in P&L. Rebalancing more often reduces hedging error but increases transaction costs.

4. **Assuming Γ is constant.** Gamma changes with spot, time, and IV ([[second-order-greeks|speed, color, vanna]]). A 5% move in spot can change Γ by 50% or more. Computing gamma P&L using start-of-day Γ overstates accuracy on big-move days. *Mitigation*: integrate Γ along the path or use scenario tools that re-price the book at multiple spots.

5. **Mixing dollar gamma units.** Dollar gamma can be quoted "per 1% move" or "per $1 move" or "per index point." Same number, three units. Always confirm unit before using the formula.

6. **Forgetting vega when IV moves with spot.** In real markets, large spot drops are accompanied by large IV jumps ([[vix|VIX]] up). The pure gamma-P&L formula ignores this. Total P&L = gamma P&L + vega × ΔIV + cross terms (vanna, volga). For a book with negative gamma and negative vega, both lines lose simultaneously in a [[volatility-spike|vol spike]] — the joint loss is much worse than the sum of average independent losses.

7. **Ignoring the asymmetry in stress.** The Γ × (ΔS)² term assumes ΔS is finite and the function is locally quadratic. For very large jumps (gap moves, [[volmageddon|Volmageddon]] 2018, [[covid-19-crash|COVID 2020]]), higher-order terms (speed, color) and discontinuities make the simple formula understate the true loss. Stress testing should re-price under jumps, not extrapolate gamma P&L.

## Related

- [[gamma]] — first-order Greek that gamma P&L derives from
- [[delta]] — gamma P&L is what remains *after* delta P&L is hedged out
- [[theta]] — gamma P&L is paid for via theta in the BSM identity
- [[vega]] — companion P&L line; together with gamma defines spot-and-vol risk
- [[options-greeks]] — primer
- [[second-order-greeks]] — speed and color modify Γ along the path
- [[options-risk-budgeting]] — framework that consumes gamma P&L as a daily attribution line
- [[gamma-scalping]] — the strategy that monetizes gamma P&L for long-Γ traders
- [[realized-volatility]] — RV is what gamma P&L pays
- [[implied-volatility]] — IV is what theta charges
- [[variance-risk-premium]] — RV² − IV²; the gamma-scalp expectancy
- [[volatility-risk-premium]] — economic counterpart for the short-vol seller
- [[delta-neutral]] — required state for gamma P&L to dominate spot-driven P&L
- [[short-strangle]] — canonical short-gamma structure
- [[iron-condor]] — same
- [[volga]] — second-order vol convexity, parallel concept

## Sources

- [[book-options-futures-other-derivatives]] — Hull's derivation of the gamma-theta identity in Black-Scholes
- [[book-option-volatility-and-pricing]] — Natenberg on dollar gamma and the practical mechanics of gamma P&L attribution
- [[book-dynamic-hedging]] — Taleb on path-dependence and the gap between continuous-time gamma P&L and discrete hedging realities
