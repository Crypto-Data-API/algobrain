---
title: "Arbitrage Strategy Correlation Matrix"
type: strategy
created: 2026-04-20
updated: 2026-06-21
status: excellent
tags: [arbitrage, portfolio-theory, risk-management, quantitative, strategy-development]
aliases: ["Arb Correlations", "Arbitrage Portfolio Construction"]
strategy_type: quantitative
timeframe: position|long-term
markets: [crypto, stocks, futures, options]
complexity: advanced
backtest_status: untested
related: ["[[strategy-correlation-matrix]]", "[[arbitrage-overview]]", "[[arbitrage-opportunity-map]]", "[[regime-matrix]]", "[[arbitrage-live-performance]]", "[[crowding-indicators]]", "[[failure-modes]]", "[[portfolio-theory]]", "[[arbitrage]]", "[[limits-to-arbitrage]]", "[[convergence-arbitrage]]"]
---

# Arbitrage Strategy Correlation Matrix

The [[strategy-correlation-matrix]] demonstrates that strategies appearing uncorrelated in normal markets can become highly correlated in crisis. This page applies that framework specifically to **arbitrage strategies**, answering: if you run multiple arbs, how many truly independent bets do you have? The short answer — and the recurring theme of [[limits-to-arbitrage]] — is *far fewer than the count of strategies suggests*, because most arbs are secretly long the same hidden factor: liquidity. When liquidity evaporates, supposedly independent [[convergence-arbitrage|convergence trades]] all lose at once. This page is the methodology hub for combining the individual arb strategies in this folder into a portfolio that does not quietly collapse to a single bet.

> **How to use this page:** treat the matrices as a *framework*, not gospel numbers. The workflow is: (1) classify each arb you run by its underlying risk factor (see "What Drives Correlations"); (2) estimate its crisis-conditional correlation to the rest of the book; (3) compute the effective number of bets; (4) size using the conditional-correlation rule, not the full-period one. The single biggest mistake in arb portfolio construction is counting strategies instead of counting factors.

> **Data basis:** The correlations below are estimated from observable market characteristics and regime analysis, cross-referenced with published academic studies on arb strategy returns (Gatev et al. 2006 for pairs, Mitchell & Pulvino 2001 for merger arb, Duarte et al. 2007 for fixed income arb). They are well-informed estimates, not proprietary trading data. Use them as starting points for your own empirical calibration with [[historical-spread-data]].

---

## Full-Period Correlation (Estimated, Normal Market Conditions)

Returns measured as daily P&L of each strategy run at standard parameters.

| | Cash-Carry | Funding Arb | Cross-Exch | Cross-Chain | Pairs (Crypto) | Merger Arb | Vol Arb | Flash Loan |
|---|---|---|---|---|---|---|---|---|
| **Cash-Carry** | 1.00 | **0.85** | 0.30 | 0.40 | 0.15 | 0.05 | 0.10 | 0.05 |
| **Funding Arb** | 0.85 | 1.00 | 0.35 | 0.45 | 0.20 | 0.05 | 0.10 | 0.08 |
| **Cross-Exch** | 0.30 | 0.35 | 1.00 | **0.55** | 0.25 | 0.00 | 0.30 | **0.60** |
| **Cross-Chain** | 0.40 | 0.45 | 0.55 | 1.00 | 0.20 | 0.00 | 0.25 | 0.50 |
| **Pairs (Crypto)** | 0.15 | 0.20 | 0.25 | 0.20 | 1.00 | 0.10 | 0.20 | 0.10 |
| **Merger Arb** | 0.05 | 0.05 | 0.00 | 0.00 | 0.10 | 1.00 | 0.15 | 0.00 |
| **Vol Arb** | 0.10 | 0.10 | 0.30 | 0.25 | 0.20 | 0.15 | 1.00 | 0.15 |
| **Flash Loan** | 0.05 | 0.08 | 0.60 | 0.50 | 0.10 | 0.00 | 0.15 | 1.00 |

### Key Clusters (Normal Conditions)

**Cluster 1: Carry strategies (correlation 0.85)**
- Cash-and-carry + Funding rate arb are **essentially the same bet** — both profit from bullish leverage demand in crypto. Running both does NOT provide diversification.

**Cluster 2: Volatility/dislocation strategies (correlation 0.55-0.60)**
- Cross-exchange + Cross-chain + Flash loan arb all profit from **price dislocations**, which increase with volatility and DEX activity. These are correlated because the same market conditions (high volume, high vol) drive all three.

**Cluster 3: Uncorrelated**
- Merger arb has near-zero correlation with all crypto strategies — it's driven by corporate deal flow, not crypto market conditions.
- Vol arb is moderately uncorrelated — driven by IV-RV spread dynamics, partially independent of crypto.

---

## Crisis-Conditional Correlation (VIX > 25 or BTC drawdown > 20%)

When markets stress, correlations change dramatically — usually toward +1.0.

| | Cash-Carry | Funding Arb | Cross-Exch | Cross-Chain | Pairs (Crypto) | Merger Arb | Vol Arb | Flash Loan |
|---|---|---|---|---|---|---|---|---|
| **Cash-Carry** | 1.00 | **0.95** | 0.50 | **0.65** | 0.40 | 0.20 | 0.35 | 0.15 |
| **Funding Arb** | 0.95 | 1.00 | 0.55 | **0.70** | 0.45 | 0.20 | 0.35 | 0.20 |
| **Cross-Exch** | 0.50 | 0.55 | 1.00 | **0.75** | 0.40 | 0.10 | **0.60** | **0.80** |
| **Cross-Chain** | 0.65 | 0.70 | 0.75 | 1.00 | 0.45 | 0.10 | 0.50 | **0.70** |
| **Pairs (Crypto)** | 0.40 | 0.45 | 0.40 | 0.45 | 1.00 | 0.25 | **0.55** | 0.20 |
| **Merger Arb** | 0.20 | 0.20 | 0.10 | 0.10 | 0.25 | 1.00 | 0.30 | 0.05 |
| **Vol Arb** | 0.35 | 0.35 | 0.60 | 0.50 | 0.55 | 0.30 | 1.00 | 0.35 |
| **Flash Loan** | 0.15 | 0.20 | 0.80 | 0.70 | 0.20 | 0.05 | 0.35 | 1.00 |

### What Changes in Crisis

| Relationship | Normal | Crisis | Why |
|---|---|---|---|
| Cash-Carry ↔ Funding Arb | 0.85 | **0.95** | Both die simultaneously when funding inverts in a bear market |
| Cross-Exchange ↔ Flash Loan | 0.60 | **0.80** | Both surge when volatility creates large dislocations |
| Pairs (Crypto) ↔ Vol Arb | 0.20 | **0.55** | Mean-reversion strategies break when correlations spike to 1.0 (see [[quant-meltdown-2007]]) |
| Cash-Carry ↔ Cross-Chain | 0.40 | **0.65** | Both depend on crypto infrastructure trust; crisis erodes trust |
| **Merger Arb ↔ everything** | 0.00-0.15 | 0.10-0.30 | Merger arb rises moderately but stays lowest-correlated |

### The Correlation Trap

An arb portfolio of **Cash-Carry + Funding Arb + Cross-Chain + Cross-Exchange** looks diversified in normal markets (4 strategies). In crisis, it becomes **~2.5 effective bets** because carry strategies correlate to 0.95 and dislocation strategies correlate to 0.75-0.80.

Using the Meucci effective bets formula:
```
Normal: 4 strategies → ~3.2 effective bets (good diversification)
Crisis: 4 strategies → ~2.0 effective bets (concentrated)
```

---

## Effective Number of Bets

The Meucci (2009) effective number of bets, N*, measures true portfolio diversification using eigenvalue decomposition of the correlation matrix:

| Portfolio | Strategies | N* (Normal) | N* (Crisis) | Assessment |
|---|---|---|---|---|
| Carry-only (Cash-Carry + Funding Arb) | 2 | ~1.1 | ~1.0 | **One bet disguised as two** |
| Crypto arb (Carry + Cross-Exchange + Cross-Chain) | 3 | ~2.3 | ~1.6 | Moderate diversification, degrades in crisis |
| Crypto + Equity (Carry + Cross-Exchange + Pairs + Merger Arb) | 4 | ~3.5 | ~2.5 | Better — merger arb provides true diversification |
| Full spectrum (Carry + Cross-Exch + Merger + Vol Arb + Flash Loan) | 5 | ~4.2 | ~3.0 | Good — three distinct risk factors |
| Full spectrum + Trend-Following (per [[arbitrage-opportunity-map]]) | 6 | ~5.0 | ~4.5 | **Best — trend-following is negatively correlated in crisis** |

**Key finding:** Adding merger-arbitrage to a crypto arb book adds ~1.0 effective bet. Adding trend-following (not technically arb, but see the "portfolio construction arbitrage" in [[arbitrage-opportunity-map]]) adds ~1.5 effective bets. These are the highest-value diversifiers for an arb portfolio.

---

## What Drives Correlations

Understanding the **underlying risk factors** explains why certain arbs correlate:

| Risk Factor | Strategies Exposed | Normal Exposure | Crisis Behavior |
|---|---|---|---|
| **Crypto leverage demand** | Cash-carry, Funding arb, Cross-exchange (indirectly) | Primary driver of carry returns | Inverts in bear market, destroying carry |
| **Crypto volatility** | Cross-exchange, Cross-chain, Flash loan | More vol = more dislocations = more opportunity | Spikes in crisis — **positive** for these strategies |
| **DEX/DeFi activity** | Flash loan, Cross-chain, Cross-exchange (CEX-DEX) | More activity = more arb | Can spike or crash in crisis |
| **Equity market risk** | Merger arb, Pairs (equity), Vol arb | Moderate | Deal breaks increase; mean-reversion breaks |
| **Interest rates** | Cash-carry (hurdle rate), Merger arb (opportunity cost) | Higher rates = higher hurdle | Rate cuts = easier hurdle |
| **Counterparty/exchange risk** | All CEX-based strategies | Background risk, usually dormant | Suddenly dominant in exchange crisis (FTX scenario) |

---

## Mapping Specific Arb Strategies onto the Framework

The matrices above use generic strategy buckets. The wiki documents many *named* arb strategies; the table below classifies each by its dominant risk factor so you can place it into one of the buckets and reason about its correlation to the rest of the book. The key column is "Dominant factor" — two strategies sharing a dominant factor are not diversifying, no matter how different they look.

| Named strategy | Bucket | Dominant risk factor | Crisis behavior | Best diversifier *against* it |
|---|---|---|---|---|
| [[put-call-parity-arbitrage]] | Vol / structural | Borrow availability + options liquidity | Borrow recalls, margin spikes | Merger arb, trend-following |
| [[on-off-the-run-treasury-arbitrage]] | Convergence (liquidity) | **Liquidity premium** | Widens violently in flight-to-quality | Trend-following (negatively correlated) |
| [[swap-spread-arbitrage]] | Convergence (liquidity) | **Liquidity premium** | Co-moves with OTR/OFR | Anything not liquidity-driven |
| [[tips-treasury-arbitrage]] | Convergence (liquidity) | **Liquidity premium** | Co-moves with OTR/OFR | Anything not liquidity-driven |
| [[gold-silver-ratio-arbitrage]] | Pairs / mean-reversion | Commodity correlation regime | Correlation breaks (0.4-0.6) in crisis | Carry, merger arb |
| [[wrapped-asset-triangular-arbitrage]] | Dislocation (crypto) | Custody/counterparty trust | Spikes with crypto stress | Equity-based arbs |
| merger-arbitrage | Event-driven | M&A deal flow | Deal breaks rise; still lowest-corr | (it *is* the diversifier) |
| cum-ex-dividend-stripping | (Retired / illegal) | Regulatory control failure | N/A — not deployable | N/A |

**The hidden cluster:** note that the three Treasury/rates convergence trades ([[on-off-the-run-treasury-arbitrage]], [[swap-spread-arbitrage]], [[tips-treasury-arbitrage]]) all carry the *same* dominant factor — the [[limits-to-arbitrage|liquidity premium]]. This is exactly the LTCM trap: a "diversified" relative-value book that is really one giant bet on liquidity not drying up. In the matrices above this is the rates analogue of the Cash-Carry ↔ Funding-Arb 0.95 cluster. Always collapse same-factor strategies into a single allocation bucket before computing effective bets.

### Quick factor-overlap heuristic

| If your book contains... | ...and you add... | Marginal diversification | Verdict |
|---|---|---|---|
| OTR/OFR Treasury arb | Swap-spread or TIPS arb | Near zero (same liquidity factor) | Don't — it's leverage, not breadth |
| Any crypto carry | Funding-rate arb | Near zero (same leverage-demand factor) | Don't — single bucket |
| Crypto-only arb book | Merger arb | High (independent deal-flow factor) | Do — best cross-asset diversifier |
| Any convergence book | Trend-following overlay | High *and negative in crisis* | Do — the crisis hedge |
| Gold-silver pairs | Wrapped-asset crypto arb | High (unrelated factors) | Do — genuinely independent |

## Portfolio Construction Implications

### Rule 1: Don't Double Up on Carry

Cash-carry and funding rate arb are 85-95% correlated. Running both at full size is 2x leverage on the same bet, not diversification. Treat them as a **single allocation bucket** and choose the more attractive on a risk-adjusted basis.

### Rule 2: Cross-Asset is the Best Diversifier

Adding equities-based strategies (merger arb, equity stat arb, vol arb) to a crypto arb book provides the highest marginal diversification because the underlying risk factors (M&A deal flow, equity factor returns, VIX dynamics) are largely independent of crypto leverage demand.

### Rule 3: Dislocation Strategies Hedge Carry

Per [[arbitrage-opportunity-map#Hidden Opportunity 1]], carry strategies die when volatility spikes, but dislocation strategies (cross-exchange, flash loan) come alive. A portfolio combining carry + dislocation has natural regime complementarity: someone is always making money.

### Rule 4: Size by Conditional Correlation

Use crisis-conditional correlations (not full-period) for position sizing:
```
max_allocation_per_strategy = target_max_loss / (conditional_correlation_with_portfolio × strategy_volatility)
```

If two strategies have 0.90 crisis correlation, treat their combined allocation as ~1.1x a single allocation, not 2x.

### Recommended Arb Portfolio Templates

**Conservative (3 bets, ~3.0 N* in crisis):**
1. Funding rate arb (30%)
2. Merger arb (30%)
3. Trend-following overlay (40%)

**Moderate (4 bets, ~3.5 N* in crisis):**
1. Funding rate arb (25%)
2. Cross-chain arb (20%)
3. Merger arb (25%)
4. Vol arb / dispersion (30%)

**Aggressive (5+ bets, ~4.0 N* in crisis):**
1. Funding rate arb (20%)
2. Cross-exchange arb (alts) (15%)
3. Cross-chain arb (15%)
4. Merger arb (20%)
5. Vol arb (15%)
6. Trend-following overlay (15%)

## Sources

- [[strategy-correlation-matrix]] — parent framework
- [[arbitrage-opportunity-map]] — portfolio construction arbitrage insight
- [[regime-matrix]] — strategy performance by market condition
- [[failure-modes]] — crowding and correlation cascade failure mode
- Gatev, Goetzmann, Rouwenhorst (2006) — "Pairs Trading: Performance of a Relative Value Arbitrage Rule"
- Mitchell & Pulvino (2001) — "Characteristics of Risk and Return in Risk Arbitrage"
- Duarte, Longstaff, Yu (2007) — "Risk and Return in Fixed-Income Arbitrage"
- Meucci (2009) — "Managing Diversification" (effective bets framework)

## Related

- [[arbitrage]] — parent concept
- [[strategy-correlation-matrix]] — the general framework this page specializes
- [[arbitrage-opportunity-map]] — where the diversifying overlays come from
- [[regime-matrix]] — strategy performance by market condition
- [[limits-to-arbitrage]] — why same-factor arbs all fail together
- [[convergence-arbitrage]] — the class most prone to the liquidity-factor trap
- [[crowding-indicators]] — detecting when a factor is over-owned
- [[failure-modes]] — the correlation-cascade failure mode
- [[portfolio-theory]] — effective-bets and diversification foundations
- Constituent strategies classified above: [[put-call-parity-arbitrage]], [[on-off-the-run-treasury-arbitrage]], [[gold-silver-ratio-arbitrage]], [[wrapped-asset-triangular-arbitrage]], merger-arbitrage
