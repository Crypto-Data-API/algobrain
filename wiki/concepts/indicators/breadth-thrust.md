---
title: "Breadth Thrust"
type: concept
created: 2026-07-02
updated: 2026-07-13
status: good
tags: [technical-analysis, indicators, market-regime, momentum]
aliases: ["Breadth Thrust", "breadth-thrust", "Zweig Breadth Thrust", "Breadth Thrust Indicator"]
domain: [indicators, technical-analysis]
prerequisites: ["[[market-breadth]]", "[[exponential-moving-average]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[market-breadth]]"
  - "[[advance-decline-line]]"
  - "[[mcclellan-oscillator]]"
  - "[[momentum-breadth]]"
  - "[[momentum]]"
  - "[[market-regime]]"
  - "[[technical-analysis]]"
  - "[[divergence]]"
---

# Breadth Thrust

A **breadth thrust** is a [[market-breadth]] momentum signal that marks a violent, broad shift from an oversold market to overwhelming buying pressure across a very large share of stocks. Rather than measuring the price of an index, a breadth thrust measures *participation*: when the proportion of advancing stocks explodes from a deeply washed-out level to a near-uniform surge within a short window, it has historically signalled the launch of a durable new bull phase. The best-known formulation is the **Zweig Breadth Thrust**, defined by Martin Zweig in *Winning on Wall Street*.

## Overview

Because major indices are capitalization-weighted, they can rise or fall on the strength of a handful of mega-cap names while most stocks do the opposite (see [[market-breadth]]). Breadth thrusts look for the rare moments when almost *every* stock reverses direction at once — a stampede of broad, indiscriminate buying that tends to occur only off major lows, when fear flips abruptly to greed. The logic is a momentum-of-participation idea: durable bull markets are typically born not from a gentle drift but from a sudden, decisive expansion in the number of stocks advancing. A thrust is therefore treated as a *regime-shift* signal (see [[market-regime]]) rather than a routine entry trigger.

## The Zweig Breadth Thrust

The classic Zweig Breadth Thrust is built on the **advancing-issues ratio** — advancing stocks as a fraction of all stocks that changed price:

```
Breadth Ratio_t   = Advancing issues_t ÷ (Advancing issues_t + Declining issues_t)

Zweig Indicator   = 10-day exponential moving average (EMA) of Breadth Ratio_t
```

A **Zweig Breadth Thrust** fires when this 10-day [[exponential-moving-average|EMA]] rises from **below 0.40 to above 0.615 within 10 trading days**.

The intuition behind the two thresholds:

- **Below 0.40** means the smoothed ratio of advancers has been depressed for a while — a market where declining issues have persistently dominated, i.e. a broadly *oversold* condition.
- **Above 0.615** means advancers have come to overwhelmingly outnumber decliners on a smoothed basis — a broad, high-conviction buying surge.
- **Within 10 trading days** forces the move to be *violent*. A slow grind from 0.40 to 0.615 over many weeks does not qualify; the signal is specifically about the *speed* and breadth of the reversal, which is what makes it rare.

Because the reading is a smoothed EMA of a ratio (not a raw count), the Zweig Breadth Thrust stays comparable across eras even as the number of listed issues has grown, and it is far less noisy than a single day's advance-decline number.

### Worked example (illustrative)

Suppose the 10-day EMA of the advancers ratio has been sitting at **0.38** after a sharp selloff. Over the next two weeks the market reverses hard and most sessions show far more advancers than decliners, pulling the smoothed ratio up day by day: 0.38 → 0.44 → 0.51 → 0.57 → 0.62. Crossing **0.615** on day 9 or 10 — having started below **0.40** — completes a Zweig Breadth Thrust. (Numbers are illustrative of the mechanics, not a specific historical event.)

## Rarity and track record

Genuine breadth thrusts are **uncommon** — the strict speed-and-breadth requirement means the signal can go years without firing. Historically, authentic Zweig-style thrusts have been followed by **strong forward returns and durable uptrends**, which is why they are prized by market timers as one of the more reliable "risk-on" confirmations. Qualitatively, thrusts tend to appear off major bear-market and correction lows, when a broad wave of buying re-engages the whole market at once. Because the specific magnitude of the subsequent advance varies from case to case, this page deliberately avoids quoting precise return figures or dates — the durable, general-knowledge fact is that authentic thrusts are *rare and historically bullish*, not any single reported statistic.

## Related breadth signals

The breadth thrust belongs to a broader family of [[market-breadth]] confirmations. Related and complementary measures include:

- **[[advance-decline-line|Advance-Decline Line]]** — the cumulative running total of (advancers − decliners); a rising A/D line that confirms new index highs signals a healthy, broad trend, and a failure to confirm flags a [[divergence]].
- **Percentage of stocks above their 200-day [[moving-averages|moving average]]** — a slower participation gauge; a surge from a very low reading (few stocks above their long-term average) toward a broad majority is itself a breadth-thrust-like regime shift.
- **[[mcclellan-oscillator|McClellan Oscillator]] and Summation Index** — breadth *momentum* (the difference of 19- and 39-day EMAs of net advances) and its cumulative companion, the [[mcclellan-summation-index|McClellan Summation Index]]; both are used to confirm that a thrust reflects broadening internal strength.
- **[[new-highs-new-lows|New highs vs. new lows]]** — expanding new highs confirm the strength implied by a thrust; a thrust that occurs while new lows still dominate is treated with suspicion.
- **Up/down volume thrusts** — [[up-down-volume|volume-weighted]] participation signals such as the "9-to-1 up day" and back-to-back up-volume thrusts popularized by researcher Wayne Whaley, which look for extreme skew of volume into advancing stocks as an alternative confirmation of a broad buying stampede.

Pairing a breadth thrust with price [[momentum]] turns "how many stocks are participating" into a tradable [[market-regime|regime]] read — see [[momentum-breadth]].

## Why breadth matters

The central value of breadth analysis is that it **distinguishes broad, healthy rallies from narrow, mega-cap-led ones** (see [[market-breadth]]). A breadth thrust is the bullish extreme of this idea: it certifies that a rally has genuinely broad participation rather than being carried by a few large names. The mirror image — **breadth divergence**, where an index makes new highs while participation deteriorates — is one of the most reliable early warnings of a market top (see [[divergence]]). Thrusts and divergences are the two ends of the same participation spectrum: thrusts confirm broad strength off lows, divergences warn of narrowing strength near highs.

## Use and limits

- **Confirmation and timing, not a standalone system.** A breadth thrust is best used to confirm that a bottom or breakout has broad support, or to raise conviction and gross exposure — not as a mechanical, self-contained trading strategy.
- **False signals happen.** Not every cross of the thresholds precedes a lasting advance; thrusts that fire in the middle of an ongoing downtrend, or on a thin/distorted universe of issues, can fail.
- **Parameter sensitivity.** The exact thresholds (0.40 / 0.615), the 10-day EMA window, and the 10-day time limit are Zweig's specific choices; variants use different smoothing, different levels, or ratio-adjusted inputs, and results are sensitive to these parameters and to which exchange's advance-decline data is used (NYSE data includes many interest-rate-sensitive closed-end funds and ETFs that can distort raw counts).
- **Works best off major lows.** The signal is designed to catch broad reversals from oversold, washed-out conditions; applied to a market that is already extended, it has far less meaning.

Like other breadth tools (see [[market-breadth]] and [[technical-analysis]]), the breadth thrust is a *context and confirmation* indicator: it tells you *how many* stocks are participating in a move, not by itself *which* individual instrument to trade.

## Sources

- Martin Zweig, *Winning on Wall Street* — the original definition of the Zweig Breadth Thrust (10-day EMA of advancers ÷ (advancers + decliners) crossing from below 0.40 to above 0.615 within 10 trading days).
- Gregory Morris, *The Complete Guide to Market Breadth Indicators* (McGraw-Hill, 2005) — catalog of breadth measures including thrust-type signals.
- John J. Murphy, *Technical Analysis of the Financial Markets* (NYIF, 1999) — market-internals and breadth chapter.
- General technical-analysis knowledge — up/down-volume thrust framing (Wayne Whaley) and the interpretation of thrusts as broad regime-shift signals are standard, widely documented material.

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

- [[market-breadth]] -- the parent category of participation indicators
- [[advance-decline-line]] -- the foundational cumulative breadth measure
- [[mcclellan-oscillator]] -- breadth momentum oscillator used to confirm thrusts
- [[momentum-breadth]] -- breadth combined with price momentum
- [[momentum]] -- the price-momentum companion to breadth participation
- [[market-regime]] -- thrusts as bullish regime-shift signals
- [[divergence]] -- the bearish mirror image (price vs. participation)
- [[technical-analysis]] -- the discipline this signal sits within
