---
title: "Put-Call Parity Arbitrage (Crypto)"
type: strategy
created: 2026-04-24
updated: 2026-07-19
status: good
tags: [arbitrage, options, crypto, derivatives, quantitative, volatility]
aliases: ["Conversion Arbitrage", "Reversal Arbitrage", "Box Spread", "Crypto Put-Call Parity Arbitrage"]
strategy_type: quantitative
timeframe: intraday
markets: [crypto, options]
complexity: advanced
backtest_status: untested
edge_source: [structural, analytical]
edge_mechanism: "Deribit options flow does not continuously enforce parity against the perp/futures curve; funding spikes, thin weekly/alt option books, and new-expiry listings let a locked conversion/reversal earn a rate above the funding-implied forward."
crowding_risk: high
decay_evidence: "BTC/ETH monthly parity holds tight as options desks arbitrage it; residual edge concentrates in funding-spike windows, thin alt/weekly options, and new expiries before market makers adjust."
related: ["[[arbitrage]]", "[[put-call-parity]]", "[[synthetic-long]]", "[[cash-and-carry]]", "[[funding-rate]]", "[[perpetual-futures]]", "[[deribit]]", "[[greeks-live]]", "[[box-spread]]", "[[volatility-arbitrage]]", "[[limits-to-arbitrage]]", "[[cryptodataapi]]"]
---

# Put-Call Parity Arbitrage (Crypto)

Put-call parity is a no-arbitrage identity linking a European call, a European put, the underlying, and financing: **C − P = S − K·e^(−rT)**, where C and P are the call and put at strike K, S is spot, r is the financing rate to expiry, and T is time to expiry. In equities the right-hand side also subtracts the present value of dividends; **in crypto there is no dividend stream, and the financing rate r is set by [[perpetual-futures|perp]] [[funding-rate|funding]] and the dated-futures basis** — funding *is* the crypto "rate" that prices the identity (a staked asset's yield can act like a small dividend, but the spot/perp legs used to arbitrage rarely capture it). When the identity is violated beyond costs, a trader locks a return by buying the cheap side and selling the rich side: a **conversion** (long spot/perp + long put + short call) or a **reversal** (short spot/perp + short put + long call). See [[put-call-parity]] for the identity and [[synthetic-long]] for the call+put synthetic that the arbitrage prices against the perp.

On [[deribit]], where BTC/ETH options are **European and cash-settled at 08:00 UTC**, the parity relationship is unusually clean: there is **no early-exercise value and no assignment risk** — the two biggest complications of American equity parity arbitrage simply do not exist. The crypto edge instead lives in the **options-implied forward versus the perp/futures curve**: funding spikes (crowded longs bid the synthetic forward), thin weekly and alt-coin option books, and freshly listed expiries before desks tighten them.

## The parity identity and its synthetic equivalences

Parity is a *constraint*; rearranging it exposes equivalences where the same payoff is priced two ways. In crypto the "stock" leg is **spot or the perp**.

| Synthetic position | Replication (same K, T) | Crypto use case |
|---|---|---|
| Synthetic long | long call + short put | Long exposure vs. paying perp funding — see [[synthetic-long]] |
| Synthetic short | short call + long put | Short exposure to a dated expiry (no floating funding) |
| Conversion (lend) | long spot/perp + long put + short call | Lend USD at the implied box rate |
| Reversal (borrow) | short spot/perp + short put + long call | Borrow USD at the implied box rate |
| [[box-spread|Box spread]] | conversion at K1 + reversal at K2 | Synthetic USD loan/deposit between two strikes, funding-linked |

The **box spread** pays exactly `K2 − K1` at expiry regardless of spot, so it is a synthetic zero-coupon USD bond whose price implies a financing rate — in crypto, one that competes with (and is anchored to) perp funding and dated-futures basis.

## Edge source

**Structural** and **analytical**. The structural component: the four legs — call, put, spot, perp/future — trade with different frictions (funding, exchange margin, index-settlement timing, single-venue concentration on Deribit). The analytical component: correctly pricing the **funding-implied forward** and the futures basis so you can spot when the listed chain is out of line with a properly adjusted parity relationship. See [[edge-taxonomy]].

## Why this edge exists

Retail and directional flow lift Deribit calls/puts without simultaneously enforcing parity against the perp curve. When funding spikes (crowded longs), the options-implied forward can dislocate from the perp/futures price; on thin weekly or alt-coin books a single aggressive order moves one leg without the synthetic being repriced; and newly listed expiries trade loosely before market-maker desks tighten them. The counterparty on a conversion is typically a directional buyer who lifted a rich call, or a basis-taker who paid up for synthetic long exposure rather than hold the perp. Violations *persist* only to the extent of the [[limits-to-arbitrage]] that bind the four-leg box in crypto: capital intensity of holding a near-zero-return position to expiry, **single-venue and counterparty risk** (Deribit concentration; exchange solvency), **liquidation risk on the perp leg** if the hedge is perp-based and margin is thin, and **index-settlement / pin uncertainty** in the final hours.

## Null hypothesis

Under no-edge conditions, parity holds exactly after adjusting for (i) the funding/basis-implied forward, (ii) round-trip exchange and settlement fees, (iii) the half-spread on each of the four legs, and (iv) perp-leg funding carry and margin cost over the hold. If a conversion/reversal scanner only ever finds "violations" inside that stack, there is no edge — you are measuring transaction cost, not alpha.

## Rules

**Entry**
1. **Scan the Deribit chain** for each expiry where a call and put share a strike.
2. **Compute the residual**: `residual = (C − P) − (S − K·e^(−rT))`, with **r derived from perp funding / futures basis**, not a T-bill rate.
3. **Check both directions**: residual > threshold + costs → **conversion** (long spot/perp, long put, short call); residual < −threshold − costs → **reversal**.
4. **Threshold** = exchange + settlement fees + half the bid-ask on each leg + a buffer for index-settlement/pin uncertainty and expected perp-leg funding.
5. **Execute as a package** where possible (combo/RFQ via [[greeks-live]]); do not leg into thin books.
6. **Hold to 08:00 UTC expiry** — European cash settlement self-liquidates the box with no assignment.

**Exit**
- **Passive expiry**: the box settles to `K2 − K1` (or the strike pins the conversion payoff) against the Deribit index.
- **Early unwind** if the dislocation reverts sooner for a smaller-but-faster capture.
- **Manage the perp leg**: keep margin headroom so a DVOL/price spike does not liquidate the hedge before convergence.

**Position sizing** — size by the lesser of margin capacity (including perp-leg maintenance margin), option open interest at the strike, and single-venue concentration limits. Risk-free in theory, capital-intensive in practice.

## Example trade

**Setup (illustrative, funding-spike conversion).** BTC spot $60,000; perp funding spikes hard positive (crowded longs), lifting the options-implied 30-day forward to ~$60,900 while the reversal/conversion residual on the Deribit chain leaves the call rich versus the funding-implied forward.

- 30-day $60,000 call: $3,900
- 30-day $60,000 put: $2,850
- Synthetic (C − P) = $1,050; funding-implied `S − K·e^(−rT)` ≈ $760 → residual ≈ **+$290 rich on the call side**.
- **Conversion**: long 1 BTC (spot or perp), buy the $60,000 put at $2,850, sell the $60,000 call at $3,900.
- At 08:00 UTC expiry the strike pins the payoff: the long-coin + long-put + short-call box settles to the $60,000 strike, locking the ~$290 residual **minus** the four legs' costs and any funding paid/earned on the coin/perp leg over the hold.

On thin weekly or alt-coin options the residual can be far wider — but so are the spreads and the counterparty/liquidation risks, which is where the net edge is usually eaten.

## Cost-aware residual decomposition (illustrative)

Naive scanners overstate the edge because the *raw* residual must survive a stack of frictions:

| Component | Effect on a quoted 40 bp residual | Notes |
|---|---|---|
| Headline quoted residual | +40 bp | What a naive `C − P − (S − Ke^-rT)` scan reports |
| Half bid-ask on 4 legs | −15 to −30 bp | Mid quotes are not executable; thin books widen this |
| Exchange + settlement fees (4 legs) | −3 to −8 bp | Per-contract Deribit fees ×4, plus settlement |
| Perp-leg funding carry over the hold | −10 to +10 bp | Funding can help or hurt; a spike is often *why* the edge appeared |
| Index-settlement / pin buffer | −1 to −5 bp | Deribit settles to a time-averaged index, not a single print |
| **Net realizable edge** | **often <5 bp, sometimes negative** | Size off this, never the headline |

## What kills this strategy

1. **Options market makers** running the same scan against the perp curve at lower latency.
2. **Funding reversals** — the spike that opened the dislocation collapses (or flips) before convergence.
3. **Perp-leg liquidation** — a sharp move liquidates a thinly-margined hedge, breaking the "locked" box.
4. **Single-venue / counterparty risk** — Deribit concentration; an exchange outage or solvency event with capital tied up in the box.
5. **Index-settlement quirks / pin** near expiry if spot sits at the strike.

## Kill criteria

- Rolling 30-day average net edge per box < fees + 2 bps.
- Any perp-leg liquidation or forced unwind loss > 3× expected per-trade profit.
- Funding volatility so high that the forward cannot be pinned over the hold.
- Exchange margin/withdrawal change that raises capital lock-up materially without a matching return.

## Advantages

- **Market-neutral** — no directional exposure when the box is complete.
- **Mathematically verifiable** — the funding-adjusted identity either holds or it does not.
- **No early-exercise or assignment risk** — Deribit's European cash settlement makes the crypto box *cleaner* than the American equity version.
- **Self-liquidating** at 08:00 UTC expiry.

## Disadvantages

- **Capital-intensive** — large notional for small absolute returns.
- **Single-venue concentration** — most BTC/ETH options liquidity is on Deribit; counterparty/outage risk is real.
- **Perp-leg liquidation risk** — a hedge that can be margin-called is not truly "locked."
- **Funding is volatile** — the crypto "rate" moves far more than a rates curve, so the forward adjustment is noisier.
- **Thin alt/weekly books** — the widest apparent edges sit exactly where spreads and slippage eat them.

## Getting the Data (CryptoDataAPI)

The Deribit chain and the options-implied forward come from Deribit / [[greeks-live]]. [[cryptodataapi|CryptoDataAPI]] supplies the **funding / basis** that sets the crypto "rate" `r` in the parity identity, plus the positioning and historical funding used to model and backtest the dislocation:

- **Funding — the rate that prices the forward** — `GET /api/v1/derivatives/funding-rates?coin=BTC` (cross-exchange). See [[cryptodataapi-derivatives]].
- **Open interest — basis / positioning context** — `GET /api/v1/derivatives/open-interest?coin=BTC`. See [[cryptodataapi-derivatives]].
- **Options OI / max pain — chain positioning near expiry** — `GET /api/v1/market-intelligence/options`. See [[cryptodataapi-market-intelligence]].
- **Historical funding — for basis/parity backtests** — `GET /api/v1/backtesting/funding`. See [[cryptodataapi-backtesting]].

The option prices, implied forward, and DVOL are Deribit / Greeks.live, not CryptoDataAPI.

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/derivatives/funding-rates?coin=BTC"
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

**Live dashboards:** [funding rates](https://cryptodataapi.com/funding-rates) · [liquidations](https://cryptodataapi.com/liquidations) · [open interest](https://cryptodataapi.com/open-interest) · [short-term regimes](https://cryptodataapi.com/market-regimes)

### AI agent workflow

An AI agent connected to the [[cryptodataapi-mcp|CryptoDataAPI MCP]] can run the rate/positioning half of this strategy (the options chain itself comes from Deribit):

- **Rate input** — `GET /api/v1/derivatives/funding-rates?coin=BTC` supplies the funding rate that replaces `r` in the parity identity; recompute the funding-adjusted forward each cycle and compare it against the Deribit synthetic to flag violations.
- **Chain positioning** — `GET /api/v1/market-intelligence/options` (BTC OI, volume, max pain) shows where expiry pinning pressure sits — apparent parity violations near heavy-OI strikes into expiry are often real dealer flow, not free money.
- **Regime gate** — `GET /api/v1/volatility/regime/score`: enter boxes/conversions when vol stress is low; in `vol_shock` conditions the perp-leg liquidation risk dominates the locked spread. Cross-check `GET /api/v1/quant/market`.
- **Backtest** — `GET /api/v1/backtesting/funding` (Hyperliquid hourly since 2023-05; Binance daily since 2026-03-30) reconstructs the historical funding-implied forward; options-chain history must come from Deribit. Pair with `/api/v1/backtesting/daily-snapshots` (since 2026-03-02) for point-in-time context.
- **Tips** — funding is the noisiest term in crypto parity: use a funding TWAP over the option's remaining life, not the instantaneous print, when sizing an apparent violation.

## Sources

- Hans Stoll (1969), *The Relationship Between Put and Call Option Prices*, *Journal of Finance* — the original parity paper
- Hull, J., *Options, Futures, and Other Derivatives* — parity derivation and forward pricing
- Natenberg, S., *Option Volatility and Pricing* — conversions, reversals, boxes from the market-maker's seat
- [[deribit]] / [[greeks-live]] documentation — European cash settlement, combos/RFQ, index settlement

## Related

- [[arbitrage]] — parent concept
- [[put-call-parity]] — the no-arbitrage identity this strategy enforces
- [[synthetic-long]] — the call+put synthetic priced against the perp; the reversal/basis-capture counterpart
- [[cash-and-carry]] — the spot-vs-futures basis trade that shares the funding/forward machinery
- [[funding-rate]] / [[perpetual-futures]] — the crypto "rate" and the leg used to arbitrage parity
- [[box-spread]] — the four-legged synthetic USD loan/deposit
- [[volatility-arbitrage]] — trades the same chain but on IV, not parity
- [[limits-to-arbitrage]] — why crypto parity violations persist at all
- [[deribit]] / [[greeks-live]] — venue and analytics
