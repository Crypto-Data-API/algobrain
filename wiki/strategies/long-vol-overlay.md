---
title: "Long Volatility Overlay"
type: strategy
created: 2026-05-07
updated: 2026-10-17
status: good
tags: [options, derivatives, volatility, risk-management, portfolio-theory, crypto, bitcoin, ethereum]
aliases: ["Long Vol Overlay", "Tail Overlay", "Convex Overlay", "Vol Sleeve", "Crypto Tail Overlay"]
strategy_type: quantitative
timeframe: position
markets: [crypto, options]
complexity: advanced
backtest_status: cost-corrected
edge_source: [risk-bearing, structural]
edge_mechanism: "Not a profit strategy in isolation; the 'edge' is portfolio-level: a small premium spend on Deribit BTC/ETH puts and DVOL convexity caps the left tail of a crypto short-vol core book, dramatically improving the geometric (compounded) return of the combined book."
data_required: [options-chain, dvol-history, ivr, underlying-ohlcv, portfolio-greeks, funding-rates]
min_capital_usd: 100000
capacity_usd: 500000000
crowding_risk: low
expected_sharpe: -0.5
expected_max_drawdown: 0.05
breakeven_cost_bps: 0
related: ["[[long-vol-vs-short-vol]]", "[[long-volatility-strategies]]", "[[short-volatility-strategies]]", "[[crypto-options-volatility-selling]]", "[[dvol]]", "[[deribit]]", "[[greeks-live]]", "[[options-premium-selling]]", "[[premium-selling-systematic]]", "[[tail-risk-hedging]]", "[[options-portfolio-construction]]", "[[vega-budgeting]]", "[[variance-risk-premium]]", "[[implied-volatility]]", "[[volatility-regime-classification]]", "[[liquidation-cascade-fade]]", "[[crisis-alpha]]", "[[sharpe-ratio]]", "[[geometric-mean]]", "[[funding-rate]]"]
gates:
  - id: btc_eth_deribit
    role: universe
    rule: "The overlay runs on Deribit BTC and ETH options only (majors-only basis risk against an alt book)"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].symbol
    note: "BTC and ETH are the coins whose Deribit implied vol is served. Free tier sees BTC only."
  - id: put_tenor
    role: entry
    rule: "Slow-burn leg: buy USDC-margined (linear) puts 2-3 months out, one new tranche per month"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "Pick the listed expiry with expiry_days about 60-90 (Pro Plus; empty on lower tiers). Monthly cadence is on the position record."
  - id: put_strike_otm
    role: entry
    rule: "Put strikes 15-25% out of the money"
    runnable: partial
    endpoint: /api/v1/hyperliquid/summary?coin={coin}
    field: mark_price
    note: "Target strike = mark x 0.75 to 0.85 (Hyperliquid perp mark as the spot proxy). The listed Deribit strike nearest that level and its price are not served."
  - id: put_payoff_target
    role: entry
    rule: "Choose the strike for a payoff of 5-10x premium on a 25-35% drawdown"
    runnable: false
    note: "Needs Deribit put prices and an option model across strikes; no option chain or prices are served."
  - id: put_budget
    role: sizing
    rule: "Put-ladder premium spend 1.5-3.0% of NAV per year"
    runnable: true
    input: position
  - id: roll_at_30dte
    role: exit
    rule: "Roll a put tranche when it reaches about 30 DTE if still out of the money; monetise per the triggers if in the money"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/summary?coin={coin}
    field: mark_price
    note: "DTE is on the position record; in or out of the money compares the mark with the tranche's strike."
  - id: dvol_leg_tenor
    role: entry
    rule: "Fast-fire leg: long-vega Deribit options (or DVOL futures) 1-2 months out, rolled monthly, losers left to expire"
    runnable: true
    endpoint: /api/v1/volatility/implied
    field: items[].term_structure[].expiry_days
    note: "Pick the listed expiry with expiry_days about 30-60 (Pro Plus)."
  - id: dvol_leg_strike
    role: entry
    rule: "Strike or position the DVOL leg to profit from DVOL rising well above its current percentile (e.g. DVOL 45 to 90+)"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].dvol
    note: "Current DVOL and about 180 days of daily history (items[].history[].dvol, Pro Plus) are served. DVOL futures and per-strike vega are not, so building the leg needs Deribit."
  - id: dvol_budget
    role: sizing
    rule: "DVOL-leg premium spend 0.5-1.5% of NAV per year; total overlay 2-4% of NAV per year"
    runnable: true
    input: position
  - id: vega_ratio
    role: sizing
    rule: "Overlay long vega = 8-15% of the core's short vega; add protection when it falls below 8%"
    runnable: partial
    input: position
    note: "Book vega comes from the trading venue's position Greeks; we serve no option Greeks."
  - id: trigger1_slow_burn
    role: exit
    rule: "Trigger 1: BTC drawdown of at least 15% within 30 days: sell 1/3 of the put ladder"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=31
    field: candles[].high
    replay: /api/v1/hyperliquid/candles?coin=BTC&interval=1d&start={start}
    replay_field: candles[].high
    note: "Drawdown = 1 - mark / highest daily high of the last 30 days; the live mark is assets[].mark_price on /api/v1/hyperliquid/open-interest. Hyperliquid BTC perp; daily history back to 2023."
  - id: trigger2_acceleration
    role: exit
    rule: "Trigger 2: BTC drawdown of at least 30%: sell another 1/3 and hold the final third"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin=BTC&interval=1d&limit=31
    field: candles[].high
    replay: /api/v1/hyperliquid/candles?coin=BTC&interval=1d&start={start}
    replay_field: candles[].high
    note: "Same drawdown as trigger1_slow_burn; the pseudocode measures both over 30 days."
  - id: trigger3_dvol_doubles
    role: exit
    rule: "Trigger 3a: DVOL doubles from the leg's entry level: sell half the DVOL convexity leg and redeploy into fresh convexity if DVOL stays elevated"
    runnable: true
    input: position
    endpoint: /api/v1/volatility/implied
    field: items[].dvol
    note: "Compare the live dvol with the dvol recorded at entry."
  - id: trigger3_dvol_95pct
    role: exit
    rule: "Trigger 3b: DVOL above about its 95th percentile: sell half the DVOL convexity leg"
    runnable: partial
    endpoint: /api/v1/volatility/implied
    field: items[].history[].dvol
    note: "About 180 days of daily DVOL are served (Pro Plus); the page names no percentile window, so a longer one needs Deribit's DVOL history."
  - id: never_sell_all
    role: sizing
    rule: "Never sell the entire overlay: always keep a residual sleeve against second-leg crashes"
    runnable: true
    input: position
  - id: reinvest_monetized
    role: sizing
    rule: "Recycle monetised proceeds into replacement protection at distressed strikes, a larger short-vol core when the DVOL percentile is rich, or spot BTC/ETH on the dip"
    runnable: partial
    input: derived
    inputs: [trigger3_dvol_95pct]
    note: "The page gives no split between the three uses or a cut for 'rich'."
---

A **long-vol overlay** is a permanent, rolling allocation to long options (a [[deribit|Deribit]] BTC/ETH put ladder plus a [[dvol|DVOL]]-referenced convexity ladder) attached to a crypto short-vol core book to **cap the left tail** of the combined portfolio. It is not a stand-alone money-maker: in isolation it bleeds 2-4% of NAV per year (fatter than the equity version because crypto premium is fatter). Its job is portfolio-level — to convert a negatively-skewed [[options-premium-selling]] / [[crypto-options-volatility-selling]] book into a roughly symmetric, survival-tolerant book whose **geometric return** dominates the naked premium-selling book over any horizon longer than a single calm regime. This page describes the mechanics, sizing, monetization rules, and integration with the short-vol core. Read [[long-vol-vs-short-vol]] for the conceptual frame, [[tail-risk-hedging]] for the stand-alone Universa-style implementation, [[long-volatility-strategies]] for the broader family.

## Edge source

**Risk-bearing** (in reverse) and **structural**.

- The overlay does not "have" an edge in the classical sense; it pays the crypto [[variance-risk-premium]] rather than collecting it.
- The portfolio-level edge is **convex offset**: small expected-cost insurance that improves the [[geometric-mean|geometric mean]] of a compounded short-vol book by far more than its premium.
- The *Safe Haven* / [[ergodicity]] argument (equity origin, transfers to crypto): a small convex overlay can raise the long-run [[geometric-mean]] return of a spot/short-vol book above the unhedged book despite the overlay's negative carry — and crypto's more frequent, deeper crashes give the overlay more chances to earn it back.

## Why this edge exists

Naked crypto short-vol books fail because they have **negative skew** and a non-trivial probability of ruin in any cycle (2020-03, LUNA, FTX, 2025-10-10). [[ergodicity|Ergodicity economics]] says the time-average return of a strategy with finite ruin probability is far below its ensemble-average return; the trader experiences the time average. A small permanent insurance position fixes the left tail and brings the time average toward the ensemble average. The buyer of the overlay — the manager running the short-vol core — is not betting on a crash; they are paying the premium to **stay in the game** through the next one, on a venue ([[deribit|Deribit]]) whose auto-liquidation engine punishes anyone who cannot.

## Null hypothesis

If the crypto [[variance-risk-premium]] were exactly zero and crashes were perfectly Gaussian, the overlay would be slightly net-negative-EV and the optimal allocation would be 0%. The empirical world rejects this null: realized crypto crashes are extremely fat-tailed and DVOL does not adequately price the worst-case tail. As a result, the overlay's portfolio-level Sharpe contribution is positive even though its stand-alone Sharpe is negative.

## Crypto specifics

- **DVOL convexity replaces VIX calls.** There is no crypto VIX-options market, so the fast-fire leg is long vega on the Deribit surface (or DVOL futures) struck well above prevailing [[dvol|DVOL]], rather than listed VIX calls.
- **Linear (USDC-margined) puts for the slow leg.** A hedge wants clean USD payoff, so the put ladder uses USDC-margined (linear) Deribit options; coin-margined (inverse) puts would let the collateral fall with spot exactly when the put pays.
- **24/7 monetization.** Triggers can fire at any hour, including weekends — an operational demand equity overlays never face, but also more windows to harvest.
- **Same-venue risk.** The overlay lives on Deribit, the venue that could halt or fail in the event being hedged; a residual off-venue reserve (stablecoin, spot) is part of the design.
- **Majors-only basis risk.** If the core sells vol on alts (rare) or the spot book is alt-heavy, the BTC/ETH overlay is an imperfect proxy — the hedge carries basis risk against the alt book.
- **Crypto crash calendar.** The overlay is calibrated to survive and monetize 2020-03 (BTC −50%/24h), LUNA, FTX (DVOL into 90s-100s), and 2025-10-10 (BTC −12%/60s, ~$19B liquidated).

## Rules

The overlay has two legs that work in series, not parallel: a **BTC/ETH put ladder** (slow-burn crash protection) and a **DVOL convexity ladder** (fast-fire vol-shock protection). Both run continuously on [[deribit|Deribit]].

**BTC/ETH put ladder:**

- Buy USDC-margined (linear) puts **2-3 months out**, strike **15-25% OTM**, in a ladder with one new tranche **per month** so a fresh strip is always being added and an aging strip rolled or monetized.
- Sized so total premium spend = **1.5-3.0% of NAV per year**.
- Roll positions when they reach **~30 DTE** if still OTM; monetize per the rules below if ITM.
- Strike selection should target **a payoff of 5-10x premium on a 25-35% drawdown** — not so deep it rarely pays, not so near-ATM it bleeds too fast.

**DVOL convexity ladder (fast-fire leg):**

- Buy long-vega Deribit options (or DVOL futures) **1-2 months out**, struck / positioned to profit from DVOL rising **well above** its current percentile (e.g., DVOL 45 → 90+).
- Sized so total premium spend = **0.5-1.5% of NAV per year**.
- Roll monthly; let losers expire.
- The DVOL leg fires faster than the put ladder in a pure vol shock (the **2025-10-10** cascade is the canonical example — DVOL gapped in minutes before a slow-developing drawdown would register) and complements the put ladder's crash payoff.

**Overlay leg summary:**

| Leg | Instrument | Tenor | Strike / positioning | Annual budget | Fires |
|---|---|---|---|---|---|
| Slow-burn | BTC/ETH puts (linear) | 2-3 months | 15-25% OTM | 1.5-3.0% NAV | Crypto crash (minutes-days) |
| Fast-fire | [[dvol\|DVOL]] convexity / DVOL futures | 1-2 months | Well above spot DVOL | 0.5-1.5% NAV | DVOL shock (seconds-hours) |

The two legs are intentionally **non-redundant**: the put ladder is the primary protection against a developing crypto drawdown; the DVOL leg fires faster in a pure vol shock, where implied vol gaps before price has fully repriced.

**Sizing the overlay against the core:**

- Total overlay premium budget: **2-4% of NAV per year** (fatter than the equity 2-3.5% because crypto convexity is more expensive).
- Target ratio: overlay long [[vega]] should equal **8-15% of the core short vega** (see [[vega-budgeting]]).
- Net portfolio vega remains slightly negative (the core dominates) but bounded.
- During a DVOL move from ~45 → 100, the overlay should gain enough to offset **30-60% of core gamma loss**.

**Monetization rules** (the discipline that separates good overlays from bad):

- **Trigger 1 (slow burn):** BTC drawdown ≥ 15% in ≤ 30 days → sell **1/3** of the put ladder. Locks in the first leg of payoff.
- **Trigger 2 (acceleration):** BTC drawdown ≥ 30% → sell another **1/3**. Hold the final third for further downside.
- **Trigger 3 (vol shock):** DVOL doubles from entry or exceeds its ~95th percentile → sell **half** of the DVOL convexity leg, redeploy into fresh convexity if DVOL stays elevated.
- **Reinvest into the core:** monetized proceeds go to **(a)** rebuying replacement overlay protection at distressed strikes, **(b)** scaling up the [[options-premium-selling|short-vol core]] at elevated DVOL percentile, or **(c)** [[buy-the-dip]] spot BTC/ETH. This is the [[barbell-portfolio|barbell alpha]].
- **Never sell the entire overlay.** A residual sleeve must always exist to protect against second-leg crashes (crypto cascades are frequently multi-leg — LUNA→3AC→FTX ran for months).

| Trigger | Condition | Action | Keep residual? |
|---|---|---|---|
| 1 — slow burn | BTC drawdown ≥ 15% in ≤ 30 days | Sell 1/3 of put ladder | Yes |
| 2 — acceleration | BTC drawdown ≥ 30% | Sell another 1/3 of put ladder | Yes (final third) |
| 3 — vol shock | [[dvol\|DVOL]] doubles / > 95th pctl | Sell 1/2 of DVOL convexity, redeploy | Yes |
| Reinvest | Realized overlay P/L > 0 | Rebuy protection at distressed strikes; scale core at high DVOL pctl; [[buy-the-dip\|buy the dip]] | — |

## Implementation pseudocode

```python
def long_vol_overlay_loop(book, market):
    nav = book.nav()
    target_annual_spend = nav * 0.03      # ~3% per year total (crypto-fatter)
    monthly_budget = target_annual_spend / 12
    put_share, dvol_share = 0.65, 0.35

    # 1. Roll/replace expiring tranches (Deribit BTC/ETH, linear puts)
    for tranche in book.overlay_tranches:
        if tranche.dte() <= 30 and tranche.is_otm():
            book.close(tranche)           # accept loss, roll
            book.open_new_tranche(tranche.kind, sized=monthly_budget * tranche.share)

    # 2. Monetization triggers
    btc_dd = market.btc_drawdown_30d()
    if btc_dd >= 0.15:
        book.partial_close_overlay(kind="btc_put", fraction=1/3, reason="trigger1")
    if btc_dd >= 0.30:
        book.partial_close_overlay(kind="btc_put", fraction=1/3, reason="trigger2")
    if market.dvol() >= 2 * market.dvol_entry() or market.dvol_pctl() > 0.95:
        book.partial_close_overlay(kind="dvol_convexity", fraction=0.5, reason="trigger3")
        book.redeploy_into_fresh_dvol_convexity()

    # 3. Reinvest monetized cash
    if book.realized_overlay_pnl_today() > 0:
        book.rebuy_overlay_at_post_shock_strikes()
        book.scale_up_short_vol_core_if_dvol_pctl_rich()

    # 4. Maintain residual overlay floor
    if book.overlay_vega() < book.core_short_vega() * 0.08:
        book.add_protection_to_floor()
```

## Payoff & Greeks

### Payoff sketch (overlay alone vs combined book)

```
P/L
  ^                          combined book (core + overlay)
  |     overlay alone   .........________________
  |          \         .       .'   <- core theta income (calm)
  |           \      .'      .'
0 +------------\---.'------.'-----------------------> BTC/ETH / DVOL move
  |  -premium   \.'     .'  ^ crossover: overlay starts paying
  |     (calm)   '.    /     in the left tail, capping drawdown
  |   short-vol   '.  /
  |   CORE ALONE    '/  <- naked core: deep, unbounded left-tail loss
  v
```

The overlay alone is the classic long-premium hockey stick: small constant bleed (premium) in calm regimes, large convex payoff in the left tail. The point of the page is the **combined** curve: the short-vol [[options-premium-selling|core]] supplies the positive carry that pays for the overlay's bleed, while the overlay truncates the core's catastrophic left tail. The result is a near-symmetric distribution whose [[geometric-mean|geometric return]] dominates the naked core. See [[long-vol-vs-short-vol]].

### Net-Greeks table (combined book: short-vol core + long-vol overlay)

| Greek | Core (short vol) | Overlay (long vol) | Net combined | Trading meaning |
|---|---|---|---|---|
| Delta | small, hedged on perp | small (puts) | ~0, actively managed | Roughly neutral; managed via [[delta-hedging]] on the Deribit perp |
| Gamma | **−** (large) | + | Slightly negative, **bounded** | Core is short gamma; overlay caps the gamma loss in a shock |
| Theta | **+** (income) | − | Net positive in calm | Core theta funds the overlay bleed |
| Vega | **−** (large) | + | Net negative, **bounded** | Target: overlay vega = 8-15% of core short vega (see [[vega-budgeting]]) |
| Skew exposure | sells skew (short tail) | buys skew (long tail) | Symmetrized | The whole point — convert negative skew to roughly symmetric |

Net exposure: **net short vol with a hard floor.** The overlay does not flip the book to net-long-vol; it caps how much the short-vol core can lose. In a DVOL 45 → 100 move the overlay is sized to offset 30-60% of core [[gamma]] loss while the core keeps its calm-regime carry.

## Indicators / data used

- Deribit BTC/ETH [[options-chain]] with greeks across 30-120 DTE.
- [[dvol|DVOL]] level, percentile, and term structure; vol-of-vol context.
- Portfolio-level [[gamma]], [[vega]], [[delta]] aggregations.
- Short-vol core position vega for sizing the overlay against it.
- [[skew-trading|skew]] surface to assess put-vs-put-spread cost-effectiveness.
- Drawdown tracker on BTC/ETH for monetization triggers.
- [[funding-rate]] + perp OI and liquidation feed — cascade early warning for the fast-fire leg.

## Example trade

*Illustrative — a $250K blended crypto account.*

- **Account:** $250,000.
- **Short-vol core:** 4 BTC 15-delta iron condors on Deribit, 35 DTE, ~$40/day theta, delta-hedged on the BTC perp.
- **Overlay (this page's scope):**
  - BTC put ladder: linear puts, 1 tranche per month, ~60 DTE, 18-20% OTM. Cost ~$400/month → $4,800/year (1.9% of NAV).
  - DVOL convexity leg: long-vega Deribit structure sized ~$250/month → $3,000/year (1.2% of NAV).
  - **Total overlay spend: ~$7,800/year = 3.1% of NAV.**
- **Calm-regime outcome:** core grosses ~$40/day = ~$10K/year theta; overlay bleeds -$7.8K/year. Net = **+$2.2K/year** before perp-hedge funding (which is a tailwind in positive-funding regimes).
- **Shock-regime outcome (illustrative, 2025-10-10-like cascade):**
  - Condor gamma loss on the day of the shock: ~$28,000 (would have been catastrophic naked; capped by the condors' long wings and this overlay).
  - BTC put ladder appreciation: ~$9,000 (puts were ~18% OTM going in, BTC gapped through them).
  - DVOL convexity appreciation: ~$11,000 (DVOL ~45 → 100+ intraday; the fast-fire leg paid in minutes).
  - Net portfolio loss: ~$8,000 = ~3% of account.
- **Recovery:** monetized overlay proceeds reinvested into elevated-DVOL condors 1-2 weeks later when vol normalizes, accelerating recovery.

## Performance characteristics

- **Stand-alone:** -2 to -4% per year expected return; Sharpe -0.5 to -1.0; max drawdown bounded at premium spent (frontmatter `expected_max_drawdown: 0.05`).
- **Combined book (core + overlay):** Sharpe rises from ~0.4-0.6 (naked core) to ~1.0-1.4 (combined); max drawdown drops from ~50-100% to ~15-30%; **geometric mean returns improve materially** even though arithmetic mean drops.
- **Best months:** vol shocks. The overlay can deliver +5 to +30% NAV gains during a single crypto shock, fully offsetting the core's gamma loss and often producing a small net positive month.
- **Hit rate:** roughly 5-10% of months profitable on a stand-alone basis; the other 90-95% are slow bleed.

## Capacity limits

- BTC/ETH put-ladder capacity is ample at retail and small-fund scale but bounded by Deribit's OTM depth (clean fills to ~$5-25M vega-notional front-month BTC; ETH thinner) — an overlay for a book much beyond ~$500M NAV must spread across strikes/tenors and use the Deribit block / Paradigm RFQ network (frontmatter `capacity_usd: 500000000`).
- The DVOL/fast-fire leg is tighter — DVOL futures and single-strike vega depth constrain large allocators.
- The overlay does NOT crowd the trade the way the [[options-premium-selling|short-vol core]] does — being long crypto puts is structurally uncrowded.
- **Single-venue capacity risk**: all protection sits on Deribit; there is no deep second venue to source or monetize convexity if Deribit is itself stressed.

## What kills this strategy

(Failures here mean "the overlay didn't do its job," not "the overlay lost money.")

1. **Slow bear market** — a multi-month grind down can fail to monetize the overlay because each month's puts expire near-the-money rather than deep ITM. Mitigant: longer-dated tranches, partial monetization.
2. **Vol-suppressed crash** — a managed sell-off with contained DVOL reduces the fast-fire leg's payoff. Mitigant: the put ladder is the primary protection; the DVOL leg is a complement.
3. **Premium drift** — in extended calm regimes the overlay becomes optically painful and managers cut it just before the cascade. Mitigant: written rules; never adjust overlay size discretionarily.
4. **Strike too far OTM** — 25%+ OTM puts are cheap but rarely pay enough to offset core losses on 20-30% drawdowns. Mitigant: strike at 15-25% OTM, accept the carry.
5. **Failure to monetize** — refusing to sell appreciated puts during a shock (waiting for "the bottom") lets the protection evaporate in a V-recovery. Mitigant: mechanical triggers above.
6. **Failure to redeploy** — monetized cash sitting in stablecoin through the recovery wastes the [[barbell-portfolio|barbell alpha]]. Mitigant: pre-defined redeployment ladder.
7. **Same-venue failure** — a Deribit outage/insolvency during the event neutralizes the overlay. Mitigant: keep a residual off-venue reserve; accept irreducible single-venue risk.

## Kill criteria

- **Overlay-attribution drag exceeding ~6% NAV per year for 24 consecutive months** → review sizing and strike selection (likely too far OTM or too short-dated).
- **A vol shock occurs in which the overlay covers <20% of core gamma loss** → the overlay was misspecified (wrong strikes, wrong tenor, or wrong sizing).
- **Trader violates monetization or sizing rules under stress** → halt the entire program until written rules are restored; discretionary management defeats the overlay.
- **Permanent change in crypto [[variance-risk-premium]]** that makes the core unprofitable → if the core is retired, the overlay is retired with it. The overlay only exists to protect a core book.

## Advantages

- **Caps the left tail** of a crypto short-vol book — the single most important risk control for Deribit premium sellers, where auto-liquidation is unforgiving.
- **Improves geometric returns** of the combined book despite negative stand-alone return.
- **Generates [[crisis-alpha|crisis alpha]]** — stablecoin exactly when crypto is cheapest and DVOL is rich, enabling [[buy-the-dip]] and rich-vol re-entry; crypto's frequent crashes give more such windows.
- **Capital-light** — premium paid is the only cost; no margin-call risk on the long legs.
- **Becomes more liquid in stress** — everyone wants the puts you own during a cascade.
- **Behaviorally enabling** — knowing the overlay is on lets the trader hold the core through a Deribit margin spike instead of panic-closing at the worst tick.

## Disadvantages

- **Persistent carry cost** of 2-4% NAV per year that hits P&L in 90-95% of months (fatter than the equity overlay).
- **Career-risk hostile** — explaining the overlay drag to allocators in calm crypto years requires institutional commitment.
- **Requires monetization discipline** — a poorly monetized overlay is nearly as bad as no overlay.
- **Strike and tenor sensitivity** — a misspecified overlay can cost the same premium and pay off far less when needed.
- **Same-venue and majors-only risk** — the protection lives on Deribit and is a BTC/ETH proxy for any alt exposure.
- **Not a stand-alone strategy** — divorced from a short-vol core, it is just slow-bleed insurance with no offsetting income.

## Getting the Data (CryptoDataAPI)

DVOL and the raw IV surface come from **Deribit** / [[greeks-live|Greeks.live]]. [[cryptodataapi|CryptoDataAPI]] supplies the vol-regime, dealer-gamma, funding, and liquidation context that drives the monetization triggers and sizing.

**Live data:**
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100); the fast-fire monetization gauge
- `GET /api/v1/volatility/regime` — per-asset vol regime (compressed / expanding / vol_shock / mean_reverting / normal)
- `GET /api/v1/market-intelligence/liquidations` — cross-exchange liquidations; a cascade in progress
- `GET /api/v1/quant/gex` — dealer gamma exposure (short-gamma dealers = cascade-prone)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — extreme funding flags a leveraged-long crowd vulnerable to a deleveraging cascade

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol-regime detail + 60-day history
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90` — OHLCV for the drawdown-tracker triggers
- `GET /api/v1/backtesting/klines` (REST bars start 2026-05-09; older 1h/4h/1d bars are in the `klines_deep` archive) — kline history to backtest overlay monetization across 2020-03/LUNA/FTX/2025-10-10

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/volatility/regime/score"
```

Auth: `X-API-Key` header. Full catalog on [[cryptodataapi]]; for DVOL index/history and the full surface use the Deribit API or [[greeks-live]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [gamma exposure](https://cryptodataapi.com/quant-gamma) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Monetisation triggers** — `GET /api/v1/volatility/regime/score` (the fast-fire gauge) + `GET /api/v1/market-intelligence/liquidations` (cascade in progress): fire the mechanical sell-1/3 ladder without the human hesitation that kills overlays; the drawdown tracker for Triggers 1-2 runs off `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=90`.
- **Roll timing** — `GET /api/v1/volatility/regime`: add monthly tranches in `compressed`/`normal` states when convexity is cheapest.
- **Cascade early warning** — `GET /api/v1/quant/gex` + `GET /api/v1/derivatives/funding-rates?coin=BTC`: short-gamma dealers plus extreme positive funding describe the leveraged crowd whose deleveraging the overlay monetises against.
- **Regime gate** — `GET /api/v1/quant/market`: a jump in `vol_spike` probability is the machine-readable analogue of "DVOL doubles from entry".
- **Backtest** — replay monetisation paths across 2020-03/LUNA/FTX/2025-10-10 on `GET /api/v1/backtesting/klines` (Binance 1h/4h/1d back to 2017-08 only in the `klines_deep` archive, while the REST route starts 2026-05-09) with point-in-time regimes from `GET /api/v1/quant/regimes/history` (hourly HMM probabilities since 2020, Parquet, Pro Plus); option premiums come from Deribit.
- **Tips** — this strategy is rules-not-forecasts: the agent's whole value is enforcing the written roll/monetisation/floor rules 24/7 — exactly the discretionary-drift failure mode ("premium drift", "failure to monetize") the page lists as its killers.

## Sources

- Spitznagel, Mark. *Safe Haven: Investing for Financial Storms* (2021) — the canonical case for convex overlays raising geometric returns (equity origin; framework transfers to crypto).
- Bhansali, Vineer. *Tail Risk Hedging* (2014) — practitioner ladder construction.
- Carr, Peter and Wu, Liuren. "Variance Risk Premiums" (2009) — VRP measurement.
- Deribit / [[greeks-live]] — DVOL, linear vs inverse puts, DVOL futures.
- Crypto vol-shock record: 2020-03-12 Black Thursday, 2022-05 LUNA, 2022-11 FTX, 2025-10-10 cascade (see [[liquidation-cascade-fade]]).

## Related

- [[long-vol-vs-short-vol]] — the parent comparison page
- [[long-volatility-strategies]] — the broader family of long-vol trades
- [[short-volatility-strategies]] / [[crypto-options-volatility-selling]] — the short-vol core this overlay protects
- [[dvol]] — the crypto vol benchmark and monetization trigger
- [[deribit]] / [[greeks-live]] — venue and analytics
- [[implied-volatility]] — the pricing input for every overlay leg
- [[sharpe-ratio]] — why stand-alone Sharpe is negative but blended Sharpe rises
- [[geometric-mean]] — the return measure the overlay actually optimizes
- [[options-premium-selling]] / [[premium-selling-systematic]] — the core implementations
- [[tail-risk-hedging]] — the stand-alone version of the overlay
- [[options-portfolio-construction]] — combining core and overlay
- [[vega-budgeting]] — formal sizing
- [[volatility-regime-classification]] — regime-conditional payoffs
- [[crisis-alpha]] — the broader concept the overlay implements
- [[funding-rate]] — the cascade early-warning input
- [[liquidation-cascade-fade]] — the crypto vol-shock case pages
