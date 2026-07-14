---
title: "Sentiment Trading"
type: strategy
created: 2026-04-06
updated: 2026-07-14
status: good
tags: [sentiment, crypto, fear-greed, funding-rate, social, contrarian, momentum, quantitative, on-chain, behavioral-finance]
aliases: ["Crypto Sentiment Strategy", "Fear and Greed Trading", "Social Sentiment Trading", "Sentiment Composite"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: intermediate

backtest_status: naive-backtested

# Edge characterization (see [[edge-taxonomy]])
edge_source: [behavioral, informational]
edge_mechanism: "Crypto is retail-dominated and reflexive; crowd fear and greed overshoot fundamentals. At extremes the marginal price-setter is an emotional forced buyer/seller, so a systematic contrarian who buys measured extreme fear and trims extreme greed is paid by the herd's loss aversion. The informational sliver is aggregating dispersed sentiment (fear-greed, funding, social, flows) faster than the crowd internalises it."

# Data and infrastructure requirements
data_required: [fear-greed-index, funding-rates, exchange-flows, stablecoin-dry-powder, social-sentiment, spot-price]
min_capital_usd: 2000
capacity_usd: 50000000
crowding_risk: medium

# Performance expectations (net of fees, funding, and slippage)
expected_sharpe: 0.7
expected_max_drawdown: 0.35
breakeven_cost_bps: 25

# Decay history
decay_evidence: "The crypto Fear & Greed Index is public and free (Alternative.me since 2018), so its contrarian signal is widely watched and partly arbitraged — extreme-fear bounces have become faster and shallower. Sentiment also stayed pinned in 'extreme fear' for most of 2022's bear market (12+ consecutive weeks), during which naive contrarian buyers were repeatedly run over — the clearest evidence that the raw signal is regime-dependent, not a standalone edge."

# Lifecycle (only if deployed — see [[live-journal]])
kill_criteria: |
  - composite signal's forward 30-day hit rate < 50% over a trailing 20 signals (out of sample)
  - rolling 6-month P&L < 0
  - drawdown > 25% on the sleeve
  - social-sentiment inputs shown to be bot/manipulation-driven (source integrity failure)
  - extreme-fear buys stop mean-reverting for 60+ days (bear-regime lock-in)

related: ["[[momentum-rotation]]", "[[funding-rate]]", "[[funding-rate-arbitrage]]", "[[fear-and-greed-index]]", "[[regime-detection]]", "[[mean-reversion]]", "[[liquidation-cascade-fade]]", "[[exchange-netflow]]", "[[behavioral-finance]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[cryptodataapi]]"]
---

# Sentiment Trading

Crypto sentiment trading aggregates public emotion-and-positioning signals — the crypto **Fear & Greed Index**, perpetual **funding rates**, **exchange flows**, **stablecoin dry powder**, and **social** mention/polarity — into a single composite score, then trades it either **contrarian at extremes** (buy measured extreme fear, trim extreme greed) or **momentum in the mid-range** (ride accelerating sentiment). It formalises the behavioural insight that crypto is a retail-dominated, reflexive market where crowd fear and greed overshoot fundamentals. The honest framing: the raw Fear & Greed signal is public, free, and heavily watched, so on its own it is close to arbitraged out — the edge, such as it remains, is in *disciplined confirmation, position sizing, and regime filtering*, not in the index reading itself.

## Edge source

Mapping to [[edge-taxonomy]]:

- **Behavioural (primary).** At sentiment extremes the marginal price-setter is emotional: a capitulating forced seller in extreme fear, a FOMO chaser in extreme greed. A systematic operator who ignores recency bias and trades the statistics is paid by the crowd's loss aversion and herding. This is the same panic-premium logic as [[liquidation-cascade-fade]], measured over days rather than seconds.
- **Informational (secondary, weak).** Aggregating dispersed inputs (funding, flows, dry powder, social velocity) into a composite *faster and more completely* than the average participant is a mild informational edge. It is weak precisely because the headline Fear & Greed component is public — the alpha is in the harder-to-assemble sub-signals (on-chain flows, funding term structure, bot-filtered social).

The strategy claims no structural, analytical, or latency edge. It is a behavioural mean-reversion/momentum bet with a heavy dependence on *regime* — which is why the null hypothesis and kill criteria below are strict.

## Why this edge exists

1. **Retail dominance and reflexivity.** Crypto's participant base skews retail and leveraged; narratives and social feedback loops amplify moves past fundamentals. Overshoots in both directions are structural to a reflexive, 24/7, high-leverage market.
2. **Positioning is observable.** Funding rates directly measure crowd leverage (crowded longs pay, crowded shorts get paid) — a positioning tell that traditional markets lack. Extreme positive funding at a greed peak is the crowd max-long into a top.
3. **Dry powder and flows lead price.** Rising stablecoin reserves on exchanges (dry powder) and net outflows of BTC/ETH (accumulation) are slow-moving, partly-informed flows that the sentiment composite front-runs the crowd on.
4. **Fear persists but eventually snaps.** Extreme fear is *usually* mean-reverting on a weeks horizon — but not always (see 2022). The edge exists in the *conditional* distribution, and its fragility is the whole game.

## Null hypothesis

Under an efficient market where sentiment is already priced:

- Forward 30-day returns conditional on Fear & Greed < 20 would equal the unconditional mean — extreme fear would predict nothing.
- Funding extremes would not precede mean reversion; crowded-long funding peaks would be as likely to keep rising as to reverse.
- Adding social/flow inputs to the composite would not improve forward hit rate over trading price alone.
- The composite's Sharpe would be indistinguishable from buy-and-hold after costs.

The record *partially* rejects the null — historically, entering BTC on confirmed extreme-fear turns has produced positive forward 30-day returns more often than not, and greed peaks have preceded drawdowns — but the null is *not* rejected in bear regimes: sentiment sat in "extreme fear" for 12+ consecutive weeks in 2022 while price kept falling, exactly the null-world behaviour. If the composite's out-of-sample forward hit rate falls below 50% over a trailing 20 signals, treat the edge as absent and pause.

## Rules

### Composite construction

1. Normalise each input to 0-100 (0 = extreme bearish, 100 = extreme bullish):
   - **Fear & Greed Index** — 30% weight.
   - **Funding rate** (8h, cross-exchange; high positive = crowded long = bearish tilt) — 25% weight.
   - **Exchange net flows** (net outflows = accumulation = bullish) — 20% weight.
   - **Stablecoin dry powder** (rising reserves = bullish) — 15% weight.
   - **Social sentiment** (bot-filtered mention polarity + velocity) — 10% weight.
2. Composite = weighted average. Regimes: 0-20 extreme fear, 20-40 fear, 40-60 neutral, 60-80 greed, 80-100 extreme greed.

### Contrarian rules (extremes)

1. **Buy:** composite < 20 **and turning up** (do not catch the falling knife — wait for the score to bottom and tick higher for 2 consecutive readings). Scale in: 50% at first up-turn, 50% on a hold above the low.
2. **Trim/short:** composite > 80 **and rolling over**. Reduce exposure or initiate a modest short; extreme greed with extreme positive funding is the highest-conviction trim.
3. **Regime gate (critical):** only take contrarian *longs* when BTC is **above its 200-day MA** or the market-health/quant regime is not "established bear." This single filter is what separates this strategy from the 2022 wipeout.

### Momentum rules (mid-range)

1. **Buy:** composite crosses **above 50 from below** with social velocity accelerating **and** price above its 20-day MA.
2. **Exit:** composite crosses back below 50, or social velocity peaks and declines.

### Funding sub-rule (crypto-specific)

- **Bearish tilt** when 8h funding > 0.05% (crowded longs; overlaps with [[funding-rate-arbitrage]] territory).
- **Bullish tilt** when 8h funding < −0.03% (crowded shorts; squeeze potential).

### Sizing

- **1-3% of sleeve per signal**, scaled by how extreme the composite is (more extreme = larger, capped at 3%).
- **Max 3 concurrent** correlated positions; BTC and ETH sentiment usually move together — treat as one.
- **Hard stop −8%** on contrarian longs (fear can deepen); time-stop 30 days.

## Implementation pseudocode

```python
# sentiment_trading.py — composite sentiment decision loop
WEIGHTS = {"fear_greed": 0.30, "funding": 0.25, "flows": 0.20,
           "dry_powder": 0.15, "social": 0.10}
EXTREME_FEAR, EXTREME_GREED = 20, 80
STOP_PCT, TIME_STOP_D = 0.08, 30
PER_SIGNAL_PCT_MAX = 0.03

def composite(sig):
    return sum(WEIGHTS[k] * getattr(sig, k) for k in WEIGHTS)  # each 0-100

def turning_up(hist):    # last 2 readings rising off a low
    return len(hist) >= 3 and hist[-1] > hist[-2] > hist[-3]

def turning_down(hist):
    return len(hist) >= 3 and hist[-1] < hist[-2] < hist[-3]

def decide(sig, hist, book):
    s = composite(sig)
    hist.append(s)
    bull_regime = sig.btc_above_200dma and sig.quant_regime != "established_bear"

    pos = book["positions"].get(sig.asset)
    if pos is not None:
        if sig.mark <= pos["stop"] or book["days_held"] >= TIME_STOP_D:
            return {"action": "EXIT", "reason": "stop/time"}
        if s >= EXTREME_GREED and turning_down(hist):
            return {"action": "TRIM", "reason": "extreme greed rolling over"}
        return {"action": "HOLD"}

    # ---- contrarian long ----
    if s < EXTREME_FEAR and turning_up(hist) and bull_regime:
        size = min(PER_SIGNAL_PCT_MAX, (EXTREME_FEAR - s) / 100 + 0.01)
        return {"action": "BUY", "size_pct": size,
                "stop": sig.mark * (1 - STOP_PCT), "reason": "extreme fear turn"}

    # ---- contrarian trim / short ----
    if s > EXTREME_GREED and turning_down(hist):
        return {"action": "REDUCE_OR_SHORT", "reason": "extreme greed peak"}

    # ---- momentum (mid-range) ----
    if 48 <= s <= 55 and s > hist[-2] and sig.social_velocity_up and sig.price_above_20dma:
        return {"action": "BUY", "size_pct": 0.015, "reason": "sentiment momentum > 50"}

    return {"action": "WAIT", "reason": f"composite {s:.0f}, no trigger"}
```

The production system adds: a bot/manipulation filter on social inputs, the 200-day-MA + quant-regime gate wired in as a hard veto, and per-signal forward-hit-rate logging for the kill criteria.

## Indicators / data used

- **Crypto [[fear-and-greed-index|Fear & Greed Index]]** — headline behavioural gauge (public; the weakest standalone but a useful anchor).
- **[[funding-rate]] (8h, cross-exchange)** — direct crowd-leverage/positioning measure; the strongest crypto-specific input.
- **Exchange net flows** — BTC/ETH inflows (distribution/selling) vs outflows (accumulation).
- **Stablecoin dry powder** — CEX stablecoin reserves and a dry-powder z-score (accumulating/neutral/depleting).
- **Social sentiment** — bot-filtered mention polarity and velocity (LunarCrush/Santiment-style); low weight due to manipulation risk.
- **Regime overlays** — BTC 200-day MA, market-health score, quant regime — the veto that prevents bear-market contrarian wipeouts.
- **Spot price + 20-day MA** — momentum confirmation.

## Example trade

**Setup (2026-06-15, BTC, contrarian):**

- BTC fell from $70,000 to $55,000 over two weeks. Inputs: Fear & Greed **12**; 8h funding **−0.04%** (shorts crowded); exchange **outflows +$800M/48h** (accumulation); stablecoin dry powder z-score **+1.3** (accumulating); social sentiment **18/100**. Composite = 0.30·12 + 0.25·(funding→82 bullish) + 0.20·(flows→75) + 0.15·(dry powder→70) + 0.10·18 ≈ **~48** on positioning but Fear & Greed pins the *emotional* read at extreme fear — the divergence (extreme fear + bullish positioning) is the classic high-conviction setup.
- **Regime gate:** BTC still above its 200-day MA (~$52,000); quant regime "bottoming," not "established bear." Gate passes.

**Entry:** composite score bottoms and ticks up two readings. Buy BTC at $56,500 (50% of a 3% sleeve allocation). On a hold above $55,000 the next day, add the remaining 50% at $55,200. Fees ~5 bps/side; slippage ~2 bps on BTC.

**Management:** BTC recovers to $64,000 by early July, composite reaches 55 (neutral) — trim half for +$8,500 on 0.5 BTC. At $68,000 the composite hits 72 (greed) and rolls over — exit the rest.

**Result:** ~+$12,800 gross on the position; costs (fees + slippage on entry/exit) ~$60; **net ~$12,740**. The trade worked *because the regime gate confirmed a bottoming market* — the identical signal in mid-2022 (fear extreme, but "established bear," BTC below 200d MA) would have been vetoed, avoiding the repeated stop-outs that destroyed naive contrarians that year.

## Performance characteristics

Honest, cost-corrected picture:

| Metric | Value | Note |
|---|---|---|
| Forward 30-day hit rate (extreme-fear buys, regime-gated) | 60-70% | Falls to ~50% without the regime gate. |
| Avg winner | +12-20% | On confirmed extreme-fear turns in bull/bottoming regimes. |
| Avg loser | −5 to −8% | Hard stop plus fear-deepening slippage. |
| Sharpe (net) | ~0.7 | Regime-dependent; collapses in bear lock-ins. |
| Max drawdown | 25-35% | Concentrated in bear regimes where fear persists. |
| Signal frequency | ~4-10 extreme signals/yr | Low; long dry spells between setups. |
| Breakeven cost budget | ~25 bps round-trip | Fees + slippage; funding if leveraged. |

**Realistic cost overlay (never assume naive):**
- **Fees:** ~5 bps/side CEX spot taker; less with maker quoting.
- **Slippage:** ~2 bps on BTC/ETH; 20-60 bps on smaller alts (avoid sentiment-trading illiquid coins).
- **Funding:** if the contrarian long is expressed on a perp, negative funding at a fear extreme *pays* you, but a leveraged greed-peak short pays funding — net it.
- **Overfitting drag:** with 5 inputs and free weights it is trivial to fit weights to history; forward hit rate typically lands 10-20 points below the fitted backtest. Assume the live edge is materially smaller than any in-sample number.
- **Lag:** the composite confirms *after* part of the move — entering on the turn (not the extreme) sacrifices the first leg for reliability.

## Capacity limits

Sentiment trades BTC/ETH and large caps on a swing horizon, so capacity is comfortable — roughly **$5-50M** before entries move price on the majors, since positions are built over hours-to-days rather than in a single sweep. Capacity shrinks fast on smaller alts (thin books, wide spreads make the slippage overlay dominate). The binding constraint is signal *frequency*, not size: with only a handful of extreme signals per year, the strategy is capital-underutilised and works best as one sleeve in a multi-strategy book.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Regime lock-in (#5).** The canonical killer: in a genuine bear market, sentiment stays pinned at extreme fear for months (2022) and every contrarian buy is run over. The 200-day-MA/quant-regime gate mitigates but cannot fully eliminate this.
2. **Crowding / signal commoditisation (#4).** The Fear & Greed Index is free and universally watched; its bounces have grown faster and shallower as everyone front-runs the same reading.
3. **Garbage social data (#6).** Crypto social is saturated with bots, paid shills, and coordinated pumps. Un-filtered social inputs produce false extremes and can be deliberately manipulated against you.
4. **Lagging-indicator trap (#6).** By the time the composite registers "extreme," the move has largely happened; the reading can mark either the bottom or merely the start of a deeper leg.
5. **Overfitting (#3).** Dozens of possible inputs and weights make in-sample optimisation easy and forward failure likely; the fitted Sharpe rarely survives out of sample.
6. **Low frequency.** Few signals per year means small samples, slow feedback, and high sensitivity to a single bad regime call.

## Kill criteria

Pause the sleeve on any of:

1. **Composite forward 30-day hit rate < 50%** over a trailing 20 signals (out of sample).
2. **Rolling 6-month P&L < 0.**
3. **Drawdown > 25%** on the sleeve.
4. **Social inputs demonstrably bot/manipulation-driven** (source-integrity audit fails) — drop or down-weight social to zero.
5. **Extreme-fear buys stop mean-reverting for 60+ days** — bear-regime lock-in confirmed; stand aside until BTC reclaims its 200-day MA.

Re-deploy when the regime gate flips constructive and a fresh out-of-sample window shows the composite predicting again. See [[when-to-retire-a-strategy]].

## Advantages

- **Quantifies crowd emotion** — turns subjective "the market feels fearful" into a tradable, logged signal.
- **Crypto-native positioning data** — funding rates give a direct long/short crowding read unavailable in traditional markets.
- **Multi-source redundancy** — if social is noisy, funding + flows + dry powder can still confirm.
- **Behavioural backing** — measured contrarian entries at confirmed extremes have real empirical support in crypto's reflexive market.
- **Flexible** — contrarian at extremes, momentum in the mid-range; adapts to regime.
- **Low capital minimum** — works at a few thousand dollars.

## Disadvantages

- **"Sentiment can stay extreme longer than you can stay solvent."** Bear-regime fear lock-ins are the dominant failure.
- **Manipulable social layer** — bots and coordinated campaigns can manufacture false readings.
- **Lagging** — confirms after the move begins; sacrifices the first leg for reliability.
- **Overfitting-prone** — many inputs, free weights; forward edge is smaller than any backtest.
- **Low signal frequency** — few high-conviction setups per year; capital-underutilised alone.
- **Regime-gate dependence** — the strategy is only as good as its bear-market veto; get the regime wrong and it is a wipeout.

## Sources

- Alternative.me crypto Fear & Greed Index (since 2018) — the headline behavioural gauge; see [[fear-and-greed-index]].
- BIS Working Papers No 1087, *Crypto carry* — Schmeling, Schrimpf, Todorov (2023). Funding as a positioning/crowding measure. https://www.bis.org/publ/work1087.pdf
- 2022 bear market record — 12+ consecutive weeks pinned in "extreme fear" while price fell; the canonical evidence that raw sentiment contrarianism is regime-dependent (see [[terra-luna-collapse]], [[ftx]]).
- LunarCrush / Santiment methodology — social mention/polarity/velocity construction and the bot-contamination problem.
- [[behavioral-finance]] — loss aversion, herding, and recency bias; the theoretical basis for the panic/greed premium.
- [[liquidation-cascade-fade]] — the same panic-premium logic on a seconds horizon.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/sentiment/fear-greed` — crypto Fear & Greed index (markdown format option)
- `GET /api/v1/derivatives/funding-rates?coin=BTC` — cross-exchange funding (crowd-leverage input)
- `GET /api/v1/on-chain/exchange-flows/BTC` — CEX inflow/outflow (accumulation vs distribution)
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — dry-powder z-score (accumulating/neutral/depleting)
- `GET /api/v1/market-health/summary` — dual-score + sentiment band (regime gate)

**Historical data:**
- `GET /api/v1/market-intelligence/fear-greed-history` — Fear & Greed timeseries (backtest)
- `GET /api/v1/sentiment/stablecoins/remote-history?days=365` — daily stablecoin/dry-powder history
- `GET /api/v1/market-health/history?days=730` — historical market-health scores for regime gating
- `GET /api/v1/backtesting/klines?symbol=BTCUSDT&interval=1d` — BTC price + 200-day MA construction

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/sentiment/fear-greed"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-sentiment]], [[cryptodataapi-on-chain]].

## Related

- [[funding-rate]] / [[funding-rate-arbitrage]] — the positioning/crowding input and an adjacent funding-based strategy.
- [[fear-and-greed-index]] — the headline sentiment gauge.
- [[momentum-rotation]] — price momentum that often correlates with sentiment momentum.
- [[mean-reversion]] — the market behaviour contrarian sentiment exploits.
- [[liquidation-cascade-fade]] — the same panic premium on a much shorter horizon.
- [[regime-detection]] — the market-regime models that gate contrarian entries.
- [[exchange-netflow]] — exchange-flow and dry-powder inputs.
- [[behavioral-finance]] — loss aversion and herding, the source of the edge.
- [[edge-taxonomy]] — where this strategy sits among the six edge categories.
- [[failure-modes]] / [[when-to-retire-a-strategy]] — kill-criteria methodology.
