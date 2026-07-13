---
title: "On-Chain Analysis"
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [crypto, bitcoin, ethereum, indicators]
aliases: ["on-chain-analytics", "blockchain-analysis", "on-chain analysis", "on-chain metrics"]
domain: [market-microstructure]
prerequisites: ["[[blockchain]]"]
difficulty: intermediate
related: ["[[blockchain]]", "[[whale-trade]]", "[[defi]]", "[[bitcoin]]", "[[ethereum]]", "[[self-custody]]", "[[defai]]", "[[ai-trading-agents]]", "[[decentralized-ai]]", "[[on-chain-regime]]", "[[crypto-market-regime-taxonomy]]", "[[bitcoin-halving]]", "[[point-in-time-data]]"]
---

# On-Chain Analysis

**On-chain analysis** is the practice of examining [[blockchain]] data -- transactions, wallet balances, smart contract interactions, and network metrics -- to derive trading signals and assess market conditions. Because blockchains are public and transparent, on-chain data provides insights unavailable in traditional markets, including real-time visibility into large holder behavior, exchange flows, and protocol activity. On-chain data is also the primary substrate for [[ai-trading-agents|AI trading agents]] operating in [[defai|DeFAI]], where models trained on on-chain behavior drive autonomous strategy execution.

This page is the **mechanics layer**: it defines the metrics and what each one measures. For how these metrics combine into market *states* (accumulation, euphoria, capitulation, etc.), see [[on-chain-regime]], which defers to this page for metric definitions. For the broader state machine across crypto, see [[crypto-market-regime-taxonomy]].

---

## Key On-Chain Metrics

| Metric | What It Signals |
|---|---|
| **Exchange inflows/outflows** | Coins moving to exchanges suggest sell pressure; outflows suggest accumulation |
| **[[whale-trade|Whale]] wallet tracking** | Large holder movements often precede significant price action |
| **Active addresses** | Network adoption and usage trends |
| **MVRV ratio** | Market value vs realized value; signals over/undervaluation |
| **Stablecoin supply on exchanges** | "Dry powder" available for buying |
| **NVT ratio** | Network value to transactions; a "P/E ratio" for blockchains |
| **[[defi|DeFi]] TVL changes** | Capital flows between protocols and chains |
| **Miner/validator flows** | [[proof-of-work|Miner]] selling patterns and staking behavior |
| **SOPR** | Whether coins are being spent at a profit or loss |
| **Coin-days-destroyed / dormancy** | Whether long-held (old) coins are moving |
| **Realized cap** | Aggregate cost basis of the supply |
| **Miner reserves / hash ribbon** | Miner balance-sheet health and capitulation |

---

## Exchange Flows

Exchange flow metrics track coins moving in and out of known exchange wallets (clustered and labelled by analytics providers). The core idea: an exchange is where coins are converted to fiat or stablecoins, so the direction of flow across the exchange boundary is a proxy for net intent to sell versus hold.

- **Net inflows** (deposits > withdrawals): coins arriving on exchanges are positioned to be sold or used as collateral, so sustained net inflows are read as building **sell pressure**. Large single deposits from previously dormant wallets are watched as a potential distribution signal.
- **Net outflows** (withdrawals > deposits): coins leaving exchanges for [[self-custody]] are read as **accumulation** and a reduction in immediately sellable float. Persistent outflows are associated with a tightening liquid supply and are often cited as a structurally bullish backdrop.
- **Exchange reserve / balance**: the running total of coins held on exchanges. A multi-month decline in exchange reserve is the cumulative result of sustained outflows -- the "float" available to be dumped is shrinking.
- **Stablecoin exchange balances**: stablecoins (USDT, USDC) sitting on exchanges are treated as **"dry powder"** -- capital staged to buy. Rising stablecoin balances on exchanges, especially alongside coin outflows, are read as latent demand; falling balances suggest dry powder has already been deployed.
- **Stablecoin Supply Ratio (SSR)**: the ratio of coin market cap to stablecoin supply. A low SSR means stablecoins are large relative to the asset -- more potential buying power on the sidelines.

Caveat: exchange labels are an *interpretation* placed on raw addresses by the data provider, not a property of the chain itself (see [[#Leading vs Lagging, and Data Caveats]]).

---

## Whale Tracking

**Whale tracking** monitors large-balance wallets (commonly cohorts holding above a threshold, e.g. 1,000+ BTC) for accumulation versus distribution.

- **Accumulation**: whale cohort balances rising, especially during sideways or falling price, is read as smart-money positioning ahead of a move.
- **Distribution**: whale balances falling into strength suggests large holders are selling into retail demand.
- **Flow direction**: whales moving coins *to* exchanges is a distribution warning; moving *off* exchanges to cold storage signals intent to hold.

Following large-holder positioning in real time is unique to transparent ledgers -- in equities or forex this order flow is private. See [[whale-trade]] for the trade-level playbook built on this.

---

## Holder Behaviour and Dormancy

These metrics infer *who* is transacting (long-term vs short-term holders) and at what cost basis, by reading the age and acquisition price of moving coins.

- **SOPR (Spent Output Profit Ratio)**: ratio of the value of coins when spent to their value when last moved. SOPR > 1 means coins are being spent at a profit on average; SOPR < 1 means at a loss. Used to gauge whether the market is realizing gains or capitulating.
- **Coin-days-destroyed (CDD)**: each coin accumulates "coin-days" the longer it sits unmoved; when it moves, those days are "destroyed." High CDD means old, long-dormant coins are moving -- often experienced holders acting.
- **Dormancy**: CDD normalized by transaction volume; the average age of the coins being spent. Rising dormancy signals older coins entering circulation.
- **MVRV ratio**: market cap divided by **realized cap**. MVRV measures aggregate unrealized profit/loss; high values flag overvaluation (large paper gains, distribution risk), low values flag undervaluation.
- **Realized cap**: values each coin at the price it last moved (its on-chain cost basis) rather than at the current price. It is the aggregate **cost basis** of the supply and the denominator behind MVRV and many holder-behaviour metrics.

These definitions are deliberately the mechanics; their *regime* interpretation (e.g. an MVRV/SOPR combination flagging a euphoria or capitulation regime) lives in [[on-chain-regime]].

---

## Miner Metrics

Miners are structural, semi-forced sellers: they earn newly issued coins and must cover energy and hardware costs, so their balance-sheet stress shows up on-chain.

- **Miner reserves**: aggregate balance held by miner wallets. Falling reserves mean miners are selling into the market (supply pressure); rising reserves mean they are holding.
- **Hash ribbon**: a moving-average crossover of network hash rate (e.g. 30-day vs 60-day). When hash rate rolls over, weaker miners are switching off -- **miner capitulation**. Historically the recovery of the hash ribbon after capitulation has been read as a **late-bear bottoming signal**, since the marginal forced sellers have already exited and remaining miners are the lowest-cost operators.
- **Puell Multiple**: daily coin issuance (in USD) divided by its 365-day average. It measures miner revenue relative to its yearly norm; very low readings have coincided with cycle bottoms (miners maximally stressed), very high readings with tops.
- **Supply / miner economics**: miner revenue per coin is structurally cut at each [[bitcoin-halving]], which halves the block subsidy. Halvings compress miner margins and have historically reshaped the supply side of the market, making miner reserves and capitulation especially informative around those events.

---

## Tools & Data Sources

Popular platforms for on-chain analysis include Glassnode, Nansen, Dune Analytics, Arkham Intelligence, and DeBank. Many traders also query blockchain data directly via RPC endpoints or SQL-based explorers (e.g., QuickNode, Flipside Crypto).

---

## Leading vs Lagging, and Data Caveats

On-chain metrics are frequently a **leading** indicator: exchange inflows, whale movement, and dormancy shifts can register *before* price reacts, because the transactions that precede selling or accumulation are visible on the ledger in real time.

However, there is a critical caveat. The **raw ledger** (transactions, balances, coin ages) is immutable, but the **interpretation layer** -- the entity, exchange, and miner *labels* that turn raw addresses into "exchange inflows" or "whale balances" -- is produced by analytics providers and is **revised over time** as clustering heuristics improve and new addresses are attributed. A metric value you query today for a past date may differ from what the provider would have reported on that date.

This means backtests built on on-chain metrics require **point-in-time discipline** (see [[point-in-time-data]]): use the labels *as they existed* at decision time, not today's restated history, or the backtest will inherit look-ahead bias from relabelled entities.

This page is the mechanics layer under the regime states defined in [[on-chain-regime]]; treat the metric definitions here as inputs, and the regime page as the rule set that maps metric combinations to actionable states.

---

## Trading Relevance

- On-chain data is uniquely transparent -- no equivalent exists in equities or forex where order flow is private
- Exchange flow data has historically provided early warnings before major selloffs (e.g., large BTC deposits to exchanges before [[crypto-winter|bear market]] legs down)
- Whale wallet monitoring enables traders to follow "smart money" positioning in real time
- Holder-behaviour metrics (SOPR, MVRV, dormancy) help distinguish profit-taking from capitulation, sharpening regime calls
- Miner metrics (reserves, hash ribbon) help time late-bear bottoms around [[bitcoin-halving]] supply shifts
- [[defi]] protocol metrics (TVL, borrowing rates, liquidation thresholds) provide actionable signals for both crypto-native and cross-market trades
- On-chain analysis is most effective for [[bitcoin]] and [[ethereum]] due to deeper data tooling; coverage for newer chains is improving

---

## Related

- [[on-chain-regime]] -- Maps these metrics into market states (this page is its mechanics reference)
- [[crypto-market-regime-taxonomy]] -- Broader crypto regime state machine
- [[whale-trade]] -- Trade-level playbook on large-holder activity
- [[bitcoin-halving]] -- Supply/miner-economics tie for miner metrics
- [[point-in-time-data]] -- Why on-chain backtests need restated-label discipline

---

## See Also

- [[blockchain]] -- The data source for on-chain analysis
- [[whale-trade]] -- Tracking large holder activity
- [[defi]] -- Protocol-level on-chain metrics
- [[bitcoin]] -- Most mature on-chain data ecosystem
