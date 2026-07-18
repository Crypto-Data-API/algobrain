---
title: "On-Chain Capitulation Confluence"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, on-chain, sentiment, mean-reversion, behavioral-finance, bitcoin, quantitative, crypto, position-trading]
aliases: ["Capitulation Confluence Entry", "On-Chain + Sentiment Bottom", "Dual-Signal Capitulation Buy"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [behavioral, structural, informational]
edge_mechanism: "At cycle bottoms, forced and emotionally exhausted sellers converge on exchanges (exchange inflow spike / realized-loss spike / dormancy break) at the same time that crowd sentiment reaches a multi-month fear floor; requiring BOTH signals reduces false-bottom entries that occur when only one trigger fires — either on-chain selling without sentiment extreme (still distributing, not yet exhausted) or sentiment extreme without on-chain capitulation (fear, but holders haven't acted yet)."

data_required: [exchange-netflow, realized-loss-metrics, dormancy-cdd, sopr, sentiment-fear-greed, ohlcv-daily, funding-rates]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: low

expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 20

decay_evidence: "Both the on-chain capitulation signals (SOPR below 1, exchange-inflow spikes, dormancy breaks) and the fear-extreme sentiment filter have been documented on BTC. The spot-ETF era (2024+) has weakened some classic on-chain signals — ETF flows route through custodians rather than classic exchange wallets, partially obscuring the exchange-inflow capitulation signal. No published study on the dual-signal confluence specifically; each leg is documented separately (see miner-capitulation-bottom and contrarian-extremes)."

kill_criteria: |
  - strategy drawdown > 35% from high-water mark
  - rolling 12-month return < -15% (position-trading strategy with wide draw tolerance)
  - on-chain capitulation signals fire 3+ times in 6 months but the thesis fails to play out (BTC does not make a higher-low within 60 days of entry) for 2 consecutive occurrences — signals may be degraded by ETF-era flow migration
  - both signals coincide but are confirmed to be caused by a single entity's large sale (non-generalised capitulation) — verify via on-chain attribution before entry

related: ["[[on-chain-flow-trading]]", "[[contrarian-extremes]]", "[[funding-flush-reversal]]", "[[miner-capitulation-bottom]]", "[[fear-and-greed-index]]", "[[on-chain-analysis]]", "[[sentiment-trading]]", "[[exchange-netflow]]", "[[mvrv]]", "[[bitcoin-cycle-regime]]", "[[crypto-market-regime-taxonomy]]", "[[on-chain-regime]]", "[[behavioral-finance-overview]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# On-Chain Capitulation Confluence

On-chain capitulation confluence is a **bottom-fishing entry framework** for BTC (and, by extension, ETH) that requires **two simultaneous signals** before initiating a position-trading long: (1) an **on-chain capitulation signal** — an exchange-inflow spike, a realized-loss spike (SOPR < 1 at a multi-month extreme), or a dormancy break (old coins moving into exchange wallets at a loss), confirming that holders are *actively selling at a loss*; and (2) a **sentiment-extreme signal** — the Fear & Greed index at a multi-month floor (≤ 20, "Extreme Fear" territory), confirming that the *crowd's emotional state* has bottomed. The strategy enters only when both conditions coincide, on the thesis that the intersection of behavioural exhaustion and on-chain supply exhaustion is a structurally lower false-bottom rate than either signal alone.

This is differentiated from [[funding-flush-reversal]] (B2 page) — that strategy uses a *perp funding flush* (sustained negative funding confirming leveraged-long deleveraging) as its bottom signal. This page does **not** use the funding state as its primary signal: it uses *on-chain* selling pressure (direct evidence of holder capitulation on the blockchain) combined with *sentiment* (the emotional extreme of the crowd). Funding may be negative at the same time, but it is not a required input here. The combination targets a different type of bottom: the late-cycle, multi-month capitulation of *long-term holders and dormant coins*, not the acute leveraged-long flush that funding-flush-reversal targets.

This is differentiated from [[contrarian-extremes]] — that page uses sentiment extremes alone (Fear & Greed at extreme readings) as the primary contrarian entry. This page requires the on-chain capitulation signal as a *second* gate that confirms the sentiment extreme reflects actual selling behaviour, not just fear without action. Many Fear & Greed extremes in minor corrections are not accompanied by realised-loss spikes or dormancy breaks — those are fear without capitulation, and historically have higher false-bottom rates.

This is differentiated from [[miner-capitulation-bottom]] — that page uses miner-specific stress signals (Hash Ribbon, Puell Multiple). This page targets the broader holder-base capitulation (any long-term holder distributing at a loss), not specifically miner forced selling.

This is differentiated from [[on-chain-flow-trading]] — that page uses on-chain health signals as a directional overlay for swing trading. This page is specifically a *confluence-required bottom-fishing entry* for position-trading bottoms, not a general directional overlay.

## Edge source

Per [[edge-taxonomy]], **behavioral + structural + informational**:

- **Behavioral (primary)** — capitulation is the behavioural endpoint of the loss-aversion cycle: holders who refused to sell at higher prices eventually reach their psychological pain limit and sell at a loss. The Fear & Greed floor confirms the crowd's emotional exhaustion. Both signals reflect mass behavioural exhaustion, not a fundamental repricing. When exhausted sellers have acted, the remaining holders are *better capitalised* (they chose to hold through the pain) and the next marginal buyer faces less supply pressure.
- **Structural** — realized losses appearing on-chain (SOPR < 1, exchange inflow of dormant coins) represent supply that has been forcibly or voluntarily moved to the sell side. Once those coins have changed hands, they are now owned by buyers who acquired at the low — a structural supply rotation that removes the overhang. The MVRV approaching 1.0 from above marks the zone where aggregate cost basis equals price: the average holder is at break-even, and the remaining buyers are comfortable holding.
- **Informational** — the blockchain provides a direct read of *actual* sell behaviour (realized losses, dormancy breaks), not just inferred sentiment. This is the same informational edge as [[on-chain-flow-trading]], applied specifically to the capitulation identification problem.

## Why this edge exists

**Confluence reduces false-bottom rate through three independent failure modes that affect each signal alone:**

1. **On-chain capitulation without sentiment extreme: distribution, not capitulation.** An exchange-inflow spike can occur during the middle of a bear market when a large holder decides to reduce risk — not at the bottom. The Fear & Greed index in this case is typically in the 20-40 range (fear, but not extreme fear). The second signal rejects these distribution moves as bottom entries.

2. **Sentiment extreme without on-chain capitulation: fear without action.** The Fear & Greed index can drop below 20 during a sharp but temporary correction in a bull market (e.g., a flash crash or a macro-driven fear spike). In this scenario, the crowd is afraid but *holders have not actually moved their coins* — SOPR may be near 1, exchange inflows are not spiking, dormancy is quiet. This is a minor dip in a healthy market, not a capitulation bottom. The on-chain gate rejects these temporary fear spikes as bottom entries.

3. **Both together: the overlap zone is historically associated with cycle lows.** The intersection — coins actually moving at a loss *and* sentiment at extreme fear — is rare. It has appeared around every major BTC cycle low (2018-12, 2020-03, 2022-06 post-LUNA, 2022-11 post-FTX). The joint probability of both conditions being noise simultaneously is lower than either individual condition.

**Who is on the other side:** the forced or exhausted seller who has held through most of the bear market and finally capitulates at the worst price, and the retail capitulation buyer who re-enters just before the deepest flush only to sell again on the retest.

## Null hypothesis

Under the null, the on-chain capitulation signal and the fear-extreme sentiment signal carry **no incremental joint predictive power** over either signal individually. Specifically:
- The forward 60-day return of BTC after joint-signal entries should not differ from entries made on just one signal.
- The false-bottom rate (entries that see a further -20% drawdown before recovery) should not be lower for joint-signal entries than single-signal entries.
- The MVRV / SOPR state at the time of both conditions coinciding should not be a reliable clustering point for cycle lows.

Currently not rejected (`backtest_status: untested`). Testable prediction: identify all historical dates when SOPR was below 0.97 for 5+ days AND Fear & Greed was ≤ 20; compute BTC forward 60-day returns and maximum adverse excursion from those dates; compare to dates when only one condition was met. Prediction: joint-signal dates show lower false-bottom rate and higher average 60-day return.

## Rules

### Signal 1 — On-chain capitulation (require at least one of three sub-signals)

**Sub-signal A: Exchange-inflow spike (dormant coins)**
- Exchange BTC netflow is **strongly positive** (inflows >> outflows): specifically, the 7-day rolling exchange inflow is in the top 10% of its trailing 180-day distribution.
- *Significance:* large, sudden inflows of BTC to exchanges — especially from older wallet cohorts — signal holders moving coins to the sell-side. On-chain vendors attribute "dormancy breaks" to coins that have not moved in 6+ months now appearing in exchange inflow.

**Sub-signal B: SOPR below 1 (realized losses dominant)**
- The 7-day smoothed **SOPR (Spent Output Profit Ratio)** is ≤ **0.97** — the average coin being transacted is being sold at a 3%+ loss relative to acquisition cost.
- SOPR < 1 for a sustained period (≥ 5 consecutive days, not a single spike) is required; isolated dips can be noise.
- *Significance:* aggregate realized losses confirm the capitulation is broad-based, not limited to a single cohort.

**Sub-signal C: MVRV-Z approaching 0 (aggregate loss territory)**
- MVRV-Z score (Market Value to Realised Value, standardised) falls **below 0** — meaning the aggregate market is at or below its own cost basis.
- This is the most powerful of the three but also the rarest; it has appeared only at the deepest bear market troughs.

**Operation:** any ONE of sub-signals A, B, or C qualifies the on-chain capitulation gate. Sub-signal C alone is sufficient for a higher-conviction entry.

### Signal 2 — Sentiment extreme

- **Fear & Greed index ≤ 20** for the current day, confirmed by **2+ consecutive days** below 20 (requires sustained extreme, not a single-day dip).
- *Source:* [[fear-and-greed-index]] as served by CryptoDataAPI `/api/v1/sentiment/fear-greed` and historical from `/api/v1/market-intelligence/fear-greed-history`.

### Entry conditions

1. **Both Signal 1 (any sub-signal) AND Signal 2 fire simultaneously** (within a 5-day coincidence window).
2. **No active regime kill:** the current regime must not be `Structural Shock` (macro systemic event — basis blowouts, exchange insolvencies — can override the capitulation signal).
3. **Stablecoin dry-powder confirmation (optional, higher conviction):** CryptoDataAPI `/api/v1/on-chain/stablecoin-reserves/dry-powder` shows an "accumulating" or "elevated" signal — idle buying power is available to absorb the supply.

**Entry execution:**
- Spot BTC (or BTC perp ≤ 2× leverage).
- Scale in: do not enter the full position on day 1. Use 3-tranche scaling over 5 days (33% per tranche), maintaining the ability to average down if the capitulation deepens.
- First tranche entry: on the day both signals are confirmed.

### Exit conditions

1. **MVRV recovery:** MVRV-Z recovers above **+1** — the market is now back above its realised value on average. This is a distribution-zone indicator; begin trimming.
2. **Sentiment normalisation:** Fear & Greed index recovers above **50** for 5 consecutive days — the extreme fear has reversed; the trade is working. Begin trimming here.
3. **Time stop:** if neither exit condition has been met within **90 days**, close half the position and hold the remainder with a trailing stop.
4. **Hard stop:** a **further -25% drawdown from the average entry price** across all tranches. This is wide by design: position-trading bottoms require room to breathe. The -25% stop is calibrated to allow for a retest of the capitulation low (common) without triggering prematurely.

### Position sizing

- Position size per tranche: 2-3% of total portfolio per tranche × 3 tranches = **6-9% total allocation**.
- Maximum concurrent allocation: 10% of total portfolio in any single bottom-fishing setup.
- Leverage: ≤ 2× on any perp expression; spot preferred for multi-month hold.
- Cash reserve: maintain 20% of total portfolio in stablecoins throughout the hold (additional dry powder for tranching if the setup deepens).

## Implementation pseudocode

```python
# onchain_capitulation_confluence.py

from dataclasses import dataclass, field
from typing import Optional

# ---- thresholds ----
EXCHANGE_INFLOW_PCTILE  = 90     # top 10% of 180d distribution
SOPR_MAX                = 0.97   # SOPR ≤ this (realized losses)
SOPR_MIN_DAYS           = 5      # consecutive days SOPR ≤ threshold
MVRV_Z_EXTREME          = 0.0    # MVRV-Z at or below 0 (deep bear)
FEAR_GREED_MAX          = 20     # extreme fear floor
FEAR_GREED_CONFIRM_DAYS = 2      # consecutive days at extreme
COINCIDENCE_WINDOW_DAYS = 5      # both signals within this window
DRAWDOWN_KILL           = 0.35
HARD_STOP_FROM_ENTRY    = 0.25
MVRV_EXIT_Z             = 1.0    # begin trimming
FEAR_GREED_EXIT         = 50     # sentiment normalised
EXIT_FG_CONFIRM_DAYS    = 5
TIME_STOP_DAYS          = 90
TRANCHE_SIZE_PCT        = 0.025  # 2.5% per tranche
MAX_TRANCHES            = 3
MAX_TOTAL_PCT           = 0.10

@dataclass
class OnChainState:
    exchange_inflow_pctile: float   # vs 180d
    sopr_7d_smooth: float
    sopr_below_threshold_days: int
    mvrv_z: float

@dataclass
class SentimentState:
    fear_greed: float
    fear_greed_extreme_days: int    # consecutive days ≤ 20

def on_chain_signal_fires(oc: OnChainState) -> str:
    """Returns the sub-signal name if any on-chain signal qualifies, else empty string."""
    if oc.mvrv_z <= MVRV_Z_EXTREME:
        return "mvrv_z_extreme"  # strongest signal
    if (oc.sopr_7d_smooth <= SOPR_MAX and
            oc.sopr_below_threshold_days >= SOPR_MIN_DAYS):
        return "sopr_realized_losses"
    if oc.exchange_inflow_pctile >= EXCHANGE_INFLOW_PCTILE:
        return "exchange_inflow_spike"
    return ""

def sentiment_signal_fires(sent: SentimentState) -> bool:
    return (sent.fear_greed <= FEAR_GREED_MAX and
            sent.fear_greed_extreme_days >= FEAR_GREED_CONFIRM_DAYS)

def confluence_entry_decision(oc: OnChainState, sent: SentimentState,
                              regime: str, book: dict) -> dict:
    if book.get("total_drawdown", 0) > DRAWDOWN_KILL:
        return {"action": "FLAT", "reason": "drawdown kill"}
    if regime == "Structural_Shock":
        return {"action": "WAIT", "reason": "structural shock — override capitulation signal"}

    oc_signal = on_chain_signal_fires(oc)
    fg_signal = sentiment_signal_fires(sent)
    existing_tranches = book.get("btc_bottom_tranches", 0)

    if not oc_signal:
        return {"action": "WAIT", "reason": "on-chain capitulation gate not met"}
    if not fg_signal:
        return {"action": "WAIT", "reason": "sentiment extreme gate not met",
                "on_chain_primed": oc_signal, "note": "waiting for Fear & Greed ≤ 20 × 2d"}
    if existing_tranches >= MAX_TRANCHES:
        return {"action": "HOLD", "reason": "max tranches deployed"}

    # both conditions met
    high_conviction = oc_signal == "mvrv_z_extreme"
    notional = book["portfolio_capital"] * TRANCHE_SIZE_PCT * (1.2 if high_conviction else 1.0)
    notional = min(notional, book["portfolio_capital"] * (MAX_TOTAL_PCT - existing_tranches * TRANCHE_SIZE_PCT))

    return {
        "action": "ADD_TRANCHE",
        "tranche": existing_tranches + 1,
        "notional": notional,
        "on_chain_trigger": oc_signal,
        "fear_greed": sent.fear_greed,
        "note": f"confluence: {oc_signal} + FG={sent.fear_greed} (extreme {sent.fear_greed_extreme_days}d)",
        "high_conviction": high_conviction,
    }

def exit_decision(pos: dict, oc: OnChainState, sent: SentimentState,
                  days_held: int, unrealised_loss_pct: float) -> Optional[dict]:
    if unrealised_loss_pct > HARD_STOP_FROM_ENTRY:
        return {"action": "CLOSE_ALL", "reason": f"hard stop -25% from avg entry"}
    if oc.mvrv_z >= MVRV_EXIT_Z:
        return {"action": "TRIM_50PCT", "reason": "MVRV-Z recovered above +1 — distribution zone entry"}
    if sent.fear_greed >= FEAR_GREED_EXIT:
        if getattr(sent, "normalised_days", 0) >= EXIT_FG_CONFIRM_DAYS:
            return {"action": "TRIM_50PCT", "reason": "Fear & Greed normalised to 50+ for 5d"}
    if days_held >= TIME_STOP_DAYS:
        return {"action": "CLOSE_HALF", "reason": "90-day time stop; hold remainder with trailing stop"}
    return None
```

The production system adds: on-chain data polling via CryptoDataAPI endpoints; a PIT (point-in-time) data discipline for the SOPR and netflow series per [[point-in-time-data]]; a stablecoin dry-powder confirmation check; and a daily P&L ledger separating the three tranches.

## Indicators / data used

- **Exchange netflow (BTC)** — `/api/v1/on-chain/exchange-flows/BTC`: rolling 7-day netflow vs 180-day percentile. Primary sub-signal A.
- **SOPR (7-day smoothed)** — `/api/v1/on-chain/dormancy/btc` returns MVRV and dormancy zone. For raw SOPR, supplement with [[glassnode]] or [[cryptoquant]]; CryptoDataAPI provides the MVRV and zone classification (capitulation zone = SOPR-equivalent distress signal).
- **MVRV-Z score** — `/api/v1/on-chain/dormancy/btc`: the zone classification includes the capitulation-to-euphoria scale; the MVRV-Z < 0 sub-signal corresponds to the "capitulation zone" classification in this endpoint.
- **[[fear-and-greed-index]]** — `/api/v1/sentiment/fear-greed`: live Fear & Greed reading; `/api/v1/market-intelligence/fear-greed-history` for historical series.
- **On-Chain Health composite** — `/api/v1/on-chain/score`: the 0-100 composite that collapses all on-chain signals; a score ≤ 20 is consistent with confluence conditions.
- **Stablecoin dry-powder z-score** — `/api/v1/on-chain/stablecoin-reserves/dry-powder`: optional higher-conviction confirmation.
- **Whale accumulation score** — `/api/v1/on-chain/whale-score/BTC`: rising whale accumulation in the capitulation window is a positive confluence signal.
- **Regime classification** — `/api/v1/regimes/current`: reject entries in `Structural_Shock` regime.

## Example trade

**Setup (illustrative — loosely analogous to 2022-11 post-FTX):**

- Date: a hypothetical deep bear market low.
- **On-chain signal:** BTC exchange-inflow percentile = 94th (top 6% of 180d). SOPR 7d smoothed = 0.94 (below 0.97 for 8 consecutive days). MVRV-Z = −0.3 (below 0). Sub-signal B (SOPR) and sub-signal C (MVRV-Z) both fire — high conviction.
- **Sentiment signal:** Fear & Greed = 14 for 3 consecutive days. Gate passes.
- **Regime:** `/regimes/current` = "Late Bear / Structural Distress" (not `Structural_Shock` specifically; proceed).
- **Portfolio:** $100,000. Target per tranche: 2.5% = $2,500. High-conviction multiplier 1.2× (MVRV-Z fired): $3,000 per tranche.

**Entry:**
- Tranche 1 (Day 1): long BTC spot at $16,200. $3,000 notional ≈ 0.185 BTC.
- Tranche 2 (Day 3): BTC dips further to $15,800. $3,000 notional ≈ 0.190 BTC. Total avg entry ≈ $16,000.
- Tranche 3: reserved; both signals still active at Day 5. BTC stabilises at $16,400 — no further dip. Decision: do not add Tranche 3 (SOPR begins recovering toward 0.98). Keep as 2-tranche position.

**Hold (62 days):** BTC recovers from $16,400 to $22,000.
- Day 45: Fear & Greed recovers to 52 for 5 consecutive days → Trim exit trigger. Sell 50% of position (~0.188 BTC at $22,000 = $4,130). Gain on trimmed tranche: ~+37% vs average entry.
- Remaining position held for MVRV-Z recovery to +1.

**Partial exit P&L (Tranche 1+2 combined at trim):** avg entry $16,000 → trim exit $22,000. Gain: +37.5%. On $6,000 deployed (2 tranches × $3,000): **+$2,250** gross from the trim. Held remainder at $22,000 with trailing stop.

**Hard stop scenario:** if BTC had fallen to $12,000 (−25% from $16,000 avg entry): close all tranches at $12,000. Loss: −$1,500 on $6,000 = −25% position loss = −1.5% of portfolio. The position size is intentionally small for this reason; worst-case portfolio drawdown from a full-signal failed entry is ~2-3% of total capital.

*(Illustrative. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.7 | Very few independent signals per year (perhaps 1-3 deep capitulation events across a cycle); Sharpe is regime-specific and has extremely high sample variance |
| Expected max drawdown | ~35% | On-chain bottom entries must tolerate deep MTM drawdowns before recovery; the wide hard stop (-25%) is intentional |
| Signal frequency | Very low | Both conditions must coincide; estimated 1-2 times per bear market cycle in BTC |
| Win rate (per entry) | ~60-70% (rough estimate) | Single on-chain signal: ~50-55%; sentiment alone: ~55-60%; confluence: predicted ~65-75% — the core hypothesis |
| Average win / average loss | ~3-5× | Position-trading bottoms: large winners when the thesis plays out; losses bounded at -25% hard stop |
| Breakeven cost budget | 20 bps | Spot BTC: minimal transaction costs; multi-month hold makes costs irrelevant relative to the expected move |
| Capacity | High relative to signal count | $50M cap reflects BTC depth, not strategy capacity; the signal fires rarely, so capacity utilisation is always low |

## Capacity limits

- **Per signal:** spot BTC and BTC perp are the deepest crypto instruments; a $50M entry can be executed without meaningful market impact over 3-5 tranches.
- **Binding constraint:** not execution capacity but *data quality*. As ETF-era flows route through custodians rather than exchange wallets, the exchange-inflow spike signal captures a decreasing fraction of total supply movement. The MVRV-Z signal is more robust (it uses realised prices from all on-chain spending, not just exchange flows).
- The `capacity_usd: 50000000` estimate is inherited from [[on-chain-flow-trading]] for the same underlying instruments.

## What kills this strategy

1. **ETF-era on-chain signal degradation (#5: Regime change).** Spot ETF and institutional custody routes move BTC off classic exchange wallets, reducing the exchange-inflow spike's signal quality. The SOPR and MVRV-Z signals are less affected (they measure all on-chain spending), but if custody rails expand further, even those signals may lag real capitulation.
2. **Secular bear or regime shift (#6).** If a genuine regime-ending event (BTC protocol failure, major regulatory prohibition) occurs, the capitulation signals fire correctly but the recovery does not happen — the hard stop at -25% is the circuit breaker.
3. **Confluence crowding (#4).** As on-chain capitulation signal dashboards proliferate (Glassnode alerts, CryptoQuant, CDA composite), more market participants watch the same conditions. If enough capital floods into the trade on the confluence signal, it front-runs the supply exhaustion — the overshoot is less, the recovery is still there but smaller.
4. **False on-chain capitulation (Operational).** A single large whale moving a dormant wallet to an exchange for reasons unrelated to selling (cold-to-warm wallet migration, custody transfer) can trigger the exchange-inflow spike sub-signal falsely. The SOPR and MVRV-Z sub-signals provide redundancy; requiring 5+ consecutive SOPR days reduces single-event noise.
5. **Sentiment/on-chain timing mismatch.** The two signals are not always simultaneous. Fear & Greed can bottom days before on-chain capitulation, or vice versa. The 5-day coincidence window accommodates this but does not eliminate the case where the signals peak at opposite ends of a 10-day window (one signal stale when the other fires).

## Kill criteria

Pause on any of:

1. **Strategy drawdown > 35%** in any rolling 180-day window.
2. **Rolling 12-month return < −15%** — the position-trading horizon is long; a 12-month negative period is evidence the bottom-fishing thesis is not working in the current cycle.
3. **On-chain signal fires 3+ times in 6 months, thesis fails 2 consecutively** — SOPR/inflow signals are degraded; the ETF-era migration hypothesis may be confirmed. Recalibrate signal thresholds.
4. **Confluence identified as false (single-entity event)** — verify on-chain attribution before the second tranche; cancel if the inflow is traceable to a single custodian transfer unrelated to capitulation.

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Reduced false-bottom rate:** the confluence requirement directly addresses the most common failure mode of single-signal bottom fishing — entering on fear alone (no supply exhaustion) or entering on supply exhaustion alone (no behavioural bottom). Requiring both dramatically narrows the entry universe.
- **Point-in-time observable inputs:** unlike sentiment-only signals, the on-chain data (exchange flows, SOPR, MVRV) is directly computable from the blockchain and not subject to survey bias or media framing.
- **Low frequency / high conviction:** because the signal fires rarely (1-2 per bear market), the strategy does not generate noise entries. The operator can take a high-conviction position when it fires, knowing it has historically been a rare, significant setup.
- **Interpretable failure mode:** if the trade fails, the post-mortem is clear — either the on-chain signal was noise (custody migration) or the sentiment signal was a minor correction (not a cycle low). Both are diagnosable.
- **Composable with on-chain flow trading:** the entry logic is a *specialised subset* of [[on-chain-flow-trading]]'s composite health score; the two frameworks share the same data rail.

## Disadvantages

- **Very few signals per cycle:** the dual-signal requirement means the strategy may fire once or twice in an entire bear cycle. In bullish regimes (most of a cycle), the strategy is inactive.
- **Wide hard stop required:** a -25% hard stop from entry is necessary to allow for retests of the capitulation low, but it means a failed entry costs 0.6-1.5% of total portfolio depending on allocation. Over multiple cycles, a loss sequence is survivable but psychologically demanding.
- **ETF-era degradation of exchange-inflow signal:** as custody rails mature, the exchange-inflow spike sub-signal weakens. Monitoring the signal's hit rate and pivoting to SOPR and MVRV-Z if exchange flows lose predictive power is an ongoing maintenance task.
- **Vendor dependency for SOPR:** raw SOPR data is not currently available via a verified CryptoDataAPI endpoint; it must be sourced from [[glassnode]], [[cryptoquant]], or a blockchain analytics provider. The MVRV-Z equivalent (the dormancy zone classification) is available via CryptoDataAPI `/on-chain/dormancy/btc`.
- **Slow thesis:** position-trading setups on multi-month timeframes require accepting a 60-90 day time stop. Operators with shorter-horizon mandates cannot implement this strategy.

## Sources

- [[on-chain-flow-trading]] — the broader on-chain directional overlay; the capitulation entry is a specialised bottom-fishing version of the same data framework.
- [[contrarian-extremes]] — the sentiment-extreme contrarian trade; this page's Fear & Greed gate is the same signal applied as one of two required conditions.
- [[miner-capitulation-bottom]] — miner-specific capitulation signals; shares the conceptual framework but uses different data (hashrate/Puell vs SOPR/MVRV-Z/exchange flows).
- Glassnode Research, various — SOPR as a realized-profit/loss indicator; MVRV-Z as a cycle positioning tool; exchange inflow as a supply distribution signal.
- BIS Working Papers No 1087 — Schmeling, Schrimpf, Todorov (2023). The leveraged-long perspective on bear-market capitulation; the perp funding dimension complementary to this on-chain approach. https://www.bis.org/publ/work1087.pdf

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/exchange-flows/BTC` — CEX inflow/outflow, 1h/6h/24h/7d windows; primary sub-signal A (exchange-inflow spike)
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + dormancy zone classification (capitulation/accumulation/euphoria); primary sub-signal C (MVRV-Z floor)
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100); a score ≤ 20 is consistent with capitulation confluence
- `GET /api/v1/sentiment/fear-greed` — live Fear & Greed index reading; Signal 2
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — stablecoin dry-powder z-score; optional higher-conviction confirmation
- `GET /api/v1/on-chain/whale-score/BTC` — whale accumulation score timeseries; secondary bullish signal
- `GET /api/v1/regimes/current` — regime classification; blocks entry in `Structural_Shock`

**Historical data:**
- `GET /api/v1/market-intelligence/fear-greed-history` — historical Fear & Greed timeseries for backtest of Signal 2
- `GET /api/v1/on-chain/exchange-flows/spike-alerts` — large transfers (≥$1M); additional whale-movement context
- `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=200` — daily OHLCV for drawdown and entry tracking

Note: raw SOPR data (sub-signal B) is not currently documented as a CryptoDataAPI endpoint. Source from [[glassnode]] (`/v1/metrics/indicators/sopr`), [[cryptoquant]], or equivalent on-chain analytics provider. The MVRV-Z zone classification via `/on-chain/dormancy/btc` is the closest CryptoDataAPI equivalent.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/dormancy/btc"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]], [[cryptodataapi-sentiment]], [[cryptodataapi-market-intelligence]].

## Related

- [[on-chain-flow-trading]] — the broader on-chain directional overlay; this page is the capitulation-specialised entry subset
- [[contrarian-extremes]] — sentiment-extreme contrarian trade; this page adds on-chain confirmation as a second required gate
- [[funding-flush-reversal]] — funding-state bottom signal; uses perp funding (not on-chain supply) as the capitulation indicator — different regime, different input
- [[miner-capitulation-bottom]] — miner-specific capitulation entry; overlapping philosophy, different data inputs
- [[fear-and-greed-index]] — the sentiment index used in Signal 2
- [[on-chain-analysis]] — the theoretical framework for interpreting on-chain signals
- [[exchange-netflow]] — the exchange-flow concept underlying sub-signal A
- [[mvrv]] — the MVRV ratio concept underlying sub-signal C
- [[bitcoin-cycle-regime]] — the macro cycle context this strategy operates within
- [[crypto-market-regime-taxonomy]] — the 14-basket regime framework; this strategy sits in basket 7 (On-Chain Intelligence) + behavioral overlay
- [[on-chain-regime]] — on-chain health as a regime signal
- [[behavioral-finance-overview]] — the loss-aversion and capitulation mechanisms
- [[edge-taxonomy]] — behavioral + structural + informational edge classification
- [[failure-modes]] — ETF-era degradation, secular bear, crowding risks
- [[when-to-retire-a-strategy]] — kill vs pause framework
