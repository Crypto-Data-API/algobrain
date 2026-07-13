---
title: "Options Liquidity Screening"
type: concept
created: 2026-05-07
updated: 2026-06-21
status: excellent
tags: [options, derivatives, market-microstructure, liquidity, slippage]
aliases: ["Options Liquidity Filter", "Options Bid-Ask Screening", "Tradeable Options Filter"]
domain: [options, market-microstructure]
prerequisites: ["[[options]]", "[[bid-ask-spread]]", "[[liquidity]]", "[[options-selection-framework]]"]
difficulty: intermediate
related:
  - "[[bid-ask-spread]]"
  - "[[slippage]]"
  - "[[liquidity]]"
  - "[[unusual-whales]]"
  - "[[options-selection-framework]]"
  - "[[strike-selection]]"
  - "[[expiration-selection]]"
  - "[[moneyness-selection]]"
  - "[[market-microstructure]]"
  - "[[clob]]"
  - "[[thinkorswim]]"
  - "[[tastytrade]]"
  - "[[interactive-brokers]]"
  - "[[tradestation]]"
  - "[[spread-width-selection]]"
  - "[[delta]]"
  - "[[probability-of-profit]]"
  - "[[vix-calls]]"
  - "[[spx-puts]]"
---

**Options liquidity screening** is the first filter in the [[options-selection-framework]]: discarding contracts that cannot be entered and exited at fair prices. Liquidity matters more in options than in stocks because options bid-ask spreads can dwarf the entire theta edge of a strategy. A "70%-PoP credit spread" on an illiquid contract is structurally a *negative* expected-value trade once round-trip slippage is priced in.

## Why Liquidity Matters

Three reasons options liquidity is more consequential than equity liquidity:

1. **Spreads are absolutely larger**. Equity bid-ask on a $50 stock might be $0.01 — 0.02% of price. Options bid-ask on the same name might be $0.10-$0.25 — 5-15% of an OTM contract's premium.
2. **Round-trips are unavoidable**. Many options structures must be closed before expiry (to avoid assignment, capture early profit, or roll). Each round-trip pays the bid-ask twice.
3. **Multi-leg structures multiply slippage**. A 4-leg iron condor pays bid-ask on every leg. Even with mid-price fills, slippage compounds — and on illiquid chains, mid-price fills are not achievable.

A short-premium strategy targeting 1.5%/month theta on a position must clear something like 0.5%/month in round-trip slippage to net the 1% the trader thinks they're earning. On illiquid contracts, slippage exceeds the theta target outright.

### Quick screen (pass all three to trade)

| Metric | Hard pass | Marginal | Skip |
|---|---|---|---|
| Bid-ask vs mid | ≤ 5% (≤ $0.05 penny-pilot) | 5-10% | > 10% |
| Open interest | ≥ 1,000 | 500-1,000 | < 500 |
| Daily volume | ≥ 100 | 10-100 | < 10 |

A contract must clear **all three** gates to be considered tradeable. A great-looking model trade on a strike that fails any gate is a worse trade than a mediocre one on a liquid strike, because the slippage tax is paid with certainty while the edge is only probabilistic.

## Bid-Ask Spread Thresholds

The single most important liquidity metric is the bid-ask spread on the specific contract being traded.

### Penny Pilot Program

The CBOE / OCC **Penny Pilot Program** designates a list of high-volume tickers where market-makers are required to quote in $0.01 increments (rather than the $0.05 default). Penny-pilot names quote tighter bid-ask:

- SPY, QQQ, IWM, DIA, EFA, EEM
- AAPL, MSFT, NVDA, TSLA, AMZN, GOOGL, META, NFLX
- A rolling list of ~250-400 underlyings updated periodically

On penny-pilot tickers, you should expect:

- ATM contracts: $0.01-0.03 bid-ask
- 30-delta OTM: $0.02-0.05
- 16-delta OTM: $0.03-0.10
- Far OTM (5-10 delta): $0.05-0.15

Anything wider on a penny-pilot name signals that you're either far from ATM, in an illiquid expiration, or trading at an off-hour.

### Non-Penny-Pilot Names

Outside the penny pilot, the minimum tick is $0.05 (for contracts under $3) or $0.10 (above $3). Practical thresholds:

- ATM: $0.05-0.15 bid-ask is normal
- 30-delta OTM: $0.10-0.20
- 16-delta OTM: $0.15-0.30
- Anything beyond $0.30 absolute or > 5% of mid-price: **skip**

### Universal Rule: 5% of Mid-Price

Across all underlyings, if the bid-ask is wider than 5% of mid-price, the contract is functionally untradeable for retail. Examples:

- Mid $1.00, bid $0.95 / ask $1.05 ($0.10 spread = 10%): **skip**
- Mid $2.50, bid $2.45 / ask $2.55 ($0.10 spread = 4%): tradeable
- Mid $0.50, bid $0.48 / ask $0.52 ($0.04 spread = 8%): **skip** unless penny pilot
- Mid $5.00, bid $4.95 / ask $5.05 ($0.10 spread = 2%): tradeable

For multi-leg structures, the *combined* mid-to-mid spread matters. A 4-leg iron condor where each leg has $0.05 bid-ask carries an effective $0.20 round-trip slippage hit (4 legs × $0.05). On a $1.50 credit, that's 13% of premium gone before the trade has decayed an hour.

### Liquidity tiers by underlying

| Tier | Examples | Typical ATM bid-ask | Multi-leg fit |
|---|---|---|---|
| Tier 1 (index/mega-cap) | [[spy\|SPY]], [[sp500\|SPX]], QQQ, AAPL, NVDA, TSLA | $0.01-0.03 | Any size; combos fill at/near mid |
| Tier 2 (large-cap penny-pilot) | Most S&P 500 names | $0.03-0.10 | Standard retail multi-leg |
| Tier 3 (mid-cap, non-penny-pilot) | Many Russell 2000 names | $0.10-0.30 | Single-leg only; spreads risky |
| Tier 4 (thin / phantom) | Micro-caps, off-cycle weeklies | > $0.30 / > 10% | **Avoid** — quotes are auto-fills, not markets |

Tier 1 names are where convex hedges such as [[vix-calls|VIX calls]], [[vix-call-spreads|VIX call spreads]], and [[spx-puts|SPX puts]] are actually executable at scale — a key reason tail-hedging programs concentrate there.

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

### Far-OTM Weeklies

The 5-delta weekly put on a mid-cap stock has an OI of 50 and a $0.05/$0.20 quote ($0.15 bid-ask, mid = $0.125 = 120% relative spread). The mid-price PoP looks attractive — "94% probability OTM, $12.50 credit per contract" — but the realized fill is $0.05 entry, and exit is impossible without dumping the contract at the bid. Net economics are negative.

### Deep ITM Long-Dated Options

A 12-month deep-ITM call (90 delta) on a mid-cap stock might have $0.50 bid-ask on a $30 contract — only 1.7% relative spread, looks fine. But OI is 200 and daily volume is 5. Closing 50 contracts will move the bid by $1+, and the trader will exit at materially below the displayed mid.

### Single-Name Names With Low Option Volume

Many S&P 500 names — particularly mid-caps in less-traded sectors — have option chains that exist nominally but trade only a handful of contracts daily. The chain might display credible-looking quotes, but those quotes are market-maker auto-fills that disappear (or widen dramatically) the moment a real order arrives.

**Rule**: if the underlying's average daily *option* volume across all strikes is under 1,000 contracts, treat the name as illiquid for options purposes regardless of equity liquidity.

### Off-Cycle Expirations

Between monthly expirations, weeklies on non-penny-pilot names often have 1-2 strike rows with quotes but near-zero OI. These are listed because the exchange auto-lists, not because anyone trades them.

### Around Earnings

Earnings-week IV inflation does not always come with proportional liquidity. Some names see option volume *spike* into earnings (good), but others see liquidity *evaporate* as market makers widen quotes against binary risk (bad). Always check bid-ask in real time the day of trade entry, not from a stale screen.

## Tools for Liquidity Screening

### Broker Built-Ins

- **[[thinkorswim|ThinkOrSwim]] Options Hacker** — scans the universe by OI, volume, IV rank, delta with custom filters. The de facto standard for retail.
- **[[tastytrade]] platform** — surfaces "liquidity score" alongside IV rank for scanned underlyings.
- **TradeStation RadarScreen** — column-based scanner with OI, volume, bid-ask filters for options. EasyLanguage allows custom liquidity formulas.
- **[[interactive-brokers|Interactive Brokers] Options Trader / Strategy Builder** — institutional-grade OI/volume display per strike with NBBO highlighting.

### Third-Party Flow Tools

- **[[unusual-whales]]** — flow scanner that includes bid-ask, OI, and volume on individual prints. Useful for confirming a strike is actively traded before entering.
- **OptionAlert, FlowAlgo, BlackBoxStocks** — competing flow scanners with similar liquidity overlays.
- **OptionStrat** — visualizes option chains with built-in liquidity color-coding by bid-ask width.

### Spreadsheets / Custom

For systematic strategies, downloading the chain via the broker API and filtering by OI/volume/spread thresholds programmatically is standard. IBKR's TWS API, TradeStation's WebAPI, and Tradier's API all expose chain-level liquidity data.

## Slicing Large Multi-Leg Orders

For orders larger than 5-10 contracts on most names (or 50+ on SPY/SPX), filling all at once at mid is unrealistic. Standard tactics:

1. **Submit at mid first**, wait 30-60 seconds. If unfilled, walk price by $0.05 toward the bad-for-you side.
2. **Slice into 2-3 sub-orders** spaced 1-2 minutes apart. Market makers refresh quotes more aggressively when they see absorbed flow.
3. **Use the spread order book** rather than legging. Most brokers route a defined-leg structure (vertical, iron condor) as a single combo order with its own NBBO; legging in separately exposes you to mid-trade mispricing.
4. **Avoid the open and close** — bid-ask routinely 2-3x wider in the first/last 15 minutes.
5. **Cancel and re-submit on different ECN routes** if the broker supports it. Sometimes the displayed NBBO is on a route that won't take your size.

## NBBO and Price Improvement

The **National Best Bid and Offer (NBBO)** is the consolidated tightest bid and ask across all options exchanges (CBOE, ISE, BOX, NYSE Arca Options, BATS, MIAX, etc.). When you submit a market order, the order is supposed to route to the exchange showing NBBO — but in practice, many retail brokers route flow to wholesalers (Citadel, Susquehanna, Wolverine) for **price improvement**.

- Price improvement on options is real but small — typically $0.001-$0.01 per contract relative to NBBO
- It does *not* compensate for trading illiquid contracts; the wholesaler may improve $0.005 on a $0.20 spread, leaving 97.5% of the spread cost intact
- Limit orders at mid bypass the wholesaler routing and engage exchange order books directly — usually preferred for non-urgent fills

A common myth: "my broker has best execution, so the bid-ask doesn't matter." False. Wholesaler price improvement is real but tiny; the bid-ask itself is the dominant cost on any contract wider than penny-pilot.

## Worked Example: Slippage Tax on Two Identical-Looking Trades

*Illustrative arithmetic, not a backtest.* Two traders each sell a 30-DTE put credit spread for a stated **$0.50 mid credit** on a $5-wide spread. The only difference is liquidity.

**Trader A — liquid penny-pilot name ([[spy|SPY]]):**

- Per-leg bid-ask: $0.02. Filling each leg ~1 cent off mid.
- Round-trip slippage (enter + exit, 2 legs): ~$0.04.
- Net credit captured: $0.50 − $0.04 = **$0.46** (92% of theoretical).

**Trader B — illiquid mid-cap, OI 200, $0.15 leg bid-ask:**

- Each leg fills ~$0.07 off mid. Round-trip across 2 legs: ~$0.28.
- Net credit captured: $0.50 − $0.28 = **$0.22** (44% of theoretical).
- Worse: at exit, OI may have fallen further; the realistic exit fill could be at the bid, turning a "winner" into a scratch.

The *displayed* trade is identical (same delta, same width, same $0.50 mid). The realized economics differ by more than 2x purely from the liquidity gate. Over a year of monthly rolls, Trader B's slippage tax can exceed the entire [[theta]] edge the structure was designed to harvest — the page's central claim, made concrete.

## Liquidity-Driven Strike Adjustments

When the strike chosen by [[strike-selection|delta convention]] is illiquid, the trader has three options:

1. **Move to a more liquid strike** (closer to ATM, where OI/volume cluster) and accept slightly different delta
2. **Move expiration** to one with better liquidity (often the next monthly)
3. **Skip the trade** — the strike's illiquidity is signaling that this particular expression of the strategy isn't economically viable

The wrong move: take the trade anyway because "the chain *has* a quote." A quote is not a fill.

## Related

- [[bid-ask-spread]] — the dominant cost on illiquid options
- [[slippage]] — realized cost beyond bid-ask
- [[liquidity]] — general concept
- [[unusual-whales]] — flow scanner with liquidity overlays
- [[options-selection-framework]] — liquidity is filter 1
- [[strike-selection]] — strike choice constrained by liquidity
- [[expiration-selection]] — DTE choice constrained by liquidity
- [[moneyness-selection]] — moneyness choice constrained by liquidity
- [[market-microstructure]] — broader context for NBBO and routing
- [[clob]] — central limit order book mechanics
- [[thinkorswim]], [[tastytrade]], [[interactive-brokers]], [[tradestation]] — broker tools
- [[spread-width-selection]] — wider spreads less punished by per-contract slippage
- [[probability-of-profit]] — the metric slippage silently erodes
- [[vix-calls]], [[spx-puts]] — Tier-1 instruments where convex hedges are executable

## Sources

- CBOE / OCC — Penny Pilot Program designation list and minimum-tick rules
- SEC Rule 611 (Reg NMS) and OCC documentation — NBBO consolidation and order routing
- tastytrade research archive — liquidity-score methodology and slippage cost studies
- Euan Sinclair, *Positional Option Trading* (Wiley) — transaction-cost modeling for options strategies
