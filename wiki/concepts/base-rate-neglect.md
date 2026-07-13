---
title: "Base-Rate Neglect"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [behavioral-finance, risk-management, education]
domain: [behavioral-finance]
prerequisites: ["[[base-rate]]", "[[probability]]"]
difficulty: intermediate
aliases: ["Base-Rate Neglect", "Base Rate Neglect", "Base-Rate Fallacy", "Base Rate Fallacy", "Base-Rate Bias"]
related: ["[[base-rate]]", "[[probability]]", "[[bayesian-inference]]", "[[representativeness-heuristic]]", "[[overconfidence-bias]]", "[[expected-value]]", "[[kelly-criterion]]", "[[win-rate]]", "[[financial-statement-analysis]]"]
---

**Base-rate neglect** (the *base-rate fallacy*) is the cognitive bias of ignoring the **prior, unconditional probability** of an outcome — the [[base-rate]] — and judging likelihood instead by how vivid, specific, or representative the individual case feels. It is one of the most consequential errors in trading and investing because it leads people to systematically overestimate the odds of compelling-but-rare outcomes, and to over-size positions on stories that the underlying statistics do not support. This page focuses on the **bias itself**; for the underlying statistic and the Bayesian machinery, see [[base-rate]].

## The mechanism

Kahneman and Tversky showed that when people forecast a specific case, they reach for the [[representativeness-heuristic]] — they judge probability by *similarity* to a mental prototype — and largely discard the base rate. If a description "sounds like" a category, subjects rate it as probable even when that category is rare. The correct logic is Bayesian: the prior (base rate) should be updated only by genuinely *diagnostic* evidence ([[bayesian-inference]]). Base-rate neglect is the failure to anchor on that prior at all.

The trap has a precise structure: a signal can be "highly accurate" yet still be wrong most of the time when the base rate is low, because false positives swamp the rare true positives. (The worked arithmetic — the classic disease-test example — is on the [[base-rate]] page.)

## Why it matters to a stock investor

Base-rate neglect is a direct, recurring source of negative [[expected-value]] in markets:

- **"This is the next Nvidia."** The story is vivid and specific, so it feels likely — yet the base rate is that the vast majority of small caps and "next-X" candidates underperform the index over time. Neglecting that prior leads to over-allocation to lottery-like bets.
- **Turnaround and "deep value" narratives.** A compelling thesis about why *this* struggling company will recover ignores how rarely similar turnarounds actually succeed. The corrective is the **outside view** — how has this reference class historically performed?
- **Chart-pattern conviction.** A setup that "obviously" looks like a breakout is traded as high-probability even though the base rate of breakouts following through after costs may be barely 50/50.
- **Believing your own backtest.** An impressive equity curve feels predictive, but the base rate of optimised backtests surviving out-of-sample is low; the result should be discounted toward that grim prior.
- **Trusting confident forecasts.** Analyst and pundit hit-rates cluster near chance. Confidence in delivery is not diagnostic evidence — and [[overconfidence-bias]] compounds the neglect by making traders both ignore the prior *and* over-bet the deviation.

## How traders correct for it

- **Take the outside view first.** Before judging a specific trade or stock, ask: "Of all cases like this, how often does it actually work out after costs?" Anchor there, then adjust only for genuinely diagnostic specifics. This is *reference-class forecasting*.
- **Write the base rate down.** Explicitly note the prior for the reference class as a counterweight to the vivid story (a written pre-mortem).
- **Feed honest priors into sizing.** Inflated win probabilities propagate straight into [[expected-value]] and the [[kelly-criterion]], causing systematic over-sizing and elevated risk of ruin. Calibrate [[win-rate]] inputs to realistic base rates, not hopes.
- **Demand diagnostic, not merely consistent, evidence.** Information that is equally likely under "win" and "lose" does not move the odds — only genuinely discriminating evidence justifies departing from the prior.
- **Use it in research too.** Treat a single company's bullish narrative against the base rates that [[financial-statement-analysis]] reveals for similar firms.

## Base rates worth knowing (equities)

The antidote to the bias is to carry a few real reference-class numbers in your head. Some of the most durable, widely documented base rates in stock investing:

- **Most individual stocks are lifetime losers versus cash.** Hendrik Bessembinder's study of the CRSP database (1926–2016) found that the *majority* of individual US common stocks generated a lifetime buy-and-hold return below that of one-month Treasury bills, and that just over **4%** of listed companies accounted for the *entire* net wealth the market created above T-bills. Aggregate market gains come from a thin right tail — the opposite of the "any stock could be the next winner" story.
- **Most active managers lag the index.** S&P's SPIVA scorecards repeatedly show that a large majority of actively managed US equity funds — commonly **80%+** over 10–15 year windows — underperform their benchmark net of fees. The prior for "this manager will beat the market over a decade" is low.
- **IPOs tend to underperform after listing.** Jay Ritter's long-run studies find that, on average, newly public companies lag comparable seasoned firms in the years following their offering. The vivid new-listing narrative fights a poor base rate.

None of these say *your* specific pick will lose — they set the prior you must start from before the story is allowed to move the odds. Anchor here, then adjust only for genuinely diagnostic, discriminating evidence.

## Distinguishing it from related biases

- **[[representativeness-heuristic]]** — the *mental shortcut* (judging by similarity) that *causes* base-rate neglect; neglect is the *outcome*.
- **[[overconfidence-bias]]** — makes the error worse by inflating certainty in the deviation from the prior.
- **Conjunction fallacy** — judging a specific, detailed scenario as more probable than a more general one; a close cousin driven by the same representativeness shortcut.
- **The inside view** — forecasting a case purely from its own details while ignoring how its reference class performed; base-rate neglect is the inside view's signature failure.

## Worked example (hypothetical)

A stock screener flags names as "high-probability breakouts." Historically only **10%** of flagged names actually follow through (the base rate). The screen catches **80%** of real winners but also misfires on **20%** of eventual failures. Out of 1,000 flags:

| Group | Count | Flagged | Flagged count |
|-------|-------|---------|---------------|
| Real follow-throughs (10%) | 100 | 80% caught | **80** |
| Failures (90%) | 900 | 20% misfire | **180** |
| **Total flags** | | | **260** |

P(follow-through \| flagged) = 80 / 260 ≈ **31%**. A trader exhibiting base-rate neglect reads the "high-probability" label and the convincing chart and sizes the trade as if it were a near-certainty — when the honest, prior-anchored probability is barely one-in-three. The low base rate caps how good even a decent filter can be, and ignoring it is what turns a modest edge into a losing bet through over-sizing. (All figures hypothetical.)

## Related

- [[base-rate]] — the prior probability this bias ignores (and the full Bayesian arithmetic)
- [[representativeness-heuristic]] — the shortcut that produces the neglect
- [[bayesian-inference]] — the correct way to update a prior with evidence
- [[overconfidence-bias]] — compounds the error
- [[probability]] — the foundation base rates sit on
- [[expected-value]] / [[kelly-criterion]] / [[win-rate]] — where honest priors feed position sizing

## Sources

- Kahneman, D. & Tversky, A. (1973), "On the Psychology of Prediction," *Psychological Review*.
- Bar-Hillel, M. (1980), "The Base-Rate Fallacy in Probability Judgments," *Acta Psychologica*.
- Daniel Kahneman, *Thinking, Fast and Slow* (2011) — inside vs. outside view, reference-class forecasting.
- Philip Tetlock, *Superforecasting* (2015) — anchoring forecasts on base rates.
- Hendrik Bessembinder (2018), "Do Stocks Outperform Treasury Bills?", *Journal of Financial Economics* — the concentration of long-run equity wealth in a tiny fraction of stocks.
- S&P Dow Jones Indices, *SPIVA U.S. Scorecard* (recurring) — share of active equity funds underperforming their benchmark.
- Jay R. Ritter — long-run studies of post-IPO underperformance.
