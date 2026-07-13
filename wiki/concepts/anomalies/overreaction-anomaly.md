---
title: "Long-Term Overreaction Anomaly"
type: concept
created: 2026-04-11
updated: 2026-06-11
status: good
tags: [anomalies, behavioral-finance, mean-reversion, stocks]
aliases: ["Overreaction Anomaly", "DeBondt-Thaler Reversal", "Long-Term Reversal", "Long-Term Overreaction", "Contrarian Anomaly"]
domain: [anomalies]
prerequisites: ["[[anomalies-overview]]", "[[behavioral-finance]]"]
difficulty: intermediate
related: ["[[anomalies-overview]]", "[[momentum-anomaly]]", "[[value-anomaly]]", "[[behavioral-finance]]"]
---

# Long-Term Overreaction Anomaly

Stocks that have performed extremely poorly over a 3-5 year window systematically outperform stocks that have performed extremely well over the same window, in the subsequent 3-5 years. This "long-term reversal" pattern contradicts the [[momentum-anomaly]] (which operates at 3-12 month horizons) and is interpreted as evidence that investors *overreact* to sustained good and bad news over multi-year horizons.

## What

Rank stocks on their cumulative returns over the prior 36-60 months. Form a "winner" portfolio (top decile) and a "loser" portfolio (bottom decile). Over the subsequent 3-5 years, the loser portfolio outperforms the winner portfolio by a substantial margin. DeBondt & Thaler (1985) reported 25% cumulative excess return over 36 months in a 1926-1982 US sample.

## Original Paper

DeBondt, W. & Thaler, R. (1985) "Does the Stock Market Overreact?" — *Journal of Finance*.

## Mechanism

- **Overreaction and reversion** — investors become excessively pessimistic about long-term losers and excessively optimistic about long-term winners, pushing prices beyond fundamentals in both directions. Eventually fundamentals reassert themselves.
- **Representativeness heuristic** (Kahneman & Tversky) — investors extrapolate recent trends into the distant future, leading to overpricing of "good stories" and underpricing of "bad stories"
- **Relationship to value** — long-term losers are mechanically value stocks by the time they're sorted (low P/B, high B/P), so the overreaction anomaly overlaps heavily with the [[value-anomaly]]. Some researchers argue long-term reversal is essentially value in disguise.

Fama & French (1996) showed that the DeBondt-Thaler reversal is largely absorbed by the Fama-French three-factor model — it is mostly a value story with extra steps.

## Edge Category

**Behavioral** (representativeness + overreaction), overlapping heavily with value.

## Replication Status

Replicated in the original horizon but with smaller magnitudes than DeBondt-Thaler reported. The effect is concentrated in small caps and largely absent in large caps after controlling for size and value.

## Decay History

Substantially decayed and mostly absorbed into the value factor. Long-term reversal as a distinct alpha beyond value is weak or absent in modern US data.

## Current Viability

Not a standalone strategy. Useful as:

- A diagnostic for strategies that are implicitly making overreaction bets (they are also making value bets)
- A lens on the coexistence of [[momentum-anomaly]] at short horizons and reversal at long horizons — the two form a "momentum then reversal" pattern consistent with delayed overreaction models (Hong-Stein 1999)

## Related Strategies

- [[value-anomaly]] — overlaps heavily; long-term reversal is mostly value
- [[momentum-anomaly]] — complementary short-horizon pattern
- Contrarian long-only strategies

## Sources

- DeBondt & Thaler (1985) — original
- DeBondt & Thaler (1987) "Further Evidence on Investor Overreaction and Stock Market Seasonality"
- Fama & French (1996) "Multifactor Explanations of Asset Pricing Anomalies" — absorbs reversal into value
- Hong & Stein (1999) "A Unified Theory of Underreaction, Momentum Trading, and Overreaction"

## Related

- [[anomalies-overview]]
- [[momentum-anomaly]]
- [[value-anomaly]]
- [[behavioral-finance]]
