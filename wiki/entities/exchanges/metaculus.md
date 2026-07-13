---
title: "Metaculus"
type: entity
created: 2026-05-14
updated: 2026-06-10
status: good
tags: [behavioral-finance, event-driven, ai-trading, company]
aliases: ["Metaculus.com"]
entity_type: company
founded: 2015
headquarters: "Santa Cruz, California, USA"
website: "https://www.metaculus.com"
related: ["[[prediction-markets]]", "[[polymarket]]", "[[kalshi]]", "[[manifold-markets]]", "[[prediction-market-calibration]]", "[[forecasting]]"]
---

Metaculus is a non-profit forecasting platform that aggregates predictions from trained forecasters on long-horizon questions across science, technology, geopolitics, and economics. Unlike [[polymarket]] or [[kalshi]], no real money is deployed; aggregation uses statistical methods (weighted by past Brier scores) rather than market pricing, which makes it a useful calibration benchmark in [[prediction-market-calibration]] studies.

## History

Founded in 2015 by Anthony Aguirre (physicist, UC Santa Cruz / Future of Life Institute co-founder) and Greg Laughlin (astronomer, Yale). Originally built as a research platform supporting the Future of Humanity Institute and the broader academic forecasting community. Operates as a non-profit (Metaculus Inc), with revenue from tournaments, research grants, and partnerships rather than user trading fees.

Key recent developments:

- **April 2024** — Deger Turan (previously head of the AI Objectives Institute) became CEO, succeeding founder-era leadership and steering the platform toward AI-forecasting evaluation
- **2024** — Metaculus rewrote its platform and **open-sourced the codebase under the BSD-2-Clause license**, an unusual move among forecasting platforms
- **2024–2026** — Launched the **AI Forecasting Benchmark (AIB) tournament series**: quarterly (later seasonal) tournaments with ~$30,000 prize pools per quarter pitting forecasting bots against Metaculus Pro Forecasters, plus a bi-weekly "MiniBench". The Q2 2025 edition ran 348 questions with 54 bot-makers. Through 2025, human Pro Forecasters maintained a statistically significant accuracy lead over the best LLM-based bots — a live benchmark for whether AI can match elite human judgment

## Mechanism

Users submit point predictions and, on continuous questions, full confidence intervals. The headline aggregate — the "community prediction" — is a recency- and track-record-weighted median of individual forecasts, with weights derived from each forecaster's historical Brier score. Both binary (yes/no) and continuous (scalar) questions are supported, with continuous questions resolving against a numeric value rather than a discrete outcome.

Forecasters can update their predictions as often as they like up until resolution. Scoring is proper (Brier for binary, log score for continuous), which incentivises honest probability reporting rather than gaming.

## Calibration track record

Metaculus publishes public calibration plots and historical Brier scores by question category. The community prediction is typically well-calibrated on resolved questions, especially in the medium term. The platform is frequently used as a research benchmark for evaluating forecasting LLMs (e.g. AI vs. human forecaster tournaments) and as a comparison point against market-based platforms in [[prediction-market-calibration]] studies.

## Crypto and trading-relevant questions

Metaculus hosts long-horizon questions on Bitcoin/Ethereum price levels, regulatory outcomes (SEC actions, ETF approvals), exchange milestones, and protocol upgrades. The question pool is smaller and slower-moving than [[polymarket]] but extends further out — some questions resolve 5 to 50 years in the future, which no real-money market can practically support.

## Comparison to market-based platforms

| Dimension | Metaculus | [[polymarket\|Polymarket]] | [[manifold-markets\|Manifold]] |
|-----------|-----------|------------|----------|
| Incentive | Reputation (no money) | Real USDC | Play money |
| Aggregation | Track-record-weighted median | Market price | Market price |
| Time horizon | Hours to decades | Hours to ~2 years | Hours to years |
| Crypto markets | Few, slow-moving | Many, fast-moving | Few |
| Use for trading | Long-horizon calibration benchmark | Short-medium catalyst signal | Sentiment proxy only |

## Use cases for traders

- **Calibration benchmark** — compare the Metaculus community prediction to the [[polymarket]] price on the same (or near-identical) question; persistent divergence indicates either market mispricing, different participant pools, or a liquidity/incentive premium worth investigating
- **Long-horizon thesis validation** — Polymarket markets typically resolve within two years; Metaculus extends to multi-year and multi-decade theses, useful for position-trading and macro overlays
- **Forecasting LLM evaluation** — Metaculus runs ongoing AI forecaster tournaments and tracks model performance versus human aggregates, relevant to anyone building LLM-driven research workflows

## Limitations

- No financial stake means weaker incentive for diligence relative to a real-money market — Metaculus relies on reputation, scoring, and intrinsic motivation
- Small forecaster pool relative to Polymarket's user base (a few thousand active forecasters versus hundreds of thousands of monthly Polymarket users)
- Slower to update on news — there is no continuous price discovery; the aggregate moves only when forecasters choose to submit, which can lag market reactions by hours to days
- Question wording is curated by moderators, which can introduce framing bias and limits coverage of fast-breaking catalysts

## API and data access

Metaculus provides a public API for fetching question metadata, historical community predictions, individual forecast trajectories, and resolution data. This is useful for backtesting [[prediction-market-calibration]] hypotheses and for building cross-platform divergence signals against [[polymarket]] or [[kalshi]] order books.

## Related

- [[prediction-markets]]
- [[polymarket]]
- [[kalshi]]
- [[manifold-markets]]
- [[prediction-market-calibration]]
- [[forecasting]]

## Sources

See [[prediction-markets]] for general prediction-market context and cross-platform comparisons.

- Metaculus AI Forecasting Benchmark — https://www.metaculus.com/aib/
- Metaculus Tournaments index (AIB Q1/Q2 2025, Fall 2025) — https://www.metaculus.com/tournaments/
- LessWrong, "Q2 AI Benchmark Results: Pros Maintain Clear Lead" (2025) — https://www.lesswrong.com/posts/Surnjh8A4WjgtQTkZ/q2-ai-benchmark-results-pros-maintain-clear-lead
- Metaculus open-source repository (BSD-2-Clause) — https://github.com/Metaculus/metaculus
- Metaculus track record / calibration — https://www.metaculus.com/questions/track-record/
- Verified via web search, 2026-06-10
