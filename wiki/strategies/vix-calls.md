---
title: "Crypto Long-Vol Overlay (DVOL / Deribit)"
type: strategy
created: 2026-04-15
updated: 2026-07-19
status: review
tags: [options, derivatives, volatility, risk-management, crypto, dvol, hedging]
aliases: ["Crypto Long-Vol Overlay", "DVOL Long Vol", "Deribit Straddle Hedge", "VIX Calls", "Crypto Volatility Hedge", "BTC Put Wings"]
strategy_type: technical
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: naive-backtested
related: ["[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[long-volatility-strategies]]", "[[tail-risk-hedging]]", "[[tail-hedging]]", "[[protective-puts]]", "[[crypto-options-volatility-selling]]", "[[variance-risk-premium]]", "[[realized-volatility]]", "[[implied-volatility]]", "[[funding-rate]]", "[[gamma-exposure]]", "[[risk-reversal]]", "[[volatility-regime]]", "[[liquidation-cascade-fade]]", "[[risk-management]]"]

# Edge characterization
edge_source: [risk-bearing, behavioral]
edge_mechanism: "The overlay pays the variance risk premium to vol sellers in exchange for convex crash protection; the behavioral angle is that in positive-funding regimes the crowd ignores downside protection, making OTM put wings temporarily cheap relative to their cascade payoff. Edge is not positive standalone expectancy but portfolio-level convexity and survivorship during liquidation cascades."

# Data and infrastructure requirements
data_required: [options-chain, funding-rates, volatility-regime, open-interest]
min_capital_usd: 10000
capacity_usd: 100000000
crowding_risk: low

# Performance expectations
expected_sharpe: -0.4
expected_max_drawdown: 0.02
breakeven_cost_bps: 60

# Kill criteria
kill_criteria: |
  - DVOL structurally above 80th percentile for > 21 days → suspend new tranches (too expensive)
  - monetization missed through DVOL spike → process failure; fix rules before next tranche
  - annual bleed exceeds 2.5% of NAV → reduce tranche size or shift to put spreads
  - Deribit access restriction (regulatory/operational) → halt program pending venue alternative
---

# Crypto Long-Vol Overlay (DVOL / Deribit)

A crypto long-vol overlay buys **convexity on [[bitcoin|BTC]]/[[ethereum|ETH]] volatility** — long OTM put "wings" and long straddles/strangles on [[deribit]] — used primarily as a tail-risk hedge to protect a crypto book against sharp declines and volatility spikes. Because [[dvol|DVOL]] (Deribit's 30-day implied-vol index, the "crypto VIX") spikes violently when crypto sells off — it has jumped from the 50s into the 100s+ during cascades — owning long-vol structures provides convex, leveraged exposure to volatility increases that offset spot losses. Like the equity VIX-call hedge it is modelled on, it is **expensive to hold continuously**: crypto vol mean-reverts hard, option theta bleeds daily, and standalone the overlay has **negative expected value** — it only makes sense as a portfolio overlay funded by carry elsewhere.

## Edge source

The overlay captures a **risk-bearing** edge with a secondary **behavioral** component.

- **Risk-bearing (insurance buyer)**: vol sellers on Deribit (strangle sellers, on-chain vault sellers) are structurally short convexity; the overlay is the counterparty buying that convexity. The expected value is negative (the insurance premium), but the portfolio-level payoff — cash delivered during a cascade when leveraged books are force-liquidated — makes it net-positive for a hedged book. See [[variance-risk-premium]] and [[crypto-options-volatility-selling]].
- **Behavioral cheapness**: In positive-funding/call-skew regimes, the leveraged crowd is entirely focused on upside; downside puts are relatively unloved and can be bought at a discount to their realized crash value. This cheapness is not permanent — it normalizes after a cascade — but it makes the best overlay entries genuinely cheap relative to intrinsic hedge value.
- **No clean VIX-future equivalent**: the DVOL index (Deribit's 30-day IV composite) is a reference index only — there is no listed DVOL future or DVOL call to buy. Long-vol exposure is achieved entirely through spot-option structures (put wings, straddles) with their own delta, gamma, and theta. This is a structural limitation vs. the equity VIX-call world.

## Null hypothesis

A systematic long-vol overlay program run without entry discipline or monetization has **negative expected return by construction**: the overlay donor pays the [[variance-risk-premium]] to Deribit vol sellers. Under the null, the overlay costs 1–3% of NAV per year and the payoffs (while convex) do not recoup the bleed over a cycle unless (a) structures are bought when DVOL is genuinely cheap (low-percentile, call-skew regime), and (b) cascade payoffs are *sold quickly* into DVOL spikes rather than held to mean-reversion. A program that fails either discipline should expect pure insurance drag with no convexity benefit.

## No clean "VIX call" analog in crypto

The equity version of this hedge buys **VIX calls** — call options on a *tradeable volatility future*. **Crypto has no VIX call, because it has no tradeable vol index or vol future.** [[dvol|DVOL]] is a published reference index only. There is nothing to buy that pays off directly on "DVOL going up." The honest crypto substitutes for "a call on vol" are spot-option structures that are *net long vega and gamma*:

| Equity instrument | Crypto substitute | What it captures | Caveat |
|---|---|---|---|
| VIX call (long a vol future call) | Long ATM/OTM **straddle** on Deribit | Long vega + gamma; pays on a DVOL spike either direction | Decays via theta; no vol-future leverage |
| VIX call (crash hedge) | Long **OTM BTC/ETH put wing** | Directional-down convexity; DVOL spikes usually accompany crashes | Misses a *melt-up* vol spike a straddle would catch |
| VIX call spread | Deribit **put spread / ratio backspread** | Capped-cost convexity | Path-dependent payoff |

Because crypto DVOL spikes most violently on *down* moves, a **long OTM put wing** captures most of the crash-hedge value a VIX call would — but a **long straddle** is the truer "pays on any vol spike" analog. Neither is a call on a vol future; both are spot-option structures with their own theta and delta. Everywhere below, "long-vol" = this basket, not a VIX call.

## Overview

DVOL measures the 30-day expected volatility of BTC/ETH from the full [[deribit]] options surface. It is the crypto "fear gauge," though — unlike the VIX — a DVOL spike is not always fear: crypto rallies can be as violent as sell-offs, so DVOL can spike on melt-up gamma too. Historically BTC DVOL has ranged from the high-20s (deep calm) to 130+ during shocks (2020-03-12, LUNA, FTX, 2025-10-10).

Deribit options are European-style and **cash-settled to the Deribit index**. Critically, they can be **coin-margined (inverse)** or **USDC-margined (linear)**; a long-vol overlay intended as clean USD protection should use linear options, because inverse options pay out in a collateral currency that is itself crashing. There is no VIX-futures-style term-structure contract, but the Deribit surface still shows a **vol term structure** (front- vs back-month implied vol) you can read for contango/backwardation.

Despite the cost, long-vol overlays remain one of the most effective crypto tail hedges available. A small allocation can produce outsized returns during a cascade, offsetting a significant share of spot/perp losses. The key challenge is sizing and timing to avoid excessive premium bleed during calm 24/7 markets.

## Why long-vol is expensive in crypto

Several structural factors make the overlay persistently costly — analogous to the equity headwinds, but re-based on crypto mechanics:

1. **Mean reversion of DVOL.** Like the VIX, DVOL is strongly mean-reverting: a spike from 55 to 110 almost always reverts toward baseline within days. This limits the window in which long-vol structures are in the money and makes it hard to capture the full value of a spike.
2. **Vol-of-vol premium.** The market charges a premium for options on volatile underlyings; crypto vol-of-vol is high, so straddles/wings tend to be expensive relative to realized movement.
3. **Wide bid-ask on the wings.** Deribit OTM wing spreads run 3–8 vol points round-trip — far wider than SPX/VIX options — a real, recurring drag on cheap options.
4. **Theta / roll cost.** Maintaining a continuous hedge means rolling across weekly/monthly Deribit expiries; each roll resets the theta clock and pays the spread. This is the crypto analogue of VIX roll cost — but it is *option theta*, not VIX-futures roll yield (there is no vol future to roll).
5. **No §1256 shelter.** Unlike SPX/VIX options, offshore Deribit contracts get no 60/40 blended tax treatment, worsening after-tax economics.

## Portfolio-level rationale

Standalone, systematic long-vol buying is a slow donation of the [[variance-risk-premium|variance risk premium]] to crypto vol sellers ([[crypto-options-volatility-selling]]) — negative carry of a few percent of NAV per year. The overlay only beats that null if (1) spikes are actually *sold* near the highs rather than held to mean-reversion, and (2) proceeds are redeployed into depressed coins during the cascade. The value is **state-contingent liquidity**: cash delivered exactly when leveraged crypto books are being auto-liquidated, when a marginal dollar is most valuable. A hedger who cannot demonstrate both behaviours should expect pure negative carry.

## Rules

### When to buy (entry)

Long-vol structures are most cost-effective when:

- **DVOL is in the low part of its trailing-year percentile** (deep calm): premium is cheapest, and the next spike statistically starts from a compressed base.
- **Funding is richly positive / call-skew regime:** when [[funding-rate|perp funding]] is deeply positive and 25-delta [[risk-reversal|risk reversal]] shows call skew, downside **puts are relatively cheap** — the ideal moment to buy put wings the crowd is ignoring in favour of upside calls.
- **Vol term structure is in steep contango:** front-month implied vol well below back-month signals complacency.
- **Ahead of known catalysts:** ETF decisions, major token unlocks, macro prints (CPI/FOMC), halving windows — binary events that can trigger vol spikes.

Avoid initiating when:

- **DVOL is already elevated (upper percentile / backwardation):** you are buying the peak just before mean reversion.
- **Realized vol already exceeds implied for weeks** (regime break like LUNA/FTX): the premium has inverted and the hedge is expensive.

### Entry decision table

| DVOL percentile (1y) | Skew / funding | Term structure | Action | Rationale |
|---|---|---|---|---|
| Low (<40th) | Call-skew (positive funding) | Steep contango | **Buy put wings (best entry)** | Cheap premium, max convexity, downside unloved |
| Low–mid (40–60th) | Balanced | Mild contango | Buy straddle tranche | Acceptable; size to budget |
| Mid–high (60–85th) | Put-skew (post-selloff) | Flat | Reduce / wait | Premium rich, less mean-reversion edge |
| High (>85th) | Put-skew, funding negative | Backwardation | **Do not initiate** | Buying the peak just before reversion |
| Any | — | Backwardation >3–4 weeks | Suspend program | Systematic buying is chasing a regime break |

### Contract selection and mechanics

1. **Structure:** long OTM put wing for crash-hedge convexity, or long straddle/strangle for direction-agnostic vol-spike exposure. Prefer **USDC-margined (linear)** for clean USD payoff.
2. **Expiry:** 21–60 DTE. Shorter = more gamma (reacts faster) but faster decay; longer = more vega but costlier. Avoid weeklies for a *continuous* hedge (theta too hot).
3. **Strike:** 15–30% OTM puts for the wing (max leverage, needs a real move); ATM/near-ATM for a straddle (profits from smaller spikes at higher cost).
4. **Buy the structure:** pay the premium upfront — this is the maximum loss on the hedge leg.

### Exit / monetization

5. **Monetize fast into a DVOL spike.** Crypto vol reverts within days — do not wait. A practical rule: scale out in thirds at 3×, 5×, and 8× cost.
6. **Let calm-market structures expire** and roll to the next cycle.
7. **Roll periodically** across staggered expiries to maintain continuous protection without a hedge gap.
8. **Redeploy gains** into cheap BTC/ETH during the cascade — the rebalancing step that makes the overlay worth its bleed.

### Position sizing

Allocate a fixed **small % of NAV per year** to the overlay (fund it from short-vol carry where possible). Deploy in tranches rather than all at once, and never exceed the annual budget chasing a spike already underway.

## Implementation pseudocode

```python
# Rolling crypto long-vol overlay on Deribit BTC/ETH
ANNUAL_BUDGET = 0.02 * NAV          # small % of NAV per year
TRANCHE       = ANNUAL_BUDGET / 4

def roll_cycle(dvol_pctl, funding_8h, term_structure):
    if term_structure.is_backwardated() or dvol_pctl > 0.85:
        hold_stablecoin(TRANCHE)                 # don't buy the peak
        return
    expiry = pick_expiry(days_out=45)            # 21-60 DTE
    if funding_8h > 0.0003:                       # call-skew: buy cheap downside
        buy_otm_put_wing(underlying="BTC", otm=0.25, expiry=expiry, spend=TRANCHE)
    else:                                         # direction-agnostic spike hedge
        buy_straddle(underlying="BTC", expiry=expiry, spend=TRANCHE)

def monitor(pos):
    m = pos.mark / pos.cost
    if m >= 3: sell_fraction(pos, 1/3)           # scale out fast; DVOL mean-reverts
    if m >= 5: sell_fraction(pos, 1/2)
    if m >= 8: sell_all(pos)
    if pos.days_to_expiry <= 3 and m < 1:
        let_expire(pos)                           # bleed is the insurance cost
    redeploy_gains_into_coins()                   # the rebalance that makes it work
```

## Payoff & Greeks

### Net-Greeks table (long straddle / long put wing, low-DVOL entry)

| Greek | Sign | Trading meaning |
|---|---|---|
| Delta | put wing: − ; straddle: ~0 | Put wing gains as spot falls; straddle is direction-neutral until a leg dominates |
| Gamma | + | Convexity engine — delta ramps into a cascade; the source of the multi-× payoff |
| Vega (long DVOL) | + | Gains as implied vol / DVOL rises, even before a large spot move |
| Theta | − | The persistent daily bleed; the reason base-case P/L is negative every calm week |
| Vol-of-vol | + | The structure is long the volatility of DVOL itself |

Net exposure: **long convexity (long gamma + long vega), short theta** — the mirror image of the [[crypto-options-volatility-selling|Deribit vol seller]], who is short gamma/vega and long theta. Unlike a VIX call, the x-axis is BTC/ETH *spot* (via the option), not a vol future — so a put wing looks "further OTM" in spot terms but captures the DVOL spike that co-moves with a crash.

## Indicators / data used

- **[[dvol|DVOL]] level and percentile** (BTC and ETH) — the primary entry gate (there is no VIX-futures curve; use DVOL percentile + front/back implied-vol spread from the surface).
- **[[funding-rate|Perp funding]] and 25-delta [[risk-reversal|risk reversal]]** — crypto skew driver; positive funding → cheap downside puts.
- **Deribit IV surface** (strikes, expiries, vol-of-vol) — strike/expiry selection via [[greeks-live]].
- **[[realized-volatility]] (10/21/30-day)** — DVOL − RV shows how richly the tail is priced.
- **Liquidation and [[gamma-exposure|dealer-gamma]] tape** — cascade fragility and monetization timing.
- **Event calendar** (ETF, unlocks, halving, CPI/FOMC) — catalyst-timed tranches.

## Example trade

A desk runs a $500,000 BTC book and budgets ~2% ($10,000)/year for a long-vol overlay. In a calm regime with BTC at $60,000, DVOL at 48 (low percentile), and funding richly positive (call-skew → cheap puts):

- **Buy:** a 45-DTE BTC 25%-OTM put wing (strike $45,000), USDC-margined, for ~$2,400.

**Scenario 1 — Market stays calm:** DVOL drifts 48 → 44, BTC chops $58–62K. The wing decays and expires worthless. Loss: ~$2,400. Roll a new tranche next cycle.

**Scenario 2 — Weekend cascade:** an exchange-solvency headline gaps BTC −25% to $45,000 over a Saturday; DVOL spikes 48 → 100. The put wing goes ITM and its vega/gamma explode — the structure marks up roughly 6–9×. Sell into the DVOL spike for ~$18,000, a ~7× return; the ~$15,600 gain offsets a large share of the book's spot loss and funds a rebalance into cheaper BTC.

**Scenario 3 — Flash cascade (2025-10-10 style):** BTC drops −12% in 60 seconds with ~$19B liquidated; DVOL briefly triples. The wing spikes even harder; if the desk monetizes quickly (crypto vol reverts within hours here), the payoff can exceed the book's realized loss on the move.

## Performance characteristics

- **Base case (most months):** the overlay loses 50–100% of its budget — a few-percent drag on book return; negative standalone expectancy.
- **Cascade months:** payoffs of several× deployed premium are realistic for OTM wings/straddles bought in low-DVOL regimes and sold into the spike (2020-03, LUNA, FTX, 2025-10-10). Poorly timed monetization can halve this because crypto spikes retrace within days — or hours.
- **Cost overlay:** Deribit wing bid-ask (3–8 vol points round-trip) plus a taker fee capped at 12.5% of premium plus frequent rolls consume a meaningful share of the annual budget — heavier than the VIX-call version's friction. The convex payoff still survives wide spreads that would kill a fine-edged strategy.
- **Portfolio level:** small allocations meaningfully cut book drawdown *across a cascade window* while long melt-ups see the hedged book lag the unhedged one by roughly the bleed. Judging it on calm-regime carry alone is the central analytical error — it is a portfolio component, not a standalone strategy.

## Crypto specifics

- **No VIX call / vol future** — long-vol is spot-option structures (put wings, straddles), not a call on a vol index.
- **24/7 + weekend gaps** — the biggest DVOL spikes hit in thin weekend liquidity with no close; the hedge must be pre-positioned.
- **DVOL spikes ≠ only fear** — melt-up gamma also spikes DVOL, so a straddle (not just a put wing) may be the right structure when the risk is a violent rally.
- **Inverse (coin-margined) settlement** — coin-collateralised long-vol pays in a crashing currency; use USDC-margined (linear) options for clean USD protection.
- **Perp-funding skew** — positive-funding euphoria makes downside puts cheap; the overlay's best entries are exactly when the leveraged crowd is paying up for calls.
- **Single-venue counterparty tail** — Deribit is effectively the only deep options venue; an outage/insolvency during a cascade is un-hedgeable, and Deribit puts do not hedge Deribit's own solvency (an FTX-type exchange-failure needs a spot-put or exchange-token short).
- **On-chain / depeg tail** — stablecoin depegs and DeFi exploits spike DVOL through a counterparty/protocol mechanism, not a price move; long-vol captures the vol spike but not the specific credit event.
- **No §1256 shelter** — after-tax payoff is worse than the SPX/VIX version's.

## What kills this strategy

- **Monetization failure:** holding through the spike. Crypto vol mean-reverts within days (sometimes hours); a hedger who waits watches an 8× mark round-trip to zero — the single most common failure mode.
- **Buying high:** initiating or up-sizing after DVOL has already exploded (backwardation), locking in expensive protection right before reversion.
- **Budget creep:** letting the bleed exceed a few % of NAV/year, which compounds into more damage than the drawdowns it insures.
- **Slow grinding alt bleed:** a multi-month −25% drift where each put expires worthless before the strike is hit — the crypto analogue of a slow bear the wing never catches.
- **Structural change:** compression of the crypto vol premium as covered-call ETFs and on-chain vaults scale, flattening the priced-in spike premium.
- **Inverse-settlement wrong-way risk** and **Deribit single-venue failure** — crypto-specific.

## Capacity limits

The overlay is wing-buying so its constraint is **Deribit put-wing liquidity**, not capital.

- **Single-strike deep-OTM (20–40% OTM) BTC put**: clean fills to ~$500K–$1M notional per strike per expiry; above that the market widens against you. A $10M notional hedge needs to be laddered across 3–5 strikes.
- **Full straddle on BTC/ETH**: ATM options are more liquid; $1–5M notional per tenor is achievable without significant slippage. Beyond $5M, use RFQ or split across tenors.
- **Total overlay book for a retail/small-fund operator**: $1–5M notional per cycle. For a $20–50M hedge fund: $5–20M notional, using a ladder of strikes and tenors. Institutional ($200M+): the wing capacity becomes the binding constraint; spread and OTC structures required.
- **Crowding risk**: low — there is no systematic over-crowding on the buy side of crypto put wings; structural sellers dominate, making this a buyer's market most of the time.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- DVOL above 80th percentile of trailing-1y range for > 21 calendar days → suspend new tranches; at that cost level the annualized bleed is unsustainable and mean reversion risk dominates.
- Any cascade payoff not partially monetized within 72 hours of the DVOL spike peak → process failure; address the execution/decision rule before deploying the next tranche.
- Rolling 12-month bleed exceeds 2.5% of NAV → reduce tranche size by 50% or shift from put wings to put spreads (cap the upside payoff in exchange for lower premium).
- Deribit access suspended due to regulatory action or operational outage → halt program until an alternative venue (e.g., CME micro futures, OTC dealer puts) is evaluated; do not shift to an untested venue under pressure.
- DVOL term structure in sustained backwardation (3-month > 1-month) for > 30 days → suspend and reassess — this signals a structural vol regime where new additions are expensive and the spike-reversion thesis is less reliable.

## Advantages

- **Convex payoff:** small cost in calm markets, potentially large returns during cascades that recur *annually* in crypto.
- **Negative correlation with the book when it matters** — pays exactly when perp longs are being liquidated.
- **Defined risk:** maximum loss is the premium paid.
- **Favourable entry windows:** positive-funding euphoria makes downside protection cheap.
- **Portfolio-level hedge:** one BTC/ETH overlay can hedge a diversified majors book.
- **Cleaner than the ETP world:** no VXX-style roll-decay or ETP path-dependence — you hold exactly the options you chose.

## Disadvantages

- **Persistent cost:** most of the time the structures expire worthless — steady negative standalone carry; Deribit spreads make the bleed heavier than VIX calls.
- **No vol-future instrument:** you cannot isolate "long vol" cleanly; every structure carries delta and theta baggage.
- **Mean reversion:** crypto vol spikes are short-lived; slow to act and the opportunity passes.
- **Inverse-settlement and single-venue** hazards with no equity equivalent.
- **Complexity:** requires managing the Deribit surface, skew, funding, and coin-vs-linear margin.
- **No §1256 tax shelter.**

## Getting the Data (CryptoDataAPI)

[[dvol|DVOL]], the vol term structure, and the tradeable IV surface come from **[[deribit|Deribit]]** / [[greeks-live|Greeks.live]] — CryptoDataAPI does **not** serve DVOL or the option chain. [[cryptodataapi|CryptoDataAPI]] supplies the complementary volatility-regime, options-flow, dealer-gamma, and funding context used to time and size the overlay.

**Live:**
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0–100)
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, [[max-pain]]
- `GET /api/v1/quant/gex` — dealer [[gamma-exposure|Gamma Exposure]]
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (skew driver)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (monetization timing)

**Historical:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime + 60-day history
- `GET /api/v1/backtesting/klines` — OHLCV archive for realized-vol computation (DVOL − RV)

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

For DVOL levels/history and the full IV surface, use the Deribit API (`/api/v2/public/get_volatility_index_data`) or [[greeks-live]]. Full catalog: [[cryptodataapi-market-intelligence]] and [[cryptodataapi-regimes]].

## Sources

- [[deribit]] / [[greeks-live]] documentation — DVOL construction, IV surface, coin-margined vs USDC-margined (linear) settlement.
- Alexander & Imeraj, and Deribit Insights research on DVOL and the crypto variance risk premium.
- Equity origins (for the convex-hedge logic that ports): CBOE VIX white paper; Szado (2009) on VIX hedging in the 2008 crisis; the CBOE VXTH systematic VIX-call overlay — cited as the *methodological ancestor*, not a crypto-tradeable instrument.
- Crypto tail record: 2020-03-12 ([[covid-crash]]), 2022-05 [[terra-luna-collapse|LUNA]], 2022-11 [[ftx-collapse|FTX]], 2025-10-10 ([[2025-10-crypto-liquidation-cascade|liquidation cascade]]).

## Related

- [[dvol]] — the crypto vol benchmark this overlay is long
- [[deribit]], [[greeks-live]] — venue and IV-surface workbench
- [[long-volatility-strategies]] — the broader long-vol family
- [[tail-risk-hedging]], [[tail-hedging]] — the portfolio-insurance disciplines this implements
- [[protective-puts]] — the put-wing expression
- [[crypto-options-volatility-selling]] — the short-vol counterparty the overlay pays
- [[variance-risk-premium]] — the premium the hedger pays
- [[funding-rate]], [[risk-reversal]] — the crypto skew drivers
- [[realized-volatility]], [[implied-volatility]] — the vol inputs
- [[gamma-exposure]] — dealer-gamma / cascade-fragility context
- [[volatility-regime]] — regime detection for entry timing
- [[liquidation-cascade-fade]] — the cascade dynamic behind DVOL spikes
- [[risk-management]] — portfolio-protection framework
