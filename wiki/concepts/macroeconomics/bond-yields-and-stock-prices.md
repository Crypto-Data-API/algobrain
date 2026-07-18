---
title: "Bond Yields and Stock Prices"
type: concept
created: 2026-07-01
updated: 2026-07-01
status: review
tags: [valuation, fundamental-analysis, bonds, treasuries]
aliases: ["Bond Yields vs Stocks", "10-Year Yield and Stocks", "Treasury Yields and Equities", "TINA"]
domain: [fundamental-analysis, macro-trading]
prerequisites: ["[[interest-rates]]", "[[equity-risk-premium]]"]
difficulty: intermediate
related:
  - "[[macroeconomics]]"
  - "[[interest-rates]]"
  - "[[equity-risk-premium]]"
  - "[[yield-curve]]"
  - "[[treasuries]]"
  - "[[treasury-bonds]]"
  - "[[bonds]]"
  - "[[duration]]"
---

The **10-year Treasury yield** is the most-watched number in finance, and stock investors track it for good reason: it is the benchmark "risk-free" return that every stock is implicitly measured against. This page answers a common investor FAQ — **"why do my stocks drop when the 10-year yield jumps, and what should I actually watch?"**

## The Two Channels: Why Yields Move Stocks

A change in long-term bond yields hits stock prices through two reinforcing channels.

### 1. The discount-rate channel (valuation)

A stock is worth the present value of its future cash flows. The rate used to discount those cash flows is the risk-free yield plus the [[equity-risk-premium]]:

```
price  =  Σ  cash_flow_t / (1 + r)^t       where  r = 10-year_yield + equity_risk_premium
```

When the [[treasuries|10-year yield]] rises, `r` rises, and the same future earnings are worth less *today*. Nothing about the business changed — the math of discounting did. This is why a yield spike can knock the index lower on a day with no company news. (See [[interest-rates]] for the full mechanism.)

### 2. The competition-for-capital channel (TINA / TARA)

Stocks and bonds compete for the same dollar. When Treasuries yield almost nothing, investors are pushed into stocks for any return at all — the **"There Is No Alternative" (TINA)** regime that supports high equity valuations. When bond yields rise to attractive levels, the slogan flips to **"There Are Reasonable Alternatives" (TARA)**: a saver can lock in a solid, near-certain bond yield instead of accepting equity risk, so money rotates out of stocks and valuations compress.

## Rate of Change Beats the Level

A frequent FAQ: *"Rates are high — does that mean stocks must fall?"* Not necessarily. Markets care more about the **change and the surprise** than the absolute level:

- A **fast, surprising rise** in yields is the classic valuation headwind — it forces a quick repricing before earnings can catch up.
- A **stable high level** can be perfectly fine for stocks if earnings are growing into it. Equities have delivered strong returns across a wide range of yield levels historically.
- A **falling yield** is usually a tailwind for valuations — *unless* it is falling because the economy is collapsing (see below).

## The "Good Reason / Bad Reason" Nuance

Why yields are moving matters as much as the move itself:

| Yields rising because… | Typical read for stocks |
|------------------------|-------------------------|
| Strong growth, healthy demand | Often **OK** — earnings rise alongside the discount rate |
| Inflation/term-premium fears, supply of debt | Usually **bad** — discount rate up with no earnings offset |
| Central bank hiking aggressively | **Bearish** — tightening financial conditions (see [[fed-policy]]) |

| Yields falling because… | Typical read for stocks |
|-------------------------|-------------------------|
| Inflation cooling, soft landing | Usually **bullish** — lower discount rate, intact earnings |
| Recession / flight to safety | **Bearish** — earnings about to fall faster than rates help |

A sharply *falling* 10-year yield during a [[recession]] does not save stocks, because collapsing earnings (the numerator) overwhelm the lower discount rate (the denominator).

## Not All Stocks React Equally (Duration)

The discount-rate channel hits **long-[[duration]]** equities hardest — companies whose cash flows are mostly far in the future (high-growth, high-multiple, profitless tech). Their value sits in distant years that get discounted by many periods of `r`, so a yield move swings them like a long-dated bond. **Short-duration** equities — profitable, cash-generative value names and high-dividend payers — are less sensitive. This is the duration logic behind value vs growth leadership and is detailed in interest-rate-sensitive-sectors.

## Worked Illustration (Hypothetical)

Imagine the 10-year yield rises from 3% to 5% and the [[equity-risk-premium]] holds at 4%, so the required return `r` goes from 7% to 9%. For a stable-earnings index, a required earnings yield rising from 7% to 9% implies the P/E falling from about 14× to about 11× — roughly a 20% valuation hit, *with no change in earnings*. A long-duration growth basket might fall considerably more; a cash-rich value basket considerably less. (Illustrative arithmetic, not a forecast.)

## The Earnings-Yield Comparison

A simple way investors gauge "stocks vs bonds" value is the earnings-yield spread:

```
spread  =  S&P 500 earnings yield  −  10-year Treasury yield
```

A wide positive spread says stocks are cheap relative to bonds; a thin or negative spread says bonds look competitive. This is the "Fed model." It is a useful *relative-value sentiment gauge* but is academically criticised (it compares a real earnings yield with a nominal bond yield) — see earnings-yield and [[equity-risk-premium]] for the caveats. Do not treat it as a precise fair-value signal.

## What to Actually Watch

- The **10-year Treasury yield** — the headline benchmark discount rate.
- The **real (inflation-adjusted) yield** — see [[real-interest-rates]]; rising *real* yields are an especially clean valuation headwind.
- The **speed of the move**, not just the level.
- The **[[yield-curve|shape of the yield curve]]** — an inversion is a recession warning that affects the earnings side.
- **Why** yields are moving (growth vs inflation vs policy vs supply).

## Limitations and Cautions

- The yield-to-stocks relationship is **not mechanical**; lags vary and earnings growth can fully offset a higher discount rate.
- Central-bank bond buying (QE) can **suppress** long yields artificially, distorting the signal.
- The earnings-yield "Fed model" has **weak long-run forecasting power** — relative-value only.
- Correlation between bonds and stocks **flips by regime**: in low-inflation eras they often move opposite (bonds hedge stocks); in high-inflation eras they can fall together, weakening diversification.

## Related

- [[macroeconomics]] — the macro framework
- [[interest-rates]] — policy vs market rates and the discount-rate mechanism
- [[equity-risk-premium]] — the premium added to the bond yield to value stocks
- [[yield-curve]] — the term structure and its recession signal
- [[duration]] — why long-dated cash flows are most rate-sensitive
- [[real-interest-rates]] — inflation-adjusted yields, a cleaner valuation driver
- [[treasury-bonds]] / [[treasuries]] — the instruments behind the benchmark yield

## Sources

- US Treasury / FRED — constant-maturity Treasury yield series (the 10-year benchmark).
- Gordon Growth / discounted-cash-flow valuation framework (general finance literature).
- General market commentary on the "Fed model" and TINA/TARA dynamics. No specific wiki source ingested yet.
