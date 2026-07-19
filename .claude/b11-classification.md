# B11 Classification — 99 `type: strategy` pages missing `edge_source:`

Generated 2026-07-19. Column meanings:
- **Class**: GUIDE | STRUCTURE | STRATEGY
- **Reason**: one-line rationale
- **B11**: `yes` = upgraded in Batch B11; `no` = still needs work or left as-is (GUIDE/STRUCTURE)

| # | Page (path relative to wiki/strategies/) | Class | Reason | B11 |
|---|------------------------------------------|-------|---------|-----|
| 1 | `5-percent-otm-put-overlay.md` | STRATEGY | Deployable crypto put-overlay with entry/exit/sizing rules and DVOL gating; clearly edge-seeking | yes |
| 2 | `algorithmic/black-litterman.md` | GUIDE | Portfolio-allocation framework / TradFi theory page; markets=[stocks,bonds]; no edge deployment logic | no |
| 3 | `algorithmic/cppi.md` | GUIDE | Portfolio-insurance framework; no specific alpha source; markets=[stocks,bonds,crypto] but no crypto entry rules | no |
| 4 | `algorithmic/portable-alpha.md` | GUIDE | Institutional overlay concept; markets=[stocks,bonds]; no crypto edge mechanism | no |
| 5 | `algorithmic/risk-budgeting.md` | GUIDE | Portfolio-construction methodology; markets=[stocks,bonds]; meta/reference not deployable strategy | no |
| 6 | `algorithmic/trend-following-cta.md` | STRATEGY | Deployable systematic trend-following; crypto-applicable with entry/sizing rules; multi-asset but has crypto relevance | yes |
| 7 | `arbitrage/arbitrage-backtesting-guide.md` | GUIDE | Methodology guide for backtesting arb strategies; companion reference not a deployable strategy | no |
| 8 | `arbitrage/arbitrage-correlation-matrix.md` | GUIDE | Portfolio-construction reference for combining arb strategies; no direct deployment | no |
| 9 | `arbitrage/arbitrage-live-performance.md` | GUIDE | Performance tracker / live monitoring reference; journal-style page | no |
| 10 | `arbitrage/arbitrage-monitoring-setup.md` | GUIDE | Technical setup guide with runnable code; companion infra page not a strategy | no |
| 11 | `arbitrage/arbitrage-parameter-cheatsheet.md` | GUIDE | Parameter/threshold reference across multiple arb strategies; no standalone deployment | no |
| 12 | `arbitrage/arbitrage-seasonality.md` | GUIDE | Seasonality reference across arb strategies; meta/analytical reference | no |
| 13 | `arbitrage/arbitrage-worked-examples.md` | GUIDE | Worked examples / case-study page; companion not a deployable strategy | no |
| 14 | `arbitrage/etf-arbitrage.md` | GUIDE | ETF creation-redemption arb; markets=[bonds]; equity/ETF framing, not crypto-deployable | no |
| 15 | `arbitrage/multi-venue-capital-management.md` | GUIDE | Capital logistics guide; explains how to manage capital across venues, not an entry/exit strategy | no |
| 16 | `arbitrage/nft-arbitrage.md` | STRATEGY | Crypto-native NFT floor/trait arb with entry logic; genuine edge-seeking | yes |
| 17 | `arbitrage/regulatory-arbitrage.md` | GUIDE | Jurisdictional/compliance reference; describes regulatory landscape not a trading strategy | no |
| 18 | `cash-secured-puts.md` | STRUCTURE | Options income structure; construction/payoff/greeks on Deribit; Wave 3 deliberate structure template — leave as-is | no |
| 19 | `combinations/alternative-data-alpha.md` | STRATEGY | Edge-seeking alt-data strategy with entry logic; markets=[stocks,crypto] but crypto-applicable | yes |
| 20 | `combinations/asymmetric-barbell.md` | STRATEGY | Deployable portfolio construction with convexity; crypto-applicable barbell approach | yes |
| 21 | `combinations/core-satellite-portfolio.md` | GUIDE | Meta portfolio-construction framework; no specific entry/exit rules; reference/methodology | no |
| 22 | `combinations/cross-asset-signals.md` | STRATEGY | Deployable intermarket signal system with crypto entry rules; genuine edge-seeking | yes |
| 23 | `combinations/expiration-and-rebalancing-flows.md` | STRATEGY | Structural-flow based strategy with entry timing; markets=[stocks,futures] but crypto-applicable concept | yes |
| 24 | `combinations/gamma-exposure-trading.md` | STRATEGY | Dealer GEX-based strategy with entry/exit logic; crypto-applicable via DVOL/Deribit | yes |
| 25 | `combinations/multi-strategy-portfolio.md` | GUIDE | Meta-portfolio construction methodology; describes how to combine strategies, not itself a strategy | no |
| 26 | `combinations/multi-timeframe-confluence.md` | STRATEGY | Deployable multi-TF entry system with specific confluence rules; markets=[crypto,forex] | yes |
| 27 | `combinations/regime-adaptive-strategy.md` | STRATEGY | Deployable regime-switching strategy with entry/exit per regime; markets=[crypto,futures] | yes |
| 28 | `combinations/risk-on-risk-off-framework.md` | GUIDE | Macro regime framework/reference; describes the RORO concept, no specific entry criteria | no |
| 29 | `combinations/stop-hunting-and-liquidity-sweeps.md` | STRATEGY | Entry strategy exploiting stop-hunt mechanics; markets=[forex,crypto,futures] | yes (B11-2) |
| 30 | `combinations/structural-forced-selling.md` | STRATEGY | Strategy exploiting forced-seller flows with entry triggers; markets=[stocks,bonds] — equity-framed; flag | yes (B11-2) |
| 31 | `combinations/trend-plus-tail-hedge.md` | STRATEGY | Deployable combination of trend following + tail hedge; markets=[futures] but crypto-applicable | yes (B11-2) |
| 32 | `combinations/volatility-targeting.md` | GUIDE | Vol-targeting is a sizing methodology (meta); describes how to size, not when to enter/exit | no |
| 33 | `conversion-reversal-arbitrage.md` | STRATEGY | Crypto options put-call parity arb with specific entry/exit; genuine edge-seeking on Deribit | yes (B11-2) |
| 34 | `credit-spread.md` | STRUCTURE | Options structure page; construction/payoff/greeks for bull-put/bear-call spreads on Deribit; Wave 3 — leave as-is | no |
| 35 | `delta-hedged-options.md` | STRATEGY | Volatility isolation via delta-hedging with specific entry/size/management rules; genuine strategy | yes (B11-2) |
| 36 | `fundamental-analysis/crack-spread.md` | GUIDE | Commodity refinery-margin spread; markets=[commodities]; out-of-crypto-scope reference | no |
| 37 | `fundamental-analysis/crush-spread.md` | GUIDE | Soybean processing-margin spread; markets=[commodities]; out-of-crypto-scope reference | no |
| 38 | `fundamental-analysis/news-trading.md` | STRATEGY | Event-driven news/catalyst trading with entry logic; markets=[stocks,forex,crypto] | yes (B11-2) |
| 39 | `fundamental-analysis/seasonal-spread-trading.md` | GUIDE | Commodity seasonal calendar reference; markets=[commodities]; out-of-scope for crypto | no |
| 40 | `fundamental-analysis/spark-spread.md` | GUIDE | Power generation margin spread; markets=[commodities]; out-of-scope | no |
| 41 | `long-call.md` | STRUCTURE | Long call is an options structure primitive; construction/payoff/greeks on Deribit; Wave 3 — leave as-is | no |
| 42 | `long-put.md` | STRUCTURE | Long put is an options structure primitive; construction/payoff/greeks on Deribit; Wave 3 — leave as-is | no |
| 43 | `options-income.md` | STRATEGY | Systematic options-income class with edge analysis, entry/exit/regime gating on Deribit; already has "## Edge Source" prose | yes (B11-2) |
| 44 | `options-premium-selling.md` | STRATEGY | Core short-vol crypto strategy with edge source prose already present; needs frontmatter fields | yes (B11-2) |
| 45 | `position-trading/carry-trade.md` | GUIDE | FX carry trade reference; markets=[forex]; crypto carry is covered by funding-rate-arbitrage and carry-with-tail-hedge | no |
| 46 | `position-trading/dollar-cost-averaging.md` | GUIDE | DCA accumulation methodology; not an edge-seeking strategy; reference/education | no |
| 47 | `premium-selling-systematic.md` | STRATEGY | Mechanical crypto premium-selling with DVOL gate, 16d, 35-DTE rules; fully deployable; already has edge prose | yes (B11-2) |
| 48 | `put-spread.md` | STRUCTURE | Bear put spread / vertical spread structure; construction/payoff/greeks on Deribit; Wave 3 — leave as-is | no |
| 49 | `quantitative/tail-risk-hedging.md` | STRATEGY | Crypto tail-hedge strategy with specific OTM put accumulation rules on Deribit; deployable | yes (B11-2) |
| 50 | `quantitative/vix-trading.md` | STRATEGY | Crypto vol trading (DVOL) with straddle/strangle entry logic; crypto-native reframe already done | yes (B11-2) |
| 51 | `ratio-calendar-spread.md` | STRUCTURE | Ratio calendar spread structure; construction/payoff/Greeks on Deribit; Wave 3 — leave as-is | no |
| 52 | `short-put-spread.md` | STRUCTURE | Bull put spread / put credit spread structure; construction/payoff/Greeks; Wave 3 — leave as-is | no |
| 53 | `tail-hedging.md` | STRATEGY | Tail-hedging discipline with specific OTM put strategy on Deribit; deployable; complements tail-risk-hedging | yes (B11-2) |
| 54 | `technical-analysis/0dte-trading.md` | STRATEGY | 0DTE crypto options trading with entry/sizing/management rules; deployable on Deribit | yes (B11-2) |
| 55 | `technical-analysis/backspread.md` | STRUCTURE | Backspread (ratio spread long side) is an options structure; construction/payoff/greeks; Wave 3 | no |
| 56 | `technical-analysis/bear-call-spread.md` | STRUCTURE | Bear call spread options structure; construction/payoff/Greeks; Wave 3 — leave as-is | no |
| 57 | `technical-analysis/bear-put-spread.md` | STRUCTURE | Bear put spread options structure; construction/payoff/Greeks; Wave 3 — leave as-is | no |
| 58 | `technical-analysis/box-spread.md` | STRUCTURE | Box spread (locked-in arbitrage structure); construction/payoff; Wave 3 — leave as-is | no |
| 59 | `technical-analysis/broken-wing-butterfly.md` | STRUCTURE | Broken-wing butterfly options structure; Wave 3 — leave as-is | no |
| 60 | `technical-analysis/bull-call-spread.md` | STRUCTURE | Bull call spread options structure; Wave 3 — leave as-is | no |
| 61 | `technical-analysis/bull-put-spread.md` | STRUCTURE | Bull put spread options structure; Wave 3 — leave as-is | no |
| 62 | `technical-analysis/butterfly-spread.md` | STRUCTURE | Butterfly spread options structure; Wave 3 — leave as-is | no |
| 63 | `technical-analysis/calendar-spread.md` | STRUCTURE | Calendar / time spread options structure; Wave 3 — leave as-is | no |
| 64 | `technical-analysis/cash-secured-put.md` | STRUCTURE | Cash-secured put options structure (duplicate of cash-secured-puts.md); Wave 3 — leave as-is | no |
| 65 | `technical-analysis/channel-breakout.md` | STRATEGY | Breakout strategy with specific channel-entry rules; generic but deployable in crypto | yes (B11-2) |
| 66 | `technical-analysis/christmas-tree-spread.md` | STRUCTURE | Christmas tree spread options structure; Wave 3 — leave as-is | no |
| 67 | `technical-analysis/collar.md` | STRUCTURE | Collar options structure; construction/payoff/greeks; Wave 3 — leave as-is | no |
| 68 | `technical-analysis/covered-call.md` | STRUCTURE | Covered call options structure; Wave 3 — leave as-is | no |
| 69 | `technical-analysis/diagonal-spread.md` | STRUCTURE | Diagonal spread options structure; Wave 3 — leave as-is | no |
| 70 | `technical-analysis/double-diagonal.md` | STRUCTURE | Double diagonal options structure; Wave 3 — leave as-is | no |
| 71 | `technical-analysis/gut-spread.md` | STRUCTURE | Gut spread options structure; Wave 3 — leave as-is | no |
| 72 | `technical-analysis/iron-butterfly.md` | STRUCTURE | Iron butterfly options structure; Wave 3 — leave as-is | no |
| 73 | `technical-analysis/iron-condor.md` | STRUCTURE | Iron condor options structure; Wave 3 — leave as-is | no |
| 74 | `technical-analysis/jade-lizard.md` | STRUCTURE | Jade lizard options structure; Wave 3 — leave as-is | no |
| 75 | `technical-analysis/macd-crossover.md` | STRATEGY | MACD crossover is a deployable signal-based strategy; crypto-applicable | yes (B11-2) |
| 76 | `technical-analysis/married-put.md` | STRUCTURE | Married put options structure (protective put variant); Wave 3 — leave as-is | no |
| 77 | `technical-analysis/opening-range-breakout.md` | STRATEGY | ORB is a deployable intraday entry system; crypto-applicable on session open | yes (B11-2) |
| 78 | `technical-analysis/options-selling.md` | STRATEGY | Deployable options-selling framework with entry/regime/exit for Deribit; genuine strategy | yes (B11-2) |
| 79 | `technical-analysis/options-strategies.md` | GUIDE | Overview/taxonomy of options strategies; no specific deployment rules; index-style reference | no |
| 80 | `technical-analysis/protective-put.md` | STRUCTURE | Protective put options structure; Wave 3 — leave as-is | no |
| 81 | `technical-analysis/rate-of-change.md` | STRATEGY | ROC momentum strategy with crossover entry rules; deployable in crypto | yes (B11-2) |
| 82 | `technical-analysis/ratio-spread.md` | STRUCTURE | Ratio spread options structure; Wave 3 — leave as-is | no |
| 83 | `technical-analysis/reverse-iron-condor.md` | STRUCTURE | Reverse iron condor options structure; Wave 3 — leave as-is | no |
| 84 | `technical-analysis/risk-reversal.md` | STRUCTURE | Risk reversal options structure; construction/payoff/greeks; Wave 3 — leave as-is | no |
| 85 | `technical-analysis/rsi-divergence.md` | STRATEGY | RSI divergence is a deployable reversal signal strategy; crypto-applicable | yes (B11-2) |
| 86 | `technical-analysis/seagull-option.md` | STRUCTURE | Seagull option structure; Wave 3 — leave as-is | no |
| 87 | `technical-analysis/short-straddle.md` | STRUCTURE | Short straddle options structure; Wave 3 — leave as-is | no |
| 88 | `technical-analysis/short-strangle.md` | STRUCTURE | Short strangle options structure; Wave 3 — leave as-is | no |
| 89 | `technical-analysis/straddle-strangle.md` | STRUCTURE | Straddle/strangle family overview structure page; Wave 3 — leave as-is | no |
| 90 | `technical-analysis/strangle.md` | STRUCTURE | Strangle options structure; Wave 3 — leave as-is | no |
| 91 | `technical-analysis/strip-strap.md` | STRUCTURE | Strip/strap options structure; Wave 3 — leave as-is | no |
| 92 | `technical-analysis/support-resistance-breakout.md` | STRATEGY | Deployable S/R breakout strategy with volume-confirmation rules | yes (B11-2) |
| 93 | `technical-analysis/synthetic-long.md` | STRUCTURE | Synthetic long/short is an options structure; construction/payoff/replication; Wave 3 — leave as-is | no |
| 94 | `technical-analysis/turtle-trading.md` | STRATEGY | Turtle system is a fully deployable trend-following strategy; crypto-native reframe done; high priority | yes (B11-2) |
| 95 | `technical-analysis/vertical-spread.md` | STRUCTURE | Vertical spread options structure (generic); Wave 3 — leave as-is | no |
| 96 | `technical-analysis/volatility-breakout.md` | STRATEGY | ATR/NR7 volatility breakout system with entry rules; deployable in crypto | yes (B11-2) |
| 97 | `technical-analysis/wheel-strategy.md` | STRUCTURE | Wheel options income structure (CSP + CC cycle); Wave 3 — leave as-is | no |
| 98 | `vix-calls.md` | STRATEGY | Crypto long-vol overlay with specific Deribit structures and entry/sizing logic; deployable | yes (B11-2) |
| 99 | `zero-dte-options.md` | STRATEGY | 0DTE overview + deployment structures; complements 0dte-trading.md; deployable | yes (B11-2) |

---

## Tally

| Class | Count |
|-------|-------|
| GUIDE | 25 |
| STRUCTURE | 40 |
| STRATEGY | 34 |

- **GUIDE pages (25)**: `algorithmic/black-litterman`, `algorithmic/cppi`, `algorithmic/portable-alpha`, `algorithmic/risk-budgeting`, `arbitrage/arbitrage-backtesting-guide`, `arbitrage/arbitrage-correlation-matrix`, `arbitrage/arbitrage-live-performance`, `arbitrage/arbitrage-monitoring-setup`, `arbitrage/arbitrage-parameter-cheatsheet`, `arbitrage/arbitrage-seasonality`, `arbitrage/arbitrage-worked-examples`, `arbitrage/etf-arbitrage`, `arbitrage/multi-venue-capital-management`, `arbitrage/regulatory-arbitrage`, `combinations/core-satellite-portfolio`, `combinations/multi-strategy-portfolio`, `combinations/risk-on-risk-off-framework`, `combinations/volatility-targeting`, `fundamental-analysis/crack-spread`, `fundamental-analysis/crush-spread`, `fundamental-analysis/seasonal-spread-trading`, `fundamental-analysis/spark-spread`, `position-trading/carry-trade`, `position-trading/dollar-cost-averaging`, `technical-analysis/options-strategies`

- **STRUCTURE pages (40)**: `cash-secured-puts`, `credit-spread`, `long-call`, `long-put`, `put-spread`, `ratio-calendar-spread`, `short-put-spread`, `technical-analysis/backspread`, `technical-analysis/bear-call-spread`, `technical-analysis/bear-put-spread`, `technical-analysis/box-spread`, `technical-analysis/broken-wing-butterfly`, `technical-analysis/bull-call-spread`, `technical-analysis/bull-put-spread`, `technical-analysis/butterfly-spread`, `technical-analysis/calendar-spread`, `technical-analysis/cash-secured-put`, `technical-analysis/christmas-tree-spread`, `technical-analysis/collar`, `technical-analysis/covered-call`, `technical-analysis/diagonal-spread`, `technical-analysis/double-diagonal`, `technical-analysis/gut-spread`, `technical-analysis/iron-butterfly`, `technical-analysis/iron-condor`, `technical-analysis/jade-lizard`, `technical-analysis/married-put`, `technical-analysis/protective-put`, `technical-analysis/ratio-spread`, `technical-analysis/reverse-iron-condor`, `technical-analysis/risk-reversal`, `technical-analysis/seagull-option`, `technical-analysis/short-straddle`, `technical-analysis/short-strangle`, `technical-analysis/straddle-strangle`, `technical-analysis/strangle`, `technical-analysis/strip-strap`, `technical-analysis/synthetic-long`, `technical-analysis/vertical-spread`, `technical-analysis/wheel-strategy`

- **STRATEGY pages upgraded in B11-1 (10)**: `5-percent-otm-put-overlay`, `algorithmic/trend-following-cta`, `arbitrage/nft-arbitrage`, `combinations/alternative-data-alpha`, `combinations/asymmetric-barbell`, `combinations/cross-asset-signals`, `combinations/expiration-and-rebalancing-flows`, `combinations/gamma-exposure-trading`, `combinations/multi-timeframe-confluence`, `combinations/regime-adaptive-strategy`

- **STRATEGY pages upgraded in B11-2 (24 — final batch)**: `combinations/stop-hunting-and-liquidity-sweeps`, `combinations/structural-forced-selling`, `combinations/trend-plus-tail-hedge`, `conversion-reversal-arbitrage`, `delta-hedged-options`, `fundamental-analysis/news-trading`, `options-income`, `options-premium-selling`, `premium-selling-systematic`, `quantitative/tail-risk-hedging`, `quantitative/vix-trading`, `tail-hedging`, `technical-analysis/0dte-trading`, `technical-analysis/channel-breakout`, `technical-analysis/macd-crossover`, `technical-analysis/opening-range-breakout`, `technical-analysis/options-selling`, `technical-analysis/rate-of-change`, `technical-analysis/rsi-divergence`, `technical-analysis/support-resistance-breakout`, `technical-analysis/turtle-trading`, `technical-analysis/volatility-breakout`, `vix-calls`, `zero-dte-options`

- **All 34 STRATEGY pages upgraded as of B11-2. No remaining STRATEGY pages with missing edge_source.**
