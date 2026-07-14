---
title: "Skew Trading (Crypto Options)"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [options, quantitative, volatility, crypto, derivatives, deribit, vol-trading]
aliases: ["Crypto Skew Trading", "Risk Reversal Trading", "Deribit Skew", "Volatility Skew Harvest", "RR25 Trading"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested

# Edge characterization
edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "Tail-hedgers and FOMO call buyers overpay for the rich wing of the BTC/ETH surface (downside puts in stress, upside calls in euphoria); the skew trader sells that rich convexity delta-hedged and is paid the variance/skew risk premium for warehousing gamma and vega the crowd refuses to hold."

# Data and infrastructure requirements
data_required: [options-chain, implied-vol-surface, deribit-dvol, perp-price, funding-rates, realized-vol]
min_capital_usd: 25000
capacity_usd: 40000000
crowding_risk: medium

# Performance expectations (net of Deribit fees + delta-hedge friction)
expected_sharpe: 0.8
expected_max_drawdown: 0.35
breakeven_cost_bps: 40

# Decay history
decay_evidence: "Crypto 25-delta risk reversal has compressed and normalised as the Deribit options market matured (BTC options OI grew from <$1B in 2020 to >$30B by 2025) and institutional flow arrived via US spot-ETF option listings (2024). The BTC variance risk premium — implied minus realised vol — narrowed from ~15-20 vol points in 2020-2021 to ~4-10 points in 2024-2025, and the persistent bull-market CALL skew of 2020-2021 has flattened as two-sided institutional hedging replaced pure retail call-buying."

# Lifecycle
kill_criteria: |
  - rolling 60-day realised vol exceeds sold implied vol by more than the collected premium (VRP inverted)
  - net short-vega book loses > 25% peak-to-trough
  - Deribit DVOL gaps > 40% intraday while the book is net short wing (crash/melt-up regime)
  - 25-delta RR sits inside +/-1 historical std for > 30 days (no dislocation to fade)

related: ["[[implied-volatility]]", "[[volatility-skew]]", "[[volatility-smile]]", "[[volatility-surface]]", "[[risk-reversal]]", "[[skew]]", "[[cboe-skew-index]]", "[[variance-risk-premium]]", "[[volatility-risk-premium]]", "[[options-greeks]]", "[[vega]]", "[[gamma]]", "[[delta-hedging]]", "[[gamma-scalping]]", "[[straddle]]", "[[strangle]]", "[[crypto-options-volatility-selling]]", "[[crypto-options-dispersion]]", "[[volatility-carry]]", "[[deribit]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[garch-volatility]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Skew Trading (Crypto Options)

Skew trading harvests the **implied-volatility skew** of crypto options — the difference in [[implied-volatility]] between out-of-the-money puts and calls on the same expiry, almost always traded on [[deribit|Deribit]] (which clears ~85-90% of global BTC/ETH options volume). The trader **sells the rich wing and buys the cheap wing** as a delta-hedged [[risk-reversal|risk reversal]], collecting the variance/skew risk premium when the skew mean-reverts or when realised outcomes prove the wing was overpriced. Unlike equity indices, crypto skew is *regime-dependent and sign-unstable*: BTC/ETH often carried **positive** 25-delta risk reversals (call-over-put, upside FOMO) in the 2020-2021 bull, then flipped to equity-style **negative** (put-over-call) skew during 2022 stress and post-ETF institutional hedging. That sign instability is both the opportunity and the trap.

## Edge source

Mapping to the six categories in [[edge-taxonomy]], crypto skew trading is a three-way hybrid:

- **Behavioural (primary).** Crypto option demand is lopsided and emotional. In euphoric regimes, retail chases upside via cheap OTM calls (right-tail FOMO), bidding call IV above put IV — the opposite of equities. In stress regimes, funds and treasuries buy downside crash protection, bidding put IV up. Either way, one wing is bid by non-price-sensitive hedgers/speculators and the skew trader sells it. This is the [[variance-risk-premium|variance risk premium]] expressed on the *wings* rather than at the money.
- **Structural.** Deribit dealers must hedge their books. Persistent one-directional wing demand forces dealers to carry inventory they lay off through the skew, and the marginal liquidity provider is compensated with a spread — the skew premium is partly a market-maker inventory rent that a patient seller can share.
- **Risk-bearing.** Selling the rich wing means being **short convexity into the exact move the buyer feared**. You are paid to warehouse gamma and vega that the crowd will not hold. This is a genuine risk premium, not a free lunch: the premium is the price of bearing the crash (or melt-up) the wing insures against. Zero or negative realised skew premium in a tail event is the cost of the trade, not a malfunction.

The strategy does **not** rely on informational or latency edge. Deribit's surface, DVOL index, and 25-delta RR are public. The edge is having the balance-sheet and hedging discipline to be short the rich wing at size and survive the tail.

## Why this edge exists

Three durable biases keep paying the skew seller:

1. **Asymmetric option demand.** Crypto has no natural two-sided hedger base the way equities have (pension funds long stock buying puts, corporates selling calls). Instead demand clusters: retail buys upside convexity in bulls, structured-product desks and miners/treasuries buy downside in bears. The wing that is being *bought* is systematically rich relative to its realised payoff.
2. **Realised vol undershoots implied on average.** BTC/ETH implied vol embeds a premium over subsequent realised vol in most regimes (the crypto [[variance-risk-premium|VRP]]). Because the wings carry the most vega convexity, the premium is concentrated there. He et al. and multiple Deribit-data studies document BTC implied-minus-realised spreads averaging positive over multi-year windows.
3. **Coin-margined settlement frictions.** Deribit BTC/ETH options are inverse (coin-settled unless USDC-margined linear), so option payoff and collateral value are correlated with the underlying. This embeds a subtle, persistent mispricing between naive Black-Scholes skew and the true coin-denominated payoff that sophisticated sellers can capture, and that keeps casual traders from arbitraging the skew away cleanly.

## Null hypothesis

Under a no-edge world, the implied-vol surface is an unbiased forecast of the risk-neutral distribution and the 25-delta risk reversal is fair compensation for realised wing risk. In that world:

- The realised payoff of a delta-hedged short-rich-wing / long-cheap-wing risk reversal would average zero net of fees.
- The 25-delta RR would be a random walk with no mean-reversion — extreme readings would not predict subsequent normalisation.
- Realised vol would match the skew-implied conditional vol of each wing; selling the rich wing would earn nothing after hedging cost.
- Implied minus realised vol (VRP) would average zero.

Empirically, for BTC/ETH options 2019-2025 the null is rejected in *calm and moderate* regimes: VRP is positive on average, extreme RR readings mean-revert, and delta-hedged wing-selling shows positive expectancy. **But the null is not rejected in tail events** — 2020-03-12, 2022 (LUNA/FTX), and 2025-10-10 all produced episodes where the sold wing paid off catastrophically and a full year of skew premium vanished in hours. The strategy is a positive-carry, negative-skew trade: it looks like free money in any window that excludes a tail, exactly as the null would predict for a risk premium.

## Rules

### Instrument and venue

- **Venue:** [[deribit|Deribit]] BTC and ETH options (USDC-margined linear preferred to avoid inverse-payoff distortion; coin-margined acceptable with the correlation adjustment).
- **Expiry:** 14-45 DTE. Shorter than 14 DTE the gamma risk dominates the vega premium; longer than 45 DTE the skew is stickier and capital is tied up.
- **Strikes:** 25-delta put and 25-delta call as the reference wings; 10-delta for aggressive tail-skew expressions.

### Entry

Enter a delta-hedged risk reversal when **all** hold:

1. **Skew dislocation.** The 25-delta risk reversal (RR25 = IV_25dcall − IV_25dput) is beyond **+/-1.5 historical standard deviations** of its trailing 90-day distribution for that asset and tenor. Sell the rich wing, buy the cheap wing.
2. **VRP positive.** Trailing 30-day realised vol is **below** the ATM implied vol you would be net short (implied-minus-realised > 3 vol points) — confirms you are being paid to be short vol overall, not just short skew.
3. **DVOL not spiking.** Deribit DVOL (BTC vol index) is not in the top decile of its 1-year range and is flat-to-falling — avoids selling wings into an accelerating vol regime.
4. **Delta-neutral at inception.** Hedge net delta to ~0 using the [[perpetual-futures|perp]] or dated future; re-hedge on a delta band (below).

### Exit

Whichever comes first:

1. **Skew normalises** — RR25 returns inside +/-0.5 std of its 90-day mean (primary profit target).
2. **Vega P&L target** — +50% of the premium collected on the risk reversal.
3. **Time exit** — 7 DTE remaining. Close before terminal gamma risk explodes.
4. **Hard vol stop** — DVOL gaps > 40% intraday, or the net-short wing's IV expands > 2x from entry: close regardless of P&L.

### Position sizing

- **Vega budget:** cap net short vega at **0.5% of book NAV per 1 vol point** move (so a 10-vol shock costs ~5% NAV before hedge P&L).
- **Per-expiry cap:** no more than 30% of the vega budget in any single expiry.
- **Delta re-hedge band:** re-hedge when net delta drifts beyond +/-0.05 per BTC of notional; hedge on the perp to keep the [[funding-rate|funding]] leg cheap.
- **Reserve:** hold >=40% of margin as buffer for a Deribit margin call during a wing blowout.

## Implementation pseudocode

```python
# crypto_skew_rr.py — delta-hedged 25-delta risk reversal on Deribit
RR_ENTRY_STD   = 1.5     # enter beyond +/-1.5 std of 90d RR distribution
RR_EXIT_STD    = 0.5     # exit inside +/-0.5 std
VRP_MIN_VOLPTS = 3.0     # implied - realised must exceed this
DVOL_MAX_PCTL  = 0.90    # skip if DVOL in top decile
DELTA_BAND     = 0.05    # per BTC notional
VEGA_STOP_MULT = 2.0     # net-short wing IV doubles -> stop
DTE_MIN        = 7

def decide(surface, book):
    rr   = surface.iv_25d_call - surface.iv_25d_put      # signed skew
    rr_z = (rr - surface.rr_mean_90d) / surface.rr_std_90d
    vrp  = surface.atm_iv - surface.realised_vol_30d

    # ---- risk stops first ----
    if book.net_short_wing and surface.wing_iv >= VEGA_STOP_MULT * book.entry_wing_iv:
        return {"action": "CLOSE_ALL", "reason": "wing IV blowout"}
    if surface.dvol_gap_intraday > 0.40:
        return {"action": "CLOSE_ALL", "reason": "DVOL gap"}

    # ---- manage open book ----
    if book.position is not None:
        if abs(rr_z) <= RR_EXIT_STD or book.vega_pnl >= 0.5 * book.premium_collected:
            return {"action": "CLOSE", "reason": "skew normalised / target"}
        if book.dte <= DTE_MIN:
            return {"action": "CLOSE", "reason": "time exit"}
        if abs(book.net_delta) > DELTA_BAND:
            return {"action": "REHEDGE_PERP", "target_delta": 0.0}
        return {"action": "HOLD"}

    # ---- entry ----
    if surface.dvol_pctl_1y > DVOL_MAX_PCTL:  return {"action": "WAIT", "reason": "DVOL elevated"}
    if vrp < VRP_MIN_VOLPTS:                  return {"action": "WAIT", "reason": "VRP too thin"}
    if abs(rr_z) < RR_ENTRY_STD:              return {"action": "WAIT", "reason": "skew fair"}

    sell_wing = "25d_call" if rr > 0 else "25d_put"   # sell the rich side
    buy_wing  = "25d_put"  if rr > 0 else "25d_call"
    return {"action": "OPEN_RR", "sell": sell_wing, "buy": buy_wing,
            "hedge": "perp_to_delta_zero", "reason": f"RR z={rr_z:.2f}"}
```

The production version adds: Deribit REST/WS plumbing for the live surface and DVOL, per-strike liquidity checks (wing quotes are thin — never lift more than ~10% of the resting size), automated perp delta-hedging with a funding-cost guard, and a manual kill switch.

## Indicators / data used

- **[[implied-volatility]] surface** — per-strike IV from Deribit; the raw material. Sourced directly from Deribit or an aggregator (Laevitas, Amberdata, [[greeks-live|Greeks.live]]).
- **25-delta risk reversal (RR25)** — IV_25dcall − IV_25dput; the skew signal. Track its 90-day mean and std per asset/tenor.
- **Deribit DVOL** — BTC 30-day forward implied-vol index; the regime filter.
- **[[realized-volatility|Realised vol]]** — 30-day close-to-close or Parkinson high-low; the VRP denominator.
- **[[variance-risk-premium|VRP]]** — ATM implied minus realised; confirms the net short-vol carry.
- **[[perpetual-futures|Perp]] price + [[funding-rate|funding]]** — the delta-hedge leg and its carry cost.
- **[[options-greeks|Greeks]]** — net delta, vega, gamma of the book for sizing and re-hedge triggers.

> **Data honesty:** [[cryptodataapi|CryptoDataAPI]] provides BTC options **summary** data (OI, volume, max pain) and realised-vol/vol-regime context, *not* a full per-strike IV surface or DVOL. The live surface and RR must come from Deribit directly or a dedicated options-analytics vendor.

## Example trade

**Setup (2026-05-18, Deribit BTC, 30 DTE, USDC-margined):**

- BTC spot/perp: $61,000. ATM IV: 52%. 30-day realised vol: 44% → VRP +8 vol points (positive).
- RR25 = IV_25dcall (58%) − IV_25dput (49%) = **+9 vol points**. Trailing 90-day RR mean +2, std 4 → **z = +1.75** (call wing rich; a FOMO-driven upside bid). DVOL at the 55th percentile, flat.

**Entry:**

1. Sell 1.0 BTC of the 25-delta call at 58% IV; buy 1.0 BTC of the 25-delta put at 49% IV — a short-call/long-put risk reversal (net short the rich upside wing).
2. Net delta of the RR at inception ≈ +0.02 BTC (short call − long put leaves slight short delta plus the put delta). Hedge to zero with a small perp buy.
3. Premium collected net: ~0.006 BTC (~$366) after paying the long-put debit.

**Hold (12 days):**

- BTC drifts $61k → $63.5k (+4%), never approaching the short call strike ($68k). Upside FOMO fades; RR25 compresses from +9 to +3 vol points (z falls to +0.25).
- Delta re-hedged twice on the +/-0.05 band; perp funding paid ~$18 over the hold.
- The short call decays with theta faster than the long put; vega P&L on the skew compression accrues.

**Exit (day 12):**

- RR z back inside +0.5 std → close both wings.
- Skew-compression + theta P&L: **+0.011 BTC (~$700)**.

**Cost overlay (the load-bearing part):**

- Deribit option fee: 0.03% of underlying per option, **capped at 12.5% of premium**. Two legs in + two legs out = 4 option fees. On 1.0 BTC each ≈ 4 × 0.0003 BTC = 0.0012 BTC (~$75), but the 12.5%-of-premium cap binds on the cheap wing.
- Delta-hedge perp taker (0.05%) on ~0.1 BTC of re-hedges ×2 ≈ $6; perp funding ~$18.
- **Net P&L ≈ 0.011 − 0.0013 (fees) BTC − hedge ≈ +$600 on ~$4,000 margin committed over 12 days.** Roughly +15% on committed margin for the trade — attractive *only* because no tail fired. A single 2020-03-12-style gap through the short wing erases 20+ such trades.

## Performance characteristics

Realistic, cost-corrected expectations (2023-2026 BTC/ETH regime):

| Metric | Value | Note |
|---|---|---|
| Net Sharpe | ~0.8 | Positive carry, negative skew; Sharpe flatters the trade between tails. |
| Win rate (per trade) | 70-80% | Most skew dislocations normalise; the loss tail dominates EV. |
| Avg winner | +8-15% of committed margin | Skew compression + theta. |
| Avg loser | -20-40% of committed margin | Wing blowout; slippage on thin wing quotes inflates it. |
| Max drawdown | 30-40% | Concentrated in tail events (2020-03, 2022, 2025-10). |
| Breakeven cost budget | ~40 bps round-trip | Deribit option fees (capped at 12.5% of premium) + delta-hedge friction. |

**Cost overlay detail:** Deribit charges **0.03% of the underlying per option, capped at 12.5% of the option's premium**, plus **0.015% settlement/exercise**. Delta-hedging on the perp/future costs ~5 bps taker per rebalance plus [[funding-rate|funding]] carry. On low-premium far-OTM wings the 12.5% cap makes fees a large *fraction of premium* — wing-selling economics are far worse than the headline 0.03% suggests. Any backtest that applies a flat bps fee without the premium cap materially overstates edge.

## Capacity limits

Capacity is bounded by **wing liquidity on Deribit**, not by the underlying:

- BTC 25-delta wings on front-month expiries quote in low single-digit BTC size at the top of book; ETH thinner. Lifting more than ~10% of resting size walks the wing IV against you and leaks the trade.
- Realistic single-operator capacity: **$5-40M vega-equivalent** across BTC + ETH + multiple expiries, laddered over time. Above that, market impact on the wings and the correlation of all short-wing positions to one tail event make the book un-hedgeable.
- 10-delta tail-skew expressions have even lower capacity (quotes are sporadic) but larger percentage mispricing.

Scaling further requires diversifying across expiries and both assets, and accepting that in a real tail *all* short-wing positions correlate to 1.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Tail realised (Failure Mode #6).** The dominant risk. A gap through the sold wing (2020-03-12, LUNA, FTX, 2025-10-10) pays the buyer the exact convexity you sold. Negative skew means one event can erase a year of premium.
2. **Regime change / skew sign flip (Failure Mode #5).** Crypto skew is *sign-unstable*. A book calibrated to bull-market call skew gets run over when the regime flips to put skew (and vice versa). The RR mean/std must be re-estimated continuously; a stale 90-day window mis-signs the trade at the turn.
3. **Crowding (Failure Mode #4).** Ethena-style and structured-product desks systematically sell crypto vol/skew; ETF-option overlay funds add supply. The VRP and skew premium have compressed since 2022 as this capital arrived.
4. **Vol-of-vol shock.** DVOL itself can gap, expanding both wings simultaneously; the delta hedge does nothing for a pure vega/vol-of-vol move.
5. **Deribit counterparty / operational risk.** Single-venue concentration (~90% of the market). A Deribit outage or socialised-loss/clawback event during a tail leaves the short-wing book unhedgeable exactly when it matters. Deribit uses a portfolio-margin + insurance-fund model with potential position reduction in extremis.
6. **Coin-margin correlation.** For inverse options, a spot crash simultaneously marks the option against you *and* devalues the BTC collateral — a double hit that USD-margined equity option sellers never face.

## Kill criteria

Pause (not retire — the wing premium recurs) on any of:

1. **VRP inverted** — trailing 60-day realised vol exceeds the implied vol you sold by more than the premium collected.
2. **Book drawdown > 25%** peak-to-trough on the net-short-vega sleeve.
3. **DVOL gaps > 40% intraday** while net short a wing (crash or melt-up regime confirmed).
4. **No dislocation for 30 days** — RR25 sits inside +/-1 std with no entry signal; capital better deployed elsewhere.
5. **Deribit insurance-fund socialised loss or clawback** of any size.

Re-deploy when all clear and RR25 again reaches +/-1.5 std with positive VRP and non-elevated DVOL. See [[when-to-retire-a-strategy]].

## Advantages

- **Delta-neutral, view-free direction.** No opinion on BTC price required — only on skew mean-reversion and VRP persistence.
- **Positive carry.** Theta and skew compression pay while you wait; high win rate in calm/moderate regimes.
- **Documented premium.** The crypto VRP and skew risk premium are supported by academic and Deribit-data studies.
- **Public, transparent inputs.** No information asymmetry can be used against you; the surface is observable.
- **Diversifying.** Vol/skew P&L is largely orthogonal to directional trend/momentum books.

## Disadvantages

- **Negative skew / fat left tail.** "Picking up pennies" — one wing blowout dominates the EV, and it lands in the data you have least of.
- **Sign instability.** Crypto skew flips sign across regimes; equity-trained intuition ("always sell puts") is actively dangerous here.
- **Fee structure is punitive on wings.** Deribit's 12.5%-of-premium cap makes far-OTM wing-selling far less profitable than a naive bps model implies.
- **Single-venue concentration.** ~90% of the market is one exchange; counterparty and outage risk are non-diversifiable.
- **Coin-margin double-jeopardy** on inverse options during a crash.
- **Requires a real options stack.** Live surface, DVOL, greeks, automated delta-hedging — not a chart-trader strategy.
- **Capacity is modest** and wing liquidity is thin.

## Sources

- He, Manela, Xu, Yan, *Fundamentals of Perpetual Futures* (2022/2024) — establishes the crypto derivatives risk-premium context that the options VRP sits alongside. arxiv.org/abs/2212.06888.
- Deribit Insights and DVOL methodology documentation — BTC/ETH implied-vol index construction, option fee schedule (0.03% of underlying, capped at 12.5% of premium; 0.015% settlement), portfolio margin. (Public docs; see [[deribit]].)
- Alexander & Imeraj and related academic work on Deribit implied-vol surface and BTC variance risk premium — document positive implied-minus-realised spreads and skew dynamics on crypto options.
- CBOE SKEW methodology (equities) — conceptual reference for the tail-skew index framing, adapted to crypto. See [[cboe-skew-index]].
- Practitioner literature on the 25-delta risk reversal as the standard skew metric (FX and crypto options desks). See [[risk-reversal]], [[volatility-skew]].

## Getting the Data (CryptoDataAPI)

CryptoDataAPI provides BTC options **summary** and realised-vol/vol-regime context. The full per-strike IV surface, DVOL, and 25-delta RR must come from Deribit directly or an options-analytics vendor (Laevitas, Amberdata, Greeks.live).

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, max pain
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed/expanding/vol_shock/mean_reverting/normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding for the delta-hedge perp leg

**Historical data:**
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=730` — daily OHLCV for realised-vol estimation
- `GET /api/v1/volatility/regime/BTC` — per-asset vol-regime detail + 60d history
- `GET /api/v1/backtesting/klines` — deep OHLCV archive for realised-vol / VRP backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-intelligence]], [[cryptodataapi-regimes]].

## Related

- [[implied-volatility]] — the foundation of all skew analysis
- [[volatility-skew]], [[volatility-smile]], [[volatility-surface]] — the surface being traded
- [[risk-reversal]] — the primary instrument for expressing a skew view
- [[skew]], [[cboe-skew-index]] — skew measurement
- [[variance-risk-premium]], [[volatility-risk-premium]] — the premium harvested
- [[options-greeks]], [[vega]], [[gamma]], [[delta-hedging]] — the risk being managed
- [[gamma-scalping]] — the long-convexity mirror image of this trade
- [[straddle]], [[strangle]] — ATM vol expressions vs the wing focus here
- [[crypto-options-volatility-selling]], [[crypto-options-dispersion]], [[volatility-carry]] — adjacent crypto vol strategies
- [[deribit]] — the venue that is effectively the whole market
- [[perpetual-futures]], [[funding-rate]] — the delta-hedge leg
- [[garch-volatility]] — a forecast to compare against implied for the VRP filter
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]] — methodology
</content>
</invoke>
