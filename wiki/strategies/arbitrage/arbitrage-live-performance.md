---
title: "Arbitrage Strategy Performance Tracker"
type: reference
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [arbitrage, risk-management, backtesting, strategy-development, meta]
aliases: ["Arb Performance", "Live Arb Tracker", "Arbitrage Returns"]
strategy_type: quantitative
timeframe: position|long-term
markets: [crypto, futures, options]
complexity: advanced
backtest_status: untested
related: ["[[arbitrage-overview]]", "[[arbitrage-opportunity-map]]", "[[strategy-monitoring]]", "[[failure-modes]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[arbitrage-parameter-cheatsheet]]", "[[crowding-indicators]]", "[[arbitrage-seasonality]]", "[[arbitrage-competitive-landscape]]"]
---

# Arbitrage Strategy Performance Tracker

Every return figure elsewhere in this wiki is theoretical, backtested, or historically reported. This page tracks **observed performance** of arbitrage strategies based on publicly available data, third-party reports, and observable market metrics. The goal: an agent (or human) should be able to look at this page and answer "is this strategy currently alive, dying, or dead?"

> **Methodology:** Returns below are derived from observable market data (funding rates, basis spreads, deal spreads) and published fund/index performance where available. They are NOT proprietary trading results. Actual performance will vary based on execution quality, fee tier, and capital deployed. See [[arbitrage-parameter-cheatsheet]] for cost assumptions.

> **Data vintage warning.** This is a *snapshot* page. The regime tables below are anchored to **April 2026**; market conditions move, so figures decay quickly. Re-run the data-source checks in [How to Update This Page](#how-to-update-this-page) before relying on any number. Nothing here is investment advice.

## How to Read This Page

Each strategy is scored against a simple, repeatable rubric so the page answers one question: **alive, dying, or dead?**

| Signal | What to look at | Interpretation |
|--------|-----------------|----------------|
| **Gross spread vs hurdle** | Gross return minus (risk-free + cost + counterparty premium) | If gross < hurdle, the strategy is structurally dead for that participant tier |
| **Net after costs** | Gross minus [[arbitrage-parameter-cheatsheet\|cost stack]] (fees, slippage, financing) | The only number that matters; retail and VIP tiers diverge sharply |
| **Sharpe trend** | Direction of the Sharpe over 2020→2026 | Falling = crowding/decay; cyclical = regime-driven, not permanent decay |
| **Crowding** | Capital chasing the trade (see [[crowding-indicators]]) | High crowding compresses spreads toward the hurdle |
| **Capacity tier** | Does the edge survive at the size you'd deploy? | Some edges exist only at retail size; others only at institutional size |

The hurdle rate in April 2026 is high: with the Fed funds rate at ~4.25%, any arb netting under ~6-7% is barely paying for its risk-free alternative plus counterparty risk — a recurring theme below.

---

## Current Market Regime (April 2026)

| Indicator | Value | Regime Signal |
|---|---|---|
| VIX | ~18 | Low-moderate volatility |
| BTC 30-day realized vol | ~45% | Moderate (down from 70%+ in Q1) |
| Crypto market sentiment | Cautiously bullish post-tariff uncertainty | Mixed carry/structural opportunity |
| Fed funds rate | ~4.25% | High risk-free rate = high hurdle for arb strategies |
| DeFi TVL | ~$120B | Moderate; recovered from 2022 lows |

**Regime implication per [[regime-matrix]]:** Carry strategies (funding arb, basis trade) moderately favorable. Structural arb (cross-exchange, ETF) neutral — volatility not high enough for large dislocations. Trend-following favored if tariff uncertainty creates directional moves.

---

## Strategy Performance Snapshot

### Crypto Carry Strategies

#### Funding Rate Arbitrage

| Metric | Current (April 2026) | Peak (Nov 2024) | Trough (Jun 2022) |
|---|---|---|---|
| BTC avg funding rate (8h) | 0.008-0.015% | 0.08-0.15% | -0.01 to -0.03% |
| Annualized carry (gross) | 9-16% APY | 88-164% APY | Negative |
| Estimated net carry (after fees) | 6-12% APY | 80-150% APY | Negative |
| Strategy viability | Marginal-Good | Excellent | Dead (inverted) |

**Data source:** Coinglass aggregated funding rates across Binance, OKX, Bybit, Hyperliquid.

**Interpretation:** Funding rate arb is *alive but compressed* in April 2026. Net carry of 6-12% APY barely exceeds risk-free rate (~4.25%) plus counterparty risk premium (~2-3%). Only viable with VIP-tier fees. Compare to Nov 2024 when gross carry exceeded 100% APY — that was the golden period.

**Trend:** Declining from Q1 2025 peak. Consistent with [[crowding-indicators|crowding]] — more capital chasing the trade compresses rates.

#### Cash-and-Carry (Futures Basis)

| Metric | Current | Q1 2025 | Q3 2022 |
|---|---|---|---|
| BTC quarterly basis (annualized) | 6-10% | 15-25% | 2-4% |
| ETH quarterly basis (annualized) | 5-8% | 12-20% | 1-3% |
| CME BTC futures basis | 5-7% | 10-15% | 3-5% |

**Interpretation:** Basis has normalized. Crypto basis is converging toward TradFi levels (~risk-free + small premium), suggesting the trade is becoming commoditized. CME basis consistently lower than offshore — reflects institutional capital arbitraging efficiently.

### Cross-Exchange Arbitrage

| Metric | Current (2026) | 2023 | 2020 |
|---|---|---|---|
| BTC/USDT cross-exchange spread (median) | 0.01-0.03% | 0.03-0.08% | 0.10-0.50% |
| Profitable spread frequency (>0.10%) | < 5 per day | 20-50 per day | 100+ per day |
| Estimated Sharpe (retail execution) | < 0.3 | 0.8-1.5 | 2.0+ |

**Interpretation:** Cross-exchange arb on major pairs is **effectively dead for retail**. Spreads have compressed to near-zero on liquid pairs. Profitable opportunities require sub-10ms execution (institutional infrastructure). Occasional spikes during volatility events (tariff announcements, exchange outages) still create brief windows.

**Where opportunities remain:** Altcoin pairs with thinner books, newly listed tokens, and CEX-DEX price gaps during DeFi events.

### Statistical Arbitrage / Pairs Trading

| Metric | Current | Historical Avg |
|---|---|---|
| Equity pairs (cointegrated, US large-cap) | Sharpe 0.3-0.8 | Sharpe 0.5-1.5 |
| Crypto pairs (BTC/ETH, major alts) | Sharpe 0.5-1.2 | Sharpe 1.0-2.0 |
| Mean reversion half-life (typical pair) | 8-15 days | 5-20 days |
| Cointegration stability (12-month pass rate) | ~40% of pairs | ~50% |

**Interpretation:** Equity stat arb is increasingly crowded (Sharpe declining decade-over-decade). Crypto pairs remain more attractive due to less sophisticated competition, but cointegration relationships are less stable (pairs break more often due to narrative-driven crypto regime shifts).

### Merger Arbitrage

| Metric | 2026 YTD | 2025 | 2024 |
|---|---|---|---|
| Average deal spread at announcement | 6-10% annualized | 8-12% | 10-15% |
| Deal completion rate | ~90% | ~88% | ~85% |
| Estimated Sharpe | 0.5-0.8 | 0.6-1.0 | 0.8-1.2 |
| Active US deals > $1B | 15-25 | 30-40 | 25-35 |

**Data source:** Bloomberg M&A monitor, public deal announcements.

**Interpretation:** Merger arb spreads have tightened as more capital enters the space. Deal activity moderate. Regulatory risk remains elevated (FTC/DOJ scrutiny of tech M&A). Strategy is alive but returns are converging toward risk-free + modest spread.

### Volatility Arbitrage

| Metric | Current | Historical Avg |
|---|---|---|
| VRP (implied - realized, SPX 30-day) | 2-4 vol points | 3-5 vol points |
| VRP Sharpe (systematic short vol) | 0.3-0.6 | 0.4-0.8 |
| Dispersion (index IV - avg component IV) | 2-3 vol points | 3-6 vol points |

**Interpretation:** Volatility risk premium is compressed but positive. Short-vol strategies remain modestly profitable but the memory of [[flash-crashes|Volmageddon]] keeps AUM below pre-2018 levels, which paradoxically sustains some edge.

### DeFi / On-Chain Arbitrage

| Metric | Current | Peak (DeFi Summer 2021) |
|---|---|---|
| DEX-CEX spread frequency (>0.1%) | 10-30 per day (altcoins) | 100+ per day |
| Flash loan arb revenue (Ethereum) | $1-5M/month ecosystem-wide | $20-50M/month |
| MEV extraction (total, Ethereum) | $10-30M/month | $50-100M/month |
| Cross-chain spread frequency | Moderate (new L2s create gaps) | Low (fewer chains) |

**Interpretation:** On-chain arb revenue has declined significantly from DeFi Summer peaks but remains meaningful. New L2 launches (Blast, Mode, Scroll, Linea) periodically create fresh cross-chain opportunities. MEV is increasingly dominated by sophisticated searchers using [[mev-strategies|Flashbots]] infrastructure.

---

## Strategy Viability Summary (April 2026)

| Strategy | Gross Return | Net After Costs | Sharpe | Crowding | Verdict |
|---|---|---|---|---|---|
| [[funding-rate-arbitrage]] | 9-16% APY | 6-12% APY | 0.6-1.0 | High | Alive but compressed. VIP fees required |
| [[cash-and-carry]] | 6-10% APY | 4-8% APY | 0.5-0.8 | Medium-High | Barely above risk-free. Commoditized |
| [[cross-exchange-arbitrage]] (BTC) | < 2% APY (retail) | Near zero | < 0.3 | Extreme | Dead for retail. HFT-only |
| [[cross-exchange-arbitrage]] (alts) | 5-15% APY | 3-10% APY | 0.5-1.0 | Medium | Alive on illiquid pairs |
| [[pairs-trading]] (crypto) | 10-20% | 7-15% | 0.5-1.2 | Medium | Viable with good pair selection |
| [[pairs-trading]] (equities) | 5-12% | 3-8% | 0.3-0.8 | High | Crowded. Factor models needed |
| merger-arbitrage | 6-10% | 5-8% | 0.5-0.8 | Medium | Alive. Spread = risk-free + regulatory risk |
| [[volatility-arbitrage]] | Variable | 3-8% | 0.3-0.6 | Medium | VRP positive but thin |
| [[cross-chain-arbitrage]] | 10-25% APY | 7-18% APY | 0.8-1.5 | Medium | Best current crypto arb opportunity |
| [[flash-loan-arbitrage]] | Variable | Variable | High variance | Extreme | Dominated by sophisticated searchers |
| [[staking-yield-arbitrage]] | 5-10% APY | 3-7% APY | 0.5-0.8 | Medium | Steady but low. DeFi risk premium |

---

## Historical Return Decay

Returns for most arb strategies decline over time as competition increases. Tracking this decay reveals which strategies are dying:

| Strategy | 2020 Sharpe | 2022 Sharpe | 2024 Sharpe | 2026 Sharpe | Decay Rate |
|---|---|---|---|---|---|
| Cross-exchange (BTC) | 2.0+ | 1.0-1.5 | 0.5-0.8 | < 0.3 | ~35%/year |
| Funding rate arb | N/A | 0.5-1.0 | 1.5-2.5 | 0.6-1.0 | Cyclical (regime-dependent) |
| Stat arb (equity) | 1.0-1.5 | 0.5-1.0 | 0.4-0.8 | 0.3-0.8 | ~10%/year |
| Merger arb | 1.0-1.5 | 0.8-1.2 | 0.8-1.2 | 0.5-0.8 | ~5%/year |
| Cross-chain arb | N/A | N/A | 1.0-2.0 | 0.8-1.5 | ~15%/year (new, declining) |

**Key insight:** Funding rate arb Sharpe is **cyclical, not linearly decaying** — it spikes in bull markets and dies in bear markets. This is because the edge source is structural (leverage demand), not behavioral (which gets arbitraged away permanently). See [[edge-taxonomy]] for why this matters.

---

## Cross-Strategy Patterns

Reading the tables above together yields a few durable principles, independent of the exact April-2026 numbers:

1. **Decay is fastest for latency/structural edges.** Cross-exchange arb on liquid pairs (a pure speed edge) decayed ~35%/year and is now dead for retail. Anyone whose only advantage is "the spread exists" loses to faster infrastructure. See [[edge-taxonomy]].
2. **Behavioral/structural edges decay slower or cyclically.** Merger arb (~5%/year) and stat arb (~10%/year) decay gently; funding-rate arb is *cyclical*, not decaying, because it rents out leverage demand rather than correcting a one-time mispricing.
3. **The hurdle rate is a regime variable.** A high risk-free rate (~4.25% in 2026) silently kills low-spread arbs by raising the bar every trade must clear. Many strategies that "worked" in the zero-rate era are now net-negative after the hurdle.
4. **The frontier migrates to where competition is least sophisticated.** As majors get arbitraged flat, edge persists on altcoin pairs, new L2s, and novel mechanisms (cross-chain arb is the current "best crypto arb"). The opportunity set is always at the edge of capacity and tooling.
5. **Crowding is the leading indicator of decay.** Watch capital inflow ([[crowding-indicators]]) before Sharpe falls; rising AUM in a strategy reliably precedes spread compression.

### Edge-Source Map for Arb Strategies

| Strategy | Dominant edge source ([[edge-taxonomy]]) | Decay profile |
|----------|------------------------------------------|---------------|
| Cross-exchange (BTC) | Latency / structural | Fast, near-complete |
| Funding-rate arb | Risk-bearing (leverage demand) | Cyclical, regime-driven |
| Cash-and-carry | Structural (basis) | Gradual commoditization |
| Pairs / stat arb | Statistical / behavioral | Gradual; pair-dependent |
| Merger arb | Risk-bearing (deal/regulatory risk) | Slow |
| Volatility arb | Risk-bearing (variance risk premium) | Slow; AUM-constrained |
| Cross-chain / MEV | Structural + latency | New, declining as tooling matures |

---

## How to Update This Page

This page should be refreshed **monthly** or after significant market regime changes. Data sources for each strategy:

| Strategy | Primary Data Source | How to Check |
|---|---|---|
| Funding rate arb | Coinglass.com/FundingRate | Check 30-day avg across exchanges |
| Cash-and-carry | Coinglass.com/FuturesBasis, CME QuikStrike | Check annualized basis for BTC/ETH quarterly futures |
| Cross-exchange | Manual sampling or Tardis.dev historical | Measure BTC/USDT bid-ask cross-venue spread |
| Pairs / stat arb | AQR factor returns, Ken French data | Check rolling factor Sharpes |
| Merger arb | Bloomberg M&A, MergerArb.com | Check avg spread and deal count |
| Vol arb | CBOE VIX, SpotGamma | IV-RV spread on SPX 30-day |
| Cross-chain | DefiLlama bridge volume, manual L2 price checks | Compare token prices across DEXs on different chains |
| DeFi / MEV | Flashbots transparency dashboard, EigenPhi | Monthly MEV extraction totals |

## Sources

- Coinglass (funding rate, basis, open interest data)
- CME Group (futures basis, volume data)
- CBOE (VIX, volatility surface data)
- Bloomberg M&A monitor (deal spreads, completion rates)
- Flashbots transparency dashboard (MEV extraction)
- DefiLlama (DeFi TVL, bridge volume)
- AQR Factor Returns (equity factor performance)
- General market knowledge; no proprietary trading results — all figures are observable-market-derived and indicative.

## Related

- [[arbitrage]] — strategy family overview
- [[arbitrage-overview]] — catalog of arbitrage strategies
- [[arbitrage-opportunity-map]] — where opportunities currently sit
- [[arbitrage-parameter-cheatsheet]] — cost and parameter assumptions
- [[arbitrage-competitive-landscape]] — who is competing in each strategy
- [[arbitrage-seasonality]] — calendar effects on arb spreads
- [[strategy-monitoring]] — monitoring framework
- [[crowding-indicators]] — leading indicator of decay
- [[edge-taxonomy]] — why some edges decay and others don't
- [[regime-matrix]] — which strategies fit which regime
- [[failure-modes]] — how arb strategies break
- [[funding-rate-arbitrage]] · [[cash-and-carry]] · [[cross-exchange-arbitrage]] · [[pairs-trading]] · merger-arbitrage · [[volatility-arbitrage]] · [[cross-chain-arbitrage]] · [[flash-loan-arbitrage]] · [[staking-yield-arbitrage]] — individual strategy pages
- carbon-credit-arbitrage · [[multi-dvn-bridge-config-arbitrage]] — specialist arbs tracked elsewhere
