---
title: "Moneyness Selection"
type: concept
created: 2026-05-07
updated: 2026-06-20
status: excellent
tags: [options, derivatives, greeks, methodology]
aliases: ["ATM vs OTM vs ITM", "Moneyness Choice", "ITM/ATM/OTM Selection", "Moneyness"]
domain: [options]
prerequisites: ["[[options]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[options-selection-framework]]"]
difficulty: intermediate
related:
  - "[[delta]]"
  - "[[gamma]]"
  - "[[theta]]"
  - "[[vega]]"
  - "[[non-linear-payoff]]"
  - "[[strike-selection]]"
  - "[[options-selection-framework]]"
  - "[[options-liquidity-screening]]"
  - "[[expiration-selection]]"
  - "[[spread-width-selection]]"
  - "[[implied-volatility]]"
  - "[[iv-rank-and-iv-percentile]]"
  - "[[long-call]]"
  - "[[long-put]]"
  - "[[credit-spread]]"
  - "[[debit-spread]]"
  - "[[iron-condors]]"
  - "[[leaps]]"
  - "[[iv-crush]]"
  - "[[volatility-risk-premium]]"
  - "[[probability-of-profit]]"
---

**Moneyness** describes the relationship between an option's strike and the underlying's spot price. Selecting the right moneyness is filter 4 in the [[options-selection-framework]] and the choice that most directly determines a structure's Greeks profile, capital requirement, and payoff shape. The same strategy ("buy a call") at three different moneyness levels behaves like three different trades — gamma scalp, balanced directional bet, or stock replacement.

## Definitions

For a **call** option with strike $K$ and spot $S$:

- **In-the-money (ITM)**: $S > K$ — the option has intrinsic value (would be worth $S − K$ if exercised today)
- **At-the-money (ATM)**: $S \approx K$ — strike equals spot; intrinsic value is zero, all premium is extrinsic
- **Out-of-the-money (OTM)**: $S < K$ — no intrinsic value; premium is entirely extrinsic (time value)

For a **put** option, the relationships invert:

- ITM: $S < K$
- ATM: $S \approx K$
- OTM: $S > K$

Quantitatively, "ATM" usually means within $0.50-$1.00 of strike for stocks under $100, or within 0.5-1% of spot for indices. Most option chains have one strike that is "the ATM strike" at any moment; everything above is OTM (calls) or ITM (puts), and vice versa.

A second definition uses **forward price** rather than spot — ATM-forward (ATMF) is the strike equal to the forward price (spot adjusted for carry/dividends). For most short-dated equity options, ATM and ATMF differ by < 0.1% and the distinction doesn't matter; for LEAPS or commodity options it can.

## ATM Characteristics

ATM options sit at peak [[gamma]] and peak [[vega]] (in absolute dollar terms).

**Greeks at ATM** (approximate, for a 30 DTE option, 16% IV):

| Greek | ATM value (approx) | Notes |
|---|---|---|
| Delta (call) | ~+0.50 | Half the directional exposure of stock |
| Delta (put) | ~−0.50 | |
| Gamma | Maximum | Steepest rate of delta change |
| Theta | Largest absolute decay | "$/day" terms peak at ATM |
| Vega | Maximum | Largest IV sensitivity |

**Implications**:

- Maximum **gamma**: small spot moves create large delta changes. ATM options "wake up" quickly when the underlying moves; this is why gamma scalpers prefer ATM straddles.
- Maximum **vega**: ATM options gain or lose the most per unit IV change. Vol traders express vol views via ATM positions because the vega-to-premium ratio is highest there.
- Maximum **theta in absolute terms**: ATM ATM straddle decays $0.10-$0.30/day on liquid names — the dollar bleed is largest at ATM, even though the *percent* bleed is largest OTM.
- ~50% probability of finishing ITM at expiry — neither high-probability nor low-probability; balanced.

**When ATM is the right choice**:

- Long volatility (long straddle, long strangle near-ATM, ATM-ATM debit spreads)
- Gamma scalping (delta-hedged ATM positions)
- Earnings IV-crush short trades (short ATM straddles for max vega)
- Directional trades where the trader wants both gamma kick and vega exposure

## OTM Characteristics

OTM options are cheaper, lower-probability, with payoff profiles that emphasize the tail.

**Greeks at OTM** (16-delta example):

| Greek | OTM value | Notes |
|---|---|---|
| Delta (16d call) | ~+0.16 | Smaller directional exposure |
| Gamma | Modest | Lower than ATM but still meaningful |
| Theta | Smaller absolute, larger % of premium | OTM contracts decay 5-10%/day at 14 DTE |
| Vega | Smaller absolute, larger % of premium | OTM contracts are most exposed to IV crush |

**Implications**:

- **Cheap, lottery-ticket payoff**: a $1.00 16-delta OTM call can return 10-30x if a 1.5-sigma move occurs. The expected value, however, is *negative* on average for buyers because of vol risk premium.
- **Theta-bleed-as-percent-of-premium is largest** at OTM. A 16-delta OTM call at 14 DTE can lose 8-12% of its remaining premium per day, even when ATM contracts of the same DTE lose only 3-5%/day.
- **IV crush victims**: OTM options' premium is almost entirely extrinsic. When IV drops 30% (typical post-earnings crush), OTM premium can drop 50-70%. This is why long OTM pre-earnings trades systematically lose money even when the directional thesis is correct.
- **Higher P(losing the entire premium)**: ~84% chance the 16-delta call expires worthless. Premium-buyers lose total premium frequently, premium-sellers collect partial premium frequently.

**When OTM is the right choice**:

- Short premium (credit spreads, iron condors, short strangles, naked short calls/puts)
- Cheap directional speculation when the trader has high conviction on a *large* move
- Long tail hedges (e.g., 5% OTM SPY puts as portfolio insurance — see [[5-percent-otm-put-overlay]])
- Covered call overwrites and cash-secured put income strategies

## ITM Characteristics

ITM options behave more like the underlying — high delta, low time value, capital-intensive.

**Greeks at ITM** (70-delta example):

| Greek | ITM value | Notes |
|---|---|---|
| Delta (70d call) | ~+0.70 | Substantial directional exposure |
| Gamma | Modest, decreasing | Approaches zero deep ITM |
| Theta | Small | ITM premium is mostly intrinsic, not extrinsic |
| Vega | Smaller | Lower IV sensitivity than ATM |

**Implications**:

- **Behaves like stock**: a deep-ITM (80-90 delta) call rises $0.80-$0.90 when the underlying rises $1. Capital is committed but max loss is bounded — this is the essence of [[long-dated-options|stock replacement]].
- **High dollar premium**: a 70-delta call costs perhaps 7-10% of the underlying for 30-DTE expiration. This is capital-intensive in absolute terms but small relative to outright stock purchase.
- **Lower vega and theta**: time value is small relative to total premium. The trade is a delta+small-vega position.
- **High probability of ITM at expiry**: 70% chance of finishing ITM, 30% chance of expiring worthless or partly worthless.
- **Defined risk**: max loss is the premium paid — much less than the underlying's capital required for the equivalent stock position.

**When ITM is the right choice**:

- Stock replacement (deep-ITM LEAPS calls)
- High-conviction directional trades where the trader wants stock-like exposure
- Long leg of debit spreads (e.g., bull call spread: long 60-70 delta, short 25-30 delta)
- Synthetic positions (deep-ITM long call + short stock = synthetic long put, etc.)

## Strategy-by-Moneyness Mapping

A canonical mapping of common strategies to their typical moneyness profile:

| Strategy | Long leg moneyness | Short leg moneyness |
|---|---|---|
| **Long call (directional bullish)** | ATM (50d) standard; OTM if low-conviction lottery; ITM (70d+) for stock replacement | n/a |
| **Long put (directional bearish or hedge)** | Same as long call: ATM standard, OTM cheap-tail, ITM for high conviction | n/a |
| **Bull call spread (debit)** | ATM or slightly ITM (50-60d) | OTM (25-30d) |
| **Bear put spread (debit)** | ATM or slightly ITM (50-60d) | OTM (25-30d) |
| **Bull put spread (credit)** | OTM (5-10d) — protective long | OTM (16-30d) — premium-collecting short |
| **Bear call spread (credit)** | OTM (5-10d) | OTM (16-30d) |
| **Iron condor** | OTM both wings | OTM both shorts (16-delta both) |
| **Long straddle** | ATM (both call and put) | n/a |
| **Long strangle** | OTM both legs (16-30d each side) | n/a |
| **Short strangle** | n/a | OTM both legs (16-delta each side) |
| **Covered call** | underlying stock | OTM (20-30d) |
| **Cash-secured put** | n/a | OTM (20-30d) |
| **Stock replacement (LEAPS)** | Deep ITM (80-90d) | n/a |

The pattern: **debit spreads tend to be ATM-or-slightly-ITM long leg with OTM short leg** (capture intrinsic appreciation, finance with sold extrinsic). **Credit spreads are OTM both legs** (collect premium with defined wing). **Long premium directional trades pick moneyness by conviction** — high conviction → ITM, balanced → ATM, lottery → OTM.

## Decision Summary — Picking Moneyness by Objective

A one-table cheat sheet that collapses the trade-offs above. Pair this with [[strike-selection]] (which expresses the same choice as a delta target) and [[expiration-selection]].

| Trading objective | Moneyness | Why | Caveat |
|---|---|---|---|
| Max gamma (gamma scalp, vol play) | **ATM (50d)** | [[gamma]] and [[vega]] peak at ATM | Largest absolute [[theta]] bleed |
| Express a pure vol view | **ATM (50d)** | Highest vega-per-premium | IV must move your way |
| Cheap directional lottery | **OTM (5-16d)** | Low premium, convex payoff | Negative EV; [[iv-crush]] destroys it pre-earnings |
| Stock-like exposure, capped loss | **Deep ITM (80-90d)** | Delta near 1; low vega/theta | Capital-intensive in dollars |
| Premium income (sell vol) | **OTM short (10-30d)** | High [[theta]] as % of premium; high P(OTM) | Tail risk if move exceeds wing |
| Tail hedge / portfolio insurance | **OTM put (5-16d)** | Cheap convexity; captures skew | Bleeds [[theta]] when nothing happens |
| Finance a directional bet | **Debit spread: ITM long + OTM short** | Sell extrinsic to fund intrinsic | Caps upside at short strike |

The single most consequential mistake in moneyness selection is buying OTM premium into an earnings-announcement: the [[iv-crush]] guts the entirely-extrinsic premium even when the directional call is right (see earnings-iv-crush).

## Greek Behavior Across Moneyness

Visualizing how the Greeks change as a single option moves from deep OTM to deep ITM (constant DTE, constant IV):

```
Delta:    0.05 (deep OTM) → 0.16 → 0.30 → 0.50 (ATM) → 0.70 → 0.84 → 0.95 (deep ITM)
Gamma:    near 0          → rising → peaks at ATM → falling → near 0
Theta:    small absolute  → rising → peaks at ATM in $/day → falling → small
Vega:     small absolute  → rising → peaks at ATM → falling → small
Theta %:  largest         → smaller → smallest absolute → smaller as % → tiny
```

Key observations:

- **Delta** maps roughly to the standard normal CDF; flat in the tails, steep through ATM.
- **Gamma** is the *derivative* of delta — peaks where delta is changing fastest, which is ATM.
- **Theta in $/day** peaks ATM because that's where the most extrinsic value exists.
- **Theta as % of premium** is largest OTM because OTM premium is *entirely* extrinsic and small in absolute terms — losing $0.05 from a $0.50 OTM contract is 10%, while losing $0.10 from a $5.00 ATM contract is 2%.
- **Vega** peaks ATM and decays both directions because deep-ITM and deep-OTM options have less time value to be sensitive to IV.

This matters for **strategy design**: if you want maximum gamma exposure (gamma scalp, earnings vol play), pick ATM. If you want maximum vega exposure as a percentage of capital (long vol on a vol-rank-low underlying), still ATM. If you want maximum theta as a percentage of premium (short premium income), pick OTM. If you want stock-like behavior with capped downside, pick deep ITM.

## Worked Example — The Same Bullish View at Three Moneyness Levels

A trader is bullish on a $100 stock over the next 30 days and considers three single-leg long-call expressions (illustrative premiums, 30 DTE, ~25% IV):

| Expression | Strike / [[delta]] | Premium | Behaves like | Best case (stock → $115) | Worst case |
|---|---|---|---|---|---|
| **OTM lottery** | 110 / ~16d | ~$1.20 | A convex bet on a *large* move | ~$5 intrinsic ≈ +300% | Total loss (~84% of the time) |
| **ATM balanced** | 100 / ~50d | ~$4.00 | Half-delta directional + gamma + vega | ~$15 intrinsic ≈ +275% | Total loss; bleeds [[theta]] fastest in $/day |
| **ITM stock replacement** | 90 / ~80d | ~$11.50 | Leveraged long stock, capped downside | ~$25 intrinsic ≈ +117% | Loss bounded at $11.50 (vs ~$100 to own shares) |

Reading the table:

- If the trader's edge is a **specific large catalyst** (e.g., a buyout rumor), the OTM call's convexity wins — but only if the move is big and *soon*, because [[theta]] as a % of premium is brutal OTM.
- If the trader wants a **balanced directional bet** with some vol kicker, ATM is the default — most directional speculation lives here.
- If the trader essentially wants to **own the stock with less capital and a hard floor on loss**, the deep-ITM call is the [[leaps|stock-replacement]] choice; it surrenders the highest percentage return for the highest probability of a positive outcome (~80% finish ITM).

There is no universally "best" moneyness — the right choice is the one whose Greek profile matches the *thesis* (conviction, expected move size, time horizon, and vol view), filtered by [[options-liquidity-screening|liquidity]].

## Synthetic Positions

The relationship between ITM/ATM/OTM combinations creates **synthetic equivalents**:

- **Deep-ITM long call ≈ long stock** (delta near 1.0, theta and vega small)
- **Deep-ITM long put + long stock ≈ synthetic long call** (the put is cheap insurance)
- **Long call + short put (same strike, same expiry) = synthetic long stock** (put-call parity)
- **Long put + short call (same strike, same expiry) = synthetic short stock**
- **Deep-OTM call + deep-OTM put ≈ long volatility wings** (used in [[iron-condors]] as the protective wings)

Synthetic equivalences explain why stock-replacement with deep-ITM LEAPS is structurally equivalent to leveraged long stock — the LEAPS holder pays small theta and small vega in exchange for capping downside at the premium paid, which is the cost of an embedded out-of-the-money put.

## Moneyness, Liquidity, and Slippage

Moneyness and [[options-liquidity-screening|liquidity]] interact: liquidity peaks ATM and decays both directions. The 50-delta strike on SPY has 5-10x the OI of the 5-delta strike. Implications:

- ATM options have the tightest bid-ask in absolute and percentage terms
- Far-OTM options have the widest *relative* bid-ask (low absolute price, fixed minimum tick)
- Deep-ITM options have wide *absolute* bid-ask but reasonable relative spread (because absolute premium is high)

Practical rule: stay within 2 standard deviations of ATM (roughly 5-95 delta range) for any structure that needs to be exited cleanly. Beyond that, liquidity collapses and fill economics dominate any theoretical edge.

## Moneyness and IV Skew

[[implied-volatility|IV]] varies across moneyness — the **volatility smile/skew**. For equity indices (SPX, SPY), the skew is "negative-skewed":

- OTM puts have higher IV than OTM calls of equivalent moneyness
- The 16-delta SPX put might trade at 18 vol, while the 16-delta call trades at 13 vol
- This is "downside skew" — the market prices crash insurance at a premium

Implications for moneyness selection:

- Selling OTM puts on equity indices captures **skew premium** in addition to vol risk premium — structurally attractive for premium sellers
- Buying OTM puts as hedges is *expensive* relative to equivalent OTM calls — but the embedded crash insurance is what's being paid for
- ATM options sit at the "neutral" point of the smile; their IV is roughly the index's central vol estimate
- Deep ITM options inherit the IV of their OTM counterpart via put-call parity — a deep ITM call has the IV of the deep-OTM put at the same strike

## Common Pitfalls

1. **Buying OTM premium into earnings.** The premium is entirely extrinsic and the earnings [[iv-crush]] destroys it regardless of direction. The directional move must beat the *full* premium plus the crush.
2. **Confusing absolute and percentage theta.** ATM has the largest *dollar* decay; OTM has the largest decay *as a percent of premium*. Income sellers want the latter, which is why short premium lives OTM.
3. **Over-paying for OTM convexity.** Cheap-looking OTM calls/puts carry deeply negative expected value because of the [[volatility-risk-premium]]. "Cheap in dollars" is not "cheap in EV."
4. **Treating deep ITM as risk-free leverage.** Deep-ITM stock replacement still carries the full directional downside down to the strike; the embedded put only caps loss at the premium paid.
5. **Ignoring liquidity far from ATM.** Beyond ~5-95 delta, [[options-liquidity-screening|liquidity]] collapses and bid-ask economics swamp any theoretical edge.
6. **Mismatching moneyness to thesis.** A high-conviction directional view executed via far-OTM contracts is a vol/timing bet in disguise, not a directional bet.

## Related

- [[delta]] — primary Greek that varies with moneyness
- [[gamma]] — peaks at ATM
- [[theta]] — largest absolute at ATM, largest % at OTM
- [[vega]] — peaks at ATM
- [[non-linear-payoff]] — moneyness drives the curvature of the payoff diagram
- [[strike-selection]] — moneyness choice expressed via delta target
- [[options-selection-framework]] — moneyness is filter 4
- [[options-liquidity-screening]] — liquidity collapses far from ATM
- [[expiration-selection]] — interacts with moneyness (e.g., far-OTM weeklies are illiquid)
- [[spread-width-selection]] — width choice given a chosen moneyness
- [[implied-volatility]], [[iv-rank-and-iv-percentile]] — IV context that shifts optimal moneyness
- [[iv-crush]] — why OTM premium evaporates after earnings
- [[volatility-risk-premium]] — structural reason OTM buyers lose on average
- [[probability-of-profit]] — moneyness expressed as a probability
- [[long-call]], [[long-put]], [[credit-spread]], [[debit-spread]], [[iron-condors]] — strategies with canonical moneyness choices
- [[leaps]] — deep-ITM moneyness is the standard for stock replacement

## Sources

- Sheldon Natenberg, *Option Volatility and Pricing* — Greek behaviour across moneyness, the volatility smile/skew
- John C. Hull, *Options, Futures, and Other Derivatives* — delta as the option's probability proxy, put-call parity and synthetics
- Lawrence McMillan, *Options as a Strategic Investment* — moneyness choices for directional and income structures
- CBOE Options Institute — strike-selection and moneyness educational materials
- General market knowledge; no specific wiki source ingested yet.
