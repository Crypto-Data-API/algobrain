---
title: "Options Selection Framework"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, risk-management, position-sizing, methodology]
aliases: ["How to Pick Options", "Options Selection Methodology", "Options Filter Funnel", "Strike Picking Process"]
domain: [options, risk-management]
prerequisites: ["[[options]]", "[[delta]]", "[[implied-volatility]]", "[[iv-rank-and-iv-percentile]]"]
difficulty: intermediate
related:
  - "[[options-liquidity-screening]]"
  - "[[strike-selection]]"
  - "[[expiration-selection]]"
  - "[[moneyness-selection]]"
  - "[[iv-rank-and-iv-percentile]]"
  - "[[spread-width-selection]]"
  - "[[delta]]"
  - "[[theta]]"
  - "[[gamma]]"
  - "[[vega]]"
  - "[[probability-of-profit]]"
  - "[[credit-spread]]"
  - "[[long-call]]"
  - "[[covered-calls]]"
  - "[[cash-secured-puts]]"
  - "[[iron-condors]]"
  - "[[debit-spread]]"
  - "[[leaps]]"
  - "[[skew]]"
  - "[[vix-calls]]"
  - "[[options-position-management]]"
---

The **Options Selection Framework** is a five-filter funnel that walks the trader from the universe of all listed contracts down to a single tradeable structure. Every option chain on a liquid name like SPY exposes thousands of strike-by-expiration combinations; the job of the framework is to systematically discard the unsuitable ones before the trader ever looks at price. Skipping the funnel — picking a strike "by gut" because the premium looks juicy — is the single most common failure mode for retail options traders.

## The 5-Filter Funnel

The funnel is ordered: each filter removes contracts so the next filter operates on a smaller, cleaner set. Reordering wastes time and can hide problems (e.g., a 16-delta strike that looks attractive on paper but is functionally untradeable because of bid-ask).

| # | Filter | Question it answers | Primary metric | Detail page |
|---|---|---|---|---|
| 1 | Liquidity | Can I get in and out at fair prices? | Bid-ask, OI, volume | [[options-liquidity-screening]] |
| 2 | IV regime | Should I be a buyer or a seller of premium? | [[iv-rank-and-iv-percentile\|IV rank]] | [[iv-rank-and-iv-percentile]] |
| 3 | Expiration / DTE | How long for the thesis to play out? | DTE, [[theta]] curve | [[expiration-selection]] |
| 4 | Moneyness | ATM, OTM, or ITM? | [[delta]], standard deviations | [[moneyness-selection]] |
| 5 | Strike-by-Greeks | Exactly which strike? | [[delta]] then [[theta]]/[[gamma]]/[[vega]] | [[strike-selection]] |

Each filter is a hard gate: a contract that fails any one is discarded before the next is considered.

### 1. Liquidity Screen

Before anything else, drop contracts that cannot be entered and exited at fair prices. See [[options-liquidity-screening]] for full thresholds. Quick filter:

- **Bid-ask spread** ≤ $0.05 on penny-pilot tickers (SPY, QQQ, AAPL, TSLA), ≤ $0.10 on most large-caps, ≤ 5% of mid-price as a universal cap.
- **Open interest** ≥ 1,000 for entry; ≥ 500 to plan a clean exit.
- **Volume** ≥ 100 on the contract that day, or ≥ 50 daily average for the strike over the past 5 sessions.
- **Underlying** must have an active options market, not just a listed one — many small-caps technically have option chains that almost never trade.

If a strike fails liquidity, the rest of the funnel is moot: a 70%-PoP credit spread on an illiquid contract loses more to slippage than it ever earns in theta.

### 2. IV Regime Check

Before choosing direction or structure, check the volatility environment using [[iv-rank-and-iv-percentile|IV rank]] (IVR) on the underlying:

- **IVR > 50** → premium-selling environment. Favor [[credit-spread|credit spreads]], [[iron-condors]], [[covered-calls]], [[cash-secured-puts]]. Theta and vega both work *for* the seller.
- **IVR 20-50** → neutral. Either side works; emphasize directional conviction and structure efficiency.
- **IVR < 20** → premium-buying environment. Favor long calls/puts, debit spreads, calendars, diagonals. Vega and gamma both work *for* the buyer if the move materializes.

This is the "[[tom-sosnoff|Sosnoff]] / [[tastytrade]] check" — match the structure to the regime before choosing strikes. Selling 16-delta puts at IVR 8 is the same structure as at IVR 80, but the expected value is dramatically different because the credit collected is half as large.

### 3. Expiration / DTE Selection

See [[expiration-selection]] for the full mechanics. Quick map:

- **Credit spreads, iron condors, short strangles**: 30-45 DTE — sweet spot of theta-curve acceleration, manageable gamma, deep enough to roll if needed.
- **Long premium (long calls, long puts, debit spreads)**: 60-90 DTE — gives the thesis time to play out, minimizes daily theta bleed.
- **Weekly income**: 7-14 DTE — extreme theta but extreme gamma; only on the highest-liquidity names (SPX, SPY, QQQ).
- **0DTE**: intraday only, used as gamma scalps, hedges, or lottery tickets — never as an income stream for sub-$1M accounts.
- **LEAPS** (12+ months): for stock replacement (deep ITM long calls) or long-dated thesis trades.

### 4. Moneyness Selection

See [[moneyness-selection]] for full coverage. The choice between ATM, OTM, and ITM is a function of strategy:

- **Short premium**: OTM by 1-2 standard deviations (~16-30 delta). ATM short straddles only when explicitly targeting earnings IV crush.
- **Long premium directional**: ATM (~50 delta) for balanced gamma/vega exposure; slightly ITM (~70 delta) when conviction is high; OTM (~30 delta or less) only for lottery-ticket sizing.
- **Stock replacement**: deep ITM (~80 delta) so the option behaves nearly like the underlying, with [[leaps|LEAPS]] expirations.
- **Income overwrites (covered calls)**: 20-30 delta OTM — collect premium without high assignment probability.

### 5. Strike-by-Greeks

The final filter is the precise strike pick using [[delta]] as the dominant input. See [[strike-selection]] for the full table. Common conventions:

- **16 delta** ≈ 1 standard deviation OTM ≈ ~84% probability of expiring OTM ≈ ~68% PoP on a credit spread (after debit-cushion arithmetic) — the "tastytrade default" for short premium.
- **30 delta** — tighter, larger credit, lower PoP (~70% on the strike alone, ~60-65% PoP on a spread). Used when IVR is moderate and the trader wants meaningful credit.
- **50 delta** = ATM — used for ATM straddles, ATM debit spreads, gamma-scalping setups.
- **70 delta** ITM — used as the long leg in deep-ITM debit spreads or as stock replacement.

Once the strike is picked by delta, sanity-check theta (decay velocity), vega (IV exposure), and gamma (delta sensitivity) to confirm the trade has the Greeks profile the strategy demands.

#### Delta → probability reference

[[delta|Delta]] doubles as a rough probability that the option finishes ITM. The complement (1 − delta) approximates the probability of expiring OTM — the headline for short-premium sellers.

| Delta | ≈ SD from ATM | ≈ P(expire OTM) | Typical use |
|---|---|---|---|
| 50 | 0.0 (ATM) | ~50% | ATM straddles, ATM debit spreads, gamma scalps |
| 30 | ~0.5 SD | ~70% | Aggressive short premium, larger credit |
| 16 | ~1.0 SD | ~84% | "tastytrade default" short strike |
| 10 | ~1.3 SD | ~90% | Conservative wings, far-OTM hedges |
| 5 | ~1.6 SD | ~95% | Deep tail; often illiquid (see [[options-liquidity-screening]]) |
| 70-80 | ITM | ~25-30% OTM | Stock replacement / long leg of deep-ITM [[debit-spread\|debit spreads]] |

Caveat: delta-as-probability is a risk-neutral approximation under the option's own IV; it is not the real-world probability and it diverges under heavy [[skew]]. For a spread, the strike-level OTM probability is **not** the [[probability-of-profit]] — see the worked example below for the breakeven-win-rate arithmetic.

## Strategy-Driven Selection

The funnel is universal but the parameter values change by strategy. The table below summarizes the parameter choices for common structures; the three canonical examples that follow walk the funnel end-to-end.

| Strategy | IV regime | DTE | Moneyness | Strike (delta) |
|---|---|---|---|---|
| [[credit-spread\|Credit spread]] | IVR > 30 (ideally > 50) | 30-45 | OTM both legs | short 16-30Δ |
| [[iron-condors\|Iron condor]] | IVR > 50 | 30-45 | OTM both wings | 16Δ each side |
| [[long-call\|Long call]] (directional) | IVR < 30 | 60-90 | ATM / slightly ITM | 50-70Δ |
| [[covered-calls\|Covered call]] | any (adjust by IVR) | 30-45 | OTM | 20-30Δ |
| [[cash-secured-puts\|Cash-secured put]] | IVR > 30 | 30-45 | OTM | 16-30Δ |
| Stock replacement | any | 12+ months ([[leaps\|LEAPS]]) | deep ITM | ~80Δ |
| [[vix-calls\|VIX call]] tail hedge | low VIX (regime, not IVR) | 30-90 | OTM | 20-35 strike |

Three canonical examples:

### Credit Spreads (e.g., SPY put credit spread)

1. Liquidity: SPY weeklies/monthlies — always passes.
2. IV regime: only enter when IVR > 30; ideally > 50.
3. DTE: 30-45.
4. Moneyness: OTM both legs.
5. Strike: short leg at 16-30 delta; long leg 5-10 wide (see [[spread-width-selection]]).

### Long Call (directional bullish thesis)

1. Liquidity: penny-wide on the chosen strike.
2. IV regime: prefer IVR < 30 (don't pay up for vega).
3. DTE: 60-90.
4. Moneyness: ATM (50d) for balanced exposure; 70d if conviction is high and you want stock-like behavior with capped downside.
5. Strike: pick by delta first, then check that vega exposure is consistent with your IV view.

### Covered Call (yield overlay on long stock)

1. Liquidity: monthly on a name with active chain.
2. IV regime: don't gate — covered calls are always running. Just adjust strike by IVR (see below).
3. DTE: 30-45 (monthly).
4. Moneyness: OTM.
5. Strike: 20-30 delta in normal IVR; tighter (30-40 delta) when IVR is high and credit is fat; wider (10-15 delta) when IVR is low and you don't want to risk being called away.

## Common Selection Mistakes

The mistakes are predictable. The framework exists because every one of these failures has been documented thousands of times in retail-trader case studies.

### Chasing High Premium on Illiquid Options

A 25-delta put on a $40 small-cap might quote at $1.50 mid with a $1.30/$1.70 bid-ask. The "credit" is fictional — fills happen at $1.30 entry and $1.70 exit, eating $0.40 (27%) of the theoretical premium per round-trip. Filter 1 (liquidity) prevents this entirely.

### Ignoring IV Rank

Selling premium at IVR 5 looks identical mechanically to selling at IVR 80, but the risk-adjusted edge is gone. The trader collects half the credit for the same gamma exposure. Conversely, buying long premium at IVR 90 means paying for vega that almost certainly mean-reverts against you (IV crush). Filter 2 catches both.

### Picking Strikes by Gut

"This level looks like good support" is not a strike-selection method. Discretionary chart-based strike picks systematically deviate from delta-based picks in the worst direction (selecting closer-to-ATM strikes that *feel* like they "won't get hit," while collecting too little credit for the gamma assumed). Filter 5 (strike-by-Greeks) imposes statistical discipline.

### Mismatched DTE

A 7-DTE iron condor is structurally a different trade from a 45-DTE iron condor on the same strikes — the former is a gamma trade, the latter a theta trade. Traders who treat DTE as a free parameter ("I'll just go shorter for more theta") quickly discover they've taken a position they cannot manage. Filter 3 forces an explicit DTE choice.

### Skipping the Greek Sanity Check

Picking a 16-delta short put at 5 DTE on an earnings stock looks like a normal credit spread but has a gamma-to-theta ratio 10× a 45-DTE position on the same strike. Filter 5's "Greek sanity check" prevents this — short premium near earnings or near expiry without explicit awareness of gamma is a recipe for tail blowups.

### Pitfalls quick reference

| Mistake | Filter that catches it | Symptom |
|---|---|---|
| Chasing premium on illiquid strikes | 1 — [[options-liquidity-screening\|Liquidity]] | Fills far from mid; "credit" never realized |
| Ignoring [[iv-rank-and-iv-percentile\|IV rank]] | 2 — IV regime | Half the credit for the same [[gamma]] |
| Picking strikes by gut / "support" | 5 — [[strike-selection\|Strike-by-Greeks]] | Too little credit for the risk assumed |
| Mismatched DTE | 3 — [[expiration-selection\|DTE]] | Gamma trade managed as a theta trade |
| Skipping the Greek sanity check | 5 — Greek check | Hidden gamma blowup near earnings/expiry |

## Worked Example: 16-Delta SPY Put Credit Spread

Walk the funnel end-to-end on a real chain.

**Setup**: SPY at $510 on 2026-05-07. Looking for a bullish-to-neutral premium-selling trade. Account size $100K, risk budget 1% per trade ($1,000).

**Filter 1 — Liquidity**: SPY weeklies and monthlies are penny-wide with OI > 10K on most strikes. Pass.

**Filter 2 — IV regime**: SPY IVR = 42 (moderate). Premium-selling viable but not optimal. Proceed but accept smaller credit.

**Filter 3 — DTE**: target 30-45 DTE. The June 19 monthly is 43 DTE. Pick June 19.

**Filter 4 — Moneyness**: OTM both legs.

**Filter 5 — Strike-by-Greeks**: scan the put side for the 16-delta strike.

| Strike | Delta | Mid | Bid-Ask |
|---|---|---|---|
| 495 | -0.22 | $2.10 | $2.08/$2.12 |
| 490 | -0.16 | $1.45 | $1.43/$1.47 |
| 485 | -0.11 | $0.98 | $0.96/$1.00 |
| 480 | -0.08 | $0.70 | $0.68/$0.72 |

Short the **490 put** (16 delta). For the long leg, pick a width per [[spread-width-selection]] — 5-wide on SPY is the standard. Long the **485 put** for $0.98.

**Spread**: short 490p / long 485p, June 19 expiration.

- Credit: $1.45 − $0.98 = **$0.47** ($47/contract)
- Width: $5.00, max loss $5.00 − $0.47 = **$4.53** ($453/contract)
- R:R: 1 : 9.6 — ouch. Below the 1/3-of-width rule (would need credit ≥ $1.67).

**Verdict**: filter 5 reveals that the 16-delta strike at IVR 42 doesn't pay enough to clear the 1/3 rule. Two fixes:

1. **Move closer in**: short the 30-delta 495 put for $2.10. Spread credit: $2.10 − $1.45 = $0.65. Still below 1/3 of width. Move closer again.
2. **Skip the trade**: the framework correctly identified that this name/structure/regime combination doesn't have edge today. Wait for IVR > 50.

A trader without the funnel might still take the 16-delta trade at $0.47 because "70% PoP feels good" — and lose money over a year because the breakeven win-rate (1 / (1 + 9.6) = 9.4%... wait, no — breakeven win-rate = max-loss / (max-loss + max-profit) = 4.53 / 5.00 = **90.6%**) requires winning 90.6% of trades to break even. The model PoP is ~84%. The trade is structurally edge-negative even before costs.

This is exactly the failure mode the framework catches. The filters worked.

## When to Skip the Funnel

The funnel applies to *new* trade entries. It doesn't apply to:

- **Position management** (rolling, adjusting, closing) — different rule sets, see [[options-position-management]].
- **Hedges** chosen for portfolio-Greek reasons rather than expected value (e.g., a 5% OTM SPY put bought for tail protection regardless of IVR — see [[5-percent-otm-put-overlay]]).
- **Earnings binary plays** where the trader is explicitly buying gamma, not pricing a regime — though the IV-regime check still applies in reverse (IVR usually inflates pre-earnings).

## Related

- [[options-liquidity-screening]] — Filter 1 in detail
- [[iv-rank-and-iv-percentile]] — Filter 2 in detail
- [[expiration-selection]] — Filter 3 in detail
- [[moneyness-selection]] — Filter 4 in detail
- [[strike-selection]] — Filter 5 in detail
- [[spread-width-selection]] — pairs with strike selection for spreads
- [[delta]] — primary strike-selection metric
- [[theta]] — decay budget
- [[gamma]] — risk concentration metric
- [[probability-of-profit]] — the headline number every filter feeds into
- [[credit-spread]], [[iron-condors]], [[covered-calls]], [[cash-secured-puts]], [[long-call]] — strategy pages

## Sources

- tastytrade research archive — IV-rank-gated structure selection, 16-delta short-premium convention, 30-45 DTE entry studies
- Euan Sinclair, *Positional Option Trading* — systematic strike/expiration selection and cost-aware filtering
- Lawrence McMillan, *Options as a Strategic Investment* — strategy-to-regime matching
- CBOE Options Institute — probability-of-profit and delta-as-probability educational materials
