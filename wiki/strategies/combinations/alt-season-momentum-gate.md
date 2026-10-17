---
title: "Alt-Season Momentum Gate (Dominance / Alt-Season Gate)"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, momentum, bitcoin, altcoins, market-regime, regime-detection, quantitative, crypto, behavioral-finance]
aliases: ["Alt Season Momentum", "Dominance-Gated Momentum", "BTC Dominance Rotation Gate", "Alt-Season Cross-Sectional Gate", "Dominance Regime Momentum"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [structural, behavioral]
edge_mechanism: "BTC dominance is a real-time regime indicator for where in the crypto cycle the momentum factor concentrates: when dominance is rising (BTC capturing market share), cross-sectional momentum on altcoins generates false signals (alts lose to BTC regardless of their relative price performance); when dominance is falling (alts outperforming BTC), cross-sectional momentum on alts is at its most productive (relative-strength in alts reflects genuine sector rotation, not noise). By restricting alt-momentum deployment to falling-dominance regimes and shifting to BTC-only momentum in rising-dominance regimes, the strategy captures the momentum premium in its highest-quality environments while avoiding the dominance-regime mismatch that creates the most common cross-sectional momentum losses in crypto."

data_required: [btc-dominance, market-cap-ranking, altcoin-breadth, ohlcv-daily, realized-vol-cross-sectional, funding-rates, regime-current]
min_capital_usd: 10000
capacity_usd: 20000000
crowding_risk: medium

expected_sharpe: 1.0
expected_max_drawdown: 0.35
breakeven_cost_bps: 30

decay_evidence: "Cross-sectional momentum in crypto (Liu, Tsyvinski & Wu 2022) is documented as a premium, but its regime-dependence on BTC dominance has not been formally studied. The underlying mechanism — that retail capital rotates sector-by-sector during alt seasons while BTC is the safe-haven in dominance-rising regimes — is consistent with observed crypto market behavior in every cycle since 2017. As institutional participation grows (ETF flows creating persistent BTC bid), the classic alt-season pattern may elongate or compress, changing the optimal dominance threshold."

kill_criteria: |
  - rolling 6-month cross-sectional alt momentum (falling-dominance gate active) Sharpe < 0 (the dominance gate is not identifying productive alt-momentum windows)
  - BTC-dominance data feed unavailable for 10+ days (cannot compute the gate; pause alt deployments)
  - 3 consecutive falling-dominance periods where the alt-momentum basket underperforms BTC by > 20% (the dominance-to-momentum relationship has broken down in the current cycle)
  - alt-universe liquidity below minimum (top-5-alt-basket 24h volume < $200M combined) — capacity insufficient for cost-efficient execution

related: ["[[momentum-rotation]]", "[[crypto-beta-rotation]]", "[[funding-filtered-momentum]]", "[[vol-targeted-trend-following]]", "[[unlock-aware-momentum]]", "[[contrarian-extremes]]", "[[regime-adaptive-strategy]]", "[[spot-led-momentum-filter]]", "[[bitcoin-dominance-rotation]]", "[[btc-dominance]]", "[[market-breadth]]", "[[altcoins]]", "[[bitcoin]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-market-health]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi]]"]
gates:
  - id: dom_roc_falling
    role: filter
    rule: "Alt-season leg 1: BTC dominance 14-day rate of change at or below -0.5 percentage points per week, i.e. (btc_dom now - btc_dom 14 days ago) / 2 <= -0.5"
    runnable: true
    endpoint: /api/v1/backtesting/snapshots?data_type=cycle_regime&start={start}&limit=1000
    field: snapshots[].data.signals.btc_dom
    note: "start = 14 days ago (about 800 rows at the ~25-minute archive tick; Pro Plus). btc_dom is BTC's % share of the top-100 coins' market cap, so it reads a few points above total-market dominance charts; the pp thresholds apply to this series. Archived from 2026-08-07; before that, rebuild it from coin_profiles snapshots (BTC market_cap over the sum of the 100 rows, from 2026-05-09). Dominance is not on /market-health/summary or /components, which the page body names."
  - id: dom_below_ma50
    role: filter
    rule: "Alt-season leg 2: BTC dominance at or below its 50-day moving average"
    runnable: true
    endpoint: /api/v1/backtesting/snapshots?data_type=cycle_regime&start={start}&limit=1000
    field: snapshots[].data.signals.btc_dom
    note: "start = 50 days ago: about 2,850 rows, so page with three calls (limit caps at 1,000; restart from the last row's time). Reduce to one value per UTC day before averaging. The series first covered 50 days on 2026-09-26; earlier backtests rebuild it from coin_profiles snapshots as in dom_roc_falling."
  - id: breadth_min
    role: filter
    rule: "Alt-season leg 3: at least 45% of the top-50 alts above their 200-day moving average"
    runnable: partial
    endpoint: /api/v1/market-health/altcoin-breadth?ma_period=200
    field: breadth_pct
    replay: /api/v1/backtesting/snapshots?data_type=altcoin_breadth&start={start}&limit=1000
    replay_field: snapshots[].data.details.breadth_pct
    note: "Served breadth covers a fixed list of about 30 Binance large caps that includes BTC and ETH (coins[] names them), not the top-50 alts, and skips coins with under 200 daily bars. For the page's exact universe, count closes above the 200-day MA per alt from daily klines. The archive (replay) runs from 2026-05-09. The page body's ?period=200 is ma_period on the API."
  - id: breadth_rising
    role: filter
    rule: "Alt-season confirmation: altcoin breadth rising"
    runnable: partial
    endpoint: /api/v1/backtesting/snapshots?data_type=altcoin_breadth&start={start}&limit=1000
    field: snapshots[].data.details.breadth_pct
    note: "From the page's quantitative-signal list; the Rules section and the pseudocode leave it out. No window is given for rising (for example against 7 days ago), so that is the desk's call. Same 30-coin universe as breadth_min; samples every ~25 minutes from 2026-05-09, Pro Plus."
  - id: alt_season_mode
    role: filter
    rule: "Alt-season mode (deploy the full alt basket) when dom_roc_falling, dom_below_ma50 and breadth_min all hold"
    runnable: partial
    input: derived
    inputs: [dom_roc_falling, dom_below_ma50, breadth_min]
    note: "Only as runnable as breadth_min, whose served universe is not the page's top-50 alts."
  - id: dom_roc_rising
    role: filter
    rule: "BTC-only leg 1: BTC dominance 14-day rate of change at or above +0.5 percentage points per week"
    runnable: true
    endpoint: /api/v1/backtesting/snapshots?data_type=cycle_regime&start={start}&limit=1000
    field: snapshots[].data.signals.btc_dom
    note: "Same series and window as dom_roc_falling."
  - id: dom_above_ma50
    role: filter
    rule: "BTC-only leg 2: BTC dominance at or above its 50-day moving average"
    runnable: true
    endpoint: /api/v1/backtesting/snapshots?data_type=cycle_regime&start={start}&limit=1000
    field: snapshots[].data.signals.btc_dom
    note: "Same series and paging as dom_below_ma50."
  - id: btc_only_mode
    role: filter
    rule: "BTC-only mode (no alt positions; run BTC trend only) when dom_roc_rising and dom_above_ma50 both hold"
    runnable: true
    input: derived
    inputs: [dom_roc_rising, dom_above_ma50]
  - id: dom_roc_sideways
    role: filter
    rule: "Ambiguous mode: absolute 14-day rate of change of BTC dominance below 0.5 percentage points per week (either this or dom_near_ma50)"
    runnable: true
    endpoint: /api/v1/backtesting/snapshots?data_type=cycle_regime&start={start}&limit=1000
    field: snapshots[].data.signals.btc_dom
    note: "Same series as dom_roc_falling. The text overlaps with alt-season mode near the MA; the pseudocode settles it: alt-season first, then BTC-only, and anything else is ambiguous."
  - id: dom_near_ma50
    role: filter
    rule: "Ambiguous mode: BTC dominance within 1 percentage point of its 50-day moving average (either this or dom_roc_sideways)"
    runnable: true
    endpoint: /api/v1/backtesting/snapshots?data_type=cycle_regime&start={start}&limit=1000
    field: snapshots[].data.signals.btc_dom
    note: "Same series and paging as dom_below_ma50."
  - id: no_choppy_regime
    role: filter
    rule: "Even in alt-season mode, deploy no alt momentum while the HMM market regime is choppy_high_vol"
    runnable: true
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "From the page's indicator list and agent workflow, not its Rules section."
  - id: universe_top50_volume
    role: universe
    rule: "Top 50 alts (BTC excluded) by 30-day average daily USD volume on Hyperliquid perps"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles/batch?coins={coin}&interval=1d&limit=30&closed_only=true
    field: series.{coin}[].volume
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].volume
    note: "volume is in coin units: average volume x close over the 30 bars for USD. Take the coin list from assets[].coin on /api/v1/hyperliquid/open-interest (about 180 perps) and batch 25 coins per call."
  - id: exclude_stable_wrapped
    role: universe
    rule: "Exclude stable proxies and wrapped tokens from the alt universe"
    runnable: partial
    endpoint: /api/v1/coins/{symbol}
    field: categories
    note: "Drop a coin whose categories include Stablecoins or Wrapped-Tokens. Whether an asset-backed token such as PAXG counts as a stable proxy is the desk's call, and Hyperliquid names that /coins does not resolve (kPEPE) need mapping first."
  - id: momentum_score
    role: entry
    rule: "Risk-adjusted momentum = 4-week (28 daily bars) trailing return divided by the 20-day realised volatility of daily returns; rank descending"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles/batch?coins={coin}&interval=1d&limit=30&closed_only=true
    field: series.{coin}[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
  - id: funding_cap
    role: filter
    rule: "Skip any alt whose 8h funding is at or above +0.06%: the sum of its last 8 hourly Hyperliquid settlements >= 0.0006"
    runnable: true
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=8
    field: history[].funding_rate
    replay: /api/v1/backtesting/funding?symbol={coin}&exchange=hyperliquid&grain=hourly&start={start}
    replay_field: data[].funding_rate
    note: "Hyperliquid settles hourly, so 8h funding is the sum of 8 settled prints, not 8x the current predicted rate. Hourly prints are served locally from 2024-01-01."
  - id: top5_basket
    role: entry
    rule: "Long the top 5 eligible alts by momentum_score, replacing any that fail funding_cap with the next rank"
    runnable: partial
    input: derived
    inputs: [universe_top50_volume, exclude_stable_wrapped, momentum_score, funding_cap]
    note: "Only as runnable as exclude_stable_wrapped."
  - id: vol_target_size
    role: sizing
    rule: "Vol-target each alt position to a 2% daily risk budget using its 20-day realised volatility"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles/batch?coins={coin}&interval=1d&limit=30&closed_only=true
    field: series.{coin}[].close
  - id: alt_book_cap
    role: sizing
    rule: "The alt-momentum book is at most 10% of the portfolio"
    runnable: true
    input: position
  - id: btc_book_size
    role: sizing
    rule: "In BTC-only mode run the BTC trend book (vol-targeted-trend-following, funding-filtered-momentum for timing) at 5-8% of the portfolio"
    runnable: true
    input: derived
    inputs: [btc_only_mode]
    note: "The BTC entry and exit rules live on those two pages."
  - id: ambiguous_half_size
    role: sizing
    rule: "In ambiguous mode cut every momentum position, alt and BTC, to 50% of its normal size"
    runnable: true
    input: derived
    inputs: [dom_roc_sideways, dom_near_ma50]
  - id: ambiguous_top3
    role: sizing
    rule: "In ambiguous mode hold only the top 3 alts by momentum_score instead of the top 5"
    runnable: true
    input: derived
    inputs: [dom_roc_sideways, dom_near_ma50, momentum_score]
  - id: ambiguous_funding_tighter
    role: filter
    rule: "In ambiguous mode tighten the funding filter below the +0.06%/8h cap"
    runnable: partial
    input: derived
    inputs: [dom_roc_sideways, dom_near_ma50, funding_cap]
    note: "The page gives no tighter threshold, so the level is the desk's call."
  - id: rebalance_out_of_top10
    role: exit
    rule: "Weekly rebalance: replace any position that has dropped out of the top 10 by momentum_score"
    runnable: true
    input: derived
    inputs: [momentum_score]
  - id: trailing_stop
    role: stop
    rule: "Exit an alt position when price is 8% or more below its rolling 10-day high"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=10
    field: candles[].high
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].high
    note: "The 10 bars include the forming one; compare the current mark (assets[].mark_price on /api/v1/hyperliquid/open-interest) with 0.92 x the highest high."
  - id: profit_target
    role: exit
    rule: "Take profit at +20% from the entry fill before the weekly rebalance"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: mode_switch_exit
    role: exit
    rule: "Exit all alt positions within 5 days of the mode switching from alt-season to BTC-only or ambiguous"
    runnable: partial
    input: derived
    inputs: [alt_season_mode]
    note: "Only as runnable as alt_season_mode (the breadth universe)."
---

# Alt-Season Momentum Gate (Dominance / Alt-Season Gate)

Alt-season momentum gate **conditions cross-sectional momentum deployment on the BTC-dominance regime**: deploy alt-basket momentum only when BTC dominance is falling (alt-season active or beginning to form); shift to BTC-only or BTC-paired momentum entries when BTC dominance is rising (BTC capturing market share); sit flat or minimal in both when dominance is ambiguous (sideways). The gate solves the single most common failure mode of cross-sectional crypto momentum strategies — deploying alt-relative-strength signals during dominance-rising regimes where every altcoin loses market share to BTC regardless of its internal relative strength.

**This is differentiated from [[momentum-rotation]]** — that page is the *cross-sectional crypto momentum* primitive itself: rank assets by trailing returns, long top decile, short bottom decile, rebalance weekly. It does not condition its alt-deployment on the BTC dominance regime; it runs cross-sectional momentum unconditionally across the alt universe. This page adds the dominance-regime gate as a selective overlay: deploy the [[momentum-rotation]] signal in alts only during falling-dominance regimes; suppress it otherwise. The dominance gate is a filter on an existing strategy, not a standalone strategy.

**This is differentiated from [[crypto-beta-rotation]]** — that page manages *crypto's aggregate beta to the Nasdaq/DXY macro tape*: it reduces crypto-directional exposure when the macro regime is risk-off (BTC-Nasdaq correlation high, DXY rising). The question there is: "should the entire crypto book be long or hedged?" This page does not address aggregate crypto beta; it addresses *intra-crypto allocation* between BTC and alts. Both gates can operate simultaneously (crypto-beta-rotation manages total crypto exposure; this page manages the BTC vs alt split within the crypto book).

**This is differentiated from [[funding-filtered-momentum]]** — that page gates momentum entries on the funding rate (crowd not yet positioned in the momentum direction). This page gates the *universe of momentum deployment* (alts vs BTC) on the dominance regime. The two are composable: use [[funding-filtered-momentum]] to gate individual signal entries AND this page to restrict the entry universe to the regime-appropriate assets.

**This is differentiated from [[spot-led-momentum-filter]]** — that page gates momentum entries on whether the move is spot-led (Coinbase premium, spot volume growing faster than OI). This page gates on the dominance regime, which is a multi-week structural signal, not a per-signal quality check.

## Edge source

Per [[edge-taxonomy]], **structural + behavioral**:

- **Structural (primary)** — BTC dominance is a real-time measure of intra-crypto capital flows. When dominance rises, marginal capital entering crypto is flowing primarily into BTC (or flowing OUT of alts specifically); alt relative-strength signals in this regime are contaminated by a structural headwind — even the best-performing alt is likely losing ground relative to BTC. The momentum premium in alts is structurally suppressed by the dominance regime headwind. When dominance falls, marginal capital is flowing into alts sector-by-sector (L1 season, memecoin season, DeFi season); alt relative-strength signals in this regime reflect genuine sector rotation with structural tailwinds.
- **Behavioral** — Retail crypto participants rotate from BTC into alts in a predictable cycle: they accumulate BTC first (dominance rises), then rotate into large-cap alts (ETH, SOL), then into mid-cap alts, then into small-cap speculative tokens. This rotation cycle creates serial momentum within the alt universe that correlates with the dominance decline. The behavioral predictability of this rotation allows the dominance gate to correctly time the *beginning* of an alt momentum deployment and the *end* when rotation has overextended.

## Why this edge exists

**The dominance-momentum relationship:**

In a rising-dominance regime:
- BTC outperforms alts on an absolute basis (BTC is rising faster or falling less)
- Relative performance within alts (ETH vs SOL vs AVAX) becomes noisy — all alts are losing to BTC
- Cross-sectional alt momentum signals fire (some alts rank higher than others on trailing returns) but the realized return differential between top-decile and bottom-decile alts is compressed or negative net of BTC beta
- The momentum strategy pays for turnover without capturing the momentum premium

In a falling-dominance regime:
- Alts outperform BTC as capital rotates within crypto
- Relative performance within alts becomes meaningful (L1s beat DeFi; memecoins beat L1s in the speculative phase)
- Cross-sectional alt momentum captures genuine sector rotation with structural tailwinds
- The momentum premium is at its widest — top-decile alts compound the alt-season beta with genuine relative strength

**Quantitative signal:**
- BTC dominance falling: 14-day rate-of-change of BTC dominance < −0.5 percentage points per week AND dominance below its 50-day moving average
- Alt season confirmed: altcoin breadth (% of top-50 alts above their 200-day MA) ≥ 45% AND rising
- BTC-only mode: dominance rising > +0.5 pp/week AND dominance above its 50-day MA
- Ambiguous: dominance sideways (|RoC| < 0.5 pp/week) — reduce position sizes 50%, deploy BTC-only until direction confirmed

**Who is on the other side:** the undifferentiated cross-sectional momentum operator who deploys alt-momentum signals regardless of the dominance regime. In rising-dominance regimes, they pay turnover costs to own relative alt-strength signals that are overwhelmed by the BTC-dominance headwind. The dominance-aware operator avoids this period entirely, deploying only when the regime is supportive.

## Null hypothesis

Under the null, the BTC dominance regime at the time of cross-sectional momentum deployment adds **no incremental predictive power** to the subsequent returns of the long/short alt-momentum portfolio:

- Top-decile minus bottom-decile alt momentum returns during falling-dominance regimes should NOT materially exceed those during rising-dominance regimes.
- The dominance gate should not materially improve the Sharpe or reduce drawdowns of the [[momentum-rotation]] strategy.

Testable: split all [[momentum-rotation]] deployment dates into (a) falling-dominance (as defined above) and (b) rising-dominance. Compare 4-week forward long-short spread returns. Prediction: group (a) has materially higher mean L-S spread and lower drawdown, because the dominance headwind that contaminates group (b)'s signals is absent.

## Rules

### Dominance regime classification

**Alt-season mode (deploy full alt-momentum basket):**
- BTC dominance 14-day RoC ≤ **−0.5 percentage points/week** (dominance falling)
- AND BTC dominance ≤ its **50-day MA** (structural downtrend in dominance)
- AND altcoin breadth ≥ **45%** of top-50 alts above their 200-day MA (broad participation)
- Source: `GET /api/v1/market-health/altcoin-breadth?period=200` (breadth); BTC dominance from `GET /api/v1/market-health/summary` or `GET /api/v1/market-health/components`.

**BTC-only mode (deploy BTC-only momentum; suppress alt-basket):**
- BTC dominance 14-day RoC ≥ **+0.5 pp/week** (dominance rising)
- AND BTC dominance ≥ its **50-day MA** (structural uptrend in dominance)
- In this mode: apply [[funding-filtered-momentum]] and [[vol-targeted-trend-following]] to BTC only; no alt positions.

**Ambiguous/sideways mode:**
- |Dominance 14-day RoC| < 0.5 pp/week OR dominance near its 50-day MA (within 1 pp)
- In this mode: reduce all momentum position sizes to 50%; deploy only the top-3 relative-strength alts rather than full top-decile basket; increase funding filter stringency.

### Alt-basket construction (alt-season mode only)

1. **Universe:** top 50 alts by 30-day avg volume on Hyperliquid perps (excludes extremely illiquid). Exclude stable proxies and wrapped tokens.
2. **Ranking:** 4-week trailing return / 20-day realised vol (risk-adjusted momentum score). Rank descending.
3. **Long basket:** top 5 by risk-adjusted score.
4. **Position sizing:** vol-target each position to 2% of portfolio daily risk budget (per [[vol-targeted-trend-following]] framework applied to the alt sub-book). Total alt-momentum book: 10% of portfolio maximum.
5. **Rebalance:** weekly; replace any position where the asset has dropped out of the top-10 ranking.
6. **Funding check (per-position):** apply [[funding-filtered-momentum]] logic: skip any alt where 8h funding ≥ +0.06%/8h (crowd too far ahead for this specific name).

### BTC-only mode rules

- Apply [[vol-targeted-trend-following]] on BTC/USD at 5–8% of portfolio. No alt exposure.
- Supplement with [[funding-filtered-momentum]] for entry timing on BTC.
- This mode explicitly deactivates the alt-basket ranking and selection logic.

### Exit rules

**Alt-season mode exits:**
- Individual position exits: [[momentum-rotation]] standard exits (trailing stop at −8% from rolling 10-day high; profit target at +20% before rebalance).
- Full mode switch: exit all alt positions within 5 days of dominance mode switching from "alt-season" to "BTC-only" or "ambiguous."

**BTC-only mode exits:**
- Standard [[vol-targeted-trend-following]] exits.

## Implementation pseudocode

```python
# alt_season_momentum_gate.py

from dataclasses import dataclass
from typing import Literal

# Dominance regime thresholds
ALT_SEASON_ROC_MAX     = -0.005   # dominance RoC ≤ −0.5 pp/week
ALT_SEASON_BREADTH_MIN = 0.45     # ≥ 45% of top-50 alts above 200d MA
BTC_ONLY_ROC_MIN       = +0.005   # dominance RoC ≥ +0.5 pp/week
AMBIGUOUS_ROC_BAND     = 0.005    # |RoC| < 0.5 pp = ambiguous

# Alt basket
BASKET_SIZE          = 5
MAX_BASKET_FUNDING   = 0.0006   # skip alts with 8h funding ≥ +0.06%
ALT_BOOK_MAX_PCT     = 0.10     # max 10% of portfolio in alt-momentum
DAILY_RISK_PER_POS   = 0.02     # 2% portfolio daily-risk per alt position

# BTC mode
BTC_BOOK_MAX_PCT     = 0.08     # max 8% of portfolio in BTC-only trend mode

@dataclass
class DominanceState:
    btc_dominance:          float    # current BTC dominance (fraction, e.g., 0.54)
    dominance_50d_ma:       float    # 50-day MA of BTC dominance
    dominance_14d_roc:      float    # 14-day rate-of-change per week (fraction)
    altcoin_breadth:        float    # fraction of top-50 alts above 200d MA

DominanceMode = Literal['alt_season', 'btc_only', 'ambiguous']

def classify_dominance(state: DominanceState) -> DominanceMode:
    falling = (state.dominance_14d_roc <= ALT_SEASON_ROC_MAX
               and state.btc_dominance <= state.dominance_50d_ma
               and state.altcoin_breadth >= ALT_SEASON_BREADTH_MIN)
    rising = (state.dominance_14d_roc >= BTC_ONLY_ROC_MIN
              and state.btc_dominance >= state.dominance_50d_ma)
    if falling:
        return 'alt_season'
    elif rising:
        return 'btc_only'
    return 'ambiguous'

@dataclass
class AltCandidate:
    symbol:              str
    risk_adj_momentum:   float   # 4w return / 20d realised vol
    funding_8h:          float
    vol_20d:             float   # annualised 20-day realised vol
    eligible:            bool

def build_alt_basket(candidates: list[AltCandidate]) -> list[dict]:
    eligible = [c for c in candidates
                if c.eligible and c.funding_8h < MAX_BASKET_FUNDING]
    ranked = sorted(eligible, key=lambda c: c.risk_adj_momentum, reverse=True)
    basket = []
    for c in ranked[:BASKET_SIZE]:
        daily_risk_usd = 0.0  # placeholder — requires portfolio_capital
        basket.append({
            'symbol':         c.symbol,
            'risk_adj_mom':   c.risk_adj_momentum,
            'funding_8h':     c.funding_8h,
            'vol_20d':        c.vol_20d,
            'daily_risk_pct': DAILY_RISK_PER_POS,
        })
    return basket

def deployment_decision(mode: DominanceMode,
                        basket: list[dict],
                        portfolio_capital: float) -> dict:
    if mode == 'alt_season':
        total_book = min(portfolio_capital * ALT_BOOK_MAX_PCT,
                         BASKET_SIZE * DAILY_RISK_PER_POS * portfolio_capital / 0.02)
        return {
            'mode': 'alt_season',
            'action': 'DEPLOY_ALT_BASKET',
            'basket': basket,
            'total_notional': total_book,
            'btc_book': 0.0,
        }
    elif mode == 'btc_only':
        return {
            'mode': 'btc_only',
            'action': 'DEPLOY_BTC_TREND',
            'basket': [],
            'btc_book': portfolio_capital * BTC_BOOK_MAX_PCT,
        }
    else:  # ambiguous
        half_basket = basket[:min(3, len(basket))]
        return {
            'mode': 'ambiguous',
            'action': 'REDUCED_DEPLOYMENT',
            'basket': half_basket,
            'basket_size_fraction': 0.5,
            'btc_book': portfolio_capital * BTC_BOOK_MAX_PCT * 0.5,
        }
```

## Indicators / data used

- **BTC dominance** — `GET /api/v1/market-health/components` or `GET /api/v1/market-health/component/btc_dominance` — BTC market cap as fraction of total crypto market cap; use `history` variant for 50-day MA calculation. Source: [[cryptodataapi-market-health]].
- **Altcoin breadth** — `GET /api/v1/market-health/altcoin-breadth?period=200` — percentage of top-50 alts above their 200-day MA; used to confirm broad alt participation (Gate: alt-season mode requires ≥ 45%). Source: [[cryptodataapi-market-health]].
- **Market health history** — `GET /api/v1/market-health/history?days=90` — 90-day health score timeseries; compute 50-day MA of dominance component from this history.
- **Meme regime** — `GET /api/v1/meme/regime` and `/meme/regime/score` — meme lifecycle (euphoric/ignition/distribution/dormant) helps identify within-alt-season sector rotation (meme-coin phase = ignition/euphoric; L1 blue-chip phase = earlier). Useful for sub-selecting which alts to include in the basket.
- **Quant regime** — `GET /api/v1/quant/market` — HMM 6-regime classification; use to exclude `choppy_high_vol` regime from alt-momentum deployments even within alt-season mode (high-chop kills cross-sectional momentum).
- **Funding rates (per alt)** — `GET /api/v1/derivatives/funding-rates?coin={symbol}` — per-alt funding gate (skip alts with 8h funding ≥ +0.06%/8h). Source: [[cryptodataapi-derivatives]].
- **OHLCV daily (per alt)** — `GET /api/v1/market-data/klines?symbol={SYMBOL}USDT&interval=1d&limit=60` — trailing 4-week returns and 20-day realised vol for the risk-adjusted momentum ranking. Source: [[cryptodataapi-market-data]].

## Example trade

**Setup (illustrative — 2024 alt-season deployment)**

- BTC dominance: 50.2%, declining from 54.8% four weeks ago. 14-day RoC = −0.56 pp/week. Dominance below its 50-day MA (51.1%). Altcoin breadth: 52% above 200d MA. **Dominance mode: ALT-SEASON.**
- Top-5 risk-adjusted momentum basket (from 50-alt universe): SOL, AVAX, WIF, ONDO, ARB.
  - SOL funding 8h: +0.018% (below +0.060% cap) — include.
  - WIF funding 8h: +0.075% (above +0.060% cap) — **exclude**. Replace with 6th-ranked INJ.
- Portfolio: $500,000. Alt-momentum book: 10% = $50,000. Per position: $10,000.

**4-week outcome:**
- BTC up +12% during the period. SOL up +28%, AVAX up +19%, INJ up +31%, ONDO up +22%, ARB up +14%.
- Simple basket avg return: +22.8% vs BTC +12% = **+10.8pp alpha vs BTC** (roughly in line with historical alt-momentum premium in alt-season phases).
- On $50,000 alt-momentum book: +$5,400 gross return − turnover cost (1 rebalance × 5 positions × 30 bps): −$150 = **+$5,250 net.**

**Dominance mode switch (week 6):**
- BTC dominance reverses: 14-day RoC = +0.58 pp/week, dominance above 50d MA (52.3%). Altcoin breadth falls to 39%.
- **Mode switches: ALT-SEASON → BTC-ONLY.**
- Exit all 5 alt positions within 5 days. Deploy $40,000 into BTC-only trend via [[vol-targeted-trend-following]].

*(Illustrative round numbers. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | Higher than [[momentum-rotation]] baseline due to regime filtering |
| Expected max drawdown | ~35% | Alt-season drawdown risk: if dominance reverses sharply after deployment, alt positions drop together |
| Signal frequency (mode change) | 4–8 regime changes per year | Alt-season and BTC-dominance regimes each lasting 6–16 weeks historically |
| Average alt-season deployment | 6–14 weeks | Duration of falling-dominance regimes |
| Turnover | Weekly rebalance of basket | 5 positions × weekly = high; cost is material at > 30 bps per round trip |
| Breakeven cost | 30 bps | Weekly rebalance at 30 bps/round trip = ~1.5%/year cost; must be < alt-season alpha |

**Cost overlay:** alt-momentum strategies are turnover-intensive. The dominance gate reduces the number of deployments (restricts to alt-season periods) which reduces annual turnover relative to continuous deployment. However, within an alt-season deployment, weekly rebalancing creates real costs, especially for mid-cap alts with 50–100 bps bid-ask spreads.

## Capacity limits

- `capacity_usd: 20000000` — limited by mid-cap alt perp depth on Hyperliquid. At $20M AUM, $4M per position ($20M / 5) is within Hyperliquid perp depth for top-10 alts. Below that for mid-cap alts.

## What kills this strategy

1. **Dominance regime oscillation (#2: Regime change).** If BTC dominance oscillates rapidly around its threshold (rising one week, falling the next) without establishing a clear alt-season, the strategy incurs high turnover switching between modes without capturing either the alt-momentum or BTC-trend premium. The 50-day MA gate and 0.5 pp/week RoC requirement are designed to prevent whipsaw; the ambiguous mode with 50% sizing handles the transition.
2. **Alt-season without momentum continuation (#2: Regime change).** The 2022–2023 cycle produced dominance-falling periods where alts declined in absolute terms (risk-off deleveraging). A falling dominance in a bear market (all coins falling, but alts falling harder → then dominance falls as BTC holds better) is NOT an alt-season. Gate: altcoin breadth ≥ 45% above 200d MA prevents this scenario — in an absolute bear, breadth collapses below this threshold.
3. **Specific alt positions hit concentrate liquidation (#4: Crowding).** Individual alt positions in the basket may be the target of large unlock events or protocol failures (see [[defi-yield-event-calendar]], [[unlock-cascade-watch]]). Position-level stops (−8% trailing) and diversification (5 positions, 2% daily risk each) limit individual position impact.
4. **BTC dominance data staleness (#6: Data / execution).** If the market health endpoint has a data delay, the dominance classification may lag by 24–48 hours. This is acceptable for a weekly-rebalanced strategy; the dominance regime is slow-moving enough that a 48-hour lag has minimal impact.

## Kill criteria

Pause or retire on any of:

1. **Rolling 6-month L-S alt-momentum spread (falling-dominance deployments only) Sharpe < 0** — the dominance gate is not identifying productive alt-momentum windows; reassess threshold.
2. **3 consecutive alt-season deployments where alt basket underperforms BTC by > 20% over the deployment window** — the dominance-to-momentum link has broken down in the current macro regime.
3. **BTC dominance metric unavailable from CryptoDataAPI for 10+ days** — gate cannot be evaluated; switch to ambiguous mode (50% sizing across all momentum signals) until data restores.
4. **Alt-universe perp liquidity (top-5 basket 24h combined volume) < $200M** — position sizes cannot be executed with acceptable slippage; pause or shrink book.

See [[when-to-retire-a-strategy]] for the broader framework.

## Instrument Structures

Alt-season momentum gate switches the deployment structure between basket mode and single-asset mode depending on the dominance regime.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Basket** | Activated in falling-dominance (alt-season) mode. The strategy deploys cross-sectional momentum across sector baskets (e.g., [[l1-blockchains-basket]], [[ai-tokens-basket]], [[solana-ecosystem-basket]], [[defi-bluechip-basket]]): long the top-momentum baskets, underweight or short the bottom. The basket structure captures the sector-rotation pattern that characterises genuine alt-seasons. |
| **Single-asset** | Activated in rising-dominance mode. The strategy shifts to BTC-only trend-following — one single-asset position — because alt baskets produce false signals when BTC is capturing market share. The mechanics simplify to a single trend signal (BTC above/below 50-day MA). |
| Pair | Not deployed. The strategy is directional in both modes (either long alts or long BTC), not market-neutral. |
| Cross-venue | Not deployed. |

The critical mechanic is the mode switch itself: the 14-day rate of change in BTC dominance and the altcoin breadth indicator determine which structure is active. Running both modes simultaneously (a basket + a BTC long) is permitted as a transitional position during the first 3 days of a mode change, but not as a steady-state.

## Advantages

- **Eliminates the most common crypto momentum failure mode** — deploying cross-sectional alt momentum in rising-dominance regimes is the single biggest loss-generator for crypto momentum strategies; this gate cleanly avoids it.
- **Composable with existing momentum pages** — [[funding-filtered-momentum]] and [[vol-targeted-trend-following]] plug directly into this framework as the per-signal and sizing layers within each mode.
- **BTC-only fallback maintains exposure** — switching to BTC-only trend in rising-dominance regimes means the portfolio stays invested in the strongest-performing crypto asset during those periods, not idle.
- **Breadth confirmation prevents bear-market false positives** — the altcoin breadth ≥ 45% gate distinguishes genuine alt-seasons (broad participation, positive absolute returns) from dominance-falling bear markets (alts declining less fast than BTC).

## Disadvantages

- **Signal lag risk** — the dominance and breadth signals are computed from daily data; a fast reversal from alt-season to BTC-dominance can take 5–7 days to register clearly, during which the alt basket may suffer the beginning of the dominance reversal.
- **Individual alt selection quality** — the risk-adjusted momentum ranking is simple (4-week return / 20d vol). More sophisticated multi-factor ranking (incorporating on-chain metrics, developer activity, relative TVL growth) would likely improve within-basket selection.
- **High turnover in active periods** — weekly rebalancing of a 5-position basket is expensive in mid-cap alts with wide spreads. The strategy's Sharpe is sensitive to round-trip costs.
- **Concentration risk** — 5 positions at 2% daily risk each means correlated alt draws-downs (a sector-wide flush) can hit the full alt-basket simultaneously.

## Sources

- Liu, Y., Tsyvinski, A. & Wu, X. (2022). "Common Risk Factors in Cryptocurrency." *Journal of Finance*. Documents the cross-sectional momentum premium in crypto.
- [[momentum-rotation]] — the underlying cross-sectional momentum primitive; this page adds the dominance-regime gate as a deployment overlay.
- [[crypto-beta-rotation]] — the macro beta management overlay; operates at the aggregate-crypto level while this page operates at the intra-crypto BTC-vs-alt level.
- [[bitcoin-dominance-rotation]] — the concept page on BTC dominance as a rotation signal.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-health/altcoin-breadth?period=200` — Alt-season gate: % of top-50 alts above 200d MA (≥ 45% required)
- `GET /api/v1/market-health/summary` — BTC dominance current reading (component in summary)
- `GET /api/v1/market-health/history?days=90` — 90-day health history for 50d MA computation
- `GET /api/v1/meme/regime/score` — meme-hype score; use to sub-select meme alts during meme-season within broader alt-season
- `GET /api/v1/quant/market` — HMM regime; exclude `choppy_high_vol` from alt-momentum deployments
- `GET /api/v1/derivatives/funding-rates?coin={symbol}` — per-alt funding gate (exclude alts with 8h funding ≥ +0.06%)
- `GET /api/v1/market-data/klines?symbol={SYMBOL}USDT&interval=1d&limit=60` — trailing returns and vol for momentum ranking

**Historical data:**
- `GET /api/v1/market-health/history?days=730` — 2-year health history for backtesting dominance-regime classification
- `GET /api/v1/quant/timeline` — daily market regime labels back to 2019; use to cross-reference HMM regime with dominance regime

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth?period=200"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-health]], [[cryptodataapi-regimes]], [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

**Live dashboards:** [market health](https://cryptodataapi.com/market) · [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Gate leg** — `GET /api/v1/market-health/altcoin-breadth?period=200` + `GET /api/v1/market-health/summary` — recompute the dominance mode (alt-season / BTC-only / ambiguous) daily; the mode decides which book runs
- **Momentum leg** — `GET /api/v1/market-data/klines?symbol={SYMBOL}USDT&interval=1d&limit=60` across the alt universe for the risk-adjusted momentum ranking; `GET /api/v1/derivatives/funding-rates?coin={symbol}` drops alts with 8h funding ≥ +0.06%
- **Regime gate** — `GET /api/v1/quant/market` — suppress alt deployments while `choppy_high_vol` leads the HMM probabilities, even inside alt-season mode
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08) for basket returns; `GET /api/v1/market-health/history?days=730` caps the dominance-gate replay at ~2 years; `GET /api/v1/quant/regimes/history` (hourly HMM since 2020, Pro Plus) extends the regime overlay further back
- **Tips** — batch the alt screen via `GET /api/v1/quant/coins/risk` instead of looping symbols; respect `insufficient_history` / `new_listing` flags before admitting a recently listed alt to the basket

## Related

- [[momentum-rotation]] — the cross-sectional momentum primitive; this page adds the dominance-regime gate
- [[crypto-beta-rotation]] — aggregate crypto beta management (macro risk-on/off); different level (total crypto) vs this page (BTC vs alt allocation)
- [[funding-filtered-momentum]] — funding gate for individual momentum entries; composable layer within each deployment mode
- [[vol-targeted-trend-following]] — BTC-mode deployment sizing framework
- [[unlock-aware-momentum]] — momentum book pause around unlock events; composable event gate on top of this dominance gate
- [[spot-led-momentum-filter]] — entry quality gate (spot-led vs perp-driven); per-signal quality check composable within alt-season basket construction
- [[contrarian-extremes]] — exits when the alt-season becomes over-extended (greed extreme); complementary exit signal
- [[bitcoin-dominance-rotation]] — the BTC dominance concept and historical cycle data
- [[btc-dominance]] — BTC market dominance as a market regime indicator
- [[market-breadth]] — altcoin breadth metric underlying the alt-season confirmation gate
- [[altcoins]] — the alt universe this strategy deploys into
