---
title: "Second-Order Greeks"
type: concept
created: 2026-04-13
updated: 2026-06-21
status: excellent
tags: [options, derivatives, risk-management, greeks]
aliases: ["Higher-Order Greeks", "Exotic Greeks", "Vanna", "Charm", "Vomma", "Volga", "Speed", "Color"]
domain: [risk-management, derivatives]
prerequisites: ["[[options-greeks]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]"]
difficulty: advanced
related: ["[[options-greeks]]", "[[delta]]", "[[gamma]]", "[[vega]]", "[[theta]]", "[[implied-volatility]]", "[[volatility-surface]]", "[[gamma-scalping]]", "[[delta-neutral]]", "[[vanna]]", "[[vomma]]", "[[charm]]", "[[gamma-explosion]]", "[[volatility-spike]]", "[[dealer-positioning]]", "[[0dte-trading]]", "[[volatility-risk-premium]]", "[[vix]]"]
---

The second-order (and higher-order) Greeks measure how the primary Greeks themselves change in response to market variables. While [[delta]], [[gamma]], [[theta]], and [[vega]] capture first-order sensitivities, professional traders and market makers need second-order Greeks to understand how their risk profile evolves dynamically — especially for large portfolios, exotic options, and positions held through volatile conditions.

## Overview

The primary Greeks tell you your current exposure. The second-order Greeks tell you how that exposure will shift when something changes. A portfolio that is delta-neutral and gamma-neutral *right now* may not stay that way if volatility moves ([[vanna]] effect) or time passes ([[charm]] effect). Ignoring second-order Greeks leads to surprises — hedges that drift, P&L that doesn't match expectations, and risk that appears from nowhere.

### The derivative lattice

Every Greek is a partial derivative of the option value `V` with respect to one of four state variables: spot `S`, volatility `σ`, time `t`, and rate `r`. The first-order Greeks are the four edges; the second-order Greeks are the cross- and self-derivatives that connect them. The table below organises the family so the relationships are visible at a glance.

| | ∂/∂S | ∂/∂σ | ∂/∂t |
|---|---|---|---|
| **Delta** (∂V/∂S) | [[gamma]] (∂Δ/∂S) | [[vanna]] (∂Δ/∂σ) | [[charm]] (∂Δ/∂t) |
| **Vega** (∂V/∂σ) | [[vanna]] (∂Vega/∂S) | [[vomma]] (∂Vega/∂σ) | veta (∂Vega/∂t) |
| **Gamma** (∂²V/∂S²) | speed (∂Γ/∂S) | zomma (∂Γ/∂σ) | color (∂Γ/∂t) |

Note that vanna appears twice — it is genuinely the same number whether you read it as "how delta moves with vol" or "how vega moves with spot" (mixed partials commute, Schwarz's theorem). The same symmetry makes charm `= −∂Θ/∂S` and speed `= ∂³V/∂S³`. The practically important members are vanna, charm, vomma, speed, and color; the rest (veta, zomma, ultima) appear mainly in exotic-desk risk reports.

## The Key Second-Order Greeks

### Vanna — Delta Sensitivity to Volatility

```
Vanna = ∂Δ/∂σ = ∂Vega/∂S
```

Vanna measures how [[delta]] changes when [[implied-volatility]] changes — or equivalently, how [[vega]] changes when the underlying price moves. It is a cross-derivative: it captures the interaction between price risk and volatility risk.

**Practical meaning**: If you hold a delta-neutral portfolio with significant vanna exposure, a spike in IV will shift your delta. You thought you were market-neutral, but now you have directional exposure that appeared solely from a volatility move.

**Where vanna is largest**:
- OTM options (both calls and puts) have the highest vanna in absolute terms
- ATM options have vanna near zero (their delta is relatively stable across IV changes)
- Vanna flips sign on either side of ATM: OTM calls have positive vanna (delta increases as IV rises), OTM puts have negative vanna

**Trading implications**:
- Market makers managing large OTM option inventory are heavily exposed to vanna
- After a volatility spike, market makers with short OTM put exposure experience delta shifts that force them to sell stock (hedging the new delta), amplifying the sell-off
- The "vanna flow" from dealer hedging is a significant driver of intraday market dynamics, particularly around [[vix]] spikes
- [[spotgamma|SpotGamma]] and other gamma exposure services track aggregate vanna positioning to predict these dealer-driven flows

### Charm (Delta Decay) — Delta Sensitivity to Time

```
Charm = ∂Δ/∂t = -∂Θ/∂S
```

Charm measures how [[delta]] changes as time passes — or equivalently, how [[theta]] changes as the underlying moves. It quantifies the "drift" in delta that occurs overnight even with no price movement.

**Practical meaning**: A delta-neutral portfolio today will not be delta-neutral tomorrow. Charm tells you how much delta you'll gain or lose overnight. This is especially important for positions near expiration, where charm effects are large.

**Where charm is largest**:
- OTM options: Charm causes OTM options to lose delta over time (they become "more OTM" in delta terms as time decays their probability of expiring ITM)
- ITM options: Charm causes ITM options to gain delta magnitude over time (approaching ±1.0)
- ATM options: Charm is relatively small (delta stays near 0.50 until close to expiration)
- Near expiration: Charm effects accelerate dramatically — this is why [[0dte-trading|0DTE]] positions require constant rehedging

**Trading implications**:
- Traders holding overnight positions must account for charm-induced delta drift
- Short-dated options portfolios need rehedging every morning even if the stock hasn't moved
- Calendar spread traders are exposed to charm differentials between the near-term and far-term legs

### Vomma (Volga) — Vega Sensitivity to Volatility

```
Vomma = ∂Vega/∂σ = ∂²Price/∂σ²
```

Vomma (also called volga) measures how [[vega]] changes when implied volatility changes. It is the "gamma of vega" — the convexity of the option price with respect to volatility.

**Practical meaning**: If you are long vomma, your vega increases as IV rises and decreases as IV falls. This is beneficial — you become more long vega when vega is profitable (rising IV) and less long vega when it's not. Long vomma creates a convex relationship to volatility.

**Where vomma is largest**:
- OTM and ITM options have the highest vomma (their vega is most sensitive to IV changes)
- ATM options have near-zero vomma (their vega is relatively stable)
- Long-dated options have higher vomma than short-dated options

**Trading implications**:
- Portfolios of OTM options (e.g., strangles, wide iron condors) have significant vomma exposure
- Long vomma is desirable for volatility traders — it creates convexity (you gain more from vol spikes than you lose from vol drops)
- The [[volatility-risk-premium]] partly compensates sellers for bearing negative vomma exposure — they suffer disproportionately from vol spikes
- Exotic options (barrier options, cliquets) can have extreme vomma, making them difficult to hedge

### Speed — Gamma Sensitivity to Price

```
Speed = ∂Γ/∂S = ∂³Price/∂S³
```

Speed measures how [[gamma]] changes as the underlying price moves. It is the third derivative of option price with respect to the underlying.

**Practical meaning**: Speed tells you how quickly your gamma exposure shifts when the market moves. A trader who is gamma-neutral may find their gamma position changes rapidly if speed is large — requiring more frequent rehedging.

**Where it matters**:
- Most relevant for market makers with large option inventories
- Important near expiration when gamma is already extreme and shifting rapidly
- Critical for [[0dte-trading|0DTE]] risk management where gamma can change by orders of magnitude with small price moves

### Color — Gamma Sensitivity to Time

```
Color = ∂Γ/∂t
```

Color measures how [[gamma]] changes as time passes. It quantifies overnight gamma drift.

**Practical meaning**: As expiration approaches, ATM gamma increases while OTM/ITM gamma decreases. Color tells you the rate of this convergence. A short gamma portfolio may find its gamma exposure intensifies overnight near expiration even with no price change.

## Summary Table

| Greek | Formula | Measures | Most Relevant For |
|-------|---------|----------|-------------------|
| **Vanna** | ∂Δ/∂σ | Delta change per IV change | OTM option books, dealer flows, crash dynamics |
| **Charm** | ∂Δ/∂t | Delta drift over time | Overnight hedging, near-expiry positions |
| **Vomma** | ∂Vega/∂σ | Vega change per IV change | Vol trading, tail risk, exotic options |
| **Speed** | ∂Γ/∂S | Gamma change per price move | Market making, 0DTE, large gamma books |
| **Color** | ∂Γ/∂t | Gamma drift over time | Expiration week, short gamma portfolios |

## Sign and Magnitude Map

Knowing the *sign* of each second-order Greek for a given position is what lets a trader anticipate which way their first-order Greeks will drift. The table below is for a **long single option** (buying a call or put); flip every sign for the short side. "Peak strike" is where the magnitude is largest relative to spot.

| Greek | Long call | Long put | Peak location | Decays toward expiry? |
|-------|-----------|----------|---------------|------------------------|
| [[vanna]] | + above ATM, − below | mirror | ~±15–25Δ wings (OTM) | rises (peak sharpens) |
| [[charm]] | drains delta if OTM, adds if ITM | mirror | OTM, accelerates near expiry | accelerates |
| [[vomma]] | + (long convexity) | + | OTM/ITM wings | falls (vega → 0) |
| speed | + for OTM call, sign varies | varies | just OTM of ATM | rises sharply |
| color | sign varies by moneyness | varies | ATM near expiry | accelerates |

Two readings make this table actionable:

1. **Wing Greeks vs body Greeks.** Vanna, vomma, and speed all peak in the *wings* (OTM/ITM), while plain gamma peaks ATM. A position that is gamma-flat at ATM can still be loaded with vanna and vomma if it holds wing strikes — this is exactly the profile of a [[short-strangle]] or wide [[iron-condor]].
2. **Time-accelerating vs time-decaying Greeks.** Charm, speed, and color all *intensify* as `t → 0` (they inherit the gamma explosion's `1/√t`-flavoured divergence — see [[gamma-explosion]]). Vomma *fades* as expiry approaches because vega itself collapses to zero. This is why second-order risk near expiry is dominated by charm/speed/color (delta- and gamma-drift), not by vomma.

## Worked Example — Vanna Surprise on a Delta-Neutral Book

*(Numbers are illustrative, chosen to show the mechanism, not from a live book.)*

A market maker is short 1,000 SPX 25-delta puts (struck at 4,800, spot 5,000, 20 DTE, IV 16%) and has hedged the position delta-neutral by buying index futures. The book reads delta ≈ 0, gamma small-and-short, vega short. The desk *thinks* it is directionally flat.

Overnight, an unexpected headline lifts SPX IV from 16% to 22% with **no change in spot**. Because OTM puts carry negative vanna, the rise in IV makes each short put's delta *more negative* (puts gain delta magnitude as IV rises). Suppose each contract's delta moves from −0.25 to −0.32. The book was short 1,000 puts, so the short-put delta moved from +250 (short of −0.25 is +0.25 each) to +320 — the book is now **+70 deltas long** purely from a vol move, with spot unchanged.

The maker's existing futures hedge is now wrong-sized. To re-neutralise they must *sell* 70 deltas of futures into a market that just got more volatile. Multiply this across every dealer running short-wing inventory and you get the **vanna flow** that mechanically pushes spot in the direction the vol move implied — a documented driver of the feedback between [[vix]] spikes and equity selloffs (see [[volatility-spike]] and [[dealer-positioning]]). The "surprise" P&L the desk sees the next morning is not noise; it is vanna doing exactly what its formula says it will.

## Portfolio Risk Management

At the institutional level, risk managers set limits not just on delta, gamma, theta, and vega but also on second-order exposures:

- **Vanna limits**: Prevent unexpected delta shifts from IV moves
- **Vomma limits**: Control non-linear vega exposure (particularly for short vol portfolios)
- **Charm budgets**: Account for overnight delta drift in hedging cost estimates

A portfolio that appears delta-neutral, gamma-neutral, and vega-neutral can still generate significant P&L from second-order effects. This "unexplained P&L" is often the second-order Greeks at work — particularly vanna during vol regime changes.

## When Second-Order Greeks Matter Most

1. **Volatility events**: Earnings, FOMC, geopolitical shocks — vanna and vomma dominate P&L
2. **Expiration week**: Charm and color effects accelerate; gamma changes rapidly
3. **Large portfolios**: Small second-order effects aggregate across many positions
4. **Exotic options**: Barriers, digitals, and path-dependent options have extreme second-order Greeks
5. **Short vol strategies**: [[iron-condor]], [[short-strangle]], [[short-straddle]] — negative vomma creates convex losses in vol spikes

## Common Pitfalls

- **Treating "delta-neutral" as "risk-free overnight."** Charm guarantees a delta-neutral book drifts away from neutral by morning even with a frozen tape. Re-mark and re-hedge at the open; do not assume yesterday's hedge still holds.
- **Vega-hedging a near-expiry position.** As `t → 0`, vega and vomma collapse while charm, speed, and color explode. Buying vega to "hedge" a 0–2 DTE short position spends money on a risk that is already gone and ignores the real (gamma/delta-drift) risk. See [[gamma-explosion]].
- **Forgetting vanna/vomma live in the wings.** A book hedged flat at ATM gamma can carry enormous wing exposure. Stress the book at ±1σ and ±2σ spot *with* a simultaneous IV shift, not one variable at a time — vanna only shows up in the joint move.
- **Ignoring sign flips across ATM.** Vanna changes sign at the money. A position that is net-positive vanna for an up-move can be net-negative for a down-move; a single aggregate number hides the asymmetry.
- **Confusing "unexplained P&L" with model error.** The residual after attributing delta/gamma/theta/vega P&L is usually second-order Greeks (especially vanna during regime changes), not a broken pricer. Build a second-order attribution bucket before blaming the model. See [[theta-realisation-ratio]] for the related decay-attribution discipline.
- **Reading exotic-Greek magnitudes off a vanilla intuition.** Barrier, digital, and cliquet options can have vomma and speed orders of magnitude larger than a vanilla and can flip sign across the barrier. Vanilla rules of thumb do not transfer.

## Related

- [[options-greeks]] — the primary Greeks from which these derive
- [[delta]] — first-order: vanna and charm are its second-order sensitivities
- [[gamma]] — first-order: speed and color are its second-order sensitivities
- [[vega]] — first-order: vomma is its second-order sensitivity
- [[vanna]] — delta-vs-vol cross-Greek; the dealer-flow driver
- [[vomma]] — vega convexity; the long-vol trader's friend
- [[charm]] — overnight delta drift
- [[volatility-surface]] — second-order Greeks shape how the vol surface deforms
- [[gamma-scalping]] — practical application requiring awareness of charm and speed
- [[gamma-explosion]] — why charm/speed/color explode near expiry
- [[volatility-spike]] — vanna and vomma dominate P&L during vol shocks
- [[dealer-positioning]] — aggregate vanna/charm flow as a market driver
- [[0dte-trading]] — extreme charm, speed, and color effects near expiration
- [[delta-neutral]] — maintaining neutrality requires understanding vanna and charm
- [[volatility-risk-premium]] — compensation for bearing negative vomma

## Sources

- [[book-option-volatility-and-pricing]] — Natenberg discusses higher-order Greeks and their role in professional risk management
- [[book-options-futures-other-derivatives]] — Hull's mathematical treatment of second-order partial derivatives of option pricing functions
- General market-making and dealer-flow literature on vanna/charm hedging flows ([[spotgamma]], [[squeezemetrics]] and similar dealer-positioning analytics) for the market-impact mechanism.
