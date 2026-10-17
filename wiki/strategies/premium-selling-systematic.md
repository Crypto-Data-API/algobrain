---
title: "Systematic Premium Selling (Crypto)"
type: strategy
created: 2026-05-07
updated: 2026-10-17
status: review
tags: [options, crypto, derivatives, volatility, quantitative, algorithmic, risk-management, bitcoin, ethereum]
aliases: ["Systematic Premium Selling", "Mechanical Premium Selling", "Systematic Short Vol", "Crypto Systematic Premium Selling"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, options]
complexity: advanced
backtest_status: untested
related: ["[[options-premium-selling]]", "[[crypto-options-volatility-selling]]", "[[options-selling]]", "[[short-strangle]]", "[[iron-condor]]", "[[short-put-spread]]", "[[long-vol-overlay]]", "[[long-vol-vs-short-vol]]", "[[variance-risk-premium]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[funding-rate]]", "[[section-1256-contracts]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[tom-sosnoff]]", "[[tastytrade-mechanics]]", "[[managing-winners]]", "[[volatility-regime-classification]]"]

# Edge characterization
edge_source: [risk-bearing, behavioral, structural]
edge_mechanism: "Harvests the crypto variance risk premium (DVOL > realized RV) via mechanically executed 16-delta strangles; the systematic overlay reduces execution variance — the dominant real-world source of premium-seller underperformance — delivering the edge minus the discretionary mistakes."

# Data and infrastructure requirements
data_required: [options-chain, funding-rates, volatility-regime, open-interest, ohlcv-daily]
min_capital_usd: 25000
capacity_usd: 300000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 60

# Kill criteria
kill_criteria: |
  - DVOL rises > 50% in a single session → flatten short vega immediately
  - strategy-level drawdown ≥ 20% → halve size; ≥ 30% → halt new entries
  - rolling 12-month Sharpe < 0 (9+ months data) → halt
  - realized VRP (DVOL − subsequent RV) negative on 6-month rolling basis → halt new entries
  - vol shock with overlay covering < 30% of core gamma loss → overlay misspecified; halt and re-architect
  - discretionary deviation from rules ≥ 3 times per quarter → halt
gates:
  - id: btc_primary_eth_secondary
    role: universe
    rule: "Primary: Deribit BTC strangles and condors; secondary: ETH at smaller size; altcoin options excluded from the engine"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "BTC and ETH are the coins whose Deribit implied vol is served. Free tier sees BTC only."
  - id: dte_band
    role: entry
    rule: "Entry 1: DTE between 21 and 45 (pseudocode 35)"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "The 12 nearest Deribit expiries with days to expiry and ATM IV (Pro Plus; empty on lower tiers)."
  - id: short_strike_delta
    role: entry
    rule: "Entry 2-3: short call delta 16 (plus or minus 2), short put delta -16 (plus or minus 2); condor wings at 8-10 delta each side"
    runnable: false
    note: "No option chain or per-strike Greeks are served; strikes and deltas need Deribit's instruments and ticker API."
  - id: dvol_percentile_band
    role: filter
    rule: "Entry 4: DVOL percentile between about 40 and 90 for the underlying"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "About 180 days of daily DVOL are served (Pro Plus); the page's sibling options-premium-selling ranks against a trailing year, which needs Deribit's DVOL history."
  - id: vrp_five_points
    role: filter
    rule: "Entry 5: DVOL minus 30-day realised vol above 5 vol points"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].vrp
    note: "vrp = dvol - realized_30 on the same item; the page says DVOL comes from Deribit, but it is served here."
  - id: catalyst_blackout
    role: filter
    rule: "Entry 6: no major macro or crypto catalyst within the next 7 days (FOMC, CPI, large token unlocks, known protocol events)"
    runnable: partial
    endpoint: /api/v1/event/calendar?window_days=7
    field: items[].event_type
    note: "Macro prints (FOMC, CPI, NFP, PCE, PPI) and unlocks are served; protocol events are not. 'Large' unlock has no cut on the page: items[].unlocked_value_usd and pct_of_fdv size them."
  - id: vol_regime_gate
    role: filter
    rule: "The vol regime must not read vol_shock or expanding"
    runnable: true
    endpoint: /api/v1/volatility/regime/{coin}
    field: regime
    note: "From the page's AI-agent workflow."
  - id: vega_budget
    role: sizing
    rule: "Entry 7 and exit 5: total short vega at most about 1% of NAV per DVOL point; when breached, close the largest-vega trade first"
    runnable: partial
    input: position
    note: "Book vega comes from the trading venue's position Greeks; we serve no option Greeks."
  - id: margin_limits
    role: sizing
    rule: "Entry 8: Deribit portfolio-margin utilisation below 25%; per-trade margin under 5% of NAV"
    runnable: true
    input: position
  - id: skew_tilt_funding
    role: entry
    rule: "Tilt the strangle toward the call wing when 8h funding is above 0.03% (funding_8h > 0.0003), else balanced"
    runnable: true
    endpoint: /api/v1/derivatives/funding-rates?coin={coin}
    field: binance.current_rate
    note: "Binance's 8-hour rate; for Hyperliquid use 8 x hyperliquid.current_rate."
  - id: profit_take_50
    role: exit
    rule: "Exit 1: close at 50% of max profit"
    runnable: partial
    input: position
    note: "Needs the trade's live option marks from Deribit; we serve no option prices."
  - id: time_exit
    role: exit
    rule: "Exit 2: close at DTE 10-14 (pseudocode 12) regardless of P&L"
    runnable: true
    input: position
  - id: stop_2x_credit
    role: stop
    rule: "Exit 3: close when the loss reaches 2x the credit collected"
    runnable: partial
    input: position
    note: "Needs the trade's live option marks from Deribit."
  - id: dvol_shock_kill
    role: stop
    rule: "Exit 4: flatten short vega if DVOL rises more than 50% in a session"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol_change_24h
    note: "dvol_change_24h is the vol-point change between the last two daily DVOL closes: percent = change / (dvol - change). Daily resolution, so an intraday spike shows late; the agent workflow's faster proxy is composite_score on /api/v1/volatility/regime/score with a liquidation burst."
  - id: untested_side_roll
    role: exit
    rule: "If one short strike is breached inside the profit window, roll the untested side closer to spot for a credit only; never roll the tested side out in time; at most two adjustments, then close"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/summary?coin={coin}
    field: mark_price
    note: "Breach compares the mark (perp as spot proxy) with the short strike and the adjustment count is on the position record; the credit check needs Deribit prices."
  - id: delta_band_hedge
    role: sizing
    rule: "Hedge aggregate net delta within a band (pseudocode 0.5% of NAV) with the perp or a dated future; re-hedge at least once per 8-hour funding boundary"
    runnable: partial
    input: position
    note: "The 8-hour cadence is a clock rule; book delta comes from the venue's Greeks."
  - id: mandatory_overlay
    role: sizing
    rule: "Permanent long-vol overlay at a fixed annual premium spend (pseudocode 5% of NAV a year): BTC/ETH put ladder 3-6 months out, 15-25% OTM, rolled monthly, plus DVOL convexity armed when DVOL is low"
    runnable: true
    input: position
    note: "The overlay's own entry and monetisation rules are gated on the long-vol-overlay page."
  - id: drawdown_cuts
    role: stop
    rule: "Strategy drawdown of 20% or more: halve size; 30% or more: halt new entries"
    runnable: true
    input: position
  - id: realized_vrp_halt
    role: filter
    rule: "Halt new entries while realised VRP (DVOL minus the realised vol that followed) is negative on a 6-month rolling basis"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "Pair each day's DVOL with the realised vol over the next 30 days from daily candles. About 180 days of DVOL are served, too short for a full 6-month window of completed pairs."
---

Systematic premium selling is the **mechanical, rules-based implementation of [[options-premium-selling]]**, re-scoped to crypto: 21-45 DTE [[deribit]] BTC/ETH strangles, 16-delta short strikes, mechanical entries gated by [[dvol|DVOL]] percentile, exits at 50% of max profit or the crypto gamma-zone time stop (whichever comes first), with an institutional risk-discipline overlay including a permanent [[long-vol-overlay]] and a hard DVOL vol-shock kill switch. The rule set is the tastytrade / [[tom-sosnoff]] research lineage (see [[tastytrade-mechanics]]) cleaned up with institutional risk controls and tightened for crypto's fatter tail. This is the systematic implementation referenced in [[long-vol-vs-short-vol]]'s synthesis section, recommended for traders who cannot reliably make discretionary calls under stress.

## Edge source

**Risk-bearing**, **behavioral**, **structural** (see [[edge-taxonomy]]).

- The mechanical rules harvest the same [[variance-risk-premium]] as discretionary crypto premium selling — a VRP that runs 2-4× the equity premium but underwrites a fatter tail.
- The systematic overlay reduces **execution variance**: most premium-selling losses come from discretionary management under stress, not from the rules themselves.
- The rule set is empirically calibrated — 16-delta, ~35-DTE, 50% profit target, gamma-zone time exit — from the tastytrade equity research lineage, with the key crypto adaptations being a *tighter* vega budget, an *earlier* time stop, and a *hard DVOL kill switch* to survive crypto's genuinely fatter tail.

## Why this edge exists

Same edge as [[options-premium-selling]] — VRP — but with one additional mechanism: **trader-error reduction**. Empirically, discretionary premium sellers underperform their rule set due to:

- Rolling losers (giving losing trades "more time") in stress.
- Adding to losers during a liquidation cascade.
- Skipping high-DVOL entries that "feel scary."
- Cutting winners early in calm regimes due to greed.
- Sizing up after winning streaks — right before the shock.

Mechanical execution removes these failures. The systematic edge is **the discretionary edge minus the discretionary mistakes** — and in crypto, where a single 24/7 gap can be terminal, the mechanical kill switch is worth even more than in equities.

## Null hypothesis

Under the null where DVOL equals subsequently realized RV and there is no VRP, the strategy earns zero before costs. Under the additional null that mechanical and discretionary execution produce identical returns, there is no incremental edge from systematization. Empirical Deribit/[[greeks-live]] data and the equity tastytrade record reject both nulls: the crypto VRP exists on average, and trader execution variance is large — arguably larger in a market with no session close and unbounded overnight gaps.

## Rules

This is the canonical institutional rule set. [[options-premium-selling]] and this page share the same underlying rules; this page is the **systematic** version with strict, written triggers.

**Universe and instrument:**

- Primary: Deribit BTC strangles/condors. Secondary: ETH (smaller size). Altcoin options are explicitly EXCLUDED from the systematic engine — they go in a separate, smaller satellite book given their thin liquidity.

**Entry rules (all must be true):**

1. **DTE between 21 and 45.**
2. **Short call delta = 16 (±2). Short put delta = -16 (±2).**
3. **For defined-risk variant (iron condor):** long wings at 8-10 delta each side (preferred in crypto).
4. **[[dvol|DVOL]] percentile between ~40 and ~90** for the underlying (rich but not an active vol-shock).
5. **DVOL − 30-day realized vol > 5 vol points** (VRP confirmation).
6. **No major macro or crypto catalyst within next 7 days** — skip FOMC, CPI, large token unlocks, known protocol events.
7. **Aggregate book vega within budget** (see [[vega-budgeting]]).
8. **Deribit portfolio-margin utilisation < 25%.**

**Exit rules (any one triggers exit):**

1. **50% of max profit reached** → close immediately.
2. **DTE ≤ 10-14** → close at next opportunity regardless of P&L (never let a strangle live into the crypto gamma zone).
3. **Loss = 2x credit collected** → close as a stop-loss.
4. **DVOL rises > 50% in a session** → flatten short vega (vol-shock kill).
5. **Aggregate book vega budget breached** → close largest-vega trade first.

**Roll/adjustment rules:**

- If one short strike is breached but the trade is still inside the profit window, **roll the untested side** closer to spot to harvest more credit — **for a credit only**. Do NOT roll the tested side out in time — this converts a small loss into a path-dependent disaster.
- Maximum **two adjustments per trade**, then mandatory close.

**Sizing rules:**

- Total short vega capped at **≤ ~1% of NAV per vol point** of DVOL (crypto DVOL can move 20-40 points in a session — tighter than an equity book).
- Per-trade margin use under 5% of NAV.
- Aggregate net delta hedged within a band via the Deribit **perpetual** / dated future; re-hedge at least once per 8-hour funding boundary (which collects or pays funding).

**Overlay (mandatory):**

- Permanent [[long-vol-overlay]] sized at a fixed annual premium spend.
- Specifically: a BTC/ETH long-dated OTM **put ladder** (rolling monthly, ~3-6mo out, 15-25% OTM) plus long DVOL-sensitive convexity (long-dated ATM/OTM calls-on-vol proxy via Deribit or a long-vega calendar) armed when DVOL is low.
- Without the overlay, this strategy degrades to naked [[options-premium-selling]] and inherits the full crypto tail (2020-03, LUNA, FTX, 2025-10-10).

## Implementation pseudocode

```python
def systematic_premium_selling_loop(book, market):
    # 0. Vol-shock kill switch first
    if market.dvol_session_change >= 0.50:
        return book.flatten_short_vega(reason="dvol_shock_kill")

    # 1. Mandatory overlay maintenance
    book.maintain_long_vol_overlay(target_annual_pct_nav=0.05)

    # 2. Process all open trades
    for trade in book.open_trades:
        if trade.pct_max_profit_realized() >= 0.50:
            book.close(trade, reason="50pct_profit_target")
        elif trade.dte() <= 12:
            book.close(trade, reason="time_exit_crypto_gamma")
        elif trade.pnl_dollars() <= -2.0 * trade.credit_collected:
            book.close(trade, reason="2x_credit_stoploss")
        elif one_side_breached(trade) and trade.untested_roll_count() < 2:
            book.roll_untested_side(trade)  # for a credit only

    # 3. Vega budget gate
    if book.total_short_vega() / book.nav() > vega_budget_per_volpt:
        return

    # 4. Entry gates (DVOL percentile band + VRP + catalyst blackout)
    if not (0.40 <= market.dvol_pctl("BTC") <= 0.90):
        return
    if (market.dvol("BTC") - market.rv30("BTC")) < 5.0:
        return
    if market.catalyst_within_7d("BTC"):
        return

    # 5. Open new mechanical trade
    if book.open_trade_count() < book.target_count():
        trade = build_strangle(
            underlying="BTC",
            dte=35,
            short_call_delta=0.16,
            short_put_delta=-0.16,
            wings_at_delta=0.09,          # iron condor wings
            skew_tilt="call" if market.funding_8h("BTC") > 0.0003 else "balanced",
        )
        if trade.margin_use() < 0.05 * book.nav():
            book.open(trade, size=size_by_vega_budget(trade))

    # 6. Delta hedge if drift exceeds band
    if abs(book.net_delta_per_nav()) > 0.005 or market.funding_boundary:
        book.hedge_delta_with_perp()
```

## Indicators / data used

- Real-time Deribit BTC/ETH [[options-chain]] with greeks (via [[greeks-live]]).
- [[dvol|DVOL]] level and DVOL percentile (trailing year) per underlying; DVOL term structure.
- [[funding-rate]] and perp [[open-interest]] — the skew driver.
- Macro and crypto-catalyst calendars (event blackouts).
- Portfolio aggregate vega, delta, gamma; Deribit portfolio-margin utilisation.
- [[realized-volatility]] tracker for ex-post VRP measurement; [[max-pain]] / [[gamma-exposure|GEX]] for dealer context.

## Payoff & Greeks

The engine sells 16-delta strangles (or iron condors for defined risk). The naked strangle payoff is the classic short-vol tent — capped gain at the net credit, losses that accelerate past either short strike; the iron-condor variant truncates the tails with 8-10-delta long wings. The **mandatory** permanent [[long-vol-overlay]] then bolts a convex left-tail payoff onto the book, so the *combined* profile is "collect credit in calm markets, but cap the crash."

Short 16-delta strangle (per structure), with iron-condor wings shown dashed:

```
   P&L
    |        ________________________            <- max gain = net credit
    |       /                        \
    |      /                          \
  0 +-----/----------- spot -----------\----------  underlying at expiry
    |    /                              \
    | _ /  (uncapped loss naked)         \ _      <- IC long wings cap here
    |  (put short K)                (call short K)
```

Net Greeks of one short 16-delta strangle, and the book-level controls applied to each:

| Greek | Sign | Systematic control |
|---|---|---|
| [[delta]] | ~0 at entry (balanced strikes) | Re-hedged to a band via the Deribit perp, at least once per funding boundary |
| [[gamma]] | **Short** | The 10-14 DTE time exit removes the trade before the crypto gamma-heavy final weeks |
| [[theta]] | **Positive** | The carry; the 50%-of-max-profit target banks accumulated theta early |
| [[vega]] | **Short** | Capped at ~1% NAV per vol point via [[vega-budgeting]]; the [[long-vol-overlay]] holds offsetting long vega; DVOL kill switch flattens on a spike |

The book is **short gamma, short vega, long theta** — identical in sign to discretionary [[options-premium-selling]] and to the short-VRP variant on [[crypto-options-volatility-selling]]. The entire systematic apparatus exists to *bound* these Greeks: the time exit bounds gamma, the vega budget bounds vega, the DVOL kill switch caps the tail event, and the overlay converts the residual short-vega tail into a defined, hedged exposure.

## Example trade

*Illustrative — a mid-size Deribit book.*

- **2026-04-15:** BTC = $68,000, DVOL = 55, DVOL percentile = 63%, RV30 = 40 (VRP = 15). No catalyst for 14 days. All gates pass.
- **Open:** 5 BTC iron condors, 35 DTE, 16-delta short strikes, 9-delta long wings (USDC-margined):
  - Short $76,000 call / Long $80,000 call (call wing).
  - Short $60,000 put / Long $56,000 put (put wing).
  - Net credit ~$1,150 per 1-BTC condor = ~$5,750 total; max loss capped by the long wings.
- **2026-05-05 (20 days in):** BTC = $65,500. Trades marked at 50% of max profit. **Mechanical close: bank the profit.** No discretion.
- **Same day:** DVOL percentile = 58%, VRP still > 5 → reload 5 new condors at 35 DTE.
- **Concurrently:** the overlay bleeds a small daily premium; when a vol spike later fires, the OTM put ladder monetizes and caps the left tail — a small net-positive or small-loss month instead of ruin.

## Performance characteristics

- **Calm-regime gross return:** steady positive theta accrual (before overlay).
- **Calm-regime net return** (after overlay bleed): lower, smoother.
- **Hit rate:** 75-92% of months profitable.
- **Sharpe (calm regime, in-sample):** high and misleading (short-vol violates the Sharpe assumptions catastrophically).
- **Sharpe (full-cycle, with overlay):** ~0.9-1.4 — meaningfully above naked premium selling because the overlay + kill switch fix the left tail.
- **Max drawdown (full-cycle, with overlay):** ~15-25%.
- **Max drawdown (no overlay — DO NOT RUN):** 50-100% (a single Black-Thursday gap).
- **Worst-window historical:** manageable with overlay running per spec; catastrophic for the naked variant in 2020-03, 2022 (LUNA/FTX), and 2025-10-10.
- **Cost sensitivity:** Deribit spreads on the wings run 3-8 vol points round-trip; the taker fee is capped at 12.5% of premium. Use limit orders and mid-price entries; the crypto cost floor is roughly double an SPX book's.

### Behaviour by market regime

The DVOL-percentile entry gate is itself a [[market-regime]] filter, but realized P&L still tracks the regime closely:

| Regime | Engine behaviour | Overlay behaviour | Net |
|---|---|---|---|
| Low, stable DVOL | Few entries (gate often blocks); thin theta | Bleeds the annual budget | Modest positive |
| Elevated-but-calm DVOL (high percentile, RV stays low) | Best regime — rich credits, DVOL mean-reverts | Bleeds | Strong positive |
| Vol spike / crisis | Kill switch + 2x-credit stops fire; new entries blocked | **Monetizes** — caps the left tail | Small loss instead of ruin |
| Post-spike normalization | High DVOL + falling RV → reload aggressively | Re-arm ladders | Recovery regime |

The design intent is explicit: the engine harvests the [[variance-risk-premium|VRP]] in the first two regimes and the overlay + kill switch survive the third. Run without them, the third column becomes -50% to -100%.

## Capacity limits

- **BTC/ETH strangles/condors:** capacity bounded by Deribit depth — $5-25M vega-notional clean on front-month BTC (ETH thinner), then RFQ.
- **Practical retail/small-fund cap:** the vega budget and Deribit portfolio margin bind before raw balance sheet; the whole book caps around $50-300M notional before roll impact dominates.
- **Crowding risk:** rising as covered-call ETFs and on-chain option vaults scale systematic call-writing supply, compressing the call-side premium — the crypto analogue of equity vol-crowding.

## What kills this strategy

1. **Running without the overlay / kill switch** — the single greatest failure mode. The systematic rules manage normal-regime trades; only the overlay and DVOL kill switch cap the tail.
2. **Discretionary deviation under stress** — "this trade is special, I'll roll it." The whole point of systematization is to make this impossible.
3. **Margin reprice / Deribit auto-liquidation** — even with overlay, portfolio margin can rise 5-10x and force liquidation. Mitigant: keep margin utilisation low so shocks don't force closures.
4. **VRP regime change** — if the crypto VRP structurally compresses (vault/ETF supply crowding the call wing), expected return drops below cost.
5. **Single-venue concentration** — a Deribit outage/insolvency during a vol event is existential.
6. **Coin-margined wrong-way risk** — inverse collateral falls in USD terms as the short goes against you; use USDC-margined (linear) options for clean P&L.
7. **Altcoin contagion** — if the satellite altcoin book is too large, a single gap can hurt the core book via cross-collateralized portfolio margin.

## Kill criteria

- **DVOL rises > 50% in a single session** → flatten short vega immediately.
- **Strategy-level drawdown ≥ 20%** → halve size; **≥ 30%** → halt new entries.
- **Rolling 12-month Sharpe < 0** (9+ months data) → halt; **< 0.5** → review.
- **Realized VRP** (DVOL − subsequent RV) negative on 6-month rolling basis → halt new entries until it recovers.
- **Round-trip cost above the crypto budget (≈ 60 bps)** → review; well above → retire.
- **Vol shock with overlay covering < 30% of core gamma loss** → overlay misspecified; halt and re-architect.
- **Deribit auto-liquidation / socialised-loss / unscheduled-outage event** → flatten and stand down.
- **Discretionary deviation from rules ≥ 3 times per quarter** → halt; the trader has lost the systematic discipline that is the strategy's edge.

## Advantages

- **Removes execution variance** — the largest empirical source of premium-seller underperformance.
- **Hard tail controls** — the DVOL kill switch and overlay are the crypto-critical additions over discretionary trading.
- **Auditable and back-testable** — every decision is rules-based, so performance attribution is clean.
- **Scales to multiple accounts** — the rules can be replicated or run partly automated.
- **Fatter premium than equities** — more room to absorb Deribit's wider costs.
- **Behavioral protection** — mechanical rules prevent the rolling-losers spiral that kills most discretionary premium sellers.

## Disadvantages

- **Boring during calm regimes** — discipline drift is the main risk. Traders with the discretionary instinct abandon the rules just as they start working.
- **Inflexible on edge cases** — a rule set cannot adapt to novel conditions (new vault-flow regime, novel catalyst). Periodic rule review is required.
- **Still negative-skew without overlay + kill switch** — systematization alone does not remove tail risk.
- **No [[section-1256-contracts|§1256]] shelter** — premium is ordinary/short-term income.
- **Single-venue (Deribit) dependency** with no deep fallback.
- **Requires automation infrastructure** — mechanical execution at the required speed is hard to do manually under stress, especially with no market close.
- **Crowded** — the 16-delta, ~35-DTE, 50%-target rule is widely known; some compression of edge is plausible as vault/ETF supply grows.

## Crypto specifics

- **Deribit is the market.** The systematic engine trades BTC/ETH on [[deribit]]; altcoin chains are excluded from the core (too thin) and run only in a small satellite.
- **DVOL, not VIX.** Entries are gated on Deribit's [[dvol|DVOL]] percentile plus a DVOL−RV spread — not VIX/IV-rank — with a hard **> 50% DVOL session** kill switch the equity playbook lacks.
- **Tighter and hard-stopped.** Versus the equity rule set, crypto tightens the time stop (10-14 DTE), tightens the vega budget (~1% NAV per DVOL point), and makes the DVOL kill switch and [[long-vol-overlay]] mandatory — because the tail is fatter and the market never closes.
- **European, cash-settled.** No early [[assignment]] or delivery; clean mechanical closes.
- **Inverse vs linear settlement.** USDC-margined (linear) for clean USD P&L; coin-margined (inverse) carries quanto-like non-linearity and wrong-way collateral risk.
- **Perp-funding sets the skew.** Richly positive [[funding-rate|funding]] firms call skew; the engine tilts the short toward the overbid wing.
- **No [[section-1256-contracts|§1256]].** Premium is ordinary/short-term income — no 60/40 shelter.
- **Single-venue and margin risk.** Deribit portfolio margin can reprice 5-10x in a spike and auto-liquidate; keeping utilisation low is a first-class rule.

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
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history for VRP backtesting

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; IV/DVOL from Deribit / [[greeks-live]].

**Live dashboards:** [liquidations](https://cryptodataapi.com/liquidations) · [funding rates](https://cryptodataapi.com/funding-rates) · [gamma exposure](https://cryptodataapi.com/quant-gamma)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] is the natural executor of this rule set — every entry/exit trigger is mechanical and machine-checkable:

- **Entry gates** — `GET /api/v1/volatility/regime` (must not read `vol_shock`/`expanding`) + realized vol from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` for the DVOL−RV > 5 check (DVOL from Deribit)
- **Catalyst blackout** — `GET /api/v1/event/calendar` (filterable events up to 30 days out: macro prints, unlocks) automates entry rule 6, "no major catalyst within 7 days"
- **Kill switch** — `GET /api/v1/volatility/regime/score` + `GET /api/v1/market-intelligence/liquidations` polled each cycle as the automated DVOL-shock flatten trigger; `GET /api/v1/quant/gex` flags the dealer-short-gamma states where a spike cascades fastest
- **Wing tilt** — `GET /api/v1/derivatives/funding-rates?coin=BTC` drives the `skew_tilt` branch in the pseudocode
- **Backtest** — replay the mechanical loop on `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) with point-in-time regime states from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02) — validating against today's regime labels is lookahead bias
- **Tips** — the "discretionary deviation ≥ 3×/quarter → halt" kill criterion is best enforced by logging every agent decision against the written rules; append `?format=markdown` for cleaner context

## Sources

- [[tastytrade-mechanics]] / [[tom-sosnoff]] — the mechanical-rules philosophy (equity-origin; ports to crypto with tighter stops).
- [[crypto-options-volatility-selling]] — the wiki's canonical crypto VRP + kill-switch treatment.
- Carr, Peter and Wu, Liuren. "Variance Risk Premiums" (2009).
- Bondarenko, Oleg. "Why Are Put Options So Expensive?" (2014).
- Spitznagel, Mark. *Safe Haven* (2021) — the case for the mandatory overlay.
- Crash record: 2020-03-12, 2022-05 [[terra-luna|LUNA]], 2022-11 [[ftx-collapse|FTX]], 2025-10-10 [[liquidation-cascade|liquidation cascade]] — empirical worst-cases for the naked variant.

## Related

- [[options-premium-selling]] — the parent strategy page.
- [[crypto-options-volatility-selling]] — the deep short-vol-book treatment.
- [[options-selling]] — the crypto premium-selling family hub.
- [[long-vol-overlay]] — the mandatory overlay.
- [[long-vol-vs-short-vol]] — the comparison context.
- [[short-strangle]], [[iron-condor]], [[short-put-spread]] — the structures used.
- [[tastytrade-mechanics]] / [[tom-sosnoff]] — popularizers of the rule set.
- [[managing-winners]] — the 50% / time-stop management discipline.
- [[dvol]] — the entry-gate metric.
- [[funding-rate]] — the perp linkage that shapes crypto skew.
- [[vega-budgeting]] — the sizing framework.
- [[options-portfolio-construction]] — portfolio integration.
- [[volatility-regime-classification]] — regime mapping.
- [[section-1256-contracts]] — the tax shelter crypto options do *not* get.
- [[theta]], [[vega]], [[delta]], [[gamma]] — the Greeks the rule set bounds.
