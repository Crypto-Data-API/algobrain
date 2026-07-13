---
title: "Momentum Crashes"
type: concept
created: 2026-04-15
updated: 2026-06-11
status: good
tags: [anomalies, momentum, risk-management, behavioral-finance, volatility]
aliases: ["Momentum Crash", "Daniel-Moskowitz Momentum Crashes", "Momentum Tail Risk"]
related: ["[[momentum-anomaly]]", "[[momentum-factor]]", "[[time-series-momentum]]", "[[volatility-targeting]]", "[[tail-risk]]", "[[risk-management]]", "[[mean-reversion]]", "[[factor-investing]]"]
domain: [anomalies, risk-management]
prerequisites: ["[[momentum-anomaly]]", "[[volatility]]"]
difficulty: advanced
---

A **momentum crash** is a rare but severe drawdown in a cross-sectional [[momentum-anomaly|momentum]] strategy — typically a loss of 15-40% over days to a few weeks — that occurs when a falling market suddenly and violently rebounds. Because the momentum strategy is short the prior "losers" (the most beaten-down, high-beta stocks) and long the prior "winners" (often defensive), a sharp reversal rally lifts exactly what momentum is short and lags exactly what it is long. The phenomenon was formally documented by Daniel and Moskowitz (2016) and is the single largest obstacle to sizing momentum as a standalone strategy.

## The Mechanism

The defining feature is a **time-varying, asymmetric market beta** in the momentum portfolio:

1. The market falls sharply for an extended period (a bear market or crash).
2. The "loser" decile fills up with high-beta, distressed, low-priced stocks that fell hardest — the strategy is **short** these.
3. The "winner" decile rotates toward defensive, low-beta survivors — the strategy is **long** these.
4. The momentum portfolio's net market beta turns sharply **negative** at exactly the wrong moment (it becomes implicitly short the market near the bottom).
5. When sentiment flips and a violent risk-on rebound arrives, the cheap, high-beta losers explode upward (the "junk rally" or "dash for trash"). The strategy's short leg detonates while its long leg lags.
6. The result is a large loss concentrated into a short window.

In options language, momentum behaves like a written (short) call on the market in the recovery phase: limited upside in calm trends, large losses when the market snaps back from a panic. Its return distribution is therefore **left-skewed with fat tails** — the opposite of the lottery-like positive skew naive backtests imply.

## The Documented Evidence

**Daniel and Moskowitz (2016), "Momentum Crashes," *Journal of Financial Economics*** is the canonical study. Key findings:

- The worst momentum months cluster in the rebound phases following market crashes, when contemporaneous market returns are high but lagged market returns are low (a "bear-market panic followed by rebound" state).
- In July-August 1932, US momentum lost roughly **-91%** over two months as the market rebounded off the Great Depression low.
- In March-May 2009, momentum lost roughly **-73% (Daniel-Moskowitz estimate; ~-25% in the single worst month)** as the post-GFC junk rally lifted the most distressed names. This was the largest crash in the modern era.
- Smaller crashes occurred in 2001-2002 and around the November 2016 US election.
- These crashes are **partially forecastable**: they occur disproportionately when the market is down over the prior two years (a "bear" state) *and* when ex-ante (option-implied or realized) volatility is high.

## Why It Is Not Diversifiable Away

Momentum crashes are not idiosyncratic noise — they are a structural property of the strategy. The crash months are precisely when most other risk assets are recovering, so momentum's tail loss tends to coincide with a *good* tape for everything else, making the loss feel especially painful and ill-timed. The crash is the price paid for the smooth, attractive returns in normal trending regimes. As [[factor-investing|factor]] research puts it, the momentum premium is in part compensation for bearing this crash risk.

## Mitigation Techniques

Several approaches reduce the tail without destroying the premium:

- **[[volatility-targeting|Constant-volatility scaling]]** — scale exposure inversely to the strategy's own recent realized volatility. Daniel-Moskowitz show this roughly doubles the strategy's Sharpe and nearly eliminates the worst crashes, because crashes occur in high-vol states where the rule has already cut exposure. This is the single most effective fix.
- **Dynamic / "smart" momentum** — explicitly forecast the crash state (bear market + high vol) and reduce or hedge the short leg during it.
- **Beta-neutralization (residual momentum)** — sort on factor-adjusted residual returns rather than raw returns (Blitz, Huij, Martens 2011), removing the time-varying market-beta that drives the crash.
- **Long-only momentum** — most of the crash comes from the *short* leg (the exploding losers). Dropping or down-weighting the short side removes much of the tail at the cost of some long-short premium and market neutrality.
- **Combination with value** — value and momentum are negatively correlated and value tends to do well in the rebound regimes that hurt momentum, so a value+momentum blend smooths the combined drawdown (Asness, Moskowitz, Pedersen 2013).
- **Explicit tail hedges** — cheap OTM index calls to cap the cost of a junk rally.

## Trading Relevance

The practical takeaways for any trader running [[momentum-anomaly|momentum]], [[time-series-momentum|trend]], or factor portfolios:

- **Naive backtests dramatically overstate momentum's risk-adjusted attractiveness** because the worst observations are rare and may not appear in a short sample. Always stress-test against 1932, 2009, and 2016 analogues.
- **Position sizing must account for the left tail**, not just historical volatility — use [[volatility-targeting]] and cap gross exposure.
- **Watch the regime**: deep bear markets with elevated implied volatility are the danger zone. This is exactly the signal [[market-regime-detection-ml|regime detection]] aims to flag.
- The crash risk is why standalone, fully-levered cross-sectional momentum is rarely deployed at institutional scale without volatility scaling or a crash overlay.

## Related

- [[momentum-anomaly]] — the underlying premium and its decay
- [[momentum-factor]] — the factor-portfolio construction
- [[time-series-momentum]] — trend-following's analogous (milder) tail behaviour
- [[volatility-targeting]] — the primary mitigation
- [[tail-risk]] / [[risk-management]] — managing left-skewed return distributions
- [[mean-reversion]] — the rebound dynamic that drives the crash
- [[factor-investing]] — momentum as one factor among several

## Sources

- Daniel, K., and Moskowitz, T. (2016). *Momentum Crashes*. *Journal of Financial Economics*, 122(2): 221-247. The canonical study documenting the crashes, their forecastability, and the volatility-scaling fix.
- Barroso, P., and Santa-Clara, P. (2015). *Momentum has its moments*. *Journal of Financial Economics*, 116(1): 111-120. Independently shows constant-volatility momentum nearly eliminates the crashes and roughly doubles the Sharpe.
- Asness, C., Moskowitz, T., and Pedersen, L. (2013). *Value and Momentum Everywhere*. *Journal of Finance*. Value-momentum diversification.
- Blitz, D., Huij, J., and Martens, M. (2011). *Residual Momentum*. *Journal of Empirical Finance* — beta-neutralized momentum with reduced crash exposure.
- Jegadeesh, N., and Titman, S. (1993). *Returns to Buying Winners and Selling Losers*. *Journal of Finance* — the original momentum anomaly.
