---
title: "Options Premium Selling (Crypto)"
type: strategy
created: 2026-05-07
updated: 2026-07-19
status: review
tags: [options, crypto, derivatives, volatility, risk-management, premium-selling, bitcoin, ethereum]
aliases: ["Premium Selling", "Theta Gang", "Short Vol Core", "Selling Premium", "Crypto Premium Selling"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[long-vol-vs-short-vol]]", "[[variance-risk-premium]]", "[[crypto-options-volatility-selling]]", "[[options-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[short-put-spread]]", "[[premium-selling-systematic]]", "[[long-vol-overlay]]", "[[tail-risk-hedging]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[volatility-regime-classification]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[tom-sosnoff]]", "[[ergodicity]]"]

# Edge characterization
edge_source: [risk-bearing, behavioral, structural]
edge_mechanism: "Leveraged spot holders buy crash protection above actuarially fair value and retail buyers overpay for OTM lottery calls; the premium seller collects the variance risk premium in exchange for tail exposure — compensation for absorbing a risk the counterparty is structurally compelled to offload regardless of price."

# Data and infrastructure requirements
data_required: [options-chain, funding-rates, volatility-regime, open-interest, ohlcv-daily]
min_capital_usd: 25000
capacity_usd: 300000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 0.6
expected_max_drawdown: 0.40
breakeven_cost_bps: 60

# Kill criteria
kill_criteria: |
  - DVOL rises > 50% in a single session → flatten short vega immediately
  - drawdown > 25% → halve size; > 35% → halt new entries
  - rolling 12-month Sharpe < 0.0 (≥9 months data) → halt
  - realized VRP (DVOL − subsequent RV) negative on 6-month rolling basis → halt new entries
  - round-trip cost above 60 bps crypto budget → review; well above → retire
---

Options premium selling is the **canonical short-vol strategy**, re-scoped to crypto: the trader systematically sells out-of-the-money puts, calls, [[short-strangle|strangles]], or [[iron-condor|condors]] on [[deribit]] BTC and ETH (plus on-chain vaults and BTC-ETF options) and harvests the [[variance-risk-premium]] (VRP) — the persistent gap between implied volatility ([[dvol|DVOL]]) and subsequently realized volatility. It is the **short-vol core** referenced throughout [[long-vol-vs-short-vol]]: the income engine that, paired with a [[long-vol-overlay]], forms the [[options-portfolio-construction|portfolio construction]] template. In crypto the VRP is structurally wider than in equities (DVOL routinely runs 2-4× the SPX premium), but it underwrites a genuinely fatter tail on a single dominant offshore venue.

## Edge source

Primarily **risk-bearing**, secondarily **behavioral** and **structural** (see [[edge-taxonomy]]).

- **Risk-bearing** — the seller is the insurer. Buyers of crypto puts pay above fair statistical value for crash protection; the seller collects this premium in exchange for tail exposure. Crypto's tail is genuinely fatter (BTC has printed −50% in 24h and −12% in 60 seconds), so the equilibrium premium is larger.
- **Behavioral** — buyers persistently overestimate left-tail probability and overpay for [[skew]] and OTM strikes; retail overpays for OTM "100x" calls ([[overweighting-small-probabilities]]).
- **Structural** — the *supply* of crypto vol sellers is small and capital-constrained (offshore venue, crypto/USDC collateral, willingness to warehouse tail risk), which keeps premium on the table for those who can bear it. Additionally, the option [[skew]] is mechanically linked to the [[perpetual-futures|perp]] book: richly positive [[funding-rate|funding]] firms call skew, so the surface inherits perp positioning rather than being set by hedgers.

## Why this edge exists

The other side of the trade is dominated by **price-insensitive buyers** of optionality. Leveraged spot holders and whales buy BTC/ETH puts for balance-sheet-survival reasons regardless of price. Fund managers buy protection for career-risk reasons (avoiding a fund-ending drawdown). Retail buys lottery-like OTM calls and crash-protection puts driven by [[loss-aversion]] and [[recency-bias]]. None of these buyers are *pricing* the options; they pay whatever the market charges.

The seller, by contrast, accepts a negatively-skewed payoff that most participants find psychologically and career-wise intolerable, on a venue that demands crypto collateral and can force-liquidate in a spike. The premium is the fee for absorbing this tail. Deribit/[[greeks-live]] measurement shows BTC/ETH DVOL averaging materially above subsequently realized RV over multi-year horizons — persistent and economically meaningful.

The edge does **not** disappear with arbitrage because the buyer side is structurally unable to stop buying. It does, however, compress in calm regimes (buyers reduce hedging) and expand in stressed regimes (buyers panic-buy puts).

### Structure menu

Premium selling is a family, not a single trade. The structure chosen trades expected return against tail control:

| Structure | Risk | Vega/Theta intensity | Typical use | Page |
|---|---|---|---|---|
| Short [[short-strangle\|strangle]] | undefined | high | capital-efficient core in calm regimes | [[short-strangle]] |
| [[short-straddle]] | undefined | highest | maximum ATM premium, maximum [[gamma]] | [[short-straddle]] |
| [[iron-condor]] | defined | medium | the workhorse defined-risk income trade; preferred in crypto | [[iron-condor]] |
| [[iron-fly]] | defined | high theta / high gamma | rich-DVOL, range-bound tape | [[iron-fly]] |
| [[short-put-spread]] | defined | low-medium, bullish tilt | accumulation-intent, directional bias | [[short-put-spread]] |
| [[cash-secured-put\|cash-secured put]] | undefined notional | low | acquisition-intent, USDC collateral | [[cash-secured-put]] |
| [[calendar-spread]] | defined (debit) | **long** vega | low-DVOL, expect DVOL to rise | [[calendar-spread]] |

Note the [[calendar-spread]] is the odd one out: it is *long* vega and benefits from rising DVOL, so it is the natural complement when [[dvol|DVOL]] percentile is too low to justify the short-vega structures above.

## Null hypothesis

If DVOL exactly equaled realized volatility on average, premium selling would earn **zero** before costs and **negative** after Deribit's wide spreads and delta-hedge slippage. The position would still have negative skew but the long-run mean would be flat; daily theta would be exactly offset by daily gamma losses on average. Empirically the null is rejected — DVOL averages several vol points above subsequently realized RV on BTC/ETH — but in any single window the realized VRP can be zero or negative (LUNA-to-FTX 2022, the weeks after 2025-10-10).

## Rules

**Universe:** Deribit BTC and ETH as the core (the deep, dominant chains); altcoin options (SOL and a handful of others) only as a small, thinly-sized satellite.

**Entry:**

- Sell strangles or iron condors at **21-45 days to expiration (DTE)** — the steep part of the [[theta-decay]] curve. Avoid weeklies (crypto gamma too hot for the gap profile).
- Strike selection: **15-16 delta** on each side for undefined-risk strangles; **16 delta short / 8-10 delta long wing** for defined-risk condors (preferred in crypto).
- Enter only when [[dvol|DVOL]] percentile is **above ~40** (and below ~90) of its trailing-year range — avoid selling premium when it is already cheap, and avoid selling into an active vol-shock.
- Require **DVOL − 30-day realized vol > 5 vol points** (crypto's healthy-premium threshold).
- Avoid the 24-48h before scheduled macro (FOMC, CPI) and known crypto catalysts (large token unlocks, major protocol events) unless explicitly trading event vol.
- **Skew-aware wing selection**: read [[funding-rate|perp funding]] and 25-delta [[risk-reversal]] — lean the short toward the wing the leveraged crowd has overbid.

**Position sizing:**

- Total short-vol [[vega]] capped at a fixed % of NAV: **≤ ~1% of NAV per 1 vol point** of DVOL (crypto DVOL can move 20-40 points in a session — tighter than an equity cap).
- Per-trade margin use under 5% of NAV for BTC/ETH, under 2% for altcoins.
- Aggregate [[delta]] kept inside a band via the Deribit **perpetual** or dated future; re-hedge at least once per 8-hour funding boundary.
- Keep Deribit portfolio-margin utilisation ≤ 25% — spike-driven margin expansion is the most common force-liquidation path.

**Exit:**

- Close at **50% of max profit** for strangles, **25-50%** for condors. Mechanical — not discretionary.
- Roll the **untested side** (for a credit only) when one strike is breached and the trade is still inside the profit window.
- **Close at 10-14 DTE** if not yet at target — crypto gamma accelerates faster into expiry than equity gamma (24/7, unbounded gaps).
- Close immediately if a single trade exceeds **2x credit collected** (stop-loss) or the portfolio vega budget is breached.
- **Vol-shock kill:** flatten short vega if DVOL rises **> 50% in a session** — the load-bearing risk control.

**Overlay:**

- Maintain a [[long-vol-overlay]] (long-dated OTM BTC/ETH puts and/or long DVOL-sensitive convexity) of roughly 5-10% of capital at all times (see [[vega-budgeting]]). The overlay caps tail loss; without it this is naked short crypto vol on a venue that can auto-liquidate.

## Implementation pseudocode

```python
def daily_premium_selling_loop(book, market):
    # 0. Vol-shock kill switch first
    if market.dvol_session_change >= 0.50:
        return book.flatten_short_vega(reason="dvol_shock_kill")

    # 1. Cost-of-business overlay
    book.maintain_long_vol_overlay(target_pct_nav=0.07)

    # 2. Book hygiene -- close winners and laggards first
    for trade in book.open_trades:
        if trade.pct_max_profit_realized() >= 0.50:
            book.close(trade, reason="50pct_profit_target")
        elif trade.dte() <= 12 and trade.pct_max_profit_realized() < 0.50:
            book.close(trade, reason="time_exit_crypto_gamma")
        elif trade.pnl_dollars() <= -2.0 * trade.credit_collected:
            book.close(trade, reason="2x_credit_stoploss")

    # 3. Vega and delta budget check
    if book.total_short_vega() > book.vega_budget():
        return  # at risk capacity; open nothing

    # 4. Entry filter (DVOL percentile band + VRP)
    if not (0.40 <= market.dvol_pctl("BTC") <= 0.90):
        return
    if (market.dvol("BTC") - market.rv30("BTC")) < 5.0:
        return

    # 5. Enter new mechanical trade
    if book.open_trade_count() < book.target_trade_count():
        trade = build_strangle(
            underlying="BTC",
            dte=35,
            short_call_delta=0.16,
            short_put_delta=-0.16,
            wings=(buy_8_delta_protection_if_defined_risk),
            skew_tilt="call" if market.funding_8h("BTC") > 0.0003 else "balanced",
        )
        book.open(trade, size=size_by_vega_budget(trade))

    # 6. Delta hedge with the Deribit perp (band + funding boundary)
    if abs(book.net_delta_per_nav()) > 0.005 or market.funding_boundary:
        book.hedge_delta_with_perp()
```

## Indicators / data used

- Real-time Deribit [[options-chain]] with greeks; bid-ask, IV, [[delta]], [[vega]], [[theta]] per strike (via [[greeks-live]]).
- [[dvol|DVOL]] level and DVOL percentile per underlying over a trailing-year window; DVOL term structure (contango vs backwardation of the forward-vol curve).
- [[realized-volatility]] — 10/20/30-day rolling, to gauge VRP capture.
- [[funding-rate]] and perp [[open-interest]] — the skew driver.
- [[skew]] and [[volatility-surface|surface]] for relative-value entries and wing selection.
- [[max-pain]] / options OI by strike, and [[gamma-exposure|GEX]] for dealer-gamma context.
- Macro and crypto-catalyst calendars for blackout periods.

## Payoff & Greeks

The canonical short-strangle payoff is a **flat-topped tent**: maximum profit equals the total credit collected, realised when the underlying expires between the two short strikes; the loss legs open up once price breaches a short strike. Defined-risk [[iron-condor|condor]] variants clip those tails at the long wings, converting the unbounded slopes into a capped trapezoid — the strongly-preferred crypto expression given the gap risk.

```
Short strangle P&L at expiration (per unit of underlying)

 credit ┤        ┌──────────────┐
        │       /                \
   0  ──┼──────/──────────────────\──────────────
        │     /  Kp          Kc    \
        │    /                      \
 -loss  ┤ (steepening via skew)      (linear)
        └────────────────────────────────────────
              breakeven_low      breakeven_high
        breakeven_low  = Kp − total_credit
        breakeven_high = Kc + total_credit
```

Net Greeks for the core 16-delta strangle (the signs define the strategy as **short vol**):

| Greek | Sign | At entry | In a vol shock | Comment |
|---|---|---|---|---|
| [[delta]] | ~0 (managed) | near-neutral; hedged to a ±band | turns sharply against you as the tested strike gains delta | requires active perp-hedging in stress |
| [[gamma]] | **negative** | small at 35 DTE | explodes near a tested short strike and into expiry | the engine of fast losses; see [[gamma-explosion]] |
| [[theta]] | **positive** | the daily income; peaks 21-45 DTE | overwhelmed by gamma P&L in a fast gap | mechanical 10-14 DTE exit preserves the favourable theta/gamma ratio |
| [[vega]] | **negative** | the dominant exposure; sized via [[vega-budgeting]] | large mark-to-market loss as DVOL expands | the [[long-vol-overlay]] is bought to offset this leg |
| Rho | small | minor | minor | rarely binds |

The trade is short [[gamma]], short [[vega]], long [[theta]] — the textbook short-volatility signature. The whole edge is collecting positive theta and the [[variance-risk-premium]] faster than negative gamma and vega bleed it back in adverse paths. See [[long-vol-vs-short-vol]] for the mirror-image profile on the other side.

## Example trade

*Illustrative only — not a recommendation.*

- **Date:** 2026-04-15. BTC = $68,000, DVOL = 55 (63rd percentile), 30-day RV = 40 → VRP ≈ 15 vol points.
- **Trade:** Sell BTC strangle, 35 DTE, USDC-margined (linear):
  - Short 1 BTC $76,000 call (~16 delta) for a call-side credit.
  - Short 1 BTC $60,000 put (~16 delta) for a put-side credit.
  - Total credit ≈ $1,400 per 1-BTC strangle. Funding is +0.03%/8h (mild call-skew richness → tilt the short toward the call wing).
- **Margin:** varies by Deribit portfolio margin; keep utilisation ≤ 25%.
- **Daily theta** at entry: positive.
- **Outcome (base case):** BTC drifts to $65,500 at 20 DTE; strangle marked at ~$700 = 50% of max profit. Close per the rule. Perp delta-hedging roughly nets to zero (small funding collection offsets slippage).
- **Realized P&L:** ~$700 profit per strangle in 15 days (before the inevitable drawdown cycle).

## Performance characteristics

- **Gross expected return** (before overlay): steady positive in the 80-90% of time markets are calm-to-elevated-but-stable; flat to deeply negative in shock windows.
- **Net expected return** (after [[long-vol-overlay]]): smoother, lower-mean distribution.
- **Hit rate:** 70-90% of months profitable.
- **Worst-window historical** (naked, no overlay): short BTC/ETH strangles were devastated in **2020-03** (BTC −50% in 24h), the **2022** LUNA→FTX bear, and **2025-10-10** (BTC −12% in 60 seconds, ~$19B liquidated).
- **Sharpe (calm regime, in-sample)**: high and misleading. **Full-cycle Sharpe**: ~0.4-0.8 naked, ~0.8-1.4 with overlay.
- **Skew:** strongly negative without overlay; roughly symmetric with overlay.
- **Cost sensitivity:** Deribit spreads on 15-delta wings run 3-8 vol points round-trip, and the taker fee is capped at 12.5% of premium; bid-ask discipline is non-negotiable — the breakeven cost budget is roughly double an SPX book's.

### Regime conditioning

Premium selling is one of the most [[market-regime|regime]]-dependent strategies in the catalog (see [[volatility-regime-classification]]):

| [[market-regime\|Regime]] | DVOL / VRP state | Short-vol outcome | Action |
|---|---|---|---|
| Calm, low-DVOL grind | low DVOL, thin VRP | steady theta accrual; the 80-90% case | normal sizing; resist upsizing |
| High-DVOL, post-shock | elevated DVOL, fat VRP | the richest window; premium genuinely expensive | best risk-adjusted entries (but wait for the spike to roll over) |
| Trending / drift | rising realised vol, drifting underlying | one side tested repeatedly; gamma bleed | reduce size; manage tested side mechanically |
| Vol shock / crisis | DVOL gap +50%, backwardation | the kill scenario; months of theta erased in a day | overlay + kill switch cap the loss; do not add |

The strategy's expectancy is positive *across* the cycle only because the long calm stretches outnumber the shocks — but the shocks are where the entire distribution's tail lives, which is why the [[long-vol-overlay]] and the DVOL kill switch are non-negotiable.

## Capacity limits

- **BTC/ETH strangles:** capacity is bounded by Deribit depth — clean fills to roughly $5-25M vega-notional on front-month BTC (ETH thinner) before you move the surface; beyond that, use the [[greeks-live]]/Paradigm RFQ network.
- **Altcoin strangles:** capacity is far tighter — often a small fraction of BTC/ETH size, with far wider spreads.
- **Whole book:** an individual/small-fund operator caps around $50-300M notional before roll impact dominates — one to two orders of magnitude smaller than an SPX vol book.
- The strategy's true capacity constraint is **risk-bearing capital and venue depth**, not the trader's own balance sheet — selling more strangles requires linearly more shock-absorbing capital on a single venue.

## What kills this strategy

The dominant failure modes (see [[failure-modes]]):

1. **Vol shock with gap** — DVOL spikes 50-100%+ in hours; gamma losses dwarf theta accrued for months. Examples: 2020-03-12, [[terra-luna|LUNA]], [[ftx-collapse|FTX]], 2025-10-10.
2. **Margin reprice / Deribit auto-liquidation** — portfolio-margin requirements can rise 5-10x in hours, forcing liquidation at the worst prices. This is **liquidity-driven ruin**, not directional ruin.
3. **Crowded trade unwind** — systematic covered-call and vault flow all hitting the same wing; cascade dynamics amplified by perp liquidations. See [[liquidation-cascade]].
4. **Altcoin gap** — a single uncovered short put on an altcoin that gaps −50% can erase months of BTC/ETH theta.
5. **Coin-margined wrong-way risk** — inverse options let collateral fall in USD terms exactly as the short goes against you (quanto-like double hit).
6. **Single-venue concentration** — a Deribit outage, hack, or insolvency during a vol event is existential and un-hedgeable.
7. **Discretionary intervention** — rolling losers, doubling down in stress; the KKMFA/[[karen-the-supertrader]] and [[ljm-preservation-and-growth]] blowups (equity, but the failure mode is universal) are the cautionary record.

## Kill criteria

Mechanical retirement/pause triggers (also see [[when-to-retire-a-strategy]]):

- **DVOL rises > 50% in a single session** → flatten short vega immediately.
- **Drawdown** exceeds **25%** → halve size; **35%** → halt new entries pending review.
- **Rolling 12-month Sharpe** below **0.0** (≥ 9 months data) → halt; below **0.5** → review.
- **Realized VRP** (DVOL − subsequent RV) negative on a 6-month rolling basis → halt new entries until it recovers.
- **Deribit portfolio-margin** rising > 50% of equity in a single session, or any auto-liquidation/socialised-loss event → halt and re-architect overlay.
- **Cost increase**: round-trip cost above the crypto budget (≈ 60 bps) → review; well above → retire.
- **Regime change**: structural change in VRP (vault/ETF supply crowding the call wing) → review.

## Advantages

- High [[hit-rate]] and [[positive-theta]] generate steady, psychologically rewarding daily P&L.
- **Fatter structural premium than equities** — more room to absorb Deribit's wider costs.
- **Cash-settled to index** — no physical assignment, minimal pin risk.
- **Readable skew** — the perp/funding link often reveals the overbid wing in advance.
- **Mechanical and rule-based** — once the rules are set, execution can be partly automated.
- Compounds consistently in the 80-90% of time markets are not in crisis.
- The empirical edge ([[variance-risk-premium]]) is one of the most rigorously documented anomalies in finance and runs fatter in crypto.

## Disadvantages

- **Negative skew** — fast, large losses in shocks; months of gains erased in a day. Crypto's tail is genuinely fatter than equities'.
- Without an explicit [[long-vol-overlay]] this is **leveraged short tail** on a venue that can auto-liquidate — one shock can be terminal.
- **No [[section-1256-contracts|§1256]] shelter** — premium is ordinary/short-term income; after-tax net is materially below an SPX program, with onerous coin-margined record-keeping.
- **Single-venue (Deribit) dependency** with no deep fallback.
- **Coin-margined non-linearity** if inverse options are used.
- **Margin reprices in stress**, removing capital exactly when it is needed to defend the book.
- **Behaviorally hostile** — looks easy in calm stretches and tempts size increases right before shocks.

## Crypto specifics

- **Deribit is the market.** The overwhelming majority of crypto options OI is on [[deribit]]; the core book is BTC/ETH there, with altcoin chains far thinner.
- **DVOL, not VIX.** The regime gauge and entry gate are Deribit's [[dvol|DVOL]] index and its percentile, plus a DVOL−RV spread — not VIX/IV-rank.
- **European, cash-settled.** No early [[assignment]], no delivery, minimal pin risk.
- **Inverse vs linear settlement.** USDC-margined (linear) options give clean USD P&L; coin-margined (inverse) options carry quanto-like non-linearity and wrong-way collateral risk.
- **Perp-funding sets the skew.** The option [[skew]] is mechanically linked to the [[perpetual-futures|perp]] book — richly positive [[funding-rate|funding]] firms call skew — so the seller can lean into the overbid wing.
- **24/7 markets, unbounded gaps.** No session close to cap a move; the time stop is pulled to 10-14 DTE and the DVOL kill switch is mandatory.
- **No [[section-1256-contracts|§1256]].** Premium is ordinary/short-term income — no 60/40 shelter.
- **Single-venue concentration.** A Deribit outage/insolvency during a shock is existential and un-hedgeable; the crypto VRP is *less* crowded than SPX vol, which is part of why the raw premium is fatter (and more fragile).

## Getting the Data (CryptoDataAPI)

DVOL and the IV surface come from Deribit / [[greeks-live]]; [[cryptodataapi]] supplies the options-flow, vol-regime, dealer-gamma, funding, and liquidation context for gating entries and firing the kill switch.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/quant/gex` — Gamma Exposure (dealer inventory + liquidation profile)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — funding (skew driver)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations (vol-shock early warning)

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for realized-vol computation
- `GET /api/v1/backtesting/klines` — deep kline archive for VRP backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

## Sources

- [[crypto-options-volatility-selling]] — the wiki's canonical treatment of the crypto VRP and its kill-switch risk framework.
- [[greeks-live]] / [[deribit]] documentation — DVOL, European cash settlement, coin-margined vs USDC-margined mechanics.
- Carr, Peter and Wu, Liuren. "Variance Risk Premiums" (2009) — canonical academic measurement of VRP.
- Bondarenko, Oleg. "Why Are Put Options So Expensive?" (2014) — direct empirical case for VRP.
- Spitznagel, Mark. *Safe Haven* (2021) — the case for pairing premium selling with a [[long-vol-overlay]] (equity-origin, applies with more force in crypto).
- Crash record: 2020-03-12, 2022-05 [[terra-luna|LUNA]], 2022-11 [[ftx-collapse|FTX]], 2025-10-10 [[liquidation-cascade|liquidation cascade]] — empirical worst-cases for naked short crypto vol.

## Related

- [[long-vol-vs-short-vol]] — the comparison page that frames this strategy as the short-vol core.
- [[crypto-options-volatility-selling]] — the systematic, delta-hedged short-vol book (the deep treatment).
- [[options-selling]] — the crypto premium-selling family hub.
- [[long-vol-overlay]] — the protective sleeve that should always run alongside this strategy.
- [[premium-selling-systematic]] — the systematic, rules-based implementation.
- [[short-strangle]] — canonical undefined-risk structure.
- [[iron-condor]] — defined-risk variant (preferred in crypto).
- [[short-put-spread]] — vertical credit spread implementation.
- [[variance-risk-premium]] — the underlying anomaly.
- [[dvol]] — the crypto vol gauge that gates entries.
- [[funding-rate]] — the perp linkage that shapes crypto skew.
- [[options-portfolio-construction]] — how to combine core and overlay.
- [[vega-budgeting]] — formal sizing framework.
- [[volatility-regime-classification]] — regime-conditional performance.
- [[tail-risk-hedging]] — the buy-side counterpart paying the premium.
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get.
- [[ergodicity]] — why time-average matters more than expected return for this profile.
