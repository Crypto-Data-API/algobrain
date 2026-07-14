---
title: "Paper-to-Live Promotion"
type: concept
created: 2026-07-14
updated: 2026-07-14
status: good
tags: [ai-trading, algorithmic, backtesting, risk-management, deployment, crypto]
aliases: ["Promotion Ladder", "Canary Deployment", "Backtest to Live", "Going Live Gates"]
domain: [risk-management, market-microstructure]
prerequisites: ["[[backtesting]]", "[[paper-trading]]", "[[deployment]]"]
difficulty: advanced
related:
  - "[[deployment]]"
  - "[[bot-architecture]]"
  - "[[bot-risks-and-pitfalls]]"
  - "[[bot-kill-switch-design]]"
  - "[[position-reconciliation]]"
  - "[[when-to-retire-a-strategy]]"
  - "[[backtesting]]"
  - "[[paper-trading]]"
  - "[[deflated-sharpe-ratio]]"
  - "[[walk-forward-optimization]]"
---

# Paper-to-Live Promotion

Paper-to-live promotion is the disciplined, gated progression of a crypto strategy from **backtest → testnet/paper → small-live (canary) → scaled-live**, where each rung has explicit numerical go/no-go criteria and a strategy is only promoted when it *proves* the assumptions the previous rung could not test. It is the operational answer to the [[deployment|backtest-to-live gap]]: most strategies that die in production do so because they were promoted on hope rather than evidence, skipping the rung that would have caught the failure cheaply.

> This page is the promotion *protocol*. For the engineering of where a bot runs, see [[deployment]] and [[cloud-trading-infrastructure]]; for what breaks in production, [[bot-risks-and-pitfalls]]; for the halt mechanism referenced in every gate below, [[bot-kill-switch-design]].

## Why a ladder, not a switch

Each rung tests something the previous one structurally cannot:

| Rung | What it can prove | What it *cannot* prove |
|---|---|---|
| Backtest | The signal had statistical edge on history, net of modeled costs | That your live code produces the same signal; real slippage; latency; venue behavior |
| Testnet / paper | The *plumbing* is correct — order lifecycle, reconciliation, restart, kill switch | Real fills (testnet liquidity is fake); real funding/fees; adverse selection |
| Canary (small-live) | Real execution economics at trivial risk — slippage, fill rate, funding accrual, MEV | Behavior at size (market impact, capacity, crowding) |
| Scaled-live | Capacity and impact at target notional | (this is the destination) |

Promoting past a rung imports every un-proven assumption at full risk. The ladder converts one large, correlated bet into a sequence of small, independent, cheap-to-fail bets.

## Rung 0 → 1: Backtest gate

Do not promote a backtest to *any* capital, real or paper, until it clears the research gates. A strategy page's `backtest_status` should read at least `cost-corrected` and ideally `deflated-sharpe-significant` before this rung.

**Go criteria (all required):**

- **Cost-corrected, not naive.** The backtest models realistic taker/maker fees, spread, gas/priority-fee (for on-chain legs), funding, and slippage sized to order-book depth — not close-price fills. A naive backtest is not evidence (see [[bot-risks-and-pitfalls]]).
- **Walk-forward validated.** Out-of-sample performance via [[walk-forward-optimization]], not a single in-sample fit.
- **Deflated Sharpe significant.** After correcting for the number of trials tried, the [[deflated-sharpe-ratio]] remains > 0 with the intended confidence — guards against selection under multiple testing.
- **Sane capacity and crowding.** `capacity_usd` and `crowding_risk` are estimated, and the target canary size is orders of magnitude below capacity.
- **A written kill spec.** Numerical `kill_criteria` exist *before* any capital, not after the first loss.

**No-go:** any of the above missing, or the edge depends on a data window that cannot be reproduced live (look-ahead, survivorship, unavailable-in-realtime features).

## Rung 1 → 2: Testnet / paper gate

Run the **exact live code path** against the live market — same feature pipeline, same order router, same reconciliation loop — with simulated or testnet capital. Crypto specifics:

- **Testnet validates plumbing, not economics.** Binance Spot/Futures Testnet, Bybit Testnet, and dYdX/Hyperliquid testnets have thin, synthetic liquidity and free "gas". A profitable testnet result is *meaningless* as a P&L signal; its only job is to prove the order lifecycle, signing, WebSocket handling, and restart logic work. For economic realism, prefer **paper trading against live mainnet data** (real book, real funding, fills simulated conservatively).
- **Run long enough to hit the edge cases.** At least one full weekend (thin liquidity), one funding cycle if perps are involved, and one deliberate fault injection.

**Go criteria (all required):**

- Order lifecycle correct end-to-end: submit → ack → partial fill → fill/cancel → position update, with **idempotent client order IDs** so a retry never double-sends.
- **Reconciliation clean:** internal state matches venue truth across a forced restart and a simulated WebSocket gap (see [[position-reconciliation]]).
- **Kill switch fires** on every configured trigger in a drill (drawdown, staleness, latency) and unwinds reduce-only (see [[bot-kill-switch-design]]).
- No crash, memory leak, or unhandled exception over the observation window (≥ 3–7 days of continuous run).
- Feature parity check: live-computed signals match the research pipeline on the same timestamps within numerical tolerance (catches look-ahead leakage that only surfaces in real-time arrival).

**No-go:** any reconciliation break, any double-order, any silent crash, or live/research signal divergence beyond tolerance.

## Rung 2 → 3: Canary (small-live) gate

The canary is real capital at deliberately trivial size — the first and only rung that can measure real execution economics (slippage, fill rate, funding accrual, fee drag, MEV/adverse selection). This is where most "profitable-on-paper" strategies quietly reveal negative net edge.

### Canary sizing

Start at the **smaller of** `min_capital_usd` from the strategy spec **or** 1–5% of the eventual target allocation — whatever is small enough that a total loss is an acceptable tuition payment. Concretely, a strategy targeting a $200k sleeve might canary at $2k–$5k. Size the canary so that:

- A single worst-case adverse move (from `expected_max_drawdown` × leverage) is a rounding error on the book.
- Fixed costs (gas, minimum fees) do **not** dominate — on Ethereum L1 a $200 canary is uninformative because gas swamps everything; either canary larger or canary on the cheap L2/venue you will actually trade.

### Go criteria (all required, measured over a pre-committed sample)

- **Sample size:** at least N ≥ 30–50 live round-trips (or enough funding periods) so the estimate is not noise. Pre-commit N; do not stop early on a good streak.
- **Slippage realized ≤ modeled** (or the model is updated and the backtest re-passes with the worse number).
- **Fill rate / inclusion rate ≥ threshold** appropriate to the strategy (for MEV, bundle inclusion; for limit-maker strategies, fill ratio).
- **Realized edge within the confidence interval of expected edge.** Compare live per-trade P&L distribution to the backtest's; a rough KS-test or a simple "live mean within ±1.5σ of backtest mean" gate. If live is materially below, the edge did not survive costs.
- **Zero unexplained P&L.** Every dollar reconciles to fills, funding, and fees (see [[position-reconciliation]]). Unexplained drift is a bug or a leak, not alpha.
- **Drawdown within bound** and kill switch never tripped by a real (non-drill) event during the window.

**No-go:** live net edge indistinguishable from zero (or negative) after costs; slippage/latency materially worse than modeled; any reconciliation gap; any unexplained loss.

## Rung 3: Scale (ramp) gate

Once the canary proves positive net edge, scale in **steps**, not in one jump. A typical ramp doubles size per step (e.g., $5k → $10k → $25k → …), and each step must re-clear a lightweight version of the canary gate at the new size before the next step.

**What you are now testing:** capacity and market impact. Monitor at each step:

- **Slippage as a function of size** — the first sign of capacity limits is slippage growing super-linearly with notional.
- **Realized edge decay** — if per-unit edge falls as size rises, you are approaching `capacity_usd`; stop one step below where net edge times size peaks.
- **Crowding** — if the same opportunity starts filling worse or vanishing, competitors are on the same signal.

**Halt the ramp** (do not necessarily kill) whenever a step fails its gate; hold at the last good size and investigate.

## Promotion scorecard (pseudocode)

```python
# promotion_gate.py — evaluate whether a strategy may advance one rung
from dataclasses import dataclass

@dataclass
class RungReport:
    rung: str                 # "backtest" | "paper" | "canary" | "scale"
    sample_size: int
    live_edge_bps: float      # realized net edge per trade
    expected_edge_bps: float  # from backtest, cost-corrected
    edge_ci_bps: float        # 1.5-sigma band on expected
    slippage_realized_bps: float
    slippage_modeled_bps: float
    fill_or_inclusion_rate: float
    unexplained_pnl_usd: float
    reconciliation_clean: bool
    kill_switch_drill_passed: bool
    max_drawdown: float
    drawdown_limit: float

def may_promote(r: RungReport, min_sample: int) -> tuple[bool, list[str]]:
    fails = []
    if r.sample_size < min_sample:
        fails.append("insufficient sample — keep observing")
    if not r.reconciliation_clean or abs(r.unexplained_pnl_usd) > 0:
        fails.append("state does not reconcile — likely a bug, not alpha")
    if r.slippage_realized_bps > r.slippage_modeled_bps:
        fails.append("live slippage exceeds model — re-backtest with true costs")
    if r.live_edge_bps < r.expected_edge_bps - r.edge_ci_bps:
        fails.append("edge did not survive live costs")
    if r.max_drawdown > r.drawdown_limit:
        fails.append("drawdown breached limit")
    if r.rung in ("paper",) and not r.kill_switch_drill_passed:
        fails.append("kill switch did not fire in drill")
    return (len(fails) == 0, fails)
```

The rule the pseudocode encodes: **never promote on a good return alone.** A rung is passed only when the return is real *and* explained *and* the machinery that will contain the downside has been proven to work.

## Common failure modes this ladder prevents

- **Skipping the canary** and going straight to size — imports slippage, funding, and MEV assumptions at full risk. The classic "great backtest, immediate live loss."
- **Promoting on a lucky streak** by stopping the canary early — pre-committing N defeats this.
- **Confusing testnet profit with edge** — testnet only proves plumbing.
- **Scaling in one jump** — hides the capacity cliff until you are already over it.
- **No kill spec before capital** — you discover the drawdown limit by blowing through it.

## Trading relevance

Promotion discipline is itself a repeatable edge. Two operators with the *same* strategy diverge sharply in realized P&L based on whether they caught the cost/latency/impact reality at the $5k canary rung or at the $500k scaled rung. The ladder makes the discovery cheap. Every rung's gate is enforced by the [[bot-kill-switch-design|kill switch]] and audited by [[position-reconciliation|reconciliation]] — the three concepts are one system.

## Getting the Data (CryptoDataAPI)

The backtest rung consumes historical data; the canary and scale rungs benefit from a live regime gate so promotion is not attempted into a hostile market.

**Backtest rung (historical):**
- `GET /api/v1/backtesting/klines` — OHLCV archive for the cost-corrected backtest
- `GET /api/v1/backtesting/funding` — historical funding for perp/carry strategies
- `GET /api/v1/backtesting/export` — custom-range export for the research pipeline

**Live rungs (regime gate — avoid promoting into stress):**
- `GET /api/v1/market-health/summary` — current dual-score market health before sizing up
- `GET /api/v1/market-health/history?days=90` — recent regime context for the canary window

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/summary"
```

Auth: `X-API-Key` header. Catalogs: [[cryptodataapi-backtesting]], [[cryptodataapi-market-health]].

## Related

- [[deployment]] — the engineering context this protocol sits inside
- [[bot-architecture]] — the components each rung exercises
- [[bot-risks-and-pitfalls]] — the failures the ladder is designed to catch
- [[bot-kill-switch-design]] — the halt mechanism every gate depends on
- [[position-reconciliation]] — the audit that makes "unexplained P&L" observable
- [[paper-trading]] — the rung-1 tool
- [[backtesting]] / [[walk-forward-optimization]] / [[deflated-sharpe-ratio]] — the rung-0 gates
- [[when-to-retire-a-strategy]] — the inverse process (demotion / kill)

## Sources

- General knowledge of production trading-system promotion practice; synthesized with this wiki's [[deployment]] and [[bot-risks-and-pitfalls]] pages. No raw external source ingested yet.
