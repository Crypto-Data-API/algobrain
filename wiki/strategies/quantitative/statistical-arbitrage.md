---
title: Statistical Arbitrage
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: excellent
tags:
  - quantitative
  - arbitrage
  - pairs-trading
  - mean-reversion
  - crypto
aliases:
  - stat-arb
  - stat arb
  - statistical arb
related: ["[[pairs-trading]]", "[[mean-reversion]]", "[[arbitrage]]", "[[cointegration]]", "[[kalman-filter-trading]]", "[[ornstein-uhlenbeck]]", "[[funding-rate-arbitrage]]"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: untested
edge_source: [analytical, behavioral, risk-bearing]
edge_mechanism: "Temporary divergences between cointegrated crypto assets (or a coin and its factor basket) are created by single-name flow — listings, unlocks, narrative rotations, liquidations; the stat-arb book supplies liquidity against that flow, neutralizes BTC-beta, and harvests the reversion in aggregate across many spreads."
data_required: [ohlcv-1h, ohlcv-daily, funding-rates, open-interest, volatility-regime]
min_capital_usd: 25000
capacity_usd: 30000000
crowding_risk: high
expected_sharpe: 0.6
expected_max_drawdown: 0.20
breakeven_cost_bps: 30
decay_evidence: "The crypto analogue of the equity decay story: the obvious relationships (ETH/BTC, major L1 baskets) are traded by every quant desk and offer thin, well-arbitraged edges, while the loose relationships break structurally more often than equities. Naive z-score reversion that worked in 2019-2021 alt markets degrades as CEX/perp-DEX market-making tightens and as BTC-dominance rotations decouple whole sectors at once."
kill_criteria: |
  - strategy-level drawdown > 20% from high-water mark
  - rolling 12-month net Sharpe < 0
  - fraction of pairs/baskets failing weekly cointegration re-test > 40% for 2 consecutive weeks
  - average realized half-life > 2x modeled over a 60-trade sample
  - median realized round-trip cost > 30 bps for a full month
---

# Statistical Arbitrage

A quantitative strategy that exploits statistical mispricings between related crypto assets, most simply through [[pairs-trading]] and more generally through factor-residual baskets. Positions are dollar- or BTC-beta-neutral (long the cheap leg/coins, short the rich ones) and rely on [[mean-reversion]] of a price *relationship*, not a directional view. It is a systematic, probabilistic form of [[arbitrage]] — unlike true arbitrage, each individual trade can lose; the edge only exists in aggregate across many spreads. The technique was pioneered on equities at Morgan Stanley in the mid-1980s (Tartaglia's group, Bamberger's original pairs idea) and industrialized by D. E. Shaw and Renaissance; crypto is a newer, noisier, more reflexive proving ground for the same machinery.

Statistical arbitrage is the systematic, market-neutral end of the [[mean-reversion]] family. Where [[contrarian-extremes]] reverts on *sentiment* and directional reversion reverts on a single price, stat arb reverts on a *statistical relationship* between assets — and hedges out BTC-beta so the only bet is convergence. [[pairs-trading]] is its simplest two-asset instance; factor-basket and residual-reversion variants generalize it to hundreds of coins. The edge is real but crowded on the obvious relationships and fragile on the loose ones, with a notorious tail-risk signature (correlated deleveraging — the crypto analogue of the August 2007 equity quant quake).

### At a Glance

| Dimension | Detail |
|---|---|
| Family | Market-neutral [[mean-reversion]] / relative value |
| Simplest case | [[pairs-trading]] (two cointegrated coins) |
| Edge type | Analytical (modeling) + behavioral/risk-bearing (liquidity provision) |
| Required statistic | [[cointegration]], NOT correlation |
| Reversion model | [[ornstein-uhlenbeck]] half-life (≈ 2–20 days) |
| Hedge ratio | OLS or dynamic [[kalman-filter-trading\|Kalman filter]] |
| "Borrow cost" analogue | Perp [[funding-rate]] carry on the short legs |
| Return skew | Negative — many small wins, sharp deleveraging losses |
| Crowding risk | **High** (capacity is shared, not per-fund) |
| Canonical disaster | Correlated liquidation deleveraging (2022-05, 2024-08-05, 2025-10-10) |

## Edge source

Primarily **analytical**, secondarily **behavioral / risk-bearing** (see [[edge-taxonomy]]):

- **Analytical** — the edge comes from modeling skill: identifying genuinely cointegrated crypto relationships (not just BTC-beta co-movement), estimating hedge ratios and reversion speeds correctly, and separating temporary divergence from a structural break (unlock, delisting, migration). Most participants run correlation, not [[cointegration]], and mistake shared BTC-beta for a tradeable spread.
- **Behavioral / risk-bearing** — divergences are created by flow insensitive to relative value: exchange listings, token unlocks, narrative rotations (capital fleeing L1s for memecoins), and single-coin liquidation flushes. The book sells liquidity to that flow and is paid for warehousing convergence risk.

## Why this edge exists

Related crypto assets — two L1s competing for TVL, a token and its liquid-staking derivative, a coin and its factor basket, an asset and its perp — are tied by fundamentals, but their short-term order flow is not synchronized. When a large uninformed order hits one leg (a listing pump, an unlock dump, a headline overreaction), its price temporarily detaches from its statistical twin.

**Who is on the other side:** liquidity-demanding traders who must transact *now* (forced sellers, momentum chasers, liquidation engines) and discretionary traders who evaluate each coin on its own narrative rather than relative to its cointegrated peers. They "lose" the spread because they are paying for immediacy or trading a single-name story; the stat-arb trader prices the relationship.

The edge persists, in attenuated form, because warehousing convergence risk is genuinely unpleasant: spreads widen violently before converging (the classic "picking up nickels in front of a steamroller"), and the strategy suffers correlated losses exactly when leveraged peers deleverage. Crypto's version of the **August 2007 quant quake** is a mass liquidation cascade (2022-05 LUNA, 2024-08-05 yen-carry unwind, 2025-10-10) — when crowded reversion books all hold similar inventory and one forced unwind moves every spread at once. The equity evidence sets the base rate: Gatev, Goetzmann & Rouwenhorst (2006) documented ~11%/yr excess returns for simple pairs over 1962–2002 with clear decay in later sub-periods; Avellaneda & Lee (2010) found similar decay in PCA-based stat arb after ~2002–2007. Crypto edges are larger but noisier and decay faster.

### Variants of crypto stat arb

| Variant | Construction | Primary edge | Capacity per signal | Infrastructure |
|---|---|---|---|---|
| [[pairs-trading]] | One cointegrated coin pair, z-score entry | Analytical | Smallest | Modest (klines, Python) |
| Sector basket | Long cheap / short rich within L1s, LSDs, DeFi, or memes | Analytical | Medium | Moderate (basket construction) |
| BTC-factor residual | Trade residuals after removing BTC (and ETH) beta from each coin | Analytical | Medium-large | Heavy (factor model) |
| PCA / cross-sectional | Reversion of residuals vs principal components of the alt universe (Avellaneda-Lee style) | Analytical | Medium-large | Heavy |
| HFT cross-venue | Microsecond CEX-vs-DEX / cross-exchange | Latency ([[edge-taxonomy]]) | Tiny per signal | Extreme (co-location) |

All but the HFT row rely on the same analytical edge; the daily/hourly forms are the focus of this page.

## Null hypothesis

If prices follow independent random walks, no linear combination of two coins is stationary and any "spread" is itself a random walk: z-score entries at ±2 are followed by divergence as often as convergence, and P&L equals the negative of fees plus funding carry. The null is directly testable — cointegration tests (Engle-Granger, Johansen) should *fail* at the 5% level, and a backtest on **shuffled/randomly matched** crypto tickers should produce zero gross alpha. A real edge requires (a) in-sample cointegration that (b) survives out-of-sample, and (c) reversion fast enough (half-life of days to weeks) to beat funding carry and cost drag. The crypto-specific trap: shared BTC-beta makes almost any two majors look cointegrated, so the null must be tested against **BTC-neutralized residuals**, not raw prices.

## Rules

**Pair / basket selection:**
- Universe: liquid coins with an economic reason to co-move (same sector, derivative vs underlying, coin vs its factor basket). Exclude thin alt perps you cannot exit.
- Test for **cointegration**, not correlation: Engle-Granger or Johansen, p < 0.05 on 60–180 days of 1h/1d data.
- Require an [[ornstein-uhlenbeck]] spread half-life of ~2–20 days; discard slower relationships (funding carry eats them).
- Re-test **weekly**; drop pairs/baskets that fail. Crypto relationships decay faster than equities.

**Entry:**
- Compute the spread `S = P_A − β·P_B` (static regression or dynamic [[kalman-filter-trading|Kalman filter]]), or the residual of each coin vs its BTC-factor fit.
- Rolling z-score of S (60-bar window). z ≥ +2.0: short A, long β·B (dollar-neutral). z ≤ −2.0: long A, short β·B.

**Exit:**
- Take profit when z reverts to ±0.5 or crosses 0.
- **Stop-loss:** exit if |z| ≥ 3.0–3.5 (structural break, not noise), or if the pair fails its weekly cointegration re-test, or after 2× the estimated half-life with no convergence.

**Position sizing:**
- Risk ≤ 0.5–1% of equity per spread; 15–40 spreads concurrently for diversification.
- Cap gross leverage (2–4×). Higher leverage is what turns a correlated-deleveraging drawdown into a wipeout — the recurring lesson of every crypto cascade.

## Implementation pseudocode

```python
for spread in universe_spreads:                    # pairs or BTC-factor residuals
    # weekly re-qualification (crypto decays fast)
    if engle_granger_pvalue(spread, lookback_days=90) > 0.05:
        retire(spread); continue
    beta      = kalman_hedge_ratio(spread)         # or OLS on 90d
    s         = spread.A - beta * spread.B
    half_life = ou_half_life(s)
    if not (2 <= half_life <= 20):                 # days
        retire(spread); continue

    z = (s[-1] - mean(s[-60:])) / std(s[-60:])

    if no_position(spread):
        if z >= 2.0:  open(short=spread.A, long=beta*spread.B, risk=0.005*equity)
        if z <= -2.0: open(long=spread.A,  short=beta*spread.B, risk=0.005*equity)
    else:
        if abs(z) <= 0.5:                    close(spread)   # converged
        elif abs(z) >= 3.0:                  close(spread)   # structural-break stop
        elif failed_retest(spread):          close(spread)   # cointegration broke
        elif days_held(spread) > 2*half_life: close(spread)  # time stop
```

## Indicators / data used

- 1h/1d OHLCV for the full universe, clean and corporate-action-free (in crypto: token migrations, rebases, redenominations must be handled explicitly).
- Cointegration tests: Engle-Granger, Johansen; spread z-score; [[ornstein-uhlenbeck]] half-life.
- Dynamic hedge ratio via [[kalman-filter-trading|Kalman filter]] or rolling regression.
- For basket variants: a BTC/ETH factor model (and sector dummies) to build long/short portfolios and neutralize systematic exposure.
- **Perp [[funding-rate]]** on every short leg — the crypto analogue of stock borrow cost; persistently expensive shorts kill a spread outright.
- **[[open-interest]]** and **[[volatility]]/[[regime-detection]]** — to avoid entering spreads into a `vol_shock` regime where correlated deleveraging dominates.
- Python (statsmodels, pandas, scikit-learn) for research; production execution typically async REST/WebSocket against CEX and perp-DEX venues.

## Example trade

Two large-cap L1 tokens test as cointegrated on 1h data (Engle-Granger p = 0.02, β = 0.9, OU half-life ≈ 5 days) after neutralizing BTC-beta. Coin A rallies on a listing announcement while coin B drifts; the residual z-score hits +2.3. The trader shorts $25,000 of A-perp and longs $22,500 of B-perp (dollar-neutral). Over the next four days the listing flow fades and the residual reverts to z = +0.4; both legs close for a +1.3% gain on gross exposure (~$1,300 on the $50k spread) before costs — roughly +0.9% after four-fill taker fees, slippage, and a small adverse funding differential on the short leg. Had A instead announced a genuine ecosystem catalyst and the residual pushed through +3.0, the stop would have cut the trade for roughly −1%.

## Performance characteristics

Realistic, cost-corrected expectations (illustrative magnitudes, not a backtest of this exact spec):

- **Realistic modern expectation** for a daily/hourly, non-HFT crypto book: net Sharpe ~0.4–0.8 (frontmatter assumes 0.6), mid-single-to-low-double-digit annual returns at modest leverage — lower and noisier than the equity literature because crypto cointegration is less stable and costs are higher.
- **Cost overlay matters enormously**: the strategy trades often, holds a long and a short (four fills per completed spread), and earns small per-trade edges.
- **Return profile**: many small wins, occasional sharp losses when relationships break (negative skew); losses cluster during liquidation-deleveraging episodes.
- Expected max drawdown for a diversified, modestly levered book: ~15–20%; leveraged books saw far worse in every crypto cascade.

**Cost-aware reality check.** Stat arb is the clearest case where cost is the *binding constraint*:

| Cost component | Magnitude | Why it bites crypto stat arb hard |
|---|---|---|
| Taker fees, both legs, entry + exit | ~16–22 bps | Four fills per completed spread |
| Slippage | ~4–25 bps | Loose alt legs are thin during divergence windows |
| Funding carry (short legs) | ±1–4 bps/day | Crypto's "borrow"; a persistently positive-funding short bleeds |
| Gross edge per converged trade | ~80–200 bps | Costs consume 20–40% |
| Breakeven (frontmatter) | ~30 bps | Edge must clear this *before* funding carry |
| Net result | Sharpe ~0.4–0.8 at modest leverage | Faster decay than equities narrows the margin |

The arithmetic is unforgiving: a high-turnover book earning small per-trade edges only survives with tightly controlled execution and short-leg funding. This is why retail-scale crypto stat arb is marginal and why breadth, maker execution, and infrastructure matter.

## Capacity limits

Daily/hourly crypto stat arb scales meaningfully only on the liquid majors and their baskets; the *edge per dollar* shrinks fast because every desk trades the same obvious relationships. A single mid-frequency book targeting the numbers above is realistically capped around **$30M** before its own entries/exits move the spreads it trades; the loose sector/alt spreads that carry the most edge absorb the least size. [[high-frequency-trading|HFT]] crypto stat arb variants (CEX-vs-DEX, cross-exchange) have far smaller capacity per signal and require co-location. Crowding risk is **high** — capacity is shared across all players in the trade, not per-fund, and a peer's deleveraging widens your spreads.

## What kills this strategy

- **Structural breaks** — an unlock, delisting, migration, hack, or narrative death permanently breaks the cointegrating relationship; the spread never comes back (the largest single source of pair-level losses in crypto).
- **Crowding / deleveraging spirals** — when a large peer unwinds, all crowded spreads widen together (the crypto cascade analogue of Aug 2007); stops then force selling into the widening.
- **BTC-dominance regime shifts** — reversion speeds lengthen and whole sectors decouple in alt-seasons or flights to BTC, turning a 5-day trade into a multi-week carry bleed.
- **Funding recalls / short squeezes** on the short leg — persistently expensive-to-short coins bleed the spread.
- **Overfitting** — data-mining thousands of coin pairs guarantees spurious in-sample cointegration; see [[overfitting-detection]].
- **Cost creep** — widening alt spreads, rising adverse funding, or compressing volatility pushing the gross edge below the ~30 bps breakeven.

| Failure mode | Mechanism | Early warning | Defense |
|---|---|---|---|
| Structural break | Unlock/delisting/migration breaks cointegration | Spread blows past stop, fails re-test | \|z\| ≥ 3 stop + weekly cointegration re-test |
| Crowding / deleverage | Peer unwinds; all crowded spreads widen (cascades) | Sector-wide spread widening, vol_shock regime | Lower gross leverage; diversify spread sources |
| Reversion-speed regime shift | Half-lives lengthen in trending/rotation markets | Realized half-life > 2× modeled | Time stop at 2× half-life; halt if persistent |
| Funding recall / squeeze | Short leg funding turns expensive | Rising funding on short leg | Pre-screen funding; cap costly-to-short coins |
| Overfitting | Data-mining thousands of pairs | In-sample only, fails OOS | [[overfitting-detection]]; OOS validation, multiple-testing correction |
| Cost creep | Gross edge falls below breakeven | Net Sharpe trending to 0 | Monitor net-of-cost edge per trade |

## Kill criteria

- Strategy-level drawdown > 15% from high-water mark → halve gross; > 20% → flat and full review.
- Rolling 12-month net Sharpe < 0 → stop new entries, wind down.
- Fraction of spreads failing weekly cointegration re-test > 40% for 2 consecutive weeks → universe is broken, halt.
- Average realized half-life > 2× modeled over a 60-trade sample → reversion regime changed, halt.
- Any single spread: |z| ≥ 3.0, cointegration p > 0.05 on re-test, or 2× half-life time stop → close it (per Rules).

See [[when-to-retire-a-strategy]].

## Advantages

- Market-neutral: returns largely uncorrelated with BTC direction, attractive in a portfolio context.
- High trade frequency gives statistical significance quickly — you learn fast whether the edge is real.
- Fully systematic and backtestable; minimal discretionary judgment at execution time.
- Decades of academic documentation (rare for a trading strategy) and a well-understood failure history to learn from.

## Disadvantages

- Edge is thin and crowded on the obvious crypto relationships and fragile (structural breaks) on the loose ones.
- Negative skew: steady small gains punctuated by sharp correlated losses during deleveraging cascades.
- Requires shorting: funding carry, recalls, and squeeze risk on the short legs.
- Statistically demanding — correlation/cointegration confusion (the BTC-beta trap) and multiple-testing bias produce convincing but fake backtests.
- Infrastructure- and data-intensive relative to the net returns available at retail scale.

## Cointegration vs correlation

A common and expensive mistake is confusing correlation with cointegration. Two coins can be highly correlated (they move together, usually because both are BTC-beta) without being cointegrated (their spread is not mean-reverting). Statistical arbitrage requires **cointegration** — the linear combination (spread) reverts to a stable mean even as prices wander. Engle-Granger and Johansen are the standard tests. See [[pairs-trading]] for implementation.

| Property | Correlation | [[cointegration]] |
|---|---|---|
| What it measures | Co-movement of *returns* | Stationarity of a *price combination* |
| Spread mean-reverts? | Not guaranteed | Yes (the definition) |
| Tradeable signal? | No — two BTC-beta coins can be 0.9 correlated and drift apart forever | Yes — spread pulls back to its mean |
| Test | Pearson / rolling corr | Engle-Granger, Johansen |
| Crypto failure if confused | Spread trends instead of reverting — the BTC-beta trap | — |

Only a passing cointegration test (and one that *survives out-of-sample* — see [[overfitting-detection]]) justifies a position.

## Basket approaches

Beyond simple pairs, institutional stat arb trades **baskets** — long a portfolio of undervalued coins, short a portfolio of overvalued coins, based on factor models. In crypto the dominant factor is BTC-beta; sector factors (L1, DeFi, LSD, meme) and momentum/reversion signals build the residuals. Diversifying across many spreads reduces idiosyncratic risk and smooths returns. The Avellaneda & Lee (2010) PCA/ETF-residual formulation maps directly onto trading coin residuals versus principal components of the alt universe.

## High-frequency stat arb

At the highest frequencies, crypto stat arb exploits sub-second mispricings across venues — CEX vs perp-DEX, cross-exchange, a coin vs its perp. These require co-located servers, ultra-low-latency execution, and [[market-microstructure]] models. It is a different business from the daily/hourly version above: latency edge ([[edge-taxonomy]]) rather than analytical edge, with tiny per-signal capacity.

## Sources

- Gatev, E., Goetzmann, W., & Rouwenhorst, K. G. (2006). "Pairs Trading: Performance of a Relative-Value Arbitrage Rule." *Review of Financial Studies*, 19(3) — the canonical academic study (decaying ~11%/yr excess returns); the base rate crypto edges are measured against.
- Khandani, A., & Lo, A. (2007/2011). "What Happened to the Quants in August 2007?" — the crowding/deleveraging failure mode, whose crypto analogue is the liquidation cascade.
- Avellaneda, M., & Lee, J.-H. (2010). "Statistical Arbitrage in the US Equities Market." *Quantitative Finance*, 10(7) — the PCA/residual formulation that generalizes to crypto factor baskets.
- Vidyamurthy, G. (2004). *Pairs Trading: Quantitative Methods and Analysis*. Wiley.
- Chan, E. P. (2013). *Algorithmic Trading: Winning Strategies and Their Rationale*. Wiley — practical cointegration/Kalman implementations directly usable on crypto spreads.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000` — OHLCV per coin for spread / residual construction
- `GET /api/v1/hyperliquid/candles?coin=SOL&interval=1h&limit=1000` — broad alt-perp OHLCV for basket construction
- `GET /api/v1/derivatives/funding-rates?coin=ETH` — per-leg funding (the short-leg "borrow cost")
- `GET /api/v1/volatility/regime` — vol regime gate to avoid entering into deleveraging

**Historical data:**
- `GET /api/v1/backtesting/klines` — full OHLCV archive for cointegration + residual backtests
- `GET /api/v1/backtesting/funding` — funding history for the carry overlay
- `GET /api/v1/quant/history` — point-in-time regime probabilities for leak-free basket gating

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-data/klines?symbol=ETHUSDT&interval=1h&limit=1000"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]].

## Related

- [[pairs-trading]] — the simplest two-asset instance
- [[cointegration]] — the required statistical property (not correlation)
- [[ornstein-uhlenbeck]] — the mean-reversion model for half-life
- [[kalman-filter-trading]] — dynamic hedge-ratio estimation
- [[mean-reversion]] — the parent family
- [[funding-rate-arbitrage]] — the perp-vs-spot basis trade and short-leg funding mechanics
- [[arbitrage]] — the broader relative-value category
- [[quantitative-trading]] — methodology context
- [[edge-taxonomy]] — analytical / latency edge classification
- [[overfitting-detection]] — defense against spurious cointegration
- [[high-frequency-trading]] — the latency-edge variant
- [[market-microstructure]] — order-flow context for HFT variants
