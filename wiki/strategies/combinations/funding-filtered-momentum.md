---
title: "Funding-Filtered Momentum"
type: strategy
created: 2026-07-18
updated: 2026-07-18
status: good
tags: [combinations, meta-strategy, momentum, funding-rate, perpetual-futures, behavioral-finance, quantitative, crypto]
aliases: ["Funding-Gated Momentum", "Funding-Conscious Breakout", "Non-Consensus Trend Entry"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [behavioral, structural]
edge_mechanism: "Leveraged retail persistently bids perps when they are bullish, pushing funding positive and crowding out the long side; a momentum signal that only fires when funding is flat or negative finds the non-consensus trend — where the marginal buyer is not yet in — and avoids paying crowding costs and becoming a liquidation target when the crowd unwinds."

data_required: [ohlcv-daily, ohlcv-4h, funding-rates, open-interest, mark-price]
min_capital_usd: 5000
capacity_usd: 100000000
crowding_risk: medium

expected_sharpe: 0.9
expected_max_drawdown: 0.25
breakeven_cost_bps: 30

decay_evidence: "No published study specifically on funding-filtered crypto momentum. The underlying funding-rate edge has compressed since 2024 as Ethena/Resolv industrialised the carry trade, but the *filter logic* — avoiding stretched-funding longs — gains validity as the crowd of carry arbitrageurs grows and crowded longs become more vulnerable to squeezes."

kill_criteria: |
  - strategy drawdown > 25% from high-water mark
  - rolling 6-month Sharpe < 0 on a minimum 20-trade sample
  - signal frequency collapses: fewer than 2 qualifying entries per calendar month over 3 months (funding permanently at extremes or momentum signal decayed)
  - funding filter disagrees with >70% of momentum signals for 60+ days (regime where funding and momentum are structurally anti-correlated; overlay losing information value)

related: ["[[funding-rate-arbitrage]]", "[[oi-confirmed-trend]]", "[[crowded-long-funding-fade]]", "[[crowded-short-funding-fade]]", "[[trend-following-cta]]", "[[momentum-rotation]]", "[[breakout-trading]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Funding-Filtered Momentum

Funding-filtered momentum is a [[breakout-trading|breakout]] and [[trend-following-cta|trend-following]] strategy on crypto perpetuals that uses the prevailing [[funding-rate]] as a positioning filter: it blocks new longs when funding is stretched positive (the crowd is already long and paying for the privilege) and upweights entries when momentum is positive but funding is flat or negative (a non-consensus trend where institutional or informed capital may be leading retail). The primitive edge is momentum persistence; the overlay is a crowding-cost and squeeze-risk screen derived from the funding mechanism.

This is differentiated from [[crowded-long-funding-fade]] — that strategy *fades* momentum when funding is stretched. This page *rides* momentum when funding is *not* stretched, capturing the subset of momentum moves most likely to persist without a crowded-unwind penalty.

## Edge source

Per [[edge-taxonomy]], this is a **behavioral + structural** hybrid:

- **Behavioral (primary)** — [[perpetual-futures]] retail longs systematically bid perps above spot when they are bullish, expressing the same overconfidence and leverage preference documented in BIS Working Paper 1087 (*Crypto carry*, Schmeling, Schrimpf, Todorov 2023). When funding is highly positive the crowd has already acted on a bullish view; the marginal entrant is late, paying crowding costs, and exposed if sentiment shifts. Filtering to low-funding momentum identifies the regime where the crowd has *not* yet front-run the move — behavioral edge is strongest when the trade is non-consensus.
- **Structural (secondary)** — the funding mechanism creates a contractually enforced drag on the long side during high-funding regimes: longs must periodically pay shorts regardless of price action. A new long entered at +0.10%/8h is paying ~110% APY in funding overhead — a constant head wind. Filtering these entries away removes a structural cost that compresses the strategy's net carry.

## Why this edge exists

Three mechanisms reinforce each other:

1. **Crowding penalty on late longs.** When BTC funding exceeds 0.05%/8h, the pool of potential new longs willing to pay that rate shrinks; the marginal buyer is a more aggressive or irrational participant. Historical momentum research (Moskowitz, Ooi, Pedersen 2012; various crypto replications) shows momentum is weakest immediately following periods of extreme one-sided positioning — the "crowded momentum" problem.
2. **Squeeze asymmetry.** A perp long entered into a crowd of other longs faces a squeeze risk: if price dips and the crowd of leveraged longs liquidates, the liquidation cascade overshoots to the downside, amplifying the loss. A momentum entry made when shorts are the crowded side (funding flat or negative) has a different asymmetry — a short squeeze can accelerate the upward move in the entrant's favour.
3. **Non-consensus trend persistence.** Institutional accumulation in crypto often precedes retail FOMO by days to weeks (observable via on-chain exchange outflows and large-cap OI growth). A trend that develops while funding is still flat or negative is more likely to reflect informed-money buying before retail piles in. That early-stage trend tends to have more continuation than a trend that starts when everyone is already long.

**Who is on the other side:** the late retail participant who enters a trend after it has already crowded the funding book, paying ~30-110% APY in funding overhead plus bearing the full squeeze risk.

## Null hypothesis

Under the null — no filtering value — the funding rate at entry carries zero information about forward momentum performance. Specifically:

- Average forward 10-day returns on momentum signals should be equal regardless of whether funding at entry was above or below a threshold.
- The Sharpe of a funding-filtered signal set should be statistically indistinguishable from an unfiltered signal set on the same assets and period.
- Win rates and average win/loss ratios should not differ meaningfully across funding quintiles at entry.

The null is currently not rejected in this wiki (strategy is `backtest_status: untested`). Testable prediction: sort historical momentum entries by funding quintile at entry; the lowest funding quintile should show materially better forward Sharpe than the highest quintile. Costs must be included; the filter's benefit is structural (lower funding drag), not just return — so net-of-funding-cost P&L is the right metric.

## Rules

### Entry conditions (long)

1. **Momentum signal active.** Price has broken above a defined momentum threshold — either a N-day channel high breakout (e.g. 20-day Donchian), a fast/slow EMA crossover (e.g. 12/26 EMA on 4h), or a positive 20-day rate-of-change reading. All three approaches are compatible with the overlay; choose one consistently.
2. **Funding gate: NOT stretched positive.** 8h funding rate at the time of entry is ≤ **0.04%** (~44% APY) on the primary venue. At elevated levels beyond this threshold, skip the entry. Rationale: funding ≤ 0.04% means the long side is not yet paying a large crowding premium; the trend is not universally consensus.
3. **OI gate: not collapsing.** 24h rolling [[open-interest]] change is non-negative or only mildly negative (> −5% from prior day). Collapsing OI into a breakout signals a short-covering squeeze, not a genuine new-money trend — a more fragile setup.
4. **No regime kill active.** The current market-wide regime (from `/api/v1/regimes/current`) is not `Established Bear` or `Structural Shock`; funding-filtered momentum underperforms in outright bear regimes even at flat funding.

### Entry conditions (short)

Mirror of the long rules with reversed funding logic: enter short momentum (price below N-day low / bearish EMA cross) only when funding is ≥ **−0.04%** (shorts are not already crowded). Avoid adding to a bearish momentum move when funding is deeply negative (the crowd is already short and a squeeze is a primary risk).

### Exit conditions

1. **Momentum signal reverses** (price breaks back below the entry level, or EMA crosses back).
2. **Funding becomes stretched against position** — for longs: funding rises above **0.08%/8h** (≥88% APY); consider cutting or trimming. For shorts: funding falls below **−0.08%/8h**.
3. **Time stop**: if entry has not shown positive mark-to-market within **10 trading days**, close at market — the signal may have been a false breakout.
4. **Kill criteria** (see frontmatter) — drawdown or rolling Sharpe thresholds trigger full strategy pause.

### Position sizing

- Base position = (target risk bps × sleeve capital) / (ATR × contract face value). Use ATR(14) on the 4h chart.
- **Vol-scale modifier**: optionally multiply by `1 / (realized_vol_20d / target_vol)` to target equal-risk across different volatility regimes. This is the vol-targeting overlay described in [[vol-targeted-trend-following]] — the two can be stacked.
- **Funding upweight**: when entry funding is ≤ **0.01%/8h** (≤11% APY) AND momentum is confirmed AND OI is rising, apply a 1.25× multiplier (non-consensus trend bonus).
- Maximum single-position size: 10% of sleeve.
- Concurrent positions: maximum 3 crypto assets to bound monitoring complexity.

## Implementation pseudocode

```python
# funding_filtered_momentum.py — decision loop
from dataclasses import dataclass

# ---- thresholds ----
MOMENTUM_LOOKBACK    = 20      # N-day channel high/low for breakout detection
EMA_FAST, EMA_SLOW   = 12, 26  # EMA period lengths (4h bars)
FUNDING_MAX_LONG     = 0.0004  # 0.04% / 8h: block longs above this
FUNDING_MAX_SHORT    = -0.0004 # -0.04% / 8h: block shorts below this
FUNDING_IDEAL_LONG   = 0.0001  # <= 0.01% / 8h: non-consensus bonus
FUNDING_KILL_LONG    = 0.0008  # 0.08% / 8h: exit longs
OI_MIN_CHANGE        = -0.05   # OI cannot be collapsing more than 5% per day
ATR_PERIOD           = 14
TARGET_RISK_PCT      = 0.01    # risk 1% of sleeve capital per trade
UPWEIGHT_FACTOR      = 1.25
MAX_POS_PCT          = 0.10
MAX_CONCURRENT       = 3
DRAWDOWN_KILL        = 0.25
SHARPE_KILL          = 0.0     # rolling 6-month Sharpe floor
TIME_STOP_DAYS       = 10

@dataclass
class Signal:
    asset: str
    price: float
    ema_fast: float; ema_slow: float
    channel_high_20d: float; channel_low_20d: float
    funding_8h: float          # current 8h funding rate
    oi_change_24h_pct: float   # OI % change over 24h
    atr_4h: float
    days_since_entry: int       # 0 if not in position

def momentum_long(s: Signal) -> bool:
    return s.price > s.channel_high_20d and s.ema_fast > s.ema_slow

def momentum_short(s: Signal) -> bool:
    return s.price < s.channel_low_20d and s.ema_fast < s.ema_slow

def decide(s: Signal, book: dict) -> dict:
    if book["sleeve_drawdown"] > DRAWDOWN_KILL:
        return {"action": "FLATTEN_ALL", "reason": "drawdown kill"}

    pos = book["positions"].get(s.asset)

    # ---- exits for existing positions ----
    if pos is not None:
        side = pos["side"]
        if side == "long" and s.funding_8h > FUNDING_KILL_LONG:
            return {"action": "EXIT", "asset": s.asset, "reason": "funding too stretched for long"}
        if side == "short" and s.funding_8h < -FUNDING_KILL_LONG:
            return {"action": "EXIT", "asset": s.asset, "reason": "funding too stretched for short"}
        if side == "long" and not momentum_long(s):
            return {"action": "EXIT", "asset": s.asset, "reason": "momentum reversed"}
        if side == "short" and not momentum_short(s):
            return {"action": "EXIT", "asset": s.asset, "reason": "momentum reversed"}
        if s.days_since_entry >= TIME_STOP_DAYS and pos["unrealized_pnl"] <= 0:
            return {"action": "EXIT", "asset": s.asset, "reason": "time stop — no profit in window"}
        return {"action": "HOLD", "asset": s.asset}

    # ---- entries ----
    if len(book["positions"]) >= MAX_CONCURRENT:
        return {"action": "WAIT", "reason": "max concurrent"}

    if momentum_long(s) and s.funding_8h <= FUNDING_MAX_LONG and s.oi_change_24h_pct >= OI_MIN_CHANGE:
        multiplier = UPWEIGHT_FACTOR if s.funding_8h <= FUNDING_IDEAL_LONG else 1.0
        notional = min(
            TARGET_RISK_PCT * book["sleeve_capital"] / (s.atr_4h / s.price),
            MAX_POS_PCT * book["sleeve_capital"]
        ) * multiplier
        return {"action": "LONG", "asset": s.asset, "notional": notional,
                "reason": f"momentum breakout, funding {s.funding_8h*100:.4f}%/8h (clear)"}

    if momentum_short(s) and s.funding_8h >= FUNDING_MAX_SHORT and s.oi_change_24h_pct >= OI_MIN_CHANGE:
        multiplier = UPWEIGHT_FACTOR if s.funding_8h >= -FUNDING_IDEAL_LONG else 1.0
        notional = min(
            TARGET_RISK_PCT * book["sleeve_capital"] / (s.atr_4h / s.price),
            MAX_POS_PCT * book["sleeve_capital"]
        ) * multiplier
        return {"action": "SHORT", "asset": s.asset, "notional": notional,
                "reason": f"momentum breakdown, funding {s.funding_8h*100:.4f}%/8h (clear)"}

    return {"action": "WAIT", "reason": "signal or filter not met"}
```

The production system adds: regime check via `/api/v1/regimes/current` before each signal; real-time funding polling via the CryptoDataAPI derivatives endpoint; daily P&L accounting; and a manual kill switch.

## Indicators / data used

- **Price momentum** — 20-day channel high/low (Donchian) or EMA(12)/EMA(26) crossover on 4h bars.
- **[[funding-rate]] (8h)** — the core filter signal. Entry gate and exit trigger.
- **[[open-interest]] (24h change)** — OI gate confirms fresh money behind the move.
- **ATR(14) on 4h** — position sizing denominator.
- **Regime classification** — `/api/v1/regimes/current` to avoid entering trend signals in bear/shock regimes.

## Example trade

**Setup (illustrative, not a historical backtest):**

- Asset: SOL-PERP on Hyperliquid, 4h chart.
- Price: $145 (2026-04-05). 20-day channel high: $142 — price broke above on 4h bar close. EMA(12) crossed above EMA(26) three bars ago.
- Funding (8h): **+0.008%** (~8.8% APY annualised). Gate: 0.008% ≤ 0.04% → **PASS**.
- OI 24h change: +3.2%. Gate: +3.2% ≥ −5% → **PASS**.
- Regime: `/regimes/current` → "Early Recovery". Gate: not Bear or Shock → **PASS**.
- Sleeve capital: $50,000. ATR(14) on 4h = $4.20. Target risk = 1% = $500. Size = 500 / (4.20 / 145) = 500 / 0.029 ≈ $17,241 notional. Below 10% cap ($5,000 hard cap applied: final notional $5,000 for illustration). Non-consensus bonus: funding ≤ 0.01% → 1.25× → $6,250 notional.

**Entry:** Long SOL-PERP at $145, $6,250 notional, Hyperliquid maker order (0.02% fee ≈ $1.25).

**Hold (8 days):** SOL rallies to $163 (+12.4%). Funding remains +0.012%/8h throughout — still below the 0.04% gate; no exit triggered. Funding cost over hold period: 0.012% × 24 periods × $6,250 ≈ $18.

**Exit (day 8):** 20-day channel high has moved; price pulls back to $157. EMA(12) crosses below EMA(26). Momentum signal reverses → exit. Hyperliquid taker $157 × $6,250/$145 ≈ 43.1 SOL × 0.045% ≈ $2.73.

**Net P&L:** Entry: $6,250 at $145. Exit: ~$157 equivalent notional. Directional gain: ($157−$145)/$145 × $6,250 ≈ +$517. Minus: entry $1.25 + exit $2.73 + funding drag $18 = $21.98. **Net ≈ +$495 on $6,250 deployed in 8 days (~10.0% in 8 days, ~458% annualised — illustrative, exceptional result; realistic expectation is 0.9 Sharpe on a per-year basis)**. Entry at high-funding ($0.08%/8h) would have incurred ~$120 in funding drag, cutting net P&L by 24%.

*(This is an illustrative round-trip. Actual results will vary. Not investment advice.)*

## Performance characteristics

Cost-corrected picture — conservative, based on strategy design principles and analogous momentum work:

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.9 | Momentum Sharpe typically 0.4-0.7 unfiltered; filter adds ~0.2-0.3 by removing crowded entries |
| Expected max drawdown | ~25% | Momentum drawdowns are driven by whipsaws in choppy regimes |
| Win rate (per signal) | ~45-55% | Momentum: low win rate, right-skewed P&L |
| Avg win / avg loss | ~2.0-3.0× | Trend continuation produces large wins; filter improves by removing late entries |
| Breakeven cost budget | 30 bps round-trip | Perp taker 4.5 bps (Hyperliquid) × 2 + spread + rebalance |
| Funding drag reduction | ~10-40 bps per trade saved | The main quantifiable benefit of the filter |

**Cost overlay (Hyperliquid):**
- Perp taker: ~0.045% × 2 legs = ~9 bps (or 2-4 bps with maker fills)
- Slippage: <2 bps on majors, 5-15 bps on mid-caps
- Funding saved vs unfiltered: variable but 10-120 bps per trade depending on funding level avoided

**What the filter buys (rough estimate):** In bull regimes where funding averages 0.03-0.08%/8h, momentum signals that would have been blocked by the 0.04% gate carry an average funded drag of ~60 bps per 10-day hold period (0.06%/8h × 3 × 10 days × 100). Skipping ~40% of momentum signals due to high funding can reduce average hold-period costs by ~24 bps per signal — meaningful relative to a 30 bps round-trip budget.

## Capacity limits

- **Per-asset on Hyperliquid majors (BTC/ETH/SOL)**: ~$20-50M notional before momentum signal execution becomes self-reinforcing (creates the very trend it's trading).
- **Cross-asset in a universe of 10-20 perps**: ~$100M combined.
- **Hard constraint**: as position size grows, entry must shift from taker to maker, increasing the risk of not getting filled at the breakout price.
- The strategy is moderate-capacity — above ~$5M per asset, execution quality degrades meaningfully. `capacity_usd` in frontmatter reflects a top-end aggregate estimate.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Crowding of the filter itself (#4).** If enough traders adopt the same funding-filtered entry logic, they pile into non-consensus trends simultaneously, making those trends consensus immediately — at which point the filter stops being predictive. The 2024-2025 proliferation of Coinglass dashboards and CDA funding APIs makes this a real medium-term risk.
2. **Regime change: chop (#5).** In low-trend, high-whipsaw markets (ADX < 15, multiple false breakouts per week), momentum itself has no edge; the filter cannot save a broken primitive. This is the dominant risk for any momentum strategy.
3. **Funding regime structural change (#5).** If funding rates compress permanently toward zero (as Ethena/Resolv approach saturation), the filter may block very few signals (everything is below 0.04%) — it becomes inert and the strategy degrades to unfiltered momentum.
4. **Flash-crash squeeze risk (#6).** Even with low-funding entries, a large liquidation cascade can invalidate a trend entry in hours. The time stop and ATR-based sizing contain this; they do not eliminate it.
5. **Backtest overfitting (#4 / methodology).** The specific thresholds (0.04%, 0.08%) are chosen by design logic, not by fitting to historical data — but any backtest that optimizes them will overfit. Walk-forward validation with unseen funding regimes is required before live deployment.

## Kill criteria

Pause (not retire) on any of:

1. **Sleeve drawdown > 25%** in any rolling 30-day window.
2. **Rolling 6-month Sharpe < 0** on a minimum 20-trade sample.
3. **Signal frequency collapse**: fewer than 2 qualifying entries per calendar month over 3 consecutive months.
4. **Filter divergence**: funding filter disagrees with (blocks) > 70% of all momentum signals for 60+ consecutive days — indicator that the funding and momentum regimes have become structurally anti-correlated and the overlay no longer has information value.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Removes the single largest avoidable cost** of crypto momentum: paying crowd-premium funding on entries made when the trade is already consensus.
- **Inverts squeeze asymmetry**: low-funding long entries have a short-squeeze tailwind rather than a liquidation-cascade headwind.
- **Simple, single additional data point**: the filter requires only the funding rate at entry — no exotic data, no complex model.
- **Stackable**: compatible with a vol-targeting overlay (see [[vol-targeted-trend-following]]) and an OI confirmation gate (see [[oi-confirmed-trend]]).
- **Self-funding research signal**: if the filter *never* fires (always blocking signals), that itself is valuable market information: the crowd is perpetually long, a contrarian signal for the book.

## Disadvantages

- **Reduces signal frequency**: in strong bull markets where funding is persistently above the threshold, the strategy may produce few to no entries — exactly when momentum strategies usually return their best absolute results. The filter trades expected Sharpe for signal count.
- **Asymmetric on the long side**: the filter is most active during uptrends (positive funding), so it systematically reduces long-side participation relative to unfiltered momentum in strong bull regimes. Short-side participation in bear regimes (when funding is flat/negative) is relatively unfiltered.
- **Backtest look-back sensitivity**: the right funding threshold is regime-dependent; 0.04%/8h was generous in 2024 but may be too tight in a post-Ethena world where 0.01% is the new normal. Thresholds must be revisited.
- **Does not improve the primitive's null**: if momentum has no alpha at all, the filter improves cost, not edge. The combination is only as good as the underlying momentum signal.

## Sources

- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (BIS, 2023). The empirical basis for funding as a crowding signal: carry is explained by leveraged retail demand and limited arb capital. https://www.bis.org/publ/work1087.pdf
- Moskowitz, T., Ooi, Y., Pedersen, L. (2012), *Time series momentum*, Journal of Financial Economics. Foundational momentum evidence across asset classes; the filter's motivating hypothesis is that momentum is weakest following crowded positioning periods.
- He, Manela, Xu, Yan (2022/2024), *Fundamentals of Perpetual Futures*. Documents mean absolute perp-vs-index deviations; the funding mechanism is the contractual cost the filter saves. arxiv.org/abs/2212.06888.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange 8h funding (Binance + Hyperliquid), the core filter input
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange OI for the OI gate
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — long/short account ratio as a secondary crowding check
- `GET /api/v1/regimes/current` — current 10-state market regime for regime kill

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding history for backtest signal reconstruction
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding + OI together)
- `GET /api/v1/backtesting/funding` — deep funding archive (2020+) for multi-regime backtests
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=4h&limit=200` — OHLCV for momentum signal computation

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=SOL"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]], [[cryptodataapi-regimes]].

## Related

- [[funding-rate-arbitrage]] — the funding-carry primitive; shares the same data rail
- [[funding-rate]] — the underlying contract mechanism and its sign conventions
- [[crowded-long-funding-fade]] — the inverse combination (fade momentum when funding IS stretched)
- [[oi-confirmed-trend]] — complementary OI-based filter on Hyperliquid trend entries
- [[trend-following-cta]] — the underlying momentum primitive
- [[momentum-rotation]] — cross-sectional momentum rotation, combinable with the funding filter
- [[vol-targeted-trend-following]] — stackable vol-sizing overlay on the same momentum primitive
- [[breakout-trading]] — the entry-signal mechanics used in the rules above
- [[perpetual-futures]] — the instrument carrying the funding mechanism
- [[edge-taxonomy]] — where behavioral and structural edges sit
- [[failure-modes]] — crowding and regime-change risks mapped to this strategy
- [[when-to-retire-a-strategy]] — kill vs pause framework
