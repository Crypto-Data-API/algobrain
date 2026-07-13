---
title: "OI-Confirmed Trend (Hyperliquid Basket)"
type: strategy
created: 2026-06-16
updated: 2026-07-13
status: good
tags: [crypto, perpetuals, hyperliquid, algorithmic, trend-following, derivatives, quantitative, momentum]
aliases: ["Open Interest Trend Confirmation", "OI Trend Filter Basket", "Capital-Committed Trend Following", "OI-Momentum Basket"]
related: ["[[hyperliquid-baskets-overview]]", "[[derivatives-native-regime]]", "[[technical-structural-regime]]", "[[macro-trend-regime]]", "[[defensive-majors]]", "[[full-bear-short-book]]", "[[trend-pullback-rally-fade]]", "[[major-trend-reclaim-rejection]]", "[[oi-price-exhaustion]]", "[[crowded-short-funding-fade]]", "[[crowded-long-funding-fade]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[2025-03-jellyjelly-hlp-attack]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
strategy_type: algorithmic
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: pilot
edge_source: [behavioral, structural]
edge_mechanism: "Retail traders chase price on low-OI moves that mean-revert; genuine institutional or informed-money conviction is only observable when rising OI accompanies price — those moves persist, while OI-divergent moves fade, giving the OI filter a structural advantage over pure momentum."
data_required: [ohlcv, open-interest, perp-funding, liquidation-feed, order-book-depth]
min_capital_usd: 5000
capacity_usd: 150000000
crowding_risk: medium
expected_sharpe: 0.8
expected_max_drawdown: 0.25
breakeven_cost_bps: 35
kill_criteria: |
  - Basket drawdown > 25% on rolling 6-month basis
  - Rolling 6-month Sharpe < -0.3
  - Win rate on OI-confirmed signals drops below 40% over 30 consecutive signals (edge decay)
  - Any leg up 30%+ in under 2 hours on thin OI → cover immediately (squeeze guard)
  - Funding on any held position exceeds ±0.15%/8h for 5+ consecutive days → reassess position sizing
deploy_date: 2026-06-10
capital_allocation: "$2,375 active capital across 4 open positions as of 2026-06-16"
last_review: 2026-06-16
next_review: 2026-07-16
---

# OI-Confirmed Trend (Hyperliquid Basket)

> **Live status (2026-06-16 dashboard snapshot):** Most active basket in the trading system. 4 open positions, $2,375 allocated capital. Positions are directional (long or short) in assets where price movement was confirmed by a simultaneous OI increase at signal time.

The OI-Confirmed Trend basket enters trend-following positions — long or short — only when **price movement is confirmed by a simultaneous increase in Open Interest**. The logic is simple: rising price + rising OI signals genuine capital commitment backing the move (new longs entering); falling price + rising OI signals a genuine short trend (new shorts entering). Either pattern filters out noise moves driven by low-conviction covering or thin-book order flow, where OI stays flat or declines as price moves.

*Part of the [[hyperliquid-baskets-overview|Hyperliquid basket library]].*

## Edge Source

**Behavioral** + **structural** (see [[edge-taxonomy]]).

- **Behavioral** — in crypto perpetuals markets, a large proportion of price moves are driven by low-conviction flow: short-term covering, liquidation cascades, and thin-book moves that mean-revert quickly ([[mean-reversion]]). Retail participants chase these moves, entering on the breakout and stopping out on the reversion. The OI filter identifies the minority of moves where real capital is entering — those trends persist because they reflect genuine position build, not noise.
- **Structural** — [[open-interest]] is a Hyperliquid-native, publicly auditable signal. The protocol's transparent on-chain architecture makes OI data available in near-real-time with no third-party lag ([[hypurrscan]]). Other traders operate on delayed or synthesized data; a Hyperliquid-native data pipeline provides a timing advantage.

**Honest framing:** OI-confirmation is a widely known filter in crypto derivatives trading. The edge is real but not unique — many systematic traders apply similar filters. The advantage at small scale is disciplined execution and the ability to combine OI confirmation with the regime gate, funding carry analysis, and HL-native data that less integrated systems miss.

## Why This Edge Exists

1. **Most crypto price moves are noise.** In an asset class dominated by retail speculation, high leverage, and thin order books, the majority of intraday moves are mean-reverting. A pure momentum strategy applied without filtering is buying noise. OI-confirmation selects for the fraction of moves where informed or committed capital is actually entering the market.
2. **Capital commitment is observable.** Unlike equity markets where order flow is fragmented and dark, Hyperliquid perp OI is fully transparent and on-chain. A rising OI is a direct, unfakeable signal that new contracts are being opened — someone is putting capital behind the directional view.
3. **OI divergence predicts reversals.** Conversely, price moving up while OI falls (shorts covering) or price moving down while OI falls (longs closing) indicates a move with no fresh capital behind it — the classic exhaustion signal. These set up the [[oi-price-exhaustion]] basket's trades. OI-Confirmed Trend exploits the *positive* case; OI-Price Exhaustion exploits the *negative* case.
4. **Trend confirmation compound effect.** Once a OI-confirmed trend is established, the same capital commitment that created the move tends to hold through initial pullbacks (they averaged in, not just chased). This means the trend has more durability than noise moves, giving the position time to develop without being stopped out on micro-volatility.
5. **Counterparty:** pure-price momentum chasers who enter on moves without checking capital commitment; short-term mean-reversion traders who fade OI-confirmed trends prematurely; liquidation-driven forced exits from the prior trend direction.

## Null Hypothesis

Under no-edge conditions, the OI filter identifies coincidental correlation between new position opening and price direction — both driven by the same underlying momentum that would have worked anyway. A pure momentum strategy without OI confirmation performs identically (the filter adds no signal, only reduces frequency). The OI-confirmation is measuring noise correlation in thin markets rather than genuine informed capital.

**Disconfirming evidence to monitor:**
- Win rate on OI-confirmed long signals drops below 40% over 30 consecutive signals (filter has stopped working in the current regime).
- OI-confirmed moves revert on the same or next session more than 60% of the time (market structure has changed, possibly due to increased HFT presence or a regime shift).
- The spread between OI-confirmed and OI-divergent moves narrows to statistically insignificant difference (edge has been arbitraged away or markets have matured).
- Funding consistently opposes position direction by > 0.10%/8h (the crowd's capital commitment is in the opposite direction, suggesting the OI signal is being generated by a different cohort).

## Rules

**Universe.** All liquid Hyperliquid perps with > $20M in 24h volume and > $5M in open interest. Prioritise the top 20 by market cap when the macro regime is unclear; expand to top 50 when [[macro-trend-regime]] is clearly trending.

**OI-confirmation signal (long side):**
1. Price closes above a 4-hour ATR band (breakout from a consolidation structure or key level).
2. OI increases by ≥ 3% within the same 4-hour bar.
3. Funding rate is not deeply negative (< −0.08%/8h) — avoids entering a long that is already crowded on the short side.
4. [[derivatives-native-regime]] does not show fragility-triad alignment (if all three fragility signals are red, the trend move is likely a bear trap — skip).

**OI-confirmation signal (short side):**
1. Price closes below a 4-hour ATR band (breakdown from a consolidation structure or key level).
2. OI increases by ≥ 3% within the same 4-hour bar.
3. Funding rate is not deeply positive (> +0.10%/8h) — avoids entering a short into an already-crowded long-funding environment where a squeeze is likely.
4. Macro trend regime allows shorting (not in confirmed early-bull phase).

**Position sizing:**
- Base size: 2% of book per signal, scaled by signal strength (OI increase 3–5% = 1x, 5–10% = 1.25x, > 10% = 1.5x).
- Maximum concurrent exposure: 10% of book long, 10% of book short (can be both simultaneously on different assets).
- Leverage: 2–3x isolated margin per leg. Never exceed 3x.
- ATR-based stop: 1.5× [[average-true-range]] (14-period) from entry price.

**Exit / take-profit:**
- Primary: ATR trailing stop (1.5× ATR, recomputed each close).
- Secondary: if OI starts declining while the position is profitable (position-exit signal), take 50% off — the committed capital is leaving.
- Hard stop: 1.5× ATR from entry (invalidates the signal).

## Implementation Pseudocode

```python
OI_THRESHOLD_PCT = 0.03     # OI must rise ≥ 3% in the signal bar
LEVERAGE          = 2.5
MAX_BOOK_LONG     = 0.10
MAX_BOOK_SHORT    = 0.10
ATR_STOP_MULT     = 1.5
MIN_24H_VOL       = 20_000_000
MIN_OI            = 5_000_000

def oi_confirmed_trend(state, book_size):
    legs = []
    total_long_notional  = 0
    total_short_notional = 0

    for sym in state.universe:
        if hl_24h_volume(sym) < MIN_24H_VOL:
            continue
        if hl_open_interest(sym) < MIN_OI:
            continue

        price_change_4h = price_change(sym, "4h")
        oi_change_4h    = oi_change_pct(sym, "4h")
        funding         = perp_funding_8h(sym)
        atr14           = compute_atr(sym, 14)

        # --- Long signal ---
        if (price_change_4h > atr_band_breakout(sym, "up")
                and oi_change_4h >= OI_THRESHOLD_PCT
                and funding > -0.0008
                and not state.fragility_triad_red
                and total_long_notional < MAX_BOOK_LONG * book_size):
            size_mult = oi_size_multiplier(oi_change_4h)  # 1.0 / 1.25 / 1.5
            notional = book_size * 0.02 * size_mult
            legs.append(long_perp(sym,
                                   notional=notional,
                                   leverage=LEVERAGE,
                                   margin="isolated",
                                   stop_price=entry_price - ATR_STOP_MULT * atr14))
            total_long_notional += notional

        # --- Short signal ---
        elif (price_change_4h < atr_band_breakout(sym, "down")
                and oi_change_4h >= OI_THRESHOLD_PCT
                and funding < 0.0010
                and state.macro_trend_allows_short
                and total_short_notional < MAX_BOOK_SHORT * book_size):
            size_mult = oi_size_multiplier(oi_change_4h)
            notional = book_size * 0.02 * size_mult
            legs.append(short_perp(sym,
                                    notional=notional,
                                    leverage=LEVERAGE,
                                    margin="isolated",
                                    stop_price=entry_price + ATR_STOP_MULT * atr14))
            total_short_notional += notional

    # --- OI-exit: OI declining on profitable position → partial exit ---
    for leg in legs:
        if oi_change_pct(leg.symbol, "4h") < -0.02 and leg.unrealised_pnl > 0:
            leg.action = "take_50pct_profit"

    # --- JELLY guard: thin perp squeeze ---
    for leg in legs:
        if leg.adverse_pct > 0.30 and hl_24h_volume(leg.symbol) < 50_000_000:
            leg.action = "cover_immediately"

    # --- Kill switches ---
    if state.basket_drawdown_6m > 0.25 or state.rolling_6m_sharpe < -0.3:
        return []

    return legs
```

## Indicators / Data Used

- **[[open-interest]]** — the core signal. OI change within the signal bar is the primary filter; OI decline on a profitable position is the partial-exit signal. Source: [[hypurrscan]], [[coinglass]], Hyperliquid `metaAndAssetCtxs`.
- **[[average-true-range]] / [[atr-position-sizing]]** — 14-period ATR for stop placement (1.5× ATR) and breakout band calculation. Source: [[hyperliquid|Hyperliquid]] OHLCV feed.
- **[[funding-rate]]** — used as a sentiment guard: deeply negative funding means the crowd is short (don't add a long into a crowded short); deeply positive means the crowd is long (don't add a short into a crowded long). Source: [[hyperliquid-funding-rate-microstructure]].
- **[[derivatives-native-regime]]** — the fragility-triad check (crowded basis + OI vs depth + funding extreme) prevents entering a long in a pre-cascade environment where OI confirmation may reflect forced-long accumulation rather than genuine conviction.
- **[[technical-structural-regime]]** — ATR band breakouts as the price-trigger component of the dual signal.
- **[[liquidity-depth-regime]]** — order-book depth check ensures OI growth is not outrunning book depth (pre-cascade signature).

## Example Trade

**Illustrative — not a backtest.** Hypothetical long signal on SOL-PERP, mid-2026.

Setup: SOL-PERP has been consolidating between $130–$145 for 8 days. A 4-hour bar closes at $148 (breakout above $145 resistance). OI rises by 5.2% in the same bar ($420M → $441M). BTC macro trend is bullish. Funding: +0.02%/8h (mild positive, no squeeze concern). Fragility triad: not aligned.

| Parameter | Value |
|-----------|-------|
| Entry price | $148 |
| OI signal strength | 5.2% → size_mult 1.25x |
| Position notional | $2,500 (2% × 1.25 of $100K book) |
| Leverage | 2.5x |
| ATR (14-period) | $8 |
| Stop price | $148 − (1.5 × $8) = $136 |
| Target (illustrative) | $172 (50% Fib extension of the consolidation range) |

**Scenario A (thesis confirmed):** SOL trends to $172 over 12 days; OI stays elevated or grows. ATR trailing stop trails up. Exit at $168 (trailing stop hit). P&L: +$2,500 × (168-148)/148 × 2.5 = **+$845 (~34% on notional)**.

**Scenario B (signal fails):** SOL spikes to $151 then reverses; price hits stop at $136 on day 3. Loss: $2,500 × (148-136)/148 × 2.5 = **−$506 (~−20% on notional)**. Book loss: −0.5% of total.

*All figures illustrative. Not a backtest.*

## Performance Characteristics

- **Return shape:** moderate frequency (several trades per week across the universe), positive skew — wins larger than losses when the OI confirmation is correct, because the confirmed trends tend to run further than the noise-move reversals that hit stops.
- **Expected Sharpe (illustrative estimate):** ~0.7–0.9 net in trending regimes; falls toward 0 in range-bound choppy regimes where OI signals are generated but trends are short-lived.
- **Funding carry:** neutral to mildly positive on longs in bull regimes; can be mildly negative on shorts in early bear (retail longs persist). Funding is not a primary value driver for this basket — the trend is.
- **Max drawdown estimate:** ~20–25% in a choppy or trend-reversal environment where multiple OI-confirmed signals fail in sequence (false breakout cascade).
- **Realistic round-trip cost:** ~25–40 bps per trade (taker on stops, maker on entries), plus funding. High trade frequency relative to position baskets — cost control matters.
- **Regime sensitivity:** strong in trending [[macro-trend-regime]] conditions; weakens in [[volatility-regime-classification]] expansion (OI spikes from liquidations, not genuine capital commitment) and in range-bound [[technical-structural-regime]] phases.

## Capacity Limits

The strategy trades the top 20–50 Hyperliquid perps by liquidity. Most top-20 perps support $5–50M per position without meaningful market impact at 2.5x leverage. At small-account scale, capacity is entirely unconstrained. At fund scale ($10M+), the entry/exit orders need to be split across bars to avoid self-signalling. Strategy-level capacity estimate: **$150M** across a diversified universe before OI self-contamination (entering a position that itself generates the OI signal the strategy uses) becomes a concern.

## What Kills This Strategy

The most likely failure modes (see [[failure-modes]]):

1. **False breakout cascade.** In a choppy, range-bound regime, multiple "breakouts" occur that generate OI signals (shorts/longs entering the break) but reverse immediately. The ATR stops are hit repeatedly and the strategy grinds down. The [[derivatives-native-regime]] fragility check and the macro regime gate are the primary guards.
2. **OI signal noise in high-volatility periods.** During cascade events ([[2025-10-crypto-liquidation-cascade|Oct 2025 cascade]]), OI can spike from forced liquidation activity rather than genuine trend entry. The fragility-triad check should exclude these windows, but detection lag means some false signals fire.
3. **Funding opposition.** Entering a long into deeply negative funding (crowd is short, and they're winning) is the worst of both worlds — the trend hasn't started yet, and you're paying carry. The funding guard at −0.08%/8h is the gate.
4. **Crowding decay.** OI-confirmation is a well-known filter. As more systematic strategies adopt it, the filter's predictive power decays because more capital front-runs the signal, reducing post-signal drift.
5. **Thin-perp squeeze (JELLY pattern).** For mid-cap OI-confirmed signals in Tier C assets, a JELLY-style squeeze is the tail risk. Source: [[2025-03-jellyjelly-hlp-attack]]. Guard: only trade perps with > $20M/day volume.
6. **Regime mismatch.** Running this basket during a [[volatility-regime-classification|vol expansion]] or right after a [[security-black-swan-regime|black-swan shock]] when OI signals are driven by panic, not strategy — produces losses on every signal.

## Kill Criteria

See [[when-to-retire-a-strategy]]. Specific conditions:

- **Basket drawdown > 25%** from rolling 6-month peak → flatten and assess.
- **Rolling 6-month Sharpe < −0.3** → full review; default to flatten.
- **Win rate on OI-confirmed signals < 40% over 30 consecutive signals** → edge decay; suspend until regime conditions improve.
- **Any leg up > 30% in < 2 hours on thin volume** → cover immediately (JELLY guard).
- **Funding > ±0.15%/8h on any held position sustained 5+ days** → reduce that position by 50%; reassess.

## Advantages

- **Higher signal quality than pure momentum** — the OI filter eliminates the majority of noise moves that trip stop-losses in pure momentum strategies.
- **Bi-directional** — works in both bull and bear trends; not regime-dependent for direction, only for overall market structure.
- **Transparent, native data** — Hyperliquid's on-chain OI is the most reliable, low-latency OI data available in crypto. No third-party API lag.
- **Well-defined, auditable signal** — the dual-condition entry (price breakout + OI increase) is objectively testable and leaves minimal discretionary override.
- **Live and active** — already deployed with open positions; the pilot phase is generating real PnL data for calibration.

## Disadvantages

- **Reduced signal frequency** — the OI filter eliminates many trades, including some that would have worked. In strong momentum periods the strategy underperforms pure momentum.
- **Entry timing** — waiting for OI confirmation means entering *after* the initial move; by definition the best entry has already passed.
- **OI is a lagging confirmation** — OI updates on a block-by-block basis; in fast markets the signal may arrive late.
- **Crowding risk in popular assets** — high-profile assets (BTC, ETH) have many OI-watchers; the filter is less proprietary there.
- **False OI signals from liquidations** — during cascades, liquidations open forced new positions, generating OI signals that look like capital commitment but are actually mechanical.
- **Funding carry variable** — unlike a long-only position basket, this strategy can be paying funding on shorts or receiving on longs at any time; tracking the net carry across all legs adds operational complexity.

## Hyperliquid Execution Notes

- **Funding carry direction:** varies by position direction and market regime. Long positions in bull markets typically pay positive funding (cost); short positions in bear markets may earn positive funding. The funding guard at ±0.08–0.10%/8h prevents entering positions where the carry cost would dominate the trend P&L. Source: [[hyperliquid-funding-rate-microstructure]].
- **Single-mark-tick liquidation + ADL:** At 2.5x leverage, size positions so that the 1.5× ATR stop triggers at roughly 60% of the distance to liquidation. This gives a safety buffer even if the stop is gapped through on a fast move. ADL can deleverage winning positions during extreme moves; monitor the ADL queue indicator. Source: [[hyperliquid-liquidation-engine]].
- **Isolated margin:** each leg runs in isolation. An OI-false-signal on a Tier-C asset does not imperil the BTC/ETH legs. Cross-margin is prohibited.
- **JELLY-style thin-alt squeeze risk:** the $20M/24h volume gate is the primary guard. In addition, any leg that moves adversely > 30% in under 2 hours on thin volume should be covered immediately regardless of the fundamental view — the liquidation mechanics take over. Source: [[2025-03-jellyjelly-hlp-attack]].

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — OI-Confirmed Trend as a derivatives-native basket; the framework's use of OI as a capital-commitment confirmation signal.
- [[derivatives-native-regime]] — the regime that provides the fragility-triad gate for this basket.
- [[technical-structural-regime]] — the ATR-band breakout component of the entry signal.
- [[hyperliquid-funding-rate-microstructure]] — funding dynamics used in the sentiment guard.
- [[hyperliquid-liquidation-engine]] — liquidation mechanics driving sizing and stop placement.
- [[2025-03-jellyjelly-hlp-attack]] — thin-perp squeeze precedent; drives the JELLY guard.
- [[coinglass]], [[hypurrscan]] — OI data sources.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

## Related

[[hyperliquid-baskets-overview]] · [[trend-pullback-rally-fade]] · [[major-trend-reclaim-rejection]] · [[oi-price-exhaustion]] · [[crowded-short-funding-fade]] · [[crowded-long-funding-fade]] · [[funding-rate-harvest]] · [[range-mean-reversion]] · [[defensive-majors]] · [[full-bear-short-book]] · [[derivatives-native-regime]] · [[technical-structural-regime]] · [[macro-trend-regime]] · [[market-regime]] · [[trading-strategy-baskets]] · [[open-interest]] · [[funding-rate]] · [[perpetual-futures]] · [[liquidation]] · [[hyperliquid]] · [[average-true-range]] · [[atr-position-sizing]] · [[atr-trailing-stop]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-liquidation-engine]] · [[2025-03-jellyjelly-hlp-attack]] · [[edge-taxonomy]] · [[failure-modes]] · [[when-to-retire-a-strategy]]
