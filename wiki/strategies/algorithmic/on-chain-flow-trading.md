---
title: "On-Chain Flow Trading"
type: strategy
created: 2026-06-03
updated: 2026-10-17
status: excellent
tags: [crypto, bitcoin, ethereum, quantitative, market-regime, algorithmic]
aliases: ["On-Chain Flow Trading", "Exchange Flow Trading", "On-Chain Signal Trading"]
strategy_type: quantitative
timeframe: swing
markets: [crypto]
complexity: advanced
backtest_status: naive-backtested
edge_source: [informational, behavioral]
edge_mechanism: "Aggregate on-chain flows (exchange in/outflows, stablecoin balances, dormancy, whale wallets) lead price because they reveal supply hitting/leaving exchanges and large-holder intent before it prints on the tape; the edge is reading that leakage before slower participants price it in."
data_required: [exchange-netflow, stablecoin-exchange-balances, sopr-dormancy, whale-wallet-deltas, ohlcv-daily]
min_capital_usd: 5000
capacity_usd: 50000000
crowding_risk: medium
expected_sharpe: null   # no reliable public Sharpe exists; see Performance characteristics
expected_max_drawdown: 0.20
breakeven_cost_bps: 30
decay_evidence: "On-chain signals were stronger pre-2020; the spot-ETF era (2024+) routes large flows through custodians/ETFs that are partly off the classic exchange-flow radar, weakening some signals. No reliable published Sharpe."
related: ["[[on-chain-regime]]", "[[crypto-market-regime-taxonomy]]", "[[on-chain-analysis]]", "[[whale-trade]]", "[[on-chain-smart-money-tracking]]", "[[institutional-flow-regime]]", "[[point-in-time-data]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]", "[[hyperliquid]]", "[[cryptodataapi]]"]
gates:
  - id: btc_eth_perps
    role: universe
    rule: "Trade BTC and ETH only, expressed on perps (typically Hyperliquid)"
    runnable: true
    endpoint: /api/v1/hyperliquid/prices
    field: prices.{coin}
  - id: netflow_z
    role: entry
    rule: "Netflow leg: z-score of exchange net flow against its own trailing 90-180 day distribution; an inflow spike is bearish, sustained outflow bullish"
    runnable: partial
    endpoint: /api/v1/on-chain/exchange-flows/{coin}/history?start={start}
    field: points[].net_24h
    replay: /api/v1/on-chain/exchange-flows/{coin}/history?start={start}&end={end}
    replay_field: points[].net_24h
    note: "Net flow over our tracked CEX wallets in native coin units, one point per hour, archived as captured since 2026-05-28 (so point-in-time by construction, but under 180 days deep). Max 93 days per call: page for a 90-day window. Coverage is our wallet set, not a vendor's full label set (Coinbase BTC wallets, for one, are not tracked); spike_zscore_24h on /on-chain/exchange-flows/{coin} is a served live z."
  - id: stablecoin_dry_powder
    role: entry
    rule: "Dry-powder leg: high and rising stablecoin balances on exchanges arm a long setup (arm, don't fire)"
    runnable: partial
    endpoint: /api/v1/on-chain/stablecoin-reserves/dry-powder
    field: zscore
    note: "zscore is today's exchange stablecoin balance against its 30-day mean and stdev, not the page's 90-180 day window. No SSR is served."
  - id: dormancy_cdd
    role: entry
    rule: "Dormancy leg: rising coin days destroyed (old coins moving) is a distribution warning: reduce or short"
    runnable: false
    note: "CDD and dormancy are not served; /on-chain/dormancy/btc carries MVRV, active addresses and issuance despite its name. Needs Glassnode or CryptoQuant."
  - id: whale_accumulation
    role: entry
    rule: "Whale leg: large wallets growing with no matching exchange deposits is bullish"
    runnable: false
    note: "On-chain whale wallet cohorts are not served (the whale_accumulation component of /on-chain/score is disabled). /quant/whales covers Hyperliquid perp positioning, a different population."
  - id: mvrv_elevated
    role: entry
    rule: "MVRV elevated while coins move: profit-taking into strength, caution and trim"
    runnable: partial
    endpoint: /api/v1/on-chain/dormancy/btc
    field: metrics.mvrv
    note: "BTC only. metrics.mvrv can be null for a day while the source's newest day is incomplete (the source publishes MVRV a day late); keep the last non-null value. The page gives no level for elevated, and its z-score leg needs your own logged series, since no MVRV history is served; mvrv_signal.zone is the served band."
  - id: sopr_elevated
    role: entry
    rule: "SOPR elevated while coins move: profit-taking into strength, caution and trim"
    runnable: false
    note: "SOPR is not served. Needs Glassnode or CryptoQuant."
  - id: health_score
    role: entry
    rule: "Composite health_score = 0.30 netflow + 0.15 stables + 0.20 dormancy + 0.25 whales + 0.10 SOPR (signed z-scores), clipped to -1..+1"
    runnable: false
    input: derived
    inputs: [netflow_z, stablecoin_dry_powder, dormancy_cdd, whale_accumulation, mvrv_elevated, sopr_elevated]
    note: "The dormancy and whale legs and the SOPR half of the last leg are not served (MVRV is). onchain_composite is the served substitute, with different legs and weights."
  - id: onchain_composite
    role: filter
    rule: "Read the served on-chain composite alongside the market regime before acting"
    runnable: partial
    endpoint: /api/v1/on-chain/score
    field: score
    note: "From the page's AI-agent workflow. A 0-100 score built from hash ribbon, stablecoin dry powder, exchange flow (stablecoins only), miner flow and MVRV when present, renormalised over the legs with data; not the page's health_score. Bands: bullish 70+, leaning_bullish 55-69, neutral 45-54, leaning_bearish 30-44, bearish below 30."
  - id: price_confirms
    role: filter
    rule: "Price action confirms the signal direction (do not fight a strong opposing trend; for a long, price has stopped making lower lows)"
    runnable: partial
    endpoint: /api/v1/hyperliquid/candles?coin={coin}&interval=1d&limit=60
    field: candles[].low
    replay: /api/v1/backtesting/klines?symbol={coin}&exchange=hyperliquid&interval=1d&start={start}
    replay_field: klines[].l
    note: "The page does not define the confirmation test or a strong trend; comparing recent swing lows (or highs, for a short) on daily bars is one reading."
  - id: entry_band
    role: entry
    rule: "Open a new position only when the absolute health_score exceeds the entry band and price confirms"
    runnable: false
    input: derived
    inputs: [health_score, price_confirms]
    note: "Only as runnable as health_score; the page also leaves the band level open."
  - id: dry_powder_fires
    role: entry
    rule: "Dry powder arms a long but it fires only with a confirming exchange outflow (or whale accumulation)"
    runnable: partial
    input: derived
    inputs: [stablecoin_dry_powder, netflow_z]
    note: "The outflow confirmation is served; the whale alternative is not."
  - id: regime_agrees
    role: filter
    rule: "Act only when the market regime agrees with the flow direction"
    runnable: partial
    endpoint: /api/v1/quant/market
    field: regime.label
    replay: /api/v1/quant/history?scope=market&start={start}
    replay_field: entries[].regime_label
    note: "From the page's AI-agent workflow. Which labels agree with a long or short is the desk's mapping; strong_trend_bull and strong_trend_bear are the clear ones."
  - id: spike_watch
    role: entry
    rule: "Large single transfers to exchanges (at least $1M) as the real-time whale-deposit trigger"
    runnable: partial
    endpoint: /api/v1/on-chain/exchange-flows/spike-alerts?symbol={coin}&direction=inflow
    field: alerts[].amount_usd
    note: "From the page's AI-agent workflow, which gives no rule for acting on one. source balance_delta can be an exchange's own hot-cold rebalancing. History since 2026-10-08 is the exchange_flow_spikes type on /backtesting/snapshots."
  - id: vol_scaled_size
    role: sizing
    rule: "Size the perp proportional to health_score and inverse to 20-day realised vol, up to 2-5% of book risk at full conviction"
    runnable: false
    input: derived
    inputs: [health_score]
    note: "Only as runnable as health_score. The vol leg alone is served: 20 daily closes from /hyperliquid/candles."
  - id: leverage_cap
    role: sizing
    rule: "Perp leverage at most 3x"
    runnable: true
    input: position
  - id: exit_neutral_band
    role: exit
    rule: "Exit when health_score mean-reverts inside the neutral band or flips sign"
    runnable: false
    input: derived
    inputs: [health_score]
    note: "Only as runnable as health_score."
  - id: time_stop
    role: exit
    rule: "Stand down if the thesis has not played out within about 4-8 weeks"
    runnable: partial
    input: position
    note: "The page gives a 4-8 week range; pick one horizon."
  - id: risk_stop
    role: stop
    rule: "A fixed-percentage adverse move closes the position regardless of score"
    runnable: partial
    input: position
    endpoint: /api/v1/hyperliquid/prices
    field: prices.{coin}
    note: "The page does not give the percentage."
  - id: kill_90d_loss
    role: stop
    rule: "Flatten and review when rolling 90-day PnL falls below -15% of allocated capital"
    runnable: true
    input: position
---

# On-Chain Flow Trading

**On-Chain Flow Trading** is a systematic, *directional* strategy on crypto majors (BTC and ETH) that uses aggregate on-chain flow metrics — exchange net in/outflows, stablecoin dry powder, coin dormancy and spent-output behaviour, and whale-wallet accumulation — as *leading* signals to bias and size a directional position, typically expressed on perpetual futures via [[hyperliquid]]. It is the trading layer that sits on top of basket 7 (On-Chain Intelligence) in the wiki's [[crypto-market-regime-taxonomy|14-basket crypto regime taxonomy]] and the [[on-chain-regime]] concept.

> **Disambiguation.** This page is **not** [[on-chain-smart-money-tracking]]. That strategy copies the entries of specific high-PnL *individual wallets* into *memecoins/low-caps* on Solana — a scalp-timeframe, wallet-level, micro-cap craft. **This** page is the opposite: aggregate, basket-level, *macro* reading of the whole chain's flow plumbing to take a directional swing position on BTC/ETH. The two share the word "on-chain" and nothing else — different data, horizon, instruments, and capacity.

## At a Glance

| Attribute | Value |
|---|---|
| **Type** | Systematic directional swing overlay (BTC/ETH) |
| **Edge source** | Informational (ledger leaks supply/intent) + behavioral (whale persistence) |
| **Core data** | Exchange netflow, stablecoin exchange balances, SOPR/CDD/dormancy, whale-wallet deltas |
| **Instrument** | BTC/ETH perps, typically via [[hyperliquid]], ≤ 3× leverage |
| **Lead time** | Weeks (few independent bets per year) |
| **Capacity** | High (~$50M) — deepest crypto instruments |
| **Crowding risk** | Medium — same dashboards watched by everyone |
| **Critical discipline** | **Point-in-time** label snapshots; out-of-sample validation |
| **Biggest risk** | Label revision / look-ahead bias; ETF-era flow migration |

This is the macro, basket-level member of the [[on-chain-analysis|on-chain analytics]] family; contrast with the wallet-level [[on-chain-smart-money-tracking]].

## Edge source

**Informational + behavioural** (see [[edge-taxonomy]]).

- *Informational:* The blockchain is an immutable, public ledger. Large supply movements — coins leaving cold storage *toward* an exchange, stablecoins being parked *on* an exchange, old coins waking up — are visible on-chain before the resulting buy/sell pressure prints on the tape. The edge is reading that leakage and acting before slower participants price it in.
- *Behavioural:* Large holders ("whales") and long-term holders move in slow, persistent patterns (accumulation, distribution, capitulation) driven by conviction and cost basis, not noise. Those patterns are partially observable on-chain and tend to lead price by weeks because the crowd reacts to lagging price/indicator signals instead.

## Why this edge exists

Three things keep a slower counterparty on the other side:

1. **Retail reads lagging indicators.** The marginal retail participant trades off price, moving averages, RSI, and headlines — all of which *follow* the supply that is already moving on-chain. A coin sitting in an exchange hot wallet is supply that *can* be sold; the retail trader only sees it once the sell prints.
2. **The ledger leaks intent before execution.** Exchange *inflows* of BTC/ETH frequently precede selling — holders move coins to an exchange in order to sell them. Conversely, sustained *outflows* into self-custody signal holders removing supply from the sell-side order book (a long bias). This is a structural information asymmetry favouring whoever watches the chain.
3. **Stablecoin balances reveal dry powder.** Stablecoins parked on exchanges are pre-positioned buying power. A large, rising stablecoin balance on exchanges is fuel that has not yet been deployed — a setup, not a trigger. Slower participants only see the demand once it lifts the book.

The edge survives only while interpretation of these flows remains *heterogeneous and partly off-the-radar*. As discussed below, the spot-ETF era has migrated a chunk of large flow off classic exchange wallets, and the most-watched dashboards have crowded the obvious reads.

## Null hypothesis

Under the null of **no edge**, on-chain flows are *coincident noise*: net-flow spikes correlate with volatility but carry no forward information, and any apparent predictive power is an artefact of overlapping windows or of fitting exchange-wallet labels to past price.

Two specific traps make the null easy to falsely reject:

- **Label revision / look-ahead.** Vendors continuously *re-label* which addresses belong to which exchange, and they backfill those labels into history. A "netflow" series downloaded today is not the series you would have seen in real time. Any backtest must use **[[point-in-time-data]]** snapshots of the label set, or it silently imports future knowledge.
- **In-sample overfitting of thresholds.** "Inflow > X σ → short" thresholds tuned on history will look great in-sample. Require genuine **out-of-sample / walk-forward** validation before believing any signal.

If the strategy cannot beat a price-only momentum baseline out-of-sample on point-in-time data, the on-chain layer is adding noise, not edge.

## Rules

Signals are combined into a single composite **on-chain health score** (-1 distribution → +1 accumulation) that *biases and sizes* a perp position; no single metric trades alone.

### Directional signals

| Signal | Reading | Bias |
|--------|---------|------|
| Exchange **net-inflow** spike (BTC/ETH onto exchanges) | Supply moving to sell-side | **Short / reduce long** |
| Exchange **net-outflow** / self-custody migration | Supply leaving sell-side | **Long** |
| High & rising **stablecoin exchange balances** (dry powder, low SSR) | Buying power pre-positioned | **Long setup** (arm, don't fire) |
| Rising **dormancy / CDD** — old coins moving | Long-term holders distributing | **Distribution warning → reduce / short** |
| Silent **whale accumulation** (large wallets growing, no exchange deposits) | Conviction buying off-book | **Long** (see [[whale-trade]]) |
| Elevated **SOPR / MVRV** with coins moving | Profit-taking into strength | **Caution / trim** |

### Composite gating and entry

1. Compute each sub-signal as a z-score vs its own trailing distribution (e.g. 90–180d).
2. Combine into `health_score` (weighted, clipped to [-1, +1]).
3. **Gate, don't chase:** only take a *new* directional position when `|health_score|` exceeds an entry band **and** price action confirms direction (avoid fighting a strong opposing trend). Stablecoin dry powder *arms* a long but requires a confirming outflow or whale-accumulation signal to *fire*.
4. Size the perp position proportional to `health_score` and inverse to recent realised vol.

### Exit / flip

- Exit when `health_score` mean-reverts back inside the neutral band, or flips sign.
- Hard time-stop: on-chain signals lead by **weeks**; if the thesis has not played out in ~4–8 weeks, the signal is stale — stand down.
- Risk stop independent of signal: fixed % adverse move closes the position regardless of score.

### Position sizing

- Risk a fixed fraction of book per unit of `health_score` (e.g. up to 2–5% of book at full conviction).
- Cap perp leverage low (≤ 3×) — this is a swing thesis, not a basis carry.
- Daily/weekly loss budget halts new entries.

## Implementation pseudocode

```python
# Point-in-time joins are MANDATORY: use the exchange-label set as it existed
# at each historical timestamp, never today's revised labels.

def health_score(t):
    z = {}
    z["netflow"]   = -zscore(exchange_netflow(t, pit=True))      # inflow -> negative (bearish)
    z["stables"]   =  zscore(stablecoin_exch_balance(t, pit=True))  # dry powder -> bullish setup
    z["dormancy"]  = -zscore(coin_days_destroyed(t, pit=True))   # old coins moving -> bearish
    z["whales"]    =  zscore(whale_wallet_delta(t, pit=True))    # accumulation -> bullish
    z["sopr"]      = -zscore_above_one(sopr(t, pit=True))        # heavy profit-taking -> bearish

    w = {"netflow":0.30, "stables":0.15, "dormancy":0.20,
         "whales":0.25, "sopr":0.10}
    raw = sum(w[k] * z[k] for k in w)
    return clip(raw, -1.0, 1.0)

def target_position(t, book):
    s = health_score(t)
    if abs(s) < ENTRY_BAND:
        return 0.0                       # neutral -> flat
    if not price_confirms(sign(s), t):   # don't fight a strong opposing trend
        return 0.0
    vol = realised_vol(t, window=20)
    return book * RISK_FRAC * s / vol    # signed, vol-scaled perp notional

# rebalance daily on a Hyperliquid perp; honour loss budget + time-stop
```

The sketch is illustrative — production code must handle PIT label snapshots, vendor outages, perp funding cost, and slippage on [[hyperliquid]].

## Indicators / data used

See [[on-chain-analysis]] for the mechanics of each metric.

- **Exchange netflow** and **exchange reserves** (BTC/ETH on aggregated exchange wallets).
- **Stablecoin exchange balances** and the **Stablecoin Supply Ratio (SSR)** — dry-powder proxies.
- **SOPR**, **Coin Days Destroyed (CDD)** / **dormancy**, and **MVRV** — holder profit/loss and spending behaviour.
- **Whale wallet deltas** — growth/decline of large-balance cohorts (see [[whale-trade]]).
- **OHLCV daily** — for the price-confirmation gate and vol scaling.

Data vendors (forward links): [[glassnode]], [[cryptoquant]], [[nansen]]. Vendor choice matters because each defines exchange labels and metrics slightly differently.

## Example trade

*Illustrative, not a real historical trade.*

Over two weeks, exchange BTC reserves fall steadily (sustained net-outflow), the whale cohort balance grows with no matching exchange deposits, stablecoin exchange balances sit elevated, and CDD stays quiet (long-term holders not spending). The composite `health_score` rises to +0.6 and price has stopped making lower lows — the confirmation gate opens.

The trader opens a long BTC perp on [[hyperliquid]] at ~3% of book risk, 2× leverage. Over the following 5 weeks price grinds higher; the position is trimmed as `health_score` decays toward the neutral band and exited when a fresh inflow spike pushes the score negative. Across many such signals the *aggregate* expectancy — not this single instance — is what matters; on-chain leads are noisy and several signals will whipsaw.

## Performance characteristics

Be honest: there is **no reliable, generalisable public Sharpe** for this strategy.

- Signals are **leading but noisy** — useful lead time is measured in **weeks, not days**, which means few independent bets per year and high variance in any short sample.
- Much published "proof" is **vendor marketing or survivorship-biased social content**, not statistically rigorous, point-in-time backtesting.
- The **spot-ETF era (2024+)** has weakened several classic signals (see decay below): large institutional flow increasingly moves through custodians/ETF authorised participants that do not register as ordinary exchange wallet flows.
- Realistic expectation: a **regime-bias overlay** that modestly improves a directional book, not a high-Sharpe standalone alpha. Treat it as a quantitative scaffold for discretionary conviction, validated out-of-sample.
- **Conservative planning numbers** (matching frontmatter): expect maximum drawdowns in the **15–20% range** — the kill criteria flatten the book at -15% rolling 90-day, so realised peak-to-trough can slightly exceed the trigger. Cost overlay is light: BTC/ETH perp taker fees, funding, and slippage total a few bps per leg; with multi-week holds targeting multi-percent moves the strategy can absorb roughly **30 bps round-trip** before the edge breaks even.

## Capacity limits

Capacity is **materially higher than memecoin/wallet strategies** because it trades the deepest crypto instruments — BTC/ETH perps on venues like [[hyperliquid]] — where swing-sized positions clear without dominating the book. A solo/desk ceiling on the order of tens of millions is plausible (frontmatter estimate `capacity_usd: 50,000,000`).

The binding constraint is **not** market impact but **crowding**: the metrics come from a handful of widely-watched dashboards ([[glassnode]], [[cryptoquant]]). Once a flow read is "obvious to everyone," faster participants front-run the reaction, the signal arrives already-priced, and effective capacity for *edge* (as opposed to execution) shrinks even though the instrument is deep.

## What kills this strategy

See [[failure-modes]] for the general patterns.

1. **Label revision / look-ahead bias.** Exchange-address labels are revised and backfilled; a backtest on today's labels overstates edge. Mitigate with strict [[point-in-time-data]] snapshots.
2. **ETF-era flow migration.** Spot-ETF and custody rails route large flow off classic exchange wallets (2024+), so exchange netflow captures a shrinking share of real supply movement.
3. **Crowding.** Everyone watches the same Glassnode/CryptoQuant charts; the obvious reads get arbitraged or inverted (whales who know they are watched can stage deceptive flows).
4. **False signals / regime dependence.** Outflows can mean custody migration, not bullishness; inflows can be internal rebalancing, not selling. Edge is regime-dependent and weakens in chop.
5. **Vendor / data-quality risk.** Outages, metric methodology changes, or mis-labelled clusters silently break the score.

## Kill criteria

Numeric halt conditions (see [[when-to-retire-a-strategy]]):

- Rolling **6-month Sharpe < 0** vs a price-only momentum baseline on point-in-time data → halt and re-research.
- Rolling **90-day PnL < -15%** of allocated capital → flatten and review.
- Live signal hit rate falls below the **out-of-sample baseline for 3 consecutive months** → assume decay/crowding, cut size 50%.
- Detection that a **vendor materially re-labelled** exchange addresses (invalidating the historical distribution) → re-fit before trading.
- Exchange-flow share of estimated total network flow drops below a floor (ETF migration thesis confirmed) → down-weight or retire the netflow leg.

## Advantages

- **Leading, not lagging** — reads supply/intent before it prints on the tape.
- **High capacity** relative to wallet/memecoin strategies; trades deep BTC/ETH perps.
- **Public data** — no privileged feed required; inputs are on-chain plus public dashboards.
- **Composable** with the [[on-chain-regime]] and [[institutional-flow-regime]] baskets as a directional overlay.
- **Honest framework** — naturally testable against a price-only baseline if PIT discipline is kept.

## Disadvantages

- **No reliable public Sharpe**; weak-to-moderate, regime-dependent edge.
- **Look-ahead / label-revision risk** makes honest backtesting hard.
- **ETF-era decay** of classic exchange-flow signals.
- **Crowding** — most-watched metrics are largely priced in.
- **Slow cadence** (weeks-lead) → few bets, high sample variance, patience required.
- **Vendor dependency** for metric definitions and labels.

## Sources

- [[2026-06-03-cryptodataapi-14-basket-regime-framework]] — defines the 14-basket crypto regime taxonomy, including basket 7 (On-Chain Intelligence) that this strategy operationalises.
- The specific signal-combination, gating, and sizing logic above is the **wiki's own synthesis**, not a reproduction of any single external system. No external performance numbers are claimed.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/exchange-flows/{symbol}` — CEX inflow/outflow (1h/6h/24h/7d, per-exchange breakdown)
- `GET /api/v1/on-chain/exchange-flows/{symbol}/history` (new 2026-10-08) — archived trailing 1h/24h `inflow`/`outflow`/`net` plus `per_exchange_1h`, hourly (`interval=1h`) from 2026-05-28, ≤93 days per call. Amounts are in native token units (USD for USDT/USDC/DAI). This is the replay source for netflow rules
- `GET /api/v1/backtesting/snapshots?data_type=exchange_flow_spikes` — every spike alert archived from 2026-10-08 00:25 UTC. Live, add `source=transfer` to `/on-chain/exchange-flows/spike-alerts` to drop `balance_delta` rows, which can be an exchange moving funds between its own hot and cold wallets
- `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` — stablecoin dry-powder z-score signal
- `GET /api/v1/on-chain/miners/reserves` — BTC miner pool reserves + flows
- `GET /api/v1/on-chain/miners/hash-ribbon` — Hash Ribbon state (capitulation/recovery/normal)
- `GET /api/v1/on-chain/dormancy/btc` — BTC MVRV + supply-shock zone classification
- `GET /api/v1/on-chain/score` — On-Chain Health composite (0-100)
  - **Caveat (2026-10-08 API fix):** before 2026-10-08 the score's `exchange_flow` component summed every tracked token's 24h flow in its own native units, so it pinned at 20 or 80. Any composite reading, or any threshold calibrated on readings, from before that date is biased. The component now scores the USDT/USDC/DAI 24h net only. Components with no data, currently `whale_accumulation`, carry weight 0 and the rest are renormalised; they are not scored a neutral 50. See [[cryptodataapi-on-chain]].

**Historical data:**
- ~~`GET /api/v1/on-chain/whales/accumulation-score/{symbol}` — whale accumulation score timeseries~~ — **disabled** (503 `coming_soon`; unlisted from the spec since 2026-10-09). Working substitute (2026-10-17): `GET /api/v1/on-chain/exchange-flows/{symbol}/history` — archived CEX inflow/outflow/net since 2026-05-28 (up to 93 days per call); sustained net outflow is a proxy for accumulation, not a holder-balance measure
- `GET /api/v1/market-intelligence/stablecoin-history` — stablecoin market-cap timeseries

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-on-chain]].

**Live dashboards:** [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this strategy end-to-end:

- **Signal** — `GET /api/v1/on-chain/exchange-flows/BTC` (1h-7d windows) + `GET /api/v1/on-chain/stablecoin-reserves/dry-powder` for the flow/dry-powder composite; `GET /api/v1/on-chain/miners/hash-ribbon` and `GET /api/v1/on-chain/dormancy/btc` for the slower cycle legs
- **Spike watch** — `GET /api/v1/on-chain/exchange-flows/spike-alerts` (>= $1M transfers) as the real-time whale-deposit trigger
- **Regime gate** — combine `GET /api/v1/on-chain/score` with `GET /api/v1/quant/market`; flow signals lead price by weeks, so act only when the HMM state agrees with the flow direction
- **Backtest** — point-in-time discipline is this page's core requirement: replay against `GET /api/v1/backtesting/daily-snapshots/{date}` (full daily payload since 2026-03-02) and `GET /api/v1/quant/regimes/history` (hourly HMM probabilities since 2020, Parquet, Pro Plus); ~~`GET /api/v1/on-chain/whales/accumulation-score/{symbol}` carries its own accumulation timeseries~~ (**disabled**: 503 `coming_soon`, unlisted from the spec since 2026-10-09) — replay the flow leg with `GET /api/v1/on-chain/exchange-flows/{symbol}/history` instead (since 2026-05-28, up to 93 days per call; 2026-10-17)
- **Tips** — the weeks-lead cadence means hourly polling of the cached `/api/v1/daily` bundle is plenty; never validate old signals against re-labelled current data — label revision is this strategy's lookahead trap

## Related

- [[exchange-flow-spike-reaction]] — per-event study of single large deposits (stablecoin dry powder, BTC/ETH inflows) with tape confirmation
- [[on-chain-regime]]
- [[crypto-market-regime-taxonomy]]
- [[on-chain-analysis]]
- [[on-chain-analysis]]
- [[whale-trade]]
- [[on-chain-smart-money-tracking]]
- [[miner-capitulation-bottom]]
- [[institutional-flow-regime]]
- [[point-in-time-data]]
- [[nansen]]
- [[edge-taxonomy]]
- [[failure-modes]]
- [[when-to-retire-a-strategy]]
- [[hyperliquid]]
