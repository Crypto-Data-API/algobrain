---
title: "Crypto Forward Testing"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [backtesting, crypto, derivatives, methodology, hyperliquid, algorithmic]
aliases: ["Crypto Paper Trading", "Live Shadow Testing", "Champion-Challenger Crypto", "Perp Forward Testing"]
domain: [backtesting]
prerequisites: ["[[hyperliquid-backtesting]]", "[[trading-system-deployment]]"]
difficulty: advanced
related: ["[[hyperliquid-backtesting]]", "[[trading-system-deployment]]", "[[crypto-perp-backtesting-pitfalls]]", "[[funding-rate]]", "[[slippage-modeling]]", "[[auto-deleveraging]]", "[[execution-model-differences]]", "[[transaction-cost-modeling]]", "[[hypothesis-to-backtest-workflow]]", "[[walk-forward-analysis]]", "[[cryptodataapi-hyperliquid]]"]
---

# Crypto Forward Testing

The last gate before real size, and the one crypto perp bots fail most often. Forward testing runs a finished strategy *forward in wall-clock time* against live or simulated markets, with no historical data to overfit to, and measures whether the backtest's assumptions survive contact with a venue that charges hourly funding, fills against a real book, and can [[auto-deleveraging|force-close]] winning positions. It sits between the validated backtest ([[hyperliquid-backtesting]], [[crypto-perp-backtesting-pitfalls]]) and full deployment ([[trading-system-deployment]]): the backtest proves the edge *could* have existed; forward testing proves the plumbing *can capture it now*.

## Why Backtests Aren't Enough for Perp Bots

A perp backtest, however clean, silently assumes things a live venue does not grant: instant fills at the printed price, funding modelled coarsely, no partial fills, no ADL, and a static fee tier. Forward testing exists to price the gap between those assumptions and reality *before* capital is exposed. In crypto the gap is unusually wide because the venue mechanics are unusually punishing — 24/7 operation, hourly funding capped at 4%/hour on Hyperliquid, oracle-priced liquidation, and a HLP→insurance→ADL waterfall that can break a "neutral" hedge. Forward testing is where those show up as *realised* costs rather than modelling choices.

## Two Modes: Testnet vs Live-Info Shadow

There are two ways to run a strategy forward without risking size, and they catch different things.

| Mode | What it is | Catches | Misses |
|------|-----------|---------|--------|
| **Testnet** | Run against the venue's test environment (e.g. Hyperliquid testnet) with the real matching engine, fake funds | Order-lifecycle bugs, fill logic, API integration, latency shape | Real liquidity, real funding, real adversaries — testnet books are thin and unrepresentative |
| **Live-info shadow** | Run against *live mainnet* data feeds; generate orders but log them instead of submitting | Real signal frequency, real book depth, realistic intended fills, real funding accrual | Actual fill/queue reality — your unsent orders never move the book or wait in the real queue |

**Use both, in order.** Testnet first, to shake out the [[trading-system-deployment|deployment plumbing]] (auth, order state machine, reconnection) against a real matching engine with zero financial risk. Then live-info shadow against mainnet, to reconcile the strategy's *intended* behaviour against the book that actually materialised. Neither alone is sufficient: testnet lies about liquidity; shadow lies about fills. Together they bracket the truth, and a tiny-size pilot closes the remaining gap (see the maturity ladder in [[trading-system-deployment]]).

## A/B Champion–Challenger

Once a strategy is live, forward testing does not stop — it becomes continuous via champion–challenger.

- **Champion** — the strategy currently allocated real capital.
- **Challenger(s)** — new variants or re-tuned parameters, run in shadow (or at tiny size) *alongside* the champion on the same live data, same period, same regime.
- **Promotion rule.** A challenger replaces the champion only after out-performing it on live, forward data over a pre-committed window and trade count — never on backtest alone. This structurally prevents the [[hypothesis-to-backtest-workflow#Stage 7|OOS-contamination]] trap, because the comparison happens on data that did not exist when either variant was built.

Champion–challenger also gives an honest, ongoing estimate of edge decay: if every challenger keeps beating the champion, the champion is decaying; if none can, the champion is robust. Run the comparison in the *same regime* (see [[regime-conditional-validation]]) so a challenger is not credited for merely catching a friendlier market.

## Reconciling Live vs Backtest — the Four Perp Metrics

The core work of crypto forward testing is a line-by-line reconciliation of what the backtest assumed against what live/shadow actually produced. For a perp bot, four metrics dominate.

### 1. Funding accrual

- **Backtest assumption.** Funding modelled per cycle, often coarsely (8-hour CEX convention, or ignored).
- **Live reality.** Hyperliquid charges funding **every hour** at `position_size × oracle_price × funding_rate`, capped at 4%/hour, debited from margin. A position held across many hours accrues funding far faster than an 8-hour model implies.
- **Reconcile.** Compare cumulative *realised* funding paid/received in shadow against the backtest's modelled funding for the identical position path. A persistent gap means the funding model is wrong — and for a carry-dependent strategy, funding *is* the PnL, so the whole edge estimate is off. Re-check against the post-October-2025 compression regime, where carry shrank several-fold.

### 2. Depth-aware slippage

- **Backtest assumption.** Fixed-% slippage, or midpoint fills.
- **Live reality.** Slippage is depth-dependent: a market order walks the book level by level, and on thin alt perps in stress it can be multiples of a fixed assumption. See [[slippage-modeling]].
- **Reconcile.** For each shadow order, compute the fill VWAP the live book *would* have given (walk the real L2 snapshot) and compare to the backtest's assumed fill. Where they diverge is where the strategy's tail cost lives. If live slippage systematically exceeds the model, the net edge is smaller than backtested — often the difference between viable and not.

### 3. Partial-fill rate

- **Backtest assumption.** Orders fill fully, instantly.
- **Live reality.** Limit orders sit in a queue and may fill partially or not at all; maker-fill assumptions may be fantasy. A strategy that assumed it earned maker rebates may in fact be crossing the spread as a taker.
- **Reconcile.** Track intended vs actual fill quantity and maker/taker classification in shadow. A low partial-fill rate on limit orders, or frequent taker fills where the backtest assumed maker, means the [[execution-model-differences|execution model]] is optimistic. Re-run the backtest under taker-only fees to bound the damage.

### 4. ADL exposure

- **Backtest assumption.** A winning position is held to the modelled exit.
- **Live reality.** During cascades the [[auto-deleveraging|ADL]] engine force-closes *profitable* counterparties. On 10 October 2025, Hyperliquid auto-deleveraged roughly $2.1B of winning PnL in ~12 minutes; delta-neutral traders had only their Hyperliquid leg closed, leaving them suddenly directional. A backtest that never models ADL overstates returns exactly when the market is most violent.
- **Reconcile.** Forward testing cannot easily *trigger* ADL on demand, so this is validated by (a) monitoring your position's ADL-queue ranking live and confirming the bot reacts, and (b) injecting a synthetic ADL on the most profitable position in stress replay (the playbook in [[crypto-perp-backtesting-pitfalls]]) and confirming the live risk logic would survive the forced close at bankruptcy price.

## The Reconciliation Scorecard

Run the strategy forward for a committed window and score each metric backtest-vs-live before promoting to size:

| Metric | Backtest expectation | Live / shadow result | Pass condition |
|--------|---------------------|----------------------|----------------|
| Funding accrual | Modelled per-position funding | Realised hourly funding | Within tolerance over full path |
| Slippage | Assumed fill price | Book-walked fill VWAP | Live ≤ modelled (or model widened) |
| Partial-fill rate | Full fills, maker | Actual fill %, maker/taker | Fill rate and fee class match |
| Turnover / signal freq | Backtest count | Live signal count | No signal inflation/dropout |
| Drawdown | Backtest max DD | Live DD to date | No regime-driven surprise |
| ADL exposure | (usually unmodelled) | Queue rank / synthetic ADL | Survives forced close |

Any metric that fails sends the strategy back to the backtest with the corrected assumption, not forward to capital. A strategy that reconciles cleanly across a full forward window — including at least one stressful stretch — is what "ready for pilot size" actually means.

## Where Forward Testing Sits

Forward testing is Stage 12–13 of [[hypothesis-to-backtest-workflow]] made crypto-specific, and the bridge into the [[trading-system-deployment#Deployment Maturity Ladder|deployment maturity ladder]]:

```
Validated backtest → Testnet (plumbing) → Live-info shadow (reconcile)
     → Champion–challenger (continuous) → Pilot size → Scaled live
```

Skipping it is the classic way a strategy that looked great in backtest becomes a losing live system — funding bled faster, slippage ate the edge, maker fills never came, and a cascade ADL'd the winning leg. Forward testing prices all four *before* they cost real money.

## Getting the Data (CryptoDataAPI)

Forward testing reconciles a live/shadow run against the same data shapes used to build the backtest. CryptoDataAPI supplies the mainnet feeds a live-info shadow consumes:

- **Live book & marks** — `GET /api/v1/hyperliquid/l2-book?coin=BTC` (L2 snapshot for book-walked slippage), `GET /api/v1/hyperliquid/prices` (mids), `GET /api/v1/hyperliquid/summary?coin=BTC`
- **Live funding & OI** — `GET /api/v1/hyperliquid/funding-rates?coin=BTC&limit=100` and `GET /api/v1/hyperliquid/open-interest` to reconcile realised funding accrual
- **Liquidation context** — `GET /api/v1/market-intelligence/liquidations` and `GET /api/v1/liquidity/oi-divergence` to flag cascade/ADL-risk windows during a shadow run
- **Backtest-side baseline** — `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` and `GET /api/v1/backtesting/funding` for the modelled expectation the live result is scored against

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/l2-book?coin=BTC"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-hyperliquid]].

## Related

- [[hyperliquid-backtesting]] — the backtest whose assumptions forward testing reconciles
- [[trading-system-deployment]] — the deployment ladder forward testing feeds into
- [[crypto-perp-backtesting-pitfalls]] — the perp mechanics (funding, ADL, slippage) being validated
- [[funding-rate]] — hourly funding accrual reconciliation
- [[slippage-modeling]] — depth-aware slippage reconciliation
- [[auto-deleveraging]] — ADL exposure on the winning side
- [[execution-model-differences]] — maker/taker and partial-fill reality
- [[transaction-cost-modeling]] — the cost framework live capture compares against
- [[regime-conditional-validation]] — running champion–challenger within one regime
- [[hypothesis-to-backtest-workflow]] — the paper/pilot stages this specialises
- [[cryptodataapi-hyperliquid]] — the live mainnet feeds a shadow run consumes
