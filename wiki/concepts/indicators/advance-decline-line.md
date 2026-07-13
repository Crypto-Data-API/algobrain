---
title: "Advance/Decline Line"
type: concept
created: 2026-07-01
updated: 2026-07-13
status: review
tags: [indicators, technical-analysis, market-internals, market-breadth]
aliases: ["Advance-Decline Line", "A/D Line", "AD Line", "Advance/Decline Line", "Breadth Line"]
related: ["[[market-breadth]]", "[[divergence]]", "[[mcclellan-oscillator]]", "[[arms-index]]", "[[breadth-thrust]]", "[[momentum-breadth]]", "[[trading-volume]]", "[[relative-strength]]", "[[trend]]", "[[cryptodataapi]]"]
domain: [indicators]
prerequisites: ["[[market-breadth]]", "[[trend]]"]
difficulty: beginner
---

The **advance/decline line** (A/D line) is the foundational [[market-breadth|market-breadth]] indicator: a cumulative running total of the number of advancing stocks minus declining stocks each day. Because it counts *participation* — how many stocks are rising — rather than price, it reveals whether a move in a cap-weighted index reflects broad strength or is being carried by a handful of large names. A rising A/D line confirms a healthy uptrend; an A/D line that fails to keep up with new index highs is one of the most-watched early warnings of a weakening market.

## Overview

The A/D line is built from daily "market internals" — the count of issues (stocks) that closed up versus down on an exchange such as the NYSE. The calculation is deliberately simple:

```
Net Advances_t = Advancing issues − Declining issues   (for day t)
A/D Line_t      = A/D Line_{t−1} + Net Advances_t        (cumulative)
```

Each day's net advances are added to the previous day's running total, producing a continuously cumulating line. Its absolute level is arbitrary (it depends on the start date); what matters is its **direction and slope**, and especially whether it **confirms or diverges from** the underlying index. Because it weights every stock equally — a $5 billion company counts the same as a $2 trillion one — it captures the breadth that a cap-weighted index price can hide.

## Why It Matters

1. **It measures the health beneath the index.** Major indices are dominated by their largest constituents. A handful of mega-caps can lift the index to new highs while the *typical* stock is falling. The A/D line exposes that narrowness.
2. **Divergences precede tops.** The canonical bearish signal is a [[divergence]]: the index makes a new high but the A/D line does not. Historically this "non-confirmation" has appeared months before several major market tops (e.g., the late-1990s and 2007 peaks), as leadership narrowed to fewer names.
3. **Confirmation builds conviction.** When the index and the A/D line make new highs together, the advance is broad and structurally healthier, giving trend-followers more confidence to stay long.
4. **It is a context tool, not a trigger.** Breadth deterioration can persist for a long time before price turns, so the A/D line is used as a *risk/context* overlay rather than a precise timing signal.

## How It Is Used

- **Trend confirmation:** check that the A/D line is making new highs alongside the index; agreement supports the trend.
- **Divergence spotting:** watch for the index pushing to new highs while the A/D line rolls over — a warning to tighten risk or reduce exposure.
- **Bottom hunting:** a deeply negative, washed-out A/D line that begins to turn up can help identify capitulation lows, often alongside the [[arms-index|TRIN]] and [[mcclellan-oscillator|McClellan Oscillator]].
- **Universe choice matters:** the NYSE A/D line includes many interest-rate-sensitive closed-end funds and ETFs, which can distort it; analysts often prefer a common-stock-only version to get a cleaner read on equity breadth.

The A/D line is typically used together with related breadth measures — the [[mcclellan-oscillator|McClellan Oscillator]] (breadth momentum), the [[arms-index|Arms Index/TRIN]] (volume-weighted breadth), [[new-highs-new-lows|new highs vs new lows]], and the [[breadth-thrust|breadth thrust]] — rather than in isolation.

## Hypothetical Example

Take a simplified 1,000-stock index over three sessions:

| Session | Index level | Advancers | Decliners | Net (A−D) | A/D Line (cumulative) |
|---|---|---|---|---|---|
| 1 | 4,000 (start) | 600 | 400 | +200 | +200 |
| 2 | 4,040 (new high) | 540 | 460 | +80 | +280 |
| 3 | 4,070 (new high) | 460 | 540 | −60 | +220 |

By session 3 the **index is at a fresh high (4,070)**, yet the **A/D line has turned down** (from +280 to +220) because decliners now outnumber advancers — the rally is being driven by a shrinking group of (likely large-cap) names while the average stock is falling. This price-vs-breadth **[[divergence]]** is the classic bearish non-confirmation: the "generals" advance while the "soldiers" retreat. (Illustrative numbers only — not real market data.)

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-health/summary` — dual health scores + sentiment
- `GET /api/v1/market-health/altcoin-breadth` — % of coins above N-day MA (default 200)

**Historical data:**
- `GET /api/v1/market-health/history?days=730` — historical health scores

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-health/altcoin-breadth"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-health]].

## Related

- [[market-breadth]] — the broader family of breadth measures the A/D line anchors
- [[divergence]] — the primary A/D-line signal (price vs participation)
- [[mcclellan-oscillator]] — breadth momentum derived from net advances
- [[arms-index]] — volume-weighted breadth complement
- [[breadth-thrust]] — the bullish regime-shift breadth signal
- [[new-highs-new-lows]] — companion breadth measure
- [[momentum-breadth]] — breadth combined with price momentum
- [[trading-volume]] — up/down volume version of breadth
- [[relative-strength]] — per-stock leadership that aggregates into breadth
- [[trend]] — the A/D line confirms or warns of trend health

## Sources

- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — market-internals and breadth chapter.
- Gregory L. Morris, *The Complete Guide to Market Breadth Indicators* (McGraw-Hill, 2005) — catalog of breadth measures including the A/D line.
- General technical-analysis knowledge — the A/D line formula, worked example, and divergence interpretation are standard, widely-taught material.
