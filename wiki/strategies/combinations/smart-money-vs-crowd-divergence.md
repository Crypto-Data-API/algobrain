---
title: "Smart-Money vs Crowd Divergence"
type: strategy
created: 2026-07-19
updated: 2026-10-17
status: good
tags: [combinations, meta-strategy, on-chain, funding-rate, perpetual-futures, behavioral-finance, informational-edge, mean-reversion, quantitative, crypto, bitcoin]
aliases: ["On-Chain vs Crowd Divergence", "Smart-Money Accumulation Funding Fade", "Informed Flow vs Leverage Crowd", "Whale-Accumulation Short-Squeeze Setup"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [informational, behavioral, structural]
edge_mechanism: "On-chain smart money (large non-exchange wallet accumulators) buys into weakness while the leveraged perp crowd is simultaneously positioned short (negative/flat funding, elevated short/long ratio) — when informed accumulation is confirmed on-chain while the crowd is bearishly positioned in derivatives, the setup is a squeeze in both dimensions: the on-chain bid absorbs spot supply as the short book faces increasing cost and forced covering pressure; the strategy goes long into this divergence and exits when the squeeze normalises positioning."

data_required: [exchange-netflow, whale-score, on-chain-flows, funding-rates, open-interest, long-short-ratio, ohlcv-daily, ohlcv-4h]
min_capital_usd: 10000
capacity_usd: 50000000
crowding_risk: low

expected_sharpe: 1.0
expected_max_drawdown: 0.22
breakeven_cost_bps: 25

decay_evidence: "On-chain smart-money tracking is well-documented as decaying once wallets become widely followed (see on-chain-smart-money-tracking). However, this strategy uses aggregate whale accumulation scores and exchange-flow metrics rather than individual wallet copy-trading — the aggregate signal is less susceptible to individual wallet crowding. The funding/positioning divergence component has no published crypto study on this exact combination; the BIS crowding-signal framework (Schmeling, Schrimpf, Todorov 2023) provides the conceptual basis."

kill_criteria: |
  - strategy drawdown > 22% from high-water mark
  - 5 consecutive divergence signals where on-chain accumulation was confirmed but price continued declining ≥ 15% after entry (the on-chain signal is not identifying genuine accumulation — it is identifying distribution masquerading as accumulation)
  - whale-score signal produces a positive reading while exchange inflows are simultaneously elevated (contradiction: large holders are both accumulating off-exchange AND depositing to exchange; signal is ambiguous; pause until signals re-align)
  - rolling 6-month Sharpe < 0 (the on-chain × crowd divergence is not producing a positive expectancy edge)
  - on-chain data latency > 2 hours on 3 consecutive trading days (data pipeline failure; execution becomes stale)

related: ["[[smart-money-orderflow-combo]]", "[[on-chain-smart-money-tracking]]", "[[crowded-short-funding-fade]]", "[[spot-led-momentum-filter]]", "[[onchain-capitulation-confluence]]", "[[funding-flush-reversal]]", "[[oi-flush-reversion]]", "[[exchange-netflow]]", "[[whale-onchain-flows]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[on-chain]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
gates:
  - id: whale_accumulation
    role: entry
    rule: "Gate 1: 7-day whale accumulation score at or above 65/100"
    runnable: false
    note: "The /on-chain/whales family, accumulation-score included, answers 503 (coming soon) and is outside the spec; when it ships it is a categorical ERC-20 signal, not a 0-100 BTC score. /quant/whales tracks Hyperliquid perp accounts of $100k or more, a different population. Needs an external whale-balance feed."
  - id: exchange_outflow
    role: entry
    rule: "Gate 2: BTC 24h exchange outflow in the top quartile of its trailing 30-day range, or 7-day net exchange flow negative"
    runnable: partial
    endpoint: /api/v1/on-chain/exchange-flows/{symbol}
    field: windows.7d.net
    replay: /api/v1/on-chain/exchange-flows/{symbol}/history?start={start}&interval=1h
    replay_field: points[].outflow_24h
    note: "7d leg: windows.7d.net below 0. 24h leg: rank windows.24h.outflow against points[].outflow_24h over 30 days of /history (from 2026-05-28). Coverage is tracked CEX wallets only; per_exchange_24h shows which exchanges report (on 2026-10-17 only Binance carried BTC flow), so this is a partial view of exchange flow."
  - id: funding_flat_or_negative
    role: entry
    rule: "Gate 3: 8h funding at or below 0.00%"
    runnable: true
    endpoint: /api/v1/derivatives/binance/funding-rates?symbol={coin}USDT&limit=21
    field: current_rate
    replay: /api/v1/backtesting/funding?symbol={coin}USDT&exchange=binance&start={start}
    replay_field: data[].funding_rate
    note: "Binance's 8h rate, as on the page's /derivatives/funding-rates."
  - id: ls_short_biased
    role: entry
    rule: "Gate 4a: long/short ratio at or below 0.95"
    runnable: true
    endpoint: /api/v1/derivatives/binance/long-short-ratio?symbol={coin}USDT
    field: long_short_ratio
    note: "Binance global account ratio, the page's source."
  - id: funding_7d_negative
    role: entry
    rule: "Gate 4b: 7-day average 8h funding at or below -0.01%"
    runnable: true
    endpoint: /api/v1/derivatives/binance/funding-rates?symbol={coin}USDT&limit=21
    field: rates[].funding_rate
    replay: /api/v1/backtesting/funding?symbol={coin}USDT&exchange=binance&start={start}
    replay_field: data[].funding_rate
    note: "Mean of the last 21 settlements."
  - id: crowd_short
    role: entry
    rule: "Gate 4: the crowd is short-biased when ls_short_biased or funding_7d_negative holds"
    runnable: true
    input: derived
    inputs: [ls_short_biased, funding_7d_negative]
    note: "The Rules say either leg; the pseudocode instead requires funding at or below 0 AND L/S at or below 0.95. Pick one and log it."
  - id: higher_low_10d
    role: entry
    rule: "Gate 5: no run of lower lows on the daily chart, i.e. at least one higher low in the last 10 days"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=13
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "The pseudocode reads local minima of the last 10 closed daily closes: the latest above the previous one (or fewer than two minima)."
  - id: all_gates
    role: entry
    rule: "Go long only when all five gates hold at once"
    runnable: false
    input: derived
    inputs: [whale_accumulation, exchange_outflow, funding_flat_or_negative, crowd_short, higher_low_10d]
    note: "Blocked by Gate 1: no whale accumulation score is served."
  - id: regime_size_cut
    role: sizing
    rule: "In a Structural Shock or bear-trend regime cut size to 2% and require DVOL to be declining before entry"
    runnable: partial
    endpoint: /api/v1/regimes/current
    field: regime
    replay: /api/v1/regimes/history?from={start}
    replay_field: transitions[].regime
    note: "From the indicator list. Match structural_shock_crisis or established_bear; DVOL direction is items[].dvol_change_24h on /volatility/implied, and the page gives no window for declining. Regime history starts 2026-08-07."
  - id: onchain_health_confirm
    role: filter
    rule: "Secondary confirmation: On-chain Health score at or above 50"
    runnable: true
    endpoint: /api/v1/on-chain/score
    field: score
    note: "From the indicator list, not the five gates. Components with no data (MVRV, whale accumulation) are dropped and the rest renormalised."
  - id: position_size
    role: sizing
    rule: "BTC perp long at 3-5% of portfolio notional, 1-2x leverage, at most 1 open divergence position"
    runnable: true
    input: position
  - id: crowd_long_again_exit
    role: exit
    rule: "Take profit when 8h funding is back above +0.02% and long/short is at or above 1.05"
    runnable: true
    endpoint: /api/v1/derivatives/binance/long-short-ratio?symbol={coin}USDT
    field: long_short_ratio
    note: "Funding leg: current_rate on /derivatives/binance/funding-rates?symbol={coin}USDT at or above 0.0002."
  - id: onchain_reversal_exit
    role: exit
    rule: "Close if the whale score is below 50 for 2 consecutive days and exchange inflows spike"
    runnable: false
    note: "Needs the whale accumulation score (see whale_accumulation). The inflow leg alone is spike_zscore_24h on /on-chain/exchange-flows/{symbol}."
  - id: new_10d_low_stop
    role: stop
    rule: "Close if BTC makes a new 10-day low on a daily close"
    runnable: true
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=12
    field: candles[].close
    replay: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&start={start}
    replay_field: candles[].close
    note: "The pseudocode stops below 0.995 x the lowest close of the 10 days before entry."
  - id: time_exit
    role: exit
    rule: "Close after 30 days if neither target nor stop has been reached"
    runnable: true
    input: position
---

# Smart-Money vs Crowd Divergence

Smart-money vs crowd divergence enters a long position in BTC (or ETH) when **two simultaneous and opposing signals are confirmed**: (1) on-chain smart money — large non-exchange wallets, measured by whale accumulation score and exchange-outflow trends — is actively buying into weakness, AND (2) the leveraged perp crowd is positioned bearishly — negative or flat funding rates, short-biased long/short ratio. The divergence between informed on-chain accumulation and the crowded derivative short creates a setup where the price is likely being absorbed by well-capitalised buyers at the same time that the over-leveraged short book faces increasing squeeze pressure. The strategy goes long into this convergence of on-chain demand with positioning unwind catalyst.

**This is explicitly differentiated from [[smart-money-orderflow-combo]]** — that page combines on-chain smart-money signals with real-time order-flow confirmation (CVD, taker-buy/sell imbalance, Hyperliquid perp book depth). The entry trigger there is short-term order-flow (intraday, scalp-to-swing); the on-chain signal confirms the informed-wallet context. This page uses on-chain accumulation as the primary signal and funding/positioning divergence as the second leg — both are medium-term signals (days to weeks); the entry is a swing entry into the divergence setup, not an order-flow reaction. There is no order-flow component here.

**This is differentiated from [[crowded-short-funding-fade]]** — that page enters long when the derivative crowd is bearishly crowded (negative funding, short-biased positioning) based on **positioning alone**. It does not require any on-chain accumulation confirmation; the fade is purely a positioning-exhaustion play. This page requires the on-chain accumulation confirmation as a necessary condition: the crowd is short AND informed money is buying. The on-chain confirmation distinguishes a genuine bottom from a falling knife where shorts are merely piling in on justified bearishness.

**This is differentiated from [[onchain-capitulation-confluence]]** — that page requires BOTH on-chain capitulation signals (SOPR ≤ 0.97, exchange inflow spike) AND a sentiment extreme (Fear & Greed ≤ 20), specifically for cycle-bottom entries at multi-month lows. This page targets a shorter-duration setup: smart-money accumulation at any point in the cycle when the perp crowd is simultaneously short — not specifically at a cycle extreme. The two strategies operate at different timescales and use different on-chain indicators.

**This is differentiated from [[spot-led-momentum-filter]]** — that page confirms that a momentum move is spot-led (Coinbase premium, flat funding, spot volume growing vs OI) before entering a momentum long. This page enters a long specifically because there is a divergence between smart-money ON-CHAIN accumulation and crowd DERIVATIVE positioning — a contrarian setup, not a momentum confirmation. The triggers are structurally different: spot-led momentum requires a price move already in progress; this page enters into the setup before the price move has occurred.

## Edge source

Per [[edge-taxonomy]], **informational + behavioral + structural**:

- **Informational (primary)** — large non-exchange wallets (whale accumulators) with demonstrated historical accuracy are absorbing supply off-chain. Their activity is visible on the blockchain in real time: exchange outflows, rising wallet balance scores, reduced exchange inflow from these wallets. This is an informational signal — informed large holders acting on their view before the crowd recognises the setup.
- **Behavioral** — the leveraged perp crowd is positioned short based on recent price weakness and momentum signals. This short positioning is reflexively reinforcing: shorts hold because price is falling; price falls partly because shorts are selling; the crowd over-extends its short book beyond what the on-chain supply/demand balance justifies. Behavioral overcrowding in the short direction creates the squeeze fuel.
- **Structural** — negative funding means shorts are paying longs to hold. This carry payment shifts the cost-of-carry disadvantage onto the short side: every hour the price doesn't fall, the short crowd is losing carry. The structural funding payment creates a continuous closing pressure on the short book independent of price movement.

## Why this edge exists

**The divergence captures the gap between two information sets:**

1. **On-chain large holders have a longer time horizon and different information than the futures crowd.** Whale accumulators operating on the blockchain are typically buying with a multi-week to multi-month view; they are absorbing supply from forced sellers, capitalising on illiquid conditions, or accumulating ahead of a catalyst they anticipate. The perp crowd is typically positioning with a multi-hour to multi-day view, reacting to technical signals, liquidation fears, and social sentiment. The two groups are playing on different timescales with different information — the divergence between them is an exploitable signal.

2. **Short squeezes are self-reinforcing once the price begins to recover.** When BTC starts rising from a level where the short book is maximum-extended, every tick up forces marginal shorts to cover. Short covering creates additional buying, which forces more covering, amplifying the initial move. The on-chain accumulation provides the initial bid that ignites the squeeze; the funding carry (shorters paying longs) makes every day of delay more expensive for the shorts.

3. **The combination reduces false entries relative to either signal alone.** A crowded-short signal alone fires in genuine bear markets where the crowd is correctly short. An on-chain accumulation signal alone fires in declining markets where the smart money is premature (trying to catch a falling knife). The combination — accumulation confirmed AND crowd is short — filters for the setup where both signals converge: informed money is absorbing supply at the same time the derivative crowd is wrong-footed.

**Who is on the other side:** the leveraged perp short book — typically retail momentum chasers and late-trend-followers who have built short positions after a decline. They are paying funding to hold their shorts while a well-capitalised buyer is absorbing their spot supply. Their exit (covering) funds the move that the on-chain accumulator anticipated.

## Null hypothesis

Under the null, the on-chain smart-money accumulation signal adds **no incremental predictive power** beyond the crowded-short funding signal alone:
- Long entries where BOTH whale accumulation AND negative funding are confirmed should not produce higher P&L than long entries based on negative funding alone (as in [[crowded-short-funding-fade]]).
- On-chain accumulation score increases should not predict subsequent price appreciation with higher accuracy than the baseline negative-funding mean-reversion signal.
- The false-positive reduction (filtering out falling-knife shorts by requiring on-chain confirmation) should not improve win rate enough to overcome the reduced signal frequency.

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all historical periods where BTC whale-score rose AND funding was below 0.00%/8h simultaneously; compare subsequent 10-day returns to periods where funding was below 0.00% but whale-score was declining. Predict: divergence-confirmed entries show 15–25% higher average 10-day return.

## Rules

### Entry gate (all five conditions must be simultaneously confirmed)

**Gate 1: On-chain smart-money accumulation active**
- Whale accumulation score (7-day rolling) is ≥ **65/100** (elevated accumulation, not neutral).
- Source: ~~`GET /api/v1/on-chain/whales/accumulation-score/BTC`~~ — **disabled** (503 `coming_soon`; unlisted from the spec since 2026-10-09), and ERC-20 only even when live. Substitute (2026-10-17): `GET /api/v1/quant/whales` — the `top_coins[]` row for BTC (`directional_net_usd`, `net_bias`, `long_pct_pctile_30d`) and `summary.by_tag_usd.smart_money.net_usd`. That is Hyperliquid perp positioning of ≥$100k accounts, not on-chain holder accumulation, so the ≥ 65/100 threshold does not carry over and needs recalibrating. Exchange flows are not used here because Gate 2 already reads them.
- *Rationale:* the whale-score measures large non-exchange wallet balance changes; scores ≥ 65 indicate net accumulation by the large-holder cohort over the trailing 7 days.

**Gate 2: Exchange outflows confirming off-exchange accumulation**
- BTC 24h exchange outflows are in the **top quartile** of the trailing 30-day range (large amounts leaving exchanges = HODLing / accumulation, not distribution).
- OR 7-day net exchange flow is negative (net outflow over the week).
- Source: `GET /api/v1/on-chain/exchange-flows/BTC`.
- *Rationale:* exchange outflows confirm that the whale-score accumulation is genuine (coins moving off exchange to cold wallets) rather than a statistical artefact from wallet reshuffling.

**Gate 3: Derivative crowd is bearishly positioned**
- 8h funding rate is ≤ **0.00%/8h** (flat or negative — the crowd is not net long; longs are not paying for exposure).
- Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.
- *Rationale:* flat/negative funding is a necessary (but not sufficient alone) condition for the crowd-short divergence. In itself this is the [[crowded-short-funding-fade]] signal; Gate 4 strengthens it.

**Gate 4: Elevated short positioning in perp market**
- Long/short ratio ≤ **0.95** (shorts are modestly dominant in the perp market).
- OR 7-day average funding is ≤ **−0.01%/8h** (sustained negative funding over a week, not just one reading).
- Source: `GET /api/v1/derivatives/binance/long-short-ratio` and `GET /api/v1/derivatives/funding-rates?coin=BTC`.
- *Rationale:* a single negative funding reading may be noise; a sustained shift toward short-biased positioning combined with the long/short ratio confirms the crowd is genuinely positioned against the on-chain accumulation.

**Gate 5: No structural downtrend that would justify the short crowd**
- BTC price is NOT making consecutive lower lows on the **daily** timeframe over the last 10 days (at least one higher low in the last 10 days).
- Source: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=15`.
- *Rationale:* this gate distinguishes a falling-knife scenario (crowd correctly short in a genuine downtrend) from a consolidation/accumulation scenario (crowd over-extended short while price stabilises). If price is making consistent lower lows, the short crowd may be correct; this gate filters that case out.

### Position sizing and instrument

- **Instrument:** BTC perp long on Hyperliquid or Binance. 1–2× leverage maximum (this is a swing entry into a divergence setup, not a leveraged squeeze play).
- **Size:** 3–5% of portfolio notional per entry.
- **Maximum concurrent:** 1 active smart-money-vs-crowd divergence position (the signal is specific to a single asset/regime state).

### Exit rules

1. **Primary target:** close when funding rate rises back above **+0.02%/8h** AND long/short ratio returns to ≥ **1.05** (crowd has repositioned long — the divergence has resolved; the squeeze has run).
2. **On-chain signal reversal:** close if whale-score drops below **50** for 2 consecutive days AND exchange inflows spike (smart money is rotating out or distributing to exchanges — the accumulation thesis is over).
3. **Stop:** close if BTC makes a new 10-day low (daily close) — the structural-downtrend gate has been breached; the on-chain accumulation thesis is wrong or premature.
4. **Time exit:** close after **30 days** if neither target nor stop has been reached (divergence setups that don't resolve within 30 days are typically stalling rather than setting up for a squeeze).

## Implementation pseudocode

```python
# smart_money_vs_crowd_divergence.py

from dataclasses import dataclass
from typing import Optional

# ---- entry thresholds ----
WHALE_SCORE_MIN           = 65.0    # whale accumulation score >= 65
EXFLOW_QUARTILE_MIN       = 0.75    # 24h outflow in top 25% of 30d range (0.75 = 75th pct)
FUNDING_MAX               = 0.0000  # funding <= 0.00%/8h (flat or negative)
LONG_SHORT_MAX            = 0.95    # long/short <= 0.95 (short-biased)
FUNDING_7D_AVG_MAX        = -0.0001 # 7d avg funding <= -0.01%/8h (sustained negative)
LOWER_LOWS_LOOKBACK       = 10      # check for consecutive lower lows over 10 days

# ---- exit thresholds ----
FUNDING_EXIT_MIN          = 0.0002  # exit when funding >= +0.02%/8h (crowd went long)
LONG_SHORT_EXIT_MIN       = 1.05    # exit when long/short >= 1.05 (crowd repositioned long)
WHALE_SCORE_EXIT_MAX      = 50.0    # close if whale score drops below 50 for 2 days
WHALE_EXIT_DAYS           = 2       # consecutive days below exit threshold
MAX_HOLD_DAYS             = 30

@dataclass
class DivergenceState:
    whale_score_7d:       float   # rolling 7-day whale accumulation score (0-100)
    exflow_24h_pct:       float   # 24h outflow as percentile of 30-day range (0-1)
    exflow_7d_net:        float   # 7-day net flow (negative = net outflow)
    funding_8h:           float
    funding_7d_avg:       float
    long_short_ratio:     float
    daily_closes_10d:     list[float]   # last 10 daily closes (oldest first)

@dataclass
class Position:
    entry_price:          float
    entry_10d_low:        float
    days_held:            int
    whale_below_50_days:  int   # consecutive days whale_score < 50

def has_higher_low(closes_10d: list[float]) -> bool:
    """True if there is at least one higher low in the last 10 days (not consecutive lower lows)."""
    if len(closes_10d) < 3:
        return True  # insufficient data; assume not a confirmed downtrend
    lows = []
    for i in range(1, len(closes_10d) - 1):
        if closes_10d[i] < closes_10d[i-1] and closes_10d[i] < closes_10d[i+1]:
            lows.append(closes_10d[i])
    if len(lows) < 2:
        return True   # fewer than 2 defined lows; not a confirmed downtrend
    return lows[-1] > lows[-2]   # most recent local low is higher than prior = higher low

def all_gates_pass(s: DivergenceState) -> tuple[bool, list[str]]:
    fails = []
    if s.whale_score_7d < WHALE_SCORE_MIN:
        fails.append(f"whale score {s.whale_score_7d:.0f} < {WHALE_SCORE_MIN}")
    exflow_ok = (s.exflow_24h_pct >= EXFLOW_QUARTILE_MIN or s.exflow_7d_net < 0)
    if not exflow_ok:
        fails.append(f"exchange outflows not elevated: 24h pct={s.exflow_24h_pct:.2f}, 7d net={s.exflow_7d_net:.0f}")
    crowd_short_ok = (s.funding_8h <= FUNDING_MAX
                      or s.funding_7d_avg <= FUNDING_7D_AVG_MAX
                      or s.long_short_ratio <= LONG_SHORT_MAX)
    # require BOTH: negative funding AND short-biased long/short
    derivative_divergence = (s.funding_8h <= FUNDING_MAX and s.long_short_ratio <= LONG_SHORT_MAX)
    if not derivative_divergence:
        fails.append(f"crowd not bearishly positioned: funding={s.funding_8h:.4%}/8h, L/S={s.long_short_ratio:.2f}")
    if not has_higher_low(s.daily_closes_10d):
        fails.append("consecutive lower lows on daily — structural downtrend; crowd may be right")
    return len(fails) == 0, fails

def entry_decision(s: DivergenceState, book: dict) -> dict:
    if book.get("active_position"):
        return {"action": "HOLD", "reason": "divergence position already active"}
    ok, fails = all_gates_pass(s)
    if not ok:
        return {"action": "WAIT", "reason": "divergence gates not met: " + "; ".join(fails)}
    size = book["portfolio_capital"] * 0.04   # 4% of portfolio
    entry_low = min(s.daily_closes_10d)
    return {
        "action":        "ENTER_LONG",
        "notional":      size,
        "stop_price":    entry_low * 0.995,   # new 10d low on daily close triggers stop
        "leverage":      1.5,
        "note": (f"divergence confirmed: whale_score={s.whale_score_7d:.0f}, "
                 f"funding={s.funding_8h:.4%}/8h, L/S={s.long_short_ratio:.2f}, "
                 f"exchange outflow pct={s.exflow_24h_pct:.2f}"),
    }

def exit_decision(pos: Position, s: DivergenceState, current_price: float) -> Optional[dict]:
    # profit exit: crowd repositioned long
    if s.funding_8h >= FUNDING_EXIT_MIN and s.long_short_ratio >= LONG_SHORT_EXIT_MIN:
        return {"action": "CLOSE_TARGET",
                "reason": f"divergence resolved: funding={s.funding_8h:.4%}, L/S={s.long_short_ratio:.2f}"}
    # on-chain reversal
    days_below = pos.whale_below_50_days + (1 if s.whale_score_7d < WHALE_SCORE_EXIT_MAX else 0)
    if days_below >= WHALE_EXIT_DAYS:
        return {"action": "CLOSE_ONCHAIN_REVERSAL",
                "reason": f"whale score {s.whale_score_7d:.0f} < {WHALE_SCORE_EXIT_MAX} for {days_below} days"}
    # stop: new 10-day low
    current_10d_low = min(s.daily_closes_10d)
    if current_10d_low < pos.entry_10d_low * 0.995:
        return {"action": "CLOSE_STOP",
                "reason": f"new 10d low {current_10d_low:.0f} below entry 10d low {pos.entry_10d_low:.0f}"}
    # time exit
    if pos.days_held >= MAX_HOLD_DAYS:
        return {"action": "CLOSE_TIME", "reason": f"{MAX_HOLD_DAYS}d time exit"}
    return None
```

The production system adds: a daily whale-score polling loop with the CryptoDataAPI endpoint; a 15-minute funding monitor for real-time crowd positioning; an exchange-flow spike alert integration (to catch the exchange-outflow confirmation signal within hours); and an alert that fires when all five gates pass simultaneously to enable timely entry.

## Indicators / data used

- **Whale accumulation score** — `GET /api/v1/on-chain/whales/accumulation-score/BTC`; 7-day rolling score 0–100; ≥ 65 = active accumulation (Gate 1). This is the primary on-chain signal. *Caveat (2026-09 recheck): the live endpoint returns a categorical `signal` (`accumulating`/`neutral`/`distributing`/`unknown`), not a 0–100 number; is ERC-20-only (not native BTC); and is currently disabled upstream — see the note below and [[cryptodataapi-on-chain]]. Read "≥ 65" here as "signal == accumulating" pending recalibration once the endpoint ships.*
- **Exchange flows** — `GET /api/v1/on-chain/exchange-flows/BTC`; 24h inflow/outflow and 7-day net flow; top-quartile outflow confirms off-exchange accumulation (Gate 2). `GET /api/v1/on-chain/exchange-flows/spike-alerts` for real-time large-transfer confirmation.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; 8h rate and 7-day rolling average; ≤ 0.00%/8h and sustained negative for crowd-short gate (Gate 3).
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio`; ≤ 0.95 = short-biased positioning (Gate 4).
- **Daily OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=15`; trailing 10 daily closes for higher-low check (Gate 5) and stop reference.
- **On-chain health score** — `GET /api/v1/on-chain/score`; composite 0–100; score ≥ 50 adds secondary confirmation that the on-chain environment is not in a structural deterioration phase.
- **Regime** — `GET /api/v1/regimes/current`; if `Structural_Shock` or `Bear_Trend`, reduce size to 2% and require DVOL to also be declining before entry.

*Note (2026-09 recheck): the entire `/on-chain/whales*` family — including `/on-chain/whales/accumulation-score/{symbol}` — is temporarily disabled per the live CryptoDataAPI spec, not just `/on-chain/whales` and `/on-chain/whales/{symbol}`. Use `/on-chain/exchange-flows/spike-alerts` as the live primary on-chain signal; Gate 1 (whale accumulation) currently has no working CryptoDataAPI data source. See [[cryptodataapi-on-chain]] for the disabled-family and ERC-20-only-scope details.*

## Example trade

**Setup (illustrative — post-correction accumulation divergence):**

- BTC has declined from $88,000 to $72,500 (−17.6%) over 3 weeks following macro risk-off.
- **Gate 1:** Whale score 7d = 72 (≥ 65). Large holders have been net accumulating.
- **Gate 2:** 24h exchange outflow = 18,400 BTC (82nd percentile of 30-day range, ≥ 75th). Net 7d exchange flow = −42,000 BTC (net outflow). Gate 2 passes.
- **Gate 3:** 8h funding = −0.008%/8h (negative). 7d avg funding = −0.014%/8h. Gate 3 passes.
- **Gate 4:** Long/short ratio = 0.89 (short-biased, < 0.95). Gate 4 passes.
- **Gate 5:** Daily closes 10 days: [$81K, $79K, $76K, $74K, $73K, $73.5K, $74.2K, $73.8K, $72.8K, $72.5K]. Local lows: $73K, $72.5K. Most recent low ($72.5K) < prior low ($73K) — consecutive lower lows. **Gate 5 fails.**

The entry is blocked: despite the strong on-chain + derivatives divergence, the daily price structure is still making lower lows, suggesting the short crowd may be correct in the near term. The strategy waits.

**3 days later:** Daily closes: [..., $72.5K, $72.8K, $73.5K, $74.0K, $74.5K]. New local lows: $72.5K (the prior), no lower low in the last 3 days. Higher low established. Gate 5 now passes.

**Entry:** All 5 gates pass. Portfolio $150,000. Enter BTC perp long at $74.5K, $6,000 notional (4%). 1.5× leverage = $9,000 notional. Stop: below current 10d low of $72,500 × 0.995 = $72,136.

**Exit — divergence resolves (12 days post-entry):**
- BTC has risen from $74,500 to $84,200 (+13.0%). Funding has risen to +0.025%/8h. Long/short ratio = 1.12. Both exit conditions met.
- P&L: ($84,200 − $74,500) / $74,500 × $9,000 notional = +$1,171. Net of 25 bps costs on $9,000 = −$22.50. **Net P&L: +$1,149** / +0.77% of portfolio.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.0 | On-chain confirmation improves signal quality vs pure funding-fade; lower frequency but higher conviction per signal |
| Expected max drawdown | ~22% | Sequential failed entries in a genuine downtrend; Gate 5 reduces false entries but does not eliminate them |
| Win rate (per signal) | ~55–65% (estimated) | Confluence of two independent signals improves win rate vs single-signal entry |
| Average hold duration | 7–25 days | Divergence setups that work typically resolve within 2–4 weeks; time exit at 30 days |
| Breakeven cost budget | 25 bps | Perp taker fee 4–8 bps × 2 fills = 8–16 bps; funding income on negative-funding long offsets some cost |
| Signal frequency | 6–12 per year | All 5 gates simultaneously active is a rare enough condition that signals are high-selectivity |

**Cost overlay:** the strategy earns funding carry on the long position while funding is negative (shorts paying longs), partially offsetting the entry/exit execution cost. A 30-day long at −0.01%/8h = −0.01% × 3 (8h periods per day) × 30 days = −0.9% cumulative cost to shorts / +0.9% cumulative income to longs. This carry income is a meaningful contribution when added to the price appreciation.

## Capacity limits

- **Per entry:** BTC perp on Binance/Hyperliquid at $6K notional is well within any liquidity constraint.
- **Aggregate:** `capacity_usd: 50000000` reflects the 4% of portfolio sizing rule at $50M AUM = $2M per entry, which is achievable in BTC perp markets without impact.
- **On-chain signal capacity:** the whale-score signal aggregates the top-100 non-exchange holders; this signal does not crowd out as a result of how many traders observe it (unlike individual wallet copy-trading). Capacity is set by perp market depth, not signal scarcity.

## What kills this strategy

1. **Smart money is premature — on-chain accumulation precedes further downside (#1: Primitive degradation).** Well-capitalised buyers are often early; they absorb supply at $72,000 while the market ultimately finds a floor at $58,000. Gate 5 (no consecutive lower lows) reduces this risk but cannot eliminate it — the higher-low formation can be temporary. The stop on a new 10-day low limits the damage.
2. **Exchange-flow signal misidentification (#4: Crowding).** Large exchange outflows are not always accumulation — they can reflect exchange-to-exchange transfers, OTC desk movements, or custody migrations. If a large institutional player moves coins from Binance to Coinbase custody, it registers as an outflow even though no actual accumulation is occurring.
3. **On-chain signal latency (#7: Operational).** On-chain data has a 1–2 hour lag for standard indexers. In a fast-moving market, the on-chain signal fires while the price has already moved 3–5% away from the optimal entry. The strategy must accept some slippage relative to the ideal entry.
4. **Whale-score endpoint instability (#7: Operational).** The entire `/on-chain/whales*` family, including the `accumulation-score` route that used to be the fallback, is currently disabled per CryptoDataAPI, and once re-enabled it is documented as ERC-20-only (not native BTC). Gate 1 currently cannot be evaluated via CryptoDataAPI at all; the strategy must pause or substitute an external whale-tracking source (Nansen/Arkham) until this is resolved.
5. **Structural bear market (#3: Market-structure regime change).** In a genuine prolonged bear market (BTC downtrending for 6+ months), the whale-score may consistently show accumulation (large holders buying throughout the decline) while price continues lower. The combination of on-chain accumulation + crowded shorts fires repeatedly as a false bullish signal in a downtrend. Gate 5 and the regime check partially mitigate this.

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 22%** from high-water mark — sequential failed divergence entries; either the signal quality or the market regime has changed.
2. **5 consecutive divergence entries where price continued ≥ 15% below entry before recovering** — the on-chain signal is not identifying genuine bottom accumulation; smart money is either wrong or being early in a structural downtrend.
3. **Whale-score and exchange-inflow contradiction for 5+ consecutive readings** (whale score ≥ 65 while exchange inflows are also top-quartile) — the on-chain signals are contradicting each other (accumulation score vs distribution flows); pause until signals re-align.
4. **Rolling 6-month Sharpe < 0** — the on-chain × crowd divergence is not producing positive expectancy; the two-signal combination has stopped working.
5. **On-chain data latency > 2 hours for 3 consecutive days** — data pipeline failure renders the signal stale; pause execution until pipeline reliability is restored.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Two-signal confluence filters false entries** — requiring both on-chain accumulation AND derivative crowd short positioning reduces the false-positive rate relative to either signal alone; each signal eliminates different failure modes.
- **Carry income from negative funding on the long** — entering when funding is negative means the long position earns carry while it is held. In a 2–4 week hold at −0.01%/8h funding, the carry contribution is meaningful relative to entry/exit costs.
- **Low crowding risk** — the combination of CryptoDataAPI aggregate on-chain signals with derivative positioning data is not yet a widely deployed systematic strategy. The signal is less crowded than individual wallet copy-trading or single-factor funding fades.
- **Gate 5 prevents knife-catching in downtrends** — requiring at least one higher low on the daily before entry prevents the strategy from deploying capital into a structurally declining market where both signals might be persistently active but wrong.

## Disadvantages

- **On-chain signals are coarse and subject to misidentification** — whale-score and exchange-flow aggregations are prone to false signals (custody transfers, OTC flows, cross-exchange movements). The combination of both on-chain gates (score AND outflow) reduces but does not eliminate false positives.
- **Low signal frequency requires patience** — all 5 gates firing simultaneously is uncommon; the strategy may be idle for months. During idle periods, alternative capital deployment must be considered.
- **Smart money can be and often is early** — large holders have a tolerance for paper losses at the portfolio scale that the strategy's stop-loss does not permit. The strategy must exit positions that smart money holds through; the 30-day time exit and stop-loss may truncate the return relative to simply following smart money with no exit discipline.
- **Data dependency on two distinct systems** — the on-chain layer (CryptoDataAPI whale score + exchange flows) and the derivatives layer (funding, long/short ratio) must both be operational and low-latency simultaneously. A single data-system failure invalidates the entry check.

## Sources

- [[smart-money-orderflow-combo]] — the nearest on-chain + signal combination; explicitly differentiated in the lead as order-flow-based vs this page's positioning-based second leg.
- [[crowded-short-funding-fade]] — the standalone derivative-positioning leg; this page adds on-chain accumulation confirmation to that page's entry logic.
- [[onchain-capitulation-confluence]] — the on-chain + sentiment confluence for cycle-bottom entries; this page uses a subset of on-chain signals for non-extreme, mid-cycle divergence setups.
- [[exchange-netflow]] — the exchange-flow concept underlying Gate 2.
- [[whale-onchain-flows]] — the large-holder on-chain activity concept underlying Gate 1.

## Getting the Data (CryptoDataAPI)

**Live data:**
- ~~`GET /api/v1/on-chain/whales/accumulation-score/BTC` — Gate 1: 7-day rolling whale accumulation score (primary on-chain signal)~~ — **disabled** (503 `coming_soon`; unlisted from the spec since 2026-10-09). Gate 1 substitute (2026-10-17): `GET /api/v1/quant/whales` — the `top_coins[]` row for BTC (`directional_net_usd`, `net_bias`, `long_pct_pctile_30d`) and `summary.by_tag_usd.smart_money.net_usd` (Pro; perp positioning, not on-chain accumulation)
- `GET /api/v1/on-chain/exchange-flows/BTC` — Gate 2: 24h inflow/outflow and 7-day net flow
- `GET /api/v1/on-chain/exchange-flows/spike-alerts` — Gate 2 real-time: large transfer alerts for rapid exchange-outflow confirmation
- `GET /api/v1/on-chain/score` — secondary: on-chain health composite score (context check)
  - **Caveat (2026-10-08 API fix):** before 2026-10-08 the score's `exchange_flow` component summed every tracked token's 24h flow in its own native units, so it pinned at 20 or 80. Any composite reading, or any threshold calibrated on readings, from before that date is biased. The component now scores the USDT/USDC/DAI 24h net only. Components with no data, currently `whale_accumulation`, carry weight 0 and the rest are renormalised; they are not scored a neutral 50. See [[cryptodataapi-on-chain]].
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — Gate 3: 8h funding and 7-day average
- `GET /api/v1/derivatives/binance/long-short-ratio` — Gate 4: account long/short ratio
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=15` — Gate 5: trailing daily closes for higher-low check
- `GET /api/v1/regimes/current` — regime override: reduce size or skip in `Structural_Shock` or `Bear_Trend`

**Historical data:**
- ~~`GET /api/v1/on-chain/whales/accumulation-score/BTC` — historical accumulation score timeseries for signal calibration~~ — **disabled** (503 `coming_soon`; unlisted from the spec since 2026-10-09). Substitute: `GET /api/v1/quant/whales/history?days=180&live_only=true` (daily whale long/short/net notional and top coins by net; Pro Plus; observed points start 2026-06-29, earlier points are modeled)
- `GET /api/v1/derivatives/binance/history?days=90` — extended funding and long/short history for threshold calibration
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=365` — annual daily OHLCV for divergence-signal backtesting

*Note (2026-09 recheck): `/on-chain/whales`, `/on-chain/whales/{symbol}`, AND `/on-chain/whales/accumulation-score/{symbol}` are all currently disabled ("coming soon") per the live spec. Use `/on-chain/exchange-flows/spike-alerts` as the live on-chain signal until the family re-enables.*

```bash
# 2026-10-17: was /api/v1/on-chain/whales/accumulation-score/BTC, disabled (503 coming_soon); Gate 1 substitute below
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/quant/whales"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]], [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this divergence read end-to-end:

- **Signal** — ~~`GET /api/v1/on-chain/whales/accumulation-score/BTC` (7-day accumulation score)~~ (**disabled**: 503 `coming_soon`, unlisted from the spec since 2026-10-09) was the smart-money leg; until it returns, `GET /api/v1/quant/whales` (BTC `directional_net_usd` and the `smart_money` tag) stands in as a perp-positioning proxy; `GET /api/v1/on-chain/exchange-flows/spike-alerts` confirms outflows in real time
- **Crowd leg** — `GET /api/v1/derivatives/funding-rates?coin=BTC` + `GET /api/v1/derivatives/binance/long-short-ratio` establish that the crowd is positioned opposite the whales
- **Regime gate** — `GET /api/v1/regimes/current`; skip or halve size in `Structural_Shock` / bear-trend labels
- **Backtest** — the whale-score endpoint's own historical timeseries is unavailable while the route is disabled (2026-10-17); calibrate the stand-in with `GET /api/v1/quant/whales/history?days=180&live_only=true` and join it to daily klines back to 2017-08 only in the `klines_deep` archive (`GET /api/v1/backtesting/klines`; the REST route starts 2026-05-09) and to point-in-time snapshots (`GET /api/v1/backtesting/daily-snapshots`, since 2026-03-02) for the crowd side
- **Tips** — the whole `/on-chain/whales*` family (including `accumulation-score`) currently returns "coming soon"; run the pipeline on `spike-alerts` + an external whale source and re-probe the family monthly instead of failing the run
- **Prompt library** — the "Whale Positioning Monitor" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) gives the smart-money side of this divergence read

## Related

- [[smart-money-orderflow-combo]] — on-chain smart money + real-time order flow; differentiated as intraday/order-flow vs this page's swing/positioning frame
- [[on-chain-smart-money-tracking]] — individual wallet copy-trading; this page uses aggregate whale scores rather than specific wallet tracking
- [[crowded-short-funding-fade]] — the derivative-positioning leg run in isolation; this page adds the on-chain accumulation confirmation
- [[spot-led-momentum-filter]] — momentum confirmation via cross-venue flow origin; differentiated as momentum-entry vs divergence-entry
- [[onchain-capitulation-confluence]] — on-chain + sentiment for cycle extremes; differentiated by signal type and timescale
- [[funding-flush-reversal]] — funding-flush dip buy without on-chain confirmation; this page's derivative leg is more selective
- [[oi-flush-reversion]] — OI-purge dip buy; adjacent mechanical trigger for similar setup
- [[exchange-netflow]] — the exchange inflow/outflow metric used in Gate 2
- [[whale-onchain-flows]] — large-holder on-chain activity concept
- [[funding-rate]] — the derivative crowd positioning signal
- [[open-interest]] — context metric for position sizing and crowd crowding
- [[on-chain]] — the on-chain data concept category
- [[perpetual-futures]] — the perp instrument for the long position
- [[edge-taxonomy]] — informational + behavioral + structural classification
- [[failure-modes]] — on-chain misidentification, smart money being early, structural downtrend
- [[when-to-retire-a-strategy]] — kill vs pause framework
