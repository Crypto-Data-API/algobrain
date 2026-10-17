---
title: "Exchange Net Flows"
type: concept
created: 2026-06-24
updated: 2026-10-17
status: draft
tags: [indicators, bitcoin, behavioral-finance]
aliases: ["Exchange Net Flows", "exchange-netflow", "Exchange Netflow", "Exchange Net Flow", "Exchange Reserve", "Net Exchange Flow"]
domain: [indicators]
prerequisites: ["[[on-chain-analysis]]", "[[bitcoin]]"]
difficulty: intermediate
related:
  - "[[cryptodataapi]]"
  - "[[on-chain-analysis]]"
  - "[[hodl-waves]]"
  - "[[mvrv]]"
  - "[[nupl]]"
  - "[[realized-price]]"
  - "[[bitcoin]]"
  - "[[glassnode]]"
---

# Exchange Net Flows

**Exchange net flow** is an [[on-chain-analysis|on-chain]] metric equal to coins **flowing into** known exchange wallets minus coins **flowing out** of them over a period. A *positive* net flow (inflows > outflows) means exchange-held balances are rising, often read as potential **sell pressure**; a *negative* net flow (outflows > inflows) means coins are leaving exchanges — typically interpreted as **accumulation** and withdrawal to cold storage. The running total of coins held on exchanges is the related **exchange reserve** (or exchange balance).

## How It Works

The metric rests on a simple boundary idea: an exchange is where most coins are converted to fiat or stablecoins, so the *direction of flow across the exchange wallet boundary* is a proxy for net intent to sell versus hold.

- **Net flow = inflows − outflows** over a chosen window (daily, weekly). Positive = net deposits; negative = net withdrawals.
- **Exchange reserve / balance** — the cumulative stock of coins sitting in exchange-labelled wallets. Net flow is the *change*; reserve is the *level*. A sustained run of negative net flows draws the reserve down over months.

Interpretation:

- **Rising reserves (sustained inflows)** — coins arriving on exchanges are positioned to be sold or posted as collateral, so persistent net inflows are read as **building sell pressure**. A large single deposit from a previously dormant wallet is watched as a possible distribution signal.
- **Falling reserves (sustained outflows)** — coins leaving for self-custody reduce the immediately sellable float and are read as **accumulation**; a multi-month decline in reserve is often cited as a structurally constructive (supply-tightening) backdrop.
- **Stablecoin flows** — the mirror metric. Stablecoins (USDT, USDC) *arriving* on exchanges are "dry powder" staged to buy; net stablecoin inflows alongside crypto outflows are read as latent demand.

Identifying which addresses belong to which exchange is an **entity-labelling** task performed by analytics providers (see [[glassnode]]), via clustering heuristics — it is an interpretation, not a property of the chain.

## How Traders Use It

- **Sell-pressure gauge** — spikes in net inflows, especially from whales or long-dormant coins, are treated as early warning of distribution before a selloff.
- **Accumulation / supply squeeze** — a steady multi-month drawdown in exchange reserve is used to argue that liquid float is shrinking, a backdrop that can amplify upside.
- **Confluence** — net flows are read alongside [[hodl-waves]], [[mvrv]], [[nupl]], and distance from [[realized-price]] (see [[on-chain-analysis]]) to confirm whether flow and holder behaviour agree on the regime.

## Illustrative Example

Suppose, over several weeks, the exchange reserve for [[bitcoin]] steadily declines: net flows print negative day after day as coins are withdrawn to private wallets. A trader reads this as accumulation and a shrinking sellable float — a supportive supply backdrop. Then a cluster of large deposits from older wallets pushes net flow sharply positive: long-held coins are arriving on exchanges, a possible distribution warning, prompting a more cautious stance. (Directional pattern only — real magnitudes vary widely and net flow is noisy day to day.)

## Limitations and Pitfalls

- **Entity-labelling is imperfect and revised** — exchange labels are provider heuristics that change as clustering improves. A past net-flow value may be *restated* later, so backtests need point-in-time discipline (see the caveat section in [[on-chain-analysis]]).
- **Derivatives vs spot venues** — flows to a *derivatives* exchange are often margin/collateral movements, not spot supply hitting the order book; conflating them with spot sell pressure is a common error. Distinguish spot from perp/futures venues.
- **Internal transfers and custody reshuffles** — exchanges move coins between hot/cold/internal wallets and across labelled clusters, generating flows that are *not* user deposits or withdrawals. Custodian and OTC-desk flows muddy the signal further.
- **Stablecoin confounding** — crypto outflows can coincide with stablecoin inflows (rotation, not exit), so reading coin flows in isolation can mislead. Pair the two.
- **Aggregation hides who** — net flow nets deposits against withdrawals, so a quiet net number can mask large two-sided activity. Cohorting by entity size (e.g. whale deposits) adds context.
- **Lagging/contextual** — like most on-chain flow metrics it is best as confirmation, not a standalone trigger.

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

## Related

- [[exchange-flow-spike-reaction]] — strategy that trades single large exchange deposits, with an internal-shuffle filter
- [[on-chain-analysis]]
- [[hodl-waves]]
- [[mvrv]]
- [[nupl]]
- [[realized-price]]
- [[bitcoin]]
- [[glassnode]]

## Sources

General market knowledge; no specific wiki source ingested yet.
