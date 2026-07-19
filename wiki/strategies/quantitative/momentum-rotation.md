---
title: "Momentum Rotation"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [momentum, crypto, quantitative, cross-sectional, portfolio-rotation, factor-investing, altcoins]
aliases: ["Cross-Sectional Crypto Momentum", "Crypto Momentum Rotation", "Altcoin Rotation", "Relative-Strength Rotation"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced

backtest_status: cost-corrected

# Edge characterization (see [[edge-taxonomy]])
edge_source: [behavioral, structural]
edge_mechanism: "Crypto narratives (L1 seasons, memecoin manias, sector rotations) draw reflexive retail flow that underreacts then chases, so recent relative winners keep winning for weeks. You buy the top cross-sectional performers and are paid by late trend-chasers who provide exit liquidity — until the reflexive flow reverses and momentum crashes."

# Data and infrastructure requirements
data_required: [ohlcv-daily, market-cap-ranking, realized-volatility, btc-200dma, spot-liquidity, funding-rates]
min_capital_usd: 10000
capacity_usd: 30000000
crowding_risk: medium

# Performance expectations (net of turnover fees, spread, and slippage — the crux for altcoins)
expected_sharpe: 0.8
expected_max_drawdown: 0.45
breakeven_cost_bps: 35

# Decay history
decay_evidence: "Academic crypto cross-sectional momentum (Liu, Tsyvinski & Wu 2022, and the weekly-momentum literature) documents a real premium, but the effect concentrates in small/illiquid alts where round-trip cost is 60-150 bps — so most of the gross spread is eaten by turnover. As perp liquidity deepened and quant desks entered 2023-2025, the optimal formation window shortened (multi-month → 1-4 week) and the net-of-cost edge on liquid majors compressed toward zero."

# Lifecycle (only if deployed — see [[live-journal]])
kill_criteria: |
  - long-short momentum spread (net of modelled costs) < 0 over trailing 6 months
  - realized round-trip cost > modelled gross spread on the traded universe
  - drawdown > 30% on the sleeve (momentum-crash guard)
  - BTC below 200-day MA AND crash filter fails to de-risk (execution/gap failure)
  - top-decile turnover persistently churns without follow-through (win rate < 45% for 60 days)

related: ["[[sentiment-trading]]", "[[momentum]]", "[[trend-following]]", "[[factor-investing]]", "[[mean-reversion]]", "[[volatility-targeting]]", "[[momentum-crashes]]", "[[funding-rate]]", "[[short-term-reversal]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Momentum Rotation

Cross-sectional momentum rotation ranks a liquid universe of crypto assets by recent **relative** performance and rotates capital into the top performers (optionally shorting the bottom), rebalancing on a fixed cadence. It is the crypto adaptation of the Jegadeesh-Titman (1993) cross-sectional momentum effect, confirmed for digital assets by Liu, Tsyvinski & Wu (2022). The crypto-specific twists are decisive: the effective formation window is **much shorter** (1-4 weeks, not 12 months), returns must be measured **relative to the crypto market** to strip out pervasive BTC beta, and **turnover costs on altcoins are the single factor that decides whether the strategy makes money** — which is why this page is written at `cost-corrected` status rather than presenting a naive gross backtest.

## Edge source

Mapping to [[edge-taxonomy]]:

- **Behavioural (primary).** Crypto is narrative-driven and reflexive. When a sector catches a bid (an L1 season, a memecoin mania, an AI-token wave), retail *underreacts* early then *chases* late, extending the trend past fundamentals. Buying recent relative winners captures the continuation; the late chasers who buy the top provide the exit liquidity.
- **Structural (secondary).** Flow rotates in identifiable regimes — capital migrates from BTC to ETH to large-cap alts to small-cap alts as risk appetite rises ("the alt-season conveyor"). This rotation is a semi-mechanical flow structure a cross-sectional ranker can position ahead of the crowd on.

The strategy claims no informational, analytical, or latency edge. It is a pure behavioural/flow premium — and a *negatively skewed* one: the same reflexivity that extends trends produces violent [[momentum-crashes]] when sentiment reverses and yesterday's small-cap winners collapse fastest.

## Why this edge exists

1. **Underreaction then overreaction.** Retail digests new narratives slowly (underreaction → early trend) then piles in via social feedback (overreaction → late trend). Momentum harvests the middle of that arc.
2. **Attention and reflexivity.** Price *is* the marketing in crypto — a coin going up recruits buyers, who push it up further. Recent relative strength is a genuine leading indicator of continued attention flow.
3. **Segmented, slow capital.** Much crypto capital is retail and slow to reallocate across the long tail of alts, so relative winners stay winners longer than an efficient market would allow.
4. **Narrative conveyor.** Rotations (BTC → ETH → majors → small caps) recur across cycles; a ranker that follows relative strength rides the conveyor from segment to segment.

Liu, Tsyvinski & Wu (2022) formalise the size and momentum factors in crypto; the weekly-momentum literature shows the premium concentrates at shorter horizons than equities — consistent with crypto's faster reflexive loop.

## Null hypothesis

If crypto returns are a cross-sectional random walk (no continuation):

- Past relative winners would be as likely to underperform as outperform next period; the top-decile-minus-bottom-decile spread would be zero.
- Shortening or lengthening the formation window would not change the (zero) spread.
- Any apparent gross spread would vanish entirely after realistic altcoin turnover costs.
- The strategy's Sharpe would be indistinguishable from equal-weight buy-and-hold of the universe.

The null is *rejected on gross returns* — crypto cross-sectional momentum has a real, documented premium at 1-4 week horizons — but is *nearly accepted net of costs on illiquid alts*, where 60-150 bps round-trip turnover eats most of the spread. The live question is not "does momentum exist in crypto" (it does) but "does it survive *your* execution costs on *your* universe." If the net long-short spread is below zero over a trailing 6 months, the answer is no and the strategy pauses.

## Rules

### Universe

1. **Liquidity-screened top 20-40 by market cap**, excluding stablecoins and wrapped assets, requiring **> $50M/day** spot volume and a spread tight enough to keep round-trip cost under the breakeven budget. Illiquid micro-caps are *excluded* precisely because their turnover cost destroys the edge, however tempting the gross spread.

### Ranking (entry signal)

2. **Formation window: trailing 4 weeks, skipping the most recent 3 days** to sidestep [[short-term-reversal]]. (Longer 12-week and shorter 1-week variants are valid; 4-week/skip-3d is the robust default for liquid crypto.)
3. **De-mean vs the market.** Rank on return *relative to the equal-weighted (or BTC) universe return*, not raw return — otherwise the "momentum" portfolio is just a leveraged BTC-beta bet.
4. **Portfolio construction:** buy the **top quintile** (top ~20%), inverse-volatility weighted so high-vol names get smaller allocations. Long-short variant: also short the bottom quintile (only if borrow/perp-short is available and cheap).

### Exit / rebalance

5. **Rebalance weekly.** Crypto momentum decays faster than equities; monthly is too slow, daily churns too much cost. Weekly is the cost-vs-signal sweet spot.
6. **Rotation exit:** an asset is sold when it drops out of the top quintile at rebalance.
7. **Crash filter (critical):** if **BTC closes below its 200-day MA**, cut gross exposure by 50% (or move fully to cash/stables). This is the primary [[momentum-crashes]] guard — momentum's worst drawdowns cluster at bear-regime onset.
8. **Drawdown throttle:** if sleeve drawdown > 20%, halve position sizes systematically.

### Sizing

- **Inverse-volatility weights** within the top quintile (60-day realised vol) to equalise risk contribution.
- **Per-name cap 15%** of the sleeve so one alt cannot dominate.
- **No leverage on the long book** by default (crypto vol is already high); long-short runs at ≤ 1x gross per side.

## Implementation pseudocode

```python
# momentum_rotation.py — weekly cross-sectional crypto rotation
import numpy as np

FORMATION_D   = 28     # 4-week formation
SKIP_D        = 3      # skip most-recent 3 days (short-term reversal)
TOP_QUINTILE  = 0.20
MIN_ADV_USD   = 50e6   # liquidity screen
PER_NAME_CAP  = 0.15
VOL_WINDOW_D  = 60

def cross_sectional_scores(px, adv):
    # px: dict{sym -> daily close series}; adv: dict{sym -> avg daily $volume}
    universe = [s for s in px if adv[s] >= MIN_ADV_USD]
    rets = {}
    for s in universe:
        p = px[s]
        rets[s] = p[-SKIP_D-1] / p[-FORMATION_D-SKIP_D-1] - 1   # skip-adjusted formation return
    mkt = np.mean(list(rets.values()))                          # equal-weight market return
    return {s: rets[s] - mkt for s in universe}                 # de-meaned (beta-stripped) momentum

def target_weights(scores, vol, btc_below_200dma):
    ranked = sorted(scores, key=scores.get, reverse=True)
    n_top = max(1, int(len(ranked) * TOP_QUINTILE))
    longs = ranked[:n_top]
    inv_vol = {s: 1.0 / max(vol[s], 1e-6) for s in longs}
    z = sum(inv_vol.values())
    w = {s: min(inv_vol[s] / z, PER_NAME_CAP) for s in longs}
    gross = 0.5 if btc_below_200dma else 1.0                    # crash filter halves exposure
    return {s: w[s] * gross for s in w}

def weekly_rebalance(px, adv, vol, btc_series, book):
    if book["drawdown"] > 0.20:
        return {"action": "THROTTLE", "scale": 0.5}
    btc_below = btc_series[-1] < np.mean(btc_series[-200:])
    scores = cross_sectional_scores(px, adv)
    w = target_weights(scores, vol, btc_below)
    return {"action": "REBALANCE", "target_weights": w,
            "note": "cash 50%+" if btc_below else "fully invested"}
```

The production system adds: cost-aware rebalancing (skip a swap if the name is a marginal top-quintile member and the turnover cost exceeds its expected edge), borrow/perp-short availability checks for the short leg, and per-rebalance realised-cost logging feeding the kill criteria.

## Indicators / data used

- **Daily OHLCV** — the formation-window return and rebalance prices; the core ranking input.
- **Market-cap ranking + $ volume** — the liquidity screen that defines the tradable universe (and excludes cost-destroying micro-caps).
- **Realised volatility (60-day)** — inverse-vol position weighting.
- **BTC 200-day MA** — the crash filter / regime gate.
- **Spot liquidity / spread depth** — per-name round-trip cost estimation (decides inclusion).
- **[[funding-rate]]** — for the long-short variant's short leg (perp short cost) and as a crowding backdrop.

## Example trade

**Setup (2026-05-04, weekly rebalance, universe = top 30 liquid coins):**

- Compute 4-week/skip-3d returns, de-meaned vs the equal-weight market. Top quintile (6 names) by relative momentum: SOL (+34% rel), a leading L1 (+28%), an AI-sector token (+26%), a DeFi large-cap (+19%), an L2 (+17%), a majors laggard turned leader (+14%).
- Inverse-vol weight: SOL (vol 70%) gets ~11%; the DeFi large-cap (vol 45%) gets ~17%; capped at 15% per name.
- **Crash filter:** BTC above its 200-day MA → fully invested.

**Execution:** rotate the sleeve into the six names, inverse-vol weighted. Round-trip cost this rebalance: majors ~10-15 bps, the smaller L2/AI names ~30-50 bps; blended ~22 bps on the turned-over portion (~40% of book) ≈ **~9 bps drag on total book**.

**Next rebalance (2026-05-11):** the AI token and the L2 have dropped out of the top quintile (relative momentum faded); they are sold and replaced by two new entrants. Turnover ~35%. The retained names (SOL, the L1, the DeFi large-cap) continued higher, contributing ~+4% each over the week.

**Result:** book +2.3% for the week gross; ~9 bps rebalance cost → **+2.2% net**. The trade *worked because it stayed in liquid names* — the identical strategy run on the illiquid long tail would have shown a higher gross return and a *negative* net after 80-120 bps round-trip costs churned every week.

## Performance characteristics

Cost-corrected picture (the naive gross numbers are materially higher and misleading):

| Metric | Value | Note |
|---|---|---|
| Net CAGR (liquid universe, long-only) | 15-30% | Highly regime-dependent; concentrated in alt-seasons. |
| Sharpe (net) | ~0.6-0.9 | Long-only; long-short ~0.8-1.1 gross but costs bite harder. |
| Max drawdown | 40-45% | Momentum crashes at bear-regime onset dominate. |
| Weekly turnover | 25-45% | The cost driver; every point of turnover is fee + spread + slippage. |
| Win rate (per name held) | 45-55% | Winners run further than losers fall — positive skew per name, negative skew per regime. |
| Breakeven cost budget | ~35 bps round-trip | Above this on the traded universe, the net edge is negative. |

**Realistic cost overlay (never assume naive — this is the whole story):**
- **Turnover fees:** ~5 bps/side CEX taker × 25-45% weekly turnover; annualised this is a large, relentless drag.
- **Spread:** 5-15 bps on liquid majors; **50-150 bps on small/illiquid alts** — the reason the universe is liquidity-screened.
- **Slippage:** grows with size and shrinks with liquidity; a rebalance that moves a thin book pays the impact twice (in and out).
- **Short-leg cost:** perp funding on shorts plus borrow — often makes the long-short variant *worse* net than long-only despite higher gross Sharpe.
- **Momentum-crash tail:** a single regime reversal can erase a year of accumulated momentum premium; this is not a cost you can net out, it is the risk you are paid to bear.

A gross backtest on the full universe including micro-caps can show a 2.0+ Sharpe that is entirely an artefact of ignoring 100 bps round-trip costs; realistic net Sharpe on a tradable liquid universe is ~0.6-0.9.

## Capacity limits

Bounded by the **liquidity of the traded universe** and **weekly turnover**. On the liquid top-20-40, an operator can run roughly **$1-30M** before rebalance impact on the smaller names in the basket starts eating the edge. Scaling further forces you either up into only the most liquid majors (where the net momentum edge is thinnest) or down into illiquid alts (where cost destroys it) — a genuine capacity wall. This is a satellite-to-mid-size strategy, not a mega-fund book; the frontmatter `capacity_usd` reflects the practical ceiling for a liquid-universe implementation.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Momentum crashes (#6).** The signature tail: at a sharp regime reversal, past losers surge and past winners (often small-cap, high-beta) collapse, inflicting violent drawdowns exactly when the book is most concentrated in extended names. The equity "quant quake" (Aug 2007) and March 2009 have direct crypto analogues at every cycle top.
2. **Turnover costs (#2/#4).** The quiet killer: even a real gross edge dies if weekly turnover on illiquid names costs more than the spread it captures. This is why the strategy lives or dies on the liquidity screen.
3. **Regime change / beta collapse (#5).** In a broad bear market *everything* falls together, cross-sectional dispersion collapses, and there are no relative winners to rotate into — the crash filter must move to cash.
4. **Crowding (#4).** As quant desks run the same signal, the premium on liquid majors compresses and the formation window shortens; a static 12-month window (equity-style) badly underperforms in crypto.
5. **Beta illusion.** Without de-meaning vs the market, the "momentum" book is just a leveraged BTC bet that looks great in a bull market and blows up in a drawdown — a specification error, not a real edge.
6. **Universe/liquidity shifts.** A name that was liquid at entry can gap illiquid in stress, trapping the exit at the worst moment.

## Kill criteria

Pause the sleeve on any of:

1. **Net long-short (or long-only vs equal-weight) momentum spread < 0** over a trailing 6 months.
2. **Realised round-trip cost > modelled gross spread** on the traded universe (turnover is winning).
3. **Drawdown > 30%** on the sleeve.
4. **BTC below its 200-day MA and the crash filter fails to de-risk** (an execution/gap failure that let the momentum crash through).
5. **Top-decile churn without follow-through** — per-name win rate < 45% for 60 days (the continuation the strategy depends on has stopped).

Re-deploy when cross-sectional dispersion returns, BTC reclaims its 200-day MA, and a fresh out-of-sample window shows the net spread positive on the liquid universe. See [[when-to-retire-a-strategy]].

## Instrument Structures

Momentum rotation deploys primarily on **baskets**, with a single-asset mode during BTC-dominance-rising regimes.

| Structure | Role in this strategy |
|-----------|----------------------|
| **Basket** | The primary deployment. The strategy buys the top momentum quintile (a long basket of relative winners) and sells the bottom quintile (a short basket of relative losers) within a sector. The basket structure provides diversification across the momentum signal, reducing single-name blow-up risk. Sector baskets from the [[hyperliquid-baskets-overview|basket library]] (e.g., [[l1-blockchains-basket]], [[defi-bluechip-basket]], [[ai-tokens-basket]]) serve as the deployment vehicles. |
| Single-asset | Reduced role. When BTC dominance is rising ([[alt-season-momentum-gate]] fails), the strategy shifts to BTC-only or ETH-only positioning — single-asset — rather than cross-sectional baskets. |
| Pair | Not the base form, but a natural extension: within-sector top-vs-bottom pairs from the basket ranking are the atomic units of [[cross-sectional-relative-value]], which is the market-neutral version of the same momentum signal. |
| Cross-venue | Not deployed. |

The basket structure changes the mechanics: position sizing is per-basket-notional (not per-coin), rebalancing is weekly across the basket, and the edge is the *average* momentum premium across N coins rather than a single-name bet. This distributes the unavoidable momentum-crash risk (when the factor reverses, all positions in the basket are simultaneously wrong) but does not eliminate it.

## Advantages

- **Documented factor** — cross-sectional momentum is one of the most robust anomalies, confirmed for crypto (Liu, Tsyvinski & Wu 2022).
- **Systematic and rules-based** — removes discretion; every decision is a ranking and a rebalance.
- **Rides crypto's strongest behavioural feature** — narrative/attention reflexivity is the market's defining dynamic.
- **Diversifies a book** — its winners are what other strategies (mean-reversion, sentiment contrarian) are fading; low correlation to those sleeves.
- **Regime-aware by construction** — the 200-day-MA crash filter is a simple, effective drawdown guard.

## Disadvantages

- **Negatively skewed** — steady gains punctuated by violent momentum crashes; the tail dominates the risk.
- **Turnover-cost sensitive** — the entire net edge can be eaten by spread and slippage on the wrong universe.
- **Beta-contamination risk** — mis-specified (raw instead of de-meaned) it becomes a hidden BTC-beta bet.
- **High realised drawdowns** — 40-45% is normal, larger at cycle turns.
- **Needs a liquid, dispersed universe** — thin in flat/low-dispersion regimes.
- **Crowding decay** — the liquid-majors premium is compressing as quant capital arrives.
- **Infrastructure-heavy** — reliable ranking, liquidity screening, cost-aware rebalancing, and regime gating are all required.

## Sources

- Jegadeesh & Titman (1993), *Returns to Buying Winners and Selling Losers* — the foundational cross-sectional momentum result the crypto version adapts.
- Liu, Tsyvinski & Wu (2022), *Common Risk Factors in Cryptocurrency*, Journal of Finance — documents size and momentum factors in crypto; the primary crypto-specific evidence.
- Weekly-momentum crypto literature — shows the premium concentrates at 1-4 week formation horizons, shorter than equities, consistent with crypto's faster reflexive loop.
- Daniel & Moskowitz, *Momentum Crashes* (2016) — the canonical treatment of momentum's negative skew and regime-onset drawdowns; the basis for the crash filter.
- [[momentum-crashes]] — the failure-mode page this strategy's tail risk draws from.
- [[factor-investing]] — the broader factor context.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/coins/top?limit=50` — top coins by market cap (universe construction)
- `GET /api/v1/market-data/klines?symbol=SOLUSDT&interval=1d&limit=60` — daily OHLCV per name (formation return + realised vol)
- `GET /api/v1/market-data/btc-price-history?days=365` — BTC price + 200-day MA (crash filter)
- `GET /api/v1/market-health/altcoin-breadth?ma=200` — % of coins above MA (dispersion / regime context)
- `GET /api/v1/liquidity/depth` — per-coin depth/spread at 10/25/50/100 bps (cost screen)

**Historical data:**
- `GET /api/v1/backtesting/klines?symbol=SOLUSDT&interval=1d` — full OHLCV archive for the ranking backtest
- `GET /api/v1/backtesting/symbols` — backtest-available universe
- `GET /api/v1/quant/timeline` — daily market-regime labels (2019-now) for regime-conditioned backtests

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/coins/top?limit=50"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-market-data]], [[cryptodataapi-coins]].

## Related

- [[momentum]] / [[trend-following]] — the parent factor and its time-series cousin.
- [[factor-investing]] — the broader factor framework.
- [[short-term-reversal]] — the effect the skip-3-days rule avoids.
- [[momentum-crashes]] — the dominant tail risk and reason for the crash filter.
- [[volatility-targeting]] — the inverse-vol weighting principle.
- [[mean-reversion]] — the opposing behaviour; a natural diversifier to this sleeve.
- [[sentiment-trading]] — sentiment momentum that often correlates with price momentum.
- [[funding-rate]] — the short-leg cost input for the long-short variant.
- [[edge-taxonomy]] — where this strategy sits among the six edge categories.
- [[failure-modes]] / [[when-to-retire-a-strategy]] — kill-criteria methodology.
