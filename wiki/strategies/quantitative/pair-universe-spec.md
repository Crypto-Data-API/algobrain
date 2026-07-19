---
title: "Pair Universe Specification"
type: reference
created: 2026-07-19
updated: 2026-07-19
status: good
tags: [quantitative, pairs-trading, statistical-arbitrage, crypto, hyperliquid, perpetual-futures, methodology, backtesting, market-microstructure, correlation]
aliases: ["Pair Universe", "AlgoBrain Pair Universe", "Tradeable Pair Universe", "Crypto Pairs Candidate Universe"]
related: ["[[pairs-trading]]", "[[stat-arb]]", "[[statistical-arbitrage]]", "[[correlation-regime-pairs]]", "[[pairs-with-funding-differential]]", "[[vol-balanced-pairs]]", "[[oi-gated-pairs]]", "[[unlock-pair-hedge]]", "[[ornstein-uhlenbeck]]", "[[cointegration]]", "[[hyperliquid]]", "[[funding-rate]]", "[[open-interest]]", "[[liquidity]]", "[[cryptodataapi]]"]
---

# Pair Universe Specification

This page is the canonical reference for AlgoBrain's **tradeable pair universe** on Hyperliquid perpetuals. It defines the candidate pool, the screening funnel that converts candidates into actively tradeable pairs, the refresh cadence, and which strategy pages consume the output. All funnel-attrition figures are honest estimates labeled as such — no backtest has been run against this exact specification.

The pair universe is a shared input. Every pairs/stat-arb strategy in this wiki — [[pairs-trading]], [[statistical-arbitrage]], [[correlation-regime-pairs]], [[pairs-with-funding-differential]], [[vol-balanced-pairs]], [[oi-gated-pairs]], [[unlock-pair-hedge]] — starts here and applies its own additional filters on top of the universe screen.

## Candidate Universe

**Base pool:** all unordered pairs of actively-traded Hyperliquid perpetual markets.

As of mid-2026, Hyperliquid lists approximately **206 perpetual markets** (this count fluctuates as new listings are added and delistings occur; verify against `GET /api/v1/hyperliquid/meta` before each refresh). The number of unordered pairs from N markets is N(N−1)/2:

> **206 markets → ~21,115 candidate pairs** (estimate; exact count depends on current HL listings at refresh time)

In practice, candidates are filtered to a **working set** before cointegration testing — applying the liquidity-depth minimum (see Funnel Step 4 below) up-front reduces computation from ~21,000 pairs to a manageable subset of a few hundred.

## Screening Funnel

The funnel runs in five sequential gates. A pair must pass all five to enter the tradeable universe. Gates are applied in order of computational cost — cheapest first.

---

### Gate 1: Rolling Correlation Floor

**Filter:** 30-day rolling Pearson correlation of log-returns ≥ **0.70**

- Computed on 1h close prices from `/api/v1/hyperliquid/candles`.
- Captures structural co-movement. A pair that does not co-move reliably 70%+ on a rolling basis has no basis for a mean-reverting spread — any "cointegration" found in Gate 2 is likely spurious.
- This gate eliminates the majority of the ~21,000 candidates. Most cross-sector pairs (e.g., a DeFi token paired with a gaming token) fail here. The typical pass rate from this gate alone is estimated at **15–25%** of candidates, leaving ~3,000–5,000 pairs for Gate 2.
- Re-checked weekly at re-screen.

**Inline exit during a live trade:** if rolling correlation falls below **0.60** while a spread position is open → immediate flatten. (See [[correlation-regime-pairs]] for the full regime-gate flatten logic.)

---

### Gate 2: Engle-Granger / ADF Cointegration Test

**Filter:** Engle-Granger two-step cointegration test on a rolling **90-day** window of daily closes; ADF on the residual with p-value ≤ **0.10**

- Run via `statsmodels.tsa.stattools.coint` (Python) on daily kline data from `/api/v1/market-data/klines` or `/api/v1/hyperliquid/candles` resampled to daily.
- The 10% significance level (rather than the more conventional 5%) is chosen deliberately — crypto pair relationships are less stable than equity pairs, and setting p ≤ 0.05 would reject too many genuinely co-moving pairs on short windows. Traders using this universe for higher-conviction entries (e.g., [[correlation-regime-pairs]]) can tighten to p ≤ 0.05.
- Alternative: Johansen trace test at 5% significance on the same 90-day window; either test is accepted.
- **Estimated pass rate from Gate 2:** approximately 40–60% of Gate 1 survivors (the correlation floor strongly pre-selects for cointegrated pairs). Roughly **1,200–3,000 pairs** reach Gate 3.

> **Honest note:** cointegration tests on 90-day crypto windows have moderate statistical power. At p ≤ 0.10 and ~3,000 tests, statistical noise generates approximately 300 false positives (10% of 3,000). Gates 3–5 provide additional rejection power that reduces false positives in the final universe.

---

### Gate 3: Ornstein-Uhlenbeck Half-Life Bounds

**Filter:** OU process half-life of the spread **≥ 3 days AND ≤ 45 days**

- Estimated by fitting an AR(1) to the spread residual: `half_life = ln(2) / abs(log(ar1_coeff))`.
- **Half-life < 3 days:** spread reverts too quickly; round-trip execution costs (4 fills at ~5 bps taker each = 20 bps) consume the reversion signal before it can be captured. Exclude.
- **Half-life > 45 days:** spread reverts too slowly; funding-rate carry on the perp legs accumulates for weeks before the trade resolves. At 0.03%/8h positive funding on one leg × 45 days = ~40 bps of carry drag, which competes with a typical 2σ entry's gross reversion P&L. Exclude.
- See [[ornstein-uhlenbeck]] for the OU model and half-life derivation.
- **Estimated pass rate from Gate 3:** ~60–80% of Gate 2 survivors. Some pairs that appear cointegrated have very long or very short mean-reversion times. Net estimate: **~720–2,400 pairs** reach Gate 4.

---

### Gate 4: Liquidity-Depth Minimums (Both Legs)

**Filter:** both legs must individually pass:
1. Average **daily perpetual volume ≥ $5M** (7-day trailing average): ensures the position can be built and unwound at a target notional of up to $250K without moving the market more than ~5 bps.
2. **Bid-side depth within 25 bps ≥ $100K** at the time of the weekly screen: from `/api/v1/liquidity/depth?coin=X&type=bid&bps=25`.

- The $5M volume floor and $100K depth floor are conservative minimums for a book targeting $50K–$500K per pair. Scale these proportionally for larger or smaller books.
- This gate is the hardest practical bottleneck for the long tail of HL-listed tokens. Approximately half of the ~206 HL perps have < $5M daily volume. Applied to Gate 3 survivors: **estimated ~200–600 pairs** pass.

---

### Gate 5: Funding-Differential Check

**Filter:** |funding_A − funding_B| < **0.10%/8h** on a 7-day average

- A persistent large funding differential between the two perp legs creates a structural carry headwind on one side of every spread entry. If the funding spread is > 0.10%/8h (annualizing to > 109% p.a. on one leg), the carry erodes the spread-reversion P&L faster than the edge can compound.
- Pairs that fail this gate with a *favourable* funding differential (the spread direction earns net positive funding) are **not excluded** — they are flagged as "funding-enhanced" and routed to the [[pairs-with-funding-differential]] strategy for priority deployment.
- Funding data: `/api/v1/derivatives/funding-rates?coin=X` and equivalent for both legs.
- **Estimated pass rate from Gate 5:** ~80–90% of Gate 4 survivors pass. The funding-differential exclusion bites most on pairs where one leg is a meme coin or a high-speculative asset with persistent extreme funding. Net estimate: **~160–540 pairs** in the tradeable universe.

---

## Funnel Summary

| Gate | Filter | Pass rate (estimate) | Running count (estimate) |
|------|--------|---------------------|--------------------------|
| Candidate pool | All HL perp pairs | — | ~21,100 |
| Gate 1 | Rolling correlation ≥ 0.70 (30d) | ~15–25% | ~3,150–5,280 |
| Gate 2 | Cointegration p ≤ 0.10 (90d Engle-Granger or Johansen) | ~40–60% | ~1,260–3,170 |
| Gate 3 | OU half-life 3–45 days | ~60–80% | ~760–2,540 |
| Gate 4 | Both legs: volume ≥ $5M/day AND depth ≥ $100K at 25 bps | ~25–40% | ~190–1,020 |
| Gate 5 | |funding differential| < 0.10%/8h (unfavourable pairs only) | ~80–90% | **~150–920** |

> **Honest attrition estimate:** approximately **2–5% of the ~21,100 candidate pairs pass all five gates** and enter the tradeable universe. The wide range reflects uncertainty about the distribution of HL-listed token liquidity and cointegration stability at any given re-screen date. The final universe is expected to contain **roughly 150–500 pairs**, heavily weighted toward liquid major-pairs, L1-L1 peers, L2-L2 peers, and same-sector DeFi token pairs.

No backtest has validated these attrition rates. They are illustrative estimates derived from applying the gate parameters to the logic of the tests and the known liquidity distribution of HL perpetuals. They should be verified empirically on the first full re-screen.

## Refresh Cadence

| Cycle | Action |
|-------|--------|
| **Weekly re-screen** | Re-run Gates 1–3 on all pairs currently in the tradeable universe. Drop any pair that now fails any gate. Add new candidates that have recently entered Gate 1. Re-estimate the hedge ratio (OLS β) for all surviving pairs using the most recent 90-day window. **Do not re-fit the hedge ratio on an open position** (PIT discipline — see [[correlation-regime-pairs#Indicators / data used]]). |
| **Monthly full re-estimation** | Re-run the full funnel (all five gates) starting from the complete ~21,100 candidate pool. Update the OU half-life, cointegration p-value, and liquidity metrics. Accept new pairs, formally retire pairs that fail two consecutive monthly screens. Update the funded-pair flag for [[pairs-with-funding-differential]] routing. |
| **New HL listing** | Any new Hyperliquid listing is added to the candidate pool immediately. It enters Gate 1 as soon as 30 days of 1h kline data is available. Do not fast-track new listings — 30-day correlation and 90-day cointegration windows are required minimums. |
| **Post-shock re-check** | After a structural event (exchange exploit, major protocol upgrade, governance attack, large unlock ≥ 10% of supply), immediately re-run Gates 1–3 on all pairs involving the affected token. Remove immediately if any gate fails. |

## Sector Prioritisation

Within the tradeable universe, pairs are additionally tagged by sector relationship for deployment by consuming strategies:

| Sector tag | Representative pairs | Notes |
|------------|---------------------|-------|
| `major-cross` | BTC/ETH, ETH/SOL | Highest liquidity; tight spreads; lowest alpha but most reliable |
| `l1-peers` | SOL/AVAX, SUI/APT, NEAR/ATOM | Same-layer competition; cointegration driven by shared TVL contest |
| `l2-peers` | ARB/OP, STRK/MANTA | Optimistic/ZK rollup pairs; similar token economics, similar unlock schedules |
| `defi-peers` | AAVE/COMP, UNI/CRV, GMX/DYDX | Same-protocol-category pairs; cointegration driven by shared DeFi narrative |
| `lst-peers` | LDO/RPL, ETHFI/SSV | Ethereum liquid-staking competitors; tight ETH-staking anchor |
| `ai-peers` | TAO/FET, WLD/RNDR | AI-narrative sector; less stable cointegration; higher alpha when it holds |
| `cex-token-peers` | BNB/OKB, etc. | Exchange-token pairs; cointegration via shared exchange-volume driver |

Sector tags inform which strategy consumes which pairs. [[cross-sectional-relative-value]] runs sector-ranked long-short books within each sector. [[unlock-pair-hedge]] sources its beta-matched peer from the same sector tag as the unlocking token.

## Strategy Consumers of This Universe

The following strategy pages draw their eligible pair sets from this specification:

| Strategy | How it uses the universe |
|----------|-------------------------|
| [[pairs-trading]] | The foundational pairs strategy; the universe is its eligible set |
| [[stat-arb]] | Statistical arbitrage across a diversified book of universe pairs |
| [[statistical-arbitrage]] | Same as stat-arb; this page provides the theoretical framework |
| [[correlation-regime-pairs]] | Applies an additional three-factor regime gate (correlation ≥ 0.70, cointegration p ≤ 0.10, half-life 3–45 days) — these mirror Gates 1–3 of this funnel, run daily rather than weekly |
| [[pairs-with-funding-differential]] | Sources "funding-enhanced" pairs flagged at Gate 5 (favourable funding differential agrees with spread direction) |
| [[vol-balanced-pairs]] | Draws from the universe and applies vol-ratio position sizing between legs |
| [[oi-gated-pairs]] | Draws from the universe and adds an OI-based squeeze-precondition exclusion on the short leg |
| [[unlock-pair-hedge]] | Sources the beta-matched hedge leg from the same sector tag as the unlocking token |

## Data Endpoints

All data used in the funnel is available from [[cryptodataapi|CryptoDataAPI]]. No third-party cointegration API is used — test computations are performed in Python using `statsmodels` and `scipy`.

**Live data:**
- `GET /api/v1/hyperliquid/meta` — full list of current HL perp markets (for candidate pool enumeration)
- `GET /api/v1/hyperliquid/candles?coin=X&interval=1h&limit=720` — 30 days of 1h klines for Gate 1 correlation
- `GET /api/v1/hyperliquid/candles?coin=X&interval=1d&limit=120` — 90+ days of daily klines for Gate 2 cointegration
- `GET /api/v1/liquidity/depth?coin=X&type=bid&bps=25` — bid-side depth for Gate 4
- `GET /api/v1/derivatives/funding-rates?coin=X` — 8h funding for Gate 5

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for rolling re-estimation and walk-forward screening
- `GET /api/v1/backtesting/funding` — historical funding for Gate 5 back-validation

```bash
# Enumerate current HL perp universe
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/meta"

# Pull 90-day daily klines for cointegration test
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/hyperliquid/candles?coin=SOL&interval=1d&limit=120"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]], [[cryptodataapi-market-data]], [[cryptodataapi-derivatives]].

## Related

- [[pairs-trading]] — the foundational strategy; this page is its universe specification
- [[statistical-arbitrage]] — the theoretical framework for convergence trades
- [[stat-arb]] — redirect to statistical-arbitrage
- [[correlation-regime-pairs]] — adds a live three-factor regime gate on top of this funnel
- [[pairs-with-funding-differential]] — priority deployment for funding-enhanced pairs from Gate 5
- [[vol-balanced-pairs]] — vol-ratio sizing layer applied to universe pairs
- [[oi-gated-pairs]] — OI squeeze-precondition filter applied on top of the universe
- [[unlock-pair-hedge]] — beta-matched short hedge sourced from sector-tagged universe
- [[ornstein-uhlenbeck]] — OU half-life estimation (Gate 3)
- [[cointegration]] — Engle-Granger / Johansen cointegration theory (Gate 2)
- [[hyperliquid]] — the exchange whose perpetual markets form the candidate universe
- [[cryptodataapi-hyperliquid]] — endpoint catalog for HL market data
- [[cryptodataapi-market-data]] — klines and OHLCV endpoints
