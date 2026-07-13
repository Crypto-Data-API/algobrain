---
title: "Arbitrage Parameter Cheatsheet"
type: strategy
created: 2026-04-20
updated: 2026-06-20
status: excellent
tags: [arbitrage, execution, quantitative, risk-management, backtesting]
aliases: ["Arb Parameters", "Arbitrage Thresholds", "Arb Entry Triggers"]
strategy_type: quantitative
timeframe: scalp|intraday|swing|position
markets: [crypto, stocks, futures, options, forex]
complexity: advanced
backtest_status: untested
related: ["[[arbitrage-overview]]", "[[arbitrage-opportunity-map]]", "[[transaction-cost-modeling]]", "[[fees]]", "[[funding-rate-arbitrage]]", "[[cross-exchange-arbitrage]]", "[[pairs-trading]]", "[[statistical-arbitrage]]", "[[cash-and-carry]]", "[[volatility-arbitrage]]", "[[exchange-api-reference]]"]
---

# Arbitrage Parameter Cheatsheet

Concrete entry thresholds, exit triggers, and position sizing parameters for every arbitrage strategy in the wiki. Individual strategy pages describe *how* each trade works; this page answers **"at what exact number do I pull the trigger?"** with all costs baked in.

All thresholds assume **retail/prosumer fee tiers** (not institutional). If you have VIP-level fees, your minimum viable thresholds are lower. See [[fees]] for tier breakdowns by exchange.

> **Warning:** These parameters are calibrated to market conditions as of early-to-mid 2026. Arbitrage thresholds drift as competition increases, fee structures change, and market microstructure evolves. Treat these as starting points for your own calibration, not as permanent constants.

This page is the threshold companion to the methodology pages: [[arbitrage-backtesting-guide]] (how to validate these numbers honestly), [[transaction-cost-modeling]] (the cost stack the thresholds must clear), and [[arbitrage-overview]] / [[arbitrage]] (the strategy family). Every "minimum spread" below is fundamentally `cost_stack + safety_margin` — see [[limits-to-arbitrage]] for why that floor exists at all.

## Quick index — minimum trigger by strategy

The single number that gates each trade, with the binding constraint. Click through for the detailed parameter tables below and the strategy pages for mechanics.

| Strategy | Primary trigger | Binding constraint | Section |
|---|---|---|---|
| [[cross-exchange-arbitrage]] | Spread > 0.15% (BTC) / 0.30% (alts) | Round-trip [[fees]] + [[slippage]] | [Pure](#pure--deterministic-arbitrage) |
| [[triangular-arbitrage]] | Circular profit > 0.06% | Three taker fees, <500ms window | [Pure](#pure--deterministic-arbitrage) |
| [[cash-and-carry]] | Annualized basis > 8% APR | Risk-free + [[counterparty-risk]] | [Pure](#pure--deterministic-arbitrage) |
| [[funding-rate-arbitrage]] | Funding > 0.01%/8h (~11% APY) | Fees + risk-free + exchange risk | [Pure](#pure--deterministic-arbitrage) |
| [[pairs-trading]] | \|z\| > 2.0 entry | Cointegration p < 0.05, half-life | [Statistical](#statistical--quantitative-arbitrage) |
| [[statistical-arbitrage]] | \|z\| > 1.5 residual | Market-neutrality, [[transaction-cost-modeling\|turnover cost]] | [Statistical](#statistical--quantitative-arbitrage) |
| [[volatility-arbitrage]] | IV-RV > 3 vol pts | Gamma/vega limits, hedge cost | [Volatility](#volatility--options-arbitrage) |
| merger-arbitrage | Annualized spread > 8% | Deal-break downside gap | [Event-Driven](#event-driven-arbitrage) |
| [[flash-loan-arbitrage]] | Profit > 2× gas | Gas, MEV competition | [DeFi](#defi--crypto-native-arbitrage) |
| Staking / LST | Yield spread > 3% or discount > 0.5% | Smart-contract + [[depeg-risk]] | [DeFi](#defi--crypto-native-arbitrage) |

---

## Pure / Deterministic Arbitrage

### Cross-Exchange Arbitrage

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum spread (BTC/USDT)** | > 0.15% | Covers ~0.10% round-trip fees (retail) + 0.03% slippage + margin of safety |
| **Minimum spread (altcoins)** | > 0.30% | Wider spreads needed: thinner books, higher slippage, withdrawal delays |
| **Order book depth check** | Spread must exist at ≥ $5,000 depth | Prevents triggering on phantom liquidity |
| **Maximum position per trade** | ≤ 10% of thinnest side's book depth | Minimizes [[market-impact]] |
| **Withdrawal time budget** | Include in spread calc as opportunity cost | ETH mainnet ~12 min, Solana ~0.4s, BTC ~60 min |
| **Entry order type** | LIMIT_MAKER on both sides, or IOC on taker side | Guarantees maker fee on at least one leg |
| **Kill threshold** | Close if spread inverts or narrows below cost within 30s | Prevents holding a losing arb |

**Minimum viable spread formula:**
```
min_spread = maker_fee_A + taker_fee_B + expected_slippage_A + expected_slippage_B + withdrawal_fee + gas_fee + safety_margin
```

Example (BTC, Binance VIP0 → Coinbase):
```
0.10% + 0.60% + 0.01% + 0.02% + ~$5 equiv + $0 + 0.05% = ~0.78% minimum
```
At retail Coinbase fees, cross-exchange BTC arb requires nearly 1% spread — which is rare. This is why fee tier optimization matters enormously.

### Triangular Arbitrage

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum circular profit** | > 0.06% (3 × 0.02% taker fee) | Three legs, each paying taker fee |
| **Execution window** | < 500ms for all three legs | Beyond this, prices have moved |
| **Maximum notional** | ≤ $10,000 per loop (typical) | Limited by thinnest order book in the triangle |
| **Pairs to monitor** | Top 20 triangles by combined volume | Focus liquidity where books are deepest |
| **Minimum book depth** | All three legs must show ≥ $2,000 at quoted price | Prevents hitting air pockets |

**Profitability formula:**
```
profit = (bid_C / ask_A × 1/ask_B) - 1 - (3 × taker_fee)
```
Where A→B→C→A is the triangle. Positive = executable arb.

### Cash-and-Carry (Crypto Futures Basis)

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum annualized basis** | > 8% APR | Must beat risk-free rate (~5%) + fees + counterparty risk premium |
| **Entry basis (quarterly futures)** | > 2% for 90-day contract | Equivalent to ~8% annualized |
| **Exit trigger** | Basis narrows to < 1% annualized OR < 7 days to expiry | Basis convergence accelerates near expiry |
| **Position sizing** | ≤ 25% of portfolio per exchange | [[counterparty-risk]] diversification |
| **Hedge ratio** | 1:1 spot-to-futures notional, rebalance if drift > 2% | Maintain delta neutrality |

### Funding Rate Arbitrage

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum funding rate (8h)** | > 0.01% per period (~11% APY) | Must cover: fees (~0.02% entry+exit), opportunity cost (~5% risk-free), counterparty premium |
| **Attractive funding rate** | > 0.03% per period (~33% APY) | Strong signal; historically persistent for days-weeks in bull markets |
| **Exit trigger** | Trailing 24h avg funding < 0.005% (~5.5% APY) | Below risk-free rate after costs |
| **Emergency exit** | Funding inverts (goes negative) for 2+ consecutive periods | Bleed accelerates; exit within 1 funding cycle |
| **Max per-exchange allocation** | 20-30% of arb portfolio | Recall [[ftx]] — exchange risk is real |
| **Rebalance trigger** | Spot/perp notional diverges > 3% | Drift erodes delta neutrality |
| **Leverage on short perp** | 1x (fully collateralized) | Higher leverage = liquidation risk in flash moves |

**Minimum viable funding rate formula (per 8h period):**
```
min_rate = (entry_fee + exit_fee) / expected_holding_periods + risk_free_rate / (3 × 365) + counterparty_premium / (3 × 365)
```

Example (Binance VIP0, 30-day hold):
```
(0.10% + 0.10%) / 90 periods + 5% / 1095 + 2% / 1095 = 0.0022% + 0.0046% + 0.0018% = ~0.0086% per 8h
```
So any rate above ~0.01% per 8h is marginally profitable at retail fees.

**Hyperliquid adjustment:** Funding is hourly, not 8-hourly. Minimum rate = `min_8h_rate / 8 ≈ 0.00125%` per hour.

---

## Statistical / Quantitative Arbitrage

### Pairs Trading (Cointegration-Based)

| Parameter | Value | Rationale |
|---|---|---|
| **Cointegration test** | Engle-Granger or Johansen p-value < 0.05 | Must establish statistical relationship before trading |
| **Lookback for cointegration test** | 252 trading days (1 year) | Balances recency with statistical power |
| **Z-score entry (long spread)** | z < -2.0 | Spread is 2 standard deviations below mean — historically reverts ~95% of the time |
| **Z-score entry (short spread)** | z > +2.0 | Mirror of above |
| **Z-score exit** | |z| < 0.5 (profit target) OR |z| > 3.5 (stop loss) | Take profit near mean; stop loss if divergence accelerates |
| **Z-score stop loss** | |z| > 4.0 (hard stop) | Relationship may be breaking — cointegration failure |
| **Hedge ratio recalculation** | Every 21 trading days (monthly) | Ratio drifts over time; Kalman filter is more adaptive alternative |
| **Maximum holding period** | 20 trading days | If it hasn't reverted in a month, the relationship may have changed |
| **Minimum half-life** | > 5 days, < 60 days | Too fast = can't capture; too slow = capital tied up |
| **Position size** | 2% risk per pair, max 5 pairs simultaneously | Pairs can correlate in stress — see [[strategy-correlation-matrix]] |

**Half-life formula (Ornstein-Uhlenbeck):**
```
half_life = -ln(2) / ln(β)
```
Where β is the AR(1) coefficient of the spread. See [[ornstein-uhlenbeck]].

### Statistical Arbitrage (Basket/Factor)

| Parameter | Value | Rationale |
|---|---|---|
| **Universe** | Top 500 most liquid stocks or top 100 crypto by volume | Liquidity is non-negotiable for stat arb |
| **Factor model** | PCA with 5-15 components, or Fama-French + momentum | Residual returns after removing systematic factors |
| **Entry z-score (residual)** | |z| > 1.5 | Less extreme than pairs — diversification across many names compensates |
| **Exit z-score** | |z| < 0.25 | Close to mean reversion |
| **Stop loss** | |z| > 3.0 or 5% loss on individual name | Hard limit to prevent blow-up |
| **Gross exposure** | ≤ 200% (100% long + 100% short) | Standard for market-neutral |
| **Net exposure** | ≤ ±10% | Must stay market-neutral |
| **Sector exposure** | ≤ ±5% per sector | Prevents sector concentration disguised as alpha |
| **Turnover** | 15-30% daily | High turnover = high cost sensitivity; model must clear [[transaction-cost-modeling|cost hurdle]] |

---

## Volatility & Options Arbitrage

### Volatility Arbitrage (IV vs RV)

| Parameter | Value | Rationale |
|---|---|---|
| **IV-RV spread entry** | IV > RV + 3 vol points (sell vol) or IV < RV - 3 vol points (buy vol) | 3-point cushion covers transaction costs and gamma risk |
| **IV measurement** | ATM 30-day implied vol | Most liquid point on the surface |
| **RV measurement** | 20-day close-to-close realized vol, or Yang-Zhang estimator | Yang-Zhang is more efficient (uses O/H/L/C) |
| **Delta hedge frequency** | Daily for swing, intraday for active management | Each re-hedge costs spread + commission |
| **Gamma exposure limit** | ≤ 0.5% portfolio value per 1% underlying move | Prevents gamma blowup on gap moves |
| **Vega exposure limit** | ≤ 2% portfolio value per 1 vol point move | Controls total vol exposure |
| **Max days to expiry** | 7-45 DTE for gamma trades, 30-90 DTE for vega trades | Theta decay profile differs |
| **Stop loss** | Close if P&L reaches -2× initial credit received | Limits tail loss |

### Dispersion Trading

| Parameter | Value | Rationale |
|---|---|---|
| **Index-component IV spread** | Index IV > weighted-avg component IV + 2 vol points | Systematic premium due to correlation risk premium |
| **Minimum number of components** | Trade ≥ 15-20 single names | Diversification across names |
| **Correlation entry** | Implied correlation > 75th percentile historical | Sell correlation when it's rich |
| **Position sizing** | Vega-neutral at portfolio level | Net vega exposure near zero |
| **Hedge rebalance** | Weekly delta hedge, daily if underlying moves > 2% | Balance cost vs. drift |

---

## Event-Driven Arbitrage

### Merger Arbitrage

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum annualized spread** | > 8% | Must beat risk-free (~5%) + deal-break risk premium (historically ~7% of deals fail) |
| **Entry timing** | After definitive agreement announced | Avoid rumor-stage — deal certainty is too low |
| **Position size** | ≤ 5% of portfolio per deal | Single deal failure can lose 20-40% of position value |
| **Maximum number of concurrent deals** | 10-20 | Diversification across deals reduces idiosyncratic risk |
| **Stop loss** | Exit if spread widens > 2× entry spread | Indicates new information suggesting deal break |
| **Hold period** | Average 3-6 months (until close or break) | Capital is locked; opportunity cost is real |
| **Hedge ratio (stock deals)** | Exchange ratio × target shares = acquirer short shares | Must match deal terms exactly |

**Annualized spread formula:**
```
annualized_spread = (deal_price / current_price - 1) × (365 / expected_days_to_close)
```

---

## DeFi / Crypto-Native Arbitrage

### Flash Loan Arbitrage

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum profit per transaction** | > gas cost × 2 | Must cover gas + failed-tx gas + competition. On Ethereum mainnet, gas for a flash loan arb = $10-200+ |
| **Profitable on L2** | > $0.50 per tx | L2 gas is 10-100× cheaper; smaller arbs become viable |
| **Slippage tolerance** | Set to 0.1-0.5% | Tighter = more reverts, wider = more competition captures profit |
| **Block timing** | Submit in same block as opportunity detection | Atomic — either all legs execute or none |
| **MEV protection** | Use Flashbots Protect or private mempool | Prevents frontrunning by [[mev-strategies|MEV searchers]] |

### Staking Yield Arbitrage

| Parameter | Value | Rationale |
|---|---|---|
| **Minimum yield spread** | > 3% annualized over risk-free | Must compensate for smart contract risk + [[depeg-risk]] |
| **LST discount entry** | stETH/ETH < 0.995 (0.5% discount) | Historical depegs have reached 5-7%; entering at 0.5% discount adds margin |
| **Exit trigger** | LST returns to ≥ 0.999 of peg | Most of the return is captured |
| **Smart contract risk budget** | ≤ 15% of portfolio in any single protocol | Protocol exploits are binary — see [[2020-2024-bridge-exploits]] |
| **Protocol diversification** | ≥ 3 protocols (e.g., Lido + Rocket Pool + Coinbase cbETH) | Reduces single-protocol concentration |

---

## Universal Parameters (Apply to All Strategies)

| Parameter | Value | Rationale |
|---|---|---|
| **Maximum portfolio allocation per strategy** | ≤ 25% | Prevents single-strategy concentration |
| **Maximum per-exchange exposure** | ≤ 30% | [[counterparty-risk]] cap |
| **Daily drawdown halt** | Pause if daily P&L < -2% of arb portfolio | Prevents compounding losses from correlated failures |
| **Weekly drawdown halt** | Pause if weekly P&L < -5% | System-level kill switch |
| **Correlation monitoring** | Check pairwise strategy correlations monthly | If correlation > 0.6, treat as single bet for sizing — see [[strategy-correlation-matrix]] |
| **Cost recalibration** | Re-measure actual vs. modeled costs quarterly | Fee tiers change, spreads evolve, market structure shifts |
| **Backtest-to-live decay assumption** | Expect 30-50% Sharpe degradation from backtest to live | Standard for [[walk-forward-analysis|walk-forward]] efficiency |

## Parameter Calibration Workflow

1. **Start with the formulas above** to calculate theoretical minimum thresholds
2. **Backtest with historical data** (see [[historical-spread-data]]) to validate that the threshold generates positive expectancy after costs
3. **Paper trade for 2-4 weeks** to measure actual execution vs. theoretical fills
4. **Measure realized costs** (actual fees + slippage + missed fills) and recalibrate thresholds
5. **Deploy with 25% of target capital** for 1-2 months, then scale up
6. **Recalibrate quarterly** — thresholds drift as competition and market structure evolve

## Seasonal Parameter Adjustments

Parameters should not be static year-round. Cross-reference with [[arbitrage-seasonality]] for the full calendar. Key adjustments:

### Funding Rate Arbitrage — Seasonal Thresholds

| Season | Minimum Funding Rate (8h) | Rationale |
|---|---|---|
| **Nov-Feb** (bull peak) | 0.010% (standard) | Rates naturally elevated; standard thresholds apply |
| **Mar-May** (transitional) | 0.015% (tighter) | Rates declining; raise minimum to avoid marginal trades |
| **Jun-Sep** (summer doldrums) | 0.020% (strictest) | Average rates compress ~40% from peak. Only enter above-average opportunities |
| **Oct** (pre-bull) | 0.012% (easing) | Rates beginning to recover; slightly relaxed threshold |

### Cross-Exchange Arbitrage — Event-Window Adjustments

| Event | Threshold Adjustment | Window |
|---|---|---|
| FOMC announcement | Widen min spread by 50% (more slippage) | -2h to +1h around announcement |
| Major exchange maintenance | Pause trading on that venue | During maintenance window |
| Crypto options expiry | Tighten position size by 50% (pin risk) | Last 4 hours before expiry |
| New token listing | Reduce min spread requirement by 30% (wider spreads available) | First 24 hours |

### Merger Arbitrage — Calendar Adjustments

| Period | Adjustment |
|---|---|
| **Q4 (Oct-Dec)** | Most new deal announcements. Deploy fresh capital, widen deal pipeline |
| **Q1 (Jan-Mar)** | New regulatory administrations may shift deal-break probability. Reassess all positions |
| **Election years** | Add 2-3% regulatory risk premium to spreads (antitrust uncertainty) |
| **Summer (Jun-Aug)** | Fewer new deals. Maintain existing positions but don't chase thin spreads |

### Volatility Arbitrage — VIX Regime Adjustments

| VIX Level | IV-RV Entry Threshold | Position Size Adjustment |
|---|---|---|
| < 15 (low vol) | ≥ 4 vol points (stricter — VRP compressed) | 75% of standard |
| 15-25 (normal) | ≥ 3 vol points (standard) | 100% |
| 25-35 (elevated) | ≥ 5 vol points (wider — tail risk higher) | 50% of standard |
| > 35 (crisis) | Pause short-vol entirely | 0% — be a vol buyer, not seller |

## Worked example — deriving a threshold from scratch

Suppose you want the minimum [[cross-exchange-arbitrage]] spread for BTC at retail Coinbase taker fees. Do not copy the table — derive it, because your fee tier is the dominant term:

1. **List the cost stack** (see [[transaction-cost-modeling]]): taker fee venue A + taker fee venue B + expected [[slippage]] A + expected slippage B + withdrawal/transfer + safety margin.
2. **Plug in your actual numbers.** At Coinbase retail ~0.60% taker on one leg and ~0.10% maker on the other, plus ~0.03% combined slippage and ~0.05% margin → minimum viable spread ≈ **0.78%**.
3. **Reality-check against frequency.** A ~0.8% BTC cross-exchange spread is rare; this is why the table's 0.15% figure assumes VIP/maker fees. The lesson: **fee-tier optimization changes the strategy's existence**, not just its margin.
4. **Validate, don't trust.** Run the threshold through the [[arbitrage-backtesting-guide]] (bid/ask fills, latency, partial fills, leg failure) before risking capital, then haircut for the backtest-to-live decay below.

This derive-then-validate loop applies to every threshold on this page: the formulas give a theoretical floor, the backtest confirms positive expectancy after honest costs, and paper trading measures the gap.

## Common calibration pitfalls

| Pitfall | Symptom | Fix |
|---|---|---|
| Using table values verbatim at retail fees | Live fills never trigger or trigger into losses | Derive your own floor from your actual [[fees]] tier |
| Sizing off gross spread, not downside | One merger-arbitrage break wipes a year of carry | Size off the loss-given-break / depth, not the headline |
| Static thresholds year-round | Edge erodes in summer / low-VIX regimes | Apply the seasonal/regime tables above |
| Ignoring [[leg-risk]] in multi-leg | Backtest shows 100% fills; live strands legs | Model leg-failure rate (Sin 4 in [[arbitrage-backtesting-guide]]) |
| No cost recalibration | Drift between modeled and realized cost | Re-measure quarterly (Universal Parameters table) |
| Over-fitting z-score / lookback | Great backtest, dead live | [[deflated-sharpe-ratio]], [[walk-forward-analysis]] |

## Related

- [[arbitrage]] · [[arbitrage-overview]] -- the strategy family these thresholds gate
- [[arbitrage-backtesting-guide]] -- how to validate every number here honestly
- [[arbitrage-opportunity-map]] · [[arbitrage-seasonality]] -- where and when to look
- [[transaction-cost-modeling]] · [[fees]] · [[slippage]] · [[market-impact]] -- the cost stack
- [[limits-to-arbitrage]] -- why the cost floor exists at all
- [[cross-exchange-arbitrage]] · [[triangular-arbitrage]] · [[cash-and-carry]] · [[funding-rate-arbitrage]] -- pure-arb pages
- [[pairs-trading]] · [[statistical-arbitrage]] · [[volatility-arbitrage]] -- statistical/vol pages
- [[flash-loan-arbitrage]] · [[slippage-optimal-pathfinding]] -- DeFi pages
- [[walk-forward-analysis]] · [[deflated-sharpe-ratio]] -- out-of-sample rigor
- [[counterparty-risk]] · [[strategy-correlation-matrix]] -- portfolio-level caps

## Sources

- Wiki cross-references: [[arbitrage-opportunity-map]], [[arbitrage-seasonality]], [[transaction-cost-modeling]], [[fees]], [[edge-taxonomy]], [[failure-modes]], [[research-checklist]], [[walk-forward-analysis]].
- General market knowledge; no specific wiki source ingested yet.
