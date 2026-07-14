<!-- Source: user-provided briefing (conversational ingest), 2026-06-14 -->
<!-- Topic: overfitting in backtesting — general techniques + Hyperliquid-specific anti-overfit methods -->
<!-- Provenance: user pasted briefing material; Hyperliquid claims cite official Hyperliquid docs (URLs below). -->

# Overfitting in Backtesting — General + Hyperliquid-Specific (user briefing, 2026-06-14)

This is the raw briefing material supplied by the user for the gap-analysis run that produced
`wiki/concepts/backtesting/in-sample-vs-out-of-sample.md` and
`wiki/concepts/backtesting/hyperliquid-backtesting.md`.

## Part A — Strict chronological split vs walk-forward

- **Strict chronological split**: a one-time separation of history into development and testing blocks
  (e.g. Jan–Jun train, Jul–Sep validation, Oct–Dec final out-of-sample). Answers "did the strategy work on
  one clean unseen future block?" Simple, but gives only one final test window.
- **Walk-forward testing**: repeated rolling train→test (train Jan–Mar / test Apr; train Feb–Apr / test May; …).
  Answers "would this keep working if I had been re-optimizing over time?" Many OOS windows instead of one.
- Key difference: chronological split tests one fixed strategy on one future block; walk-forward simulates
  repeated real-world redeployment.
- Recommended workflow: **research split → validation split → walk-forward robustness test → final untouched holdout.**
  Keep a final holdout that was NOT used to design the walk-forward process itself.

## Part B — What overfitting is

A strategy that looks excellent on history because it learned noise/quirks of that dataset, not a repeatable edge.
Common causes: too many parameters, excessive testing (keeping the best of thousands), curve fitting, small sample,
ignoring costs, data leakage, survivorship bias. Signs: smooth equity curve, extreme Sharpe, hyper-specific
parameters, weak logic. In-sample vs out-of-sample gap is the canonical tell.

## Part C — Hyperliquid-specific anti-overfit techniques (15)

1. Strict chronological splits (train / validation / final out-of-sample).
2. Walk-forward testing (rolling windows) — funding/liquidity/OI/vol change fast on HL.
3. Purge and embargo overlapping data (lookback + multi-hour holds cause train/test overlap).
4. Test across assets, not only time (BTC/ETH vs large alts vs small perps vs newly listed).
5. Model HL funding correctly — funding paid **every hour**, added/subtracted at the funding interval,
   based on `position_size * oracle_price * funding_rate` (NOT mark price). Use only known-at-the-time funding.
6. Include realistic fees — HL fees depend on rolling 14-day volume, assessed daily UTC; perps and spot have
   separate schedules; spot volume counts double toward fee-tier volume. Don't assume best tier.
7. Backtest on order book data, not only candles — HL `l2Book` returns up to 20 levels/side; L2 snapshots
   are in the `hyperliquid-archive` S3 bucket (approximate, may be missing).
8. Don't let the strategy trade inside the same candle (no same-bar lookahead).
9. Parameter stability tests — want a plateau, not a spike.
10. Penalize multiple testing — track every variation; use the Deflated Sharpe Ratio.
11. Simulate margin and liquidation rules — HL uses USDC margining with USDT-denominated linear contracts
    for most assets; cross or isolated margin at the wallet level.
12. Stress test execution assumptions (double slippage, taker-only, 1–5s latency, half depth, worse funding/fees,
    no-fill on some limits).
13. Separate entry logic from risk parameters — fix risk rules first, then test if the entry adds value.
14. Use regime-based holdouts (high/negative funding, high OI, low liquidity, trending vs choppy). HL perpetual
    asset-context endpoint exposes mark price, funding, OI, premium, oracle price, day notional volume.
15. Keep an untouched "live shadow" test — run live with tiny/no size and compare fill rate, slippage, funding,
    turnover, drawdown, signal frequency vs backtest.

Practical checklist: profitable after fees+funding+slippage; survives 1.5–2x worse costs; works OOS; works across
windows; works across >1 asset (or has a reason not to); parameter plateau; no same-candle lookahead; hourly funding;
margin/liquidation simulated; limit orders include partial/no-fill risk; not driven by one trade/day/coin;
final holdout tested once.

## Cited Hyperliquid documentation

- Funding: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/funding
- Fees: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees
- Info endpoint (l2Book): https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint
- Historical data (hyperliquid-archive S3): https://hyperliquid.gitbook.io/hyperliquid-docs/historical-data
- Contract specifications (margin): https://hyperliquid.gitbook.io/hyperliquid-docs/trading/contract-specifications
- Perpetuals asset context: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint/perpetuals
- Deflated Sharpe Ratio (Bailey & López de Prado): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
