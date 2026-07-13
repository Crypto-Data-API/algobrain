---
title: "Earnings"
type: concept
created: 2026-04-07
updated: 2026-06-21
status: excellent
tags: [fundamental-analysis, valuation]
aliases: ["Earnings Per Share", "EPS", "Earnings Report", "Quarterly Earnings"]
related: ["[[price-to-earnings-ratio]]", "[[earnings-per-share]]", "[[earnings-momentum]]", "[[earnings-season]]", "[[post-earnings-announcement-drift]]", "[[fundamental-analysis]]", "[[dividend]]", "[[valuation]]"]
domain: [fundamental-analysis]
difficulty: beginner
---

Earnings — specifically [[earnings-per-share|earnings per share (EPS)]] — represent a company's net income divided by its total shares outstanding. EPS is the single most important fundamental metric in equity analysis, serving as the denominator in the [[price-to-earnings-ratio|P/E ratio]] and the foundation for virtually all valuation models. Quarterly earnings reports are among the highest-impact catalysts for stock price movement, and the calendar of those reports — [[earnings-season]] — concentrates that volatility into a few predictable weeks each quarter.

## Overview

Earnings measure what a company actually makes after all expenses, taxes, interest, and depreciation. While revenue shows the top line (total sales), earnings show the bottom line — what remains for shareholders. A company can grow revenue rapidly but still have declining earnings if costs rise faster.

There are several earnings definitions in common use:

- **GAAP EPS**: Earnings calculated under Generally Accepted Accounting Principles. The official, audited number.
- **Non-GAAP / Adjusted EPS**: Excludes "one-time" charges like restructuring costs or stock-based compensation. Companies prefer to report this, but it can obscure real costs. [[benjamin-graham]] warned about the manipulation of "extraordinary items" in [[book-security-analysis|Security Analysis]].
- **Diluted EPS**: Accounts for all potential shares (stock options, convertible bonds) that could dilute existing shareholders. Always use diluted EPS for conservative analysis.
- **Forward EPS**: Analyst consensus estimates for future earnings. Drives forward P/E ratios and is the basis for earnings surprise calculations.
- **TTM EPS**: Trailing-twelve-months EPS — the sum of the last four reported quarters. Smooths quarterly seasonality and is the basis of the trailing P/E.

### EPS definitions at a glance

| Variant | What it captures | Typical use | Watch out for |
|---------|------------------|-------------|---------------|
| GAAP EPS | Audited net income ÷ shares | The legal "true" figure | Lumpy one-offs distort comparisons |
| Adjusted / Non-GAAP EPS | GAAP excluding "one-time" items | Management's preferred headline | Habitual "one-offs" that recur every quarter |
| Basic EPS | Net income ÷ weighted shares | Quick read | Ignores dilution from options/converts |
| Diluted EPS | Net income ÷ fully diluted shares | Conservative analysis | The number serious analysts use |
| Forward EPS | Analyst consensus for next 4 quarters | Forward P/E, surprise base | Estimates drift and can be stale |
| TTM EPS | Last four reported quarters | Trailing P/E | Backward-looking |

### The basic formula

```
EPS = (Net Income − Preferred Dividends) / Weighted Average Shares Outstanding
```

A worked example: a company earns $500m of net income, pays $20m in preferred dividends, and has 240m diluted weighted-average shares. Diluted EPS = (500 − 20) / 240 = **$2.00**. If the stock trades at $40, the trailing [[price-to-earnings-ratio|P/E]] is 40 / 2.00 = 20×.

## How It Works

The quarterly earnings cycle drives much of the stock market's short-term price action:

1. **Earnings estimates**: Wall Street analysts publish consensus EPS estimates before each quarter's report. The consensus is the mean (or median) of individual analyst forecasts; a "whisper number" is the unofficial, often higher, figure the buy-side actually expects.
2. **Earnings report**: The company releases actual results, typically after market close or before market open (so the price gap shows up at the next session's open). Most large caps follow with a management conference call.
3. **Earnings surprise**: The difference between actual EPS and consensus estimate, usually expressed as a percentage: `surprise % = (actual EPS − consensus EPS) / |consensus EPS|`. A positive surprise (beat) tends to drive the stock higher; a negative surprise (miss) drives it lower. The magnitude of the surprise matters, but so does the quality — did the beat come from revenue growth or cost-cutting? Standardized Unexpected Earnings (SUE) scales the surprise by its historical standard deviation to make surprises comparable across stocks.
4. **Guidance**: Forward-looking statements from management about expected future earnings. Guidance revisions often matter more than the current quarter's results — a company can beat on EPS yet sell off hard if it cuts guidance (a "beat and lower").
5. **[[post-earnings-announcement-drift|Post-earnings-announcement drift (PEAD)]]**: Academic research (Ball & Brown 1968; Bernard & Thomas 1989) shows that stocks tend to drift in the direction of the earnings surprise for weeks or months after the report — an anomaly that contradicts the [[efficient-market-hypothesis]] and is one of the most robust documented in equity markets.

### Anatomy of the reaction

The stock's move on results is driven by the gap between *reported reality* and *priced-in expectation*, not by the absolute number. The four canonical outcomes:

| Outcome | EPS vs consensus | Guidance | Typical reaction |
|---------|------------------|----------|------------------|
| Clean beat | Above | Raised | Gap up, often follow-through (PEAD) |
| Beat and lower | Above | Cut | Initial pop then sell-off; net negative |
| In-line | At consensus | Reaffirmed | Muted; "priced in" |
| Miss | Below | Cut | Gap down, frequent continuation lower |

A worked example: XYZ is expected to earn $1.20. It reports $1.35 — a +12.5% surprise — but warns next-quarter revenue will be flat. The headline beat is real, yet the lowered outlook can send the stock down 5% at the open. The lesson: trade the *reaction to expectations*, not the headline.

[[benjamin-graham]] emphasized analyzing earnings over multi-year periods (7-10 years minimum) rather than focusing on any single quarter, to smooth out cyclical effects and accounting anomalies — the inverse of the short-horizon event trader's lens.

## Earnings Season

[[earnings-season]] is the cluster of weeks each quarter — typically beginning a week or two after quarter-end — when the bulk of public companies report. The U.S. season is informally kicked off by the big banks (JPMorgan, etc.) and runs roughly mid-January, mid-April, mid-July, and mid-October. For traders it concentrates idiosyncratic risk: single-stock [[implied-volatility]] rises into the report and collapses immediately after (the "IV crush"), index correlation falls as names move on their own news, and overnight gap risk spikes. Calendars from data vendors flag the exact date and whether a company reports before the open (BMO) or after the close (AMC).

## Trading Applications

- **Valuation**: EPS is the denominator of the [[price-to-earnings-ratio|P/E ratio]], the most widely used valuation metric. Higher earnings growth justifies higher P/E multiples.
- **[[earnings-momentum]]**: Strategies that buy stocks with accelerating earnings growth and rising analyst estimates. [[peter-lynch]] famously sought companies with strong earnings growth at reasonable prices (the PEG ratio).
- **[[post-earnings-announcement-drift|Drift trading]]**: Buying the strongest positive surprises (high SUE) and shorting the largest misses, holding for the multi-week drift window — the systematic expression of PEAD.
- **Earnings event trading**: Some traders specialize in positioning around earnings reports, using [[options]] straddles or strangles to profit from the expected volatility. The catch is **[[implied-volatility|IV]] crush** — a long straddle bought before the print can lose even on a correct directional call because the post-report collapse in implied volatility deflates both legs. The break-even is the *expected move* the [[options-chain]] is pricing, not zero.
- **Quality screening**: Consistent earnings growth (e.g., 10+ years of positive EPS growth) is a quality signal. Erratic earnings suggest a cyclical or poorly managed business.
- **Margin of safety**: Graham's concept of [[margin-of-safety]] is fundamentally about buying at a price low enough relative to demonstrated earning power that even a decline in earnings would not result in permanent capital loss.

## Pitfalls and Risks

- **Beating low expectations is not strength.** A "beat" against an estimate that was guided down all quarter is hollow; track estimate revisions, not just the final surprise.
- **Adjusted-EPS games.** Serial "one-time" charges (restructuring every year, perpetual stock-comp add-backs) inflate non-GAAP EPS. Reconcile to GAAP.
- **Buybacks flatter EPS.** Shrinking the share count raises EPS even with flat net income — growth in *earnings* and growth in *per-share earnings* can diverge.
- **Gap and overnight risk.** Because most reports land outside regular hours, [[stop-loss]] orders give no protection across the gap; position sizing must assume the worst plausible jump.
- **IV crush punishes naive option buyers.** See above — long premium into earnings needs a move larger than the chain's implied move just to break even.
- **One quarter is noise.** Per Graham, a single quarter rarely changes a thesis; the signal is in the trend and the guidance trajectory.

## Related

- [[earnings-per-share]] — The headline metric itself
- [[earnings-season]] — The quarterly reporting calendar
- [[post-earnings-announcement-drift]] — The multi-week drift anomaly after surprises
- [[price-to-earnings-ratio]] — Stock price divided by EPS
- [[earnings-momentum]] — Trading strategy based on earnings acceleration
- [[fundamental-analysis]] — Analytical framework that centers on earnings
- [[implied-volatility]] — Rises into reports, crushes after (IV crush)
- [[options-chain]] — Prices the expected move around the report
- [[dividend]] — Payments funded by earnings
- [[margin-of-safety]] — Buying below intrinsic value derived from earnings

## Sources

- (Source: [[book-security-analysis]]) — Graham and Dodd's comprehensive framework for earnings analysis
- (Source: [[book-one-up-on-wall-street]]) — Peter Lynch's approach to earnings-driven stock selection
