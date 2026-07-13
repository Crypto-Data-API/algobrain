---
title: "Behavioral Finance Overview"
type: index
created: 2026-04-06
updated: 2026-06-22
status: excellent
tags: [behavioral-finance, psychology]
aliases: ["Behavioral Finance Index", "Psychology of Trading"]
related: ["[[behavioral-finance]]", "[[cognitive-biases]]", "[[cognitive-bias]]", "[[trading-psychology]]", "[[prospect-theory]]", "[[loss-aversion]]", "[[sentiment]]", "[[efficient-market-hypothesis]]"]
---

# Behavioral Finance Overview

> Category hub. For the standalone concept page see [[behavioral-finance]].

Psychology of trading, cognitive biases, and how human behavior affects markets.

Markets are not purely rational pricing machines -- they are driven by millions of human decisions shaped by fear, greed, overconfidence, and cognitive shortcuts. Behavioral finance studies these systematic deviations from rationality and explains phenomena like bubbles, panics, and the persistent under-performance of most retail traders. It stands in direct tension with the [[efficient-market-hypothesis]]: where EMH assumes rational agents arbitrage mispricings away, behavioral finance argues that limits to arbitrage let predictable human errors persist in prices.

Understanding [[trading-psychology]] and biases like [[loss-aversion]] can directly improve your trading: you will recognize when your own decisions are being distorted and learn to exploit the predictable mistakes of others. [[sentiment|Market sentiment]] analysis turns crowd psychology into a quantifiable trading signal.

## Foundations: Prospect Theory

The intellectual core of the field is **[[prospect-theory]]** (Kahneman & Tversky, 1979), which replaced the rational "expected utility" model of decision-making with one that matches how people actually behave:

- **Reference dependence** — outcomes are judged as gains or losses relative to a reference point (often the entry price; see [[anchoring-bias]]), not as final wealth states.
- **[[loss-aversion]]** — the pain of a loss is roughly twice the pleasure of an equivalent gain (a loss-aversion coefficient of ~2). This single asymmetry drives the [[disposition-effect]] and the tendency to cut winners and ride losers.
- **Diminishing sensitivity** — the value function is concave for gains (risk-averse) and convex for losses (risk-seeking), so people gamble to avoid a sure loss but take a sure gain.
- **Probability weighting** — small probabilities are overweighted (why lotteries and far-OTM options attract buyers) and large probabilities underweighted.

These four properties together explain a large share of the "irrational" trading behavior catalogued below.

## Start Here

- [[behavioral-finance]] -- The field: what it is and why markets deviate from rationality
- [[cognitive-biases]] -- The full catalog of systematic judgment errors and how they interact
- [[prospect-theory]] -- The formal model behind loss aversion and framing
- [[trading-psychology]] -- Discipline, emotional control, and decision-making under uncertainty
- [[loss-aversion]] -- Why losses hurt twice as much as gains feel good
- [[sentiment]] -- Measuring crowd psychology as a contrarian or confirming signal

## Catalog of Major Biases

Each is a [[cognitive-bias]] with its own page; the table maps the bias to how it manifests at the trading desk and the market-level effect it produces.

| Bias | What it is | Trading manifestation | Market-level effect |
|------|-----------|-----------------------|---------------------|
| [[loss-aversion]] | Losses hurt ~2× as much as equivalent gains feel good | Refusing to take small losses; oversized hedging | Underpins the [[disposition-effect]] and the equity-premium puzzle |
| [[disposition-effect]] | Selling winners too early, holding losers too long | Realizing gains fast, "averaging down" losers | Momentum / under-reaction to news |
| [[confirmation-bias]] | Over-weighting evidence that supports a held view | Only reading bullish takes on a long position | Slow price discovery; echo chambers |
| [[anchoring-bias]] | Fixating on a salient reference number | Treating entry price or a round number as "fair value" | Support/resistance clustering at anchors |
| [[overconfidence-bias]] | Overestimating one's own edge and precision | Over-leverage, over-trading, under-diversification | Excess volume and volatility |
| [[framing-effects]] | Same choice decided differently by wording | "90% win rate" vs "10% loss rate" changes sizing | Mispricing of equivalent payoffs |
| [[recency-bias]] | Over-weighting the most recent outcomes | Chasing what just worked; abandoning a strategy after a drawdown | Trend extrapolation, bubbles |
| [[herding]] | Following the crowd over private information | FOMO entries near tops, panic exits near bottoms | Bubbles, crashes, fat tails |
| [[recency-bias\|FOMO / fear-greed cycle]] | Emotion-driven crowd swings | Buying euphoria, selling capitulation | The boom-bust [[sentiment]] cycle |
| [[gamblers-fallacy]] | Believing past independent outcomes change future odds | "Due for a bounce" after a losing streak | Misjudged mean-reversion |
| [[dopamine-loop]] | Variable-ratio reinforcement of trading | Compulsive over-allocation to a "hot" strategy | Excess churn |
| [[ergodicity]] | Time-average ≠ ensemble-average outcomes | Misjudging the real risk of compounding/leverage | Ruin risk hidden by average-return thinking |
| [[anchoring-bias\|mental accounting]] | Treating money differently by arbitrary category | "House money" gambling with profits; segregating losses | Sub-optimal portfolio decisions |

(Pages that do not yet exist appear as forward links — gaps to fill.)

## Pages

```dataview
TABLE status, updated, tags
FROM "wiki/concepts/behavioral-finance"
WHERE type != "index"
SORT updated DESC
```

## Market Implications

Behavioral biases do not just hurt individuals — when they are correlated across many participants, they leave footprints in prices that systematic traders try to harvest:

- **Bubbles and crashes** — [[herding]], [[recency-bias|recency]], and overconfidence amplify trends until they overshoot; [[loss-aversion]] and panic then drive disorderly reversals. See [[history|market history]] for recurring episodes.
- **Momentum and under-reaction** — the [[disposition-effect]] (selling winners early) slows the incorporation of good news into price, leaving a tradeable drift; this is one behavioral explanation for the [[momentum|momentum anomaly]].
- **Mean-reversion / over-reaction** — sentiment extremes overshoot fair value, the basis of [[contrarian-extremes|contrarian]] strategies that fade crowd euphoria and capitulation.
- **Limits to arbitrage** — rational traders cannot always correct mispricings (costs, risk, short horizons), which is why behavioral mispricings *persist* rather than being instantly arbitraged away as strict [[efficient-market-hypothesis|EMH]] would predict.
- **The [[sentiment]] signal** — survey, positioning, options-skew, and put/call data turn crowd psychology into a quantifiable, often contrarian, input.

## Using Biases Defensively (Trading Psychology)

The flip side of exploiting others' biases is controlling your own. Practical guardrails map directly onto specific biases:

| Guardrail | Counteracts |
|-----------|-------------|
| Predefined stop-losses and position sizing rules | [[loss-aversion]], [[disposition-effect]] |
| A written trading plan / checklist | [[confirmation-bias]], [[overconfidence-bias]] |
| Journaling and reviewing losing trades | [[recency-bias]], overconfidence |
| Fixed-fractional risk per trade | [[ergodicity]] / ruin risk, overconfidence |
| Waiting periods before adding to a position | FOMO, [[herding]] |

See [[trading-psychology]] and [[risk-management-overview]] for the full discipline.

## Related Strategies

- [[contrarian-extremes]] -- exploiting behavioral biases and sentiment extremes for mean-reversion trades
- [[momentum]] -- under-reaction driven partly by the disposition effect

## Sources

General market knowledge; no specific wiki source ingested yet. Foundational references for this field include Kahneman & Tversky (1979) "Prospect Theory" (*Econometrica*), Kahneman *Thinking, Fast and Slow* (2011), Shiller *Irrational Exuberance* (2000), and Thaler *Misbehaving* (2015). Add a `(Source: [[source-id]])` citation here as relevant sources are ingested.
