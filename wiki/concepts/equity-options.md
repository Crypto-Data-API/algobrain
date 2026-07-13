---
title: "Equity Options"
type: concept
created: 2026-04-15
updated: 2026-06-21
status: excellent
tags: [options, derivatives, volatility]
aliases: ["Equity Options", "Stock Options"]
domain: [derivatives, market-microstructure]
prerequisites: ["[[options]]", "[[stocks]]"]
difficulty: intermediate
related: ["[[options]]", "[[assignment]]", "[[options-greeks]]", "[[options-chain]]", "[[implied-volatility]]", "[[weekly-options]]", "[[long-dated-options]]", "[[covered-call]]", "[[protective-put]]"]
---

Equity options are [[options]] contracts where the underlying instrument is an individual stock. In the US, equity options are predominantly American-style, meaning the holder can exercise at any time before expiration -- unlike European-style options on indices such as the [[spx|S&P 500]], which can only be exercised at expiration. Each standard equity options contract represents 100 shares of the underlying stock, so a contract priced at $3.00 costs $300 in premium. This 100x multiplier is fundamental to understanding position sizing, margin requirements, and risk exposure.

Equity options are listed across multiple expiration cycles. Monthly options expire on the third Friday of each month and have been the traditional standard. Weekly options ("weeklies"), introduced by the CBOE in 2005 and now available on hundreds of liquid names, expire every Friday and have grown to represent over 40% of total options volume. For highly liquid stocks like [[apple|AAPL]], [[nvidia|NVDA]], and [[tesla|TSLA]], the [[options-chain]] may display dozens of expiration dates spanning from days to over two years out (LEAPS -- Long-term Equity Anticipation Securities). Strike prices are typically listed in $1 or $2.50 increments near the current stock price, widening further out-of-the-money.

Key considerations for equity options traders include the risk of early [[assignment]] (particularly on short [[call-option|calls]] ahead of ex-dividend dates, where a holder may exercise to capture the dividend), the impact of [[earnings-calendar|earnings announcements]] on [[implied-volatility]] (the well-known [[iv-crush]] effect), and the influence of [[dividends]] on put-call parity. Corporate actions such as stock splits, mergers, and special dividends can result in "adjusted" or non-standard contracts with modified deliverables, which often have reduced liquidity. Understanding these mechanics is essential before deploying strategies like [[covered-call|covered calls]], [[protective-put|protective puts]], or multi-leg spreads.

## Contract specifications

Standardized US-listed equity options share a common specification, which is what makes them fungible and centrally cleared through the [[options-clearing-corporation|Options Clearing Corporation (OCC)]]. Every contract is defined by five attributes: the underlying stock, the type ([[call-option|call]] or [[put-option|put]]), the [[strike-price|strike]], the [[expiration-date|expiration]], and the exercise style (American for nearly all single names).

| Attribute | Standard equity option | Notes |
|---|---|---|
| Multiplier | 100 shares | A $2.50 quote = $250 of premium per contract |
| Exercise style | American | Holder may exercise any trading day before expiry |
| Settlement | Physical (share delivery) | Contrast index options, which are cash-settled |
| Strike increments | $1.00 / $2.50 / $5.00 | Tighter ($1) near the money on liquid names |
| Expiration cycles | Weeklies, monthlies, quarterlies, LEAPS | Monthlies = 3rd Friday; LEAPS up to ~3 years out |
| Last trading day | Usually the expiration Friday | PM-settled for most equities |
| Auto-exercise threshold | ITM by $0.01 at expiry (OCC "exercise-by-exception") | Holder can opt out via contrary instructions |

A useful rule: because the multiplier is 100, every $1.00 move in the option's quoted price changes the position value by $100 per contract, and every full-point move in a delta-1.00 stock moves a long call/put by 100 × delta dollars.

## Pricing and the Greeks

An equity option's premium decomposes into **intrinsic value** (how far in-the-money it is) and **extrinsic / time value** (everything else — a function of time to expiry, [[implied-volatility|IV]], rates, and dividends). The market prices options through models in the [[black-scholes|Black-Scholes]] / [[binomial-options-pricing|binomial]] family, with the binomial (or trinomial) lattice preferred for American equity options because it can value the early-exercise premium that closed-form Black-Scholes cannot.

The [[options-greeks|Greeks]] are the sensitivities traders actually risk-manage:

| Greek | Measures sensitivity to | Sign for long call | Sign for long put |
|---|---|---|---|
| Delta (Δ) | $1 move in the underlying | + (0 to 1) | − (0 to −1) |
| Gamma (Γ) | change in delta | + | + |
| Theta (Θ) | passage of time (decay) | − | − |
| Vega (ν) | 1-vol-point change in IV | + | + |
| Rho (ρ) | 1% change in rates | + | − |

For single names, vega and gamma exposure cluster around [[earnings-calendar|earnings]], and theta decay accelerates non-linearly in the final weeks of a contract's life — the source of the "[[theta-decay|theta ramp]]" that short-premium sellers harvest.

### Worked example: a long call

Suppose [[apple|AAPL]] trades at $190 and you buy one 30-day $195 call for $3.20.

- Premium outlay = $3.20 × 100 = **$320** (this is your maximum loss).
- Breakeven at expiry = strike + premium = $195 + $3.20 = **$198.20**.
- If AAPL closes at $205 at expiry: intrinsic = $205 − $195 = $10.00, so the call is worth $1,000; profit = $1,000 − $320 = **$680** (+213%).
- If AAPL closes at or below $195 at expiry: the call expires worthless and you lose the full **$320**.

The same $320 controls $19,000 of notional stock exposure (100 × $190) — the leverage that makes options both attractive and dangerous.

## Trading relevance

Equity options give traders precise, leveraged, and risk-defined exposure that cannot be replicated with shares alone. The 100x multiplier and the convexity of the [[options-greeks|Greeks]] mean small moves in the underlying produce large percentage P&L swings, so position sizing is dominated by notional delta and gamma rather than premium outlay. The two structural features that most distinguish equity options from index options -- American-style early [[assignment]] and single-name [[earnings-calendar|earnings]] volatility cycles -- are also the two most common sources of unexpected losses for newer traders. The earnings cycle drives a recurring [[implied-volatility|IV]] term-structure pattern (elevated IV into the print, [[iv-crush|IV crush]] after) that underlies most single-name volatility strategies, while the early-assignment risk on short in-the-money calls around [[ex-dividend-date|ex-dividend dates]] is the central hazard of [[covered-call|covered-call]] and short-call books.

## How traders use equity options

Common single-name structures, ordered roughly from simplest to most complex:

| Structure | Composition | Market view | Max risk |
|---|---|---|---|
| Long call / put | Buy 1 option | Directional + long vol | Premium paid |
| [[covered-call|Covered call]] | Long 100 shares + short call | Mildly bullish, income | Large (stock to $0, capped upside) |
| [[protective-put|Protective put]] | Long 100 shares + long put | Bullish but hedged | Premium + (entry − strike) |
| [[cash-secured-put|Cash-secured put]] | Short put + cash collateral | Willing buyer below market | Strike − premium |
| [[vertical-spread|Vertical spread]] | Long + short same expiry, diff strikes | Directional, defined-risk | Net debit (or width − credit) |
| [[iron-condor|Iron condor]] | Two credit spreads (call + put side) | Range-bound, short vol | Width − net credit |
| [[calendar-spread|Calendar spread]] | Short near-dated + long far-dated, same strike | Long term structure / time | Net debit |
| [[straddle|Straddle]] / [[strangle|strangle]] | Long call + long put | Big move, direction unknown | Premium paid |

The recurring trade structures break into three families: **directional leverage** (long calls/puts and verticals to express a view cheaply), **income / premium selling** ([[covered-call|covered calls]], [[cash-secured-put|cash-secured puts]], iron condors that monetize the [[volatility-risk-premium|volatility risk premium]]), and **volatility / event trades** (straddles and [[calendar-spread|calendars]] timed around [[earnings-calendar|earnings]], built around the [[iv-crush|IV crush]] pattern).

## Common pitfalls and risks

- **Early [[assignment]]** on short ITM calls just before an [[ex-dividend-date|ex-dividend date]] (counterparty exercises to grab the dividend) and on deep-ITM short puts — turns a defined-risk spread into an unhedged stock position overnight.
- **[[iv-crush|IV crush]]**: buying a straddle into earnings, being right on direction, and still losing because [[implied-volatility|IV]] collapsed post-print faster than the stock moved. The move must beat the *implied* move, not just be nonzero.
- **Pin risk** at expiration when the stock closes exactly at a short strike — uncertain whether you'll be assigned, leaving an unwanted Monday gap exposure.
- **Liquidity / wide spreads**: out-of-the-money and longer-dated single-name options can have $0.20+ bid-ask spreads that quietly erode edge; always check [[open-interest]] and quoted depth.
- **Adjusted (non-standard) contracts** after splits, mergers, or special dividends — the deliverable may no longer be 100 shares, and these contracts are thinly traded.
- **Overpaying for theta**: holding long premium through a quiet period, where [[theta-decay|time decay]] grinds down value even when the thesis is intact.
- **Hidden leverage**: sizing by premium ($320 "feels small") rather than by notional delta ($19,000 of stock-equivalent exposure) is the classic blow-up path.

## Related

- [[options]]
- [[options-greeks]]
- [[options-chain]]
- [[implied-volatility]]
- [[assignment]]
- [[weekly-options]]
- [[long-dated-options]]
- [[covered-call]]
- [[protective-put]]
- [[american-vs-european-options]]
- [[black-scholes]]
- [[theta-decay]]
- [[volatility-risk-premium]]
- [[options-clearing-corporation]]
- [[iv-crush]]
- [[vertical-spread]]
- [[iron-condor]]
- [[straddle]]

## Sources

- Options Clearing Corporation (OCC), *Characteristics and Risks of Standardized Options* (the "options disclosure document"), theocc.com
- Cboe Global Markets, equity and weekly options product specifications and volume statistics, cboe.com
- John C. Hull, *Options, Futures, and Other Derivatives* -- contract mechanics, early exercise, and put-call parity (see [[book-options-futures-other-derivatives]])
- Sheldon Natenberg, *Option Volatility and Pricing* -- earnings IV behaviour and the volatility term structure (see [[book-options-volatility-and-pricing]])
