---
title: "Low-Leverage Vol Selling"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, options, volatility, derivatives, open-interest, funding-rate, risk-management, behavioral-finance, quantitative, crypto, bitcoin, ethereum]
aliases: ["Deleveraged-State Vol Selling", "Structural-Leverage-Absent Short Vol", "Zero-Cascade-Fuel Vol Entry", "Clean-Book Vol Selling"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, risk-bearing]
edge_mechanism: "The vol-seller's dominant risk is a cascade that cannot be stopped once it begins; structural cascade fuel (elevated OI/market-cap, stretched funding, one-sided long positioning) is the necessary precondition for unstoppable cascades; by entering short-vol ONLY when all three structural-leverage indicators are simultaneously LOW — OI/MC below threshold, funding flat, long/short ratio balanced — the seller operates exclusively in the state where the leverage-fuelled tail risk is structurally absent, making the VRP harvestable without the overlay of crash-from-leverage."

data_required: [open-interest, funding-rates, long-short-ratio, dvol-history, realized-vol-calc, options-chain, market-cap, ohlcv-daily]
min_capital_usd: 25000
capacity_usd: 150000000
crowding_risk: medium

expected_sharpe: 1.1
expected_max_drawdown: 0.28
breakeven_cost_bps: 60

decay_evidence: "Short-vol strategies in crypto have been compressed by covered-call vault proliferation (Ribbon/Aevo, Deribit auction flow, Lyra vaults) and systematic short-vol funds. The leverage-state filter is a subset that has not been widely adopted; the idea of gating on structural leverage absence rather than IV richness alone is novel. The structural basis — that low-leverage states precondition lower crash probability — is supported by the OI/market-cap literature and the BIS leverage-buildup framework. This gate narrows the entry window, reducing competition for the same post-entry vol-sell positions."

kill_criteria: |
  - DVOL rises > 50% in a single session after entry (standard vol-selling circuit breaker; exit immediately)
  - sleeve drawdown > 28% from high-water mark
  - a cascade occurs within 5 days of entry where OI/MC was confirmed below threshold at entry (the leverage-absent gate is being invalidated — cascades are occurring without leverage pre-buildup; recalibrate thresholds or retire)
  - realized vol exceeds DVOL for 15+ consecutive days after entry (structural VRP inversion; IV surface under-pricing RV; short vol is systematically losing)
  - rolling 8-event P&L negative across all 8 consecutive events where all three structural gates were simultaneously LOW (the clean-book gate is not producing a positive-expectancy window)

related: ["[[crypto-options-volatility-selling]]", "[[funding-conditioned-vol-selling]]", "[[post-panic-vol-selling]]", "[[trend-aligned-premium-selling]]", "[[leverage-stress-tail-hedge]]", "[[funding-flush-reversal]]", "[[oi-flush-reversion]]", "[[short-volatility-strategies]]", "[[deribit]]", "[[dvol]]", "[[implied-volatility]]", "[[variance-risk-premium]]", "[[open-interest]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Low-Leverage Vol Selling

Low-leverage vol selling enters a short-vol position (selling BTC or ETH options on [[deribit]]) **only when the structural preconditions for a leverage-fuelled cascade are simultaneously absent**: OI/market-cap is below a threshold (no excess leverage accumulated in perps), 8h funding is within a flat band (neither crowded longs nor panic shorts), and the long/short ratio is balanced (no one-sided positioning). The strategy is the **structural inverse of [[leverage-stress-tail-hedge]]**: while that page buys puts specifically when the three leverage-stress gates are simultaneously elevated, this page sells vol specifically when those same three gates are simultaneously low — in the state where the fuel for an unstoppable cascade is structurally absent.

**This is explicitly differentiated from [[crypto-options-volatility-selling]]** — that page's entry gate is a DVOL-percentile filter (IV elevated relative to the trailing year) applied continuously; it does not gate on the structural leverage state. It can enter short-vol at any time IV is elevated, including during high-OI, high-funding stress windows when cascade risk is elevated. This page adds the structural gate as a **prerequisite**: the IV must be elevated (same VRP logic) AND the leverage state must be clean (no cascade fuel).

**This is differentiated from [[funding-conditioned-vol-selling]]** — that page enters short-vol when elevated perp funding (≥ 0.03%/8h) confirms a crowded-long regime driving IV richness — a HIGH-leverage, HIGH-funding entry. This page enters short-vol when funding is FLAT (not crowded in either direction) — a LOW-leverage, NEUTRAL-funding entry. The two strategies occupy opposite ends of the funding spectrum: funding-conditioned vol selling exploits the crowded-long richness premium; this page exploits the clean-book vol-selling window when there is no directional crowd at all.

**This is differentiated from [[post-panic-vol-selling]]** — that page enters after a panic event (Fear & Greed ≤ 20, DVOL spiked, realized vol rolling over) — a specific event-triggered entry. This page is not triggered by a specific event; it is triggered by a structural leverage state. The two strategies are time-regime opposites: post-panic vol selling enters in the aftermath of a crash; low-leverage vol selling enters in the quiet, clean-book regime that precedes any major event.

**This is differentiated from [[trend-aligned-premium-selling]]** — that page selects which wing to sell (puts in uptrends, calls in downtrends) based on trend confirmation. This page makes no wing selection based on trend; it gates on the structural leverage state and sells strangles (both wings) in the deleveraged regime. Trend alignment and leverage-state can be combined as independent gates; they are not redundant.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + risk-bearing**:

- **Behavioral (primary)** — the [[variance-risk-premium|VRP]] in crypto options is persistently positive: IV exceeds subsequent realized vol on average across all regimes. The vol-seller harvests this VRP. The leverage-state gate restricts entry to the regime where this VRP is harvestable without the left-tail catastrophe that kills the strategy.
- **Structural** — leverage metrics (OI/market-cap, funding, long/short ratio) are leading indicators of cascade potential. In the low-leverage state, the structural preconditions for an unstoppable cascade are absent: there is no large pool of leveraged longs to liquidate, no crowded position book to cascade, and no excess funding payments creating carry-driven position buildup. The cascade tail risk is structurally lower in this state.
- **Risk-bearing** — the vol-seller in the low-leverage state is bearing the residual realized-vol risk (the market can still move; it just cannot cascade from leverage). The premium earned is the compensation for that residual risk. In the low-leverage state, the risk-bearing is more purely VRP harvesting and less leveraged-crowd-implosion insurance.

## Why this edge exists

**The key insight: leverage is the necessary precondition for catastrophic vol-selling losses.**

The vol-seller's catastrophic scenario is not any large price move — it is a **cascade**: a rapid, self-reinforcing move driven by leveraged liquidations that creates a gap-fill that cannot be managed. Review the evidence:
- May 2021: BTC −35% in 1 day. OI/MC was at ~4% at peak (excessive leverage). Funding had been 0.10–0.20%/8h (crowded longs). The vol-seller was destroyed by the cascade, not by a rational price discovery move.
- November 2022 (FTX): BTC −25% in days. Leverage and contagion, not natural price discovery.
- In contrast, many 8–15% corrective moves in 2024 occurred in low-OI, flat-funding environments — regular price discovery moves that the vol-seller managed through normal delta-hedging.

**The low-leverage gate separates these two regimes:**

1. **Low OI/market-cap means fewer positions to liquidate.** When OI/market-cap is below the cascade threshold, there is simply less fuel for forced selling. A 5% price decline in a low-leverage regime causes proportionally small liquidations; the same 5% decline in a high-leverage regime triggers a liquidation cascade that accelerates the move.

2. **Flat funding means no one-sided crowd to unwind.** When funding is flat (neither crowded longs nor panic shorts), there is no structural imbalance in the position book. The vol-seller in this state faces mean-reverting noise, not directional crowd explosions.

3. **Balanced long/short ratio means no clear squeeze or cascade direction.** When longs and shorts are balanced, neither a squeeze nor a cascade can create a reinforcing loop; the position book is balanced.

**Who is on the other side:** the options buyer in the low-leverage state is not an emergency put-buyer (that's post-panic) nor a speculative crowded-long call-buyer (that's funding-conditioned). In the low-leverage regime, the option buyer is more likely a tactical hedger, a delta-hedging market-maker, or a speculative buyer with no particularly strong directional information. The vol-seller earns the VRP without facing a structurally-informed counterparty.

## Null hypothesis

Under the null, the leverage-state gate adds **no incremental Sharpe improvement** over the DVOL-percentile gate alone:
- Short-vol positions entered when DVOL is elevated AND all three leverage metrics are low should not produce higher P&L than positions entered on DVOL elevation alone.
- The low-leverage state should not predict lower subsequent realized vol or lower cascade probability relative to the high-leverage state at the same DVOL level.
- The tighter entry gate (fewer signals) should not improve win rate enough to compensate for the reduced signal frequency.

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all BTC options vol-selling windows (e.g., DVOL ≥ 50th percentile); split by leverage state (OI/MC above vs below 2.5%); compare the subsequent realized vol, the occurrence of cascades, and the P&L of short strangles. Predict: low-leverage-state entries show 30–50% lower cascade frequency and measurably lower maximum drawdown.

## Rules

### Entry gate (all four conditions must be simultaneously confirmed)

**Gate 1: Structural leverage is absent — OI/market-cap LOW**
- BTC OI/market-cap ≤ **2.0%** (deleveraged state; well below the 3.0% [[leverage-stress-tail-hedge]] stress trigger).
- Source: OI from `GET /api/v1/derivatives/open-interest?coin=BTC`; market cap from `GET /api/v1/coins/BTC` or equivalent.
- *Rationale:* 2.0% is the "clean book" threshold; historically, cascades of ≥ 10% in 24h have been heavily concentrated in windows when OI/MC was above 2.5–3.0%. Below 2.0%, the structural cascade fuel is minimal.

**Gate 2: Funding is flat — no directional crowding**
- 8h funding rate is between **−0.01%** and **+0.02%/8h** (neither panic-short nor crowded-long).
- 7-day average funding is between **−0.005%** and **+0.015%/8h**.
- Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.
- *Rationale:* flat funding means neither directional extreme. Below −0.01% is the beginning of a panic-short regime; above +0.02% begins the crowded-long territory that [[funding-conditioned-vol-selling]] targets separately. This page targets the neutral zone.

**Gate 3: Long/short ratio is balanced**
- Long/short ratio is between **0.9** and **1.2** (neither heavily short- nor long-biased).
- Source: `GET /api/v1/derivatives/binance/long-short-ratio`.
- *Rationale:* a balanced long/short ratio confirms that neither a squeeze nor a cascade has a one-sided inventory book ready to amplify. This is the derivative-positioning counterpart of the OI/MC check.

**Gate 4: IV is elevated enough to justify the trade (VRP present)**
- DVOL ≥ **45th percentile** of its trailing 52-week distribution (options are not in the cheapest regime; there is a premium to sell).
- IV − 20-day realised vol ≥ **5 vol points** (the VRP spread is present and meaningful).
- Source: `GET /api/v1/market-intelligence/dvol-history`; RV computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200`.
- *Rationale:* the lower DVOL percentile threshold (45th vs the 40th–90th in [[crypto-options-volatility-selling]]) reflects that in the low-leverage state, even modest IV richness is harvestable because the catastrophic left tail has been filtered out. The IV−RV spread requirement ensures there is a real premium to capture.

### Instrument selection

- **Primary:** short BTC strangle — sell 25-delta put AND 15-delta call, nearest monthly expiry with DTE 21–35 days. In the low-leverage, neutral-regime state, the put-to-call skew is modest (no directional fear or greed premium), making the strangle more symmetric than in other regimes.
- **Delta hedge:** delta-neutral within ±5 delta per unit notional; hedge daily unless spot moves > 2.5% intraday.
- **Avoid front-week:** same as all vol-selling pages — gamma risk in short-dated options can exceed the premium collected.

### Position sizing and exit

- **Size:** premium collected = 1.5–2.5% of portfolio per entry. Maximum one active low-leverage vol position at a time.
- **Profit exit:** close when DVOL falls back to within **3 vol points** of its 30-day trailing average (IV normalisation complete) or at 80% of maximum theoretical premium decay.
- **Stop:** close if DVOL rises ≥ **20 vol points** above entry level (unexpected vol expansion; the structural guarantee has failed).
- **Leverage-state breach exit:** close immediately if OI/market-cap rises above **2.8%** while the position is open (structural leverage is rebuilding; exit before cascade fuel accumulates to dangerous levels).
- **Time exit:** close at expiry −3 days.

## Implementation pseudocode

```python
# low_leverage_vol_selling.py

from dataclasses import dataclass
from typing import Optional

# ---- entry gates ----
OI_MC_MAX_CLEAN            = 0.020   # OI/market-cap <= 2.0% (deleveraged)
FUNDING_8H_MIN             = -0.0001 # funding >= -0.01%/8h
FUNDING_8H_MAX             = +0.0002 # funding <= +0.02%/8h
FUNDING_7D_AVG_MIN         = -0.00005
FUNDING_7D_AVG_MAX         = +0.00015
LONG_SHORT_MIN             = 0.90    # long/short >= 0.90 (not too short-biased)
LONG_SHORT_MAX             = 1.20    # long/short <= 1.20 (not too long-biased)
DVOL_PERCENTILE_MIN        = 45.0    # DVOL >= 45th percentile (IV present to harvest)
IV_RV_SPREAD_MIN           = 5.0     # IV - 20d RV >= 5 vol points

# ---- exit thresholds ----
DVOL_PROFIT_WITHIN_VOLS    = 3.0     # close at profit when DVOL within 3 vol pts of 30d avg
DVOL_STOP_ABOVE_ENTRY      = 20.0    # stop: DVOL +20 vol pts above entry
OI_MC_EXIT_HIGH            = 0.028   # exit if OI/MC rises above 2.8% (leverage rebuilding)
DTE_TIME_EXIT              = 3

@dataclass
class MarketState:
    oi_mc_ratio:          float   # OI / market-cap (e.g. 0.018 = 1.8%)
    funding_8h:           float
    funding_7d_avg:       float
    long_short_ratio:     float
    dvol_current:         float
    dvol_percentile_52w:  float
    dvol_30d_avg:         float
    iv_rv_spread:         float   # DVOL - 20d realized vol (vol points)

@dataclass
class ShortVolPosition:
    entry_dvol:           float
    entry_oi_mc:          float
    current_dvol:         float
    current_oi_mc:        float
    dvol_30d_avg:         float
    dte:                  int

def all_gates_pass(s: MarketState) -> tuple[bool, list[str]]:
    fails = []
    if s.oi_mc_ratio > OI_MC_MAX_CLEAN:
        fails.append(f"OI/MC {s.oi_mc_ratio:.2%} > clean threshold {OI_MC_MAX_CLEAN:.2%} — leverage present")
    funding_ok = (FUNDING_8H_MIN <= s.funding_8h <= FUNDING_8H_MAX
                  and FUNDING_7D_AVG_MIN <= s.funding_7d_avg <= FUNDING_7D_AVG_MAX)
    if not funding_ok:
        fails.append(f"funding {s.funding_8h:.4%}/8h outside flat band [{FUNDING_8H_MIN:.4%}, {FUNDING_8H_MAX:.4%}]")
    if not (LONG_SHORT_MIN <= s.long_short_ratio <= LONG_SHORT_MAX):
        fails.append(f"L/S {s.long_short_ratio:.2f} outside balanced range [{LONG_SHORT_MIN}, {LONG_SHORT_MAX}]")
    if s.dvol_percentile_52w < DVOL_PERCENTILE_MIN:
        fails.append(f"DVOL {s.dvol_percentile_52w:.0f}th pct < {DVOL_PERCENTILE_MIN:.0f}th — VRP not present")
    if s.iv_rv_spread < IV_RV_SPREAD_MIN:
        fails.append(f"IV-RV spread {s.iv_rv_spread:.1f} vol pts < {IV_RV_SPREAD_MIN} minimum")
    return len(fails) == 0, fails

def entry_decision(s: MarketState, book: dict) -> dict:
    if book.get("drawdown", 0) > 0.28:
        return {"action": "FLAT", "reason": "sleeve drawdown kill"}
    if book.get("active_vol_position"):
        return {"action": "HOLD", "reason": "short-vol position already active"}
    ok, fails = all_gates_pass(s)
    if not ok:
        return {"action": "WAIT", "reason": "gates not met: " + "; ".join(fails)}
    premium_target = book["portfolio_capital"] * 0.020
    return {
        "action":          "SELL_STRANGLE",
        "instrument":      "25-delta put + 15-delta call, DTE 21-35, BTC on Deribit",
        "premium_target":  premium_target,
        "entry_dvol":      s.dvol_current,
        "dvol_30d_avg":    s.dvol_30d_avg,
        "entry_oi_mc":     s.oi_mc_ratio,
        "note": (f"structural clean-book gates pass: OI/MC={s.oi_mc_ratio:.2%} (≤{OI_MC_MAX_CLEAN:.2%}), "
                 f"funding={s.funding_8h:.4%}/8h (flat), L/S={s.long_short_ratio:.2f} (balanced), "
                 f"DVOL={s.dvol_current:.1f} ({s.dvol_percentile_52w:.0f}th pct), "
                 f"IV-RV spread={s.iv_rv_spread:.1f} vol pts"),
    }

def exit_decision(pos: ShortVolPosition) -> Optional[dict]:
    # leverage rebuilding: exit before cascade fuel accumulates
    if pos.current_oi_mc > OI_MC_EXIT_HIGH:
        return {"action": "CLOSE_LEVERAGE_REBUILD",
                "reason": f"OI/MC {pos.current_oi_mc:.2%} > exit threshold {OI_MC_EXIT_HIGH:.2%}; cascade fuel building"}
    # profit: DVOL back near 30d avg
    if (pos.current_dvol - pos.dvol_30d_avg) <= DVOL_PROFIT_WITHIN_VOLS:
        return {"action": "CLOSE_PROFIT",
                "reason": f"DVOL {pos.current_dvol:.1f} within {DVOL_PROFIT_WITHIN_VOLS} vol pts of 30d avg {pos.dvol_30d_avg:.1f}"}
    # stop: unexpected vol expansion
    if (pos.current_dvol - pos.entry_dvol) >= DVOL_STOP_ABOVE_ENTRY:
        return {"action": "CLOSE_STOP",
                "reason": f"DVOL +{pos.current_dvol - pos.entry_dvol:.1f} vol pts above entry — unexpected expansion"}
    # time exit
    if pos.dte <= DTE_TIME_EXIT:
        return {"action": "CLOSE_TIME",
                "reason": f"expiry-{DTE_TIME_EXIT}d exit"}
    return None
```

The production system adds: a Deribit WebSocket for live DVOL and options pricing; a daily OI/MC ratio monitor that fires the leverage-rebuild exit in real time; an automated delta-hedge runner; and a P&L attribution between theta decay and vega P&L to evaluate whether the leverage-state gate is contributing to cleaner entry timing.

## Indicators / data used

- **Open interest** — `GET /api/v1/derivatives/open-interest?coin=BTC`; OI numerator for the OI/MC ratio (Gate 1).
- **Market cap** — `GET /api/v1/coins/BTC` or equivalent; MC denominator for OI/MC ratio.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; 8h rate and 7-day rolling average (Gate 2 and leverage-rebuild exit monitoring while position is open).
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio`; balanced-positioning confirmation (Gate 3).
- **DVOL** — `GET /api/v1/market-intelligence/dvol-history`; current DVOL, 52-week percentile, and 30-day trailing average (Gate 4, profit exit target, stop reference).
- **Realized vol (20-day)** — computed from `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200`; 20-day annualised RV for the IV−RV spread check (Gate 4).
- **Regime** — `GET /api/v1/regimes/current`; if `Trending_Momentum` or `Structural_Shock`, the vol surface may be directionally skewed; reduce position size or skip.
- **OTM option pricing (Deribit)** — specific strike/delta options pricing NOT available via CryptoDataAPI; source from [[deribit]] API directly.

*Note: 25-delta put and 15-delta call pricing at specific strikes requires [[deribit]] API access, consistent with [[funding-conditioned-vol-selling]], [[post-panic-vol-selling]], and [[trend-aligned-premium-selling]].*

## Example trade

**Setup (illustrative — clean-book mid-cycle window):**

- BTC is trading at $68,000 in a quiet range. OI = $16.2B. Market cap = $1.35T. OI/MC = 16.2 / 1350 = **1.2%** (well below 2.0% threshold).
- **Gate 1:** OI/MC = 1.2% ≤ 2.0%. Passes.
- **Gate 2:** 8h funding = +0.010%/8h. 7d avg = +0.008%/8h. Both within the flat band [−0.01%, +0.02%]. Passes.
- **Gate 3:** Long/short ratio = 1.04. Within [0.90, 1.20]. Passes.
- **Gate 4:** DVOL = 61 vol points. DVOL 52-week percentile = 58th (≥ 45th). DVOL 30d avg = 54. 20-day RV = 52 vol points. IV−RV spread = 61 − 52 = 9 vol points (≥ 5 threshold). Passes.

**Entry:** All four gates pass.
- Sell 25-delta BTC put AND 15-delta BTC call, 28 DTE.
- Put strike (25-delta at $68,000, DVOL=61): ≈ $57,800. Put premium ≈ 1.8% of spot = $1,224/unit.
- Call strike (15-delta): ≈ $81,600. Call premium ≈ 0.8% of spot = $544/unit.
- Total premium per strangle ≈ 2.6% of spot = $1,768/unit.
- Portfolio: $250,000. Premium target = 2.0% × $250,000 = $5,000. Units = $5,000 / $1,768 ≈ **2.83 units** (sell 3 strangles, collecting approximately $5,304 premium).

**Scenario A — IV normalises as expected:**
- Over 18 days, BTC remains in $64,000–$72,000 range. No leverage build. DVOL declines from 61 to 56 (within 3 vol points of 30d avg = 54). Profit exit.
- Buy back put (25-delta, 10 DTE remaining): ≈ 0.9% of spot = $612/unit. Buy back call: ≈ 0.3% of spot = $204/unit. Total buyback: $816/unit × 3 = $2,448.
- **Net P&L: $5,304 − $2,448 = +$2,856 gross** / +1.14% of portfolio.

**Scenario B — OI rebuilds, leverage-exit fires:**
- Day 8 after entry: BTC begins trending up. OI climbs from $16.2B to $24.2B. Market cap rises with BTC to $1.45T. OI/MC = 24.2 / 1450 = **1.67%**. Not yet at the 2.8% exit threshold.
- Day 14: OI = $40.6B. Market cap = $1.45T. OI/MC = 40.6 / 1450 = **2.80%** — exit threshold reached.
- Close strangle to avoid cascade exposure. DVOL has risen from 61 to 74 (vol expansion accompanied the OI build).
- Buy back put at ≈ 2.4% of spot = $1,680/unit. Buy back call at ≈ 1.8% of spot = $1,296/unit. Total buyback: $2,976/unit × 3 = $8,928.
- **Net P&L: $5,304 − $8,928 = −$3,624 gross** / −1.45% of portfolio.
- Note: without the OI-rebuild exit, holding to expiry at DVOL=74 would have been significantly worse.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Higher than raw DVOL-percentile vol selling due to cascade-risk filtering; fewer but cleaner signals |
| Expected max drawdown | ~28% | Unexpected vol spikes even in low-leverage regimes (news-driven); OI-rebuild exit limits exposure to rebuilding leverage |
| Win rate (per signal) | ~65–75% (estimated) | Low-leverage state is structurally less prone to cascades; IV mean-reversion more reliable in clean-book windows |
| Signal frequency | 8–15 times per year | Clean-book + VRP-present windows occur during mid-cycle, post-flush, and low-vol periods; less frequent than raw DVOL-percentile |
| Breakeven cost budget | 60 bps | Same as other crypto vol-selling pages; Deribit fees, delta-hedge slippage, bid-ask on strangle |
| Average hold duration | 10–25 days | IV normalisation in the clean-book regime typically faster than in stressed regimes |

**Cost overlay:** the OI-rebuild exit is a meaningful cost driver: when leverage rebuilds mid-position, the strategy exits at a loss despite the IV normalisation not having occurred. This is the price of the structural gate — the strategy exits any time the precondition that justified entry is no longer valid, regardless of P&L.

## Capacity limits

- **Per entry:** Deribit BTC strangle (25d put + 15d call) in the monthly expiry can support $5–25M in sold premium, similar to other vol-selling pages.
- **Aggregate:** `capacity_usd: 150000000` reflects the broader capacity of this gate vs. the narrower post-panic or post-event gate. Clean-book windows are more frequent and the vol surface is more liquid than in post-panic windows.
- **Binding constraint:** the low-leverage state, by definition, corresponds to periods of lower spot trading activity and potentially thinner Deribit options markets. Larger positions in the quiet-regime options market may face wider bid-ask spreads than in active-regime periods.

## What kills this strategy

1. **Cascades without leverage pre-buildup (#3: Market-structure regime change).** In some crash scenarios, a major negative catalyst (exchange hack, protocol failure, macro shock) creates a large cascade even in a low-OI environment: the market sells because of news-driven fear, not because of leveraged liquidation loops. The OI/MC gate does not protect against these fundamental-shock cascades. The stop-loss at +20 DVOL points limits the loss but does not prevent it.
2. **OI rebuilds faster than the option's decay captures (#2: Cost structure).** In a rapidly rallying market, OI and funding can rebuild from the clean-book state to the high-leverage state within days. The leverage-rebuild exit fires quickly, forcing the position to close at a loss before theta and vega have had time to produce profit.
3. **Crowding as vol-selling grows (#4: Crowding).** The clean-book window is not yet widely targeted as a distinct entry criterion. If systematic vol-sellers adopt leverage-state filtering, the clean-book premium compresses — lower IV in these windows, less VRP to harvest.
4. **False clean-book readings from OI fragmentation (#7: Operational).** OI migrating from Binance to Hyperliquid, CME, or Bybit without aggregate monitoring can create a false "low OI" reading on the primary endpoint while total multi-venue OI is elevated. Multi-venue OI monitoring is essential.
5. **Structural VRP inversion (#1: Primitive degradation).** If a regime emerges where RV consistently exceeds IV (covered-call supply glutting the market or fundamental structural change), the VRP harvest fails. The kill criterion (RV > DVOL for 15+ days) covers this.

## Kill criteria

Pause on any of:

1. **DVOL rises > 50% in a single session after entry** — standard vol-selling circuit breaker; exit immediately regardless of regime state.
2. **Sleeve drawdown > 28%** from high-water mark — the clean-book gate is not protecting the vol-selling P&L as expected.
3. **A cascade ≥ 10% in 24h occurs within 5 days of an entry where OI/MC was confirmed ≤ 2.0%** — the low-leverage gate is being invalidated; cascades are occurring without leverage preconditions. Recalibrate the OI/MC threshold downward or retire the strategy.
4. **Realized vol exceeds DVOL for 15+ consecutive days** — structural VRP inversion; the vol-selling book is systematically losing.
5. **Rolling 8-event P&L negative across all 8 events where all gates simultaneously confirmed** — the clean-book window is not producing a positive-expectancy edge; the filter is not working.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Cascades are the vol-seller's primary risk — this gate filters them structurally.** Unlike DVOL-percentile or funding-richness gates that address *why IV is elevated*, this gate addresses *why catastrophic vol-selling losses occur*. The leverage-buildup-to-cascade mechanism is the primary kill scenario for vol-sellers; removing it structurally is a direct defence against the most dangerous failure mode.
- **Inverse relationship with [[leverage-stress-tail-hedge]]** — the leverage-state thresholds are mirrored: the tail-hedge buyer enters when OI/MC ≥ 3.0%; the low-leverage vol-seller enters when OI/MC ≤ 2.0%. The two strategies are structural complements; a portfolio that runs both harvests carry in the clean state and gains in the crash state.
- **Lower crowding risk relative to other vol-selling gates** — the DVOL-percentile gate is widely observed; the post-panic gate is well-known among options traders. The structural-leverage-absence gate is less commonly implemented and thus less susceptible to crowding.
- **OI-rebuild exit limits exposure to regime transitions** — the live monitoring of OI/MC while the position is open provides a dynamic circuit breaker that closes the position before the leverage environment that justified entry has been replaced by a high-risk environment.

## Disadvantages

- **Lower signal frequency than raw DVOL-percentile vol selling** — requiring simultaneous satisfaction of three leverage-state gates reduces the number of qualifying entry windows. During high-activity crypto markets where OI builds continuously, the clean-book window may be rare.
- **News-driven cascades bypass the gate** — the gate protects against leverage-fuelled cascades, not against fundamental-shock cascades. A regulatory ban, exchange failure, or systemic crypto contagion can produce large moves even in a low-OI environment.
- **Leverage-rebuild exit produces mid-position losses** — the OI-rebuild exit is a mark-to-market loss whenever it fires; the strangle premium decay has not had time to run. In rapidly rallying markets, this is the most common loss mechanism.
- **Deribit dependency** — same as all crypto options pages; Deribit is the primary liquid options venue. Deribit downtime or liquidity stress creates operational risk.

## Sources

- [[crypto-options-volatility-selling]] — the canonical short-vol primitive; this page is a leverage-state-gated subset operating exclusively in the low-stress regime.
- [[leverage-stress-tail-hedge]] — the structural inverse: buys puts when leverage is HIGH. This page sells vol when leverage is LOW. The two pages together cover the two tails of the leverage-state distribution.
- [[funding-conditioned-vol-selling]] — the high-funding, crowded-long subset of vol selling. That page enters when leverage is ONE-SIDEDLY HIGH (crowded longs). This page enters when leverage is LOW (both-sided neutral).
- [[post-panic-vol-selling]] — the post-event subset. This page is regime-ongoing, not event-triggered; the two pages are temporal complements.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/open-interest?coin=BTC` — Gate 1 numerator: OI for OI/MC ratio
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — Gate 2: 8h rate and 7-day average
- `GET /api/v1/derivatives/binance/long-short-ratio` — Gate 3: account long/short balance
- `GET /api/v1/market-intelligence/dvol-history` — Gate 4: DVOL percentile, 30d avg; profit-exit and stop reference
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=15m&limit=200` — Gate 4: 20-day realised vol from 15m OHLCV
- `GET /api/v1/regimes/current` — directional-regime context; reduce size if `Trending_Momentum`
- `GET /api/v1/derivatives/binance/summary?symbol=BTCUSDT` — combined snapshot of OI, funding, and long/short for a single-call check at strategy startup

**Historical data:**
- `GET /api/v1/derivatives/binance/history?days=90` — extended OI and funding history for leverage-state threshold calibration and clean-book window frequency analysis
- `GET /api/v1/market-intelligence/dvol-history` — extended DVOL series for 52-week percentile calibration
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — annual daily OHLCV for post-cascade OI/MC analysis

*Note: 25-delta put and 15-delta call pricing at specific strikes requires [[deribit]] API access directly. DVOL index, OI, and funding data are available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/derivatives/binance/summary?symbol=BTCUSDT"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-market-intelligence]], [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [long-term regimes](https://cryptodataapi.com/regimes) · [open interest](https://cryptodataapi.com/open-interest)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Leverage gates (1–3)** — `GET /api/v1/derivatives/binance/summary?symbol=BTCUSDT` — one call covers OI, funding, and long/short for the clean-book check
- **Vol gate (4)** — `GET /api/v1/market-intelligence/dvol-history` + 15m klines for the 20-day realized-vol comparison
- **Regime context** — `GET /api/v1/regimes/current` — reduce size in `Trending_Momentum`
- **Backtest** — `GET /api/v1/derivatives/binance/history?days=90` for gate calibration; post-window realized-vol outcomes from `GET /api/v1/backtesting/klines` (back to 2017-08); funding context from `GET /api/v1/backtesting/funding` (HL hourly since 2023-05; Binance daily since 2026-03-30)
- **Tips** — clean-book windows are rare: run the four gates as a daily screen off the single `/derivatives/binance/summary` call and alert on all-clear rather than streaming every input

## Related

- [[crypto-options-volatility-selling]] — the canonical DVOL-percentile short-vol book; this page is the leverage-state-filtered subset
- [[funding-conditioned-vol-selling]] — enters short-vol when funding is HIGH (crowded longs); this page enters when funding is FLAT — the two gates are at opposite ends of the funding spectrum
- [[post-panic-vol-selling]] — enters after a specific panic event; this page enters in the ongoing quiet, clean-book regime — temporal complements
- [[trend-aligned-premium-selling]] — selects which wing to sell based on trend; composable with this page's structural gate as an additional layer
- [[leverage-stress-tail-hedge]] — structural inverse: buys puts when leverage is HIGH; this page sells vol when leverage is LOW
- [[funding-flush-reversal]] — mean-reversion long entry after a funding flush (low-leverage post-flush environment); similar regime but opposite position (long vs short-vol)
- [[oi-flush-reversion]] — mean-reversion long after OI purge; similar low-leverage regime, different strategy type
- [[short-volatility-strategies]] — the broad short-vol category
- [[deribit]] — the options execution venue
- [[dvol]] — DVOL index; primary IV baseline
- [[implied-volatility]] — the options surface concept
- [[variance-risk-premium]] — the VRP that the low-leverage vol-seller is harvesting
- [[open-interest]] — OI/MC ratio; Gate 1
- [[funding-rate]] — funding; Gate 2
- [[perpetual-futures]] — perp markets where OI and funding are measured
- [[edge-taxonomy]] — behavioral + structural + risk-bearing classification
- [[failure-modes]] — news-driven cascades, leverage-rebuild exit losses, crowding
- [[when-to-retire-a-strategy]] — kill vs pause framework
