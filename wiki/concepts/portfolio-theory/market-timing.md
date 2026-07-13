---
title: "Market Timing"
type: concept
created: 2026-04-13
updated: 2026-06-22
status: excellent
tags: [portfolio-theory, behavioral-finance, valuation, risk-management]
aliases: ["Market Timing", "tactical-asset-allocation"]
domain: [portfolio-theory, behavioral-finance]
prerequisites: ["[[portfolio-theory]]"]
difficulty: intermediate
related: ["[[market-crashes]]", "[[cash-as-asset]]", "[[yield-curve]]", "[[volatility]]", "[[dollar-cost-averaging]]", "[[trend-following]]"]
---

Market timing is the strategy of moving in and out of the market — or switching between asset classes — based on predictive methods, in an attempt to buy before rallies and sell before declines. It sits in direct tension with the buy-and-hold doctrine, and the academic consensus is that consistent, profitable timing is extremely difficult because it requires being right *twice*: when to exit and when to re-enter. Fred takes a nuanced view: "It's not timing, but time in the market that counts — this statement is only partially true. Timing is important. You wish to buy at the lowest possible price, so the time to buy is when the market as a whole dips."

## Why It Is So Hard

Equity returns are highly concentrated in a small number of days, and those days cluster *around* volatile periods (often right after sharp declines). An investor who sidesteps a crash but is also out of the market for the violent rebound can permanently impair returns. Widely cited illustrations (e.g. analyses of the S&P 500 over multi-decade windows) show that missing just the 10 best trading days over ~20 years roughly halves the cumulative return versus staying fully invested; missing the best 20-30 days can turn a positive return negative. Because the best and worst days are temporally adjacent, attempts to dodge the worst days usually forfeit the best ones too.

This is compounded by:

- **Transaction costs and taxes** — frequent switching incurs spreads, commissions, and short-term capital gains.
- **Behavioral failure** — most discretionary timing is fear-and-greed driven: investors capitulate near bottoms and chase near tops, the opposite of the intended edge (see [[behavioral-finance]]).
- **The two-decision problem** — even a 70%-accurate exit signal paired with a 70%-accurate re-entry signal is right on both only ~49% of the time.

### The "missing the best days" arithmetic

The standard illustration takes a fully-invested benchmark over a multi-decade window and removes the single best trading days. The shape of the result is remarkably consistent across studies and time windows (figures below are *illustrative round numbers* showing the well-documented pattern, not a specific dataset):

| Scenario over a ~20-year window | Effect on ending wealth |
|---|---|
| Stay fully invested | Baseline (full compounded return) |
| Miss the **10 best days** | Roughly **half** the ending wealth |
| Miss the **20 best days** | Returns cut to a small fraction of the baseline |
| Miss the **30–40 best days** | A positive market turns into a **net loss** |

**Why this is so punishing:** the best and worst days cluster together. Many of the largest single-day *gains* in history occurred within days of the largest single-day *losses*, inside the same crisis. An investor who panics out after a crash to "avoid the worst" is almost mechanically positioned to miss the violent rebound — forfeiting the best days while sitting in cash. Because of compounding, a handful of missed days at the *start* of a recovery permanently lowers the entire forward path.

**The symmetric caveat:** these studies almost always exclude the mirror exercise of *missing the worst days*, which would look spectacular. The honest reading is not "timing is impossible" but "you must be right about *both* the worst and the best days, which are temporally inseparable" — which is why [[time-in-market|time in the market]] beats *timing* the market for the vast majority of participants.

## Disciplined vs. Reactive Timing

The key distinction is between **rules-based, systematic** timing and **reactive, emotional** timing. Tactical approaches that have empirical support when applied mechanically include:

- **Valuation-based** — scaling equity exposure inversely to valuation (e.g. CAPE/Shiller PE). High starting valuations predict lower forward 10-year returns, but the signal is slow and can be early by years.
- **[[yield-curve]] / macro** — reducing net exposure when the 2s/10s curve inverts or when [[leading-indicators|leading indicators]] deteriorate.
- **[[trend-following|Trend / momentum]]** — time-series momentum rules (e.g. hold equities only above the 200-day moving average) historically reduce drawdowns and improve risk-adjusted returns, at the cost of whipsaws in choppy markets.
- **[[volatility]] targeting** — cutting exposure as realized/implied vol rises, raising it as vol falls; mechanically improves Sharpe by avoiding the highest-vol (and lowest-return) regimes.

These add value primarily by **reducing drawdowns and improving risk-adjusted return (Sharpe)**, not by reliably beating buy-and-hold on raw return.

| Approach | Signal | Primarily helps | Main weakness |
|---|---|---|---|
| **Valuation tilt** | CAPE / Shiller PE, earnings yield | Long-horizon return + drawdown avoidance | Very slow; can be early by *years* |
| **Yield-curve / macro** | 2s10s inversion, [[leading-indicators]] | Recession-drawdown avoidance | Few signals; long, variable lead times |
| **Trend / momentum** | Price vs. 200-day MA, time-series momentum | Drawdown reduction, Sharpe | Whipsaws in range-bound markets |
| **Volatility targeting** | Realized / implied vol | Sharpe, tail-risk | Lags fast vol spikes; can de-risk into bottoms |
| **Discretionary / emotional** | Gut, news, fear/greed | (nothing reliably) | Buys tops, sells bottoms — value-destroying |

## Trading / Portfolio Relevance

For most investors, the practical conclusion is to favour [[dollar-cost-averaging]] and a strategic allocation over discretionary timing, while reserving systematic tactical overlays (trend, vol-targeting, valuation tilts) for a portion of the book. Fred's framing — buy *into weakness* when the whole market dips rather than trying to predict tops — is a contrarian, rules-light version of timing that aligns with contrarian-investing and the long-run upward drift of equities. The danger is the same one [[market-crashes]] expose: timing decisions made in panic almost always destroy value.

**Worked example — DCA vs. waiting for the dip.** An investor has $24,000 to deploy and is tempted to "wait for a better entry." Compare two disciplined plans:

- *Time in the market (lump sum + DCA):* invest a portion now and the rest over 12 monthly tranches of $2,000 via [[dollar-cost-averaging]]. Capital is working immediately, harvesting the equity drift and any dividends, and the monthly buys automatically purchase *more* shares when prices dip.
- *Timing (cash on the sidelines):* hold the full $24,000 in [[cash-as-asset|cash]] waiting for a 10% drop. If the market drifts up 15% before any dip arrives, the "better entry" is still above today's price — the wait *cost* money. If the dip does come, the investor must then make a *second* correct decision (re-enter at the bottom, against their own fear) — the [[#Why It Is So Hard|two-decision problem]] in action.

The asymmetry favours staying invested: the cost of being out during the drift is large and certain, while the benefit of a perfectly-timed dip is small and uncertain. The hybrid that survives contact with reality is a strategic allocation, DCA on new cash, and a *rules-based* tactical overlay (e.g. trend or vol-targeting) on a slice of the book — never an all-in/all-out discretionary call.

## How traders actually use this

- **Separate the book.** Keep the core in a strategic [[asset-allocation|allocation]] compounded via [[time-in-market|time in the market]]; ring-fence a defined, smaller satellite sleeve for *systematic* tactical timing (trend, vol-target, valuation tilt). Never let a discretionary timing call touch the whole portfolio.
- **Pre-commit the rules.** Write entry/exit rules and rebalance bands *before* the volatility arrives, so panic cannot rewrite them. A 200-day-MA rule or a vol-target band is only useful if you actually follow it through the drawdown.
- **Deploy cash methodically.** New cash goes in via DCA or rules-based tranches, not a single "I'll wait" decision. Hold [[cash-as-asset|dry powder]] deliberately and deploy it *into* weakness, per Fred's contrarian framing — not as an open-ended bet on calling the top.
- **Measure on Sharpe, not bragging rights.** Judge any timing overlay by whether it improved *risk-adjusted* return and drawdown, not whether it occasionally dodged a crash. Most honest overlays earn their keep by smoothing the ride, not by beating buy-and-hold on raw return.

## Common pitfalls

- **The single-decision illusion.** Selling out feels like one good call; it is actually two (when to leave *and* when to return), and being right on both is rare.
- **Cash drag.** Sitting in cash "until things calm down" forfeits the equity drift and dividends every day the market doesn't crash — usually most days.
- **Whipsaw on mechanical rules.** Trend and vol rules whipsaw in choppy markets; over-trading the signal bleeds the edge through costs.
- **Survivorship in the story.** "I'd have sold before the crash" ignores the symmetric requirement to also buy back the rebound; the worst and best days are inseparable.
- **Fighting the drift.** Equities have a long-run upward drift; persistent net-short or all-cash "timing" fights a structural tailwind and loses on average.


## Related

- [[dollar-cost-averaging]] — the systematic alternative to timing entries
- [[trend-following]] — rules-based momentum timing
- [[yield-curve]] — a macro timing signal
- [[volatility]] — volatility-targeting overlays
- [[cash-as-asset]] — holding cash as a timing/dry-powder decision
- [[market-crashes]] — where emotional timing does the most damage
- [[behavioral-finance]] — why most timing fails
- [[time-in-market]] — the buy-and-hold alternative to timing
- [[asset-allocation]] — the strategic anchor a tactical overlay rides on
- [[leading-indicators]] — macro inputs for systematic timing

## Sources

- Sharpe, W.F. (1975). *"Likely Gains from Market Timing."* *Financial Analysts Journal* — establishes the high accuracy required for timing to beat buy-and-hold.
- Shiller, R. — cyclically-adjusted PE (CAPE) and the valuation-return relationship.
- AQR / academic literature on time-series momentum and volatility targeting (Moskowitz, Ooi, Pedersen 2012).
