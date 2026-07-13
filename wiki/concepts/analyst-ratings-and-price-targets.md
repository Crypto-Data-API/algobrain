---
title: "Analyst Ratings and Price Targets"
type: concept
created: 2026-07-01
updated: 2026-07-02
status: good
tags: [stocks, fundamental-analysis, valuation, education]
aliases: ["Analyst Ratings", "Price Targets", "Sell-Side Ratings", "Wall Street Ratings", "consensus rating", "PT"]
domain: [valuation, behavioral-finance]
prerequisites: ["[[valuation]]", "[[fundamental-analysis]]"]
difficulty: beginner
related: ["[[valuation]]", "[[fundamental-analysis]]", "[[earnings]]", "[[discounted-cash-flow]]", "[[short-interest]]", "[[behavioral-finance]]", "[[efficient-market-hypothesis]]", "[[relative-strength-rating]]"]
---

# Analyst Ratings and Price Targets

An **analyst rating** is a sell-side equity analyst's published recommendation on a stock — typically a label like *Buy / Hold / Sell* (or *Overweight / Neutral / Underweight*) — and a **price target** is that analyst's estimate of where the stock should trade over a defined horizon, almost always the next **12 months**. They are produced by research analysts at banks and brokerages (the "sell side"), distributed to clients, and widely republished on financial dashboards. ALFRED surfaces them because they are one of the most-asked-about numbers on a stock page — but they are opinions with well-documented biases, not predictions to be taken at face value.

## What the Ratings Mean

Firms use different vocabularies for the same three-way idea. The mapping is roughly:

| Bullish | Neutral | Bearish |
|---|---|---|
| Buy, Strong Buy | Hold | Sell, Strong Sell |
| Overweight | Equal-weight / Neutral / Market Perform | Underweight |
| Outperform | In-line / Sector Perform | Underperform |

A rating is a *relative* call — usually relative to the analyst's coverage universe or sector, and over the same ~12-month horizon as the price target. "Overweight" means *hold more of this than the benchmark weight*, not "this stock will definitely go up."

## What a Price Target Is

A price target is the analyst's modeled fair value 12 months out, derived from some mix of:

- a **valuation multiple** applied to forward estimates — e.g. a target P/E times next year's expected [[earnings]] per share;
- a **[[discounted-cash-flow|discounted cash flow]] (DCF)** model;
- **sum-of-the-parts** or comparable-company analysis.

The target and the rating should be internally consistent: a large gap between the target and the current price ("implied upside") typically pairs with a Buy, a small gap with a Hold.

## Consensus and the Mean/Median Target

Because dozens of analysts may cover one large-cap stock, the more useful figures are the **consensus**:

- **Consensus rating** — the average of all ratings, often shown on a 1–5 scale (1 = Strong Buy) or as a count (e.g. "18 Buy, 7 Hold, 2 Sell").
- **Consensus (mean) price target** — the average of individual targets; the **high** and **low** targets show the spread of opinion.

A wide spread between the high and low target signals genuine disagreement about the company's future — itself useful information.

## Why It Matters to a Retail Stock Investor

- **A free synthesis of professional models.** Analysts spend full time modeling the company; the consensus aggregates many such models into one number.
- **Catalysts move price, not the static rating.** Markets react far more to *changes* — an **upgrade, downgrade, or target revision** — than to a standing rating, because the change carries new information. An upgrade can move a stock several percent in a session.
- **Estimate revisions are a documented signal.** The trend in analysts' *earnings estimates* (up vs down) is the basis of well-known momentum effects (e.g. the [[post-earnings-announcement-drift|post-earnings-announcement drift]] and estimate-revision strategies). The direction of revisions often matters more than the level of the target.
- **A reference point for your own thesis.** If your view differs sharply from consensus, that is worth understanding — either you see something the street misses, or you are missing something the street sees.

## How to Interpret Ratings Sensibly

1. **Read the implied upside, not just the label.** Current price $100, mean target $120 → ~20% implied 12-month upside. That framing is more informative than "Buy."
2. **Watch revisions over levels.** A stream of target *cuts* with the rating still at "Buy" is more bearish than the standing label suggests.
3. **Look at dispersion.** A tight cluster of targets means agreement; a high-vs-low spread of 2–3x means the outcome is genuinely uncertain.
4. **Cross-check with other signals** — valuation, [[earnings]] trend, [[short-interest]], and price action. Ratings are one input, not a verdict.

## Limitations and Biases

Analyst output carries structural biases every retail investor should price in:

- **Bullish skew.** Across the market, *Buy/Outperform* ratings vastly outnumber *Sell* ratings. Maintaining management access, avoiding conflicts with the bank's investment-banking relationships, and career incentives all push ratings upward. An outright "Sell" is rare and therefore notable.
- **Lagging targets.** Targets are frequently revised *after* the stock has already moved, chasing price rather than leading it — analysts raise targets into rallies and cut them into declines.
- **Conflicts of interest.** This is why post-2003 regulation (the Global Research Analyst Settlement and FINRA/SEC rules) mandates disclosure of banking relationships and separation of research from banking. Read the disclosures.
- **Horizon mismatch.** A 12-month target says nothing about the path; a stock can hit the target after first falling 30%.
- **Herding.** Analysts cluster near consensus to limit career risk, so the "average" can be anchored rather than independent.
- **Not an [[efficient-market-hypothesis|edge by itself]].** Because ratings are public, any easy alpha is largely arbitraged away; the residual signal lives mostly in *revisions* and *surprises*, not static labels.

## Hypothetical Example

Imagine a fictional company, "Acme Corp," trading at **$50**. Coverage looks like:

- 20 analysts: **12 Buy, 6 Hold, 2 Sell** → consensus skews bullish.
- Mean 12-month target **$58** (≈16% implied upside); high **$75**, low **$40**.

Two days after a strong earnings report, three analysts **raise** their targets and one **upgrades** Hold → Buy. Even though the *label* for most was already "Buy," the *revisions* are the news — and the stock gaps up on the upgrade. A month later, a guidance cut prompts two **downgrades** and a wave of target reductions toward the low end; the wide high–low spread that existed beforehand was a clue that conviction was thin. All figures here are invented to illustrate the mechanics, not a real recommendation.

## Related

- [[valuation]] — the models behind price targets
- [[fundamental-analysis]] — the research process analysts perform
- [[earnings]] — the estimates that drive targets and revisions
- [[discounted-cash-flow]] — a common price-target methodology
- [[short-interest]] — a complementary sentiment input
- [[behavioral-finance]] — herding and anchoring biases in ratings
- [[relative-strength-rating]] — a price-based rating, contrasted with fundamental ratings
- [[post-earnings-announcement-drift]] — the drift that estimate revisions help drive

## Sources

- U.S. Securities and Exchange Commission, *Investor Bulletin: Analyzing Analyst Recommendations* (investor.gov)
- FINRA Rule 2241, "Research Analysts and Research Reports" — disclosure and conflict rules
- Global Research Analyst Settlement (2003) — separation of research from investment banking
- CFA Institute, *Standards of Practice* — analyst independence and objectivity guidance
