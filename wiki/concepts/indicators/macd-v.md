---
title: "MACD-V (Volatility-Normalised MACD)"
type: concept
created: 2026-07-20
updated: 2026-07-20
status: draft
tags: [indicators, technical-analysis, momentum, volatility, quantitative, crypto]
aliases: ["MACD-V", "MACD-v", "Volatility Normalised MACD", "Volatility Normalized Momentum", "Spiroglou MACD"]
related: ["[[macd]]", "[[macd-histogram]]", "[[macd-crossover]]", "[[atr]]", "[[exponential-moving-average]]", "[[moving-averages]]", "[[momentum-(indicator)]]", "[[rsi]]", "[[chande-momentum-oscillator]]", "[[volatility]]", "[[volatility-regime-classification]]", "[[z-score]]", "[[standard-deviation]]", "[[stretch-revert]]", "[[mean-reversion]]", "[[trend-following]]", "[[hurst-exponent]]", "[[regime-detection]]", "[[overfitting]]", "[[false-signals]]", "[[normalization]]", "[[keltner-channels]]", "[[bollinger-bands]]", "[[cross-sectional-momentum]]", "[[cryptodataapi-hyperliquid]]", "[[cryptodataapi-mcp]]"]
domain: [technical-analysis, indicators]
prerequisites: ["[[macd]]", "[[atr]]"]
difficulty: intermediate
---

# MACD-V (Volatility-Normalised MACD)

MACD-V is a volatility-normalised reformulation of [[macd|MACD]] created by **Alex Spiroglou, CFTe, DipTA (ATAA)**. It divides the classic MACD spread by the Average True Range of the longer lookback, converting a raw price-unit quantity into a dimensionless one expressed in **volatility units**. That single change makes readings comparable across instruments, across time, and across volatility regimes — none of which raw MACD supports.

Spiroglou developed the indicator in 2015 and published it in 2022. The paper, *MACD-V: Volatility Normalised Momentum*, won both the **Charles H. Dow Award (2022)** from the CMT Association and the **NAAIM Founders Award for Advances in Active Investment Management (2022)**.

> **Important scope caveat.** This page documents the **published indicator** as described by Spiroglou and by StockCharts ChartSchool. The user's own trading system contains a group named "MACD-V" (listed as a sibling family on [[stretch-revert]]). That implementation is **not documented here and should not be assumed identical** to the published indicator — same name, unverified relationship. Do not read parameter values, zone thresholds, or signal rules from this page into that group.

## Formula

```
MACD-V = [ ( EMA(12) − EMA(26) ) / ATR(26) ] × 100

Signal line = EMA(9) of MACD-V
Histogram   = MACD-V − Signal line
```

```python
def macd_v(high, low, close, fast=12, slow=26, atr_len=26, signal=9):
    """Spiroglou MACD-V. Output is in volatility units x 100."""
    macd_line = ema(close, fast) - ema(close, slow)
    atr_series = atr(high, low, close, atr_len)
    mv = [100.0 * m / a if a else 0.0 for m, a in zip(macd_line, atr_series)]
    return mv, ema(mv, signal), [m - s for m, s in zip(mv, ema(mv, signal))]
```

The numerator is **exactly the classic MACD line** — Gerald Appel's 12/26 EMA spread, unchanged. The only modification is the denominator. Defaults are 12/26 for the EMAs, 26 for the [[atr|ATR]] period (deliberately matched to the slow EMA), and 9 for the signal line, preserving MACD's familiar settings so the two can be read side by side.

Note that the normalisation is by **ATR, not by price**. Dividing by price would give a percentage spread, which fixes cross-asset comparability but *not* comparability across volatility regimes — a 2% spread means something very different in a quiet market than in a violent one. Dividing by ATR fixes both at once. That choice is the substance of the contribution.

## Why normalisation matters

Raw [[macd|MACD]] is denominated in **price units**, and that single fact is responsible for most of its practical awkwardness.

**It is not comparable across assets.** A MACD line of 0.004 on a $0.30 altcoin and 240 on $60,000 BTC could represent identical momentum in any meaningful sense, or wildly different momentum — the numbers carry no information on their own. There is no threshold you can write down that means the same thing on both. This makes raw MACD nearly useless for anything cross-sectional: ranking a perp universe by momentum, screening for the strongest movers, or applying a uniform entry rule across a basket. MACD-V readings are dimensionless, so a value of +120 means the same thing on both instruments.

**It is not comparable across time on the same asset.** BTC's price has moved through several orders of magnitude. A MACD reading from 2017 and one from 2026 are not on the same scale, which means any threshold fitted on old history is silently wrong on new data. This is a slow, invisible form of parameter drift that a price-unit indicator cannot avoid.

**It is not comparable across volatility regimes.** This is the subtlest failure and the one ATR specifically addresses. Even holding price level constant, the same MACD value means something completely different in a 2%-daily-range market than in an 8%-daily-range one. In the calm regime it is a substantial directional move; in the violent one it is noise. Traders handle this informally by "eyeballing" MACD relative to its own recent range — which is an unstated, undisciplined normalisation. MACD-V makes it explicit and consistent.

**What you get in exchange for the division.** Fixed, meaningful thresholds. Because the output is in volatility units, statements like "beyond ±150 is an extreme momentum reading" are portable across instruments and eras. Raw MACD supports no such statement at any level. This also makes MACD-V usable as a genuine cross-sectional ranking input, which raw MACD is not.

**The cost.** ATR is itself an estimate, computed over a rolling window, and it is neither instantaneous nor robust. During a sharp volatility expansion the denominator lags the numerator: the spread widens immediately while ATR(26) takes many bars to catch up, so MACD-V *overshoots* on the initial impulse and then mean-reverts as ATR fills in — a move partly in the indicator rather than in the market. In a volatility collapse the reverse happens and readings are damped. Any zone-based rule inherits this timing artifact.

## Signal zones

Spiroglou's framing is a **momentum lifecycle** — a set of zones a market rotates through rather than a simple overbought/oversold binary. The level anchors are **±50** and **±150**, combined with the position of MACD-V relative to its signal line.

Per StockCharts ChartSchool:

| Zone | Condition |
|---|---|
| Risk (overbought) | MACD-V > 150, above signal line |
| Rallying | 50 < MACD-V < 150, above signal line |
| Rebounding | −150 < MACD-V < 50, above signal line |
| Retracing | MACD-V > −50, below signal line |
| Reversing | −150 < MACD-V < −50, below signal line |
| Risk (oversold) | MACD-V < −150 |
| Ranging | −50 < MACD-V < 50 sustained for 20–30+ bars |

The three level bands — beyond ±150 (extreme), ±50 to ±150 (directional), inside ±50 (neutral/ranging) — are the durable part and are consistently reported. **The exact zone boundary conventions vary slightly between secondary sources**, and some summaries present a simpler seven-band split on level alone without the signal-line condition. Spiroglou's original SSRN paper is the authority; where a rule matters, check it there rather than relying on this table.

**What "Risk (overbought)" means.** It is not a sell signal, and Spiroglou's naming is deliberate — *risk*, not *reversal*. A reading beyond +150 says momentum is extreme relative to the market's own volatility, which historically is a poor moment to initiate new long risk and says nothing reliable about when the move ends. Trends can and do hold extreme readings. Trading these zones as reversal triggers is the standard oscillator error and a straightforward source of [[false-signals]].

## Relationship to MACD and its components

| | [[macd]] | MACD-V |
|---|---|---|
| Line | EMA12 − EMA26 | Same, ÷ ATR26, × 100 |
| Units | Price | Dimensionless (volatility units) |
| Signal line | EMA9 of MACD | EMA9 of MACD-V |
| [[macd-histogram\|Histogram]] | MACD − signal | MACD-V − signal |
| Cross-asset comparable | No | Yes |
| Cross-era comparable | No | Yes |
| Fixed thresholds meaningful | No | Yes |
| Crossover signals | [[macd-crossover]] | Structurally identical |

Because the transformation is a division by a positive quantity, **the sign of MACD-V always matches the sign of MACD**, and zero-line crosses occur at exactly the same bars. What changes is *magnitude*, and therefore everything that depends on magnitude: threshold rules, cross-sectional ranking, and how the histogram's size should be read.

[[macd-crossover]] signals are not identical, however. The signal line is an EMA of the *normalised* series, so when ATR changes materially within the signal window, MACD-V and its signal line can cross at different bars than MACD and its own signal line do. In stable volatility the two agree closely; in an expansion they can diverge.

Note the conceptual family resemblance to [[keltner-channels]] (ATR-based bands) and to a [[z-score]] (dividing a deviation by a scale). MACD-V is the same manoeuvre applied to a momentum spread. The relevant caveat from [[median-absolute-deviation]] applies here too: ATR is a mean-based scale with a low breakdown point, so a single extreme bar inflates the denominator and *shrinks* subsequent readings. On thin crypto perp books that is a real effect, not a hypothetical.

## Crypto-specific notes

Crypto is close to the ideal case for this indicator, and also one of the harder ones:

- **Extreme cross-asset price dispersion.** A perp universe spanning sub-cent memecoins to five-figure BTC makes raw MACD comparisons meaningless. Normalisation is not a refinement here, it is a prerequisite for any universe-wide rule.
- **Extreme volatility regime shifts.** Crypto moves between 20% and 150% annualised vol regularly. This is precisely the variation ATR normalisation is designed to absorb.
- **Fixed thresholds finally become portable.** A ±150 rule can be applied across a forty-coin universe without per-asset calibration — the main practical benefit for systematic use.
- **ATR contamination on thin books.** [[atr|ATR]] is built from true ranges, which on illiquid alt perps are inflated by [[bid-ask-spread|spread]] and wicks. An inflated denominator systematically damps MACD-V on exactly the assets whose momentum readings are least trustworthy. That direction of bias is arguably conservative, but it is a bias.
- **24/7 trading, no gaps.** The gap component of true range rarely fires on perps, making ATR a somewhat different quantity than in a session-based market.

## Parameters and tuning

| Parameter | Default | Notes |
|---|---|---|
| Fast EMA | 12 | Appel's original; retained so MACD-V sits alongside MACD |
| Slow EMA | 26 | As above |
| ATR period | 26 | Matched to the slow EMA. Decoupling them is a design change, not a tuning step |
| Signal EMA | 9 | Appel's original |
| Level anchors | ±50, ±150 | Portable *because* the series is normalised; that is the whole point of the design |

**Overfitting warning.** The zone thresholds are the obvious tuning target and they should largely be left alone. Their value is that they are **fixed and portable** — the moment you fit ±137 to one asset's history, you have discarded the property that made the indicator worth using and reintroduced the per-asset calibration that raw MACD forced on you. Similarly, decoupling the ATR period from the slow EMA adds a degree of freedom to a design that was deliberately parameter-frugal. See [[overfitting]]. If a threshold genuinely needs to move, move it once, globally, on a stated rationale, and never per-asset.

## Advantages

- **Genuinely comparable across assets, eras, and volatility regimes** — the core contribution, and it solves a real defect in one of the most widely used indicators in existence.
- **Fixed thresholds carry meaning**, which raw MACD can never support at any level.
- **Usable cross-sectionally** — a universe of perps can be ranked by MACD-V directly, enabling [[cross-sectional-momentum|cross-sectional]] applications MACD cannot serve.
- **Minimal change from a familiar indicator.** Same EMAs, same signal line, same histogram, same zero crosses. Adoption cost is near zero for anyone already reading MACD.
- **Parameter-frugal by design** — no new tunable knobs beyond the ATR period, which is deliberately tied to the slow EMA.
- **Peer-recognised research** — the Charles H. Dow Award and the NAAIM Founders Award, both 2022, represent more external scrutiny than almost any retail indicator receives.

## Limitations

- **ATR lags the numerator.** In a fast volatility expansion the spread widens before ATR does, so MACD-V overshoots and then reverts as the denominator catches up. That reversion is an artifact of the indicator, not a market move.
- **ATR is not robust.** A single extreme bar inflates the denominator and damps subsequent readings — the same self-suppression pathology described on [[median-absolute-deviation]] for standard-deviation scaling.
- **Still a momentum indicator.** Normalisation fixes comparability; it does not make extreme readings into reversal signals. The "Risk" zones are risk flags, not triggers.
- **Zone conventions vary between secondary sources.** The ±50 / ±150 anchors are consistent; the precise zone definitions differ in how they combine level with signal-line position. Verify against the original paper before coding a rule.
- **Shares MACD's lag.** The numerator is an EMA spread with all of the responsiveness limits that implies.
- **No independent validation reviewed in this vault.** The awards recognise the research contribution; this vault has reviewed no out-of-sample, cost-corrected study of MACD-V's profitability, in crypto or elsewhere.
- **Not a documented member of [[stretch-revert]].** MACD-V is a momentum indicator; the stretch-revert family fades deviation from an adaptive baseline. Its relevance here is as a sibling group on the same bot and as a normalisation design pattern, not as a family baseline.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/candles?coin=X&interval=15m&limit=500` — OHLC bars; both the EMA spread and the ATR denominator need highs and lows, not closes alone
- `GET /api/v1/volatility/regime/{symbol}` — the regime read; MACD-V is explicitly built to be stable across these states, so it is the direct test of whether the normalisation is doing its job
- `GET /api/v1/quant/market` — HMM regime probabilities, to distinguish an extreme reading inside a genuine trend from one inside chop
- `GET /api/v1/hyperliquid/l2-book?coin=X` — spread and depth; on thin books the true ranges feeding ATR are partly spread, which damps MACD-V on exactly the assets it should be read most cautiously

**Historical data:**
- `GET /api/v1/backtesting/klines` — OHLCV archive for computing the MACD-V distribution per asset and checking whether the ±50 / ±150 anchors actually land where they should
- `GET /api/v1/quant/regimes/history` — hourly regime labels since 2020, for testing threshold stability across labelled regimes

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=ETH&interval=15m&limit=500"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

**Live dashboards:** [market regimes](https://cryptodataapi.com/market-regimes) · [order-book depth](https://cryptodataapi.com/quant-order-books)

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can verify the indicator's central claim rather than assume it:

- **Test comparability directly — this is the whole thesis.** Compute MACD-V across a wide perp universe from `GET /api/v1/hyperliquid/candles` and compare the distributions. If the ±150 threshold is hit at a similar rate on a sub-cent memecoin and on BTC, normalisation is working. If hit rates differ by an order of magnitude, it is not, and per-asset thresholds are back — which would defeat the point.
- **Check threshold stability across volatility regimes.** Bucket historical MACD-V by the label from `GET /api/v1/volatility/regime/{symbol}`. A well-normalised series should show similar distributions in each bucket; systematic drift means ATR(26) is not absorbing the regime on that asset.
- **Measure the ATR-lag overshoot.** During volatility expansions, log MACD-V alongside the ATR denominator. The portion of the reading attributable to a stale denominator is an artifact, and entries taken on it are entries on the indicator's own transient.
- **Rank cross-sectionally, which raw MACD cannot support.** MACD-V's dimensionless output makes a universe-wide momentum ranking meaningful. This is the application where the normalisation earns most of its value.
- **Keep this page's indicator and the bot's "MACD-V Group" strictly separate.** An agent reasoning about the live group must read that group's own configuration; the parameters and zones documented here are Spiroglou's published indicator and carry no authority over the bot's implementation.

## Related

- [[macd]] — the parent indicator; MACD-V's numerator is unchanged from it
- [[macd-histogram]] — the same construction applied to the normalised series
- [[macd-crossover]] — the crossover strategy; signals can differ from raw MACD when ATR moves within the signal window
- [[atr]] — the normalising denominator, and the source of most of MACD-V's artifacts
- [[volatility]] · [[volatility-regime-classification]] — the variation the normalisation absorbs
- [[z-score]] · [[median-absolute-deviation]] · [[standard-deviation]] — the general deviation-over-scale pattern, and the robustness caveat that applies to ATR too
- [[keltner-channels]] · [[bollinger-bands]] — ATR-scaled and σ-scaled band constructions, the same idea in a different form
- [[momentum-(indicator)]] · [[rsi]] · [[chande-momentum-oscillator]] — the bounded-oscillator alternatives Spiroglou positions MACD-V against
- [[cross-sectional-momentum]] — the application normalisation unlocks
- [[trend-following]] · [[mean-reversion]] — the two readings of an extreme momentum value
- [[hurst-exponent]] · [[regime-detection]] — the regime context any extreme reading must be interpreted inside
- [[stretch-revert]] — sibling strategy family on the same bot; separate thesis
- [[false-signals]] · [[overfitting]] — the zone-trading and threshold-tuning hazards
- [[exponential-moving-average]] · [[moving-averages]] — the underlying smoothers

## Sources

- Spiroglou, Alex (2022). *MACD-V: Volatility Normalised Momentum*. SSRN Working Paper 4099617 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4099617. The original paper; authority for the formula, the momentum-lifecycle framework, and the zone definitions.
- StockCharts ChartSchool — MACD-V: https://chartschool.stockcharts.com/table-of-contents/technical-indicators-and-overlays/technical-indicators/macd-v. Source for the formula `[(EMA12 − EMA26)/ATR(26)] × 100`, the EMA(9) signal line, the histogram definition, and the zone table reproduced above.
- CMT Association — Charles H. Dow Award: https://cmtassociation.org/association/award-recognizing/charles-h-dow-award/. Spiroglou is the 2022 recipient.
- NAAIM (2022) — Founders Award for Advances in Active Investment Management, hosted paper: https://www.naaim.org/wp-content/uploads/2022/05/MACD-V-Alex-Spiroglou-WEB.pdf.

**Verification status (checked 2026-07-20).** Confirmed: the formula and its components; the ATR(26) denominator matched to the slow EMA; the ±50 / ±150 level anchors; Alex Spiroglou as author; the Charles H. Dow Award (CMT Association, 2022) and the NAAIM Founders Award (2022); development in 2015 and publication in 2022. **Not fully confirmed:** the exact seven-zone boundary conventions, which differ slightly between secondary sources — the table above follows StockCharts ChartSchool and should be checked against the SSRN paper before any rule is coded against it. No independent, out-of-sample, cost-corrected performance study of MACD-V has been reviewed in this vault, and no vault source-summary page covers it. The relationship between this published indicator and the user's own "MACD-V Group" is **unverified**.
