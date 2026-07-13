---
title: "TWAP (Time-Weighted Average Price)"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [market-microstructure, algorithmic, execution, indicators]
aliases: ["TWAP", "Time-Weighted Average Price", "twap"]
related: ["[[vwap]]", "[[execution-algorithms]]", "[[implementation-shortfall]]", "[[market-impact]]", "[[slippage]]", "[[transaction-costs]]", "[[best-execution]]", "[[order-types]]"]
domain: [market-microstructure]
prerequisites: ["[[market-impact]]", "[[order-types]]"]
difficulty: intermediate
---

TWAP (Time-Weighted Average Price) is both a benchmark price and the [[execution-algorithms|execution algorithm]] that targets it: the average of an asset's price sampled at uniform time intervals over a window, ignoring volume. As an algorithm, TWAP slices a large parent order into equal-sized child orders released at regular intervals so the average fill price tracks the simple time average of market prices over the execution horizon.

## How It Works

The TWAP benchmark over a window is just the arithmetic mean of prices sampled at fixed time steps:

```
TWAP = (1/N) · Σ P(t_i)   for i = 1..N, with t_i evenly spaced
```

The TWAP *algorithm* turns this into an execution schedule. To buy Q units over a window of duration T split into N slices:

```
slice_size  = Q / N
slice_clock = T / N          # release one child order every T/N
# at each tick: send child order of slice_size (often via limit or
# small marketable order), optionally randomising size/timing to
# reduce predictability
```

Unlike [[vwap|VWAP]], which front-loads or back-loads child orders to match the day's historical volume curve (heavy at the open and close), TWAP trades the **same amount in every time bucket** regardless of how much the market itself is trading. This makes it volume-blind: simple, deterministic, and easy to reason about, but it can trade too aggressively during thin periods and too passively during liquid ones.

## Trading Relevance

- **When traders choose TWAP over VWAP.** TWAP is preferred when historical volume profiles are unreliable or absent — newly listed names, illiquid securities, crypto pairs without a stable intraday volume shape, or when the trader wants a constant, predictable footprint. It is also used to deliberately avoid the open/close volume spikes that VWAP leans into.
- **Reducing [[market-impact]] and [[slippage]].** By spreading the order evenly, TWAP avoids the price impact of a single large [[order-types|market order]] and limits information leakage about total order size. The trade-off is exposure to adverse price drift over the (often longer) execution window — the core tension formalised by [[implementation-shortfall|implementation shortfall]] and Almgren-Chriss.
- **Crypto and DeFi.** TWAP is ubiquitous in crypto: centralised-exchange execution desks use it, and on-chain it appears as TWAP oracles (e.g. Uniswap v3's time-weighted price accumulator) used to resist short-term price manipulation, and as the basis for on-chain TWAP order protocols.
- **Predictability is a double-edged sword.** A naive, perfectly periodic TWAP is easy for other participants and [[high-frequency-trading|HFT]] systems to detect and front-run; production TWAP implementations randomise slice size and timing to obscure the schedule.
- **Benchmark for [[best-execution|TCA]].** Like VWAP, achieved-price-vs-TWAP is a standard transaction-cost-analysis benchmark, especially for orders worked evenly across a fixed window.

## Advantages and Disadvantages

- **Advantages:** simple, deterministic, no dependence on a volume forecast, works in low-data or illiquid markets, easy to audit.
- **Disadvantages:** ignores real-time liquidity, can over-trade thin periods, predictable if not randomised, and carries timing risk over long windows (price can drift away during execution).

## Related

- [[vwap]] — the volume-weighted counterpart benchmark and algorithm
- [[execution-algorithms]] — broader family (TWAP, VWAP, IS, POV, iceberg)
- [[implementation-shortfall]] — execution framework that balances impact vs timing risk
- [[market-impact]] — the cost TWAP is designed to reduce
- [[slippage]] — price movement during execution
- [[transaction-costs]] — total cost of trading
- [[best-execution]] — regulatory and TCA context
- [[order-types]] — the child-order primitives TWAP uses

## Sources

- (Source: [[book-algorithmic-and-high-frequency-trading]]) — Cartea, Jaimungal & Penalva on execution algorithms and the impact/timing trade-off
- (Source: [[book-trading-and-exchanges]]) — Harris on execution benchmarks and order-working strategies
