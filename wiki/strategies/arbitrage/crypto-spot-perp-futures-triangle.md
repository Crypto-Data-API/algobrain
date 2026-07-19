---
title: "Crypto Spot-Perp-Futures Triangular Arbitrage"
type: strategy
created: 2026-04-25
updated: 2026-07-19
status: good
tags: [arbitrage, crypto, derivatives, futures]
aliases: ["Three-Wrapper Triangle", "Spot-Perp-Future Box"]
related: ["[[funding-rate-arbitrage]]", "[[basis-trading]]", "[[cash-and-carry]]", "[[triangular-arbitrage]]", "[[cryptodataapi]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto, futures]
complexity: advanced
backtest_status: cost-corrected
edge_source: [structural, informational]
edge_mechanism: "Three crypto wrappers (spot, perpetual, dated future) of the same underlying clear on different mechanisms (instant, funding-rate, basis-decay). Mismatched implied yields create a closed triangle when one leg drifts."
data_required: [spot-ohlcv, perp-funding-history, dated-futures-curve, exchange-fee-schedule]
min_capital_usd: 50000
capacity_usd: 1000000000
crowding_risk: medium
expected_sharpe: 1.5
expected_max_drawdown: 0.06
breakeven_cost_bps: 25
decay_evidence: "Spread compression 2021→2024 as cross-venue arb desks normalized funding; remains alive around major events (halving, ETF launches, mass liquidations)."
---

# Crypto Spot-Perp-Futures Triangular Arbitrage

Triangular arbitrage across the three native wrappers of crypto majors: **spot** (immediate delivery), **perpetual swap** (funding-rate-clearing), and **dated futures** (basis-decay-clearing). Each implies a forward yield on the same underlying via a different mechanism; the triangle is closed only when funding × time ≈ basis ≈ borrow-cost-of-spot. Active venues: Binance, Bybit, OKX, Deribit (dated), CME (institutional dated), Hyperliquid (perp).

## Edge Source

**Structural** + **informational** (see [[edge-taxonomy]]). The three wrappers settle through different infrastructure (matching engine vs funding mechanism vs delivery), so dislocations persist for hours-days when one venue's order book is thin or one cohort of traders concentrates in one wrapper.

## Why This Edge Exists

Funding payments occur every 8 hours and converge perp price to spot via mark-to-mark P&L. Dated futures converge via basis decay across the calendar. Spot reflects current supply/demand. When retail flow piles into perps (e.g. post-tariff news pumps), funding spikes to 0.1%+/8h (~110% APR) while dated futures barely move — a triangle opens.

Counterparty: retail directional perp longs vs institutional dated-futures basis sellers vs spot holders.

## Null Hypothesis

Under efficient markets:

```
spot_price ≈ perp_price = future_price * (1 - basis_decay * t)
funding_rate * 1095 ≈ futures_basis_apr ≈ spot_borrow_apr
```

Empirically, the three rates diverge by 5-30% APR for hours to weeks during regime shifts.

## Rules

1. Compute three implied rates: 8-hour funding × 1095 (annualized perp yield); (futures - spot) / spot × 365/days_to_expiry (annualized future yield); spot borrow APR (lending markets like Aave, Compound, or CEX margin).
2. Open the triangle when the spread between any two rates exceeds 25 bp net of fees.
3. Long the cheap leg, short the expensive leg, hedge the third with spot.
4. Hold to next funding-reset for perp leg, to delivery for futures, indefinitely for spot.
5. Roll futures monthly when needed.
6. Position sizing: cap collateral per venue at 25% of book (counterparty risk); cap each leg at ~1% of that instrument's open interest to stay inside funding-rate concavity.

## Implementation Pseudocode

```python
funding_apr = perp_8h_funding * 365 * 3
basis_apr   = (future_price/spot_price - 1) * 365 / days_to_expiry
borrow_apr  = max(cex_margin_rate, defi_lend_rate)

if basis_apr - funding_apr > 25bp:
    sell_dated_future()
    buy_perp()
    # net: collect basis, pay funding
elif funding_apr - basis_apr > 25bp:
    sell_perp()
    buy_dated_future()
    # net: collect funding, pay basis decay
else:
    skip()
```

## Indicators / Data Used

- Coinglass funding-rate history.
- Deribit / CME / Binance Futures term structure.
- Lending rates: Aave, Compound, Bybit margin.
- Open-interest concentration (one-sided OI signals incoming dislocation).

## Example Trade

**March 2021 BTC contango blowout.**

BTC spot $58,000. June 2021 futures (Deribit) $63,500 — basis 9.5% over 3 months → 38% APR. Perp funding 0.04%/8h → 44% APR. Spot lending 5% APR.

Triangle: future yield 38% < perp yield 44%, both >> spot lend 5%. Trade:
- Buy spot BTC $58,000.
- Sell June futures $63,500.
- (Optional second triangle: short perp, long future — net long basis, short funding.)

P&L on basis leg over 3 months: 9.5% gross, ~8.5% net of fees on $1M = $85,000.

## Performance Characteristics

2020-2022: 15-50% APR on basis-perp arb during bull runs; 5-15% during bear. 2023-2024: compressed to 8-15% APR steady-state; spikes to 30%+ around halving, ETF launches, FTX collapse aftermath. Sharpe ~1.5-2.5 net of costs.

## Capacity Limits

Per-venue OI limits and funding-rate concavity. Realistic single-account capacity ~$50-200M; total cross-venue strategy ~$1-5B before market-impact dominates. Hyperliquid HLP demonstrates the institutional ceiling.

## What Kills This Strategy

- Exchange insolvency (FTX November 2022).
- Funding-rate cap changes (Bybit imposed dynamic caps post-2023).
- Liquidation cascades that fail mark-to-market hedges.
- Cross-venue basis blow-out where one leg unfundable.

## Kill Criteria

- Basis-perp spread compresses below 8 bp for 30+ days running.
- Counterparty exchange shows withdrawal restrictions.
- Funding flips negative for 7+ days running on the long leg.

## Advantages

- Three-leg hedge: any two-of-three failure contained.
- High Sharpe in stable regimes.
- Scales to 9-figure capital.

## Disadvantages

- Counterparty risk on each venue.
- Capital-inefficient (collateral on 3 venues).
- Requires 24/7 monitoring (funding resets every 8h).

## Sources

- Coinglass funding-rate dashboard.
- Deribit Insights basis-trade explainers.
- Hyperliquid HLP performance reports.
- BitMEX perpetual-swap contract documentation — the original funding-rate mechanism design (Arthur Hayes et al., launched May 2016).

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding rates (Binance + Hyperliquid)
- `GET /api/v1/derivatives/open-interest?coin=BTC` — cross-exchange open interest
- `GET /api/v1/derivatives/binance/long-short-ratio?symbol=BTCUSDT` — top-trader account long/short ratio
- `GET /api/v1/derivatives/summary?coin=BTC` — all-in-one derivatives overview (markdown format available)

**Historical data:**
- `GET /api/v1/derivatives/binance/funding-rates?symbol=BTCUSDT&limit=500` — funding-rate history
- `GET /api/v1/derivatives/binance/history?days=90` — daily derivatives series (funding, OI, long/short)
- `GET /api/v1/backtesting/funding` — deep funding archive for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-derivatives]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [open interest](https://cryptodataapi.com/open-interest) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can compute two of the triangle's three implied rates and monitor the dislocation:

- **Implied rates** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (annualised perp yield) and `GET /api/v1/derivatives/open-interest?coin=BTC` (one-sided OI signals the incoming dislocation); the dated-future yield comes from native Deribit/CME and the spot-borrow APR from Aave/Compound/CEX margin.
- **Regime gate** — `GET /api/v1/quant/market`: avoid opening the triangle into a `vol_spike` where one leg can become unfundable and mark-to-market hedges fail.
- **Backtest** — `GET /api/v1/backtesting/funding` (funding leg; Hyperliquid hourly since 2023-05, Binance daily since 2026-03-30) + `GET /api/v1/backtesting/klines` for the spot/basis leg.
- **Tip** — cap per-venue collateral (counterparty risk); poll `GET /api/v1/derivatives/summary?coin=BTC` for the single-call positioning snapshot before each 8h funding reset.

## Related

[[funding-rate-arbitrage]] · [[basis-trading]] · [[cash-and-carry]] · [[triangular-arbitrage]] · [[cross-exchange-arbitrage]] · [[liquidation-cascade-arbitrage]]
