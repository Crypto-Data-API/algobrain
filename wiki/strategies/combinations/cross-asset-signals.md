---
title: Cross-Asset Signals
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: review
tags: [combinations, alpha-edge, intermarket-analysis, cross-asset, macro, correlation, regime-detection, crypto]
strategy_type: hybrid
markets: [crypto, forex, bonds, commodities]
complexity: advanced
backtest_status: untested
related: ["[[regime-adaptive-strategy]]", "[[gamma-exposure-trading]]", "[[contrarian-extremes]]", "[[funding-rate-arbitrage]]", "[[cryptodataapi]]", "[[dvol]]"]

# Edge characterization
edge_source: [informational, analytical]
edge_mechanism: "Cross-asset traders see the full chain of capital flows (bonds → credit → equities → crypto) before silo-focused traders; the counterparty is the crypto-only participant who is blindsided by a DXY break or credit-spread widening that the multi-asset view telegraphed days earlier."

# Data and infrastructure requirements
data_required: [ohlcv-daily, funding-rates, open-interest, fear-greed-index, volatility-regime, on-chain-flows]
min_capital_usd: 10000
capacity_usd: 500000000
crowding_risk: medium

# Performance expectations
expected_sharpe: 0.8
expected_max_drawdown: 0.20
breakeven_cost_bps: 30

# Kill criteria
kill_criteria: |
  - rolling 6-month win rate on DXY-crypto divergence setups drops below 45%
  - macro-crypto correlation regime breaks (DXY-BTC correlation near 0 for > 90 days)
  - drawdown > 15% in cross-asset book

---

# Cross-Asset Signals

## Edge source

**Informational** and **analytical**. See [[edge-taxonomy]].

The edge is panoramic information: by monitoring bonds, credit, DXY, VIX, and crypto funding simultaneously, the cross-asset trader sees the transmission mechanism between markets before single-silo participants do. Bonds and credit typically lead equities by 3–7 days; forex (DXY, JPY carry) leads crypto in risk-off regimes by 1–3 days. The counterparty is the crypto-native participant running stops at technical levels who is unaware of the DXY break or credit-spread widening already in progress.

**Crypto-specific relationships with documented relevance:**
- **DXY vs BTC**: −0.5 to −0.8 correlation in risk-off regimes; DXY breaks above resistance → BTC weakness follows within 1–5 days
- **BTC perp funding rate**: >+0.05%/8h is the crypto equivalent of crowded equity longs; combine with DXY strength for a high-conviction short
- **VIX term structure backwardation**: precedes risk-off crypto drawdowns; the signal is often visible in crypto DVOL structure before the spot price moves

## Null hypothesis

If cross-asset correlations are noise and not causally linked, any observed divergence-to-convergence pattern is coincidence. The strategy's Sharpe would be ≈ 0 net of costs, and out-of-sample win rates would be near 50%. The strength of the case: DXY-BTC correlation during the 2022 bear market was −0.75, and the DXY breakouts at 104 and 107 predicted BTC legs lower with <48h lag, consistently.

## The Edge

Markets are connected, but most traders operate in silos. The forex trader watches currency pairs. The crypto trader watches Bitcoin. The equity trader watches the S&P. Each ignores the signals screaming from adjacent asset classes -- signals that frequently predict moves in their own market before they happen. This strategy operationalizes [[john-murphy]]'s [[intermarket-analysis]] framework — that bonds, currencies, [[commodities]], and stocks move in an interconnected chain — into actionable trading signals.

The US dollar strengthens and crypto traders are blindsided by the selloff that bond traders saw coming a week ago. Credit spreads widen and equity traders are caught long as the risk-off wave hits stocks 3-5 days after it hit high-yield bonds. Options flow turns aggressively bearish on a single stock and the price does not drop -- yet. It will.

The edge: by monitoring signals across asset classes, you trade with a panoramic view while your competitors stare through a keyhole. Divergences between asset classes are the highest-conviction setups in all of trading because they represent a temporary mispricing that MUST resolve.

## Why It Persists

1. **Specialization creates silos** -- bond traders do not watch crypto. Crypto traders do not watch credit spreads. Each market has its own ecosystem of analysts, tools, and media. Cross-pollination is rare
2. **Different settlement and trading hours** -- bonds close at 3pm ET, equities at 4pm, crypto trades 24/7, forex opens Sunday. Dislocations persist because the markets literally cannot arbitrage each other in real-time
3. **Institutional mandates** -- a bond fund cannot buy equities even if the signal says "risk on." A crypto fund cannot short Treasury futures. Mandate constraints prevent capital from flowing to resolve the divergence quickly
4. **Complexity** -- processing signals from 6+ asset classes simultaneously requires a mental model that most traders never build. The learning curve is steep and the payoff is delayed
5. **Noise vs. signal** -- correlations shift between regimes. DXY-crypto correlation was -0.7 in 2022 but -0.3 in 2024. Identifying when a cross-asset signal is active requires regime awareness from [[regime-adaptive-strategy]]

## How to Implement

### The Cross-Asset Dashboard

Build or subscribe to a dashboard tracking these key relationships:

| Signal | Relationship | Trading Implication |
|---|---|---|
| **DXY (Dollar Index) ↔ Crypto** | Inverse correlation (~-0.5 to -0.8) | DXY breaks above resistance → short crypto. DXY breaks down → long crypto |
| **10Y Treasury Yield ↔ Equity Sectors** | Rising yields → financials outperform, growth/tech underperform | 10Y yield breakout above key level → rotate from tech to financials |
| **VIX Term Structure ↔ Market Regime** | Contango (VIX < VIX futures) = calm. Backwardation (VIX > futures) = fear | Backwardation → reduce equity exposure, buy puts, tighten stops |
| **Credit Spreads (HY-IG) ↔ Risk Assets** | Widening spreads = risk-off incoming | HY spread expansion → fade equity rallies, reduce crypto exposure |
| **Funding Rates ↔ Crypto Spot** | Extreme positive funding = longs overleveraged | Funding > 0.1%/8hr → expect spot correction within 1-3 days |
| **Options Flow ↔ Stock Direction** | Unusual call/put volume predicts moves 1-5 days ahead | Large put sweeps on SPY → hedge or reduce equity longs |
| **Copper/Gold Ratio ↔ Economic Growth** | Rising = growth expectations up. Falling = recession fear | Ratio declining → defensive positioning, long [[gold]] |
| **JPY ↔ Risk Sentiment** | Yen strengthens during risk-off (safe haven flows) | USD/JPY dropping sharply → risk-off incoming for equities |

### Trading Divergences

The highest-alpha setup occurs when one asset class has moved but another has not yet reacted:

1. **Identify the divergence** -- bonds are selling off (yields rising) but equities are flat or up. Credit spreads are widening but SPX has not dropped
2. **Determine which market is "right"** -- typically the less-manipulated, more-institutional market leads. Bonds lead stocks. Credit leads equity. Forex leads crypto
3. **Position for convergence** -- fade the lagging market in the direction the leading market has already moved
4. **Set a time limit** -- if the divergence does not resolve within 5-10 trading days, the signal may be invalid. Cut the position

### Regime-Based Signal Weighting

Not all cross-asset signals work all the time. Weight them by regime:

- **Risk-on regime** (VIX < 15, credit spreads tight, DXY weak): equity momentum and crypto signals dominate. Bond signals less relevant
- **Risk-off regime** (VIX > 25, spreads widening, DXY strong): bond and credit signals dominate. Ignore bullish equity technicals
- **Transitional regime** (mixed signals): reduce size, trade only the highest-conviction divergences

## Example Setup

**DXY-Crypto divergence trade -- February 2025:**

1. DXY breaks above 107 (key resistance), rallying on strong jobs data. Signal: dollar strength = crypto weakness incoming
2. BTC is still trading at $95,000, flat on the day. Crypto market has not yet reacted to the dollar move
3. Funding rates on BTC perpetual futures: +0.08%/8hr -- longs are overleveraged (confirming signal from another cross-asset indicator)
4. VIX term structure flips to mild backwardation -- risk-off regime beginning
5. **Confluence**: DXY strong (bearish crypto) + high funding (bearish crypto) + VIX backwardation (risk-off) = triple cross-asset confirmation
6. Short BTC at $95,000. Stop at $97,500 (above recent swing high). Target: $85,000 (prior support)
7. Over the next 10 days, BTC drops to $86,000 as the dollar rally compresses risk assets. Funding rates normalize, confirming the deleveraging
8. Close at $86,000. Risk: $2,500. Reward: $9,000. R:R = 1:3.6

## Risk Management

- **Correlation is not constant** -- the DXY-crypto relationship can decouple for weeks during idiosyncratic crypto events (ETF approval, protocol hack, regulatory news). Always check whether the correlation is active before trading it
- **Leading indicators can be early** -- bonds may signal risk-off 2 weeks before equities react. Being early feels the same as being wrong. Use stop losses calibrated to the lagging market's technicals, not the leading market's signal
- **Do not over-diversify signals** -- 3-4 high-quality cross-asset relationships are sufficient. Monitoring 20+ creates noise and analysis paralysis
- **Position sizing**: 2-3% risk per divergence trade. These setups are high-probability but not immediate -- expect 3-10 day holding periods
- **Beware of crowded cross-asset trades** -- the DXY-crypto inverse trade is increasingly well-known. When a trade becomes consensus, the edge erodes. Seek less-obvious relationships (copper/gold, JPY carry, credit spreads)
- **Build the dashboard before you need it** -- in a crisis, you will not have time to set up cross-asset monitoring. Have alerts pre-configured for key levels on DXY, 10Y yield, VIX, and HY spreads via [[trading-platforms]] like TradingView or Bloomberg

## Real-World Examples

- **March 2023 banking crisis** -- credit spreads blew out 3 days before SVB's stock collapse. Traders monitoring HY spreads exited financials before the crash hit equity screens
- **2022 crypto winter** -- the DXY rally from 95 to 114 (20% surge) preceded and caused BTC's decline from $48,000 to $16,000. Every major DXY resistance breakout corresponded to a BTC leg lower. Cross-asset traders were short crypto the entire way down
- **Japan carry trade unwind (Aug 2024)** -- USD/JPY crashed from 162 to 142 as the [[bank-of-japan|BOJ]] hiked rates. The yen carry trade unwound, forcing liquidation across global equities. Forex traders saw the signal days before the Nikkei crashed 12%
- **VIX backwardation and 2020 crash** -- VIX term structure flipped to backwardation on Feb 24, 2020 -- a week before the S&P's fastest 30% decline in history. Traders who respected the signal exited equities and bought puts with perfect timing
- **Funding rate extremes in crypto** -- BTC funding rates hit +0.15%/8hr in November 2024 (extreme long crowding). Spot price corrected 15% within 4 days as overleveraged longs were liquidated

The unifying principle: no market moves in isolation. Capital flows between asset classes create a chain of cause and effect. Reading that chain is the meta-skill that separates strategists from speculators.

## Capacity limits

The strategy itself is signal generation, not a stand-alone position book — it is applied on top of directional or swing-trading instruments. Capacity is determined by the underlying instrument. For BTC perp trades sized on cross-asset signals, $500M+ is feasible before market impact. For altcoin applications of the same framework, capacity is $1M–$20M.

## What kills this strategy

1. **Correlation regime breaks** — the DXY-BTC relationship is not permanent; in idiosyncratic crypto regimes (ETF approval, regulatory shock), macro signals are overridden by crypto-specific flows.
2. **Being early** — leading indicators can be 2–3 weeks early; a DXY rally that eventually causes BTC weakness may first see BTC rally on crypto-specific news.
3. **Crowded cross-asset trades** — when DXY-crypto inverse is consensus, its predictive power diminishes as everyone pre-positions.
4. **Data staleness** — using weekly correlation estimates that have regime-shifted is a silent killer.

## Kill criteria (numeric)

*(From frontmatter — duplicated here for reference)*
- Rolling 6-month win rate on DXY-crypto divergence setups < 45%
- DXY-BTC correlation near 0 for > 90 days (regime break)
- Drawdown > 15% in cross-asset book

## Getting the Data (CryptoDataAPI)

- `GET /api/v1/regimes/current` — macro regime (risk-on / risk-off classification)
- `GET /api/v1/sentiment/macro` — macro sentiment composite
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — perp funding (crowding signal)
- `GET /api/v1/volatility/regime/score` — vol-stress composite

Full catalog: [[cryptodataapi-regimes]], [[cryptodataapi-derivatives]].
