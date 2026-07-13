---
title: "Full Bear Short Book (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-06-20
status: good
tags: [crypto, perpetuals, hyperliquid, algorithmic, trend-following, risk-management, quantitative, derivatives, on-chain]
aliases: ["Full Bear Short Basket", "Confirmed Bear Short Book", "Crypto Bear Market Shorts", "Macro Downtrend Short Sleeve"]
related: ["[[hyperliquid-baskets-overview]]", "[[macro-trend-regime]]", "[[on-chain-regime]]", "[[derivatives-native-regime]]", "[[defensive-majors]]", "[[oi-confirmed-trend]]", "[[distribution-post-peak-short-book]]", "[[long-liquidation-cascade]]", "[[crowded-long-funding-fade]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[when-to-retire-a-strategy]]"]
strategy_type: algorithmic
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [structural, behavioral]
edge_mechanism: "In confirmed bear markets the structural tide is against leveraged longs — forced sellers (liquidations, token unlock pressure, ETF outflows) dominate; behavioural overconfidence among longs who 'buy the dip' provides sustained counterparty flow for disciplined shorts."
data_required: [ohlcv, perp-funding, open-interest, liquidation-feed, on-chain-exchange-inflows, token-unlocks, bitcoin-dominance-data]
min_capital_usd: 10000
capacity_usd: 100000000
crowding_risk: medium
expected_sharpe: 0.6
expected_max_drawdown: 0.40
breakeven_cost_bps: 40
kill_criteria: |
  - Basket drawdown > 40% on rolling 6-month basis
  - Rolling 6-month Sharpe < -0.5
  - Macro trend regime flips to "early bull" or "accumulation" and holds for 15+ days
  - Any short leg up > 30% in under 4 hours on thin volume → cover that leg immediately (JELLY guard)
  - Funding on core shorts (BTC/ETH) persistently < -0.10%/8h for 5+ days (crowd is short, squeeze risk elevated)
---

# Full Bear Short Book (Hyperliquid Basket)

> **Not investment advice** — this page documents the strategy design. Positioning decisions are downstream of the system's regime detection and live portfolio management.

A directional short-only [[trading-strategy-baskets|basket]] of [[hyperliquid|Hyperliquid]] [[perpetual-futures|perp]] positions, activated exclusively during **confirmed macro downtrends** — not corrections, not pullbacks, but full bear-market conditions characterised by sustained lower highs and lower lows, deteriorating on-chain fundamentals, and broad derivatives fragility. The basket opens short perpetual positions across a diversified universe of assets, ranging from major-caps to select mid-caps, with maximum allowable short exposure across the eligible universe. The "full" label is intentional: this is not a hedging sleeve — it is an aggressive directional bet that the bear trend continues. It is gated by the bear phase of the [[macro-trend-regime]] within the broader [[market-regime]] framework.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Structural** + **behavioral** (see [[edge-taxonomy]]).

- **Structural** — confirmed bear markets create persistent one-directional pressure: exchange inflows from fearful holders, token unlock schedules converting paper gains into sell pressure, liquidation cascades that amplify downside, and ETF outflow periods that remove the structural demand floor ([[institutional-flow-regime]]). The short sits downstream of all these flows.
- **Behavioral** — retail and under-informed leveraged longs display strong recency bias from prior bull phases, repeatedly "buying the dip" in a regime where dips do not recover. This creates a persistent counterparty who enters at every bounce and is flushed on the next leg down. Source: [[macro-trend-regime]], [[on-chain-regime]].

**Honest framing:** short-only strategies in crypto carry severe asymmetric squeeze risk. The edge is real in bear markets but the strategy has a wide tail on the upside — a sudden regime flip, a policy surprise ([[policy-shock-regime]]), or a short-squeeze cascade can inflict large drawdown rapidly. The regime gate is the critical component; running this basket in the wrong regime is the primary failure mode.

## Why This Edge Exists

1. **Forced sellers dominate bear markets.** Exchange inflows spike as holders seek liquidity; token unlock schedules (often sold by insiders into strength but accel on weakness) add supply; leveraged longs face liquidations that recursively push price lower. The short is paid by these flows. Source: [[on-chain-regime]], [[token-unlocks]].
2. **Derivatives fragility amplifies downside.** In confirmed bear phases, open interest remains elevated relative to book depth ([[liquidity-depth-regime]]) — every marginal seller moves price further than a liquid order book would allow. The [[2025-10-crypto-liquidation-cascade|October 2025 cascade]] demonstrated how OI overhanging thin depth creates mechanically guaranteed downside amplification.
3. **On-chain metrics lead and confirm.** Sustained exchange inflows, whale distribution, and declining active-address counts (all captured in [[on-chain-regime]]) provide leading confirmation of a bear phase before price fully reflects it. The basket enters with this wind at its back.
4. **Negative funding is often *not* crowded in early bear.** In the first leg of a bear market, retail longs persist (recency bias from the prior bull), keeping funding mildly positive for weeks — the short earns carry while price declines. Only in the capitulation phase does funding go deeply negative (the crowd finally catches on), which is the signal to reduce.
5. **Counterparty:** leveraged-long retail, "buy the dip" DCA-ers, under-informed token project teams who bid their own tokens into weakness, and any product (index, vault) with forced rebalancing that must buy falling assets.

## Null Hypothesis

Under no-edge conditions, bear-market shorts merely replicate the inverse of the market, without strategic alpha over a short [[bitcoin-cycle-regime|cycle short]]. The distribution of bear-market recoveries is fat-tailed: V-shaped reversals driven by regulatory clarity, institutional announcements, or macro shifts ([[policy-shock-regime]]) can produce 40–60% rallies within weeks. If the basket is still short during one of these, the drawdown mimics the squeeze loss, not an orderly stop.

**Disconfirming evidence to monitor:**
- BTC posts a higher high on weekly close — the macro bear structure is broken.
- On-chain exchange inflows reverse to sustained outflows for 3+ weeks (accumulation, not distribution).
- BTC/ETH funding on Hyperliquid goes deeply negative (< −0.10%/8h) for more than 5 days — the crowd is now short; squeeze risk is elevated and the edge is crowded out.
- A large policy catalyst (e.g., pro-crypto executive order, sovereign ETF approval) fires ([[policy-shock-regime]]); cover immediately.

## Rules

**Universe.** Three tiers of shorts:

| Tier | Assets | Rationale | Max leg leverage |
|------|--------|-----------|-----------------|
| **A — Majors** | BTC-PERP, ETH-PERP | Deepest liquidity; highest certainty of bear trend confirmation | 2–3x |
| **B — Large-cap alts** | SOL, BNB, XRP (verify HL listing + depth) | Strong beta to majors; faster to move in bear phase | 1.5–2x |
| **C — Mid-cap alts** | Select liquid perps with negative on-chain metrics + high OI relative to depth | Highest alpha potential; highest squeeze risk | 1–1.5x |

**Bear confirmation threshold (all must hold before activation):**
1. BTC prints lower highs and lower lows on the weekly chart for ≥ 3 consecutive weeks.
2. [[on-chain-regime]]: exchange inflows > 60-day median for ≥ 10 of the last 14 days.
3. [[derivatives-native-regime]]: aggregate OI flat or rising into falling price on at least 2 of the 3 tiers.
4. BTC dominance stable or rising (not a meme/speculative rotation that bypasses majors).

**Activation / sizing:**
- Activate Tier A at 5% of book per leg (10% total), 2x leverage.
- Activate Tier B at 3% per selected asset, 1.5x leverage.
- Tier C is optional and capped at 2% per name; skip any name where 24h volume on HL < $10M (JELLY guard).
- Total short book: 20–30% of portfolio notional.

**Entry:** Use limit orders; never market-sell into thin books. Enter during low-volatility hours (not during Asia open cascade windows where shorts are most frequently squeezed). Prefer entries at short-term bounces (pull back to prior broken support, now resistance) rather than chasing momentum.

**Exit / take-profit:**
- Primary: trail a stop at the most recent 10-day high of the perp mark price.
- On confirmed capitulation (OI drops sharply + funding hits deeply negative), take profit on 50% of the book — this is the distribution-to-panic transition, and the remaining downside is diminishing.
- On a [[policy-shock-regime|policy catalyst]] or BTC higher-weekly-high: exit all positions within the session.

**Stop-out:** If any individual leg moves against by > 20% (on an isolated margin basis), cover that leg immediately. Do not average down into a short squeeze.

## Implementation Pseudocode

```python
TIERS = {
    "A": [("BTC", 0.05, 2.5), ("ETH", 0.05, 2.5)],   # (symbol, book_fraction, leverage)
    "B": [("SOL", 0.03, 1.5), ("BNB", 0.03, 1.5)],
    "C": [],  # populated dynamically from screener
}
MAX_BOOK_FRACTION = 0.30

def bear_confirmation(state) -> bool:
    return (
        state.btc_lower_highs_lower_lows_weekly >= 3
        and state.exchange_inflows_elevated_days_14d >= 10
        and state.oi_rising_into_falling_price_tiers >= 2
        and state.btc_dominance_trend != "falling"
    )

def full_bear_short_book(state, book_size):
    if not bear_confirmation(state):
        return []  # basket inactive

    legs = []
    total_notional = 0

    for tier, assets in TIERS.items():
        for (sym, frac, lev) in assets:
            if tier == "C":
                # JELLY guard: skip thin perps
                if hl_24h_volume(sym) < 10_000_000:
                    continue
            if total_notional / book_size >= MAX_BOOK_FRACTION:
                break
            # Crowd check: don't short if funding deeply negative (crowded)
            funding_8h = perp_funding_8h(sym)
            if funding_8h < -0.0010:  # < -0.10%/8h
                continue  # skip: crowd is short, squeeze risk dominates
            notional = book_size * frac
            legs.append(short_perp(sym,
                                    notional=notional,
                                    leverage=lev,
                                    margin="isolated",
                                    entry_type="limit_near_resistance"))
            total_notional += notional

    # --- Trailing stop: 10-day high mark price ---
    for leg in legs:
        leg.stop = rolling_max(mark_price(leg.symbol), 10, "days")

    # --- Capitulation de-risk ---
    if state.funding_deeply_negative_days >= 3 and state.oi_drop_pct > 0.15:
        legs = [resize(l, l.notional * 0.50) for l in legs]

    # --- JELLY guard: immediate cover if leg squeezes ---
    for leg in legs:
        if leg.pnl_pct > 0.30 and hl_24h_volume(leg.symbol) < 50_000_000:
            leg.action = "cover_immediately"

    # --- Kill switches ---
    if state.basket_drawdown_6m > 0.40 or state.rolling_6m_sharpe < -0.5:
        return []  # flatten

    return legs
```

## Indicators / Data Used

- **[[open-interest]]** — aggregate OI rising into falling price is the core bear-confirmation signal across all tiers. Source: [[coinglass]], [[hypurrscan]].
- **[[on-chain-regime]]** signals: exchange inflows (Tier 1 bear gate), whale wallet activity, active-address trend. Source: [[cryptoquant]].
- **[[funding-rate]]** — carried as a tailwind (positive funding = longs pay shorts) in early bear; flipping deeply negative is the crowd-crowded exit signal. Source: [[hyperliquid-funding-rate-microstructure]].
- **[[token-unlocks]]** — upcoming unlock schedules on Tier B/C assets accelerate sell pressure; use as a supplementary timing tool for entry.
- **Liquidation feed** ([[liquidation]] / [[long-liquidation]]) — liquidation clusters signal regime acceleration; cascade windows are both trading opportunities and risks for open shorts (volatility spike can briefly push against the position before continuing).
- **[[bitcoin-dominance-rotation]]** — stable or rising dominance confirms the bear is macro, not a simple altcoin rotation.
- **[[200-day-moving-average]]** — BTC sustained below the 200-day MA is a necessary (not sufficient) condition for the bear confirmation gate.
- **[[atr-trailing-stop]]** — the 10-day rolling high stop is an ATR-adjacent measure of recent volatility relative to trend.

**Data-feed mapping (cryptodataapi.com).** The Hyperliquid execution layer — per-tier perp [[funding-rate]] (incl. `predictedFundings`), [[open-interest]], mark price, 24h volume (the JELLY/thin-perp guards), and the liquidation feed — is read from cryptodataapi.com's Hyperliquid endpoints. On-chain exchange inflows and whale-distribution signals come from [[cryptoquant]]; cross-venue OI/funding context from [[coinglass]]/[[hypurrscan]]; the regime gate (weekly lower-highs/lower-lows, BTC dominance) is computed from price data. cryptodataapi supplies the venue carry/OI/liquidation context on which each short leg is sized and monitored.

## Example Trade

**Illustrative — not a backtest.** Setup: June 2026. BTC has printed 4 consecutive weekly lower highs after breaking below $58K; exchange inflows have been above the 60-day median for 12 of the last 14 days; OI is flat-to-rising despite falling price. [[on-chain-regime]] confirms whale distribution. Bear confirmation gate: ACTIVE.

| Leg | Notional | Leverage | Entry (approx) | Hypothetical 6-wk exit | P&L |
|-----|----------|----------|----------------|------------------------|-----|
| BTC-PERP short | $50,000 | 2.5x | $58,000 | $42,000 (−28%) | +$14,000 |
| ETH-PERP short | $50,000 | 2.5x | $2,200 | $1,540 (−30%) | +$15,000 |
| SOL-PERP short | $30,000 | 1.5x | $110 | $72 (−35%) | +$10,500 |
| Funding earned (positive avg 0.02%/8h) | — | — | — | — | +$1,200 |
| Fees + slippage | — | — | — | — | −$900 |
| **Total** (on $130K deployed) | | | | | **+$39,800 (~31%)** |

**Counter-example (regime flip):** A surprise pro-crypto executive order fires mid-position ([[policy-shock-regime]]); BTC rallies 22% in 48h. If the stop (10-day mark high) is hit and the position is covered at −18% on BTC (−45% on 2.5x leverage) with slippage: loss ≈ −$22K on the BTC leg alone. This is the kill condition — cover immediately, do not average in.

*All figures illustrative. Not a backtest.*

## Performance Characteristics

- **Return shape:** lumpy and directional — large gains when the bear regime persists; sharp losses during bear-market rallies or regime flips.
- **Expected Sharpe (illustrative estimate):** ~0.5–0.7 net during confirmed bear regimes; negative outside those regimes (which is why the gate is the critical component).
- **Funding carry:** typically positive in early bear (longs pay); turns negative in capitulation (adds cost to the short). The net carry over a 3–6 month bear phase is usually mildly positive.
- **Max drawdown estimate:** ~35–40% on a sharp V-shaped reversal or policy shock, the majority driven by leverage. Isolated margin per leg prevents total blowup.
- **Win condition:** sustained macro downtrend. The basket's expected value is near zero or slightly negative in range/accumulation regimes — it must be inactive then.
- **Realistic round-trip cost:** 25–50 bps per leg per trade (maker fees on entries, taker on stops, slippage on Tier C).

## Capacity Limits

BTC-PERP and ETH-PERP on Hyperliquid absorb hundreds of millions in short notional without meaningful impact. Tier B (SOL, BNB) supports $10–50M per name. Tier C mid-cap perps can become illiquid in downtrends — liquidity withdraws precisely when the basket tries to scale; practical Tier-C capacity is $2–5M per name before slippage becomes prohibitive. Strategy-level capacity estimate: **$100M** on a diversified Tier A/B book; Tier C is capped at ~$10M across all names.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **Regime flip — the primary risk.** A V-shaped reversal (surprise positive catalyst: ETF approval, sovereign accumulation, rate cut) ends the bear regime abruptly while the basket is at maximum short exposure. Mitigant: the 10-day-high trailing stop and the immediate-cover kill on any policy catalyst.
2. **Short squeeze on Tier C (JELLY pattern).** A coordinated spot bid or listing-driven bid pumps a thin mid-cap perp 30–50% in hours, liquidates the short via HLP, and may trigger a governance delist. Source: [[2025-03-jellyjelly-hlp-attack]]. Mitigant: strict JELLY guard (skip names < $10M/day volume), 1–1.5x leverage, isolated margin, immediate cover if leg up > 30% in 4h.
3. **Crowded short + squeeze.** If the crowd also catches on to the bear thesis, funding goes deeply negative — now the short pays carry AND risks being squeezed when any bid appears. The "skip if funding < −0.10%/8h" rule is the primary guard.
4. **Bear rally timing.** Even in confirmed bear markets, 20–40% rallies occur over weeks. The trailing stop will be triggered; re-entry after the rally fades requires patience and discipline to avoid over-trading.
5. **Correlation breakdown.** In a broad crypto cascade, correlations spike toward 1.0 and diversification across Tier B/C fails — all names move together and offer no diversification benefit, only additional liquidation risk.
6. **On-chain signal lag.** Exchange inflows and whale data are typically 1–4 hours delayed; the basket enters on confirmed signals, not predictions, which means some early-move alpha is sacrificed.

## Kill Criteria

See [[when-to-retire-a-strategy]] for the general framework. Specific numeric conditions:

- **Basket drawdown > 40%** from rolling 6-month peak → flatten and reassess.
- **Rolling 6-month Sharpe < −0.5** → full review; default to flatten.
- **Macro trend regime flips** to "early bull" or "accumulation" sustained ≥ 15 trading days → basket deactivated; hand-off to [[defensive-majors]].
- **Any Tier-C leg up > 30% in < 4 hours on thin volume** → cover that leg immediately (JELLY guard).
- **BTC/ETH funding < −0.10%/8h sustained for 5+ days** → crowd is short; squeeze risk dominates; reduce to 25% of target sizing or exit.

## Advantages

- **Trend alignment** — in a confirmed bear market, the strategy trades in the direction of the dominant structural flow (forced sellers, liquidation cascades, ETF outflows).
- **Positive carry in early bear** — positive funding means longs pay shorts to wait; the basket earns while the thesis plays out, unlike equity short positions that bleed borrow costs.
- **Transparent Hyperliquid data** — HL's on-chain OI, leverage, and liquidation distributions allow real-time crowding assessment unavailable on most traditional venues. Source: [[hyperliquid-vault-architecture]].
- **Diversification across tiers** — Tier A provides stability and deep liquidity; Tier C provides high-beta convexity on the downside.
- **Well-defined activation gate** — the multi-signal bear confirmation prevents the basket from firing in mere corrections, the most common failure mode of short-only strategies.

## Disadvantages

- **Catastrophic squeeze risk** — the primary failure mode is fast and painful; isolated margin helps but does not eliminate cross-contagion from panic covering.
- **Crowding at capitulation** — by the time the bear is unambiguous, everyone is short; the edge has decayed and the next move is likely a squeeze.
- **Re-entry difficulty** — bear-market rallies (dead-cat bounces) can be violent (20–40%); the trailing stop forces covers that must be re-established, adding frictional costs.
- **Regime detection lag** — no regime detector is real-time; the basket is always entering a bear that is already somewhat old.
- **Negative funding in late bear** — near capitulation, deeply negative funding inverts the carry advantage.
- **Regulatory / venue risk** — Hyperliquid governance has intervened to force-settle positions in extreme scenarios ([[2025-03-jellyjelly-hlp-attack]]); shorts are not immune to venue-level intervention.

## Hyperliquid Execution Notes

- **Funding carry direction:** Typically positive (longs pay shorts) in early-to-mid bear phases; inverts in capitulation. Monitor via `predictedFundings` and adjust Tier B/C sizing to reduce carry exposure when deeply negative. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** At 2.5x leverage, a 40% adverse move reaches liquidation. Size positions such that the 10-day-high stop is triggered first (typically at 15–25% adverse). ADL can deleverage winning legs in a cascade; monitor the ADL queue indicator on the HL interface. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** Non-negotiable on this basket. A JELLY-style squeeze on one Tier C name must not cascade to the BTC/ETH legs. Cross-margin is prohibited here.
- **JELLY-style thin-alt squeeze risk:** The canonical risk for Tier C shorts. The JELLY incident (March 2025) showed a thin perp can be pumped 400% in under an hour via coordinated spot buys, forcing HLP to absorb the short at a massive loss and triggering governance delisting at a flat price. Source: [[2025-03-jellyjelly-hlp-attack]]. Mitigants: 24h volume > $10M gate, 1x leverage only on Tier C, isolated margin, immediate-cover trigger at +30% in 4h.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Full Bear Short Book as a primary strategy in the macro-trend-regime bear phase; provides the multi-signal activation framework.
- [[macro-trend-regime]] — the backdrop regime that gates this basket.
- [[on-chain-regime]] — exchange inflow and whale distribution signals used in the bear confirmation gate.
- [[derivatives-native-regime]] — OI-into-falling-price as the derivatives confirmation leg of the gate.
- [[2025-10-crypto-liquidation-cascade]] — empirical bear-cascade example; demonstrates OI-vs-depth amplification in downtrends.
- [[hyperliquid-funding-rate-microstructure]] — funding mechanics; carry direction management.
- [[hyperliquid-liquidation-engine]] — single-tick liquidation, ADL queue; informs leverage ceilings.
- [[2025-03-jellyjelly-hlp-attack]] — the thin-perp short-squeeze precedent; drives the JELLY guard design.
- [[token-unlocks]] — supplementary timing tool for Tier B/C entry.

## Related

[[hyperliquid-baskets-overview]] · [[trading-strategy-baskets]] · [[hyperliquid]] · [[perpetual-futures]] · [[market-regime]] · [[defensive-majors]] · [[distribution-post-peak-short-book]] · [[oi-confirmed-trend]] · [[long-liquidation-cascade]] · [[crowded-long-funding-fade]] · [[etf-and-institutional-flow]] · [[global-liquidity-expansion-contraction]] · [[macro-trend-regime]] · [[on-chain-regime]] · [[derivatives-native-regime]] · [[institutional-flow-regime]] · [[policy-shock-regime]] · [[token-unlocks]] · [[liquidation-cascade-fade]] · [[funding-rate]] · [[open-interest]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[2025-03-jellyjelly-hlp-attack]] · [[2025-10-crypto-liquidation-cascade]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
