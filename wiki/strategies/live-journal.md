---
title: "Live Strategy Journal"
type: index
created: 2026-04-10
updated: 2026-04-27
status: good
tags: [strategies, journal, live, tracking, production]
aliases: ["Strategy Journal", "Production Strategy Log"]
related: ["[[strategies-overview]]", "[[when-to-retire-a-strategy]]", "[[trading-journal]]", "[[strategy-development-overview]]"]
---

# Live Strategy Journal

A running log of trading strategies that are or have been *actually deployed* — not just researched. Closes the loop from the [[strategies-overview|catalog]] of strategies (what *exists*) to the operational reality of *what's running, how it's performing, and why each one started or stopped*. This page is the production-side equivalent of [[wiki/log.md]] (which tracks wiki edits) and [[trading-journal]] (which tracks individual trades).

This journal answers questions that the catalog cannot:

- Which strategies have actually been deployed?
- Which are currently running, paused, or retired?
- What was the realized vs. expected performance of each?
- What was the dated reason for each lifecycle change?
- What lessons were learned that should feed back into [[failure-modes]] and [[research-checklist]]?

## How This Page Is Maintained

Each strategy lifecycle event gets an entry. Events include:

- **Deploy** — strategy moves from research to paper or pilot
- **Scale up** — pilot to full size
- **Pause** — temporarily halted (regime, drawdown, manual)
- **Resume** — restarted after pause
- **Retire** — permanently killed
- **Restart** — re-deployed after retirement (rare but possible)
- **Modify** — material parameter or rule change

Entries are append-only and dated. Modifications and reversals are recorded as new entries, not edits to old ones.

## Entry Format

```
## YYYY-MM-DD — [Strategy Name] — [Event Type]

- **Strategy:** [[strategy-page]]
- **Status:** active | paused | retired
- **Capital:** $X (or % of book)
- **Reason:** Why this event happened
- **Expected Sharpe:** from research
- **Realized Sharpe:** so far in production (if applicable)
- **Notes:** anything noteworthy
- **Next review:** date for the next scheduled review
```

## Active Strategies

The live trading bot runs a six-strategy stack on a perpetual DEX (primarily AsterDEX). Two strategies are currently ON; four are paper-traded and gated by regime triggers. All six pages are at `status: excellent`. See the regime stack mapping in [[regime-matrix#Portfolio D Live Bot Six-Strategy Stack the deployed production system]].

### Currently ON

| Strategy | Page | Capital allocation | Activity | Last review |
|---|---|---|---|---|
| funding_arb | [[funding-rate-arbitrage]] | 1x isolated, max 25% per asset, max 3 concurrent | ~7 signals/24h | 2026-04-27 |
| stock_basis | [[stock-perp-oracle-basis]] | 2x, 11.25% per stock, max 8 stocks | ~17 signals/24h | 2026-04-27 |
| stretch_revert (10 members) | [[stretch-revert]] | ~3-5x lev, 15m (theilsen 1x; fast_kama 1-5m loop) | 53 fills total; only 4 of 14 members have traded | 2026-07-20 |

### Paper-traded / OFF (regime-gated)

| Strategy | Page | Sizing | Reason OFF | Restart trigger |
|---|---|---|---|---|
| liquidation_reversal | [[liquidation-cascade-fade]] | 3x, 5% per trade, max 2 concurrent | Awaiting cascade event | Liquidation spike ≥ 3× 24h avg + price drop > 2%/15min + CVD exhaustion |
| mean_reversion | [[rsi-mean-reversion]] | 3x, 5% per trade, BTC/ETH/SOL only | RSI(2) not at extreme + F&G not in fear zone | RSI(2) < 10 + price > 200d SMA + F&G < 30 |
| trend_following | [[moving-average-crossover]] | 2x, max 8% per asset, inverse-vol sized | Awaiting regime trend | 50/200 SMA crossover (golden or death) on monitored universe |
| grid | [[grid-trading]] | 1x, 15% across grid, 10 levels | Range filter not satisfied | ADX(14) < 20 + Bollinger bandwidth percentile < 20 |



```dataview
TABLE status, expected_sharpe, deploy_date, capital_allocation
FROM "wiki/strategies"
WHERE backtest_status = "live" AND status != "retired"
SORT deploy_date DESC
```

## Paused Strategies

*Strategies temporarily halted but not retired.*

```dataview
TABLE pause_reason, pause_date, restart_criteria
FROM "wiki/strategies"
WHERE backtest_status = "paused"
SORT pause_date DESC
```

## Retired Strategies

*Strategies that have been permanently killed. Each one is a lesson for future research.*

```dataview
TABLE retire_date, retire_reason, lifetime_sharpe, lessons_learned
FROM "wiki/strategies"
WHERE backtest_status = "retired"
SORT retire_date DESC
```

## Lifecycle Events Log

Append-only chronological log of every lifecycle event. The dataview tables above are derived from frontmatter; this section is the human-readable narrative.

---

### 2026-07-20 — Stretch Revert family — Documented (already live)

- **Strategy:** [[stretch-revert]] — 14-member baseline-estimator family, 10 members on the real-money prod bot
- **Status:** active
- **Capital:** not recorded. Average trade P/L is ~$0.94, so position sizes are very small; sizing policy for this family is undocumented in this vault.
- **Reason:** Documented retrospectively from a Hyperliquid Trader dashboard snapshot (2026-07-20 11:23:51 AEST). **This family was deployed before it was journaled** — this entry backfills the record, it does not mark a deploy event. Deploy dates for individual members are unknown.
- **Expected Sharpe:** no research figure exists. The frontmatter carries 0.5 as a literature-informed estimate, not a measured or backtested value.
- **Realized Sharpe:** not meaningfully computable. 53 fills across 4 of 14 members; the confidence interval spans zero comfortably ([[crypto-short-history-statistical-power]]).
- **Notes:** Reported snapshot totals: +$50.08 realised, 77% trade-weighted win rate. Both figures are misleading on their own and should not be quoted without the following:
  - **10 of 14 members have never traded.** The "14 live" count is an installation count, not an evidence count.
  - **`frama` is 94% of P/L** (+$47.17 of +$50.08 over 28 fills). The family result is the frama result.
  - **`theilsen`: 80% win rate, −$3.00 net.** High win rate is the *expected* shape for reversion (win small often, give it back in one unreverting move), so win rate is close to uninformative here. `vidya` shows the same tension: PF 1.34, Sharpe −0.06.
  - **Multiple-comparisons problem.** Fourteen variants were run and the best is being read as a result. [[deflated-sharpe-ratio]] deflation for 14 trials is required before frama's record means anything — and cannot be computed correctly at all for `jma_stretch_revert`, whose baseline is a proprietary black box ([[jurik-moving-average]]).
  - **Known structural defects** documented on [[stretch-revert]]: the [[z-score]] understates large dislocations, no member uses a robust scale estimator ([[median-absolute-deviation]]), [[zero-lag-exponential-moving-average|ZLEMA]] is biased toward fading accelerating moves, and 4 of 14 baselines share one author ([[john-ehlers]]).
- **No backtest, walk-forward, or cost-corrected record exists** for any member. `backtest_status: live` reflects deployment, not validation.
- **Next review:** 2026-08-20 — by then, check whether members other than `frama` have accumulated enough fills to test the defence-in-depth claim.

### 2026-04-27 — Live bot six-strategy stack — Documentation snapshot

- **Context:** Wiki upgraded all six bot strategies to `status: excellent`. This entry establishes the canonical record of deployment status as of today. Previous deployments may exist but were not journaled.
- **Stack composition:** Two ON (funding_arb, stock_basis), four paper-traded with regime gates (liquidation_reversal, mean_reversion, trend_following, grid).
- **Diversification rationale:** The six strategies span complementary regimes per [[regime-matrix#Portfolio D Live Bot Six-Strategy Stack the deployed production system]]. The cleanest inverse pair is `grid` (needs ADX < 20) vs. `trend_following` (needs sustained trend) — these should never be simultaneously ON over the same universe.
- **Next review:** 2026-05-27 (1 month).

---

### 2026-04-01 — Funding Rate Arbitrage — Deploy

- **Strategy:** [[funding-rate-arbitrage]]
- **Status:** active
- **Venue:** AsterDEX (perpetual DEX)
- **Capital:** 1x isolated leverage, max 25% per asset, max 3 concurrent positions
- **Reason:** AsterDEX 8h funding rates persistently > 0.03% on majors during 2026-Q1 bull. Strategy is delta-neutral (spot held externally), so directional risk is hedged. Edge = collecting funding from long-side speculators.
- **Expected Sharpe:** 1.5 (research; subject to compression from Ethena/Resolv)
- **Realized Sharpe:** TBD (insufficient history)
- **Activity:** ~7 signals per 24h
- **Kill criteria:**
  - 7-day rolling funding average turns negative
  - Funding falls below 0.01% (no longer covers cost of capital)
  - AsterDEX counterparty event (insolvency, withdrawal halt, exploit)
- **Next review:** 2026-05-01 (monthly cadence)

### 2026-04-01 — Stock-Perp Oracle Basis — Deploy

- **Strategy:** [[stock-perp-oracle-basis]]
- **Status:** active
- **Venue:** AsterDEX stock perps (AAPL, AMZN, GOOG, META, MSFT, NVDA, TSLA + 1 rotating)
- **Capital:** 2x leverage, 11.25% per stock, max 8 stocks
- **Reason:** AsterDEX launched 24/7 stock perps in July 2025. Pyth oracle equity feeds remain stale during NYSE-closed hours, creating systematic drift that mean-reverts at NYSE open. High signal frequency (~17/24h) and high win rate justify the deployment.
- **Expected Sharpe:** 1.5 (research)
- **Realized Sharpe:** TBD
- **Activity:** ~17 signals per 24h (highest-frequency strategy in the stack)
- **Kill criteria:**
  - 30-day rolling Sharpe < 0
  - 3 consecutive earnings-night blow-ups (where overnight news is real, not noise)
  - AsterDEX changes oracle/funding mechanism (e.g., adopts continuous after-hours feed)
  - Pyth introduces continuous out-of-hours stock pricing (would erase the edge)
- **Next review:** 2026-05-01

### 2026-04-01 — Liquidation Cascade Fade — Paper Traded

- **Strategy:** [[liquidation-cascade-fade]]
- **Status:** paper-traded (regime-gated OFF)
- **Reason:** Strategy is event-driven; trigger conditions (liquidation spike ≥ 3× 24h avg + price drop > 2%/15min + CVD exhaustion) have not occurred in monitoring window. Bot is armed and will activate automatically.
- **Sizing when active:** 3x leverage, 5% per trade, max 2 concurrent
- **Expected Sharpe:** 1.2 (paper-traded across historical events: 2024-08-05 yen carry unwind, 2025-02-03 Trump tariff weekend, 2025-10-10 China tariff cascade)
- **Kill criteria:**
  - Strategy stops out 3 consecutive times (cascade not reverting — likely regime change to bear)
  - 6-month rolling P&L negative
  - Hyperliquid/AsterDEX adopt smoothed liquidation mechanisms that eliminate overshoot

### 2026-04-01 — RSI Mean Reversion — Paper Traded

- **Strategy:** [[rsi-mean-reversion]]
- **Status:** paper-traded (regime-gated OFF)
- **Reason:** Triple-filter (RSI(2) < 10 + price > 200d SMA + F&G < 30) has not triggered recently. Strategy is dormant pending the next dip-in-uptrend setup.
- **Sizing when active:** 3x leverage, 5% per trade, BTCUSDT/ETHUSDT/SOLUSDT only
- **Expected Sharpe:** 1.0 (paper-traded; Connors RSI(2) original SPY edge has compressed but crypto adaptation may have residual edge)
- **Kill criteria:**
  - 6-month rolling Sharpe < 0
  - 5 consecutive losses
  - 200d SMA broken on all 3 majors simultaneously (regime change to bear, filter invalidated)

### 2026-04-01 — Moving Average Crossover (Trend Following) — Paper Traded

- **Strategy:** [[moving-average-crossover]]
- **Status:** paper-traded (regime-gated OFF)
- **Reason:** No fresh 50/200 SMA crossover signal on monitored universe. Strategy waits for regime trigger.
- **Sizing when active:** 2x leverage, max 8% per asset, inverse-volatility sized (smaller positions in higher-ATR assets)
- **Expected Sharpe:** 0.5 (high crowding, post-publication decay since Brock 1992)
- **Kill criteria:**
  - 6-month rolling Sharpe < 0
  - More than 5 consecutive whipsaw losses
  - Universe-wide ADX averaging < 20 (no trends to ride)

### 2026-04-01 — Grid Trading — Paper Traded

- **Strategy:** [[grid-trading]]
- **Status:** paper-traded (regime-gated OFF)
- **Reason:** Filter (ADX < 20 + Bollinger bandwidth percentile < 20) not currently satisfied across monitored universe. Bot waits for compressed-range regime.
- **Sizing when active:** 1x leverage, 15% total spread across 10 grid levels, 2× ATR range-break exit
- **Expected Sharpe:** 1.0 (in-regime; the regime filter is the entire edge)
- **Kill criteria:**
  - 3 consecutive grid sessions stopped out by range break (regime filter is failing)
  - 30-day rolling P&L negative
  - Universe never satisfies regime filter for 60+ days (strategy is dormant — fine, but check that filter thresholds aren't too strict)

### Mutual exclusion rules (cross-strategy)

- `grid` and `trend_following` should never run on the same asset simultaneously — they have mutually exclusive regime requirements (ADX < 20 vs. sustained trend). The bot's regime detector ([[adx]]-based) handles this automatically.
- `funding_arb` and `liquidation_reversal` can both be ON simultaneously: their P&L drivers are independent (carry vs. event-driven crisis alpha). Liquidation_reversal acts as a partial hedge against funding_arb during liquidation cascades that flip funding negative.
- All six strategies share venue counterparty risk (AsterDEX). This is the dominant unhedged risk in the stack — see `[[multi-venue-capital-management]]` for diversification across venues.

---

## Why Have This Page?

The single most common pathology in active management is that *failed strategies stay alive for years* because there's no organized record of what was supposed to happen and when to admit it didn't. Specifically:

1. **No record of expected performance** → no benchmark for "is this working?"
2. **No record of deployment date** → drawdowns get measured from arbitrary points
3. **No pre-committed kill criteria** → strategies are retired only after enormous losses
4. **No record of dead strategies** → the same broken approach gets re-deployed under a new name
5. **No record of lessons learned** → mistakes repeat across strategies

This journal is the antidote. It forces explicit, dated entries for every lifecycle change, with reasons. Over time it builds a *track record of decisions* that's separate from the track record of returns — and the decision log is often more diagnostically valuable than the P&L.

## Relationship to Other Wiki Pages

- **[[strategies-overview]]** — the catalog of what *exists*. Strategy pages there are mostly *research-grade* (status: stub, draft, good).
- **This journal** — what's *deployed*, with dated history.
- **[[wiki/log.md]]** — wiki edits (administrative).
- **[[trading-journal]]** — individual trade entries (much more granular).
- **[[when-to-retire-a-strategy]]** — the principles applied here.
- **[[failure-modes]]** — the catalog of how strategies die. Each retired entry should reference a failure mode.

## Frontmatter Extensions for Live Strategies

When a strategy moves from research to deployment, its frontmatter should be extended with:

```yaml
backtest_status: live | paused | retired  # extended enum
deploy_date: 2026-04-10
expected_sharpe: 0.6
capital_allocation: "5% of book"
kill_criteria: |
  - drawdown > 20%
  - rolling 6-month Sharpe < 0
  - regime indicator X drops below threshold
last_review: 2026-04-10
next_review: 2026-05-10
```

These fields enable the dataview tables above and give a quick at-a-glance view of every production strategy's status.

## Sample Entry Templates

### Deployment Entry

```
## 2026-05-15 — Crypto Funding Rate Arbitrage — Deploy (Pilot)

- **Strategy:** [[funding-rate-arbitrage]]
- **Status:** active (pilot)
- **Capital:** $50K (10% of intended $500K size)
- **Reason:** Backtest validated through walk-forward + CPCV; deflated Sharpe = 0.78. Funding rates currently positive across BTC and ETH perps on Binance, OKX, Bybit. Cost analysis shows 200 bps margin of safety after fees.
- **Expected Sharpe:** 1.2 (research)
- **Realized Sharpe:** N/A
- **Kill criteria:** annualized basis < 5% rolling 30 days; rolling 3-month Sharpe < 0.3; venue counterparty risk event.
- **Next review:** 2026-06-15 (1 month)
```

### Pause Entry

```
## 2026-08-20 — Crypto Funding Rate Arbitrage — Pause

- **Strategy:** [[funding-rate-arbitrage]]
- **Status:** paused
- **Reason:** Funding rates have compressed to <2% annualized across all monitored venues. Below the cost-adjusted breakeven of 4%. Not a thesis failure — just a temporary unfavorable carry environment.
- **Drawdown:** -2% (within expected band)
- **Restart criteria:** Funding rates back above 5% annualized for 7 consecutive days.
- **Next review:** weekly funding rate check
```

### Retire Entry

```
## 2026-12-10 — Crypto Funding Rate Arbitrage — Retire

- **Strategy:** [[funding-rate-arbitrage]]
- **Status:** retired
- **Reason:** Funding rates have remained near zero or negative for 4 months despite multiple bull-run conditions where they historically would have spiked. Hypothesis: structural change in crypto market participants (more institutional vol-selling, less retail leverage), reducing the natural funding rate level. The mechanism that produced the historical edge may no longer be active.
- **Lifetime Sharpe:** 0.4 (vs. 1.2 expected)
- **Failure mode:** [[failure-modes#3-crowding--alpha-decay|alpha decay]] — structural change in the underlying market reduced the rate at which the strategy could capture funding.
- **Lessons learned:**
  - Should have built a leading indicator of funding-rate compression into the kill criteria
  - Crypto-specific strategies need shorter expected lifetimes built into the plan
  - The mechanism check ("why does this work?") should have been re-tested every quarter, not annually
- **Restart criteria:** Funding rates sustainably > 10% annualized AND open interest growing AND retail leverage participation rising.
```

## A Note on Privacy

If using this wiki to track *real personal* strategies, consider whether dollar amounts and specific positions should be redacted or scaled (e.g., always express size as % of book instead of dollars). The journal is most valuable when honest, so the goal is to capture truth without exposing it inappropriately.

## Sources

- [[when-to-retire-a-strategy]] — the principles
- [[failure-modes]] — the catalog of deaths
- [[trading-journal]] — the trade-level analog
- [[research-checklist]] — what should have been checked at deployment

## Related

- [[strategies-overview]]
- [[strategy-development-overview]]
- [[hypothesis-to-backtest-workflow]]
- [[when-to-retire-a-strategy]]
- [[failure-modes]]
- [[trading-journal]]
