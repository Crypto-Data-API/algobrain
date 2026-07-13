---
title: "Hyperliquid Perp Trading Map"
type: concept
created: 2026-04-14
updated: 2026-06-20
status: excellent
tags: [strategy-development, hyperliquid, perpetual-futures, arbitrage, funding-rate, crypto, research]
aliases: ["Hyperliquid Strategies", "Perp Trading Map", "Hyperliquid Opportunity Map"]
domain: [strategy-development]
difficulty: advanced
related: ["[[arbitrage-opportunity-map]]", "[[edge-taxonomy]]", "[[regime-matrix]]", "[[hyperliquid]]", "[[funding-rate-arbitrage]]", "[[basis-trading]]", "[[perpetual-futures]]", "[[funding-rate]]", "[[liquidation]]", "[[delta-neutral]]", "[[strategy-correlation-matrix]]", "[[failure-modes]]"]
---

# Hyperliquid Perp Trading Map

A comprehensive strategy map for trading perpetual futures on [[hyperliquid|Hyperliquid]]. This page synthesizes every relevant strategy, concept, anomaly, and risk factor from across the wiki, filtered through the lens of what is *actually executable* on a perp-only DEX with 229 markets, hourly funding, and up to 50x leverage.

The parent document [[arbitrage-opportunity-map]] covers arbitrage opportunities wiki-wide. This page narrows to: **what can you trade, how, and what kills you — on Hyperliquid specifically.** It is the index node of the [[trading-strategy-baskets|Hyperliquid strategy basket]]; every strategy and concept below links to its own deep page.

---

## Master Strategy Index

The full executable surface on [[hyperliquid]], categorized. Each row links to the deep page. Delta-neutral strategies (Part 1) trade structure; directional strategies (Part 2) trade price; cross-asset (Part 3) and hidden edges (Part 4) are HL-unique. The HL-specific microstructure strategies — built on the [[hyperliquid-oracle-mechanics|oracle]], [[hyperliquid-liquidation-engine|liquidation engine]], and HLP vault — are the densest cluster of edge.

| # | Strategy | Category | Edge type ([[edge-taxonomy]]) | Deep page |
|---|----------|----------|-------------------------------|-----------|
| 1 | Funding Rate Arbitrage | Delta-neutral | structural | [[funding-rate-arbitrage]] |
| 2 | Basis Trading | Delta-neutral | structural | [[basis-trading]] |
| 3 | Delta-Neutral Yield Farming | Delta-neutral | structural | [[delta-neutral-yield-farming]] |
| 4 | Cross-Venue Funding Arb (HL vs CEX) | Delta-neutral | structural + latency | [[hl-vs-cex-funding-divergence]] |
| — | HLP Basis Arbitrage | Delta-neutral / risk-bearing | structural + risk-bearing | [[hyperliquid-hlp-basis-arbitrage]] |
| 5 | Trend Following | Directional | behavioral / risk-bearing | [[trend-following-cta]] |
| 6 | Mean Reversion | Directional | behavioral | [[mean-reversion]] |
| 7 | Stop-Hunting / Liquidation Cascade | Directional | informational + latency | [[stop-hunting-and-liquidity-sweeps]] |
| — | Liquidation Cascade Fade | Directional | behavioral | [[liquidation-cascade-fade]] |
| — | Liquidation Cascade Keeper Arb | Directional / latency | latency | [[liquidation-cascade-arbitrage]] |
| — | HLP Cascade-Alongside Hedge | Hedge overlay | structural | [[hlp-cascade-alongside-playbook]] |
| 8 | Grid Trading | Directional / range | behavioral | [[grid-trading]] |
| 9 | Pairs Trading (BTC/ETH + cross-asset) | Stat-arb | analytical | [[pairs-trading]] |
| 10 | Regime-Adaptive Meta-Strategy | Meta | analytical | [[regime-adaptive-strategy]] |
| 11 | Crypto-Commodity Correlation | Cross-asset | analytical | [[pairs-trading]] (cross-asset) |
| 12 | Proxy Commodity Spreads | Cross-asset | structural | [[crack-spread]] |

**Supporting concepts** (read these to run the above): [[hyperliquid-oracle-mechanics]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[cascade-detection-signals]] · [[funding-rate]] · [[open-interest]] · [[liquidation]] · [[mark-price]] · [[delta-neutral]] · [[hypurrscan]].

---

## Platform Edge: Why Hyperliquid Is Different

Before mapping strategies, understand what makes Hyperliquid structurally distinct from CEXs and other DEXs. These differences create edges *and* risks that don't exist elsewhere.

### Structural Advantages

| Feature | Hyperliquid | Binance/Bybit | dYdX | GMX |
|---|---|---|---|---|
| Order book | On-chain CLOB | Off-chain | Off-chain match + on-chain settle | Oracle-priced AMM |
| Funding interval | **1 hour** | 8 hours | 1 hour | Borrow fees |
| Maker fee | **0.015%** | 0.02% | 0.02% | 0.05-0.07% |
| Gas fees | **Zero** | N/A (CEX) | Low | Arbitrum gas |
| Custody | Self-custody | Custodial | Self-custody | Self-custody |
| Transparency | All orders on-chain | Dark pools, hidden orders | Partial | AMM pools |
| Markets | **229** (crypto + TradFi) | 300+ crypto | ~180 crypto | ~100 crypto |
| Throughput | 200K orders/sec, <200ms | Millions/sec | Lower | AMM (no order book) |

### What This Means for Strategy Selection

1. **Hourly funding** — 24 rebalancing points per day vs 3 on CEXs. Creates micro-arbitrage opportunities between funding snapshots. Strategies sensitive to funding timing (basis arb, funding arb) are more granular here.

2. **Zero gas + 0.015% maker** — High-frequency strategies (grid trading, scalping, market making) that are fee-prohibitive on other DEXs become viable. A grid bot making 100 round trips/day pays 3% in fees on GMX but 1.5% on Hyperliquid.

3. **Fully transparent order book** — Every order, fill, liquidation, and cancellation is on-chain. Institutional absorption, whale positioning, and stop clusters are all visible. Order flow strategies are *more reliable* than on CEXs with dark pools.

4. **TradFi perps** (crude oil, gold, silver, SP500, TSLA, NVDA) — Cross-asset correlation trades are possible on a single venue. No need to bridge between crypto and TradFi brokers. Crack spread proxies, gold/BTC correlation, SP500/BTC basis — all executable here.

5. **Self-custody** — No FTX-style counterparty risk *on the exchange side*. But: smart contract risk on HyperBVM (younger L1 vs battle-tested Ethereum). Trade-off, not elimination, of counterparty risk.

6. **Sub-accounts** — Each sub-account has isolated liquidation. Strategy compartmentalization is native. One blow-up doesn't cascade to other strategies.

### Structural Risks Unique to Hyperliquid

| Risk | Severity | Detail |
|---|---|---|
| Smart contract / chain risk | HIGH | HyperBVM is a young L1. Zellic-audited, $1M bug bounty, but not Ethereum-battle-tested. |
| MEV exposure | HIGH | Fully public order book means all positions visible to MEV bots. Large orders can be front-run. |
| Whale concentration | HIGH | Top 10 traders do ~$1.58B/day (20-25% of volume). Single whale liquidation can cascade. |
| Regulatory | MEDIUM | TradFi perps (stocks, commodities) without KYC may attract SEC/CFTC attention. US/Ontario blocked. |
| Oracle risk | MEDIUM | TradFi perps rely on price feeds. Oracle manipulation in thin markets (see XPL incident). |
| Single-chain concentration | MEDIUM | All execution on HyperBVM. Chain outage = all markets frozen simultaneously. |
| Validator centralization | LOW-MEDIUM | Staking distribution should be monitored over time. |

---

## Part 1: Delta-Neutral Strategies (Lowest Risk)

These strategies aim for zero directional exposure. Profit comes from structural mechanisms (funding, basis convergence) rather than price prediction.

### Strategy 1: Funding Rate Arbitrage

The flagship delta-neutral strategy. Documented fully at [[funding-rate-arbitrage]].

**Mechanism:** Long spot (self-custody or CEX) + short perp on Hyperliquid (1x leverage). Collect funding payments when longs pay shorts (positive funding = perp trading above spot).

**Hyperliquid-Specific Implementation:**
- Hyperliquid's **hourly funding** means 24 collection points per day vs 3 on Binance
- More granular entry/exit: can capture intra-day funding spikes that 8-hour averages miss
- Monitor via Coinglass or Hyperliquid's native API

**Numbers (from wiki):**
- Entry threshold: funding >0.03% per 8h equivalent (~33% APY)
- Bull market yield: 10-50% APY (2021 peaks: 100%+ APY)
- Current (April 2026): BTC ~0.005% per 8h (below neutral); ETH ~0.01% (neutral) — **not an entry point right now**
- FARTCOIN: 0.059% per 8h (~64.6% APY) — **elevated, but extreme liquidation/illiquidity risk**

**Example:**
```
Buy 10 ETH spot @ $2,132 = $21,320
Short 10 ETH perp on Hyperliquid @ $2,140 with $21,320 margin (1x)
Total capital: $42,640
Funding at 0.03% per 8h: $6.40 per 8h × 3/day = $19.20/day
Monthly: ~$576 → 16.2% APY on deployed capital
Bull market at 0.05% per 8h: $32/day → $960/month → 27% APY
```

**Kill criteria:**
- 7-day trailing average funding turns negative → exit immediately
- Funding compresses below 5% annualized → redeploy capital
- Exchange solvency concern → withdraw spot leg

**Regime from [[regime-matrix]]:** ✅ Trending up, ✅ Sideways, ➕ Down, ❌ High vol, ✅ Low vol, ➖ Risk-off

**Who is on the other side:** Retail speculators using leverage to go long. They pay the funding premium because they want leveraged upside exposure and are willing to pay for it. As long as retail uses leverage, this edge persists. (Source: [[edge-taxonomy]])

---

### Strategy 2: Basis Trading (Perp vs Spot Convergence)

Related to funding arb but conceptually distinct. Documented at [[basis-trading]].

**Mechanism:** When the perp price persistently trades above spot (positive basis / contango), buy spot and short perp. The basis either converges via funding payments or via direct price convergence.

**Hyperliquid Nuance:** Perps have no expiry, so there's no forced convergence date. Basis convergence happens through funding mechanism. This makes it functionally identical to funding rate arb on Hyperliquid — but the framing matters for monitoring. Track the *basis spread* (perp minus spot) as a signal, not just the funding rate.

**Numbers:**
- Annualized basis formula: `(Perp Price - Spot Price) / Spot Price × (365 / Holding Days) × 100%`
- Entry when annualized basis >10-15%
- Win rate: 90-95% (convergence is structural)
- Profit factor: 5.0-10.0

**Hyperliquid-Specific Risk:** Mark-to-market pain. If BTC rallies 15% in a day, your perp short shows a large unrealized loss even though the position is delta-neutral. On Hyperliquid with isolated margin, this can trigger liquidation of the perp leg if under-collateralized. **Always maintain 2-3x maintenance margin buffer on the short leg.**

---

### Strategy 3: Delta-Neutral Yield Farming (Multi-Layer)

Documented at [[delta-neutral-yield-farming]]. Layers multiple yield sources on the same capital.

**Hyperliquid Implementation:**
```
Layer 1: Hold ETH spot (staking yield: 3-5% APY)
Layer 2: Short ETH perp on Hyperliquid (funding income: 10-30% APY in bull)
Layer 3: Lend idle USDC on Aave (3-8% APY)

Combined yield in bull market: 16-43% APY with zero price exposure
Conservative estimate: ~18-25% APY
```

**Critical lesson from [[2022-05-terra-luna-depeg-arb|Terra/LUNA]]:** Each layer adds a reflexivity loop. When Layer 2 breaks (funding inverts), Layer 1 and 3 are still collecting — but if the *exchange* breaks (FTX-style), all layers fail simultaneously. Multi-layer yield is NOT the same as multi-source diversification. The common dependency is counterparty/platform solvency.

**Risk management:** Cap total delta-neutral yield farming at 30% of crypto portfolio. Diversify across 2-3 venues (Hyperliquid + Binance + Bybit). Withdraw Layer 3 yields regularly.

---

### Strategy 4: Cross-Venue Funding Rate Arbitrage

Now documented in full at [[hl-vs-cex-funding-divergence]] (this map's worked example is the conservative steady-state case there). Sits in the [[cross-exchange-arbitrage]] family and is a cross-venue variant of [[funding-rate-arbitrage]]. The cadence-mismatch mechanism is detailed in [[hyperliquid-funding-rate-microstructure]] and [[hyperliquid-oracle-mechanics]] (HL funding derives from `(mark − oracle)`).

**Mechanism:** Different exchanges charge different funding rates for the same asset at the same time. Long perp on the exchange paying you funding, short perp on the exchange charging you less.

**Example:**
```
BTC funding on Binance: +0.05% per 8h (longs pay shorts)
BTC funding on Hyperliquid: +0.02% per 8h (longs pay shorts, lower)

Trade: Long BTC perp on Hyperliquid (pay 0.02%), short BTC perp on Binance (receive 0.05%)
Net: +0.03% per 8h = ~33% APY, fully delta-neutral

Capital: $50K per venue = $100K total
Daily income: $50K × 0.03% × 3 = $45/day = $16,425/year
```

**Why this works:** Funding rates are set by local supply/demand on each exchange. Hyperliquid's hourly funding may lag Binance's 8-hour rate, creating persistent micro-dislocations.

**Risks:** Capital split across two venues (doubling counterparty risk). Funding rates converge quickly once arbed. Execution timing must be tight. More useful as a *tactic* during funding spikes than a permanent allocation.

---

## Part 2: Directional Strategies (Higher Return, Higher Risk)

These strategies take directional bets. They profit from price movement, not structural mechanisms. All executable on Hyperliquid perps using long/short positions.

### Strategy 5: Trend Following

Documented at [[trend-following-cta]], [[moving-average-crossover]], [[turtle-trading]].

**Mechanism:** Buy assets trending up, short assets trending down. Use MA crossovers, channel breakouts, or time-series momentum.

**Hyperliquid Implementation:**
- **Simple:** Buy when 50-day SMA > 200-day SMA; short when below. Apply to BTC, ETH, SOL.
- **Channel breakout:** Buy at 100-day high, short at 100-day low (Turtle rules)
- **Position sizing:** Volatility-target each position. Size = (Portfolio × 1% risk) / (ATR × contract size)

**Why it works on crypto:** Crypto exhibits persistent multi-week trends driven by macro (Fed, ETF flows, halving cycle), narrative (regulation, adoption), and reflexive leverage (funding + liquidation cascades amplify trends).

**Regime from [[regime-matrix]]:** ✅ Up, ✅ Down, ❌ Chop, ✅ High Vol, ➖ Low Vol, ✅ Risk-Off

**Performance:** Win rate 35-45% (low). Profit factor 1.3-2.0. Relies on large winners (trend catches) offsetting many small losses (false breakouts). Historical CAGR 8-15% at 10-12% vol.

**Critical insight from [[strategy-correlation-matrix]]:** Trend-following is the **ONLY strategy category with negative crisis correlations** to everything else. When carry, mean-reversion, and vol-selling all blow up simultaneously (Aug 2007, March 2020), trend-following profits. This makes it the single most important portfolio diversifier — even if its standalone returns are modest.

**Hyperliquid-specific advantage:** 229 markets including TradFi assets (crude oil, gold, SP500). A trend-following system can diversify across crypto AND commodities AND indices on a single venue. Cross-asset trend diversification was historically only possible with a futures brokerage account.

---

### Strategy 6: Mean Reversion (RSI + Bollinger)

Documented at [[mean-reversion]], [[rsi-mean-reversion]], [[bollinger-band-reversion]].

**Mechanism:** Bet that extreme price deviations revert to average. Buy oversold, sell overbought.

**Hyperliquid Implementation:**
- **Connors RSI(2):** Buy when RSI(2) < 10 *and* price above 200-day SMA (uptrend filter). Exit when RSI(2) > 70.
- **Bollinger Band:** Buy below lower band (2 std devs), target middle band or upper band.
- **Z-score on spread:** For pairs (BTC/ETH), enter when z-score > 2.0, exit at 0.

**Performance:** Win rate 55-65% with RSI+BB dual confirmation. Holding period 2-6 days. Profit factor 1.3-1.8. Sharpe 0.8-1.2.

**Regime from [[regime-matrix]]:** ❌ Trending, ✅ Chop, ➖ High Vol, ✅ Low Vol, ❌ Risk-Off

**Anti-correlated with trend-following.** These two strategies combined cover all regimes except risk-off. Add a tail hedge (long vol or long BTC puts on Deribit) to complete the portfolio.

---

### Strategy 7: Stop-Hunting / Liquidation Cascade Trading

Documented at [[stop-hunting-and-liquidity-sweeps]], [[liquidation]], [[long-liquidation]].

**Mechanism:** Institutions push price beyond key support/resistance to trigger retail stop losses and liquidations, then reverse. Trade the reversal after the sweep.

**Why this is the highest-edge strategy on Hyperliquid specifically:**

1. **Transparent liquidation data.** Every liquidation is on-chain. Coinglass and Hyperliquid's own feeds show real-time liquidation cascades. You can literally *see* the forced selling exhausting.

2. **High leverage concentration.** Hyperliquid allows up to 50x on BTC. This creates dense liquidation clusters just beyond obvious levels ($100K, $99K, $98K on BTC). These clusters are *predictable*.

3. **Daily liquidation volume is massive.** April 2 saw 32,964 liquidations. Normal days see 10,000-17,000. These are tradeable events, not rare occurrences.

4. **Open interest drops mark cascade exhaustion.** When OI drops sharply during a price decline, it means longs are being liquidated (forced closing). When the OI drop slows, the cascade is exhausting. This is the entry signal.

**Implementation:**
```
1. Identify stop clusters:
   - Below swing lows on daily chart
   - Below round numbers ($100K, $99K, etc.)
   - Below key MAs (50-day, 200-day)
   - Use Coinglass liquidation heatmap for precision

2. Wait for sweep:
   - Price breaks below support with volume spike
   - Wick extends 1-3% below the level
   - Liquidation count spikes (monitor real-time)
   - OI drops sharply (longs being force-closed)

3. Enter reversal:
   - Price closes back above the broken level
   - Delta flips positive (buy volume > sell volume)
   - Entry: On reversal candle close
   - Stop: Below sweep low
   - Target: Opposite side of range (2-3R typical)
```

**Example (BTC on Hyperliquid, hypothetical):**
```
BTC consolidates $99K-$102K for 2 weeks
Stop clusters visible at $98.8K, $98.5K, $98.2K (200-day MA)
Weekend low-volume: BTC wicks to $98.1K
Liquidation spike: 920 BTC liquidations in 1 hour (real April 6 data)
OI drops from 29,000 to 28,000 BTC (forced closing)
Next candle: closes $99.2K (back inside range)
Entry: $99.2K long
Stop: $98.0K (risk: $1,200 per BTC)
Target: $101.5K (reward: $2,300 per BTC)
R/R: 1:1.9
```

**Performance:** Win rate 60-70%. Profit factor 2.0-3.0. Works because entries are near forced-seller exhaustion points.

**Deep pages.** The detection layer is fully specified in [[cascade-detection-signals]] (the three-stage PRE-CASCADE / IMMINENT / IN-CASCADE hierarchy, with [[open-interest]]/price-divergence and depth-withdrawal computations). The fade execution is [[liquidation-cascade-fade]]; the keeper-bot variant is [[liquidation-cascade-arbitrage]]; the HLP-hedge overlay is [[hlp-cascade-alongside-playbook]]. The [[hyperliquid-oracle-mechanics|oracle]]-deviation signal `(mark − oracle)` is the earliest, HL-unique cascade trigger; the engine internals are in [[hyperliquid-liquidation-engine]].

**Regime from [[regime-matrix]]:** (closest proxy: [[contrarian-extremes]]) ✅ High vol, ✅ Risk-off — thrives exactly when other strategies die.

---

### Strategy 8: Grid Trading

Documented at [[grid-trading]].

**Mechanism:** Place buy/sell limit orders at fixed intervals. Profit from oscillation within a range.

**Hyperliquid Implementation:**
```
Asset: ETH/USDC perp
Range: $2,000-$2,300 (current price ~$2,130)
Grid levels: 15 ($20 spacing)
Capital per level: $1,000
Total: $15,000

Each completed round trip: $20 profit minus ~$0.60 fees = $19.40 net
20 round trips/week in ranging market = $388/week
Monthly: ~$1,550 (12.4% monthly, 149% annualized)

Reality check: Price won't stay in range forever.
Realistic: 50% of weeks range-bound = ~6% monthly = 72% annualized
```

**Hyperliquid advantage:** Zero gas fees + 0.015% maker fee makes grids viable. On GMX (0.05-0.07%), the same grid loses ~40% of profits to fees.

**Regime from [[regime-matrix]]:** (proxy: mean-reversion) ✅ Chop, ✅ Low vol, ❌ Trending

**Variations for Hyperliquid:**
- **Neutral grid:** Equal buys/sells around current price. Best for pure range-bound.
- **Long-biased grid:** Only buys below current price. DCA into dips, sell on bounces. Safer in uptrends.
- **Geometric grid:** % spacing instead of fixed $. Better for volatile assets (SOL, HYPE).
- **Trailing grid:** Grid center follows 20-day MA. Adapts to slow trends.

**What kills it:** Strong directional moves. Grid keeps buying as price falls (or selling as price rises), accumulating a large losing inventory. With leverage: liquidation. Without leverage: underwater position that may never recover.

---

### Strategy 9: Pairs Trading (BTC/ETH)

Documented at [[pairs-trading]], [[statistical-arbitrage]].

**Mechanism:** Long the underperformer, short the outperformer in a cointegrated pair. Profit from mean-reversion of the spread.

**Hyperliquid advantage:** Both legs on the same venue. No cross-exchange execution risk. Same margin pool (with sub-accounts for isolation).

**Implementation:**
```
1. Calculate hedge ratio: 90-day rolling regression
   Typical: ~12-15 ETH per BTC (varies with price ratio)
2. Spread = ln(BTC) - hedge_ratio × ln(ETH)
3. Z-score of spread (20-day rolling)
4. Entry: |z| > 2.0
5. Exit: z returns to 0
6. Stop: |z| > 3.5 (breakdown of cointegration)
```

**BTC/ETH cointegration:** Historically strong (correlation 0.8+). But breaks during "alt season" (ETH outperforms dramatically) or "BTC dominance" phases (ETH underperforms). Must re-test cointegration monthly. If Engle-Granger p-value > 0.10, stop trading the pair.

**Performance:** Win rate 60-70%. Average hold 5-15 days. Profit factor 1.5-2.0. Sharpe 0.8-1.2.

**Extended pairs on Hyperliquid's 229 markets:**
- **SOL/ETH** — Layer 1 competition pair
- **BTC/Gold (xyz:GOLD)** — Safe-haven correlation trade
- **Crude (xyz:CL) / Natural Gas (xyz:NG)** — Energy spread proxy
- **SP500 (xyz:SP500) / BTC** — Risk-on macro pair

The TradFi perps enable cross-asset pairs trading on a single DEX — previously impossible without a multi-asset brokerage account. This is a **unique structural edge** of Hyperliquid.

---

### Strategy 10: Regime-Adaptive Strategy

Documented at [[regime-adaptive-strategy]], [[regime-detection]].

**Mechanism:** Detect current market regime. Deploy the optimal sub-strategy. Switch when regime changes.

**Crypto-Specific Regime Signals (for Hyperliquid):**

| Signal | Data Source | Bull Trend | Consolidation | Bear/Crisis |
|---|---|---|---|---|
| [[funding-rate|Funding rate]] | Hyperliquid API | >0.03% / 8h | 0.005-0.015% | < 0 |
| Fear & Greed Index | alternative.me | > 60 | 40-60 | < 30 |
| ADX(14) | TradingView | > 25 | < 20 | > 25 (down) |
| BTC vs 200-day SMA | Price data | Price above | At/near | Price below |
| Open interest trend | Coinglass | Rising | Flat | Falling |
| Liquidation volume | Hyperliquid/Coinglass | Low (<5K/day) | Low | Spiking (>20K/day) |
| Stablecoin exchange flows | Nansen/CryptoQuant | Inflow (buying) | Flat | Outflow (de-risk) |

**Decision Matrix:**

| Regime | Detection | Deploy | Sizing |
|---|---|---|---|
| Bull trend | Funding >0.02%, ADX >25, price >200d SMA | Trend-following + funding arb | 100% |
| Consolidation | ADX <20, BB width low, neutral funding | Grid trading + mean reversion + basis arb | 100% |
| Bear trend | Price <200d SMA, ADX >25, funding negative | Short trend-following + contrarian at extremes | 50-75% |
| Crisis / cascade | Liquidations >20K/day, VIX >30, fear <20 | Reduce 75%. Liquidation hunting only. | 25% |
| Transition | Mixed signals | Reduce 50%. Wait for clarity. | 50% |

**Why regime-adaptive is the meta-strategy:** From [[regime-matrix]], the regime-adaptive row shows ✅ across ALL six regimes. No other strategy achieves this. The trade-off: it underperforms pure single-regime strategies *in that regime* but avoids catastrophic losses from regime mismatch.

---

## Part 3: Cross-Asset Opportunities (Hyperliquid-Unique)

Hyperliquid's HIP-3 program lists TradFi assets as perpetual contracts. This creates opportunities that exist on no other DEX.

### Strategy 11: Crypto-Commodity Correlation Trades

**Observation from wiki:** [[2026-03-iran-conflict-oil-spike|Iran conflict]] pushed crude to $100-120/barrel. BTC simultaneously sold off as a risk asset. Gold rallied as safe haven.

**Hyperliquid markets:** xyz:CL (crude oil, $414.5M daily volume), xyz:GOLD ($49M), xyz:SILVER ($113.9M), xyz:SP500 ($73.2M)

**Tradeable correlations:**
- **BTC/Gold:** Historically positive in risk-off (both "stores of value"), but BTC sells off harder in acute panic. When correlation breaks (BTC down, Gold up), the divergence mean-reverts within 1-2 weeks.
- **BTC/SP500:** High correlation (~0.6-0.8 in recent years). When they diverge, it's usually temporary. Long the laggard, short the leader.
- **Crude/BTC:** Negative correlation during supply shocks (crude up = inflation = risk-off = BTC down). Positive correlation during demand-driven rallies. The regime matters.

**Example (BTC/Gold divergence):**
```
Iran conflict: Gold spikes 5%, BTC drops 8% in same week
Historical: This divergence mean-reverts within 5-15 days
Trade: Long BTC perp, short xyz:GOLD perp (hedge ratio from 30-day regression)
Entry: Spread z-score > 2.0
Exit: z-score returns to 0
Stop: z-score > 3.5

This is pairs trading across asset classes — on a single DEX.
```

### Strategy 12: Proxy Commodity Spreads

The wiki documents [[crack-spread]], [[crush-spread]], and [[spark-spread]] as traditionally profitable commodity arbitrages. Hyperliquid can't perfectly replicate these (no gasoline, no soybeans, no electricity), but:

**Crude Oil Calendar Proxy:**
- If Hyperliquid lists multiple crude expiries or a front/deferred spread, calendar spreads are directly tradeable
- Even without: track the crude/gas spread (xyz:CL vs xyz:NG) as a rough energy basis proxy

**Gold/Silver Ratio:**
- From wiki's gold analysis: gold-to-silver ratio >80 historically signals silver rally (happened 4 times in 2024)
- Trade: When ratio >80, long xyz:SILVER / short xyz:GOLD
- Capacity: $113.9M silver volume / $49M gold volume — sufficient for moderate positions

---

## Part 4: Hidden Edges Specific to Hyperliquid

### Hidden Edge #1: Hourly Funding Rate Micro-Arbitrage

Hyperliquid settles funding every hour. Most competitors settle every 8 hours. This creates **intra-day funding rate volatility** that 8-hour averages mask.

**The opportunity:** Funding rate can spike to 0.05% in one hour (during a liquidation cascade) and revert to 0.001% the next hour. An 8-hour average would show ~0.007% — boring. But a trader positioned to capture the spike hour earns 7x the average.

**Implementation:** Monitor Hyperliquid's per-hour funding rate. When hourly rate exceeds 2x the 24-hour average, the spike is likely transient. Position to collect the elevated rate, then exit before it normalizes.

**Why it persists:** Most funding rate arb infrastructure is built for 8-hour cycles. The tooling to capitalize on hourly spikes is less developed. This is an **analytical edge** per [[edge-taxonomy]].

### Hidden Edge #2: Liquidation Heatmap Front-Running

On-chain transparency means liquidation levels are calculable for every position on Hyperliquid. Services like Coinglass aggregate this into heatmaps showing *exactly* where forced selling will occur.

**The play:** When price approaches a dense liquidation cluster, the cascade becomes almost inevitable (whales intentionally push price through to collect the forced selling). Position *ahead* of the cascade, then reverse when it exhausts.

**Sequence:**
1. Price approaching $98K support with 5,000+ BTC in liquidations between $97.5K-$98K
2. Short at $98.2K (expecting cascade trigger)
3. Cascade fires: price wicks to $97K as 5,000 BTC of longs are force-closed
4. Cover short at $97.2K
5. Go long at $97.2K (expecting reversal as forced selling exhausts)
6. Target: $98.5K (back inside range)

**Risk:** Cascade extends further than expected. Must have hard stops. This is inherently a **latency + informational edge** — you're using public but under-utilized data.

### Hidden Edge #3: TradFi Perps Basis vs Spot

Hyperliquid's TradFi perps (SP500, crude, gold, TSLA, NVDA) are priced via oracle feeds from traditional markets. But the Hyperliquid perp trades 24/7, while traditional markets have sessions.

**During off-hours (weekends, after NYSE close):** TradFi perps on Hyperliquid are the *only* price discovery mechanism. When traditional markets reopen, the Hyperliquid price must converge to the new spot.

**Opportunity:** If Hyperliquid's SP500 perp drifts 0.5% above fair value on Saturday night (due to crypto-native demand), it must correct Monday morning. Short on Saturday night, cover Monday at open. This is a **structural basis trade** that exists because Hyperliquid provides 24/7 trading on assets that normally trade 6.5 hours/day.

**Volume supports it:** xyz:CL did $414.5M and xyz:SP500 did $73.2M on April 6 — these are not illiquid markets.

### Hidden Edge #4: HYPE Token Reflexivity

[[hyperliquid|HYPE]] is the native token with $134.4M daily volume and 21.7M open interest. It's also the fee token, staking token, and governance token.

**Reflexive loop:** More trading volume → more fee revenue → more HYPE buyback/burn → higher HYPE price → more staking → more platform loyalty → more trading volume.

**Reversal risk:** Less volume → less revenue → HYPE price drops → staking less attractive → platform migration risk → less volume.

**Trading implication:** HYPE is a leveraged bet on Hyperliquid's volume. During platform growth phases (like current 70-80% DEX market share), HYPE outperforms crypto broadly. During platform decline, it underperforms. If you are bullish on Hyperliquid's dominance, HYPE is the highest-beta expression.

**Pair opportunity:** HYPE/BTC as a relative-value trade on DEX adoption vs broad crypto.

### Hidden Edge #5: Funding Rate as Contrarian Sentiment Indicator

From [[crypto-funding-rate-anomaly]]: extreme positive funding predicts lower returns over the next 1-3 days. Extreme negative funding predicts higher returns.

**On Hyperliquid specifically:** With hourly funding, you get 24 data points per day instead of 3. This makes the signal higher-resolution. A funding spike at 3am UTC may revert by 6am UTC. On Binance (8-hour snapshots), you'd miss this entirely.

**Implementation:**
```
Contrarian signal:
- If 1h funding > 3x 7-day average → expect mean-reversion → short bias
- If 1h funding < -2x 7-day average → expect bounce → long bias
- Combine with OI data: Funding spike + OI spike = crowded trade, reversal likely
```

---

## Part 5: Risk Management Framework for Hyperliquid Perps

### Position Sizing Rules

From [[kelly-criterion]], [[position-sizing]], [[risk-management-overview]]:

1. **Never risk >1-2% of total capital per trade.** On a $50K account, max loss = $500-$1,000.
2. **Position size = (Account × Risk%) / (Entry - Stop).** This derives naturally from the risk rule.
3. **Kelly fraction:** Use 1/4 to 1/2 Kelly. Full Kelly is too aggressive for non-ergodic systems (crypto).
4. **Maximum leverage:** 3-5x for directional trades. 1x for delta-neutral. Never 25-50x.
5. **Sub-account isolation:** Use Hyperliquid's sub-accounts to compartmentalize strategies. One blow-up should not cascade.

### Leverage Math (Why 50x Kills You)

From [[liquidation]], [[perpetual-futures]]:

| Leverage | Price Move to Liquidation |
|---|---|
| 2x | 50% |
| 5x | 20% |
| 10x | 10% |
| 20x | 5% |
| 50x | **2%** |

BTC's average daily range is 3-5%. At 50x, you are liquidated by a **normal day**. The wiki's [[failure-modes]] documents that leverage is the universal killer of every major arbitrage blow-up (LTCM, Volmageddon, Treasury basis, Tsingshan nickel).

### Margin Mode: Always Isolated

- **Isolated margin:** Only the margin allocated to this position is at risk. Account balance is safe.
- **Cross margin:** Entire account is collateral. One bad trade can wipe everything.
- **Rule:** Use isolated margin on Hyperliquid for every position. Accept the slightly higher liquidation risk per position in exchange for compartmentalization.

### Monitoring Checklist

| Signal | Source | Action Trigger |
|---|---|---|
| Funding rate (7d trailing) | Hyperliquid API | Negative → exit funding arb |
| Liquidation count (daily) | Coinglass | >20K → reduce sizing 50% |
| Open interest (24h change) | Hyperliquid API | OI drops >5% with price → cascade risk |
| Platform health | Hyperliquid status page | Any outage → withdraw excess capital |
| Whale concentration | On-chain analytics | Top trader >30% of OI → tail risk |
| Funding rate z-score (hourly) | Custom calculation | |z| > 3 → contrarian entry signal |

---

## Part 6: Portfolio Construction — Putting It Together

### Conservative Portfolio (target: 15% APY, <10% max drawdown)

| Strategy | Allocation | Expected Contribution | Regime |
|---|---|---|---|
| Funding rate arb (BTC+ETH) | 50% | 10-25% APY | Bull, Calm |
| Grid trading (BTC range) | 20% | 5-10% APY | Sideways |
| Cash / stablecoin reserve | 30% | 4-6% APY (lending) | All |

**Regime gap:** No crisis protection. Add a small trend-following allocation or accept the gap.

### Balanced Portfolio (target: 20% APY, <18% max drawdown)

| Strategy | Allocation | Expected Contribution | Regime |
|---|---|---|---|
| Trend-following (multi-asset) | 25% | 8-15% in trends | Trending |
| Mean reversion (RSI+BB) | 20% | 10-15% in chop | Sideways |
| Funding rate arb | 20% | 10-30% in bull | Bull, Calm |
| Liquidation hunting | 15% | 12-20% in vol | Crisis, Vol |
| Reserve | 20% | 4-6% (lending) | All |

**Regime coverage:** Trend covers trending. Mean reversion covers chop. Funding arb covers calm bull. Liquidation hunting covers crisis. Reserve provides buffer. All six regimes addressed.

### Aggressive Portfolio (target: 25%+ APY, <25% max drawdown)

| Strategy | Allocation | Expected Contribution | Regime |
|---|---|---|---|
| Trend-following (multi-asset) | 25% | 10-20% | Trending |
| Pairs trading (BTC/ETH + cross-asset) | 20% | 10-15% | All |
| Order flow scalping | 15% | 15-30% | High vol |
| Liquidation cascade trading | 15% | 15-25% | Crisis |
| Funding rate arb | 15% | 10-40% | Bull |
| Reserve | 10% | 4-6% | Buffer |

**Warning:** This portfolio requires active management, algorithmic infrastructure, and deep familiarity with order flow tools. Not suitable for passive deployment.

---

## Part 7: Strategy Decay & Kill Criteria

From [[failure-modes]] and [[when-to-retire-a-strategy]], adapted for Hyperliquid:

### Per-Strategy Kill Criteria

| Strategy | Kill When |
|---|---|
| Funding rate arb | 30-day annualized basis <5%; trailing 7-day funding negative |
| Grid trading | Price breaks grid bounds by >10%; 3 consecutive grid resets unprofitable |
| Trend-following | Rolling 6-month Sharpe <0; drawdown >25% |
| Mean reversion | Cointegration p-value >0.10 (pairs); out-of-sample win rate <45% |
| Liquidation hunting | Liquidation data feed becomes unreliable or delayed >5 minutes |
| Pairs trading | Cointegration breaks (re-test monthly); hedge ratio unstable (>20% change in 30 days) |

### Platform-Level Kill Criteria

| Signal | Action |
|---|---|
| Hyperliquid chain outage >1 hour | Withdraw 50% of capital |
| Regulatory announcement targeting Hyperliquid | Withdraw 100% within 24 hours |
| Smart contract exploit on HyperBVM | Withdraw 100% immediately |
| HYPE token drops >50% in 7 days | Reassess platform viability; reduce exposure |
| Daily volume drops below $1B for >30 days | Liquidity deterioration; reduce position sizes |

---

## Part 8: What This Wiki Says Will Kill You on Hyperliquid

The five fatal patterns from [[arbitrage-opportunity-map]] applied to Hyperliquid specifically:

1. **Leverage.** 50x is available. 50x means 2% moves liquidate you. BTC moves 3-5% on normal days. The math is clear. Use 1-5x maximum.

2. **Reflexivity.** Funding rate arb compressed from 30%+ (2017-2020) to single digits (2022) as more capital entered. If Hyperliquid's delta-neutral volume reaches a meaningful fraction of total OI, the funding rate itself will be suppressed by the arb. Monitor the ratio of known funding-arb positions to total OI.

3. **Platform risk replaces counterparty risk.** Self-custody eliminates FTX-style fraud. But HyperBVM smart contract risk, oracle manipulation, and validator centralization are new failure modes with no historical precedent. The risk is *different*, not *absent*.

4. **Correlation convergence in crisis.** BTC, ETH, SOL, HYPE, and all altcoins go to correlation 1.0 in panic. Crude, gold, and SP500 perps on Hyperliquid also correlate during true risk-off (everything sells). Only trend-following maintains negative crisis correlation. **Any portfolio without a trend/tail hedge is running disguised concentration risk.**

5. **Regulatory.** Hyperliquid offers stock perps (TSLA, NVDA, INTC) and commodity perps (crude, gold) without KYC. The SEC/CFTC have not yet acted, but this is the kind of product that attracts regulatory attention. A cease-and-desist or geo-fence expansion could happen without warning.

---

## Methodology

This analysis was produced on 2026-04-14 (last expanded 2026-06-20) by cross-referencing every wiki page relevant to perpetual futures, funding rates, Hyperliquid platform data, crypto market structure, and arbitrage strategies.

### How to use this map

1. **Pick the regime first** (Part 6 / [[regime-matrix]]) — regime-mismatch is the most common cause of strategy failure. The decision matrix in Strategy 10 maps regime → strategy set → sizing.
2. **Select from the Master Strategy Index** above — match the strategy's regime row to the current regime, then open its deep page for entry/exit/sizing rules.
3. **Wire the data feeds** — the recurring signal families are [[funding-rate]], [[open-interest]], [[liquidation]] tape, [[mark-price]]/[[hyperliquid-oracle-mechanics|oracle]] deviation, and depth. Cross-venue funding/OI/liquidations are available through aggregators such as [[coinglass]] and cryptodataapi.com (REST/WS); HL-native and execution-latency consumers read the [[hyperliquid]] API/websocket and [[hypurrscan]] directly.
4. **Apply the risk framework** (Part 5) — isolated margin, 1-5x max leverage, sub-account compartmentalization, the monitoring checklist.
5. **Watch the kill criteria** (Part 7) — per-strategy and platform-level. The platform-level criteria ([[hyperliquid]] chain outage, oracle exploit, regulatory action) override everything.

### Data-feed quick map

| Signal family | Free / native source | Aggregator option |
|---------------|----------------------|-------------------|
| [[funding-rate]] (HL hourly + CEX 8h) | HL API/WS; CEX APIs | [[coinglass]]; cryptodataapi.com |
| [[open-interest]] | HL API; [[hypurrscan]] | [[coinglass]]; cryptodataapi.com |
| [[liquidation]] tape | HL `userEvents`; CEX `forceOrder` etc. | [[coinglass]] (delayed) |
| [[mark-price]] / oracle deviation | HL on-chain (every block) | n/a — HL-unique, see [[hyperliquid-oracle-mechanics]] |
| Order-book depth | HL CLOB; CEX WS | n/a |

Key source pages are listed below.

## Sources

- [[hyperliquid]] — platform overview, metrics, architecture
- [[hyperliquid-market-snapshot-2026-04-06]] — live market data (April 6, 2026)
- [[2026-04-06-hyperliquid-volume-surge]] — volume surge event analysis
- [[funding-rate-arbitrage]] — delta-neutral funding strategy
- [[basis-trading]] — spot-futures convergence
- [[funding-rate]] — mechanics and interpretation
- [[perpetual-futures]] — perp mechanics, liquidation formulas
- [[liquidation]] — cascade mechanics
- [[long-liquidation]] — long-specific liquidation dynamics
- [[delta-neutral]] — hedging principles
- [[delta-neutral-yield-farming]] — multi-layer yield
- [[grid-trading]] — grid bot mechanics and risks
- [[cross-exchange-arbitrage]] — cross-venue execution
- [[cross-chain-arbitrage]] — cross-chain mechanics
- [[mev-strategies]] — MEV extraction on DEXs
- [[regime-matrix]] — strategy-regime mapping
- [[strategy-correlation-matrix]] — crisis correlation analysis
- [[edge-taxonomy]] — six sources of trading edge
- [[failure-modes]] — how strategies die
- [[crypto-funding-rate-anomaly]] — funding rate as anomaly
- [[trend-following-cta]] — trend-following implementation
- [[mean-reversion]] — mean-reversion mechanics
- [[pairs-trading]] — cointegration-based pairs
- [[stop-hunting-and-liquidity-sweeps]] — liquidation hunting
- [[contrarian-extremes]] — fading panic
- [[regime-adaptive-strategy]] — regime switching
- [[hyperliquid-vs-dydx-vs-gmx]] — DEX comparison
- [[hyperliquid-vs-asterdex-vs-tiger-brokers]] — multi-platform comparison
- [[order-flow]] — order flow mechanics
- [[footprint-charts]] — footprint analysis
- [[tape-reading]] — tape reading techniques
- [[market-making]] — market making overview
- [[arbitrage-opportunity-map]] — parent wiki-wide arbitrage synthesis
- [[hl-vs-cex-funding-divergence]] — Strategy 4 deep page (cross-venue funding arb)
- [[hyperliquid-hlp-basis-arbitrage]] — HLP-aware HL strategy family
- [[hyperliquid-oracle-mechanics]] — oracle / mark-price construction and manipulation surface
- [[hyperliquid-liquidation-engine]] — liquidation engine internals
- [[hyperliquid-funding-rate-microstructure]] — HL hourly vs CEX 8h cadence detail
- [[cascade-detection-signals]] — three-stage cascade detector (signals, thresholds, feeds)
- [[liquidation-cascade-fade]] — cascade-exhaustion fade
- [[liquidation-cascade-arbitrage]] — keeper-bot cascade arb
- [[hlp-cascade-alongside-playbook]] — HLP-hedge overlay
- [[hyperliquid-tradfi-perp-weekend-basis]] — off-session TradFi basis (Hidden Edge #3)
- [[open-interest]] — flow / cascade-exhaustion metric
- [[mark-price]] — mark vs oracle vs index
- [[hypurrscan]] — HL on-chain analytics
- [[coinglass]] — cross-venue funding / OI / liquidation aggregator
- [[trading-strategy-baskets]] — portfolio context for the HL basket
