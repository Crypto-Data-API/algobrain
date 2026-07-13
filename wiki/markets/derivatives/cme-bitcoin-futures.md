---
title: "CME Bitcoin & Ether Futures"
type: market
created: 2026-05-16
updated: 2026-06-20
status: good
tags: [crypto, futures, bitcoin, derivatives, market-microstructure]
aliases: ["CME BTC Futures", "CME ETH Futures", "CME Crypto Futures", "BTC Futures", "MBT", "MET"]
related: ["[[cme]]", "[[cme-group]]", "[[perpetual-futures]]", "[[basis-trade]]", "[[crypto-trading-sessions]]", "[[crypto-weekday-weekend-etf-era]]", "[[session-overlap-liquidity]]", "[[btc-weekend-effect]]", "[[bitcoin-etfs]]", "[[coinbase-prime]]"]
---

CME Bitcoin and Ether futures are cash-settled, USD-denominated futures contracts listed on the [[cme-group|CME]] Globex platform. They are the primary regulated US institutional venue for BTC and ETH derivatives exposure, and the basis between CME futures and offshore [[perpetual-futures|perpetuals]] is a live, real-time cross-venue stress measure used by traders to read institutional vs. crypto-native positioning (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## Contract Family

CME lists a family of crypto contracts:

- **Bitcoin Futures (BTC)** — standard contract
- **Micro Bitcoin Futures (MBT)** — smaller contract size for retail and finer hedging
- **Ether Futures (ETH)** — standard ETH contract
- **Micro Ether Futures (MET)** — smaller ETH contract

All are cash-settled in USD against CME CF reference rates, so there is no physical bitcoin or ether delivery. CME also offers options on these futures.

### Contract Specifications (General)

The two contract sizes serve different participants. The standard contract is institutional-scale; the micro is sized for retail and for fine-grained hedging. Exact contract sizes, tick values, and margin requirements are set by CME and change over time, so the table below describes the *structure* rather than fixed numbers — always confirm current specs on the CME contract pages before trading.

| Feature | Standard (BTC / ETH) | Micro (MBT / MET) |
|---|---|---|
| Relative size | Large institutional unit | A fraction of the standard contract |
| Settlement | Cash, USD, vs CME CF reference rate | Cash, USD, vs CME CF reference rate |
| Physical delivery | None | None |
| Typical user | Funds, ETF APs, institutional desks | Retail, precise hedge ratios, smaller books |
| Listing cycle | Monthly expiries plus nearer-dated listings | Same cycle as the standard contract |
| Expiry / settlement timing | Last Friday of the contract month (CME calendar) | Same convention as the standard contract |

**Cash settlement.** Because the contracts settle to a USD reference rate (the CME CF Bitcoin Reference Rate / Ether Reference Rate) rather than delivering coin, there is no custody, wallet, or on-chain settlement risk for the futures position itself. This is one of the main reasons regulated US institutions prefer CME over offshore venues.

**Margin.** CME futures are margined products: traders post initial margin and maintain maintenance margin, marked to market daily. Crypto futures carry materially higher margin percentages than, say, equity-index futures because of the underlying's volatility. Micro contracts let smaller traders hold positions whose margin would be impractical at standard-contract size. Specific margin figures are set by CME risk management and revised with volatility — do not assume a fixed number.

**Options.** CME also lists options on the BTC and ETH futures, enabling defined-risk and volatility strategies on a regulated, cleared venue.

## Contract Hours

CME crypto futures trade Sunday 17:00 CT through Friday 16:00 CT on CME Globex, with a 60-minute daily break (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]). This is distinct from the 24/7 spot and perpetual markets — the regulated US derivatives anchor goes dark for a portion of each weekday and for the full weekend.

## Why Hours Matter

The CME schedule concentrates institutional hedging and price discovery into US-centric weekday hours. This has several intraday-trading consequences:

1. **Liquidity anchoring** — CME open and the LNY overlap (see [[session-overlap-liquidity]]) both fall in the same broad window, reinforcing the US-session liquidity peak documented in [[crypto-weekday-weekend-etf-era]]
2. **Hedging cliff** — when CME closes for the daily break or the weekend, US institutional hedging stops, but offshore perp exposure continues
3. **Basis stress** — the spread between CME futures and offshore perps becomes more reactive in off-hours because one leg of the trade is unavailable for hedging

## Basis as a Signal

The CME-vs-offshore basis (typically CME futures minus Binance/Bybit/OKX perp price, annualized) is widely used as a positioning signal:

- **Contango** (CME > spot/perp) — usually indicates institutional demand for long exposure via the regulated venue; persistent steep contango is a setup for [[basis-trade|cash-and-carry basis trades]]
- **Backwardation** (CME < spot/perp) — relatively rare; often signals stress, forced de-risking, or extreme offshore-perp speculation
- **Basis widening into stress** — a sudden widening or inversion of CME-vs-perp basis often precedes or accompanies offshore-leveraged liquidation cascades

Because CME contracts are cash-settled and hedged by professional market makers, the basis tends to compress as expiry approaches; the steady-state level is set by the cost of carry, financing rates, and the demand imbalance between institutional and crypto-native participants.

## The CME Gap

The Friday 16:00 CT close to Sunday 17:00 CT reopen creates a structural gap window. Spot and perpetual markets continue trading 24/7 over the weekend; CME does not. When the perp/spot price moves materially over the weekend, the CME chart opens with a visible gap that traders watch as a magnet for subsequent price action — the well-known "CME gap" phenomenon noted in [[btc-weekend-effect]].

The gap is not a guaranteed fill (the empirical hit rate is not 100% and depends on horizon), but it is a widely watched intraday/swing reference because:

- A large unfilled CME gap implies a basis dislocation between regulated and unregulated venues
- Market makers hedging across CME and offshore have a mechanical incentive to push price back into the gap when CME reopens
- Many algorithmic and discretionary traders treat the gap level as a magnet, which can be a self-fulfilling pattern

## Why CME Futures Matter for the Wider Crypto Market

Despite being smaller than offshore perps by raw volume, CME futures are disproportionately important because:

1. They are the only regulated US venue institutional desks can use without operational headaches around offshore counterparties
2. ETF authorized participants and market makers often hedge primary-market ETF flow through CME, linking [[bitcoin-etfs]] activity directly into the futures curve via [[coinbase-prime]] custody
3. Price discovery in US hours, especially around macro releases, frequently leads spot — and CME is the cleanest read on that
4. CME settlement prices feed into reference rates used elsewhere in the institutional ecosystem

## How Traders Use CME Crypto Futures

CME crypto futures support several distinct use cases:

1. **Directional exposure with regulated clearing.** Funds and desks that cannot or will not face offshore counterparties take long or short [[bitcoin]]/ETH exposure on a cleared, USD-margined venue. The micro contracts (MBT/MET) let smaller accounts do the same at finer granularity.
2. **Cash-and-carry [[basis-trade|basis trades]].** When CME futures trade in [[contango]] above spot, a desk can buy spot (or a spot [[bitcoin-etfs|ETF]]) and sell the CME future, locking the basis as a financing-like return that converges to zero at expiry. This is one of the largest institutional crypto trades and a primary driver of ETF/futures linkage.
3. **Hedging spot and ETF inventory.** ETF authorized participants and market makers hedge primary-market creation/redemption flow through CME, often custodied via [[coinbase-prime]] — tying [[bitcoin-etfs]] activity directly into the futures curve.
4. **Reading positioning via basis and the CME gap.** As covered above, the CME-vs-perp basis and the weekend [[btc-weekend-effect|CME gap]] are watched as cross-venue stress and positioning signals.
5. **Defined-risk and volatility trades** via the listed options on the futures.

## Relation to Spot, Perpetuals, and ETFs

CME futures sit at the regulated center of a wider structure:

- **Versus spot.** Spot [[bitcoin]] trades 24/7 across many venues; CME futures track the CME CF reference rate but go dark nights and weekends, which is what creates the [[btc-weekend-effect|CME gap]].
- **Versus offshore [[perpetual-futures|perpetuals]].** Perps (Binance/Bybit/OKX) run continuously with funding-rate mechanics; CME futures have a fixed expiry and cash settlement. The CME-minus-perp basis is the headline cross-venue signal described above.
- **Versus spot [[bitcoin-etfs|ETFs]].** The launch of US spot ETFs deepened the linkage: ETF flow is frequently hedged through CME, so futures open interest and the futures basis now partly reflect ETF primary-market activity (Source: [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]).

## Related

- [[cme]] — exchange overview
- [[cme-group]] — parent exchange group
- [[futures]] — the broader instrument class
- [[bitcoin]] — the underlying asset
- [[perpetual-futures]] — the 24/7 offshore product CME futures basis is measured against
- [[basis-trade]] — cash-and-carry strategies exploiting the CME-vs-spot/perp spread
- [[contango]] — the curve shape that powers the cash-and-carry trade
- [[crypto-trading-sessions]] — Asia/London/NY hub
- [[crypto-weekday-weekend-etf-era]] — the institutional-era structural shift CME helps anchor
- [[session-overlap-liquidity]] — LNY overlap dominance
- [[btc-weekend-effect]] — Friday-close to Sunday-open gap phenomenon
- [[bitcoin-etfs]] — the spot ETF complex that hedges through CME
- [[coinbase-prime]] — the custodian whose ETF flows feed back into CME hedging demand

## Sources

- [[2026-04-22-gap-finder-crypto-intraday-session-liquidity-effect]]
