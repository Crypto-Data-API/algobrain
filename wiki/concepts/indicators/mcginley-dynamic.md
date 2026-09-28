---
title: "McGinley Dynamic"
type: concept
created: 2026-09-28
updated: 2026-09-28
status: draft
tags: [indicators, technical-analysis, trend-following, crypto]
aliases: ["McGinley Dynamic Indicator", "MD", "McGinley MA"]
related: ["[[moving-averages]]", "[[adaptive-moving-averages]]", "[[exponential-moving-average]]", "[[kama]]", "[[frama]]", "[[vidya]]", "[[hull-moving-average]]", "[[nnfx-method]]", "[[nnfx-crypto-daily-system]]", "[[stonehill-forex-nnfx]]"]
domain: [technical-analysis]
prerequisites: ["[[moving-averages]]", "[[exponential-moving-average]]"]
difficulty: intermediate
---

The **McGinley Dynamic** is a self-adjusting moving average introduced by John R. McGinley (a Chartered Market Technician and former editor of the MTA's *Journal of Technical Analysis*) in 1997. Instead of a fixed smoothing constant, it scales its effective speed by the **ratio of price to the indicator's own previous value**, so it accelerates to catch sharp moves and resists whipsaw in drifting markets. In the [[nnfx-method|NNFX]] framework it is a popular **baseline**, which [[stonehill-forex|Stonehill Forex]] describes as "underrated" yet among the most reliable (Source: [[stonehill-forex-nnfx]]).

## Construction

```
MD[t] = MD[t-1] + (Close[t] - MD[t-1]) / ( k * N * (Close[t] / MD[t-1])^4 )
```

- `N` — nominal period (Stonehill default 12; 10–20 common). McGinley suggested using about 60% of the equivalent SMA length.
- `k` — constant, typically 0.6 (some implementations fold it into `N` or use 1.0).
- Seed `MD` with the first close or a short SMA.

The fourth-power term is the adaptive part. When price runs **below** the line, `Close/MD < 1`, the denominator shrinks and the line moves *faster* — McGinley designed it to track falling markets quickly. When price is **above** the line, the denominator grows and the line slows, which dampens overshoot in rallies. The asymmetry is by design.

## How to read it

- **Direction**: close above MD = long bias; below = short bias. A close across the line is the baseline signal.
- **Distance**: `|Close - MD| / ATR` measures stretch; NNFX refuses entries beyond 1 x [[atr|ATR]].
- **Slope** is secondary; MD is used mainly as a side-of-line filter.

## NNFX role

**Baseline.** It gates trade direction, triggers baseline-cross entries, defines the 1 x ATR entry band, and a close back across it exits the runner. Its lower whipsaw rate relative to an EMA of similar lag is what makes it attractive in this slot (Source: [[stonehill-forex-nnfx]]).

## Crypto notes

- The fourth-power ratio assumes moves of a few percent per bar; in crypto, 10–20% daily bars make `(Close/MD)^4` swing much more (e.g. `1.2^4 = 2.07`), so the down/up asymmetry is far stronger than in FX. Expect the line to snap down hard in crashes and lag noticeably in vertical rallies — test longer `N` for long-side use.
- Compute on the 00:00 UTC daily close; weekend bars included.
- Treat any claimed superiority over [[kama]] or [[hull-moving-average]] as untested for crypto.

## Limitations

- The asymmetry is a design opinion, not an empirical finding; it biases the baseline toward flipping short faster than long.
- No volatility input — it cannot tell a quiet drift from a violent one of equal ratio.
- Implementations differ (`k`, seeding, `N` scaling), so "McGinley 14" is not portable between platforms without checking.

## Getting the Data (CryptoDataAPI)

**Live data:** `GET /api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500` — daily closes for the recursion; `GET /api/v1/volatility/regime/{symbol}` — volatility state the MD cannot see.
**Historical data:** `GET /api/v1/backtesting/klines` — multi-year archive to measure baseline-cross whipsaw rate versus an EMA.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=BTCUSDT&interval=1d&limit=500"
```

Catalogs: [[cryptodataapi-market-data]], [[cryptodataapi-backtesting]].

### AI agent workflow

Via the [[cryptodataapi-mcp|CryptoDataAPI MCP]]:

- **Benchmark whipsaw** — on `/api/v1/backtesting/klines` daily bars, count baseline crosses that reverse within 3 bars for MD(12/14/20) versus an EMA with matched average lag; keep MD only if it cuts whipsaws net of lag.
- **Measure the asymmetry** — compare MD's lag after +20% versus −20% daily moves on BTC and SOL; decide per side whether a longer `N` is needed.
- **Pair with the regime gate** — suppress baseline-cross entries when `/api/v1/volatility/regime/{symbol}` reports a shock state.

## Related

- [[nnfx-method]] · [[nnfx-crypto-daily-system]] — uses MD as baseline
- [[adaptive-moving-averages]] · [[kama]] · [[frama]] · [[vidya]] · [[hull-moving-average]] · [[alma]] · [[jurik-moving-average]] — alternative baselines
- [[moving-averages]] · [[exponential-moving-average]] · [[atr]]

## Sources

- [[stonehill-forex-nnfx]] — Stonehill Forex, "McGinley Dynamic Indicator as a Baseline Indicator" (2022) and indicator library, fetched 2026-09-28
- McGinley, John R. (1997), *Journal of Technical Analysis* — original publication (cited via Stonehill; not reviewed directly)
