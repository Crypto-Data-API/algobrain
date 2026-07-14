---
title: "Crypto Market Regime Taxonomy"
type: concept
created: 2026-06-03
updated: 2026-07-13
status: good
tags: [crypto, derivatives, market-microstructure, quantitative, risk-management, market-regime]
aliases: ["14-Basket Regime Framework", "Crypto Regime Taxonomy", "Crypto Market Regimes", "Regime Baskets"]
domain: [market-microstructure, risk-management]
difficulty: advanced
related: ["[[regime-strategy-playbook]]", "[[regime-matrix]]", "[[market-regime-detection-ml]]", "[[regime-adaptive-strategy]]", "[[regime-detection]]", "[[crypto-perp-backtesting-pitfalls]]", "[[macro-trend-regime]]", "[[bitcoin-cycle-regime]]", "[[meme-speculative-regime]]", "[[derivatives-native-regime]]", "[[event-catalyst-regime]]", "[[crypto-macro-correlation-regime]]", "[[on-chain-regime]]", "[[basis-carry-regime]]", "[[liquidity-depth-regime]]", "[[institutional-flow-regime]]", "[[security-black-swan-regime]]", "[[policy-shock-regime]]", "[[volatility-regime-classification]]", "[[technical-structural-regime]]", "[[hyperliquid]]", "[[cryptodataapi]]"]
---

# Crypto Market Regime Taxonomy

A **market regime** is a persistent state of the market in which the same statistical relationships, optimal strategies, and risk parameters hold — and which a different regime would invalidate. This page is the consolidated **14-basket taxonomy** of crypto regimes, organised after the [[2026-06-03-cryptodataapi-14-basket-regime-framework|Crypto Data API framework]] (a VENTURE AI LABS product) and designed for **systematic perpetual-futures trading on venues like [[hyperliquid|Hyperliquid]]**. Each basket implies a different set of coins, leverage levels, holding durations, and funding-cost tolerance; the central thesis is that regimes must be treated as **distinct strategies gated by detection**, because a strategy run in the wrong regime is not merely suboptimal — it is actively harmful (bull-run logic firing during a liquidation cascade, a range-fade dying on a breakout).

This taxonomy is **complementary to**, not a replacement for, the wiki's existing regime tooling: [[regime-matrix]] maps strategy classes across six generic dimensions, [[market-regime-detection-ml]] covers the detection machinery (HMMs, clustering, change-point), and [[regime-adaptive-strategy]] covers the gating logic. This page is the **crypto-specific, perps-native** layer that sits on top of all three.

## The 14 Baskets

| # | Basket | Timescale | Directional bias | Role |
|---|--------|-----------|------------------|------|
| 1 | [[macro-trend-regime\|Macro Trend]] | Months | Long / Short | **Backdrop** — the regime everything else trades inside |
| 2 | [[bitcoin-cycle-regime\|BTC Cycle]] | Weeks–Months | Long / Neutral | BTC-specific cycle, tradeable independent of alts |
| 3 | [[meme-speculative-regime\|Meme / Speculative]] | Hours–Days | Long / Short | Isolated lowcap vol blasts, uncorrelated to majors |
| 4 | [[derivatives-native-regime\|Derivatives-Native]] | Minutes–Days | Both | **Fragility detector** — funding, OI, liquidations |
| 5 | [[event-catalyst-regime\|Event / Catalyst]] | Hours–Weeks | Both | Discrete shocks — listings, unlocks, prints, depegs |
| 6 | [[crypto-macro-correlation-regime\|Macro Correlation]] | Days–Weeks | Short / Long | Crypto as high-beta tech — equities, DXY, gold |
| 7 | [[on-chain-regime\|On-Chain Intelligence]] | Days–Weeks | Leading signal | Flows, whales, miners, dormancy — leads price |
| 8 | [[basis-carry-regime\|Carry Trade / Basis]] | Days–Weeks | Regime health | Basis health as a fragility gauge |
| 9 | [[liquidity-depth-regime\|Liquidity / Market Depth]] | Real-time–Days | Size / risk filter | **Size filter** — OI vs book depth |
| 10 | [[institutional-flow-regime\|Institutional Flow]] | Weeks–Months | Structural floor | ETF / 401(k) flows set multi-month floors |
| 11 | [[security-black-swan-regime\|Security / Black Swan]] | Hours–Days | Short → Long | Hacks, exploits, depegs — forensic patterns |
| 12 | [[policy-shock-regime\|Geopolitical / Policy Shock]] | Hours–Weeks | Both | Pro-crypto orders, tariffs, rate signals, bans |
| 13 | [[volatility-regime-classification\|Volatility Regime]] | Days–Weeks | Risk-sizing overlay | **Overlay** — compressed vol, expansion, VRP |
| 14 | [[technical-structural-regime\|Technical / Structural]] | Hours–Days | Universal overlay | **Overlay** — MA, compression, range, exhaustion |

## How the Baskets Relate

The 14 baskets are not parallel and mutually exclusive — they nest and overlay:

- **The backdrop (1, 2).** [[macro-trend-regime|Macro Trend]] is the broadest state and sets the bias that everything else trades inside. [[bitcoin-cycle-regime|BTC Cycle]] runs partly independently — BTC can lead price discovery while alts stall.
- **Overlays (13, 14).** [[volatility-regime-classification|Volatility]] and [[technical-structural-regime|Technical/Structural]] are **not market states on their own** — they are sizing and timing overlays that fire inside any of the directional regimes. Compressed vol is dangerous *because* it can sit inside an apparently calm bull or chop regime while leverage builds.
- **Fragility detectors (4, 8, 9).** [[derivatives-native-regime|Derivatives-native]], [[basis-carry-regime|basis/carry]], and [[liquidity-depth-regime|liquidity/depth]] measure positioning fragility rather than direction. Their alignment — persistent positive funding + record OI + OI outrunning book depth — is the pre-cascade signature seen in the [[2025-10-crypto-liquidation-cascade|October 2025 cascade]].
- **Leading signals (7, 10).** [[on-chain-regime|On-chain]] and [[institutional-flow-regime|institutional flow]] tend to lead price: exchange inflows precede sell-offs, sustained ETF inflows set structural floors.
- **Shocks (5, 11, 12).** [[event-catalyst-regime|Event]], [[security-black-swan-regime|security/black-swan]], and [[policy-shock-regime|policy]] regimes are discrete, short-duration windows that temporarily override the backdrop — often with a repeatable short-then-reversal shape.
- **The wildcard (3).** [[meme-speculative-regime|Meme/speculative]] cycles are largely uncorrelated to the majors and run on social momentum.

> **Note on basket #13.** Volatility is co-equal with Technical/Structural as a universal overlay, but its page — [[volatility-regime-classification]] — lives under `concepts/indicators/` (it predates and also serves the options material), not in the `market-regimes/` folder with the other thirteen. It is a full member of the taxonomy; only its file location differs.

### The Fragility Triad (canonical)

The three fragility detectors — baskets 4, 8, 9 — are the single most important *combination* in the taxonomy, so the full mechanism is stated once here and the basket pages defer to it. None of the three dials is decisive alone; the **pre-cascade signature is their alignment**:

1. **Crowded basis** ([[basis-carry-regime]]) — a rich, persistent futures/perp basis means leveraged longs are *financing the carry*; the richer it is, the more leverage is stacked on one side.
2. **Funding + OI** ([[derivatives-native-regime]]) — persistent positive [[funding-rate|funding]] paired with record [[open-interest|open interest]] confirms that leverage is building, not bleeding.
3. **OI outrunning depth** ([[liquidity-depth-regime]]) — when that open interest grows faster than resting order-book depth, any forced flow moves price disproportionately, so an orderly unwind is impossible.

When all three align, a crowded carry + record leverage + thin absorbing depth means the unwind *is* the cascade — the signature seen in the [[2025-10-crypto-liquidation-cascade|October 2025 cascade]]. Each basket page covers only its own leg and links back here for the stack.

## Regime Gating — Why Separate Them

The framework's operating principle: **detect the regime first, then deploy only the strategy gated to it.** A funding-fade that prints in a [[derivatives-native-regime|funding-extreme]] regime will be run over by a [[liquidity-depth-regime|depth-withdrawal cascade]]; a [[technical-structural-regime|range-fade]] with the highest hit-rate in chop is a guaranteed loser the moment a [[volatility-regime-classification|vol expansion]] breaks the range. Each regime carries its own **coin set, leverage ceiling, holding duration, and funding-cost tolerance**, and mixing them turns a clean edge into noise. This is the same logic the wiki develops in [[regime-adaptive-strategy]] and [[market-regime-detection-ml]] — this taxonomy supplies the crypto-specific *states* those mechanisms switch between.

## Detection Inputs

Across baskets, the recurring detection inputs are:

- **Price structure** — HH/HL vs LH/LL, key MAs, range boundaries ([[technical-structural-regime]])
- **Derivatives** — [[funding-rate]], [[open-interest]], [[liquidation|liquidations]], [[basis]] ([[derivatives-native-regime]], [[basis-carry-regime]])
- **Liquidity** — L2 book depth vs OI growth ([[liquidity-depth-regime]]); Hyperliquid's on-chain transparency makes this uniquely trackable
- **On-chain** — exchange flows, whale wallets, miner behaviour, dormancy ([[on-chain-regime]])
- **Cross-asset** — Nasdaq/S&P beta, [[dxy|DXY]], gold/copper ([[crypto-macro-correlation-regime]])
- **Flows** — ETF inflow/outflow, cost-basis proximity ([[institutional-flow-regime]])
- **Volatility** — realized vs implied, ATR, term structure ([[volatility-regime-classification]])
- **Event calendar** — token-unlock schedules, listing announcements, macro prints (CPI/FOMC) ([[event-catalyst-regime]], [[policy-shock-regime]])
- **Security / forensic** — proof-of-reserves shifts, emergency on-chain outflows, stablecoin peg deviation ([[security-black-swan-regime]])

## Classifying the Live Regime

The baskets are not read in parallel — they are read in a **priority order**, because some are backdrops, some are gates, and some are overlays. A workable procedure:

1. **Read the backdrop** — establish [[macro-trend-regime|macro trend]] and [[bitcoin-cycle-regime|BTC-cycle]] state (bull / bear / accumulation / distribution; BTC-led vs alt-rotation). This sets the default directional bias.
2. **Check for a macro override** — is [[crypto-macro-correlation-regime|cross-asset correlation]] high right now (FOMC/CPI window, DXY spike)? If so, macro direction overrides crypto-native signals until the window passes.
3. **Apply the fragility gate** — run [[#The Fragility Triad (canonical)|the fragility triad]] (basis + funding/OI + OI-vs-depth). If it is aligned, cut leverage and bias toward the downside-cascade scenario *regardless of the bullish backdrop*.
4. **Scan for active shocks** — is an [[event-catalyst-regime|event]], [[security-black-swan-regime|security]], or [[policy-shock-regime|policy]] window live? Discrete shocks temporarily supersede everything else.
5. **Confirm with leading signals** — do [[on-chain-regime|on-chain]] flows and [[institutional-flow-regime|ETF flows]] agree with or contradict the backdrop? Disagreement (e.g. on-chain says accumulate but derivatives say fragile) is itself information — usually a sign of a regime transition in progress.
6. **Size and time with the overlays** — apply the [[volatility-regime-classification|volatility]] overlay for position sizing and the [[technical-structural-regime|technical/structural]] overlay for entry/exit timing.

When baskets conflict, the order above resolves it: **shocks > fragility gate > macro override > backdrop**, with overlays governing size/timing throughout. The mapping from each detected regime to a concrete deployable strategy lives in [[regime-strategy-playbook]].

## Regime Transitions

Regimes are not static; they hand off in recognisable chains. The canonical transitions:

- **Trend decay** — [[macro-trend-regime|Bull]] → **Distribution** (rising OI, price stalling, funding bleeding positive) → **Bear**. Distribution is the warning that the bull is ending.
- **Carry build to cascade** — Healthy [[basis-carry-regime|basis]] → High/crowded basis → **basis collapse / [[derivatives-native-regime|liquidation cascade]]** → [[liquidity-depth-regime|post-cascade impaired depth]]. The whole fragility triad walks this path together.
- **Shock sequence** — [[security-black-swan-regime|security/policy shock]] → immediate OI unwind → self-custody / de-risk → stabilisation → **[[institutional-flow-regime|institutional reaccumulation]]**. The short-then-long-reversal shape.
- **Vol regime flip** — [[volatility-regime-classification|Compressed vol]] (calm, leverage building) → **vol expansion / breakout** → vol mean-reversion. Compressed vol is the dry tinder; the triad is the spark.

Detecting the *transition* early — distribution before the bear, basis crowding before the collapse — is where most of the edge lives; see [[market-regime-detection-ml]] for change-point methods.

## Framework Thresholds (Illustrative Heuristics)

Every numeric cut point below is a **vendor heuristic from the framework, not a law** (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). The *direction of travel* matters more than the exact number; treat these as starting calibrations to be tuned and validated [[crypto-perp-backtesting-pitfalls|point-in-time]], not as hard triggers.

| Signal | Heuristic | Basket | Reads as |
|--------|-----------|--------|----------|
| Funding rate | sustained > ~0.1% / 8h (or deeply negative) | [[derivatives-native-regime\|4]] | longs (or shorts) overheated → fade |
| Annualized basis | <3% flat · 3–6% healthy · 6–8% elevated · 8%+ fragile | [[basis-carry-regime\|8]] | carry health / crowding |
| BTC dominance | falling below ~55–60% | [[macro-trend-regime\|1]] | altcoin-season trigger |
| DXY | above ~105 | [[crypto-macro-correlation-regime\|6]] | suppresses risk assets |
| ETF flows | > ~$500M/week sustained | [[institutional-flow-regime\|10]] | institutional accumulation |
| Realized vol | ~30% annualized ATR (compressed) | [[volatility-regime-classification\|13]] | calm masking leverage build |
| RSI | > 80 or < 20 (+ funding extreme + high OI) | [[technical-structural-regime\|14]] | exhaustion / fade setup |
| OI vs depth | OI growing faster than book depth | [[liquidity-depth-regime\|9]] | pre-cascade fragility |

## Current Regime Snapshot (2026-06-03)

A dated example of how the framework reads a live tape (Source: [[2026-06-03-cryptodataapi-14-basket-regime-framework]]). On 2026-06-03 the framework scored the market **bearish**: Market Health 30/100, Short-Term 33/100, Long-Term 28/100 (all bearish); BTC dominance **59.3%**; total cap **$2.40T** (−2.52% on the day); open interest **$54.16B**; 24h liquidations **$727M**; long/short **63.9% / 36.1%** (crowded long into weakness). In taxonomy terms: a [[macro-trend-regime|Full Bear / Distribution]] backdrop with elevated BTC dominance (alts bleeding), crowded-long [[derivatives-native-regime|derivatives positioning]] vulnerable to a downside [[liquidity-depth-regime|cascade]]. This snapshot is illustrative and will be stale by the time you read it — it shows the *reading method*, not a current call.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — Crypto Data API (VENTURE AI LABS), the 14-basket framework this taxonomy is organised after (#meta source summary)
- [[regime-matrix]], [[market-regime-detection-ml]], [[regime-adaptive-strategy]] — existing wiki regime tooling this layer sits on top of
- [[regime-strategy-playbook]] — the regime → concrete-strategy mapping for all 14 baskets
- [[crypto-perp-backtesting-pitfalls]] — why regime gating must be validated point-in-time
- [[2025-10-crypto-liquidation-cascade]] — worked example of a fragility-driven regime shift

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/regimes/current` — current long-horizon market regime (10-state taxonomy)
- `GET /api/v1/quant/market` — HMM regime probabilities, 4h/24h horizons (15-min refresh)
- `GET /api/v1/volatility/regime/score` — market-wide vol-stress composite (0-100)
- `GET /api/v1/liquidity/regime/score` — liquidity fragility composite (0-100)

**Historical data:**
- `GET /api/v1/quant/timeline` — daily market regime labels, 2019-now
- `GET /api/v1/quant/regimes/history` — full 6-regime Parquet download (2020-yesterday)
- `GET /api/v1/quant/history` — point-in-time probability records for backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/regimes/current"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-regimes]].

## Related

- [[regime-strategy-playbook]] — regime → concrete strategy mapping for all 14 baskets
- [[regime-matrix]] — strategy-by-regime matrix (6 generic dimensions)
- [[market-regime-detection-ml]] — HMM / clustering / change-point detection
- [[regime-adaptive-strategy]] — regime-gated strategy switching
- [[volatility-regime-classification]] — basket 13, the volatility overlay
- [[hyperliquid]] — the perps venue the framework targets
- All 14 basket pages are linked in the table above.
