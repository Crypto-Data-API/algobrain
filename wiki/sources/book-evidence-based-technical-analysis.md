---
title: "Evidence-Based Technical Analysis"
type: source
created: 2026-04-13
updated: 2026-06-12
status: good
tags: [book, technical-analysis, backtesting, education, meta]
aliases: ["Evidence-Based Technical Analysis", "EBTA", "Aronson EBTA"]
source_type: book
source_url: "https://www.wiley.com/en-us/Evidence+Based+Technical+Analysis-p-9780470008744"
source_author: "David Aronson"
source_date: 2007-01-01
source_file: ""
confidence: high
claims_count: 8
related: ["[[technical-analysis-overview]]", "[[backtesting-overview]]", "[[data-mining]]", "[[overfitting-detection]]", "[[book-advances-in-financial-ml]]"]
---

*Evidence-Based Technical Analysis: Applying the Scientific Method and Statistical Inference to Trading Signals* by David Aronson (Wiley, 2007) applies the scientific method and statistical hypothesis testing to evaluate technical analysis claims. The book argues that most traditional technical indicators lack statistically significant predictive power when properly tested with data-mining bias corrections like White's Reality Check and the Hansen Superior Predictive Ability test. A foundational text for quantitative approaches to validating trading strategies.

## Key Claims

1. [HIGH] Most chart patterns and traditional technical indicators fail standard statistical significance tests when data-mining bias is accounted for.
2. [HIGH] **White's Reality Check** (WRC) is a bootstrap-based procedure that corrects p-values for the number of rules tested across a dataset, preventing spurious "discoveries" from multiple comparisons.
3. [HIGH] The **Hansen Superior Predictive Ability (SPA) test** improves on WRC by being less sensitive to the inclusion of poor-performing rules in the test universe.
4. [HIGH] Subjective, visually-identified chart patterns (e.g., head-and-shoulders, double tops) are inherently unfalsifiable — they lack objective definitions and therefore cannot be rigorously tested.
5. [MEDIUM] Aronson tests 6,402 binary trading rules across five technical indicator categories on the S&P 500 (1980-2005) and finds no statistically significant evidence of predictive power after data-mining correction.
6. [HIGH] The scientific method requires that trading hypotheses be stated before examining data (deductive reasoning), not derived from patterns seen in the data (inductive/data-snooping).
7. [MEDIUM] The book distinguishes between "objective TA" (rules that can be precisely defined and tested) and "subjective TA" (pattern-recognition approaches that resist formal testing), arguing only the former is scientifically admissible.
8. [HIGH] Survivorship bias, look-ahead bias, and selection bias in published trading system results render most claims of technical analysis profitability unreliable.

## Relevance to Wiki

This book underpins several wiki concepts:

- **[[overfitting-detection]]** — the multiple-comparisons problem and how to correct for it when evaluating strategy performance
- **[[backtesting-overview]]** — rigorous statistical framework for what constitutes a valid backtest
- **[[technical-analysis-overview]]** — challenges the foundational assumptions of pattern-based TA
- **[[data-mining]]** — core reference on data-mining bias in financial research

## Related

- [[technical-analysis-overview]]
- [[backtesting-overview]]
- [[overfitting-detection]]
- [[data-mining]]
- [[book-advances-in-financial-ml]]

## Sources

- Aronson, David. *Evidence-Based Technical Analysis*. Wiley, 2007. ISBN 978-0470008744.
