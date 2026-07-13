---
title: "Options Chain"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility, market-microstructure]
aliases: ["Options Chain", "options-chain", "Option Chain", "Options Matrix"]
domain: [options, market-microstructure]
prerequisites: ["[[options-overview]]", "[[options-pricing]]"]
difficulty: intermediate
related: ["[[options-overview]]", "[[options]]", "[[options-pricing]]", "[[greeks]]", "[[implied-volatility]]", "[[volatility-skew]]", "[[open-interest]]", "[[options-strategies]]", "[[bid-ask-spread]]", "[[put-call-parity]]"]
---

An **options chain** (or option chain) is the full matrix of listed option contracts for a single underlying asset, organised by expiration date and strike price. It is the primary screen an options trader reads to select contracts, gauge liquidity, and infer the market's volatility expectations. Brokers and data vendors (e.g. CBOE, OPRA feed, broker platforms) present it as a table of calls on one side and puts on the other, with the strike ladder running down the middle.

## How It Is Structured

A chain is sliced first by **expiration** (each listed expiry — weekly, monthly, quarterly, LEAPS — is its own tab or block) and within an expiry by **strike price**, from deep in-the-money to deep out-of-the-money. For each strike, the row reports both the call and the put with several columns:

- **Bid / Ask** — the prices a trader can sell at (bid) or buy at (ask); the gap is the [[bid-ask-spread]], which widens on illiquid strikes and is the dominant trading cost in options.
- **Last** — the most recent traded price (can be stale on thin strikes).
- **Volume** — contracts traded that session; a liquidity gauge.
- **[[open-interest|Open Interest]]** — the number of outstanding contracts not yet closed; the better measure of where positioning and liquidity actually sit.
- **[[implied-volatility|Implied Volatility (IV)]]** — the volatility backed out of the contract's market price via an [[options-pricing|options-pricing model]]; the column that turns a chain from a price list into a forecast.
- **[[greeks|Greeks]]** — delta, gamma, theta, vega (and sometimes rho) per contract, showing each option's risk sensitivities.

The strike nearest the current underlying price is the **at-the-money (ATM)** row; calls below spot and puts above spot are **in-the-money (ITM)**, the reverse are **out-of-the-money (OTM)**.

## Illustrative Chain Layout

A single expiry of a chain reads outward from the ATM strike, calls on the left, puts on the right, the strike ladder down the centre. With the underlying XYZ at **$100** and ~30 days to expiry, a simplified block looks like this:

| Call Δ | Call OI | Call Vol | Call IV | Call Bid | Call Ask | **Strike** | Put Bid | Put Ask | Put IV | Put Vol | Put OI | Put Δ |
|-------:|--------:|---------:|--------:|---------:|---------:|:----------:|--------:|--------:|-------:|--------:|-------:|------:|
| 0.78 | 3,100 | 410 | 31% | 5.95 | 6.15 | **95** | 1.05 | 1.15 | 32% | 980 | 6,200 | -0.22 |
| 0.62 | 9,800 | 2,300 | 29% | 3.55 | 3.65 | **100** (ATM) | 2.95 | 3.05 | 29% | 2,100 | 8,400 | -0.38 |
| 0.41 | 6,400 | 1,750 | 28% | 1.85 | 1.95 | **105** | 5.30 | 5.50 | 30% | 540 | 4,900 | -0.59 |
| 0.19 | 1,200 | 220 | 30% | 0.70 | 0.85 | **110** | 9.10 | 9.40 | 33% | 90 | 1,100 | -0.81 |

Reading the block: the **100 strike is ATM**; its call and put carry matching ~29% IV, as [[put-call-parity]] requires. Calls become more expensive and higher-delta as strikes fall (deeper ITM); puts do the reverse. Note the IV **rises at the wings** (95 put at 32%, 110 put at 33%) — that upward curl on the downside is the equity [[volatility-skew]]. Liquidity is deepest at and just out-of-the-money (the 100/105 rows show the tightest spreads and largest OI); the far OTM 110 call quoted 0.70/0.85 has a ~20%-of-price spread and thin OI — expensive to enter and exit.

## How Traders Use It

The chain is where contract selection happens, and reading it well is a core skill:

- **Liquidity screening** — favour strikes with high open interest and volume and a tight bid-ask spread. Trading illiquid strikes means crossing a wide spread on both entry and exit, often the difference between a profitable and losing trade.
- **Reading implied volatility** — comparing IV across strikes within one expiry reveals the [[volatility-skew|volatility skew/smile]]; comparing ATM IV across expiries reveals the term structure. Elevated IV means options are "expensive" (favours sellers), depressed IV means "cheap" (favours buyers).
- **Building structures** — multi-leg [[options-strategies|strategies]] (vertical spreads, iron condors, straddles) are assembled by picking specific strikes and expiries straight off the chain, netting the bids and asks to compute the structure's debit or credit.
- **Positioning intelligence** — large open interest clustered at a strike ("max pain," dealer gamma walls) can act as a magnet or barrier for the underlying near expiry, a signal some traders watch around monthly expirations.
- **Estimating the expected move** — the ATM straddle price (ATM call + ATM put) approximates the move the market is pricing into the underlying by expiry. In the table above, the ATM straddle costs roughly 3.60 + 3.00 = **$6.60**, implying a ~±6.6% move on a $100 stock — the break-even hurdle a long-volatility [[earnings]] play must clear.

### The column meanings, summarised

| Column | What it tells you | How to use it |
|--------|-------------------|---------------|
| Bid / Ask | Sell / buy price | Net the legs; the spread is your entry+exit cost |
| Last | Most recent trade | Ignore on thin strikes — it goes stale |
| Volume | Today's contracts traded | Fresh interest / liquidity *today* |
| [[open-interest\|Open Interest]] | Outstanding contracts | Where positioning and durable liquidity sit |
| [[implied-volatility\|IV]] | Vol implied by the price | Cheap vs rich; build skew & term structure |
| Delta (Δ) | Sensitivity to spot | Rough probability ITM; directional exposure |
| [[greeks\|Gamma/Theta/Vega]] | 2nd-order & decay risks | Manage how the position behaves over time

## Worked Reading

Suppose XYZ trades at $100. On the monthly chain, the $100 call shows bid 3.10 / ask 3.20, OI 8,400, IV 28%; the $100 put shows bid 2.95 / ask 3.05, IV 28%. The matching IV on the ATM call and put is expected from [[put-call-parity]]. Buying the call costs the 3.20 ask plus you concede the ~$0.10 spread; a $105 call quoted 1.40/1.55 with OI 200 is far less liquid — the wider spread and thin OI warn that exiting will be costly. A trader wanting a defined-risk bullish bet might instead read off the chain to build a 100/105 call vertical, paying the 100-call ask and selling the 105-call bid.

Worked vertical: pay the 100-call ask (1.95 in the layout table) and sell the 105-call bid (1.85) for a **net debit of 0.10** — but always mid-to-mid the structure rather than paying ask and selling bid on every leg, or the [[bid-ask-spread]] eats the trade. Maximum value of a 100/105 call spread is the 5-point width; the risk is the debit paid.

## Pitfalls and Risks

- **Crossing the spread twice.** Every round trip pays the [[bid-ask-spread]] on entry *and* exit. On a 1.40/1.55 strike that ~10% spread can dwarf any directional edge — the single biggest avoidable cost in options.
- **Stale "Last" prices.** On thin strikes the last trade may be hours old and mislead you on value; price off the live bid/ask and the [[implied-volatility|IV]], not Last.
- **Mid-price illusion.** Quoted mid is not where you fill on illiquid strikes — assume you give up a meaningful fraction of the spread.
- **IV crush.** Buying rich [[implied-volatility]] before an [[earnings]] report or other event means a directionally correct trade can still lose when IV collapses afterward. Compare the chain's implied move to your expected move.
- **Pin / assignment risk near expiry.** Short ITM options can be assigned, and strikes near spot at expiry ("pinning") create unpredictable exercise; close or roll before expiry to avoid surprises.
- **Reading OI direction wrong.** Open interest shows *that* positioning exists, not whether it is long or short — do not infer direction from OI alone.
- **Wide-strike, low-liquidity wings.** Far OTM strikes look cheap in dollars but carry brutal percentage spreads and can be near-impossible to exit at a fair price.

## Sources

- CBOE, *Options Chain and Quote Conventions* — exchange documentation on listed strikes, expirations, and quote dissemination (OPRA)
- Natenberg, S. (1994), *Option Volatility and Pricing*, McGraw-Hill — implied volatility, skew, and reading volatility across strikes/expiries
- McMillan, L. (2002), *Options as a Strategic Investment*, Prentice Hall — contract selection, liquidity, and open interest interpretation

## Related

- [[options-overview]] — instrument primer
- [[options-pricing]] — how each contract's premium and IV are derived
- [[greeks]] — the risk-sensitivity columns
- [[implied-volatility]] — the forecast embedded in chain prices
- [[volatility-skew]] — the cross-strike IV pattern read from the chain
- [[open-interest]] — the positioning/liquidity column
- [[options-strategies]] — structures built by selecting strikes off the chain
- [[bid-ask-spread]] — the dominant cost when trading any contract
