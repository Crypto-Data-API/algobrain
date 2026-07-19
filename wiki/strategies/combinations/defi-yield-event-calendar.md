---
title: "DeFi Yield / LP × Unlock/Event Calendar"
type: strategy
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [combinations, meta-strategy, defi, yield-farming, event-driven, liquidity, risk-management, quantitative, crypto, impermanent-loss]
aliases: ["DeFi LP Event Calendar", "LP Unlock Calendar Gate", "DeFi Yield Catalyst De-Risk", "LP Pre-Event Withdrawal"]
strategy_type: hybrid
timeframe: position
markets: [crypto]
complexity: advanced
backtest_status: untested

edge_source: [informational, structural]
edge_mechanism: "Scheduled token unlocks and protocol catalysts (token generation events, points-program endings, pool-contract upgrades, large governance votes) predictably spike the volatility and directional price risk of the LP's pooled assets and amplify LVR costs; withdrawing LP and farming positions before the event window and redeploying after avoids the worst LVR and impermanent-loss outcomes, while capturing a re-entry bonus (fee income resets in a newly-stressed, high-volume pool). The counterparty is the passive LP who stays deployed through the event, subsidising the arbitrageur's LVR extraction during the event-induced vol spike."

data_required: [event-calendar, token-unlock-schedule, dvol-btc, dvol-eth, realized-vol-4h, dex-pool-apr, dex-pool-tvl, impermanent-loss-estimate, gas-price]
min_capital_usd: 10000
capacity_usd: 15000000
crowding_risk: low

expected_sharpe: 0.8
expected_max_drawdown: 0.15
breakeven_cost_bps: 30

decay_evidence: "The structural LVR-during-events asymmetry is mathematically durable: if the pooled token has an expected vol spike on the event date, LVR = σ²/8 per unit time grows with the square of that spike. The calendar-based gate does not depend on market inefficiency — it depends on LVR math and the availability of event calendars. The edge compresses only if all passive LPs simultaneously adopt event-aware withdrawal protocols, which is unlikely given the complexity of coordinating this across retail DeFi users. The main risk is gas costs at withdrawal/re-entry making the trade uneconomic for small positions."

kill_criteria: |
  - 6-month net P&L on event-window withdrawals (fee income missed vs IL avoided + re-entry bonus) is negative for 3 consecutive event cycles (event calendar gate not worth the gas cost)
  - Gas costs at withdrawal + re-entry exceed the expected IL saving for target events at current pool TVL (execution economics broken; pause for this pool/chain)
  - Event calendar data unavailable or systematically wrong for 2+ consecutive scheduled events (data reliability failure; use conservative full-withdrawal posture until data restored)
  - Pool TVL < $5M (insufficient fee income to justify the strategy; move to higher-TVL pools)

related: ["[[defi-yield-regime-gate]]", "[[event-calendar-risk-gating]]", "[[options-rv-event-calendar]]", "[[unlock-cascade-watch]]", "[[unlock-short-with-crowding-gate]]", "[[delta-neutral-yield-farming]]", "[[concentrated-liquidity]]", "[[defi-yield-sentiment-entry]]", "[[defi-yield-farming]]", "[[leveraged-yield-farming]]", "[[impermanent-loss]]", "[[loss-versus-rebalancing]]", "[[token-unlock]]", "[[uniswap]]", "[[aave]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi-regimes]]", "[[cryptodataapi]]"]
---

# DeFi Yield / LP × Unlock/Event Calendar

DeFi yield / LP event calendar withdraws liquidity provider and farming positions **before scheduled catalysts** — token unlocks of the pool's underlying asset, points-program endings, pool-contract upgrades, major governance votes, or large airdrop distributions — and redeploys capital after the event-induced volatility has passed and a stable post-event fee environment has re-established. The event calendar is the organising anchor: it converts a passive yield position into an actively managed one that avoids the worst LVR (Loss Versus Rebalancing) regimes while capturing the elevated fee income in the recovery window after the event. The counterparty is the passive LP who stays deployed through all events and subsidises the arbitrageur's LVR extraction during every spike in realised volatility.

**This is differentiated from [[event-calendar-risk-gating]]** — that page pauses *CEX mechanical strategies* (carry books, grids, vol-selling) around events. The mechanism there is: the strategy's operating assumption (continuous mean-reverting / carry-harvesting regime) is temporarily invalidated by the event. This page covers *DeFi LP positions specifically*, where the kill mechanism is LVR (not strategy-assumption violation) and the execution requires on-chain gas transactions to withdraw and re-enter, adding cost considerations absent from CEX strategy pausing.

**This is differentiated from [[defi-yield-regime-gate]]** — that page gates LP deployment on the *vol regime* (DVOL level and ADX): deploy in low-vol, withdraw in high-vol. It is a continuous, state-based gate with no forward-looking calendar awareness. This page is *event-calendar-based and forward-looking*: it initiates withdrawal at T − 7 days before a scheduled catalyst, regardless of whether the DVOL level is currently elevated, because the event is expected to spike vol. The two pages are composable: the regime gate handles the continuous-vol dimension; this page adds the discrete forward-event dimension. Together they avoid both the ambient high-vol regimes AND the scheduled spike events.

**This is differentiated from [[unlock-cascade-watch]]** — that page manages directional *cascade-fade entries* around unlocks (staging GTC limit buy orders to fade the liquidation cascade triggered by the unlock). This page manages *LP withdrawal discipline* — exiting the passive yield position before the unlock to avoid LVR, not staging cascade entries. The two strategies are complementary: this page exits the LP before the unlock; [[unlock-cascade-watch]] stages cascade-fade entries during the unlock's cascade if it materialises. An operator can run both simultaneously.

**This is differentiated from [[options-rv-event-calendar]]** — that page actively *trades the volatility term structure* around events on Deribit (long back-dated IV vs short near-dated IV). This page makes no options trade; it simply *withdraws a passive LP position* to avoid the event window's LVR and re-enters after. Different instrument, different mechanism, different operator profile.

## Edge source

Per [[edge-taxonomy]], **informational + structural**:

- **Informational (primary)** — Token unlock schedules, protocol upgrade dates, and points-program ending dates are publicly known in advance (often announced 30–90 days ahead). The LP operator who reads the calendar before the LP deploys is information-advantaged relative to the passive LP who does not. The information is not secret — it is merely not acted upon by the majority of retail LPs who deploy and forget.
- **Structural** — LVR is structurally asymmetric: it grows with σ², and large scheduled events cause sharp, predictable σ spikes. The LP is structurally short gamma (short a synthetic straddle on the pooled assets), meaning every vol spike increases the LVR cost. Withdrawing before the spike avoids this structural loss; re-entering after the spike captures elevated fee income in a high-volume, stabilising pool.

## Why this edge exists

**The LVR-event asymmetry:**

LP net P&L per unit time ≈ `fee_income − LVR − gas` where LVR ≈ σ²/8 per unit time (Milionis et al. 2022). During a large token unlock (≥ 5% of supply), the unlocked supply creates:

1. **Supply shock on the pool's underlying token** — large holders receive unlocked tokens and may sell into the AMM, directly driving the pool's price lower and increasing realised vol.
2. **Arbitrageur activation** — as the token price moves, arbitrageurs extract LVR continuously, paying LVR out of LP fee income. In a high-vol event window, LVR may exceed fee income by 3–10×.
3. **Slippage cost on IL** — even if the LP holds through the event and price recovers, the IL during the event is real, and the arbitrageur extracts it in real time.

**Re-entry bonus:** After a large unlock, if the token price stabilises (no death-spiral), the pool enters a recovery phase with:
- Elevated trading volume (volatility → volume → fees) while vol remains high but is mean-reverting
- A recent price reset providing a new IL reference point at a lower base
- Fewer passive LPs in the pool (those who panic-withdrew permanently) → fee income divided by fewer LPs → per-LP fee income temporarily elevated

The re-entry on the 3rd or 4th day post-event (after vol has stabilised, as confirmed by DVOL returning toward its pre-event level) captures this bonus window.

**Who is on the other side:** the passive LP who stays deployed through the event. This LP experiences the full LVR extraction during the event spike, suffers the IL from the price movement, and then participates in the recovery fee income alongside the re-entrant — but from a cost-basis that includes the event losses. The net result for the passive LP is often negative over the event window; the active calendar-aware LP avoids those costs.

## Null hypothesis

Under the null, LP fee income net of LVR is **event-date independent**: a pre-event withdrawal protocol does not produce materially higher rolling returns than continuous LP deployment, because:
- The missed fee income during the withdrawal window equals or exceeds the IL/LVR avoided
- Gas costs of 2× transactions (withdraw + re-enter) negate the cost savings

Testable on historical Uniswap v3 data: for all token unlocks ≥ 5% of supply in pools tracked since 2022, compare fee income minus IL for (a) LPs who withdrew at T − 7 and re-entered at T + 3 vs (b) LPs who held continuously. Prediction: group (a) has materially higher net P&L for unlocks with price-impact ≥ −8% and group (b) is approximately equal for unlocks with price impact < 3%.

Currently untested. The LVR math supports the hypothesis directionally; the magnitude depends on the unlock's price impact and the pool's fee tier.

## Rules

### Event classification (Tier 1 / Tier 2)

**Tier 1 — Full withdrawal (start T − 7 days; re-enter T + 3 days minimum):**
- Token unlock ≥ 5% of circulating supply
- Protocol contract upgrade with migration (pool may move)
- Points/farming program ending (TVL exodus expected)
- Token generation event (new supply enters ecosystem)

**Tier 2 — 50% withdrawal (start T − 3 days; re-enter T + 2 days minimum):**
- Token unlock 2–4.9% of circulating supply
- Major governance vote that could change pool economics (fee tier change, pool deprecation vote)
- Large airdrop to pool participants (may cause exit)
- Staking/restaking deadline creating flow pressure

**No action (monitor only):**
- Token unlock < 2% of circulating supply
- Minor protocol parameters change (fee on individual swaps, not pool fee tier)
- General crypto market events (FOMC, BTC halving) — use [[defi-yield-regime-gate]] for these

### Withdrawal execution

1. At T − 7 (Tier 1) or T − 3 (Tier 2): withdraw LP position entirely (or 50% for Tier 2).
2. Convert withdrawn tokens back to the base token (e.g., USDC) or hold the underlying tokens — decision based on which incurs less IL on re-entry.
3. Stage the capital for re-entry monitoring.

### Re-entry conditions (all must hold)

1. **Event has resolved:** the catalyst date has passed.
2. **Price stabilised:** 4h realised vol of the pool's underlying token ≤ 1.5× its 7-day pre-event average for ≥ 48 hours post-event.
3. **DVOL not further expanding:** DVOL is flat or declining from its event peak.
4. **Pool still alive:** pool TVL ≥ 50% of its pre-event level (token has not entered a death-spiral).
5. **Gas cost acceptable:** estimated gas for re-entry ≤ 0.5% of re-entry capital.

### Rejected re-entry signals

- Price making new lows post-event (structural downtrend; the re-entry opportunity is absent)
- Pool TVL < 50% of pre-event (mass LP exodus = incentive structure broken)
- DVOL still expanding (event not resolved; second event risk still active)

## Implementation pseudocode

```python
# defi_yield_event_calendar.py

from dataclasses import dataclass
from datetime import date, timedelta
from typing import Optional

# Event classification thresholds
TIER1_UNLOCK_PCT  = 0.05   # ≥ 5% of supply = Tier 1
TIER2_UNLOCK_PCT  = 0.02   # 2–4.9% of supply = Tier 2

# Withdrawal lead times (days before event)
TIER1_LEAD_DAYS   = 7
TIER2_LEAD_DAYS   = 3

# Re-entry conditions
REENTRY_VOL_MULT  = 1.5    # 4h vol ≤ 1.5× pre-event average
REENTRY_HOLD_HRS  = 48     # must hold below threshold for 48h
REENTRY_TVL_FLOOR = 0.50   # pool TVL must remain ≥ 50% of pre-event
REENTRY_GAS_MAX   = 0.005  # gas ≤ 0.5% of re-entry capital

# Partial withdrawal for Tier 2
TIER2_WITHDRAW_PCT = 0.50

@dataclass
class Event:
    symbol:       str
    event_type:   str       # 'unlock', 'upgrade', 'points_end', 'tge', 'governance', 'airdrop'
    event_date:   date
    unlock_pct:   float     # fraction of circulating supply unlocking (0.0 if not applicable)

@dataclass
class PoolState:
    tvl_current:  float
    tvl_pre_event: float
    vol_4h:       float     # current 4h realised vol (annualised)
    vol_7d_avg:   float     # 7-day pre-event average 4h realised vol
    dvol:         float     # current Deribit implied vol for the underlying
    dvol_7d_peak: float     # DVOL peak since event date
    gas_cost_usd: float     # estimated gas for withdrawal or re-entry
    capital_usd:  float     # capital to re-enter

def classify_event(ev: Event) -> Optional[str]:
    """Returns 'tier1', 'tier2', or None (no action)."""
    if ev.event_type in ('upgrade', 'points_end', 'tge') and ev.unlock_pct == 0.0:
        return 'tier1'
    if ev.event_type == 'unlock':
        if ev.unlock_pct >= TIER1_UNLOCK_PCT:
            return 'tier1'
        elif ev.unlock_pct >= TIER2_UNLOCK_PCT:
            return 'tier2'
    if ev.event_type in ('governance', 'airdrop'):
        return 'tier2'
    return None

def should_withdraw(ev: Event, today: date) -> Optional[dict]:
    tier = classify_event(ev)
    if tier is None:
        return None
    lead = TIER1_LEAD_DAYS if tier == 'tier1' else TIER2_LEAD_DAYS
    trigger_date = ev.event_date - timedelta(days=lead)
    if today >= trigger_date and today < ev.event_date:
        fraction = 1.0 if tier == 'tier1' else TIER2_WITHDRAW_PCT
        return {
            'action': 'WITHDRAW',
            'tier': tier,
            'fraction': fraction,
            'reason': (f"{ev.event_type} {ev.unlock_pct*100:.1f}% supply on {ev.event_date}; "
                       f"lead={lead}d, withdraw {fraction*100:.0f}%")
        }
    return None

def can_reenter(pool: PoolState, days_since_event: int) -> tuple[bool, list[str]]:
    fails = []
    if pool.vol_4h > pool.vol_7d_avg * REENTRY_VOL_MULT:
        fails.append(f"4h vol {pool.vol_4h:.0f}% > {REENTRY_VOL_MULT}× pre-event avg {pool.vol_7d_avg:.0f}%")
    if days_since_event < REENTRY_HOLD_HRS // 24:
        fails.append(f"only {days_since_event}d since event; need {REENTRY_HOLD_HRS//24}d stable vol")
    if pool.tvl_current < pool.tvl_pre_event * REENTRY_TVL_FLOOR:
        fails.append(f"pool TVL {pool.tvl_current/1e6:.1f}M < {REENTRY_TVL_FLOOR*100:.0f}% of pre-event {pool.tvl_pre_event/1e6:.1f}M")
    if pool.dvol > pool.dvol_7d_peak * 0.90:
        fails.append(f"DVOL {pool.dvol:.0f} still near event peak {pool.dvol_7d_peak:.0f}")
    gas_pct = pool.gas_cost_usd / pool.capital_usd if pool.capital_usd > 0 else 1.0
    if gas_pct > REENTRY_GAS_MAX:
        fails.append(f"gas {gas_pct*100:.2f}% of capital > {REENTRY_GAS_MAX*100:.1f}% max")
    return len(fails) == 0, fails
```

## Indicators / data used

- **Event calendar** — `GET /api/v1/event/calendar?type=unlock&days=30` — filterable 30-day forward event schedule; filter by `type=unlock` for token unlock events and `type=upgrade` for protocol upgrades. Source: [[cryptodataapi-regimes]] event/catalyst regime family.
- **Per-symbol event detail** — `GET /api/v1/event/regime/{symbol}` — pending catalysts for a specific token; use this to check whether the pool's underlying asset has a catalyst within the next 30 days.
- **Event Risk score** — `GET /api/v1/event/regime/score` — composite 0–100 event risk index; elevated score (> 60) indicates multiple catalysts active, suggesting heightened withdrawal posture across all LP positions.
- **Volatility regime** — `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime label and 60-day history; used to confirm post-event vol stabilisation before re-entry.
- **Vol-stress score** — `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite 0–100; used as a secondary re-entry check (re-enter only when vol-stress < 50 after an event).
- **Liquidity depth** — `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps; used to estimate gas-adjusted re-entry slippage for the on-chain transaction.
- **Regime context** — `GET /api/v1/regimes/current` — 10-state macro regime; in `Structural_Shock` or `Established_Bear` regimes, extend re-entry delay to T + 7 from default T + 3/T + 2.

*Note: DeFi-specific pool analytics (Uniswap TVL by pool, per-pool fee income, real-time IL estimates) are not available on CryptoDataAPI. Use Uniswap v3 subgraph (The Graph) or DeFiLlama API for pool-level analytics. The CryptoDataAPI event calendar covers token unlocks and macro events; verify protocol-specific upgrade dates directly from the protocol's governance forum or documentation.*

## Example trade

**Setup (illustrative — ARB token unlock in ETH/ARB Uniswap pool)**

- Capital: $80,000 in an ETH/ARB Uniswap v3 0.3% pool. Range: $1.20–$2.00 ARB/USD.
- Event detected: ARB 7.5% supply unlock in 8 days (T − 8). Tier 1 classification (≥ 5%).
- **Action at T − 7:** withdraw full LP position. Gas cost: ~$15 (Arbitrum L2).
  - Receive: ~$40,000 ETH + ~$40,000 ARB.
  - Hold ARB in wallet; may hedge via perp short if feasible.

**Event day (T = 0):**
- ARB price drops 22% as unlocked supply enters the market.
- LVR extraction during 72h event window (estimated): ~$2,800 (at 80% annualised vol for 3 days on $40k ARB).
- Missed fee income during 7-day withdrawal: ~$140 (0.3% pool × 7 days × low-vol pre-event trading volume).
- **Net saving vs passive LP: ~$2,660 avoided loss.**

**Re-entry at T + 4:**
- ARB stabilised at $1.45 (−22% from T − 7, but flat for 2 days).
- 4h vol = 62% annualised ≤ 1.5× pre-event average of 45% = 67.5% → condition met.
- Pool TVL: $12M (was $18M pre-event — 67%, above 50% floor).
- Gas cost re-entry: ~$18. Gas fraction: $18 / $80,000 = 0.02% < 0.5% threshold.
- **Re-enter LP at new reference price $1.45. New range: $1.05–$1.95.**
- Recovery window fee income (weeks 1–3 post-event, elevated vol → elevated volume): estimated $480/week vs pre-event $140/week.

*(Illustrative round numbers. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.8 | Comparing to continuous LP deployment; IL avoided minus missed fees and gas |
| Expected max drawdown | ~15% | Scenario where event resolves poorly AND no re-entry bonus (pool death) |
| Win rate per event | ~70% (estimated) | Tier 1 events with ≥ 5% unlock cause material LVR in ~70% of cases based on price-impact data |
| Average withdrawal period | 7–14 days | 7 days (Tier 1 lead) + 3–7 days to re-entry |
| Gas cost per cycle | $10–$50 (L2) / $100–$400 (Ethereum mainnet) | L2 deployment strongly preferred at sub-$100K position sizes |
| Breakeven position size | ~$10,000 (L2) | At $15 gas cost × 2 transactions, the saving must exceed $30 |

**Cost overlay:** Two gas transactions per event cycle are the primary cost. At $15/transaction on Arbitrum, two transactions = $30; the avoided LVR must exceed $30 for the trade to be net-positive. For a $10,000 LP position in a high-vol event (60% annualised vol for 7 days): LVR ≈ (0.60)²/8 × (7/365) × $10,000 = ~$108 avoided. Gas = $30. Net benefit = ~$78. The math works on L2 at $10K+ positions.

## Capacity limits

- **Per-pool:** `capacity_usd: 15000000` — above ~$15M per pool, withdrawal creates measurable price impact on pool TVL and signals the trade to competitors.
- **Cross-pool:** No effective capacity limit across multiple pools simultaneously; the strategy scales by diversifying across pools and chains.
- **Gas economics:** Capacity scales with L2 adoption. On Ethereum mainnet, minimum viable position is ~$50,000 for a Tier 2 event and ~$200,000 for a Tier 1 event (gas costs ~$400 × 2 = $800 per cycle).

## What kills this strategy

1. **Event calendar data gaps (#6: Data / execution).** If the unlock schedule is not captured by CryptoDataAPI's event calendar (e.g., community-managed or vesting-cliff unlocks not registered), the withdrawal doesn't happen and the LP absorbs the event LVR. Mitigate: cross-reference with TokenUnlocks.app, Dune Analytics unlock dashboards, or project documentation.
2. **Pool death spiral (#1: Primitive degradation).** If the underlying token enters a sustained downtrend rather than recovering post-event, the re-entry never triggers and capital sits idle. The pool may die (TVL < floor) permanently, eliminating the re-entry opportunity and forcing redeployment to a different pool.
3. **Gas spike during high-congestion event (#6: Data / execution).** Large unlock events often coincide with network congestion (many holders transacting simultaneously). If gas spikes to 10× normal at withdrawal time, the cost may exceed the LVR saving for mid-size positions. Mitigate: use L2 deployments or schedule withdrawal 7 days in advance (lead time for Tier 1 events avoids the last-minute congestion).
4. **IL on held tokens during withdrawal period (#1: Primitive degradation).** The LP holds the withdrawn tokens during the event window. If the base token (e.g., USDC) is held, there is no IL risk. If the risky token (ARB) is held, its price decline during the event creates the same IL as the LP would have suffered — the LVR saving is offset by the mark-to-market loss on the held position. Mitigate: convert 50% of risky token to stablecoin at withdrawal time, or hedge with a perp short.

## Kill criteria

Pause or retire on any of:

1. **Three consecutive event cycles where LVR avoided < gas cost paid** (event classification over-sensitive; recalibrate Tier 1/2 thresholds upward).
2. **Re-entry conditions never trigger for 3 consecutive Tier 1 events** (pools are entering death spirals; underlying token selection is too risky — reassess pool universe).
3. **Gas costs exceed 1% of withdrawn capital on any single cycle** (L1 gas too high for the position size; migrate to L2 or pause until gas normalises or position size scales).
4. **Event calendar data source produces 2+ false events** (events listed that do not materialise; recalibrate data source or add manual verification step).

See [[when-to-retire-a-strategy]] for the broader framework.

## Advantages

- **Forward-looking, not reactive** — withdrawing 7 days before the event avoids all event-window LVR, not just the worst day; the regime gate ([[defi-yield-regime-gate]]) only reacts after vol has already risen.
- **Composable with [[defi-yield-regime-gate]]** — the two pages are complementary: regime gate handles continuous vol; this page handles discrete events. Running both avoids both ambient high-vol regimes AND scheduled catalysts.
- **Re-entry bonus captures elevated fees** — the post-event recovery window has elevated fee income as high vol attracts arbitrage volume; re-entrants collect more fees per unit of LP than passive LPs who averaged in through the event.
- **Low crowding risk** — retail LPs do not systematically monitor token unlock calendars; the strategy benefits from the crowd's calendar blindness.

## Disadvantages

- **Gas costs limit viability on Ethereum mainnet** — the minimum economic position size on mainnet (~$50K–$200K per Tier 1 event) excludes many retail LPs. This strategy is most viable on L2 or on Solana-based AMMs with negligible gas costs.
- **Missed fee income during withdrawal window** — 7–14 days without fee income per Tier 1 event is a real opportunity cost, especially in high-APR pools.
- **Re-entry uncertainty** — the re-entry condition may never trigger if the pool dies or the token does not recover. Unlike a CEX strategy pause that automatically resumes, this strategy requires active re-entry execution.
- **IL on held risky tokens** — unless the risky token is hedged or converted to stablecoin during the withdrawal, the mark-to-market loss on the held tokens can negate the LVR saving.

## Sources

- Milionis, J. et al. (2022). "Automated Market Making and Loss-Versus-Rebalancing." SSRN Working Paper. Establishes the LVR = σ²/8 per unit time framework.
- [[defi-yield-regime-gate]] — the continuous vol-regime gate; this page adds the discrete event-calendar dimension.
- [[event-calendar-risk-gating]] — the CEX-side event calendar framework; this page is the DeFi LP analog.
- [[options-rv-event-calendar]] — the options RV analog (actively trading event premium vs this page's passive avoidance).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/event/calendar?type=unlock&days=30` — 30-day forward token unlock calendar; primary event detection
- `GET /api/v1/event/regime/{symbol}` — per-symbol pending catalysts (Pro+); verify specific pool tokens
- `GET /api/v1/event/regime/score` — composite event risk 0–100; use as portfolio-level alert when > 60
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime label and 60-day history; re-entry condition check
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress 0–100; secondary re-entry gate (< 50 preferred)
- `GET /api/v1/liquidity/depth` — per-coin book depth; estimate on-chain slippage for swap sizing at withdrawal
- `GET /api/v1/regimes/current` — macro regime context; extend re-entry delay in Structural_Shock or Bear regimes

**Historical data:**
- `GET /api/v1/event/calendar` with date range — historical event catalog for backtesting withdrawal protocols
- `GET /api/v1/volatility/regime/{symbol}` — 60-day vol history per asset for re-entry threshold calibration

*Note: DeFi pool-level data (TVL by pool, per-pool fee income, real-time IL) are not available via CryptoDataAPI. Use The Graph (Uniswap v3 subgraph), DeFiLlama, or TokenUnlocks.app for pool-level analytics and unlock schedule cross-referencing.*

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/event/calendar?type=unlock&days=30"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

**Live dashboards:** [long-term regimes](https://cryptodataapi.com/regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Event leg** — `GET /api/v1/event/calendar?type=unlock&days=30` + `GET /api/v1/event/regime/{symbol}` — the forward unlock calendar that schedules LP withdrawals
- **Vol re-entry leg** — `GET /api/v1/volatility/regime/{symbol}` + `GET /api/v1/volatility/regime/score` — re-enter pools only after per-asset vol normalises
- **Regime gate** — `GET /api/v1/regimes/current` — extend the re-entry delay in Structural Shock or bear states
- **Backtest** — post-unlock price paths from `GET /api/v1/backtesting/klines` (daily back to 2017-08); point-in-time event and vol state from `GET /api/v1/backtesting/daily-snapshots` (since 2026-03-02); pool-level TVL/fee history stays external (DeFiLlama, The Graph)
- **Tips** — alert on `GET /api/v1/event/regime/score` > 60 as the portfolio-level pre-withdrawal tripwire; the 60d cap on per-symbol vol history bounds how far back re-entry thresholds can be calibrated from the live endpoint

## Related

- [[defi-yield-regime-gate]] — continuous vol-regime gate for LP deployment; composable first layer under this page
- [[event-calendar-risk-gating]] — CEX strategy event calendar framework; same concept for carry/grid/vol-selling books
- [[defi-yield-sentiment-entry]] — sentiment-extreme entry gate for LP deployment; composable with both regime gate and this event calendar page
- [[options-rv-event-calendar]] — options RV term-structure positioning around events; same calendar, different instrument
- [[unlock-cascade-watch]] — cascade-fade staging around unlocks; run alongside this page (withdraw LP → stage cascade fades)
- [[unlock-short-with-crowding-gate]] — directional short into unlocks; different primitive (short vs LP withdrawal)
- [[delta-neutral-yield-farming]] — hedged LP; composable with this event calendar gate (also withdraw the delta hedge at T − 7)
- [[concentrated-liquidity]] — LP range management; this page adds the event-calendar dimension
- [[impermanent-loss]] — the LP loss mechanism; LVR is the continuous component, IL is the path-dependent realised component
- [[loss-versus-rebalancing]] — the formal LVR framework underpinning this page's math
- [[token-unlock]] — token unlock mechanics and historical price impact data
