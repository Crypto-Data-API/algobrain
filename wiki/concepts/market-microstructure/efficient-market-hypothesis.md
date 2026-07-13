---
title: Efficient Market Hypothesis
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags:
  - behavioral-finance
  - portfolio-theory
  - methodology
  - market-microstructure
aliases:
  - EMH
  - efficient-markets
  - efficient-market-hypothesis
  - Efficient Market Hypothesis
domain: [market-microstructure, portfolio-theory]
prerequisites: ["[[market-microstructure]]"]
difficulty: intermediate
related:
  - "[[behavioral-finance]]"
  - "[[technical-analysis]]"
  - "[[anomalies]]"
  - "[[random-walk]]"
---

# Efficient Market Hypothesis

The **Efficient Market Hypothesis (EMH)**, developed by Eugene Fama, states that asset prices fully reflect all available information, making it impossible to consistently achieve above-market returns.

EMH has three forms: **weak** (prices reflect all past trading data), **semi-strong** (prices reflect all public information), and **strong** (prices reflect all information, including insider knowledge). Critics like warren-buffett and [[jim-simons]] have outperformed benchmarks for decades, challenging EMH.

## Implications for Traders

If EMH holds in its strong form, no analysis -- fundamental-analysis, [[technical-analysis]], or insider knowledge -- can produce consistent excess returns. The logical conclusion is that investors should buy index funds and avoid active management entirely. In practice, most academics and practitioners accept that markets are "mostly efficient" but acknowledge persistent anomalies and inefficiencies.

## Arguments For EMH

- Most active fund managers underperform their benchmark index after fees over long periods.
- Information is rapidly incorporated into prices through arbitrage and competition among thousands of market participants.
- Market anomalies often diminish or disappear once they are published and widely known.

## Arguments Against EMH

- **[[behavioral-finance]]** documents systematic cognitive biases (overconfidence, loss aversion, herding, anchoring) that cause prices to deviate from fundamental value.
- **Market anomalies** persist as counter-evidence: the value premium, momentum effect, low-volatility anomaly, and post-earnings-announcement drift have been documented across decades and geographies.
- **Bubbles and crashes** -- episodes like the dot-com bubble, 2008 housing crisis, and meme stock mania are difficult to reconcile with the idea that prices always reflect fundamental value.
- **Consistent outperformers** -- Renaissance Technologies (Medallion Fund), Berkshire Hathaway, and other firms have generated statistically significant alpha over very long periods.

EMH remains one of the most debated ideas in finance and serves as an important benchmark: any trading strategy must articulate *why* it can succeed in a market populated by well-resourced, rational competitors.

## Trading Relevance

EMH is the **null hypothesis every strategy must beat**. The practical discipline it imposes: before deploying capital, articulate *why* an edge exists in a market full of well-resourced, competitive participants — i.e. which form of efficiency the strategy claims is violated, and why that inefficiency persists rather than being arbitraged away. A momentum or value strategy is implicitly a bet against semi-strong efficiency; an insider-information play bets against strong-form efficiency (and is usually illegal). The "[[anomalies|anomalies]]" literature catalogues documented, persistent violations (value, momentum, low-volatility, post-earnings drift), but EMH proponents counter that many decay after publication or are compensation for risk rather than free lunches. Either way, EMH disciplines a trader to be explicit about edge source and decay — see [[edge-taxonomy]].

## Related

- [[behavioral-finance]] — the main competing framework
- [[technical-analysis]] — implicitly bets against weak-form efficiency
- [[anomalies]] — documented persistent inefficiencies
- [[random-walk]] — the price-process model EMH implies

## Sources

- Eugene F. Fama, "Efficient Capital Markets: A Review of Theory and Empirical Work," *Journal of Finance* (1970)
- Eugene F. Fama, "Efficient Capital Markets: II," *Journal of Finance* (1991)
- Burton Malkiel, *A Random Walk Down Wall Street*
- Andrew Lo, "The Adaptive Markets Hypothesis" (2004) — a reconciliation of EMH with behavioral evidence
