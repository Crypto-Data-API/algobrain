---
title: "QuantConnect"
type: entity
created: 2026-04-06
updated: 2026-09-28
status: good
tags: [ai-trading, backtesting, platform, live-trading]
entity_type: company
website: "https://www.quantconnect.com"
related:
  - "[[quantconnect-strategy-library]]"
  - "[[external-strategy-sources]]"
  - "[[backtrader-framework]]"
  - "[[zipline-framework]]"
  - "[[vectorbt]]"
  - "[[walk-forward-optimization]]"
  - "[[backtesting-pitfalls]]"
---

# QuantConnect

**QuantConnect** is a cloud-based algorithmic trading platform that provides backtesting, live trading, and institutional-grade data through its open-source **LEAN** engine. It supports Python and C# across equities, options, futures, crypto, and forex -- the most complete platform for going from backtest to live.

---

## Overview

Founded in 2012 by Jared Broad, QuantConnect provides historical data (10+ years), a cloud IDE, fast backtesting, and brokerage integrations in one place. The LEAN engine is open source and runs locally too. It fills the gap left by Quantopian's closure -- combining cloud compute, data, and live trading where [[zipline-framework|Zipline]] and [[backtrader-framework|Backtrader]] each cover only part of the workflow.

---

## Key Features

| Feature | Detail |
|---|---|
| **LEAN Engine** | Open-source C#/Python backtesting and live engine |
| **Multi-Asset** | Equities, options, futures, crypto, forex |
| **Data** | 10+ years tick/minute/daily data included |
| **Cloud IDE** | Browser-based dev with Jupyter notebooks |
| **Live Trading** | IB, OANDA, Coinbase, Binance, and more |
| **Alpha Streams** | Marketplace to license strategies to institutions |

---

## How to Use

1. **Sign up** at quantconnect.com (free tier available)
2. **Create algorithm**: Cloud IDE (Python/C#) or local LEAN
3. **Define strategy**: `Initialize()` for setup, `OnData()` for logic
4. **Backtest and optimize**: Run on cloud with included data
5. **Go live**: Connect brokerage API and deploy

---

## Pricing

Free tier ($0, limited), Quant Researcher ($8/mo), Team ($20/mo), Institution (custom). Free tier is sufficient for learning and prototyping.

---

## Strengths and Weaknesses

**Strengths**: Most complete retail quant platform -- data, backtest, live trading integrated. Unmatched multi-asset support (options/futures backtesting rare elsewhere). LEAN is open source. Active community with thousands of shared algorithms. Professional [[backtesting-pitfalls|fill simulation]].

**Weaknesses**: Cloud dependency limits speed by tier. Python slower than C# on platform. LEAN API learning curve. Data not exportable. No built-in [[monte-carlo-backtesting|Monte Carlo]]. Alpha Streams has limited institutional traction.

---

## Example

```python
class MomentumAlgorithm(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetCash(100000)
        self.spy = self.AddEquity("SPY", Resolution.Daily).Symbol
        self.sma = self.SMA(self.spy, 200, Resolution.Daily)
    def OnData(self, data):
        if not self.sma.IsReady: return
        if data[self.spy].Close > self.sma.Current.Value:
            self.SetHoldings(self.spy, 1.0)
        else: self.Liquidate(self.spy)
```

---

## Strategy Library as an Idea Source

QuantConnect's free **Investment Strategy Library** (quantconnect.com/learning/articles/investment-strategy-library) is a catalog of roughly 75 short research write-ups, each with a runnable LEAN algorithm you can clone into the cloud IDE. Entries are grouped into Stocks, ETFs, Commodities, Futures & Options, Forex and Multi-Asset; many are ports of academic papers or Quantpedia descriptions. The Quant League competition was folded into a new community "Strategies" section after Q4-2025 (Source: [[quantconnect-strategy-library]]).

For this wiki the library is useful as an **idea source with reference code**, not as evidence. The equity-selection entries are out of scope; the futures, FX, commodity and multi-asset entries are the ones worth harvesting. Pages derived from it so far: [[dual-thrust]], [[dynamic-breakout-ii]], [[copula-pairs-trading]], [[paired-switching]], [[fx-skewness-risk-premia]], [[wti-brent-spread]], [[commodity-momentum-term-structure]]. See [[external-strategy-sources]] for how it compares with other catalogs.

### Licensing

The LEAN engine is open source under the **Apache License 2.0**, which allows commercial use and modification with attribution (Source: [[quantconnect-strategy-library]]). The library's articles and snippets are published on QuantConnect's site rather than in the LEAN repository, so treat them as reference material: re-implement the logic in your own code instead of copying articles wholesale, and credit the article when a strategy is derived from it.

### Translating LEAN Python

LEAN algorithms follow a fixed shape: `initialize()` subscribes to data and registers indicators, `on_data()` (or a scheduled event) runs the decision logic, and `set_holdings()` / `liquidate()` place orders. Translating a library strategy means pulling the decision logic out of that event loop.

**To a local pandas backtest on CryptoDataAPI data:**

1. Swap each `add_equity` / `add_forex` / `add_future` subscription for a crypto analog and pull history from `GET /api/v1/backtesting/klines` (Binance spot OHLCV archive) or the Parquet bulk files via `GET /api/v1/backtesting/archives`; use `GET /api/v1/backtesting/funding` when a perp leg needs carry (see [[cryptodataapi-backtesting]]).
2. Replace LEAN indicators (`self.SMA`, `self.BB`, `self.STD`) with pandas rolling windows, and **shift every signal by one bar** — LEAN's event loop hides the one-bar execution lag that a vectorized frame makes easy to forget ([[lookahead-bias]]).
3. Turn `set_holdings(symbol, w)` into a target-weight column, then compute turnover × cost per bar. Set costs explicitly (taker fee + spread + funding), because the LEAN default charged nothing for crypto.
4. Build the universe from `/backtesting/symbols` plus dated `/backtesting/daily-snapshots/{date}` so delisted coins stay in the test set.
5. For speed on parameter sweeps, port the same frame to [[vectorbt]].

**To Pine Script** ([[pine-script]]): single-instrument, bar-based entries (Dual Thrust, Dynamic Breakout II) translate almost line for line into `strategy.entry` / `strategy.close` with `request.security` for daily ranges on intraday charts. Cross-sectional, multi-asset or model-based logic (copulas, term-structure sorts, universe rotation) does not fit Pine; keep those in Python.

### Pitfalls

- **Stale results** — most published backtests end around 2017-2019 and run on one instrument or a small hand-picked set. Re-run on current data before trusting any number; several entries report negative Sharpe even in-sample (Source: [[quantconnect-strategy-library]]).
- **Zero-fee defaults** — LEAN's `DefaultBrokerageModel` applies a zero-fee `ConstantFeeModel` to Forex, CFD and Crypto, so any library FX or crypto result that did not call `set_brokerage_model(...)` or `set_fee_model(...)` is effectively gross of costs. Spread and slippage models are similarly optimistic unless set ([[transaction-costs]], [[slippage]]).
- **Survivorship in universes** — QuantConnect's own US-equity data includes delisted names, but library strategies frequently hard-code tickers chosen with hindsight (a specific ETF pair, a fixed list of 22 futures, four FX majors). Crypto universes hard-coded from today's top coins inherit the same [[survivorship-bias]].
- **Pending-review entries** — some pages are marked pending review and publish no statistics at all; treat them as untested hypotheses.
- **Paper-to-code drift** — ports of academic papers often simplify the rules (different universe, rebalance, lookback). Check the original paper before attributing the paper's results to the LEAN code.

---

## See Also

- [[backtrader-framework]] -- Local Python backtesting alternative
- [[zipline-framework]] -- Open-source equity backtesting from Quantopian
- [[vectorbt]] -- Fast vectorized backtesting for rapid exploration
- [[walk-forward-optimization]] -- Methodology for robust parameter optimization
- [[backtesting-pitfalls]] -- Avoiding common backtest mistakes
- [[quantconnect-strategy-library]] -- Source summary of the free Strategy Library
- [[external-strategy-sources]] -- Other strategy catalogs worth harvesting

## Sources

- (Source: [[quantconnect-strategy-library]])
