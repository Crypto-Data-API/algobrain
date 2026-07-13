---
title: "Arbitrage Opportunity Map"
type: concept
created: 2026-04-14
updated: 2026-06-20
status: excellent
tags: [strategy-development, arbitrage, portfolio-construction, regime-detection, risk-premia, research]
aliases: ["Arb Map", "Arbitrage Synthesis", "Cross-Wiki Arbitrage Analysis"]
domain: [strategy-development]
difficulty: advanced
related: ["[[edge-taxonomy]]", "[[regime-matrix]]", "[[strategy-correlation-matrix]]", "[[failure-modes]]", "[[arbitrage-overview]]", "[[anomalies-overview]]", "[[research-checklist]]"]
---

# Arbitrage Opportunity Map

A cross-wiki synthesis of every arbitrage opportunity — explicit, implicit, and hidden — identified by reading all strategy, concept, microstructure, anomaly, news, and source pages together. Individual strategy pages document *how* each trade works. This page maps *where* the opportunities cluster, *why* they persist, *how* they combine, and *what* kills them.

The goal: move beyond isolated strategy descriptions toward a unified map of where mispricings exist, which ones compound, which ones hedge each other, and which ones are traps.

### How to Use This Map

| If you want to know… | Read… |
|---|---|
| What explicit arb strategies exist and their metrics | [Part 1: The Explicit Catalog](#part-1-the-explicit-catalog) |
| Opportunities no single page documents | [Part 2: Hidden Opportunities](#part-2-hidden-opportunities-cross-page-synthesis) |
| The single most important structural finding | [Part 3: Portfolio Construction Arbitrage](#part-3-the-deepest-hidden-opportunity--portfolio-construction-arbitrage) |
| The raw anomalies arbitrage feeds on, with decay | [Part 4: The Anomaly Basis](#part-4-the-anomaly-basis) |
| The five ways arbitrage dies | [Part 5: What Kills Arbitrage](#part-5-what-kills-arbitrage-failure-pattern-catalog) |
| What is tradeable right now | [Part 6: Current Opportunity Assessment](#part-6-current-opportunity-assessment-april-2026) |
| How to go from this map to a sized position | [Part 7: From Map to Position](#part-7-from-map-to-position-a-decision-framework) |

This map is the cross-asset, cross-strategy synthesis. For venue-specific perp playbooks see [[asterdex-perp-trading-map]] and [[hyperliquid-perp-trading-map]]; for the Solana spot/memecoin meta see [[low-cap-crypto-trading-map]]; for the discretionary trade-construction process see [[itpm-trade-construction-playbook]]; for the execution plumbing see [[exchange-api-reference]] and [[defi-contract-registry]].

---

## Part 1: The Explicit Catalog

The wiki documents **26+ explicit arbitrage strategies** across `wiki/strategies/arbitrage/`. Summary with key metrics:

### Pure / Deterministic Arbitrage

| Strategy | Expected Return | Win Rate | Capital Required | Crowding | Edge Source |
|---|---|---|---|---|---|
| [[cash-and-carry|Cash-and-carry]] | 5-25% APR (crypto) | ~99% | High | Medium | Structural |
| [[funding-rate-arbitrage|Funding rate arb]] | 10-50% APY (bull) | 85-95% | Medium | High | Structural + risk-bearing |
| [[cross-exchange-arbitrage|Cross-exchange arb]] | 0.1-2% per trade | 80-95% | Medium | Extreme (HFT) | Latency |
| [[cross-chain-arbitrage|Cross-chain arb]] | 10-30% APY | 70-90% | $10K-$50M | Medium | Structural + latency |
| [[triangular-arbitrage|Triangular arb]] | 0.01-0.5% per loop | 90-99% | Medium-High | Extreme | Latency |
| [[flash-loan-arbitrage|Flash loan arb]] | Variable (high) | Atomic | Zero capital | Extreme | Latency + analytical |
| Index arb | 5-10 bps per trade | High | Very High | Extreme | Structural |
| [[etf-arbitrage|ETF arb]] | Variable | High | Very High (AP only) | Low | Structural |
| [[convergence-arbitrage|Convergence arb]] | 1-3% unlevered | ~85% | Very High | Medium | Analytical + risk-bearing |

### Commodity Processing Spreads

| Strategy | Expected Return | Seasonality | Capital Required | Crowding | Edge Source |
|---|---|---|---|---|---|
| [[crack-spread|Crack spread]] | $8-30/barrel | Summer peak | $500K+ | Low | Structural |
| [[crush-spread|Crush spread]] | $1-2/bushel | Harvest cycle | $50K+ | Low | Structural |
| [[spark-spread|Spark spread]] | Extreme spikes | Summer/winter | $1M+ | Low | Structural + informational |
| [[geographic-spread-trading|Geographic spreads]] | Variable | Trade flow | $500K-$1B | Low | Structural + informational |

### Risk / Event Arbitrage

| Strategy | Expected Return | Win Rate | Capital Required | Crowding | Edge Source |
|---|---|---|---|---|---|
| Merger arb | 5-15% annualized | 85-92% | High | Low-medium | Structural |
| Convertible arb | 6-12% annualized | ~70% | Very High | Medium | Analytical + structural |
| [[pairs-trading|Pairs trading]] | 5-15% annual | ~60% | Medium | High | Analytical + behavioral |
| [[statistical-arbitrage|Stat arb]] | 10-30% annual | ~55% | High | High | Analytical |
| Dispersion trading | Variable | 65-75% | Very High | Medium | Analytical + risk-bearing |

### DeFi / Crypto-Native

| Strategy | Expected Return | Win Rate | Capital Required | Crowding | Edge Source |
|---|---|---|---|---|---|
| [[staking-yield-arbitrage|Staking yield arb]] | 9-16% combined | ~80% | Medium | Medium | Structural + risk-bearing |
| [[delta-neutral-yield-farming|Delta-neutral DeFi]] | 10-40%+ APY (bull) | ~85% | Medium | Medium | Structural |
| [[mev-strategies|MEV extraction]] | Variable (high) | High | Low-Medium | Extreme | Latency + analytical |
| [[nft-arbitrage|NFT arb]] | Variable | ~60% | Medium | Low | Informational |

---

## Part 2: Hidden Opportunities (Cross-Page Synthesis)

These opportunities are not documented on any single wiki page. They emerge from reading across pages and connecting patterns that individual strategy descriptions miss.

### Hidden Opportunity #1: The Regime-Arbitrage Mismatch

The [[regime-matrix]] reveals a structural clustering that no individual page states:

**Almost every carry/yield strategy** (funding rate arb, basis trading, DeFi yield farming, covered calls, cash-secured puts) **clusters in the same regime**: calm bull / low vol. They ALL show ❌ in high-vol and risk-off.

Meanwhile, **structural arbitrage** (index arb, ETF arb, triangular arb, cross-exchange arb) **all show ✅ in high-vol**.

The implication: when carry strategies are printing money (calm bull), structural arb margins are compressed. When carry strategies blow up (crisis), structural arb opportunities explode. A portfolio running carry in calm periods + structural arb in crisis periods has natural regime complementarity.

This is a **meta-arbitrage** — arbitraging the correlation of strategy returns across regimes. The regime matrix maps it, but no single page frames it as a tradeable insight. See [[regime-adaptive-strategy]] for the switching mechanism.

### Hidden Opportunity #2: Contrarian-Extremes as Mis-Categorized Risk-Bearing

In the [[regime-matrix]], [[contrarian-extremes]] is the only mean-reversion strategy showing ✅ in high-vol and ✅ in risk-off — the *exact opposite* of every other mean-reversion strategy (which all show ❌ or ➖ in those regimes).

Cross-referencing with [[edge-taxonomy]]: contrarian-extremes is actually **liquidity provision during panic** — buying when forced sellers must exit. This maps to "risk-bearing edge," not behavioral mean-reversion.

**Portfolio construction implication:** its tail correlation with other mean-reversion strategies is likely *negative*, not positive — the opposite of what the [[quant-meltdown-2007]] pattern suggests. This makes it a valid crisis diversifier within a mean-reversion book, unlike [[pairs-trading]] or [[statistical-arbitrage]] which all blow up together in stress (see [[strategy-correlation-matrix]]).

### Hidden Opportunity #3: DeFi Yield Stacking Reflexivity (and Its Inverse)

The wiki documents crypto yield stacking (staking + restaking + LP + points) yielding 15%+ on the same capital. But cross-referencing [[failure-modes]], the [[2022-05-terra-luna-depeg-arb|Terra/LUNA case study]], and [[2020-2024-bridge-exploits|bridge exploit data]] ($2.5B+ lost) reveals:

**Every layer of yield stacking adds a new reflexivity loop.** When confidence exits one layer, it cascades through all layers because they share the same underlying collateral. Cross-protocol composability isn't free diversification — it's **correlated smart contract risk**.

The actual hidden opportunity is **the reverse**: being short/hedged on multi-layer DeFi positions during bull-to-bear transitions. The [[staking-yield-arbitrage|stETH depeg trade]] of June 2022 (bought at 5-7% discount, earned 9-11% return) was betting *against* the yield stack when it broke. This is a repeatable pattern whenever DeFi TVL concentrates in recursive yield structures.

### Hidden Opportunity #4: The Volmageddon Echo Pattern

The wiki documents [[flash-crashes|Volmageddon]] (Feb 2018), [[convergence-arbitrage|LTCM]] (1998), and the [[quant-meltdown-2007]] as separate events. Read together, they reveal a recurring structural pattern:

1. A popular strategy compresses its own source of return by sheer size (XIV/SVXY suppressed VIX; LTCM compressed bond spreads; stat arb funds compressed pairs spreads)
2. The strategy's AUM approaches a meaningful fraction of daily market volume
3. A modest adverse move triggers forced rebalancing
4. Forced rebalancing *causes* further adverse moves ([[reflexivity]])
5. Cascade destroys the strategy and creates enormous opportunity for the *opposite* position

**Tradeable signal:** monitor the ratio of strategy AUM to underlying market volume. When any single strategy or product cluster approaches >10% of daily volume, the forced-rebalancing feedback loop becomes structurally inevitable.

Current candidates to watch (as of April 2026):
- Treasury basis trade: $1T+ notional, 10-50x leverage standard
- Short-vol ETPs: rebuilt post-2018 but smaller
- Leveraged crypto derivatives: 17,214 liquidations/day on [[hyperliquid]] alone (April 6 data)

### Hidden Opportunity #5: New Kimchi Premiums from Regulatory Barriers

The [[2017-2021-kimchi-premium|Kimchi Premium]] page documents a 40% BTC premium in Korea persisting for *years* due to capital controls. Cross-referencing with current events:

- Russian sanctions create persistent crypto premium/discount in ruble markets
- Chinese capital controls create persistent A-share/H-share spreads
- The [[2025-04-02-liberation-day-tariffs|tariff regime]] has disrupted commodity trade flows (soybeans to China fell 78%)
- Hyperliquid now lists traditional assets (stocks, commodities) as perps alongside crypto, creating new cross-venue basis

These are modern versions of the Kimchi Premium: **regulatory barriers creating persistent mispricings**. The Shleifer & Vishny [[market-efficiency|limits to arbitrage]] framework says the premium compensates for barrier risk. If you can find a legal way through the barrier, the premium is yours.

### Hidden Opportunity #6: Pre-FOMC Drift + Funding Rate Compound Trade

The [[anomalies-overview|anomalies library]] documents the pre-FOMC drift (~50 bps in 24 hours, 8 times/year, ~80% of equity risk premium). The [[funding-rate-arbitrage]] page documents crypto funding rates spiking during bullish positioning.

No page connects them, but: **FOMC days are when crypto funding rates are most volatile.** A rate cut triggers risk-on, crypto longs pile in, funding rates spike. A hawkish surprise triggers the opposite.

Compound trade: position for pre-FOMC equity drift (long S&P futures 2pm day before) AND pre-position crypto funding rate arb to capture the post-announcement funding spike. Same macro catalyst, two uncorrelated profit mechanisms across two asset classes.

### Hidden Opportunity #7: Token-Unlock Forced-Flow Screening

The demerger playbook generalizes to crypto: [[token-unlock-arbitrage]] events create the same structural catalyst pattern — forced selling pressure, mechanical rebalancing, and coverage gaps around unlock dates. Cross-referencing the [[token-unlocks]] calendar with fundamental protocol screens (revenue via Token Terminal, TVL trend, holder concentration) identifies which post-unlock selloffs are genuinely cheap protocols being mispriced by mechanical flows versus fair repricings of low-float tokens (informational + structural edge).

---

## Part 3: The Deepest Hidden Opportunity — Portfolio Construction Arbitrage

The most important finding comes from the [[strategy-correlation-matrix]]. Crisis-conditional correlation data:

**Normal times (full-period):**

| | Trend | MeanRev | Carry | LS Equity | Vol Sell |
|---|---|---|---|---|---|
| Trend | 1.00 | -0.10 | 0.05 | 0.02 | -0.20 |
| MeanRev | -0.10 | 1.00 | 0.15 | 0.30 | 0.40 |
| Carry | 0.05 | 0.15 | 1.00 | 0.20 | 0.55 |
| Vol Sell | -0.20 | 0.40 | 0.55 | 0.25 | 1.00 |

**Crisis times (VIX > 25):**

| | Trend | MeanRev | Carry | LS Equity | Vol Sell |
|---|---|---|---|---|---|
| Trend | 1.00 | -0.30 | -0.15 | -0.20 | -0.50 |
| MeanRev | -0.30 | 1.00 | **0.65** | **0.70** | **0.85** |
| Carry | -0.15 | **0.65** | 1.00 | **0.55** | **0.80** |
| Vol Sell | -0.50 | **0.85** | **0.80** | **0.65** | 1.00 |

**Trend-following is the ONLY true diversifier in crisis.** Its conditional correlations go *more negative* when everything else correlates to 1.0.

> The deepest "arbitrage" in the wiki is not a single trade — it is the **portfolio construction arbitrage** of combining carry strategies (which earn premium in calm) with trend-following (which earns premium in crisis). The two harvest *different risk premia* from *different market participants* in *different regimes*, and their correlation structure means combining them produces dramatically better risk-adjusted returns than either alone.

The [[regime-matrix]] confirms this: **Trend + Carry + Tail Hedge covers all six regimes.** The [[failure-modes]] page confirms that carry strategies die from regime change (mode #3), which is exactly when trend-following activates. This isn't a trade — it's a **permanent structural allocation** hiding in plain sight across 6+ pages.

Supporting evidence:
- Portfolio Sharpe formula: S × √N where N = truly uncorrelated strategies
- Pod shops ([[citadel]], [[millennium-management]]) operate 50-200+ independent strategies for this reason
- Combination of 4-6 uncorrelated strategies historically produces Sharpe 1.5-2.0+

---

## Part 4: The Anomaly Basis

Documented market anomalies that serve as raw material for arbitrage, with decay data:

| Anomaly | Peak Magnitude | Current Magnitude | Decay Speed | Mechanism |
|---|---|---|---|---|
| [[momentum-anomaly|Momentum]] | ~1%/month | 0.2-0.3%/month | Medium | Behavioral (underreaction) |
| PEAD | 3-4% / 60d | ~1% / 60d | Medium-slow | Behavioral (anchoring) |
| [[volatility-risk-premium|VRP]] | 0.8-1.0 Sharpe | 0.4-0.6 Sharpe | Slow | Risk-bearing (fear premium) |
| [[carry-anomaly|Carry]] | 0.8 Sharpe | 0.5 Sharpe | Variable | Risk-bearing (yield compensation) |
| [[low-volatility-anomaly|Low-vol]] | 1.0 Sharpe | 0.4-0.6 Sharpe | Slow | Behavioral (lottery preference) |
| Value | 5%/year | 0.3-0.5 Sharpe | Very slow | Behavioral + structural |
| Index inclusion | 3-5% | 0.5-1% | Slow | Structural (forced flow) |
| Pre-FOMC drift | ~50 bps/24h | Compressed | Slow | Unknown (possibly informational) |
| Turn-of-month | 0.8%/window | Decayed | Medium | Structural (pension flows) |
| Crypto funding rate | 20-100% APY (peak) | 10-40% APY | Mild | Structural (leverage demand) |

**Key finding** from [[data-snooping-and-p-hacking|McLean-Pontiff (2016)]]: published anomalies lose ~26% of their effect post-publication. Structural anomalies (forced flows) decay slower than behavioral ones.

---

## Part 5: What Kills Arbitrage (Failure Pattern Catalog)

Every arbitrage failure in the wiki follows one of five patterns. These are the kill conditions to monitor:

### Pattern 1: Leverage Amplification

Every catastrophic arb failure involved leverage amplifying a modest adverse move:
- [[convergence-arbitrage|LTCM]] at 25:1 (1998) — lost $4.6B
- Treasury basis at 10-50x — systemic risk flagged by regulators
- [[flash-crashes|XIV]] leveraged inverse (2018) — lost 96% in one day
- Tsingshan nickel (2022) — oversized short triggered LME intervention

**Rule:** if the strategy requires >3x leverage for acceptable returns, the failure mode is probably leverage itself.

### Pattern 2: Reflexivity Loops

Stabilization mechanisms becoming destabilizers:
- [[2022-05-terra-luna-depeg-arb|Terra/LUNA]]: arb mechanism *caused* the death spiral ($40B destroyed)
- [[flash-crashes|Volmageddon]]: short-vol products *suppressed* vol, then forced rebalancing *caused* the vol spike ($8-15B+ losses)
- [[lme-nickel-squeeze-2022|Nickel squeeze]]: margin calls → covering → price up → more margin calls

**Rule:** when the size of a position is large enough to influence the price of the thing it's trading, [[reflexivity]] has entered the equation.

### Pattern 3: Exchange Rule Changes

Rules change without warning, destroying positions mid-trade:
- LME cancelled $3.9B in nickel trades (2022)
- COMEX imposed "liquidation only" on the Hunt brothers (1980)
- SEC banned short-selling (2008)
- Decimalization destroyed fractional-spread strategies overnight (2001)

**Rule:** if the strategy depends on exchange/regulatory rules staying constant, carry an explicit "rule change" risk premium in your sizing.

### Pattern 4: Counterparty Destruction

- FTX collapse destroyed billions in basis positions (2022)
- Bridge exploits total $2.5B+ ([[2020-2024-bridge-exploits]])
- No delta-neutral position survives the exchange holding your collateral disappearing

**Rule:** diversify counterparty exposure. Maximum 20-30% of arb capital per exchange.

### Pattern 5: Correlation Convergence

From [[strategy-correlation-matrix]]: all correlations approach 1.0 in crisis — except trend-following, which goes to -1.0. Any "diversified" arb portfolio without an explicit crisis hedge is running disguised concentration risk.

**Rule:** measure conditional (VIX > 25) correlations, not full-period correlations. Use the Meucci "effective number of bets" formula to find true diversification.

---

## Part 6: Current Opportunity Assessment (April 2026)

Based on wiki content cross-referenced against current market events:

### Highest Conviction, Lowest Crowding

1. **Geographic commodity spreads** — [[2026-03-iran-conflict-oil-spike|Iran conflict]] has crude at $100-120. WTI-Brent basis dislocated. Soybean trade flows disrupted by [[2025-04-02-liberation-day-tariffs|tariffs]]. Spark spreads volatile from weather + geopolitics. Capacity $500M-$1B. Few retail participants.

2. **Contrarian-extremes on tariff-whipsawed sectors** — The [[2026-02-supreme-court-tariffs|Feb 2026 Supreme Court ruling]] + Trump 15% tariff reversal created massive sector rotations in days. Industrials gapped 3-5% both directions. Buy the forced sellers per [[contrarian-extremes]] framework.

3. **Token-unlock forced-flow screening** — Structural catalyst + fundamental undervaluation, crypto-native: screen the unlock calendar against protocol fundamentals to separate mechanical selloffs from fair repricings.

### Highest Return, Moderate Risk

4. **Crypto funding rate arb with regime overlay** — 10-40% APY in bull markets. Add [[regime-detection]] layer (HMM claims 1-3 day advance signal on transitions). Exit immediately when regime shifts to bear.

5. **Dispersion trading with tail hedge** — Short index vol, long single-stock vol. 65-75% win rate. [[volatility-risk-premium|VRP]] of 3-5 percentage points. MUST carry tail hedges per [[flash-crashes|Volmageddon]] lesson.

6. **Trend + Carry + Tail Hedge permanent allocation** — Not a trade but a structural portfolio. The [[strategy-correlation-matrix]] proves it is regime-complete. Closest thing to a free lunch the wiki documents.

### Research Required

7. **Pre-FOMC drift + crypto funding spike combo** — Same macro catalyst, two uncorrelated profit mechanisms. Needs backtesting per [[research-checklist]].

8. **AUM-to-volume concentration monitor** — Front-run the next Volmageddon by monitoring when strategy clusters approach >10% of daily underlying volume. Needs data pipeline.

9. **New Kimchi Premiums** — Sanction/tariff barriers creating persistent cross-venue basis. Needs legal analysis of barrier-crossing feasibility.

### Traps to Avoid

- **Short volatility without tail hedges** — Volmageddon cost $8-15B+
- **Extreme crypto leverage** (>3x) — 17,214 daily liquidations on Hyperliquid alone
- **Concentrated commodity shorts** — LME/Hunt brothers pattern repeats
- **Multi-layer DeFi yield stacking in late bull** — Terra/LUNA pattern; reflexivity destroys all layers simultaneously
- **Chasing legal resolutions to policy uncertainty** — Supreme Court tariff ruling proved futile; administration immediately found alternative authority

---

## Part 7: From Map to Position — A Decision Framework

This map identifies *where* opportunities cluster. Converting a cluster into a sized position requires a repeatable filter. The sequence:

```
Step 1 — Classify the edge (see [[edge-taxonomy]])
  Structural / latency  → decays slowly; capacity-limited; crowding is the risk
  Behavioral            → decays post-publication (~26%, McLean-Pontiff); needs catalyst
  Risk-bearing          → durable but pays you for tail risk you must survive

Step 2 — Map the regime (see [[regime-matrix]])
  Carry/yield cluster   → only in calm bull; ❌ in high-vol & risk-off
  Structural arb        → ✅ in high-vol (margins widen in crisis)
  Trend-following       → the ONLY crisis diversifier (see Part 3)

Step 3 — Check the kill conditions (Part 5)
  Leverage > 3x?        → assume the failure mode IS leverage
  Position influences price?  → reflexivity has entered; size down
  Depends on a rule?    → carry an explicit rule-change premium
  Single counterparty > 20-30%?  → diversify venues

Step 4 — Size for true diversification (see [[strategy-correlation-matrix]])
  Use CONDITIONAL (VIX>25) correlations, not full-period
  Combine carry (calm) + trend (crisis) for regime completeness
  Target 4-6 truly uncorrelated sleeves → Sharpe 1.5-2.0
```

### Strategy Selection Cheat Sheet

| Your situation | Cluster to look at | Primary risk to pre-hedge |
|---|---|---|
| Calm bull, want yield | Carry: [[funding-rate-arbitrage]], [[cash-and-carry]], [[delta-neutral-yield-farming]] | Regime change → pair with trend |
| Expecting a vol spike / crisis | Structural: index-arbitrage, [[triangular-arbitrage]], [[cross-exchange-arbitrage]]; plus [[contrarian-extremes]] | Counterparty failure, rule changes |
| Want a permanent allocation | Trend + Carry + Tail Hedge (Part 3) | Underperformance of trend in calm |
| Event with a known date | merger-arbitrage, pre-FOMC drift, convertible-arbitrage | Deal break / catalyst slip |
| Crypto-native capital | Crypto carry + [[mev-strategies]] + [[cross-chain-arbitrage]] | Bridge exploit, reflexivity |
| Commodity exposure | [[crack-spread]], [[crush-spread]], [[geographic-spread-trading]] | Concentrated short squeeze |

The governing rule across all six rows: **never run a single-cluster book.** Part 3 proves that the deepest edge in this wiki is not any single trade but the *combination* of clusters that harvest different risk premia in different regimes.

---

## Methodology

This analysis was produced by a full cross-wiki synthesis on 2026-04-14, reading every page in:
- `wiki/strategies/` (all subdirectories)
- `wiki/concepts/market-microstructure/`, `anomalies/`, `risk-management/`, `behavioral-finance/`, `portfolio-theory/`
- `wiki/strategy-development/`
- `wiki/news/`, `wiki/history/`
- `wiki/sources/`, `wiki/markets/`
- `wiki/ai-trading/`

Cross-references were identified by matching edge sources, regime profiles, failure modes, and correlation data across pages that do not directly link to each other. Hidden opportunities are patterns that emerge from the *intersection* of multiple pages rather than from any single page.

## Sources

- [[edge-taxonomy]] — six categories of trading edge
- [[regime-matrix]] — strategy performance by market regime
- [[strategy-correlation-matrix]] — normal vs. crisis correlations
- [[failure-modes]] — how strategies die
- [[arbitrage-overview]] — explicit strategy catalog
- [[anomalies-overview]] — documented market inefficiencies
- [[2022-05-terra-luna-depeg-arb]] — reflexivity case study
- [[flash-crashes]] — Volmageddon, 2010, crypto cascades
- [[2017-2021-kimchi-premium]] — persistent regulatory mispricing
- [[convergence-arbitrage]] — LTCM case study

## Related

- [[asterdex-perp-trading-map]] — venue-specific perp playbook (private order book)
- [[hyperliquid-perp-trading-map]] — venue-specific perp playbook (transparent book)
- [[low-cap-crypto-trading-map]] — Solana spot/memecoin meta map
- [[itpm-trade-construction-playbook]] — discretionary trade-construction process
- [[exchange-api-reference]] — endpoints/feeds for CEX/DEX arbitrage execution
- [[defi-contract-registry]] — contract addresses for on-chain arbitrage execution
- [[edge-taxonomy]] · [[regime-matrix]] · [[strategy-correlation-matrix]] · [[failure-modes]] · [[arbitrage-overview]] · [[anomalies-overview]] · [[research-checklist]] · [[regime-adaptive-strategy]] · [[regime-detection]]
