---
title: "Carry Anomaly"
type: concept
created: 2026-04-10
updated: 2026-06-21
status: excellent
tags: [anomalies, carry, factor-investing, fx]
aliases: ["Carry Factor", "Carry Trade", "FX Carry"]
domain: [anomalies]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[carry-trade]]", "[[funding-rate-arbitrage]]", "[[edge-taxonomy]]", "[[trend-plus-tail-hedge]]", "[[volatility-risk-premium]]", "[[basis-trading]]", "[[negative-skew]]", "[[when-to-retire-a-strategy]]", "[[geometric-mean]]"]
---

# Carry Anomaly

The empirical regularity that high-yielding assets earn higher returns than low-yielding ones across asset classes — currencies, bonds, commodities, equities. The longest-running positive Sharpe strategy in finance and also the most catastrophic during crises. Carry strategies pick up nickels in front of steamrollers: small, steady gains punctuated by occasional 30%+ losses when the market regime shifts.

## The Definition

"Carry" is the return you would earn if prices stayed constant — the yield, dividend, interest rate differential, or roll yield embedded in holding a position. Across asset classes:

- **Currencies:** interest rate differential (long high-yield currency, short low-yield)
- **Bonds:** yield-to-maturity above the funding cost
- **Commodities:** the futures roll yield (positive for backwardation, negative for contango)
- **Equities:** dividend yield above the risk-free rate
- **Volatility:** implied vs. realized vol differential
- **Crypto:** funding rate on perpetuals

The "carry trade" is to systematically buy high-carry assets and sell (or fund yourself in) low-carry assets.

### Carry across asset classes

The carry signal is the *same concept* — the return earned if prices stay constant — operationalized differently in each market. The unifying insight of Koijen, Moskowitz, Pedersen & Vrugt (2018) is that these are all instances of one factor:

| Asset class | What "carry" is | Long-carry position | Short-carry position | Typical standalone Sharpe (illustrative) |
|---|---|---|---|---|
| **FX** | Interest-rate differential | High-yield currency | Low-yield currency | ~0.5 (G10) |
| **Bonds** | Yield-to-maturity − funding + roll-down | Steep, high-yielding curves | Flat/inverted curves | ~0.5–0.7 |
| **Commodities** | Futures roll yield | Backwardated contracts | Contangoed contracts | ~0.4–0.7 |
| **Equities (index)** | Dividend yield − risk-free | High-dividend markets | Low-dividend markets | ~0.3–0.5 |
| **Volatility** | Implied − realized vol (the [[variance-risk-premium]]) | Sell options / vol | Buy options / vol | ~0.5–1.0 (with severe tails) |
| **Crypto** | Perpetual funding rate | Positive-funding side | Negative-funding side | varies; high crash risk |

Sharpe figures are order-of-magnitude historical illustrations, not guarantees; all carry Sharpes overstate forward expectations because the worst crashes may not yet be in-sample. See [[funding-rate-arbitrage]] and [[basis-trading]] for the crypto/futures implementations and [[volatility-risk-premium]] for vol carry.

## The Original Findings

The carry anomaly has multiple foundational papers:

- **FX carry:** Hansen & Hodrick (1980), Fama (1984) — the "forward premium puzzle." Forward exchange rates are biased predictors of future spot rates; high-yielding currencies do not depreciate enough to offset the yield differential.
- **Bond carry:** Fama & Bliss (1987), Cochrane & Piazzesi (2005) — long-dated bonds earn term premia not predicted by expectations hypothesis.
- **Commodity carry:** Erb & Harvey (2006) — commodity returns are dominated by roll yield, not spot price movements.
- **Cross-asset carry:** Koijen, Moskowitz, Pedersen, Vrugt (2018) "Carry" — *Journal of Financial Economics* — formalized carry as a single factor across asset classes.

The Koijen et al. paper showed that a generalized cross-asset carry strategy earns positive returns in every asset class tested, with Sharpe ratios typically in the 0.4-0.8 range per class and higher when combined across classes.

## What It Says

Markets do not fully arbitrage away yield differentials. A 5% interest rate differential between two currencies is *not* fully offset by expected currency depreciation; the high-yield currency typically gains *some* of the carry plus *part* of the depreciation, leaving a positive expected return.

This violates the uncovered interest parity (UIP) hypothesis from textbook macroeconomics. UIP says forward rates should be unbiased predictors of spot rates. Empirically, they are *biased* — and carry traders profit from the bias.

## The Mechanism

Two competing theories:

### 1. Risk Compensation
Carry trades load up on *crash risk*. They earn small steady returns in normal times and lose catastrophically during crises (currency crashes, bond defaults, commodity squeezes, vol spikes). The expected return is *fair compensation* for the crash risk.

This is the orthodox view. Brunnermeier, Nagel, Pedersen (2008) showed FX carry returns have a strongly negative skew that's consistent with crash-risk compensation.

### 2. Limits to Arbitrage / Funding Constraints
Carry trades require funding. During crises, funding markets seize, forcing carry traders to unwind in the worst conditions. The crash risk isn't a fair compensation; it's a structural feature of the funding-dependent strategy.

In practice, both explanations are partially right. Carry returns have crash risk *and* funding fragility, and the returns reflect both.

In the [[edge-taxonomy]], carry is a mix of **structural** (forced flows from rate-sensitive participants) and **risk-bearing** (compensation for tail exposure).

## Replication Status

Carry has been replicated:
- **Across decades** — back to the 1970s in currencies, longer in some other classes
- **Across asset classes** — currencies, bonds, commodities, equities, vol, crypto
- **Across countries** — every major developed and emerging market
- **In real money** — many systematic and discretionary funds run carry as a core strategy

It is one of the most empirically robust anomalies in finance.

## The Crash Profile

The defining feature of carry: occasional catastrophic losses.

**FX carry crashes:**
- 1992 ERM crisis (sterling crash)
- 1998 LTCM collapse (yen rally)
- 2008 financial crisis (yen carry unwind)
- 2015 Swiss franc unpegging (instant 30% loss for short-CHF carriers)
- 2020 COVID crash

**Commodity carry crashes:**
- 2014-2015 oil price crash (crushed long-oil carry)
- 2020 negative WTI futures (crushed long-oil)

**Vol carry crashes:**
- February 2018 VIX explosion (XIV ETF wiped out overnight)
- March 2020 COVID vol spike

**Crypto carry crashes:**
- 2022 Luna/3AC collapse (crushed funding rate arb)
- November 2022 FTX collapse (vaporized basis trades on FTX)

The pattern: carry strategies look like a perfect free-money machine for years, then lose 20-50% in a single bad month or week. Risk-adjusted Sharpe over the full period is positive but not as high as the in-sample (pre-crash) Sharpe makes it look.

### The crash-risk signature

The defining statistical fingerprint of carry is **strong negative skew**: many small positive returns, occasional large negative returns. This is why naive Sharpe ratios flatter carry — Sharpe assumes symmetric, Gaussian returns and ignores the fat left tail. The same [[negative-skew]] that defines carry also defines short-vol selling (the [[variance-risk-premium]]), which is not a coincidence: both sell insurance against a regime shift.

| Crash dimension | Carry signature | Implication |
|---|---|---|
| **Skew** | Strongly negative | Sharpe over-states risk-adjusted quality |
| **Kurtosis** | Fat-tailed | Tail losses far exceed a normal model's prediction |
| **Frequency** | Rare (multi-year gaps) | Long calm periods breed complacency and over-sizing |
| **Trigger** | Funding stress, regime shift, vol spike | Correlated across *all* carry markets at once |
| **Recovery** | Slow; some unwinds are permanent (CHF 2015, FTX 2022) | Drawdown asymmetry compounds the damage — see [[geometric-mean]] |

Because the worst losses cluster across asset classes simultaneously (a global funding shock hits FX, vol, and crypto carry together), cross-asset diversification thins exactly when it is needed — the same "all correlations go to one" failure documented for [[diversification-in-options|options books]].

## Combining With Trend

The single most powerful diversifier for carry is *trend following*. The reason: when carry crashes, markets typically trend hard in the direction that hurts carry, and the trend-following overlay catches this. A combined carry + trend portfolio has roughly the same expected return as carry alone but dramatically smaller drawdowns.

This is the basis of many systematic macro funds: carry as the return engine, trend as the tail hedge. See [[trend-plus-tail-hedge]] and [[regime-matrix]] for the regime story.

## Variations

### G10 FX Carry
The classic: long high-yield G10 currencies, short low-yield. Liquid, capacity-rich, but heavily traded. Sharpe ~0.5 historically.

### Emerging Market FX Carry
Larger yield spreads but much higher crash risk and political risk. Sharpe varies widely.

### Bond Term Premium / Carry
Long the long end of yield curves with positive slope. Earns the term premium plus roll-down. Highly correlated with bond beta in normal times.

### Commodity Roll Yield
Long backwardated commodities (positive roll), short contangoed commodities (negative roll). Captures the commodity carry signal.

### Cross-Asset Carry Composite
Combine signals across all asset classes, weight by volatility, run as a single factor. Higher Sharpe than any individual carry strategy due to diversification.

### Crypto Funding Rate Arbitrage
The crypto-native carry strategy. Long spot, short perpetual futures (or vice versa) to collect funding rate differential. See [[funding-rate-arbitrage]].

### Volatility Risk Premium (Carry on Vol)
Sell volatility, collect the implied-vs-realized vol spread. The carry strategy on volatility surfaces. See [[volatility-risk-premium]].

## Current Viability

Carry is still widely traded and still earns positive returns. The Sharpe has compressed from historical levels but remains positive across asset classes. The single biggest risk is that the next crash is larger than historical, breaking even multi-decade strategies.

Recommended use: never standalone. Always combine with:
- A trend-following overlay for crisis hedging
- Position sizing that accounts for crash risk (e.g., volatility-targeted with explicit drawdown limits)
- Diversification across asset classes (FX + bonds + commodities + crypto, not just one)

### Kill criteria for a live carry book

Because carry's edge can compress slowly (yield differentials narrow) *and* break violently (a crash unwind), it needs the kind of pre-committed retirement rules described in [[when-to-retire-a-strategy]]. Carry-specific triggers:

| Trigger | Pause (reduce size) | Kill |
|---|---|---|
| **Carry compression** | Expected carry < 1.5× cost of capital | Expected carry < cost of capital |
| **Vol spike** | Implied vol > 1.5× research-time vol | Implied vol > 2× research-time vol |
| **Funding stress** | Funding spreads widening | Funding market dislocation (forced unwind risk) |
| **Drawdown** | > worst historical DD | > 1.5× worst historical DD |
| **Skew deterioration** | Realized skew worse than research | Mechanism break (peg removal, default cascade) |

These mirror the "carry strategies" row of the [[when-to-retire-a-strategy#Pre-Committed Kill Criteria|kill-criteria framework]]. The point of pre-committing is that during a funding crisis the trader will be psychologically least able to size down voluntarily.

## Strategies That Implement It

- [[carry-trade]] — basic FX carry implementation
- [[funding-rate-arbitrage]] — crypto carry
- [[basis-trading]] — futures basis as carry
- [[yield-curve-trading]] — bond carry
- [[volatility-risk-premium]] — vol carry
- [[trend-plus-tail-hedge]] — carry + trend combination

## Sources

- Hansen & Hodrick (1980) — original forward premium puzzle
- Fama (1984) "Forward and Spot Exchange Rates" — *Journal of Monetary Economics*
- Brunnermeier, Nagel, Pedersen (2008) "Carry Trades and Currency Crashes" — *NBER Macroeconomics Annual*
- Koijen, Moskowitz, Pedersen, Vrugt (2018) "Carry" — *Journal of Financial Economics*
- Erb & Harvey (2006) "The Strategic and Tactical Value of Commodity Futures" — *Financial Analysts Journal*
- [[book-expected-returns-antti-ilmanen]]

## Related

- [[anomalies-overview]]
- [[carry-trade]]
- [[funding-rate-arbitrage]]
- [[basis-trading]]
- [[volatility-risk-premium]]
- [[trend-plus-tail-hedge]]
- [[edge-taxonomy]]
