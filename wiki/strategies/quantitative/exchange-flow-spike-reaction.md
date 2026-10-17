---
title: "Exchange-Flow Spike Reaction"
type: strategy
created: 2026-10-17
updated: 2026-10-17
status: draft
tags: [crypto, on-chain, stablecoins, bitcoin, ethereum, event-driven, quantitative, alternative-data, perpetual-futures]
aliases: ["Whale Deposit Reaction", "CEX Inflow Spike Trade", "Stablecoin Dry-Powder Spike", "Spike-Alert Event Study"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto]
complexity: intermediate
backtest_status: untested

edge_source: [informational, behavioral]
edge_mechanism: "A large stablecoin deposit to an exchange is buying power arriving, and a large BTC or ETH deposit is coins arriving to be sold. Both are visible on-chain minutes to hours before the order hits the book. The trade takes the side of the depositor once the tape starts to agree, against traders who react only to price."

data_required: [exchange-flow-spike-alerts, exchange-flow-history-1h, taker-trade-flow-1m, funding-rates, mark-price]
min_capital_usd: 5000
capacity_usd: 10000000
crowding_risk: medium

expected_sharpe: 0.2   # prior only; the history-proxy event study below is consistent with zero edge
expected_max_drawdown: 0.20
breakeven_cost_bps: 15

decay_evidence: "None measurable. The alert archive starts 2026-10-08 00:25 UTC and the flow history 2026-05-28 (USDT/USDC) or 2026-06-01 (BTC/ETH). Whale-alert style deposit tracking has been public since at least 2019, so the simple version of this signal is likely already arbitraged."

kill_criteria: |
  - mean net 24h return per trade below 0 after 60 trades on either leg (retire that leg)
  - hit rate (take-profit before stop) below 45% after 60 trades on either leg
  - sleeve drawdown above 12%
  - the spike-alert feed or the flow history stops updating for more than 6 hours twice in a month

related: ["[[on-chain-flow-trading]]", "[[exchange-netflow]]", "[[stablecoin-supply]]", "[[whale-onchain-flows]]", "[[onchain-capitulation-confluence]]", "[[whale-copy-flow-funding-filter]]", "[[structural-forced-selling]]", "[[news-trading]]", "[[whale-alert]]", "[[proof-of-reserves]]", "[[coinbase-premium]]", "[[cryptodataapi-on-chain]]", "[[cryptodataapi-backtesting]]", "[[cryptodataapi-mcp]]", "[[edge-taxonomy]]", "[[failure-modes]]", "[[when-to-retire-a-strategy]]"]

gates:
  - id: stable_alerts_2h
    role: entry
    rule: "Leg A: transfer-sourced USDT and USDC inflow alerts to exchange wallets sum to at least $300M over the trailing 2 hours"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/spike-alerts?direction=inflow&source=transfer&limit=500
    field: alerts[].amount_usd
    replay: /api/v1/backtesting/snapshots?data_type=exchange_flow_spikes&start={start}
    replay_field: snapshots[].data[].amount_usd
    note: "symbol takes one token, so filter USDT and USDC client-side. alerts[].ts is unix SECONDS. The live route keeps the last 500 rows (about 10 hours). The archive starts 2026-10-08 00:25 UTC and also holds rows under $1M (the smallest seen was $105k), so apply the $1M floor yourself. Drop exact duplicates on (ts, chain, symbol, exchange, direction, amount): 72 of 9,752 archived rows were repeats."
  - id: stable_net_floor
    role: entry
    rule: "Leg A: USDT + USDC 1h net exchange flow is at least +$250M"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/{symbol}
    field: windows.1h.net
    replay: /api/v1/on-chain/exchange-flows/{symbol}/history?start={start}&interval=1h
    replay_field: points[].net_1h
    note: "Call once for symbol=USDT and once for USDC and add them. Stablecoin amounts are USD. History starts 2026-05-28 11:58 UTC; points[].ts is unix seconds; at most 93 days per call."
  - id: stable_net_z
    role: entry
    rule: "Leg A: that combined 1h net is at least 3 standard deviations above its trailing-30-day hourly mean"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/{symbol}/history?start={start}&interval=1h
    field: points[].net_1h
    note: "start = 30 days back; z = (latest - mean) / stdev over the 720 hourly points. The rows are trailing windows sampled about every 30 minutes, so never sum successive points."
  - id: funding_not_crowded_long
    role: filter
    rule: "Leg A: Hyperliquid BTC hourly funding is at most +0.005% (5e-5): the long side is not already crowded"
    runnable: true
    endpoint: /api/v1/hyperliquid/funding-rates?coin=BTC&limit=1
    field: current_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin=BTC&interval=1h&start={start}
    replay_field: data[].funding_rate_mean
    note: "5e-5 is the crowded_abs threshold the /quant/gex regime rules publish."
  - id: taker_buy_confirm
    role: entry
    rule: "Leg A: over the 60 closed minutes after the trigger, BTC taker buy notional exceeds sell notional on Hyperliquid"
    runnable: true
    endpoint: /api/v1/hyperliquid/trade-flow?coin=BTC&minutes=60
    field: data[].buy_notional
    replay: /api/v1/backtesting/hl-trade-flow?coin=BTC&start={start}
    replay_field: data[].buy_notional
    note: "Sum buy_notional and sell_notional over the rows and skip partial minutes. Replay starts 2026-09-09."
  - id: majors_inflow_alert
    role: entry
    rule: "Leg B: a BTC or ETH inflow alert of at least $50M to one exchange"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/spike-alerts?symbol={symbol}&direction=inflow&min_amount=50000000
    field: alerts[].amount_usd
    replay: /api/v1/backtesting/snapshots?data_type=exchange_flow_spikes&start={start}
    replay_field: snapshots[].data[].amount_usd
    note: "Do NOT add source=transfer here. Every BTC (924) and ETH (2,576) row archived from 2026-10-08 to 2026-10-17 was source balance_delta, so a transfer filter leaves Leg B with no signals. shuffle_filter and majors_net_confirm take its place."
  - id: shuffle_filter
    role: filter
    rule: "Leg B: drop the alert if the same exchange shows an opposite-direction alert for the same symbol within 15 minutes and within 5% of the amount (an internal hot/cold wallet move)"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/spike-alerts?symbol={symbol}&min_amount=50000000
    field: alerts[].direction
    replay: /api/v1/backtesting/snapshots?data_type=exchange_flow_spikes&start={start}
    replay_field: snapshots[].data[].direction
    note: "Compare amount (native units) and ts. 404 of 6,166 archived balance_delta rows had such a twin."
  - id: majors_net_confirm
    role: entry
    rule: "Leg B: the symbol's 1h net exchange flow, all exchanges, is at least +50% of the alert's amount in native units"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/{symbol}
    field: windows.1h.net
    replay: /api/v1/on-chain/exchange-flows/{symbol}/history?start={start}&interval=1h
    replay_field: points[].net_1h
    note: "BTC and ETH amounts are in coins, not USD. Compare with alerts[].amount, not amount_usd. In the top 1% of gross-inflow hours (2026-06-01 to 2026-10-17), the median net was 2% of gross for BTC and 3% for ETH. Most giant inflows are offset within the hour."
  - id: majors_net_z
    role: entry
    rule: "Leg B: that 1h net is at least 3 standard deviations above its trailing-30-day hourly mean"
    runnable: true
    endpoint: /api/v1/on-chain/exchange-flows/{symbol}/history?start={start}&interval=1h
    field: points[].net_1h
    note: "BTC history starts 2026-06-01 03:51 UTC, and ETH 2026-06-01 02:51 UTC."
  - id: funding_not_crowded_short
    role: filter
    rule: "Leg B: Hyperliquid hourly funding on the coin is at least -0.0025% (-2.5e-5): the short side is not already crowded"
    runnable: true
    endpoint: /api/v1/hyperliquid/funding-rates?coin={coin}&limit=1
    field: current_rate
    replay: /api/v1/backtesting/hl-funding-bars?coin={coin}&interval=1h&start={start}
    replay_field: data[].funding_rate_mean
  - id: taker_sell_confirm
    role: entry
    rule: "Leg B: over the 60 closed minutes after the trigger, the coin's taker sell notional exceeds buy notional on Hyperliquid"
    runnable: true
    endpoint: /api/v1/hyperliquid/trade-flow?coin={coin}&minutes=60
    field: data[].sell_notional
    replay: /api/v1/backtesting/hl-trade-flow?coin={coin}&start={start}
    replay_field: data[].sell_notional
  - id: entry_after_confirm
    role: entry
    rule: "Enter at the mark at the end of the 60-minute confirmation window: long BTC for Leg A, short the deposited coin for Leg B"
    runnable: true
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: take_profit
    role: exit
    rule: "Close at a 2.0% move in the trade's favour from the entry fill"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: stop_loss
    role: stop
    rule: "Stop 1.5% against the entry fill"
    runnable: true
    input: position
    endpoint: /api/v1/hyperliquid/open-interest
    field: assets[].mark_price
  - id: time_stop
    role: stop
    rule: "Close 24 hours after entry"
    runnable: true
    input: position
  - id: risk_size
    role: sizing
    rule: "Risk 0.5% of the sleeve to the stop (notional = 33% of the sleeve), at no more than 2x leverage"
    runnable: true
    input: position
  - id: one_per_leg
    role: sizing
    rule: "At most one open position per leg; a new trigger while a position is open is ignored, not added"
    runnable: true
    input: position
---

# Exchange-Flow Spike Reaction

The exchange-flow spike reaction is a short-horizon, **per-event** trade on large exchange deposits. **Leg A** goes long BTC when hundreds of millions of dollars of USDT/USDC land on exchanges within two hours: dry powder arriving. **Leg B** shorts BTC or ETH after a large deposit of the coin itself that is *not* just the exchange moving funds between its own wallets: potential sell pressure. Both legs wait 60 minutes for the Hyperliquid tape to agree before entering, and hold for at most 24 hours. The page is built on `/on-chain/exchange-flows/spike-alerts` (live), its `exchange_flow_spikes` archive (from 2026-10-08) and `/on-chain/exchange-flows/{symbol}/history` (from 2026-05-28).

**How this differs from the existing on-chain pages.** [[on-chain-flow-trading]] is a slow, multi-signal *directional bias*. It blends netflow, dry powder, dormancy and miners into a position held for days to weeks, and uses spike alerts only as a watch item. [[onchain-capitulation-confluence]] and [[put-protected-dip-buying]] use an inflow spike as one leg of a capitulation bottom. [[whale-copy-flow-funding-filter]] and [[smart-money-vs-crowd-divergence]] use outflows as accumulation confirmation. [[structural-forced-selling]] uses inflows as the leading leg of a fund unwind. This page is the **event study under all of them**: does one large deposit, on its own, move price over the next 1-24 hours? It also deals with the `source` field, which shapes every one of those pages without being mentioned on them (see the Leg B note below). The concept is on [[exchange-netflow]].

## Edge source

Per [[edge-taxonomy]], **informational + behavioral**.

- **Informational.** A deposit is visible on-chain, and in the alert feed, before the depositor's order reaches the book. Someone who sends $500M of USDT to Binance usually intends to use it, and someone who deposits $100M of BTC usually intends to sell or post it as collateral.
- **Behavioral.** Most traders react to price, not to deposits, and those who do watch deposits (whale-alert style bots) over-react to *gross* figures, which are mostly internal shuffles. Filtering to *net* flow is the analytical edge, if there is one.

## Why this edge exists

**Leg A, dry powder.** Stablecoin balances on exchanges are spendable. A deposit of hundreds of millions into Binance or Coinbase is often a fund, OTC desk or market maker positioning to buy spot or post margin. If the buying follows within hours, the front-runner earns the price impact. **Who is on the other side:** sellers into the depositor's bid who did not see it coming.

**Leg B, sell pressure.** A real BTC or ETH deposit from outside the exchange is usually followed by a sale, an OTC settlement or collateral posting, and only the first moves price down. **Who is on the other side:** buyers absorbing the deposit's sale.

**Why both legs are weaker than they look:**
- Stablecoin deposits are as often **market-maker inventory cycling** as new buying. On most days in the archive, transfer-sourced inflows of $1M+ ran $0.3-2.6B and outflows nearly matched them.
- Large BTC/ETH "inflows" are mostly **the exchange moving coins between its own wallets**. In the top 1% of gross BTC inflow hours, the median 1h net was **2% of gross** (ETH 3%). Example: in the 2026-10-15 14:05 UTC sample, BTC inflow_1h was 7,294 BTC and outflow_1h 6,973 BTC, for a net of +321 BTC.
- Large deposits are increasingly **collateral for derivatives or ETF creation flows**, not spot selling.

## Null hypothesis

Under no edge, a qualifying spike carries no information. The 24h return after it has a mean of **0** (net of the sample's drift). With **2.0% / 1.5% barriers**, a driftless walk hits the take-profit first about **43%** of the time (1.5 / 3.5). Since the win is 4/3 the loss, that gives an expected gross of **0** and a net of **minus about 10 bps** per trade.

**History-proxy event study.** This is not a backtest: no costs, no confirmation gates, a close-to-close 24h hold, and events spaced at least 24h apart. It uses `/exchange-flows/{symbol}/history` (hourly) from 2026-05-28 to 2026-10-17 with Binance `BTCUSDT`/`ETHUSDT` 1h bars.

| Trigger (1h net, z ≥ 3 vs trailing 30d) | Events | Mean 4h | Mean 24h | 24h in favour |
|---|---|---|---|---|
| USDT+USDC ≥ +$250M → long BTC | 18 | +0.26% | +0.39% | 44% |
| USDT+USDC ≥ +$250M → long ETH | 18 | −0.09% | +0.23% | 39% |
| BTC ≥ +500 BTC → short BTC | 19 | −0.34% | −0.35% | 42% |
| ETH ≥ +20,000 ETH → short ETH | 15 | −0.14% | −0.31% | 47% |

Leg A is slightly positive and Leg B slightly negative (shorting after a BTC inflow *lost* money on average). Nothing comes close to significance, and the null is **not rejected**. The alert-level version cannot be tested yet, because the archive held only nine days (9,752 rows) on 2026-10-17.

**Statistical power.** The standard deviation of BTC's 24h return over the sample was 2.08%. To detect a true +0.5% mean at 80% power and 5% two-sided needs about **136 events** (n ≈ (2.8 × 2.08 / 0.5)²). The proxy produced about 3.8 events a month, so that is about **three years**. A larger true effect, or pooling with ETH, shortens it. The confirmation gates cut it further. Until then this is a hypothesis with a pre-registered rule, not a strategy with evidence.

## Rules

**Leg A, stablecoin dry powder (long BTC):**
1. Transfer-sourced (`source=transfer`) USDT + USDC **inflow** alerts sum to at least **$300M over the trailing 2h** (deduplicated, $1M floor).
2. The USDT + USDC **1h net** is at least **+$250M**, and
3. at least **3σ** above its trailing-30-day hourly mean.
4. Hyperliquid BTC funding is at most **+0.005%/h**.
5. Over the next **60 closed minutes**, Hyperliquid BTC taker buys exceed taker sells.
6. Enter long BTC at the mark at the end of that hour.

**Leg B, BTC/ETH deposit (short the coin):**
1. A BTC or ETH **inflow alert of at least $50M** to one exchange. Any `source` qualifies: none of these alerts in the archive carried `transfer`.
2. **Shuffle filter:** no opposite-direction alert at the same exchange and symbol within ±15 minutes and within 5% of the amount.
3. The coin's **1h net** across exchanges is at least **50% of the alert amount** in coins, and
4. at least **3σ** above its trailing-30-day mean.
5. Hyperliquid funding on the coin is at least **−0.0025%/h**.
6. Over the next 60 closed minutes, taker sells exceed buys.
7. Enter short at the mark at the end of that hour.

**Exits (both legs):** take profit at +2.0%, stop at −1.5%, time stop at 24h.

**Sizing:** risk 0.5% of the sleeve to the stop (notional 33% of the sleeve, at most 2x leverage), with one position per leg.

## Implementation pseudocode

```python
# exchange_flow_spike_reaction.py — event loop (sketch); ts fields are unix SECONDS
STABLES = {"USDT", "USDC"}

def dedupe(alerts):
    seen, out = set(), []
    for a in alerts:
        k = (a["ts"], a["chain"], a["symbol"], a["exchange"], a["direction"], round(a["amount"], 6))
        if k not in seen and a["amount_usd"] >= 1e6:
            seen.add(k); out.append(a)
    return out

def leg_a_trigger(alerts, now, net_1h_usd, z_net):
    window = [a for a in alerts if a["symbol"] in STABLES and a["source"] == "transfer"
              and a["direction"] == "inflow" and now - a["ts"] <= 7200]
    return sum(a["amount_usd"] for a in window) >= 300e6 and net_1h_usd >= 250e6 and z_net >= 3

def is_shuffle(a, alerts):
    return any(b is not a and b["exchange"] == a["exchange"] and b["symbol"] == a["symbol"]
               and b["direction"] != a["direction"] and abs(b["ts"] - a["ts"]) <= 900
               and abs(b["amount"] - a["amount"]) <= 0.05 * a["amount"] for b in alerts)

def leg_b_trigger(a, alerts, net_1h_coins, z_net):
    return (a["symbol"] in {"BTC", "ETH"} and a["direction"] == "inflow" and a["amount_usd"] >= 50e6
            and not is_shuffle(a, alerts)
            and net_1h_coins >= 0.5 * a["amount"] and z_net >= 3)

def confirm(flow_rows, side):
    rows = [r for r in flow_rows if not r["partial"]]
    buy, sell = sum(r["buy_notional"] for r in rows), sum(r["sell_notional"] for r in rows)
    return buy > sell if side == "long" else sell > buy

# after a trigger: wait 60 closed minutes, check the funding filter and confirm(),
# then enter; exit on +2.0% / -1.5% / 24h
```

## Indicators / data used

From [[cryptodataapi-on-chain]] and [[cryptodataapi-backtesting]]:

- **`GET /api/v1/on-chain/exchange-flows/spike-alerts`**: large transfers to and from tracked exchange wallets. Each alert carries `ts` (unix seconds), `chain`, `symbol`, `exchange`, `direction`, `amount` (native units) with `unit`, `amount_usd` (converted at ingestion), `counterparty` and **`source`**. `source` is `transfer` (a decoded Transfer event with a real counterparty) or `balance_delta` (inferred from a wallet's balance change, which can be the exchange's own hot/cold shuffle, with `counterparty: "balance_delta"`). Filters: `min_amount` (USD, default $1M), `limit` (≤500), `symbol`, `exchange`, `chain`, `direction`, `source`. The live feed is the last 500 rows, about 10 hours.
- **`exchange_flow_spikes`** on `GET /api/v1/backtesting/snapshots`: every alert, archived in 5-minute batches of first-seen rows, from 2026-10-08 00:25 UTC. On 2026-10-17 it held 2,054 snapshots and 9,752 rows: 6,166 `balance_delta` and 3,586 `transfer`.
- **`GET /api/v1/on-chain/exchange-flows/{symbol}/history`**: trailing 1h and 24h `inflow`/`outflow`/`net` plus `per_exchange_1h`, sampled about every 30 minutes. `interval=1h` keeps the last sample per hour. **Amounts are native units except USDT/USDC/DAI, which are USD.** `ts` is unix seconds and calls are limited to 93 days. On 2026-10-17 the first points were USDT/USDC 2026-05-28 11:58 UTC, BTC 2026-06-01 03:51 UTC and ETH 2026-06-01 02:51 UTC.
- **`GET /api/v1/on-chain/exchange-flows/{symbol}`**: live `windows` (1h/6h/24h/7d), `per_exchange_24h`, `by_chain` and `spike_zscore_1h`. BTC is tracked on the `btc` chain (Binance, Kraken, Coinbase).
- **Tape and crowding** ([[cryptodataapi-hyperliquid]]): `/hyperliquid/trade-flow` (live, Pro) and `/backtesting/hl-trade-flow` (from 2026-09-09) for confirmation, and `/hyperliquid/funding-rates` / `/backtesting/hl-funding-bars` for the crowding filter.

## Example trade

**2026-10-13, Leg A trigger, no trade.** This uses the real archive and replay.

- **06:57 UTC:** a `transfer` alert shows **$543.3M of USDT** sent to Binance on Ethereum (counterparty `0x835678a6…`). Another $34.6M arrived at 07:37, so the 2h sum was **$577.9M**. Gate 1 passed.
- **Net check:** the 06:57 sample of `/exchange-flows/USDT/history` shows `net_1h` **+$515.3M** (Binance +$514.9M) and `net_24h` +$653.7M. The combined USDT + USDC 1h net was 8.1σ above its 30-day mean. Gates 2 and 3 passed.
- **Crowding:** Hyperliquid BTC funding averaged −0.00017%/h over the 07:00 hour, far below the 0.005% cap. Gate 4 passed.
- **Confirmation (07:00-08:00):** Hyperliquid BTC taker buys were **$72.9M**, against **$83.9M** of sells. Gate 5 **failed: no trade.**
- **Counterfactual:** a long at the 08:00 open ($83,829) would have reached a high of $84,133, short of the +2% target at $85,506. It would also have missed the −1.5% stop ($82,572; the low was $82,927). The 24h time stop would have closed it at $83,560: **−0.32% gross, −0.41% net.** The largest stablecoin deposit in the nine-day archive produced no follow-through, and the tape filter kept the strategy out.

*(Historical replay for illustration. Not investment advice.)*

## Performance characteristics

| Metric | Value | Note |
|---|---|---|
| Expected net Sharpe | ~0.2 (prior) | History proxy: Leg A +0.39% mean 24h (n = 18), Leg B −0.35% (n = 19), neither significant |
| Round-trip cost | ~10-14 bps | Hyperliquid taker 4.5 bps per side plus slippage. Funding over ≤24h is ±1-3 bps at normal rates |
| Breakeven cost | ~15 bps | Only if the true hit rate is about 47% against the 43% null |
| Signal frequency | ~4 per month (Leg A proxy), ~4 per month per coin (Leg B proxy) | Before the confirmation gates, which roughly halve it |
| Hold time | 1-24h | The time stop binds on most trades in a range-bound market |
| Max drawdown (expected) | ~20% | Losing streaks at 0.5% risk per trade |

Leg B's negative proxy mean is a warning, not noise to be filtered away: in 2026, large BTC deposits were as likely to precede rallies as dumps. One possible reason is collateral posted for long derivatives positions.

## Capacity limits

- **Leg A** trades BTC perps. A $1-5M position is small next to the flows that trigger it, so capacity is limited by Hyperliquid BTC depth, not by the signal.
- **Leg B** on ETH is similar. Spreading entries over the confirmation hour would help, but the page enters at one mark.
- `capacity_usd: 10000000`. Past that, entry slippage on a 2% target starts to matter, and a fund that size would want spot and CME legs as well.

## What kills this strategy

Mapped to [[failure-modes]]:

1. **Internal shuffles mistaken for flow (#7, data).** This is the dominant risk on Leg B. `balance_delta` rows can be hot/cold wallet moves, and every BTC/ETH alert in the archive is `balance_delta`. The shuffle and net filters reduce the risk but cannot remove it, because an exchange can move funds between wallets the tracker does not pair.
2. **Unit errors (#7).** Mixing `amount` (coins) and `amount_usd` in the net check, or treating BTC history values as USD, inflates or deflates triggers by a factor of roughly the coin price (about 82,000 for BTC in October 2026).
3. **No information (#1).** The proxy study is flat. Deposit trackers have been public for years, so any simple edge may be gone.
4. **Regime change.** ETF creations and basis trades route large flows through exchanges for reasons unrelated to spot direction.
5. **Feed changes (#7).** The API ships changes continuously. The 2026-10-08 release added `source` and the archive, and the same release fixed an `/on-chain/score` flow component that had been summing native token units as dollars. A tracker change in wallet coverage can shift the z-score baseline overnight.

## Kill criteria

Retire or pause a leg (see [[when-to-retire-a-strategy]]) on any of:

1. **Mean net 24h return per trade below 0** after 60 trades on that leg.
2. **Hit rate below 45%** (take profit before stop) after 60 trades. The null is about 43%; covering about 12 bps of cost needs about 46%, so 45% means the leg is not paying.
3. **Sleeve drawdown above 12%.**
4. **Data outage:** the alert feed or flow history stops updating for more than 6 hours twice in a calendar month.
5. **Shuffle contamination:** more than 30% of Leg B triggers in a month are followed, within 24 hours, by an equal outflow from the same exchange that the shuffle filter missed.

## Advantages

- **Uses data that is new and cheap.** The alert and history routes carry no plan gate in the docs, so standard plan limits apply.
- **Clear, pre-registered rules.** Every gate is runnable and replayable, and the archive accumulates forward.
- **Tape-confirmed.** It never trades on a deposit alone, which kept it out of the largest stablecoin deposit in the sample.
- **Market-neutral across legs over time.** Leg A is long and Leg B is short.

## Disadvantages

- **Statistical power is years away** at realistic effect sizes.
- **Leg B rests on inferred flows.** No transfer-sourced BTC/ETH alerts exist in the archive, so every Leg B signal depends on `balance_delta` plus heuristics.
- **The proxy evidence points the wrong way for Leg B.**
- **Exchange coverage is incomplete.** The tracked exchanges are mainly Binance, Coinbase, Kraken and Bybit. OTC desks and unlabelled wallets are invisible.

## Sources

- [[cryptodataapi-on-chain]]: spike-alert `source` semantics and filters, the exchange-flow history route (sampling, units, start dates), and the 2026-10-08 `/on-chain/score` fix.
- [[cryptodataapi-backtesting]]: the `exchange_flow_spikes` snapshot type and its start time.
- [[exchange-netflow]]: concept background on inflow and outflow interpretation.
- Live OpenAPI spec and live calls, 2026-10-17: the spike-alert and history schemas and parameters; a 500-row live alert pull; the full `exchange_flow_spikes` archive (2,054 snapshots); hourly USDT, USDC, BTC and ETH flow history from 2026-05-28; Binance 1h klines; and the Hyperliquid funding bars and trade flow for the example. Every count on this page comes from those pulls.

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/on-chain/exchange-flows/spike-alerts?direction=inflow&source=transfer&limit=500`: Leg A trigger rows (filter USDT/USDC client-side)
- `GET /api/v1/on-chain/exchange-flows/spike-alerts?symbol=BTC&direction=inflow&min_amount=50000000`: Leg B trigger rows (no `source` filter)
- `GET /api/v1/on-chain/exchange-flows/BTC`: live `windows.1h.net` for the net check
- `GET /api/v1/hyperliquid/trade-flow?coin=BTC&minutes=60`: the confirmation hour

**Historical data:**
- `GET /api/v1/backtesting/snapshots?data_type=exchange_flow_spikes&start=2026-10-08T00:25:00Z&limit=1000`: every alert since the archive began (page with `start` = last `time` + 1, since each snapshot is a distinct 5-minute tick)
- `GET /api/v1/on-chain/exchange-flows/USDT/history?start=2026-05-28&end=2026-08-28&interval=1h`: the hourly net history (93 days per call)
- `GET /api/v1/backtesting/hl-trade-flow?coin=BTC&start=2026-09-09`: replay for the confirmation gates
- `GET /api/v1/backtesting/hl-funding-bars?coin=BTC&interval=1h&start=2026-06-01`: replay for the funding filters

```bash
curl -H "X-API-Key: $CDA_KEY" \
  "https://cryptodataapi.com/api/v1/on-chain/exchange-flows/spike-alerts?direction=inflow&source=transfer&min_amount=50000000"
```

Endpoint catalogs: [[cryptodataapi-on-chain]], [[cryptodataapi-backtesting]], [[cryptodataapi-hyperliquid]].

### AI agent workflow

An agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run this page as follows:

- **Signal:** poll `/on-chain/exchange-flows/spike-alerts` every 5 minutes with `limit=500`, deduplicate, and keep a rolling 2h USDT+USDC transfer-inflow sum (Leg A) and a list of BTC/ETH inflows of $50M or more (Leg B). Remember `ts` is in seconds.
- **Net check:** on a trigger, call `/on-chain/exchange-flows/{symbol}` for `windows.1h.net` and z-score it against 30 days of `/exchange-flows/{symbol}/history`. Compare coins with coins for BTC/ETH and dollars with dollars for stablecoins.
- **Regime and crowding:** read `/hyperliquid/funding-rates?coin=BTC&limit=1` `current_rate` before arming either leg.
- **Execution:** wait 60 closed minutes, sum `/hyperliquid/trade-flow` buy versus sell notional, enter at the mark only if the tape agrees, then manage the +2.0% / −1.5% / 24h exits.
- **Backtest:** run Leg A and Leg B on the hourly history from 2026-05-28 (proxy, as above) and the alert-level rules on `exchange_flow_spikes` from 2026-10-08. Report each leg's hit rate against the 43% null, and do not pool the legs.

## Related

- [[on-chain-flow-trading]]: the slow multi-signal on-chain bias this page is the event-level complement to
- [[exchange-netflow]]: the inflow/outflow concept
- [[stablecoin-supply]], [[whale-onchain-flows]]: the narratives behind dry powder and whale deposits
- [[onchain-capitulation-confluence]], [[put-protected-dip-buying]]: inflow spikes as a capitulation leg
- [[whale-copy-flow-funding-filter]], [[smart-money-vs-crowd-divergence]]: outflows as accumulation confirmation
- [[structural-forced-selling]]: inflows as the leading leg of fund unwinds
- [[news-trading]]: on-chain alerts as early news
- [[whale-alert]], [[proof-of-reserves]]: other sources of exchange-wallet visibility
- [[liquidation-density-magnet]], [[forced-flow-exhaustion-fade]]: the other two pages built on the 2026-10 data releases
- [[edge-taxonomy]], [[failure-modes]], [[when-to-retire-a-strategy]]
