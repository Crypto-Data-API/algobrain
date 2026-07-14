---
title: "Moneyness Selection"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, derivatives, crypto, greeks, methodology]
markets: [crypto, options]
aliases: ["ATM vs OTM vs ITM", "Moneyness Choice", "ITM/ATM/OTM Selection", "Moneyness"]
domain: [options]
prerequisites: ["[[options]]", "[[delta]]", "[[gamma]]", "[[theta]]", "[[vega]]", "[[options-selection-framework]]"]
difficulty: intermediate
related:
  - "[[deribit]]"
  - "[[funding-rate]]"
  - "[[risk-reversal]]"
  - "[[crypto-options-volatility-selling]]"
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

**Moneyness** describes the relationship between an option's strike and the underlying's spot price. Selecting the right moneyness is filter 4 in the [[options-selection-framework]] and the choice that most directly determines a structure's Greeks profile, capital requirement, and payoff shape. The same strategy ("buy a call") at three different moneyness levels behaves like three different trades — gamma scalp, balanced directional bet, or coin replacement. The Greek behaviour below is universal; the one place crypto genuinely diverges from the equity framing this page was first written for is **IV skew** — where crypto's smile is driven by the [[perpetual-futures|perp]]/[[funding-rate|funding]] book rather than static hedging demand (see *Moneyness and IV Skew* and *Crypto specifics*).

## Definitions

For a **call** option with strike $K$ and spot $S$:

- **In-the-money (ITM)**: $S > K$ — the option has intrinsic value (would be worth $S − K$ if exercised today)
- **At-the-money (ATM)**: $S \approx K$ — strike equals spot; intrinsic value is zero, all premium is extrinsic
- **Out-of-the-money (OTM)**: $S < K$ — no intrinsic value; premium is entirely extrinsic (time value)

For a **put** option, the relationships invert:

- ITM: $S < K$
- ATM: $S \approx K$
- OTM: $S > K$

Quantitatively, "ATM" usually means within ~0.5-1% of spot; on BTC/ETH, where strikes are spaced in dollar increments, one listed strike is "the ATM strike" at any moment, and everything above is OTM (calls) or ITM (puts), and vice versa.

A second definition uses **forward price** rather than spot — ATM-forward (ATMF) is the strike equal to the forward. In crypto the forward embeds [[perpetual-futures|perp]]/futures **basis and [[funding-rate|funding]]**, not dividends and risk-free rates. For short-dated crypto options in calm markets ATM and ATMF differ little, but when funding is deeply positive (leveraged-long crowd) the forward can sit meaningfully above spot and the ATMF strike shifts up — a distinction that matters more in crypto than in short-dated equity options, and more again on the long end (see [[long-dated-options]]).

## ATM Characteristics

ATM options sit at peak [[gamma]] and peak [[vega]] (in absolute dollar terms).

**Greeks at ATM** (approximate, for a 30 DTE option, 16% IV):

| Greek | ATM value (approx) | Notes |
|---|---|---|
| Delta (call) | ~+0.50 | Half the directional exposure of spot |
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
- Gamma scalping (delta-hedged ATM positions) — the crypto version hedges with the [[perpetual-futures|perp]] and pays/collects [[funding-rate|funding]] on the hedge leg
- Catalyst IV-crush short trades (short ATM straddles into FOMC, a [[token-unlocks|token unlock]], or an ETF-decision date for max vega — crypto has no earnings)
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
- **IV crush victims**: OTM options' premium is almost entirely extrinsic. When IV drops 30% (a typical post-catalyst DVOL/IV crush after FOMC, an unlock, or an ETF decision), OTM premium can drop 50-70%. This is why long OTM pre-catalyst trades systematically lose money even when the directional thesis is correct.
- **Higher P(losing the entire premium)**: ~84% chance the 16-delta call expires worthless. Premium-buyers lose total premium frequently, premium-sellers collect partial premium frequently.

**When OTM is the right choice**:

- Short premium (credit spreads, iron condors, short strangles, naked short calls/puts) — see [[crypto-options-volatility-selling]]
- Cheap directional speculation when the trader has high conviction on a *large* move
- Long tail hedges (e.g., 5-10% OTM BTC puts as portfolio insurance — see [[tail-risk-hedging]])
- Covered-call overwrites on spot BTC/ETH and cash-secured put income strategies

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

- **Behaves like spot**: a deep-ITM (80-90 delta) call rises $0.80-$0.90 when the underlying rises $1. Capital is committed but max loss is bounded — this is the essence of [[long-dated-options|coin replacement]], and unlike a leveraged [[perpetual-futures|perp]] it cannot be liquidated at a bad tick.
- **High dollar premium**: a 70-delta call costs perhaps 7-10% of the underlying for 30-DTE expiration. This is capital-intensive in absolute terms but small relative to holding spot outright.
- **Lower vega and theta**: time value is small relative to total premium. The trade is a delta+small-vega position.
- **High probability of ITM at expiry**: 70% chance of finishing ITM, 30% chance of expiring worthless or partly worthless.
- **Defined risk**: max loss is the premium paid — much less than the capital required to hold the equivalent spot position.

**When ITM is the right choice**:

- Coin replacement (deep-ITM long-dated calls on BTC/ETH — see [[long-dated-options]])
- High-conviction directional trades where the trader wants spot-like exposure
- Long leg of debit spreads (e.g., bull call spread: long 60-70 delta, short 25-30 delta)
- Synthetic positions (deep-ITM long call + short perp = synthetic long put, etc.)

## Strategy-by-Moneyness Mapping

A canonical mapping of common strategies to their typical moneyness profile:

| Strategy | Long leg moneyness | Short leg moneyness |
|---|---|---|
| **Long call (directional bullish)** | ATM (50d) standard; OTM if low-conviction lottery; ITM (70d+) for coin replacement | n/a |
| **Long put (directional bearish or hedge)** | Same as long call: ATM standard, OTM cheap-tail, ITM for high conviction | n/a |
| **Bull call spread (debit)** | ATM or slightly ITM (50-60d) | OTM (25-30d) |
| **Bear put spread (debit)** | ATM or slightly ITM (50-60d) | OTM (25-30d) |
| **Bull put spread (credit)** | OTM (5-10d) — protective long | OTM (16-30d) — premium-collecting short |
| **Bear call spread (credit)** | OTM (5-10d) | OTM (16-30d) |
| **Iron condor** | OTM both wings | OTM both shorts (16-delta both) |
| **Long straddle** | ATM (both call and put) | n/a |
| **Long strangle** | OTM both legs (16-30d each side) | n/a |
| **Short strangle** | n/a | OTM both legs (16-delta each side) |
| **Covered call** | spot BTC/ETH | OTM (20-30d) |
| **Cash-secured put** | n/a | OTM (20-30d) |
| **Coin replacement (long-dated)** | Deep ITM (80-90d) | n/a |

The pattern: **debit spreads tend to be ATM-or-slightly-ITM long leg with OTM short leg** (capture intrinsic appreciation, finance with sold extrinsic). **Credit spreads are OTM both legs** (collect premium with defined wing). **Long premium directional trades pick moneyness by conviction** — high conviction → ITM, balanced → ATM, lottery → OTM.

## Decision Summary — Picking Moneyness by Objective

A one-table cheat sheet that collapses the trade-offs above. Pair this with [[strike-selection]] (which expresses the same choice as a delta target) and [[expiration-selection]].

| Trading objective | Moneyness | Why | Caveat |
|---|---|---|---|
| Max gamma (gamma scalp, vol play) | **ATM (50d)** | [[gamma]] and [[vega]] peak at ATM | Largest absolute [[theta]] bleed |
| Express a pure vol view | **ATM (50d)** | Highest vega-per-premium | IV must move your way |
| Cheap directional lottery | **OTM (5-16d)** | Low premium, convex payoff | Negative EV; [[iv-crush]] destroys it after a catalyst |
| Spot-like exposure, capped loss | **Deep ITM (80-90d)** | Delta near 1; low vega/theta | Capital-intensive in dollars |
| Premium income (sell vol) | **OTM short (10-30d)** | High [[theta]] as % of premium; high P(OTM) | Tail risk if move exceeds wing |
| Tail hedge / portfolio insurance | **OTM put (5-16d)** | Cheap convexity; captures skew | Bleeds [[theta]] when nothing happens |
| Finance a directional bet | **Debit spread: ITM long + OTM short** | Sell extrinsic to fund intrinsic | Caps upside at short strike |

The single most consequential mistake in moneyness selection is buying OTM premium into a scheduled catalyst (FOMC, a [[token-unlocks|token unlock]], an ETF-decision date): the [[iv-crush]] guts the entirely-extrinsic premium even when the directional call is right.

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

This matters for **strategy design**: if you want maximum gamma exposure (gamma scalp, catalyst vol play), pick ATM. If you want maximum vega exposure as a percentage of capital (long vol when DVOL is low in its range), still ATM. If you want maximum theta as a percentage of premium (short premium income), pick OTM. If you want spot-like behavior with capped downside, pick deep ITM.

## Worked Example — The Same Bullish View at Three Moneyness Levels

A trader is bullish on ETH (spot $3,000) over the next 30 days and considers three single-leg long-call expressions on Deribit (illustrative premiums, 30 DTE, ~55% IV — a typical crypto level):

| Expression | Strike / [[delta]] | Premium | Behaves like | Best case (ETH → $3,450) | Worst case |
|---|---|---|---|---|---|
| **OTM lottery** | 3,300 / ~16d | ~$36 | A convex bet on a *large* move | ~$150 intrinsic ≈ +315% | Total loss (~84% of the time) |
| **ATM balanced** | 3,000 / ~50d | ~$120 | Half-delta directional + gamma + vega | ~$450 intrinsic ≈ +275% | Total loss; bleeds [[theta]] fastest in $/day |
| **ITM coin replacement** | 2,700 / ~80d | ~$345 | Leveraged long ETH, capped downside | ~$750 intrinsic ≈ +117% | Loss bounded at $345 (vs $3,000 to hold spot) |

Reading the table:

- If the trader's edge is a **specific large catalyst** (e.g., an ETF approval or a major protocol upgrade), the OTM call's convexity wins — but only if the move is big and *soon*, because [[theta]] as a % of premium is brutal OTM, and crypto's fatter [[variance-risk-premium|variance risk premium]] means you overpay for that convexity.
- If the trader wants a **balanced directional bet** with some vol kicker, ATM is the default — most directional speculation lives here.
- If the trader essentially wants to **own the coin with less capital and a hard floor on loss** (and no perp-style liquidation risk), the deep-ITM call is the [[long-dated-options|coin-replacement]] choice; it surrenders the highest percentage return for the highest probability of a positive outcome (~80% finish ITM).

There is no universally "best" moneyness — the right choice is the one whose Greek profile matches the *thesis* (conviction, expected move size, time horizon, and vol view), filtered by [[options-liquidity-screening|liquidity]] (which in crypto means BTC/ETH, not alts).

## Synthetic Positions

The relationship between ITM/ATM/OTM combinations creates **synthetic equivalents**:

- **Deep-ITM long call ≈ long spot** (delta near 1.0, theta and vega small)
- **Deep-ITM long put + long spot ≈ synthetic long call** (the put is cheap insurance)
- **Long call + short put (same strike, same expiry) = synthetic long spot** (put-call parity — in crypto the parity forward embeds [[funding-rate|funding]]/basis, so the synthetic effectively bakes in the perp carry)
- **Long put + short call (same strike, same expiry) = synthetic short spot** (equivalently, a short [[perpetual-futures|perp]] with defined structure)
- **Deep-OTM call + deep-OTM put ≈ long volatility wings** (used in [[iron-condors]] as the protective wings)

Synthetic equivalences explain why coin-replacement with a deep-ITM [[long-dated-options|long-dated]] call is structurally equivalent to leveraged long spot — the holder pays small theta and small vega in exchange for capping downside at the premium paid, which is the cost of an embedded out-of-the-money put. Crucially, that capped downside means no forced liquidation, unlike the equivalent leverage taken via a perp.

## Moneyness, Liquidity, and Slippage

Moneyness and [[options-liquidity-screening|liquidity]] interact: liquidity peaks ATM and decays both directions. The 50-delta strike on Deribit BTC/ETH carries many times the OI of the 5-delta strike, and beyond BTC/ETH the whole chain is thin regardless of moneyness. Implications:

- ATM options have the tightest bid-ask in absolute and percentage terms
- Far-OTM options have the widest *relative* bid-ask (low absolute price, fixed minimum tick)
- Deep-ITM options have wide *absolute* bid-ask but reasonable relative spread (because absolute premium is high)

Practical rule: stay within 2 standard deviations of ATM (roughly 5-95 delta range) for any structure that needs to be exited cleanly. Beyond that, liquidity collapses and fill economics dominate any theoretical edge.

## Moneyness and IV Skew

[[implied-volatility|IV]] varies across moneyness — the **volatility smile/skew**. This is where crypto diverges most from equities. On equity indices (SPX, SPY) the skew is a near-*permanent* downside skew: OTM puts always trade richer than equivalent OTM calls, because the persistent bid is structural hedging demand. Crypto skew is **not static — it oscillates with the [[perpetual-futures|perp]] book**:

- In **leveraged bull runs**, [[funding-rate|funding]] is deeply positive (longs paying), the 25-delta [[risk-reversal|risk reversal]] can flip so that OTM *calls* trade rich to puts — a "perpetual-heavy" call skew that mirrors the crowded long-perp positioning. There is no equity analog to this.
- **After a crash**, protective-put demand spikes and the skew snaps to a steep downside (put) skew, just like equities — but temporarily, until funding and positioning normalize.
- So the crypto smile encodes *current leverage positioning*, not a fixed crash-insurance premium.

Implications for moneyness selection:

- The overbid wing is **observable in advance** via funding and the risk reversal — sell OTM calls when funding/call-skew is rich, OTM puts when the market has just paid up for downside. This is a readable edge equities' static skew doesn't offer (see [[crypto-options-volatility-selling]] and [[skew-trading]]).
- Buying OTM puts as hedges is *usually* expensive (downside skew), but in a funding-driven call-skew regime downside protection can be relatively cheap — check the risk reversal, don't assume.
- ATM options sit at the "neutral" point of the smile; their IV is roughly the [[dvol|DVOL]] central vol estimate.
- Deep ITM options inherit the IV of their OTM counterpart via put-call parity — a deep ITM call has the IV of the deep-OTM put at the same strike.

## Common Pitfalls

1. **Buying OTM premium into a scheduled catalyst** (FOMC, a [[token-unlocks|token unlock]], an ETF-decision date). The premium is entirely extrinsic and the post-event [[iv-crush]] destroys it regardless of direction. The directional move must beat the *full* premium plus the crush. (Crypto has no earnings, but its catalyst calendar produces the same IV-inflate-then-crush pattern.)
2. **Confusing absolute and percentage theta.** ATM has the largest *dollar* decay; OTM has the largest decay *as a percent of premium*. Income sellers want the latter, which is why short premium lives OTM.
3. **Over-paying for OTM convexity.** Cheap-looking OTM calls/puts carry deeply negative expected value because of the [[volatility-risk-premium]]. "Cheap in dollars" is not "cheap in EV."
4. **Treating deep ITM as risk-free leverage.** Deep-ITM coin replacement still carries the full directional downside down to the strike; the embedded put only caps loss at the premium paid.
5. **Ignoring liquidity far from ATM.** Beyond ~5-95 delta, [[options-liquidity-screening|liquidity]] collapses and bid-ask economics swamp any theoretical edge.
6. **Mismatching moneyness to thesis.** A high-conviction directional view executed via far-OTM contracts is a vol/timing bet in disguise, not a directional bet.

## Crypto Specifics

The Greek behaviour across moneyness (gamma/vega peak ATM, theta-% largest OTM, delta as a probability proxy) is model-driven and identical on crypto. The crypto-specific twists are:

- **Skew is dynamic and readable.** Unlike equities' near-permanent downside skew, the crypto 25-delta [[risk-reversal|risk reversal]] oscillates with [[funding-rate|funding]] — call skew rich in leveraged bull runs, put skew rich after crashes. Pick the wing to sell by reading funding and the risk reversal, not by assuming a fixed skew shape.
- **ATMF drifts with funding.** The forward embeds funding/basis, so in a high-funding regime the at-the-money-forward strike sits above spot — worth checking before calling a strike "ATM."
- **Moneyness maps onto one deep chain.** BTC/ETH have real strike-by-strike liquidity; alts don't, so the "stay 5-95 delta" liquidity rule collapses to "stay on BTC/ETH" for anything you need to exit cleanly.
- **Catalysts, not earnings.** The IV-inflate-then-crush pattern that punishes OTM buyers comes from FOMC/CPI, [[token-unlocks|unlocks]], ETF-decision dates, and upgrades — not quarterly earnings.
- **Deep-ITM = coin replacement without liquidation risk.** The embedded-put logic is the same as equities, but the practical appeal in crypto is that a deep-ITM long call gives leverage that *cannot be liquidated at a bad tick*, unlike the [[perpetual-futures|perp]] alternative.

## Getting the Data (CryptoDataAPI)

The IV surface and 25-delta risk reversal (the skew that drives moneyness/wing choice) come from [[deribit|Deribit]] / [[greeks-live|Greeks.live]]. [[cryptodataapi|CryptoDataAPI]] supplies the funding and options-positioning context that tells you which wing the leveraged crowd has overbid.

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding, the crypto skew driver (which wing is rich?)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (positioning by strike)
- `GET /api/v1/volatility/regime` — per-asset vol regime for the ATM level

**Historical data:**
- `GET /api/v1/backtesting/funding` — historical funding to study how skew tracked positioning
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; funding detail on [[cryptodataapi]].

## Related

- [[deribit]] — the venue whose chain moneyness maps onto
- [[risk-reversal]] / [[funding-rate]] — the perp-driven skew that shapes wing selection
- [[crypto-options-volatility-selling]] — trades the overbid wing the skew reveals
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
- [[iv-crush]] — why OTM premium evaporates after a catalyst
- [[volatility-risk-premium]] — structural reason OTM buyers lose on average
- [[probability-of-profit]] — moneyness expressed as a probability
- [[long-call]], [[long-put]], [[credit-spread]], [[debit-spread]], [[iron-condors]] — strategies with canonical moneyness choices
- [[leaps]] — deep-ITM moneyness is the standard for stock replacement

## Sources

- Sheldon Natenberg, *Option Volatility and Pricing* — Greek behaviour across moneyness, the volatility smile/skew
- John C. Hull, *Options, Futures, and Other Derivatives* — delta as the option's probability proxy, put-call parity and synthetics
- Lawrence McMillan, *Options as a Strategic Investment* — moneyness choices for directional and income structures
- CBOE Options Institute — strike-selection and moneyness educational materials
- [[deribit]] / [[greeks-live]] — crypto IV surface, DVOL, and the funding-driven 25-delta risk reversal (crypto's dynamic skew)
- General market knowledge; no specific wiki source ingested yet.
