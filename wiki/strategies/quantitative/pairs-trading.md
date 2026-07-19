---
title: "Pairs Trading"
type: strategy
created: 2026-04-06
updated: 2026-07-19
status: good
tags: [mean-reversion, pairs-trading, statistical-arbitrage, market-neutral, quantitative, cointegration, crypto]
aliases: ["Pairs Trade", "Statistical Pairs Trading", "Stat Arb Pairs", "Crypto Pairs"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [analytical, behavioral, risk-bearing]
edge_mechanism: "Two economically linked crypto assets are pulled apart by single-name flow (a listing, unlock, narrative rotation, or liquidation in one leg); the pairs trader models the relationship, supplies liquidity against the divergence, and is paid the reversion — while hedging out BTC-beta so the only bet is convergence."
data_required: [ohlcv-1h, ohlcv-daily, funding-rates, cointegration-window]
min_capital_usd: 5000
capacity_usd: 20000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 30
decay_evidence: "Crypto cointegration is far less stable than the equity pairs literature assumes: relationships that pass Engle-Granger in-sample routinely break when BTC dominance rotates or a token has an idiosyncratic catalyst (unlock, hack, delisting). The reliable pairs (ETH/BTC, staked-vs-spot) have tight, well-arbitraged spreads; the loose pairs revert only until they don't."
kill_criteria: |
  - strategy-level drawdown > 20% from high-water mark
  - rolling 12-month net Sharpe < 0
  - fraction of pairs failing weekly cointegration re-test > 40% for 2 consecutive weeks
  - average realized half-life > 2x modeled half-life over a 40-trade sample
  - any single pair: |z| >= 3.0, cointegration p > 0.05 on re-test, or 2x half-life time stop
related: ["[[statistical-arbitrage]]", "[[mean-reversion]]", "[[bollinger-band-reversion]]", "[[ornstein-uhlenbeck]]", "[[kalman-filter-trading]]", "[[cointegration]]", "[[correlation]]", "[[market-neutral]]", "[[funding-rate-arbitrage]]", "[[book-algorithmic-trading-ernest-chan]]", "[[book-pairs-trading-vidyamurthy]]", "[[cryptodataapi]]"]
---

# Pairs Trading

Pairs trading is a [[market-neutral]] [[statistical-arbitrage]] strategy that identifies two cointegrated crypto assets and profits from temporary divergences in their price relationship. When the spread between the two widens beyond its historical norm, you go **long the underperformer** and **short the outperformer** (usually via perps), betting the spread reverts. Because you hold offsetting legs, the trade hedges out most BTC-beta and is close to direction-neutral — the bet is convergence, not market direction. The strategy was pioneered at Morgan Stanley in the 1980s by Nunzio Tartaglia's quant group (Source: [[book-pairs-trading-vidyamurthy]]); in crypto it is harder than in equities because cointegration is less stable and almost every altcoin is dominated by a single common factor — BTC.

The critical distinction is between **correlation** and **cointegration**. Two assets can be highly correlated (move together) without being cointegrated (maintaining a stable long-run spread). Pairs trading requires **cointegration** — a *mean-reverting* spread (Source: [[book-algorithmic-trading-ernest-chan]]). In crypto this is a sharp trap: nearly all majors are ~0.7–0.9 correlated to BTC, which looks like a tradeable relationship and is not. Testing uses the **Engle-Granger two-step** or **Johansen** test on a rolling window.

## Edge source

Per [[edge-taxonomy]], crypto pairs trading is primarily **analytical**, secondarily **behavioral / risk-bearing**:

- **Analytical** — the edge is modeling skill: finding genuinely cointegrated crypto relationships (not just BTC-correlated ones), estimating a hedge ratio and reversion speed correctly, and distinguishing temporary divergence from a structural break (an unlock, a delisting, a narrative death). Most participants run correlation, not [[cointegration]], and get run over.
- **Behavioral / risk-bearing** — divergences are created by flow insensitive to the *relative* value: a single-coin listing pump, an unlock dump, a narrative rotation (money leaving L1s for memecoins), or a liquidation in one leg only. The pairs book sells liquidity to that flow and warehouses convergence risk.

## Why this edge exists

Economically linked crypto assets — ETH vs BTC, two L1s competing for the same TVL, two liquid-staking tokens, an asset and its perp, exchange tokens — are tied by fundamentals, but their short-term order flow is not synchronized. When flow hits one leg (a Coinbase listing on one L2 but not its rival, a $200M unlock, a leverage flush concentrated in one coin), its price temporarily detaches from its statistical twin.

**Who is on the other side:** momentum chasers piling into the pumping leg, forced sellers dumping the unlocking leg, and discretionary traders who evaluate each coin on its own narrative rather than relative to a peer. They "lose" the spread because they are paying for immediacy or trading a single-name story; the pairs trader prices the relationship. The edge persists in attenuated form because warehousing crypto convergence risk is genuinely unpleasant — spreads can widen violently before converging (or never converge, when the "twin" turns out to be a dying project), and the book suffers correlated losses exactly when leveraged peers deleverage.

## Null hypothesis

If the two prices follow independent random walks, no linear combination is stationary and the "spread" is itself a random walk: z-score entries at ±2 are followed by divergence as often as convergence, and P&L equals the negative of fees plus funding carry. The null is directly testable — cointegration tests should *fail* at the 5% level on the chosen pair, and a backtest on **randomly matched** crypto tickers should produce zero gross alpha. A real edge requires (a) in-sample cointegration that (b) survives out-of-sample, and (c) a half-life of days-to-weeks fast enough to beat funding carry and cost drag. The crypto-specific trap: BTC-beta makes almost any two majors *look* related, so the null must be tested against a **BTC-neutralized residual**, not raw prices.

## Rules

### Pair selection
1. Candidate pairs need an economic reason to co-move: same sector (two L1s, two DEX tokens, two LSD tokens), an asset vs its own perp, or a wrapped/staked derivative vs its underlying. Avoid pairing two coins whose only link is "both go up when BTC goes up."
2. Test for **cointegration** (Engle-Granger p < 0.05 or Johansen) on 60–180 days of 1h or 1d data. Re-test **weekly** — crypto relationships decay faster than equities.
3. Estimate the **hedge ratio** β by OLS or a dynamic [[kalman-filter-trading|Kalman filter]] (preferred in crypto, where β drifts).
4. Compute the **spread** = P_A − β·P_B; verify stationarity (ADF) and an [[ornstein-uhlenbeck]] half-life between ~2 and ~20 days.

### Entry
1. Rolling z-score of the spread (60-bar window): z = (spread − mean) / std.
2. **Long spread** (buy A, short β·B) when z ≤ −2.0. **Short spread** (short A, buy β·B) when z ≥ +2.0.
3. Confirm neither leg has an imminent catalyst (unlock, listing, upgrade) that would break cointegration — check the CDA event calendar (see [[#Getting the Data (CryptoDataAPI)]]).

### Exit
1. **Mean-reversion exit:** close both legs when z returns to 0 (or ±0.5 for partial).
2. **Stop-loss:** close both legs if |z| ≥ 3.0–3.5 (spread diverging — cointegration likely breaking).
3. **Cointegration-break stop:** close immediately if the weekly re-test fails (p > 0.05).
4. **Time stop:** close if the spread has not reverted within 2× the modeled half-life.

### Position sizing
- Dollar-neutral by hedge ratio: long-leg notional = short-leg notional × β. Risk ≤ 0.5–1% of equity per pair (measured at the |z| ≥ 3 stop); run 5–15 pairs concurrently.
- Keep gross leverage modest (1–3×). Crypto pairs blow up on correlated widening, not on any single leg — the same lesson the August 2007 equity quant quake taught, at higher vol.

## Implementation pseudocode

```python
# crypto pairs trading — perp legs, dynamic hedge ratio
for pair in candidate_pairs:                       # economically-linked, not just BTC-correlated
    if engle_granger_pvalue(pair, lookback_days=90) > 0.05:
        retire(pair); continue
    beta      = kalman_hedge_ratio(pair)           # drifts in crypto — prefer KF over static OLS
    spread    = pair.A - beta * pair.B
    half_life = ou_half_life(spread)
    if not (2 <= half_life <= 20):                 # days
        retire(pair); continue
    if catalyst_within(pair.A, days=half_life) or catalyst_within(pair.B, days=half_life):
        continue                                   # unlock / listing / upgrade breaks cointegration

    z = (spread[-1] - mean(spread[-60:])) / std(spread[-60:])

    if no_position(pair):
        if z >= 2.0:  open(short=pair.A, long=beta*pair.B, risk=0.005*equity)
        if z <= -2.0: open(long=pair.A,  short=beta*pair.B, risk=0.005*equity)
    else:
        if abs(z) <= 0.5:                    close(pair)   # converged
        elif abs(z) >= 3.0:                  close(pair)   # structural-break stop
        elif failed_retest(pair):            close(pair)   # cointegration broke
        elif days_held(pair) > 2*half_life:  close(pair)   # time stop
```

## Indicators / data used

- **Spread** (price difference adjusted by hedge ratio β) and its rolling **z-score**.
- **Cointegration tests:** Engle-Granger, Johansen; ADF for spread stationarity.
- **Dynamic hedge ratio** via [[kalman-filter-trading|Kalman filter]] — important in crypto where β between two coins drifts materially over weeks.
- **[[ornstein-uhlenbeck]] half-life** — sets the expected holding period and the time stop.
- **[[funding-rate]]** on both perp legs — the crypto analogue of equity borrow cost; a persistently negative funding differential is a hidden carry drag on the trade.
- **Rolling correlation and BTC-beta** — to confirm the spread is a *relationship*, not just two BTC-beta legs.

## Crypto pairs examples

| Pair | Category | Rationale | Caveat |
|------|----------|-----------|--------|
| ETH / BTC | Majors | The single most-traded crypto ratio; deep, liquid, relatively stable | Tight, well-arbitraged — small edge |
| SOL / ETH | L1 vs L1 | Compete for smart-contract TVL and narrative | Rotates hard; cointegration breaks in alt-seasons |
| LDO / RPL | Liquid-staking tokens | Same sector, same ETH-staking driver | Idiosyncratic governance/unlock risk |
| ARB / OP | L2 tokens | Optimistic-rollup peers with correlated flows | Unlock schedules differ — a classic break source |
| stETH / ETH | Derivative vs underlying | Tightly pegged; reverts reliably | Depeg tail (June 2022) is a total-loss scenario |
| BTC-perp / BTC-spot | Basis | The perp-vs-spot spread is [[funding-rate-arbitrage]] | Different strategy family — funding, not z-score |

## Example trade

**Pair:** ARB / OP (L2 tokens), 1h bars.
1. Hedge ratio (Kalman, ≈180-day window): β = 1.15. Spread = ARB − 1.15·OP. Engle-Granger p = 0.02; OU half-life ≈ 6 days.
2. Mean spread ≈ 0; rolling σ = 0.008. OP pumps on a listing rumor while ARB is flat. Spread = −0.017 → z = −2.1.
3. Enter: long $5,000 ARB-perp, short $5,750 OP-perp (dollar-neutral by β). Combined entry cost ~10 bps taker.
4. Over 5 days the rumor fades, OP gives back the pop, spread reverts to z = +0.3.
5. Exit both legs. Gross convergence gain ≈ +1.4% on gross exposure (~$140 on the ~$10k pair); ~+0.9% after ~30 bps all-in round-trip cost (both legs, entry + exit) and slightly adverse funding on the OP short.
6. Had OP announced a genuine ecosystem catalyst and the spread pushed through z = −3.0, the stop cuts the trade for roughly −1% — the cost of the false negatives.

## Performance characteristics

Realistic, cost-corrected expectations (not a backtest of this exact spec):

- **Win rate:** 55–65% when pairs are genuinely cointegrated and re-tested weekly; drops toward coin-flip if correlation is mistaken for cointegration.
- **Profit factor:** ~1.3–1.8. The market-neutral design caps both tails.
- **Sharpe:** net ~0.4–0.8 for a diversified crypto pairs book (frontmatter assumes 0.6). Lower than the 1.0–2.0 the equity literature quotes, because crypto cointegration is less stable and costs are higher.
- **Best conditions:** range-bound, stable-dominance regimes where sector relationships hold.
- **Worst conditions:** BTC-dominance rotations, alt-seasons, and idiosyncratic breaks (one leg gets delisted, exploited, or has a large unlock).

**Cost overlay (crypto, per pair round trip = 4 executions):**

| Component | Magnitude | Why it bites |
|---|---|---|
| Taker fees, both legs, entry + exit | ~16–22 bps | Four fills per completed trade |
| Slippage | ~4–20 bps | Alt legs are thin; the short leg especially |
| Funding carry differential | ±1–4 bps/day | Crypto's "borrow cost"; can be a credit or a drag |
| Gross edge per converged trade | ~80–200 bps | Costs consume 20–40% |
| **Breakeven (frontmatter)** | **~30 bps** | Edge must clear this before funding carry |

Costs are the binding constraint: a high-turnover, four-fill trade earning modest per-trade edges only survives with maker-biased execution, liquid legs, and disciplined weekly re-qualification.

## Capacity limits

Bounded by the thinner of the two legs. Liquid major pairs (ETH/BTC, SOL/ETH) absorb the most — into the low tens of millions — before your own entries move the spread; sector-token and L2 pairs cap out far lower ($1–5M) because the loose leg's perp book is shallow during exactly the divergence windows you trade. Frontmatter assumes **$20M** as a blended ceiling for a diversified book. Crowding risk is **high**: the obvious crypto pairs (ETH/BTC, the major L1 rotations) are traded by every quant desk, so capacity is shared, not per-fund — and a peer's forced unwind widens *your* spreads too.

## What kills this strategy

The most likely failure modes (see [[failure-modes]]):

1. **Cointegration break (structural).** An unlock, delisting, hack, migration, or narrative death permanently breaks the relationship — the spread never comes back. This is the single largest source of pair-level losses in crypto, and it happens more often than in equities.
2. **BTC-dominance rotation (regime).** In an alt-season or a flight-to-BTC, whole sectors decouple at once; every crowded spread widens together and stops force selling into the widening.
3. **Reversion-speed regime shift.** Half-lives lengthen in trending markets, turning a 6-day trade into a multi-week funding bleed.
4. **Funding/carry recall.** A persistently expensive short leg (deeply positive funding you are paying) is the crypto version of a borrow squeeze; it silently erodes the edge.
5. **Overfitting.** Data-mining thousands of coin pairs guarantees spurious in-sample cointegration — the Engle-Granger test on 1,000 random pairs "passes" ~50 by chance. See [[overfitting-detection]].
6. **Correlation-for-cointegration confusion.** Pairing two BTC-beta legs and calling it market-neutral — the spread trends instead of reverting.

## Kill criteria

- Strategy-level drawdown > 20% from high-water mark → halve gross; > 25% → flat and full review.
- Rolling 12-month net Sharpe < 0 → stop new entries, wind down.
- Fraction of pairs failing weekly cointegration re-test > 40% for 2 consecutive weeks → universe is broken, halt.
- Average realized half-life > 2× modeled over a 40-trade sample → reversion regime changed, halt.
- Any single pair: |z| ≥ 3.0, cointegration p > 0.05 on re-test, or 2× half-life time stop → close that pair (per Rules).

See [[when-to-retire-a-strategy]].

## Advantages

- [[market-neutral]] — profits in up, down, or sideways crypto markets; BTC-beta largely hedged out.
- Statistically rigorous framework with decades of academic foundation and a well-understood failure history.
- Losses are bounded when stops are respected — the two legs partially hedge each other.
- Fully automatable end-to-end (pair selection, cointegration testing, execution) on 24/7 markets.

## Disadvantages

- **Cointegration is fragile in crypto** — historical relationships break far more often than in equities (unlocks, delistings, migrations, narrative death).
- **Requires shorting both directions** — perp funding carry replaces equity borrow cost and can be a persistent drag; short squeezes in crypto are violent.
- **Execution complexity** — two (often four) simultaneous legs double the fees, slippage, and operational risk.
- **Model risk** — wrong hedge ratio, lookback, or correlation-vs-cointegration confusion produces convincing but fake signals.
- **Crowded** — the obvious pairs are traded by every quant desk; capacity and edge are shared.
- **Capital-intensive** — market-neutral returns are modest per unit of capital, tempting operators into dangerous leverage.

## Sources

- [[book-algorithmic-trading-ernest-chan]] — the definitive practical reference for pairs trading: cointegration testing, hedge-ratio estimation, the Johansen test, and the connection to [[ornstein-uhlenbeck]] and [[kalman-filter-trading]].
- [[book-pairs-trading-vidyamurthy]] — Vidyamurthy (2004): the foundational treatment of cointegration theory, spread modeling, and the Morgan Stanley origins.
- Gatev, Goetzmann & Rouwenhorst (2006), "Pairs Trading: Performance of a Relative-Value Arbitrage Rule," *Review of Financial Studies* — the canonical equity study (documented decay), directly relevant to why crypto pairs edges are modest and decaying.
- Khandani & Lo (2007/2011), "What Happened to the Quants in August 2007?" — the crowding/deleveraging failure mode this strategy shares.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000` — OHLCV for each leg (compute spread, β, z-score)
- `GET /api/v1/hyperliquid/candles?coin=SOL&interval=1h&limit=1000` — OHLCV for HL perp legs (broad alt coverage)
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — per-leg funding (the crypto "borrow cost")
- `GET /api/v1/event/calendar` — unlocks / listings / upgrades that break cointegration

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for cointegration + spread backtests
- `GET /api/v1/backtesting/funding` — funding history for the carry overlay
- `GET /api/v1/backtesting/symbols` — which symbols have backtest-grade history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — spread, β, and z-score from `GET /api/v1/market-data/klines?interval=1h` (CEX legs) and `GET /api/v1/hyperliquid/candles?interval=1h` (alt-perp legs); `GET /api/v1/derivatives/funding-rates` per leg is the crypto "borrow cost" that decides whether a slow spread is worth holding
- **Catalyst filter** — `GET /api/v1/event/calendar` before entry: an unlock or listing on either leg inside the half-life window is a cointegration-break waiting to happen
- **Regime gate** — `GET /api/v1/quant/market`: stand down in `vol_spike` (correlated deleveraging widens every crowded spread at once) and treat BTC-dominance rotations as re-test triggers
- **Backtest** — `GET /api/v1/backtesting/klines` (Binance spot 1h/4h/1d back to 2017-08; HL daily to 2023) for out-of-sample cointegration re-tests; `GET /api/v1/backtesting/funding` (HL hourly since 2023-05) for the short-leg carry; `GET /api/v1/backtesting/symbols` + dated `GET /api/v1/backtesting/daily-snapshots/{date}` (since 2026-03-02) keep delisted legs in the test universe
- **Tips** — schedule the weekly Engle-Granger re-test as an automated job and close any pair that fails it (p > 0.05) the same day; batch the pair universe against `GET /api/v1/quant/coins/risk` for per-leg sizing

## Instrument Structures

Pairs trading deploys on exactly one structure: the **pair**.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Pair** | The defining structure. Every trade is a two-legged long-short spread (long the underperformer, short the outperformer) sized to be dollar-neutral by hedge ratio. The spread is the unit of analysis; single-leg P&L is irrelevant. |
| Single-asset | Not deployed. Pairs trading is explicitly market-neutral — directional single-asset positions are a signal the hedge ratio or cointegration model has failed. |
| Basket | Not deployed in this strategy. Cross-sectional basket versions of the same logic live in [[statistical-arbitrage]] and [[cross-sectional-relative-value]]. |
| Cross-venue | Not deployed here. Cross-venue versions of the spread (same asset, different exchanges) are [[funding-rate-arbitrage]] and [[hl-vs-cex-funding-divergence]]. |

Mechanics specific to the pair structure: the hedge ratio β determines relative leg sizing; the spread z-score is the entry signal; cointegration (not correlation) is the required statistical property; and funding carry on both perp legs must be tracked as the crypto "borrow cost" for each leg independently.

## Related

- [[statistical-arbitrage]] — the broader category that includes pairs trading
- [[mean-reversion]] — the underlying market behavior it exploits
- [[ornstein-uhlenbeck]] — the model for spread half-life and holding period
- [[kalman-filter-trading]] — dynamic hedge-ratio estimation (preferred in crypto)
- [[cointegration]] — the required statistical property (not correlation)
- [[correlation]] — necessary but not sufficient; the crypto BTC-beta trap
- [[bollinger-band-reversion]] — can be applied to the spread for visual entry
- [[market-neutral]] — the portfolio characteristic pairs trading achieves
- [[funding-rate-arbitrage]] — the perp-vs-spot "basis pair" and the funding-carry mechanics
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
