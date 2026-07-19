---
title: "Whale Copy-Flow Funding Filter"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, on-chain, funding-rate, behavioral-finance, informational-edge, momentum, quantitative, crypto, bitcoin, ethereum]
aliases: ["Whale Follow Funding Gate", "Copy-Flow Funding Filter", "Informed Flow Anti-Crowding Gate", "Whale Accumulation Uncrowded Entry"]
strategy_type: hybrid
timeframe: swing
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [informational, structural, behavioral]
edge_mechanism: "Whale / large-wallet on-chain accumulation signals (Nansen, Arkham, on-chain-smart-money-tracking) provide an informational edge when they fire before the leveraged derivatives crowd has noticed and followed the move. When the same whale accumulation signal fires while funding is already elevated (> +0.03%/8h), the derivative crowd has preceded the whale signal or is simultaneously piling in — the informational edge has been captured by earlier entrants, crowding risk is high, and the position faces a higher probability of a sentiment-funded squeeze against the entry. The funding filter gates whale-copy entries to the sub-set where funding is flat or negative (crowd not yet positioned long) — preserving the edge by entering BEFORE the crowd follow-through adds its own squeeze risk, rather than after."

data_required: [whale-accumulation-scores, on-chain-wallet-flows, nansen-smart-money, arkham-labels, funding-rates, long-short-ratio, ohlcv-daily, ohlcv-4h, open-interest]
min_capital_usd: 5000
capacity_usd: 20000000
crowding_risk: low

expected_sharpe: 1.1
expected_max_drawdown: 0.20
breakeven_cost_bps: 20

decay_evidence: "On-chain wallet copy-trading is well-documented as a decaying edge when individual wallets become widely tracked (Nansen labels spread to retail; wallet alpha is arbed away). However, this strategy uses aggregate whale accumulation signals (not specific wallet following) combined with a crowd-positioning filter that specifically excludes entry when the crowd has already copied the signal — this filter mechanically reduces the population of signals where the edge has already been distributed to the crowd. The funding gate acts as an anti-crowding check that extends the useful life of the on-chain signal by excluding entries where the informational advantage has already been monetised."

kill_criteria: |
  - rolling 6-month Sharpe < 0 on all funding-filtered whale-copy entries
  - 5 consecutive whale accumulation signals where funding was flat/negative at entry but price continued declining ≥ 12% (the whale signal is not identifying genuine informed accumulation; whales are distributing to each other)
  - whale accumulation data source (Nansen smart money / Arkham / CryptoDataAPI whale score) produces contradictory signals for 5+ consecutive weeks (data reliability failure; pause)
  - funding filter becomes self-defeating: funding is persistently negative (> 80% of days) for 6+ months (all whale signals fire in negative funding; filter no longer provides selectivity)

related: ["[[smart-money-vs-crowd-divergence]]", "[[on-chain-smart-money-tracking]]", "[[copy-trading]]", "[[crowded-short-funding-fade]]", "[[funding-filtered-momentum]]", "[[smart-money-orderflow-combo]]", "[[onchain-capitulation-confluence]]", "[[narrative-crowding-exit]]", "[[funding-rate]]", "[[open-interest]]", "[[perpetual-futures]]", "[[on-chain]]", "[[nansen]]", "[[whale]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Whale Copy-Flow Funding Filter

Whale copy-flow funding filter enters a directional position in BTC or ETH when **two conditions hold simultaneously**: (1) an on-chain whale / large-wallet accumulation signal fires (smart-money wallets are net-buying into weakness or accumulating at current prices), AND (2) the perp funding rate is flat or negative — confirming that the **derivative crowd has NOT yet followed** the whale's move. The funding gate is the anti-crowding check: it ensures the entry is made while the informational edge of the whale signal is still unpriced in the derivatives market, before the crowd's follow-through compresses the remaining spread between current price and the whale's anticipated price target. The counterparty is the late follower who enters the same whale accumulation trade 24–72 hours later when funding has already risen to +0.04–0.06%/8h and most of the edge has been distributed.

**This is differentiated from [[smart-money-vs-crowd-divergence]]** — that page is specifically structured as a long entry when whale accumulation is active AND the derivative crowd is bearishly positioned (negative funding + short-biased L/S ratio). The crowd divergence there is directional: whale is buying while the crowd is short. This page has a different filter: whale is buying while the crowd has not yet followed in either direction (flat funding, not necessarily negative). The structural setup here is earlier in the information propagation cycle: crowd is neutral, not yet short. Smart-money-vs-crowd-divergence requires a crowd-short as a necessary condition; this page requires crowd-neutral. They are complementary: this page fires earlier in the information cascade; smart-money-vs-crowd-divergence fires later when the crowd has overshot to the short side.

**This is differentiated from [[on-chain-smart-money-tracking]]** — that page describes the general practice of tracking specific whale wallets and copying their trades (Nansen, Arkham, DeBank). This page does NOT copy specific wallets; it uses aggregate whale accumulation scores (or flow metrics) as a signal and applies the funding filter to gate entries. The key difference: individual wallet copying decays rapidly as the wallet becomes widely tracked; aggregate whale score + funding filter is more robust because the funding gate explicitly excludes the scenario where the wallet's trades have already been copied by the crowd.

**This is differentiated from [[funding-filtered-momentum]]** — that page uses the funding rate to gate a price-momentum signal: enter momentum long only when funding is not yet crowded (crowd hasn't amplified the move). This page uses the funding rate to gate an on-chain whale accumulation signal, not a price-momentum signal. The two signals fire in different circumstances: momentum requires a price move to already be in progress; whale accumulation may fire before any price move (accumulation precedes price recovery).

**This is differentiated from [[smart-money-orderflow-combo]]** — that page combines on-chain smart-money with real-time order-flow confirmation (CVD, taker-buy/sell imbalance, perp book depth). The second leg there is an intraday order-flow signal; this page's second leg is the multi-hour funding rate. The two strategies are adjacent in their mechanism but distinct in timescale: order-flow combo is intraday/scalp-to-swing; this page is swing-to-position. Different data sources, different hold periods.

## Edge source

Per [[edge-taxonomy]], **informational + structural + behavioral**:

- **Informational (primary)** — Large non-exchange wallets (whale accumulators) with demonstrated historical tracking accuracy are absorbing supply. Their on-chain activity (exchange outflows, rising wallet balance scores) is visible before it prices into derivatives markets.
- **Structural** — Flat or negative funding means the leveraged crowd is not net long (shorts are paying longs, or funding is near-zero indicating no directional positioning premium). The whale's accumulation is thus not yet reflected in derivatives positioning — the structural carry advantage is on the long side (earn funding while crowd is flat/short) rather than against it.
- **Behavioral** — The derivatives crowd is a momentum-follower: it positions in the direction of recent price moves and sentiment. Whale accumulation typically occurs into weakness or at consolidation lows — before the price move that triggers the crowd. The behavioral gap between informed early accumulation and reactive crowd follow-through is the timing window this strategy exploits.

## Why this edge exists

**The information propagation cycle in crypto whale activity:**

1. **T − 2 to 0 (whale accumulation begins):** large wallets begin absorbing supply. On-chain signals fire: exchange outflows rise, whale accumulation score increases. Funding is flat or negative (crowd is not positioned long; no momentum signal in derivatives).
2. **T + 0 (this strategy's entry window):** funding is still flat/negative. Price may be consolidating or weakly declining. The whale accumulation signal is active but not yet widely distributed via Nansen/Arkham labels or social media.
3. **T + 1 to 3 days (crowd discovery):** price begins rising as whale bid absorbs spot supply. Social media and Nansen alert traders notice the whale signal. Retail and systematic followers begin buying spot and longs in perps. Funding starts rising toward +0.02–0.04%/8h.
4. **T + 3 to 7 (crowd crowded):** funding reaches +0.04%/8h+. Long/short ratio shifts above 1.20. Narrative emerges ("smart money buying"). This is where [[funding-filtered-momentum]] refuses entry; [[narrative-crowding-exit]] starts monitoring for exit. The late crowd enters here — when the edge has largely been distributed.

**The funding filter gates entry to Steps T − 2 to 0 and T + 0 to +1:** the entry must occur before the crowd follow-through is visible in derivatives. The funding filter is the real-time detector of "has the crowd already priced in the whale signal?"

**Who is on the other side:** the late derivative-market follower who sees the on-chain whale signal after it has been published by Nansen/Arkham and enters at T + 3 to +7 when funding is elevated. They are entering with the crowd already positioned long, paying elevated funding on their long, into a position where the primary on-chain accumulation may be complete. Their crowded entry funds the exit for early entrants.

## Null hypothesis

Under the null, the funding rate at the time of whale signal entry adds **no incremental predictive power** to the subsequent return:

- Whale accumulation signal entries made when funding ≤ 0.00%/8h (flat/negative) should NOT produce higher subsequent 10-day returns than entries made when funding is elevated (+0.03–0.06%/8h).
- The funding gate should not reduce loss frequency or increase win rate materially relative to entering all whale signals regardless of funding state.

Testable: for all historical BTC whale score ≥ 65 signals (7-day rolling), separate by funding rate at signal date into: (a) funding ≤ 0.00%/8h and (b) funding > 0.00%/8h. Compare 10-day returns. Prediction: group (a) has materially higher average return (the entry is earlier in the information cascade, before crowd crowding has consumed the edge).

Currently untested (not rejected). Adjacent evidence: [[smart-money-vs-crowd-divergence]] documents the directional case (funding ≤ 0.00% AND crowd short confirms the divergence); this page's hypothesis is the weaker, earlier version of that signal.

## Rules

### Entry gate (all three conditions must be simultaneously active)

**Gate 1: Whale / large-wallet accumulation signal active**
- Whale accumulation score (7-day rolling) ≥ **60/100** (active accumulation; lower threshold than smart-money-vs-crowd-divergence's 65 because we do not require simultaneous crowd-short positioning).
- OR: Nansen/Arkham "smart money" category net-bought the asset in the trailing 48 hours by ≥ 0.5% of trailing 30-day average daily volume.
- Source: `GET /api/v1/on-chain/whale-score/BTC` (primary); Nansen or Arkham Intelligence (supplementary, manual check).
- *Rationale:* the whale signal must show genuine accumulation, not noise. Score ≥ 60 is above neutral (50) but does not require the strong 65+ threshold needed for the smart-money-vs-crowd-divergence setup because the funding gate compensates for the lower-conviction whale signal threshold.

**Gate 2: Derivative crowd has NOT yet followed**
- 8h funding rate ≤ **+0.015%/8h** (flat or very slightly positive — crowd is not significantly long yet).
- AND 7-day average funding ≤ **+0.010%/8h** (sustained crowd neutrality — not just a single flat reading in a generally elevated funding environment).
- Source: `GET /api/v1/derivatives/funding-rates?coin=BTC`.
- *Rationale:* the 0.015% ceiling (vs the 0.00% ceiling in smart-money-vs-crowd-divergence) allows entry into slightly positive funding environments where the crowd is modestly long but has not yet fully priced in the whale signal. The 7-day average check prevents entry into situations where funding spiked down temporarily from an otherwise elevated base.

**Gate 3: No structural downtrend that invalidates the whale signal**
- Price is NOT making consecutive lower lows on the **daily** timeframe over the last 7 days (at least one higher low or sideways consolidation visible).
- Source: `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=10`.
- *Rationale:* distinguishes whale accumulation into a genuine floor from whale accumulation that is being overwhelmed by stronger selling (falling knife). Whales are often early; Gate 3 requires at least a stabilisation signal before entry.

### Position sizing and instrument

- **Instrument:** BTC or ETH perp long (Hyperliquid or Binance). 1.5–2× leverage maximum.
- **Size:** 3–4% of portfolio per signal.
- **Maximum concurrent positions:** 2 (BTC and ETH simultaneously if both signal; no more).

### Exit rules

1. **Primary exit (crowd-follow confirmation):** close 60% of position when funding rises above **+0.035%/8h** AND long/short ratio rises above **1.15** (crowd has followed the whale move into derivatives — the follow-through phase has begun; front-run the late entries that will crowd the position).
2. **Hold remainder (20%):** trail with a 5% stop on the residual position into the momentum phase. Close when funding rises above +0.055%/8h or long/short ratio > 1.30 (crowd fully crowded; time to exit completely — see [[narrative-crowding-exit]] logic).
3. **Whale reversal stop:** close entire position if whale score drops below **50** for 2 consecutive days AND exchange inflows spike (whale is distributing rather than accumulating; the thesis has reversed).
4. **Price stop:** close if price makes a new 7-day low on daily close (structural downtrend gate re-triggered; whale is premature or wrong).
5. **Time exit:** close after **25 days** if neither crowd-follow nor stop has triggered.

## Implementation pseudocode

```python
# whale_copy_flow_funding_filter.py

from dataclasses import dataclass
from typing import Optional

# Entry thresholds
WHALE_SCORE_MIN         = 60.0     # whale accumulation score ≥ 60
FUNDING_ENTRY_MAX       = 0.00015  # 8h funding ≤ +0.015% (0.00015 decimal)
FUNDING_7D_AVG_MAX      = 0.00010  # 7d avg funding ≤ +0.010%
LOWER_LOWS_LOOKBACK     = 7        # check for higher low over 7 days

# Exit thresholds — crowd-follow phase
FUNDING_PARTIAL_EXIT    = 0.00035  # 8h funding ≥ +0.035% → exit 60%
LONG_SHORT_PARTIAL_EXIT = 1.15     # L/S ≥ 1.15 → exit 60%
FUNDING_FULL_EXIT       = 0.00055  # 8h funding ≥ +0.055% → exit remaining
LONG_SHORT_FULL_EXIT    = 1.30     # L/S ≥ 1.30 → exit remaining

# Whale reversal exit
WHALE_SCORE_REVERSAL    = 50.0     # whale score < 50 for 2 days → exit
REVERSAL_DAYS_REQUIRED  = 2

# Time exit
MAX_HOLD_DAYS           = 25

@dataclass
class WhaleSignal:
    whale_score_7d:       float   # rolling 7-day whale accumulation score
    funding_8h:           float   # current 8h funding rate (decimal)
    funding_7d_avg:       float   # 7-day average 8h funding rate
    long_short_ratio:     float
    daily_closes_7d:      list[float]   # last 7 daily closes

@dataclass
class Position:
    entry_price:          float
    entry_7d_low:         float
    days_held:            int
    partial_exit_taken:   bool    # True after 60% exit
    whale_below_50_days:  int     # consecutive days below reversal threshold

def has_higher_low_7d(closes: list[float]) -> bool:
    if len(closes) < 4:
        return True
    lows = [closes[i] for i in range(1, len(closes)-1)
            if closes[i] < closes[i-1] and closes[i] < closes[i+1]]
    if len(lows) < 2:
        return True
    return lows[-1] > lows[-2]

def gates_pass(s: WhaleSignal) -> tuple[bool, list[str]]:
    fails = []
    if s.whale_score_7d < WHALE_SCORE_MIN:
        fails.append(f"whale score {s.whale_score_7d:.0f} < {WHALE_SCORE_MIN}")
    if s.funding_8h > FUNDING_ENTRY_MAX:
        fails.append(f"funding {s.funding_8h:.5f} > {FUNDING_ENTRY_MAX} (crowd already long)")
    if s.funding_7d_avg > FUNDING_7D_AVG_MAX:
        fails.append(f"7d avg funding {s.funding_7d_avg:.5f} > {FUNDING_7D_AVG_MAX}")
    if not has_higher_low_7d(s.daily_closes_7d):
        fails.append("consecutive lower lows on 7-day daily — structural downtrend")
    return len(fails) == 0, fails

def entry_decision(s: WhaleSignal, book: dict) -> dict:
    active = book.get("active_positions", 0)
    if active >= 2:
        return {"action": "HOLD", "reason": "max 2 concurrent positions"}
    ok, fails = gates_pass(s)
    if not ok:
        return {"action": "WAIT", "reason": "; ".join(fails)}
    size = book["portfolio_capital"] * 0.035
    return {
        "action":    "ENTER_LONG",
        "notional":  size,
        "leverage":  1.5,
        "stop_ref":  min(s.daily_closes_7d),
        "note": (f"whale={s.whale_score_7d:.0f}, funding={s.funding_8h:.5f}/8h, "
                 f"7d_avg={s.funding_7d_avg:.5f}/8h, L/S={s.long_short_ratio:.2f}"),
    }

def exit_decision(pos: Position, s: WhaleSignal, current_price: float) -> Optional[dict]:
    # Partial exit: crowd follow detected
    crowd_following = (s.funding_8h >= FUNDING_PARTIAL_EXIT
                       and s.long_short_ratio >= LONG_SHORT_PARTIAL_EXIT)
    if crowd_following and not pos.partial_exit_taken:
        return {"action": "PARTIAL_EXIT_60PCT",
                "reason": f"crowd follow: funding={s.funding_8h:.5f}, L/S={s.long_short_ratio:.2f}"}
    # Full exit: crowd fully crowded
    if (s.funding_8h >= FUNDING_FULL_EXIT or s.long_short_ratio >= LONG_SHORT_FULL_EXIT):
        return {"action": "FULL_EXIT",
                "reason": f"crowd crowded: funding={s.funding_8h:.5f}, L/S={s.long_short_ratio:.2f}"}
    # Whale reversal
    days_below = pos.whale_below_50_days + (1 if s.whale_score_7d < WHALE_SCORE_REVERSAL else 0)
    if days_below >= REVERSAL_DAYS_REQUIRED:
        return {"action": "EXIT_WHALE_REVERSAL",
                "reason": f"whale score {s.whale_score_7d:.0f} below {WHALE_SCORE_REVERSAL} for {days_below}d"}
    # Price stop: new 7-day low
    current_7d_low = min(s.daily_closes_7d)
    if current_7d_low < pos.entry_7d_low * 0.998:
        return {"action": "EXIT_STOP",
                "reason": f"new 7d low {current_7d_low:.0f} < entry 7d low {pos.entry_7d_low:.0f}"}
    # Time exit
    if pos.days_held >= MAX_HOLD_DAYS:
        return {"action": "EXIT_TIME", "reason": f"{MAX_HOLD_DAYS}d time exit"}
    return None
```

## Indicators / data used

- **Whale accumulation score** — `GET /api/v1/on-chain/whale-score/BTC`; 7-day rolling 0–100 score; ≥ 60 = Gate 1 active.
- **Exchange flows** — `GET /api/v1/on-chain/exchange-flows/BTC`; 24h net flow and exchange outflow spike alerts; secondary confirmation for Gate 1.
- **Funding rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC`; 8h current rate and 7-day rolling average; ≤ +0.015%/8h (8h) AND ≤ +0.010%/8h (7d avg) = Gate 2.
- **Long/short ratio** — `GET /api/v1/derivatives/binance/long-short-ratio`; ≤ 1.10 at entry confirms crowd neutrality (supplementary gate); used for exit monitoring.
- **Daily OHLCV** — `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=10`; trailing 7 daily closes for Gate 3 (higher-low check) and stop reference.
- **Regime** — `GET /api/v1/regimes/current`; reduce size to 2% in `Bear_Trend` or `Structural_Shock` regimes.
- **Nansen / Arkham** — external, manual check; these are not CryptoDataAPI endpoints. Nansen (`nansen.ai`) and Arkham Intelligence (`arkhamintelligence.com`) provide labeled wallet analytics for supplementary whale signal confirmation.

*Note: `/on-chain/whales` and `/on-chain/whales/{symbol}` are temporarily disabled per CryptoDataAPI docs. Use `/on-chain/whale-score/{symbol}` and `/on-chain/exchange-flows/spike-alerts` as the primary on-chain signals. Nansen/Arkham are supplementary, not required.*

## Example trade

**Setup (illustrative — whale accumulation ahead of crowd)**

- BTC has consolidated at $65,000–$68,000 for 3 weeks following a −18% drawdown from $80,000.
- **Gate 1:** whale score 7d = 64 (≥ 60). CryptoDataAPI `/whale-score/BTC` shows rising score over 5 days.
- **Gate 2:** 8h funding = +0.008%/8h (near-zero, slightly positive). 7d avg funding = +0.006%/8h. Both below thresholds. Crowd is not positioned long. Gate 2 PASSES.
- **Gate 3:** Daily closes 7d: [$68K, $66K, $65.5K, $65.2K, $65.8K, $66.2K, $67.0K]. Pattern: declined to $65.2K, then bounced to $67.0K. Higher low at $65.8K vs prior low at $65.2K. Gate 3 PASSES.
- All gates pass. Portfolio $200,000. Entry: 3.5% × $200K = $7,000 notional, 1.5× leverage = $10,500 BTC perp long at $67,000. Stop: 7-day low = $65,200 × 0.998 = $65,070.

**Day 4 post-entry:**
- BTC has risen to $72,500 (+8.2%). Funding has risen to +0.038%/8h (Gate 2 would now fail). Long/short ratio = 1.18 (crowd is following the whale move). Both partial-exit conditions triggered.
- **Partial exit:** sell 60% of position at $72,500. P&L on 60%: ($72,500 − $67,000) / $67,000 × $10,500 × 60% = **+$521**. Net of 20 bps costs: **+$500**.
- Hold remaining 40% with 5% trailing stop.

**Day 9 post-entry:**
- BTC at $76,200. Funding at +0.058%/8h (≥ +0.055% full-exit trigger). Long/short ratio = 1.34.
- **Full exit:** close remaining 40% at $76,200. P&L on 40%: ($76,200 − $67,000) / $67,000 × $10,500 × 40% = **+$577**.
- **Total trade P&L: +$1,077** / +0.54% of portfolio.

*(Illustrative round numbers. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~1.1 | Funding gate improves win rate vs unconstrained whale following; lower frequency than pure funding-filtered momentum |
| Expected max drawdown | ~20% | Sequential failed entries where whales are premature in a structural downtrend |
| Win rate (per signal) | ~55–65% (estimated) | Whale + funding gate combination filters false entries; lower than smart-money-vs-crowd-divergence's ~55–65% due to higher signal frequency |
| Average hold duration | 7–25 days | Crowd-follow phase triggers partial exit in 3–10 days; residual held 5–15 days more |
| Breakeven cost budget | 20 bps | Perp taker fee 4–8 bps × 3 fills (entry + partial exit + full exit); earn funding carry while crowd is flat/negative |
| Signal frequency | 12–20 per year | Lower threshold (whale score ≥ 60 vs 65) + less restrictive funding ceiling → more frequent than smart-money-vs-crowd-divergence |

**Cost overlay:** earning carry while funding is flat/slightly negative on the long position partially offsets execution costs. At 0.00%/8h funding over a 7-day hold: neutral carry. If funding turns negative after entry (crowd goes short while whale holds), longs earn carry — additional tailwind that smart-money-vs-crowd-divergence also captures.

## Capacity limits

- **Per signal:** $7K notional ($200K portfolio × 3.5%) is well below BTC perp depth on Binance/Hyperliquid.
- **Aggregate:** `capacity_usd: 20000000` — at $20M AUM, $700K per entry is still within normal BTC perp market depth. ETH per entry is also within market depth at this scale.
- **Signal capacity:** the whale accumulation score aggregates large non-exchange holders; the aggregate signal doesn't crowd out as individual wallet copy-trading does. Capacity is set by market depth, not signal scarcity.

## What kills this strategy

1. **Whale score aggregates distribution masquerading as accumulation (#4: Crowding / data).** Large wallets shuffling coins between self-custodied wallets (cold storage reorganisation, OTC desk settlement) registers as accumulation (exchange outflow, rising wallet balance score) without representing genuine buying. The exchange-flow confirmation (Gate 1 secondary) reduces but does not eliminate this risk.
2. **Funding filter too permissive — crowded entry when 7d avg is high (#4: Crowding).** If the 7d average funding is consistently elevated (bull market phase), the 7d avg ≤ +0.010% gate filters out most signals. The strategy becomes inactive during bull-market phases — which may be the correct behavior (less edge when crowd is already positioned long) but frustrates operators looking for activity.
3. **Smart money is structurally early in a bear market (#1: Primitive degradation).** Large holders begin accumulating at what they believe are cycle lows, but price continues declining for months. Whale score fires repeatedly with positive signals (genuine accumulation by conviction buyers) while price continues to new lows. Gate 3 (higher low required) mitigates but cannot fully prevent entries in extended bear phases.
4. **Nansen / Arkham label pollution (#4: Crowding).** As specific wallet labels become widely tracked, the "smart money" wallet set on Nansen/Arkham accumulates followers. If the aggregate score in CryptoDataAPI is derived from wallet sets that are widely published, the informational advantage degrades. Mitigation: use the CryptoDataAPI aggregate score (large non-exchange holder cohort) rather than specific wallet following.

## Kill criteria

Pause or retire on any of:

1. **Rolling 6-month Sharpe < 0** on funding-filtered whale-copy entries.
2. **5 consecutive entries where funding was ≤ +0.015%/8h at entry but price declined ≥ 12% before recovering** — either the whale signal is identifying premature accumulation or the higher-low gate is failing; reassess.
3. **Whale accumulation data contradicts exchange-flow data for 5+ consecutive weeks** (whale score ≥ 60 while exchange inflows are simultaneously elevated) — data source unreliability; pause until re-aligned.
4. **Funding persistently flat (≤ 0.005%/8h) for 6+ months** — gate provides no selectivity when funding is always at entry level; adjust gate threshold upward or pause.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Early-in-cycle entry before crowd follow-through** — entering before the derivative crowd follows the whale signal captures more of the move while avoiding the crowded entry that elevates squeeze risk.
- **Positive or neutral carry during hold** — entering into flat or negative funding earns carry while the crowd remains uncrowded, partially offsetting execution costs.
- **Higher signal frequency than smart-money-vs-crowd-divergence** — the 60 (vs 65) whale threshold and +0.015% (vs 0.00%) funding ceiling generate more signals, keeping the strategy more actively deployed.
- **Partial exit discipline captures the crowd-follow phase** — the 60% exit at crowd-follow trigger realises most of the P&L before the crowded phase; the residual 40% trails into the momentum leg with a stop.

## Disadvantages

- **Whale score endpoint instability** — the CryptoDataAPI `/on-chain/whales` and `/on-chain/whales/{symbol}` endpoints are temporarily disabled; the whale-score aggregate is the fallback. Strategy pauses if the fallback also becomes unavailable.
- **Lower conviction than smart-money-vs-crowd-divergence** — by relaxing the whale threshold (60 vs 65) and the funding threshold (+0.015% vs 0.00%), the strategy accepts lower-quality signals. More false entries are expected; win rate is lower than smart-money-vs-crowd-divergence.
- **On-chain data latency** — whale accumulation signals have a 1–2 hour data lag; in fast-moving markets, the optimal entry may have passed before the signal fires.
- **Gate 3 (higher-low requirement) may prevent entry at cycle bottoms** — genuine accumulation at multi-month lows often occurs while price is still making lower lows (the higher-low formation comes after several weeks of whale buying). The gate prevents the best bottoming entries to reduce falling-knife risk.

## Sources

- [[smart-money-vs-crowd-divergence]] — the nearest combination page; explicitly differentiated as requiring crowd-short vs this page's crowd-neutral funding gate
- [[on-chain-smart-money-tracking]] — the whale wallet tracking primitive; this page uses aggregate scores rather than specific wallet following
- [[funding-filtered-momentum]] — the nearest funding-filter combination for a different primitive (price momentum vs whale accumulation)
- [[copy-trading]] — the broader copy-trading framework; this page is the funding-filtered, aggregate-signal implementation

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/whale-score/BTC` — Gate 1: 7-day rolling whale accumulation score (0–100)
- `GET /api/v1/on-chain/exchange-flows/BTC` — Gate 1 secondary: 24h exchange flow direction confirmation
- `GET /api/v1/on-chain/exchange-flows/spike-alerts` — Gate 1 real-time: large outflow confirmation
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — Gate 2: 8h funding rate and 7-day average
- `GET /api/v1/derivatives/binance/long-short-ratio` — Exit monitor: crowd positioning for partial/full exit trigger
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=10` — Gate 3: trailing 7-day daily closes for higher-low check
- `GET /api/v1/regimes/current` — regime context: reduce size in Bear_Trend or Structural_Shock

**Historical data:**
- `GET /api/v1/on-chain/whale-score/BTC` — historical score timeseries for signal frequency and threshold calibration
- `GET /api/v1/derivatives/funding-rates?coin=BTC&historical=true&days=365` — annual funding history for gate threshold calibration
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=730` — 2-year daily for higher-low pattern backtesting

*Note: `/on-chain/whales` and `/on-chain/whales/{symbol}` are currently returning 503 (temporarily disabled). Use `/on-chain/whale-score/{symbol}` and `/on-chain/exchange-flows/spike-alerts` per current API status. Nansen (nansen.ai) and Arkham Intelligence (arkhamintelligence.com) provide supplementary wallet-level analytics not available via CryptoDataAPI.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/on-chain/whale-score/BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]], [[cryptodataapi-derivatives]], [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [long-term regimes](https://cryptodataapi.com/regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — the `GET /api/v1/on-chain/whale-score/BTC` accumulation reading plus `GET /api/v1/on-chain/exchange-flows/spike-alerts` outflow confirmation form the whale leg
- **Funding filter** — the `GET /api/v1/derivatives/funding-rates?coin=BTC` 7-day average must show the crowd is NOT already long before mirroring the whales
- **Exit monitor** — `GET /api/v1/derivatives/binance/long-short-ratio` polled through the hold; crowd convergence onto the trade is the partial-exit trigger
- **Backtest** — the whale-score endpoint's own historical timeseries joined to daily klines back to 2017-08 (`GET /api/v1/backtesting/klines`) and the funding archive (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30)
- **Tips** — the `/on-chain/whales` endpoints are currently 503; run the pipeline on `whale-score` + `spike-alerts` and treat any whales-endpoint recovery as a new data source to re-validate, not silently merge
- **Prompt library** — the "Whale Positioning Monitor" prompt (Pro tier, [prompt library](https://cryptodataapi.com/prompts)) tracks >$100k Hyperliquid accounts and separates market-maker hedging from the directional conviction this strategy copies

## Related

- [[smart-money-vs-crowd-divergence]] — whale accumulation + crowd-SHORT divergence; this page is the earlier-in-cycle, crowd-neutral version; both are on-chain × funding-filter combinations
- [[on-chain-smart-money-tracking]] — individual wallet tracking; this page uses aggregate scores for lower crowding sensitivity
- [[copy-trading]] — general copy-trading framework; this page adds the funding-filter gate on aggregate signals
- [[funding-filtered-momentum]] — funding filter applied to price momentum; different primitive (momentum vs on-chain accumulation)
- [[crowded-short-funding-fade]] — pure derivative positioning fade without on-chain confirmation; differentiated from this page's on-chain-first structure
- [[smart-money-orderflow-combo]] — on-chain + real-time order-flow combo; differentiated as intraday/scalp vs this page's swing/position
- [[narrative-crowding-exit]] — exit discipline for crowded positions; the crowd-follow exit rules here parallel that page's exit framework
- [[onchain-capitulation-confluence]] — on-chain + sentiment for extreme cycle bottoms; differentiated by signal type (accumulation vs capitulation) and market phase
- [[exchange-netflow]] — exchange flow concept underpinning Gate 1 secondary check
- [[whale-onchain-flows]] — large-holder on-chain activity concept
- [[funding-rate]] — the derivative crowd positioning signal (Gate 2)
- [[nansen]] — Nansen as a supplementary whale data source
- [[on-chain]] — on-chain data category
- [[perpetual-futures]] — the instrument for the long position
- [[edge-taxonomy]] — informational + structural + behavioral edge classification
- [[failure-modes]] — whale early, data pollution, bear-market premature accumulation failure modes
- [[when-to-retire-a-strategy]] — kill vs pause framework
