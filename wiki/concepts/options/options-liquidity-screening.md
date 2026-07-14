---
title: "Options Liquidity Screening"
type: concept
created: 2026-05-07
updated: 2026-07-14
status: good
tags: [options, derivatives, crypto, market-microstructure, liquidity, slippage]
markets: [crypto, options]
aliases: ["Options Liquidity Filter", "Options Bid-Ask Screening", "Tradeable Options Filter"]
domain: [options, market-microstructure]
prerequisites: ["[[options]]", "[[bid-ask-spread]]", "[[liquidity]]", "[[options-selection-framework]]"]
difficulty: intermediate
related:
  - "[[deribit]]"
  - "[[greeks-live]]"
  - "[[crypto-options-volatility-selling]]"
  - "[[bid-ask-spread]]"
  - "[[slippage]]"
  - "[[liquidity]]"
  - "[[options-selection-framework]]"
  - "[[strike-selection]]"
  - "[[expiration-selection]]"
  - "[[moneyness-selection]]"
  - "[[market-microstructure]]"
  - "[[clob]]"
  - "[[thinkorswim]]"
  - "[[spread-width-selection]]"
  - "[[delta]]"
  - "[[probability-of-profit]]"
  - "[[vix-calls]]"
---

**Options liquidity screening** is the first filter in the [[options-selection-framework]]: discarding contracts that cannot be entered and exited at fair prices. Liquidity matters more in options than in the underlying because options bid-ask spreads can dwarf the entire theta edge of a strategy. A "70%-PoP credit spread" on an illiquid contract is structurally a *negative* expected-value trade once round-trip slippage is priced in. In crypto this filter is even more decisive: the entire tradeable options universe is essentially **[[deribit|Deribit]] BTC and ETH** (~80-90% of open interest), with everything else thin to phantom — so screening is less about ranking thousands of names and more about knowing where the liquidity cliff is. The mechanics below are stated in their crypto form; the **Crypto specifics** section collects what differs from the equity-index version this page was first written for.

## Why Liquidity Matters

Three reasons options liquidity is more consequential than spot liquidity:

1. **Spreads are absolutely larger**. Spot bid-ask on BTC/ETH at a tier-1 venue is a handful of basis points. Options bid-ask on the same underlying runs several **vol points** — which on an OTM wing can be 5-15% of the contract's premium.
2. **Round-trips are unavoidable**. Many options structures must be closed before expiry (to capture early profit, roll, or de-risk before a catalyst). Each round-trip pays the bid-ask twice.
3. **Multi-leg structures multiply slippage**. A 4-leg iron condor pays bid-ask on every leg. Even with mid-price fills, slippage compounds — and on illiquid chains (any crypto name past BTC/ETH), mid-price fills are not achievable.

A short-premium strategy targeting 1.5%/month theta on a position must clear something like 0.5%/month in round-trip slippage to net the 1% the trader thinks they're earning. On illiquid contracts, slippage exceeds the theta target outright.

### Quick screen (pass all three to trade)

| Metric | Hard pass | Marginal | Skip |
|---|---|---|---|
| Bid-ask vs mid | ≤ 5% (≈ ≤ 3-4 vol pts on BTC/ETH wings) | 5-10% | > 10% |
| Open interest | ≥ 1,000 | 500-1,000 | < 500 |
| Daily volume | ≥ 100 | 10-100 | < 10 |

A contract must clear **all three** gates to be considered tradeable. A great-looking model trade on a strike that fails any gate is a worse trade than a mediocre one on a liquid strike, because the slippage tax is paid with certainty while the edge is only probabilistic. On crypto, the practical shortcut is: BTC/ETH monthlies clear all three comfortably; weeklies/dailies clear them near ATM only; alts rarely clear them at all.

## Bid-Ask Spread Thresholds

The single most important liquidity metric is the bid-ask spread on the specific contract being traded — and on crypto it is best read in **vol points**, because Deribit quotes and prices options off implied volatility.

### There is no penny pilot — there is one dominant venue

Crypto has no equivalent of the CBOE/OCC **Penny Pilot Program**, no NBBO, and no cross-exchange consolidation. Instead, liquidity is concentrated on a single central limit order book: **[[deribit|Deribit]]**, which holds ~80-90% of BTC/ETH options open interest. OKX and Binance run smaller options books; block flow crosses via the Paradigm RFQ network into Deribit. Tick sizes are set per-underlying by Deribit (e.g., $2.50-$5 increments on BTC premiums), not by a regulator.

On Deribit BTC/ETH, you should expect (in vol-point terms, which is how market makers quote):

- ATM contracts: ~1-2 vol points bid-ask
- 30-delta OTM: ~2-4 vol points
- 16-delta OTM: ~3-6 vol points
- Far OTM (5-10 delta): ~5-10 vol points

Anything wider signals you're either far from ATM, in a thin expiration (weekly/daily), or on an alt underlying. Because crypto trades **24/7**, there is no "off-hour" in the equity sense — but liquidity still thins in the low-activity Asian-overnight window and around the 08:00 UTC expiry settlement.

### Alts and off-cycle expiries

Past BTC and ETH, the picture degrades fast. SOL options on Deribit are tradeable but noticeably thinner (wider vol-point spreads, sparser strikes); other alt options are effectively phantom. Practical thresholds on a thin crypto chain:

- Near-ATM: 4-8 vol points is normal
- 16-delta OTM: 8-15 vol points
- Anything wider than ~10% of mid-premium: **skip**

### Universal Rule: 5% of Mid-Premium

Across all underlyings, if the bid-ask is wider than 5% of mid-premium, the contract is functionally untradeable for retail. Examples (premiums in USD, USDC-margined):

- Mid $100, bid $95 / ask $105 ($10 spread = 10%): **skip**
- Mid $250, bid $245 / ask $255 ($10 spread = 4%): tradeable
- Mid $50, bid $48 / ask $52 ($4 spread = 8%): **skip** unless it's a BTC/ETH ATM strike
- Mid $500, bid $495 / ask $505 ($10 spread = 2%): tradeable

For multi-leg structures, the *combined* mid-to-mid spread matters. A 4-leg iron condor where each leg carries 3 vol points of spread compounds into a meaningful round-trip slippage hit — on a thin credit, a large fraction of premium gone before the trade has decayed an hour.

### Liquidity tiers by underlying (crypto)

| Tier | Examples | Typical ATM bid-ask | Multi-leg fit |
|---|---|---|---|
| Tier 1 (deep crypto) | Deribit **BTC**, **ETH** monthlies | 1-2 vol pts | Any retail size; combos fill at/near mid; blocks via Paradigm |
| Tier 2 (shallower) | BTC/ETH weeklies & dailies near ATM | 2-5 vol pts | Standard retail multi-leg near ATM only |
| Tier 3 (thin) | Deribit **SOL**, far wings | 5-15 vol pts | Single-leg only; spreads risky |
| Tier 4 (phantom) | Most alt options, off-cycle expiries | > 15 vol pts / > 10% | **Avoid** — quotes are auto-fills, not markets |

Tier 1 (BTC/ETH) is where convex hedges — long [[dvol|DVOL]] expressions, protective BTC puts, and [[tail-risk-hedging|tail-risk]] wings — are actually executable at scale, which is why crypto hedging programs concentrate there. There is no crypto VIX-options product; DVOL is an index, not a listed option, so tail hedges are expressed directly in BTC/ETH puts and vol structures.

## Open Interest Minimums

**Open interest** (OI) is the count of outstanding contracts at a given strike/expiration. It indicates how many contracts could theoretically be closed without finding new buyers/sellers.

| OI level | Tradeable for | Notes |
|---|---|---|
| 5,000+ | Any strategy, multi-leg, large size | Penny-pilot ATM levels routinely |
| 1,000-5,000 | Standard retail multi-leg, 1-10 contracts | Adequate for entry and exit |
| 500-1,000 | Single-leg directional trades | Marginal for spreads; exit might require walking the price |
| 100-500 | Caution; consider only as part of a larger pre-existing position | Far OTM weeklies often live here |
| <100 | Skip | "Phantom strikes" — bids/asks displayed but no real market |

A common rule of thumb: **OI ≥ 1,000 for entry, OI ≥ 500 to plan a clean exit**. If OI is below this on the strike you want, move expirations or strikes; don't trade the illiquid contract because "the model says it's a great trade."

## Volume Minimums

**Daily volume** measures how many contracts traded today (or per session). Volume tends to be concentrated in 1-2 expirations and 5-10 strikes around ATM; far-OTM and far-dated strikes can have OI without daily volume.

| Volume (today, by close) | Strategy fit |
|---|---|
| 1,000+ | Day-trading, weekly options, scalps |
| 100-1,000 | Multi-day swing trades, standard 30-45 DTE entries |
| 10-100 | Position trades, willing to be patient on fills |
| <10 | Skip for active strategies |

A strike with high OI but low daily volume is "stale liquidity" — historical positions that may not be actively traded. Stale-OI strikes can fill, but the bid-ask is often wider than recent-volume strikes at the same delta.

## Common Illiquidity Traps

Specific situations where options chains *look* liquid but aren't:

### Far-OTM Weeklies / Dailies

The 5-delta weekly put on an alt (or an off-cycle BTC weekly) has tiny OI and a quote several vol points wide — a huge relative spread. The mid-price PoP looks attractive — "94% probability OTM" — but the realized fill is near the bid on entry, and exit is impossible without dumping the contract into a thin book. Net economics are negative.

### Deep ITM Long-Dated Options

A far-dated deep-ITM BTC call (90 delta) might show a tight *relative* spread, but the far end of the crypto curve carries thin OI and near-zero daily volume. Closing size will walk the book several vol points, and the trader will exit materially below the displayed mid. The problem is worst on ETH's long end and anything beyond BTC/ETH.

### Alt Underlyings With Low Option Volume

Most non-BTC/ETH tokens have option chains (where they exist at all) that trade only a handful of contracts daily. The chain might display credible-looking quotes, but those quotes are market-maker auto-fills that disappear (or widen dramatically) the moment a real order arrives.

**Rule**: if the underlying's average daily *option* volume across all strikes is under ~1,000 contracts, treat it as illiquid for options purposes regardless of how liquid its spot/perp is. In practice this rule excludes everything except BTC and ETH (SOL sits right at the margin).

### Off-Cycle Expirations

Deribit auto-lists a dense set of daily and weekly expiries; between the monthly (last-Friday) expiries, many of these rows show quotes but near-zero OI. They exist because the venue lists them, not because anyone trades them.

### Around Scheduled Catalysts

Pre-catalyst IV inflation (FOMC, CPI, a [[token-unlocks|token unlock]], an ETF-decision date, a major protocol upgrade) does not always come with proportional liquidity. Some events see option volume *spike* (good); others see liquidity *evaporate* as market makers widen quotes against binary/gap risk (bad). Because crypto trades 24/7, a catalyst can also land mid-move with no session break to cap it — always check bid-ask in real time at entry, not from a stale screen.

## Tools for Liquidity Screening

### Venue and Analytics Tools

- **[[deribit|Deribit]] order book / options chain** — the primary source of truth: live per-strike bid-ask, OI, and volume on the dominant venue. Because it is one CLOB, "the book" *is* the market.
- **[[greeks-live|Greeks.live]]** — the purpose-built crypto-options workbench: IV surface heatmap, per-strike liquidity, position Greeks, and the block-trade tape.
- **Paradigm** — the institutional RFQ/block-liquidity network that sources size (≥ 25 BTC / 200 ETH) off-screen and prints it to Deribit; checking recent block prints confirms where real size is trading.
- **Amberdata / Laevitas** — third-party crypto-derivatives analytics with chain-level OI, volume, and spread overlays across venues.

### Programmatic / Custom

For systematic strategies, pulling the chain via the Deribit API (and DVOL/surface via Deribit or Greeks.live) and filtering by OI/volume/vol-point-spread thresholds is standard. [[cryptodataapi|CryptoDataAPI]] provides the complementary aggregated options OI, volume, and [[max-pain]] series (see *Getting the Data* below).

## Slicing Large Multi-Leg Orders

For orders larger than a few contracts on the screen (size beyond what the top-of-book shows on BTC/ETH), filling all at once at mid is unrealistic. Standard tactics:

1. **Submit at mid first**, wait 30-60 seconds. If unfilled, walk the price a tick toward the bad-for-you side.
2. **Slice into 2-3 sub-orders** spaced 1-2 minutes apart. Market makers refresh quotes more aggressively when they see absorbed flow.
3. **Use the combo / spread order** rather than legging. Deribit routes a defined-leg structure (vertical, iron condor) as a single combo; legging in separately exposes you to mid-trade mispricing — sharper in crypto because spot can gap between legs at any hour.
4. **Route real size through Paradigm (RFQ), not the screen.** Deribit block minimums are 25 BTC / 200 ETH; the Paradigm network sources competing quotes off-book and prints the block to Deribit, avoiding the market impact of sweeping a thin visible book.
5. **Mind the 24/7 liquidity cycle** — there is no open/close, but books are thinnest in the Asian-overnight window and around the 08:00 UTC expiry; avoid working size then.

## Execution Structure: One Book, No NBBO, No PFOF

Crypto options execution is structurally simpler than US equity options — and the trader carries more of the burden:

- **No NBBO, no consolidation.** There is no National Best Bid and Offer and no Reg-NMS-style routing. Deribit is a single central limit order book; OKX and Binance run separate, smaller books. The best price is whatever that one venue's book shows — you cannot rely on a regulator-mandated consolidated quote.
- **No wholesaler price improvement / no PFOF.** There is no payment-for-order-flow layer routing your order to Citadel or Susquehanna for a fraction-of-a-tick improvement. You trade the book directly (or via Paradigm RFQ for size). What you see is what you get.
- **Best execution is on you.** The "my broker has best execution, so the bid-ask doesn't matter" myth has no crypto analog to hide behind — the bid-ask *is* the cost, in full, and it is wider (in vol-point terms) than penny-pilot equity options. Limit orders at mid, patience, and RFQ for size are the only levers.

The upshot: crypto's simpler microstructure removes the routing games but offers no price-improvement cushion, so the liquidity screen matters *more*, not less.

## Worked Example: Slippage Tax on Two Identical-Looking Trades

*Illustrative arithmetic, not a backtest.* Two traders each sell a 30-DTE put credit spread for a stated **$50 mid credit** on a $500-wide spread (USDC-margined). The only difference is liquidity.

**Trader A — deep crypto name (Deribit ETH monthly):**

- Per-leg bid-ask: ~2 vol points ≈ $2 of premium. Filling each leg ~$2 off mid.
- Round-trip slippage (enter + exit, 2 legs): ~$4.
- Net credit captured: $50 − $4 = **$46** (92% of theoretical).

**Trader B — thin alt option, low OI, ~8-vol-point leg bid-ask:**

- Each leg fills ~$7 off mid. Round-trip across 2 legs: ~$28.
- Net credit captured: $50 − $28 = **$22** (44% of theoretical).
- Worse: at exit, the thin book may have thinned further; the realistic exit fill could be at the bid, turning a "winner" into a scratch.

The *displayed* trade is identical (same delta, same width, same $50 mid). The realized economics differ by more than 2x purely from the liquidity gate. Over a year of monthly rolls, Trader B's slippage tax can exceed the entire [[theta]] edge the structure was designed to harvest — the page's central claim, made concrete. This is precisely why a crypto options book stays on BTC/ETH.

## Liquidity-Driven Strike Adjustments

When the strike chosen by [[strike-selection|delta convention]] is illiquid, the trader has three options:

1. **Move to a more liquid strike** (closer to ATM, where OI/volume cluster) and accept slightly different delta
2. **Move expiration** to one with better liquidity (often the next monthly)
3. **Skip the trade** — the strike's illiquidity is signaling that this particular expression of the strategy isn't economically viable

The wrong move: take the trade anyway because "the chain *has* a quote." A quote is not a fill.

## Crypto Specifics

The screening *logic* — bid-ask, OI, volume, all three as hard gates — is identical to equities. What changes is the market structure the gates operate on:

- **Two names, one venue.** The entire deep crypto options market is [[deribit|Deribit]] BTC and ETH. There is no penny-pilot list to expand your universe and no second deep venue to roll into — a concentration that is itself a liquidity risk (a Deribit outage during a vol event has no fallback).
- **Quote in vol points, not dollars.** Deribit prices off IV, so market makers quote and think in vol points. A "3-vol-point wing" is the crypto unit of bid-ask; converting to a % of premium is how you apply the universal 5% rule.
- **24/7, no NBBO, no PFOF.** Continuous trading means no open/close liquidity pattern but continuous gap risk; a single CLOB with no consolidated quote and no wholesaler price improvement means the visible bid-ask is the full, un-cushioned cost. Size trades via Paradigm RFQ (25 BTC / 200 ETH block minimums).
- **Settlement helps.** Deribit options are cash-settled to a Deribit index — no physical assignment and minimal pin risk, so you are never forced to close purely to avoid delivery. That removes one class of forced round-trip that equity/US-single-stock traders face.
- **Alts are a liquidity trap.** SOL is marginal; everything past it is phantom. Treat the "does this chain even trade?" question as the first gate, because for most tokens the answer is no.

## Getting the Data (CryptoDataAPI)

Per-strike bid-ask lives on the [[deribit|Deribit]] book and [[greeks-live|Greeks.live]]. [[cryptodataapi|CryptoDataAPI]] provides the aggregated options OI, volume, and [[max-pain]] context plus the spot/perp depth that tells you whether the *underlying* can absorb your delta hedges.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (positioning + activity screen)
- `GET /api/v1/liquidity/depth` — per-coin spot depth/spread at 10/25/50/100 bps (can you hedge the delta?)
- `GET /api/v1/liquidity/depth/{coin}` — 24h rolling depth history for the underlying

**Historical data:**
- `GET /api/v1/backtesting/klines` — deep OHLCV archive for modeling realized round-trip costs

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; liquidity-depth detail on [[cryptodataapi]].

## Related

- [[bid-ask-spread]] — the dominant cost on illiquid options
- [[slippage]] — realized cost beyond bid-ask
- [[liquidity]] — general concept
- [[options-selection-framework]] — liquidity is filter 1
- [[strike-selection]] — strike choice constrained by liquidity
- [[expiration-selection]] — DTE choice constrained by liquidity
- [[moneyness-selection]] — moneyness choice constrained by liquidity
- [[market-microstructure]] — broader context for order-book execution
- [[clob]] — central limit order book mechanics (Deribit is one)
- [[deribit]], [[greeks-live]] — the venue and analytics workbench for crypto options
- [[spread-width-selection]] — wider spreads less punished by per-contract slippage
- [[probability-of-profit]] — the metric slippage silently erodes
- [[crypto-options-volatility-selling]] — the strategy this liquidity screen gates
- [[dvol]] — Tier-1 (BTC/ETH) is where convex/vol hedges are executable

## Sources

- [[deribit|Deribit]] / [[greeks-live|Greeks.live]] / Paradigm documentation — crypto options venue structure, block minimums (25 BTC / 200 ETH), vol-point quoting, cash settlement
- CBOE / OCC — Penny Pilot Program and minimum-tick rules (the equity-microstructure contrast crypto lacks)
- SEC Rule 611 (Reg NMS) — NBBO consolidation and order routing (again, no crypto analog)
- Euan Sinclair, *Positional Option Trading* (Wiley) — transaction-cost modeling for options strategies (ports directly to crypto)
