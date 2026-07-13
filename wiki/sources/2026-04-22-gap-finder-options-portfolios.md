---
title: "Gap Finder: Options Portfolios (Perplexity Deep Research)"
type: source
created: 2026-05-03
updated: 2026-05-03
status: good
tags: [meta, options, derivatives, data-provider]
aliases: ["Options Portfolios Gap Analysis 2026-05-03"]
source_type: article
source_url: "https://www.perplexity.ai/search (sonar)"
source_author: "Perplexity AI — gap_finder.py"
source_date: 2026-05-03
source_file: "raw/articles/2026-04-22-gap-finder-options-portfolios.md"
confidence: medium
claims_count: 30
related: ["[[probability-of-profit]]", "[[spread-width-selection]]", "[[pyalgotrade]]", "[[put-options]]", "[[short-position]]", "[[iron-condors]]", "[[options-greeks]]"]
---

Perplexity research run on 2026-05-03 via `tools/gap_finder.py --topic "options portfolios"`. Surveyed gaps in the wiki's options-portfolio coverage: education platforms, visualization tools, risk metrics, structural mechanics, and event-driven strategies. Output drove a batch of 8 new pages plus 2 thin-page upgrades.

## Key Findings (by category)

### Entities — Education and Tooling [HIGH confidence]
- **tastytrade / tastyworks** — Retail options-focused broker and education hub; strangle/iron-condor curriculum is dominant in retail education. ⬛ page created 2026-05-03.
- **OptionAlpha** — Comprehensive strategy library with auto-trading bots and backtesting; widely cited in retail options communities. ⬛ page created 2026-05-03.
- **OptionStrat** — Payoff-diagram visualizer used heavily by retail to construct multi-leg trades. ⬛ page created 2026-05-03.
- **Interactive Brokers** — ✅ already in wiki.
- **CBOE** — ✅ already in wiki (entity + exchange page).
- **Nassim Taleb** — ✅ already in wiki.

### Concepts — Risk Metrics and Mechanics [HIGH confidence]
- **Probability of Profit (PoP)** — Statistical likelihood a trade closes profitable; central metric for premium-selling. Retail platforms target ~60–70% PoP. ⬛ page created 2026-05-03.
- **Spread Width Selection** — Distance between short and long strikes; directly drives max profit, max loss, and PoP. ⬛ page created 2026-05-03.
- **Dividend Adjustments** — How dividends affect option pricing and early-exercise risk on short calls. ⬛ page created 2026-05-03.
- **Volatility Smile / Skew** — ✅ already covered.
- **Theta Decay / Gamma Risk** — ✅ already covered.
- **Assignment Risk** — ✅ already covered (`assignment.md`, `assignment-and-exercise.md`).
- **Vertical Spreads** — ✅ already covered.

### Strategies [MEDIUM confidence]
- **Earnings Volatility Trading** — IV crush playbook around earnings; distinct from earnings-calendar awareness. ⬛ page created 2026-05-03.
- **Iron Condors** — ✅ already covered (Perplexity falsely flagged it as truncated; verified complete).
- **Butterfly / Calendar / Strangle / Ratio Spreads** — ✅ all already covered.

### Data Sources / Tools [MEDIUM confidence]
- **PyAlgoTrade** — Python event-driven backtesting framework; rounds out the Zipline/Backtrader trio. ⬛ page created 2026-05-03.
- **Polygon.io / Alpaca / IB API** — ✅ already covered.
- **Zipline / Backtrader** — ✅ already covered.

### Upgraded Pages
- **Put Options** — Expanded from 46 to fuller treatment covering pricing, Greeks, strategies. 🔧 upgraded 2026-05-03.
- **Short Position** — Expanded from 36 lines with deeper coverage of mechanics and risks. 🔧 upgraded 2026-05-03.

## Recent Developments (2024-2026)
- Increased retail adoption of iron condors driven by lower commissions and educational content.
- Enhanced Greeks visualization tools now standard on retail platforms.
- Regulatory focus on options suitability — brokers tightening multi-leg approval requirements.
- AI-powered strike selection tools emerging to optimize PoP and risk/reward ratios.

## Confidence Notes
- Entity facts (tastytrade, OptionAlpha, OptionStrat) are HIGH (well-documented public companies/tools).
- Strategy and concept material is MEDIUM (synthesized from retail education sources, not academic).
- Recent-developments section is MEDIUM (forward-looking commentary).
