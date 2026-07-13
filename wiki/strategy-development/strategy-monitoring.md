---
title: "Strategy Monitoring & Alerting"
type: concept
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [strategy-development, risk-management, execution, arbitrage, backtesting]
aliases: ["Strategy Monitoring", "Trading Alerts", "Strategy Dashboard"]
domain: [strategy-development]
difficulty: advanced
related: ["[[failure-modes]]", "[[edge-taxonomy]]", "[[research-checklist]]", "[[arbitrage-overview]]", "[[risk-management-overview]]", "[[arbitrage-parameter-cheatsheet]]", "[[leg-risk]]", "[[multi-venue-capital-management]]", "[[regime-matrix]]", "[[strategy-correlation-matrix]]", "[[when-to-retire-a-strategy]]", "[[transaction-cost-modeling]]", "[[slippage]]", "[[crowding-indicators]]"]
---

# Strategy Monitoring & Alerting

The [[failure-modes]] page catalogs *how* strategies die. The [[research-checklist]] defines *what to check* before deployment. This page operationalizes both: **what to monitor in real-time, what thresholds trigger alerts, and what actions to take when alerts fire.**

A strategy without monitoring is a strategy you'll discover has been losing money for weeks.

## Monitoring Cadence at a Glance

Every observable a live strategy needs sits in one of four cadences. The cadence is set by *how fast the thing it detects can hurt you* — execution failures kill in seconds, edge erosion kills over months — and each cadence maps to a [[failure-modes|failure mode]] it is designed to catch:

| Cadence | Layer | Detects | Failure mode caught | Owner |
|---|---|---|---|---|
| Real-time (sec) | L1 Execution | API/feed health, fills, reconciliation | Operational (mode 7) | Automated alerts |
| Daily | L2 Performance | P&L, drawdown, Sharpe, win rate, turnover | Early decay, capacity, cost (modes 2/5/6) | Daily review |
| Weekly/Monthly | L3 Edge Health | Spread compression, regime, correlation, cost drift | Crowding, regime, correlation (modes 2/3/8) | Periodic deep review |
| Event-driven | Cross-layer | Rule/venue announcements, deal news | Structural/regulatory (mode 4) | News + filings monitor |

The design principle: **match the polling frequency to the failure speed.** Polling edge-health metrics every second wastes resources and creates alert fatigue; polling execution health daily means you discover a dead API after a day of unhedged exposure. The three-layer split below is the practical implementation of this principle.

## Dashboard Architecture

### Three-Layer Monitoring

| Layer | What It Monitors | Update Frequency | Who Watches |
|---|---|---|---|
| **L1: Execution** | Fill rates, slippage, API health, position reconciliation | Real-time (seconds) | Automated alerts |
| **L2: Performance** | P&L, Sharpe, drawdown, win rate, turnover | Daily | Daily review |
| **L3: Edge Health** | Regime detection, crowding signals, cost drift, correlation changes | Weekly/monthly | Periodic deep review |

### L1: Execution Monitoring (Real-Time)

These metrics detect operational failures — things breaking right now.

| Metric | Alert Threshold | Action |
|---|---|---|
| **API response time** | > 2× normal latency for 5+ consecutive calls | Switch to backup endpoint or pause strategy |
| **WebSocket disconnect** | Any disconnect > 10 seconds | Auto-reconnect, pause trading until feed confirmed live |
| **Fill rate (bilateral)** | < 80% of arb attempts completing both legs | Pause, investigate. Possible: venue issues, parameter staleness, competition |
| **Slippage vs. expected** | Actual slippage > 2× modeled slippage for 10+ consecutive trades | Recalibrate cost model. Possible: liquidity has thinned |
| **Partial fill rate** | > 30% of orders partially filling | Reduce position size or use FOK orders |
| **Position reconciliation mismatch** | Long/short notional diverges > 3% | Rebalance immediately. Reconciliation failure = directional exposure |
| **Exchange balance** | Drops below 30% of target allocation | Trigger rebalancing. See [[multi-venue-capital-management]] |
| **Order rejection rate** | > 5% of orders rejected | Investigate: margin, rate limits, ToS changes, maintenance mode |

**Position reconciliation procedure (run every 5 minutes):**
```
for each active arb position:
    long_notional = sum(long_leg_qty × current_price)
    short_notional = sum(short_leg_qty × current_price)
    imbalance = abs(long_notional - short_notional) / max(long_notional, short_notional)
    if imbalance > 0.03:
        ALERT: "Position imbalance {imbalance:.1%} on {strategy}. Rebalance needed."
```

### L2: Performance Monitoring (Daily)

These metrics detect performance degradation — the strategy slowly dying.

| Metric | Calculation | Alert Threshold | Significance |
|---|---|---|---|
| **Daily P&L** | Net realized + unrealized | Loss > 2% of allocated capital | Single-day halt trigger |
| **Rolling 5-day P&L** | Sum of last 5 trading days | Loss > 3% | Short-term trouble |
| **Rolling 30-day Sharpe** | Annualized (mean_return / std_return × sqrt(252)) | < 0.5 | Strategy underperforming. Investigate cause |
| **Rolling 30-day Sharpe** | Same | < 0.0 | Strategy losing money risk-adjusted. Prepare to pause |
| **Maximum drawdown** | Peak-to-trough of cumulative P&L | > 10% of allocated capital | Review kill criteria |
| **Maximum drawdown** | Same | > 20% | Pause strategy. Full review required |
| **Win rate** | Wins / Total trades (rolling 100 trades) | Drops > 15% below historical average | Possible edge decay |
| **Average profit per trade** | Net P&L / Trade count (rolling 100) | Drops > 30% below historical average | Possible cost inflation or spread compression |
| **Turnover** | Daily traded notional / Portfolio value | > 2× or < 0.5× normal | Unusual trading activity — investigate |

**Daily P&L report template:**
```
=== Daily Strategy Report: 2026-04-20 ===
Strategy: Funding Rate Arb (Binance + Hyperliquid)
  Gross P&L:     +$127.40
  Fees paid:     -$18.20
  Funding recv:  +$145.60
  Net P&L:       +$127.40
  Drawdown:      -1.2% (from peak)
  30d Sharpe:    2.1
  Positions:     BTC spot +2.5, BTC perp -2.5 (balanced)
  Status:        HEALTHY

Strategy: Cross-Exchange Arb (Multi-venue)
  Trades today:  12 attempted, 10 completed, 2 failed (1 stranded leg)
  Gross P&L:     +$89.50
  Unwind losses: -$31.20 (from 1 stranded leg)
  Net P&L:       +$58.30
  Fill rate:     83% (below 90% target — YELLOW)
  30d Sharpe:    1.4
  Status:        MONITOR (fill rate declining)
```

### L3: Edge Health Monitoring (Weekly/Monthly)

These metrics detect structural changes — the edge eroding or the market regime shifting.

| Metric | How to Measure | Alert Threshold | Interpretation |
|---|---|---|---|
| **Gross spread compression** | Average pre-cost arb spread over rolling 30 days | Declines > 30% from deployment baseline | Competition is increasing. See [[crowding-indicators]] |
| **Funding rate mean** | 30-day average funding rate (for funding arb) | Drops below breakeven threshold (see [[arbitrage-parameter-cheatsheet]]) | Bull market may be ending; funding arb becomes unviable |
| **Regime change** | VIX level, crypto volatility, trend indicators | VIX crosses 25 (up) or 15 (down) | Regime shift. Check [[regime-matrix]] for strategy implications |
| **Strategy correlation** | Pairwise correlation of daily P&L across all active strategies | Any pair > 0.6 for 20+ days | Concentration risk. See [[strategy-correlation-matrix]] |
| **Cost drift** | Actual execution costs vs. modeled costs | Actual > modeled by > 20% for 30+ days | Recalibrate cost model. See [[transaction-cost-modeling]] |
| **Crowding proxy** | Open interest growth, AUM-to-volume ratio | OI growth > 50% in 30 days while spread compresses | Crowding — see [[crowding-indicators]]. Consider reducing size |
| **Borrow rate changes** | Cost to borrow short-leg securities | Increases > 5% annualized | Affects [[pairs-trading]], merger-arbitrage, convertible-arbitrage profitability |
| **Regulatory change** | News monitoring, exchange announcements | Any relevant regulation proposed or enacted | See [[regulatory-risk-map]]. Assess impact within 24 hours |

**Monthly edge health review checklist:**
1. Has the gross spread (pre-cost) compressed since last month?
2. Has competition visibly increased (new bots, faster fills against you)?
3. Have exchange fees or rules changed?
4. Has the market regime shifted? What does [[regime-matrix]] say about current conditions?
5. Are strategy correlations increasing? Run crisis-conditional correlation check
6. Does the [[failure-modes]] decision tree diagnose any active failure pattern?
7. Are kill criteria approaching? How close is each metric to its threshold?

## Kill Criteria Operationalization

The [[failure-modes]] page defines kill criteria conceptually. Here's how to implement them as automated rules:

### Universal Kill Criteria

```
# Hard kills — pause immediately, do not resume without manual review
if drawdown > max_drawdown_threshold:       # typically 15-25%
    KILL("Max drawdown exceeded")

if rolling_60day_sharpe < 0:
    KILL("Negative Sharpe over 60 days")

if daily_loss > 0.03 * allocated_capital:   # 3% single-day loss
    KILL("Catastrophic daily loss")

# Soft kills — reduce position by 50%, alert for review
if rolling_30day_sharpe < 0.3:
    REDUCE_AND_ALERT("Sharpe deterioration")

if win_rate < historical_win_rate * 0.7:    # 30% decline
    REDUCE_AND_ALERT("Win rate decay")

if avg_profit_per_trade < breakeven_after_costs:
    REDUCE_AND_ALERT("Below cost breakeven")
```

### Strategy-Specific Kill Criteria

| Strategy | Kill If | Reason |
|---|---|---|
| [[funding-rate-arbitrage]] | 7-day avg funding rate < 0.005% (8h) | Below risk-free rate after costs |
| [[funding-rate-arbitrage]] | Funding negative for 3+ consecutive periods | Active bleed |
| [[cross-exchange-arbitrage]] | Bilateral fill rate < 70% for 7+ days | Execution infrastructure failing |
| [[cross-exchange-arbitrage]] | Average spread < minimum viable spread for 14+ days | Edge has been arbitraged away |
| [[pairs-trading]] | Cointegration p-value > 0.10 on rolling test | Relationship has broken |
| [[pairs-trading]] | Z-score exceeds 4.0 and continues diverging | Structural break, not mean reversion |
| merger-arbitrage | Deal officially terminated | Close position at market |
| merger-arbitrage | Regulatory challenge announced | Re-evaluate spread vs. deal-break probability |
| [[volatility-arbitrage]] | Realized vol persistently > IV for 30+ days (if short vol) | Regime of underpriced options |
| [[statistical-arbitrage]] | Net exposure > ±20% for 5+ days | Market-neutral constraint violated |

## Alert Delivery

| Severity | Channel | Response Time |
|---|---|---|
| **CRITICAL** (kill trigger, stranded leg, API down) | SMS + push notification + email | Immediate (< 5 minutes) |
| **WARNING** (threshold approaching, performance declining) | Push notification + email | Within 1 hour |
| **INFO** (daily summary, monthly review due) | Email + dashboard | Next scheduled review |

### Health-status definitions (traffic-light)

Every strategy reports a single rolled-up status each day so a portfolio of many strategies can be scanned at a glance. The status is the *worst* condition across its layers:

| Status | Meaning | Condition | Action |
|---|---|---|---|
| **GREEN / HEALTHY** | Operating within all bands | No threshold breached | Normal review cadence |
| **YELLOW / MONITOR** | A warning threshold crossed | One soft threshold breached, no kill trigger | Daily attention; investigate cause |
| **ORANGE / REDUCE** | Soft kill fired | Sharpe deterioration, win-rate decay, or cost breakeven | Cut size ~50%, schedule review |
| **RED / KILL** | Hard kill fired | Max drawdown, negative 60d Sharpe, catastrophic daily loss, or stranded leg | Pause immediately, manual review before resume |

### Alert-response runbook

An alert is only useful if the response is pre-decided. Map each alert class to a fixed first action so the on-call decision is mechanical, not improvised under stress (the same logic as pre-committed [[failure-modes#Build Kill Criteria From Failure Modes|kill criteria]]):

| Alert | Likely failure mode | First action | Then |
|---|---|---|---|
| API latency / disconnect | Operational (7) | Failover to backup endpoint; pause if feed unconfirmed | Resume only after live-feed check |
| Bilateral fill rate drop | Operational / cost (7/5) | Pause new entries | Investigate venue, competition, parameter staleness |
| Position imbalance > 3% | Operational (7) | Rebalance immediately | Reconcile; find the missed fill |
| Slippage > 2× modeled | Cost inflation (5) | Recalibrate [[transaction-cost-modeling\|cost model]] | Re-check breakeven margin; widen bands |
| 30d Sharpe < 0.3 | Decay / regime (2/3) | Reduce size, flag for review | Run monthly edge-health checklist |
| Drawdown > 20% | Any terminal mode | Pause strategy | Full review against [[failure-modes]] tree |
| Gross spread compressed > 30% | Crowding (2) | Reduce size | Check [[crowding-indicators]]; consider niche version |
| Regime indicator flip (VIX cross) | Regime change (3) | Re-check [[regime-matrix]] | Pause regime-incompatible sleeves |
| Regulatory / venue news | Structural (4) | Assess within 24h | Usually terminal — prepare to retire |
| Correlation pair > 0.6, 20d+ | Correlation surprise (8) | Cut gross exposure | Diversify across [[edge-taxonomy\|edge sources]] |

## Position Reconciliation

Reconciliation verifies that your actual positions match what you think you have. Discrepancies arise from: partial fills not properly tracked, manual interventions not logged, exchange-side liquidations, or software bugs.

### Daily Reconciliation Procedure

1. **Pull positions from each exchange** via API
2. **Pull positions from your internal system** (database/spreadsheet)
3. **Compare:** For each asset on each venue, check `exchange_qty == internal_qty`
4. **Flag discrepancies** > 0.1% of position size
5. **Resolve:** Determine source (missed fill, manual trade, exchange adjustment) and correct internal records
6. **Verify P&L:** Compare exchange-reported P&L to internally calculated P&L. Discrepancy > $50 requires investigation

### Weekly Reconciliation

1. All of the above, plus:
2. **Cross-venue net position check:** Total longs across all venues should approximately equal total shorts (for market-neutral strategies). Net exposure ≈ 0
3. **Capital balance check:** Sum of all exchange balances + reserve ≈ total allocated capital (accounting for unrealized P&L)
4. **Fee audit:** Compare fees paid (from exchange trade history) to fees expected (from your cost model)

## Dashboard Tools

| Tool | Best For | Cost |
|---|---|---|
| **Grafana + InfluxDB** | Custom real-time dashboards, time-series metrics | Free (self-hosted) |
| **TradingView alerts** | Price-based alerts, simple technical conditions | Free-$60/mo |
| **Custom Python + Telegram bot** | Programmatic alerts, position monitoring | Free |
| **QuantConnect** | Backtesting + live monitoring in one platform | Free-$100/mo |
| **3Commas / Bitsgap** | Multi-exchange portfolio tracking | $15-100/mo |
| **Excel/Google Sheets** | Manual daily tracking, works for small portfolios | Free |

For serious multi-venue arb, a custom solution (Python + exchange APIs + Grafana + Telegram alerts) is typically necessary because no commercial tool covers all the reconciliation and multi-leg tracking requirements.

## Common Monitoring Pitfalls

A monitoring system can fail in its own ways, often quietly. The recurring failure modes of the monitoring stack itself:

| Pitfall | Mechanism | Consequence | Fix |
|---|---|---|---|
| **Alert fatigue** | Too many low-value alerts | Real alerts ignored | Tune thresholds; tier by severity |
| **Missing a layer** | Only L2 P&L monitored | Blind to operational and edge failures | Implement all three layers |
| **No kill commitment** | Thresholds exist but action is discretionary | Strategy ridden into the ground | Pre-commit hard/soft actions |
| **Monitoring the monitor never** | No heartbeat on the alert system | Silent failure = false "all clear" | Dead-man's-switch / heartbeat alert |
| **Static thresholds** | Bands tuned at deployment, never updated | False alerts in new regime, or misses | Re-baseline on each regime shift |
| **No paper-vs-live diff** | Live not reconciled to backtest | Operational drift invisible | Daily paper-vs-live P&L compare |
| **Survivorship in baselines** | "Historical average" excludes bad periods | Thresholds too optimistic | Baseline on full out-of-sample history |

The most dangerous of these is the fourth: a monitoring system that has silently died reports nothing, which is indistinguishable from "everything is fine." Every alerting pipeline needs a heartbeat — a periodic "I am alive" signal whose *absence* is itself an alert.

### Monitoring maturity ladder

Where a setup sits on this ladder predicts which [[failure-modes]] will blindside it:

| Level | Setup | Blind to |
|---|---|---|
| 0 | Eyeball P&L occasionally | Everything but a big loss |
| 1 | Daily P&L + drawdown alert (L2 only) | Operational, edge erosion |
| 2 | L1 + L2: execution health + performance | Crowding, regime, correlation |
| 3 | Full L1+L2+L3 + event monitoring | Mostly unknown-unknowns only |
| 4 | Level 3 + heartbeat + paper-vs-live + crisis-conditional correlation | Genuinely robust |

## Sources

- [[failure-modes]]
- [[edge-taxonomy]]
- [[research-checklist]]
- [[arbitrage-parameter-cheatsheet]]
- [[regime-matrix]]
- [[strategy-correlation-matrix]]
- [[transaction-cost-modeling]]
- [[when-to-retire-a-strategy]]
- [[crowding-indicators]]
- [[slippage]]
- [[risk-management-overview]]
