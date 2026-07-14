---
title: "Spread Width Selection"
type: concept
created: 2026-05-03
updated: 2026-07-14
status: good
tags: [options, derivatives, crypto, risk-management]
markets: [crypto, options]
aliases: ["Wing Width", "Strike Width", "Spread Width"]
domain: [risk-management, options]
prerequisites: ["[[options]]", "[[credit-spreads]]", "[[iron-condors]]", "[[delta]]"]
difficulty: intermediate
related: ["[[deribit]]", "[[crypto-options-volatility-selling]]", "[[dvol]]", "[[options]]", "[[credit-spreads]]", "[[iron-condors]]", "[[short-strangle]]", "[[delta]]", "[[probability-of-profit]]", "[[position-sizing]]", "[[bid-ask-spread]]", "[[liquidity]]", "[[buying-power]]"]
---

Spread width — the dollar distance between the long and short strikes in a vertical or [[iron-condors|iron condor]] structure — is the single most important sizing decision after strike selection. Width determines max loss, capital required, reward-to-risk ratio, and how badly transaction costs eat into the trade. Picking the wrong width can turn a structurally good trade into a structurally bad one. The mechanics are instrument-agnostic; the examples below use [[deribit|Deribit]] BTC/ETH, and the **Crypto specifics** section flags where crypto changes the calculus (larger notionals, cash settlement, wider vol-point costs, and the fact that width is only truly free to choose on BTC/ETH — alt chains are too thin).

## What Width Controls

For a defined-risk credit spread, four numbers move with width:

1. **Max profit** = credit received (grows with width, but slowly past 1× short-leg's extrinsic)
2. **Max loss** = width − credit (grows roughly linearly with width)
3. **Capital required (buying power)** = max loss for cash-settled accounts
4. **Reward-to-risk ratio** = credit / (width − credit) — *worsens* as width grows

Crucially, the [[probability-of-profit|PoP]] of the trade is driven primarily by the *short* strike, not the width. Adding wider wings barely moves PoP because the long leg is far OTM and contributes little to breakeven. Width is therefore mostly a *risk-sizing* tool, not a probability-shaping tool.

## The Core Tradeoff

| Dimension | Narrow spread (e.g., 1-2 wide) | Wide spread (e.g., 10-20 wide) |
|---|---|---|
| **Credit** | Small (~$0.20-$0.50) | Large (~$2-$5) |
| **Max loss** | Small ($80-$180) | Large ($800-$1,800) |
| **R:R ratio** | Better (1:3 or 1:4) | Worse (1:5 or 1:6) |
| **PoP** | Slightly higher | Slightly lower |
| **Capital efficiency per dollar of credit** | Lower (commission drag) | Higher |
| **Bid-ask drag** | Severe (1-2 ticks of slippage on a $0.30 credit is 30-60%) | Mild (1-2 ticks on a $3 credit is 1-3%) |
| **Fee drag** | Severe (Deribit's 12.5%-of-premium fee cap bites hardest on thin credits) | Mild |
| **Tail risk at expiry** | Capped tightly | Capped, but the cap is large |

The narrow spread is "safer" per trade in absolute dollars but bleeds capital through fill economics; the wide spread is more expensive per loss but more efficient when liquidity is good.

## Worked Example: $150-Wide vs. $300-Wide Put Credit Spread on ETH (Deribit)

ETH at $3,000, 40 DTE, USDC-margined (linear, 1 ETH per contract). Sell the 30-delta short put at strike $2,700. DVOL ~55. Compare two long-strike choices (ETH is used rather than BTC because BTC's ~$60k notional makes single-contract spreads too large for a retail risk budget — a real crypto consideration, see *Crypto specifics*):

### $150-wide: Short $2,700 Put / Long $2,550 Put

- Credit: ~$50
- Max profit: **$50** per contract
- Max loss: $150 − $50 = **$100** per contract
- Capital required: $100
- R:R: 1 : 2.0 (need to win 67% of the time to break even)
- PoP: ~71%
- Credit / width: 33% (right at the "1/3-of-width" target)

### $300-wide: Short $2,700 Put / Long $2,400 Put

- Credit: ~$85
- Max profit: **$85** per contract
- Max loss: $300 − $85 = **$215** per contract
- Capital required: $215
- R:R: 1 : 2.53 (need to win 71.7% to break even)
- PoP: ~70% (barely changes — the short leg drives it)
- Credit / width: 28.3% (below the 1/3 rule of thumb)

### Cost Overlay

Deribit taker fees are 0.03% of the underlying per leg, **capped at 12.5% of the option premium** — and the cap bites on cheap wings. Assume that plus ~3 vol points of bid-ask per leg nets roughly $4 round-trip on the $150-wide and $5 on the $300-wide:

- $150-wide net credit: $50 − $4 ≈ **$46** (~8% drag)
- $300-wide net credit: $85 − $5 ≈ **$80** (~6% drag)

The wide spread loses a smaller percentage to costs — the case for going wider when the underlying is liquid (BTC/ETH). On thin alt options with wide vol-point spreads, the narrow spread gets crushed outright.

### Sizing

A trader with a $50,000 account willing to risk 2% per trade ($1,000) can size:

- $150-wide: $1,000 / $100 = **10 contracts** → max profit $500, max loss $1,000
- $300-wide: $1,000 / $215 = **4 contracts** (rounding down) → max profit $340, max loss $860

The $150-wide structure delivers more total credit at the same risk budget *and* spreads the position across more independent fills' worth of theta-decay/management opportunity. For risk-budget-bound retail traders, narrower-and-more-contracts is often the better answer when liquidity supports it — which in crypto means staying on BTC/ETH.

## The "1/3-of-Width" Rule of Thumb

The tastytrade educational stack popularized a heuristic that ports directly to crypto: only sell credit spreads that pay at least **one-third of the width as credit**. For a $150-wide ETH spread, demand at least ~$50 credit; for a $300-wide, at least ~$100. The reasoning:

- 1/3 credit-to-width gives a R:R of 1:2 (max loss = 2× max profit), which sets the breakeven win-rate at ~67%.
- A 30-delta short strike has model-implied [[probability-of-profit|PoP]] near 70%, providing a thin theoretical edge over breakeven.
- If the trade only pays 1/4 of width, the breakeven win-rate jumps to 75%+ and the model-PoP is no longer enough to be edge-positive.

The rule is a fast filter: if a credit spread doesn't clear the 1/3 hurdle, either the strikes are too far OTM (move strikes closer in) or the IV is too low to bother (skip the trade or wait for higher IV).

For [[iron-condors]], the equivalent rule is "1/3 of one-side's width" since you're collecting credit on both sides. A $300-wide-per-side ETH condor should pay at least ~$100 total.

## Selection Heuristics

1. **Size by risk budget first.** Pick the contract count that keeps max loss below 1-2% of portfolio. Then choose the width that lets you hit that count. Don't pick the width first.
2. **Match width to liquidity.** On Deribit BTC/ETH — wide spreads fill cleanly. On a thin alt option with a several-vol-point bid-ask, stick to a narrow width and accept the worse R:R, or (usually better) skip the name entirely — most crypto width choice collapses to "trade BTC/ETH."
3. **Match width to expected hold time.** If you plan to close at 50% max profit in 5-15 days, a narrower spread is fine — you're not holding to expiry. If you plan to manage at 21 DTE, wider gives more buffer to the short strike.
4. **Don't let one spread blow more than X% of buying power.** A common rule is 5% of buying power per single trade for defined-risk structures, lower for [[short-strangle|undefined-risk]] structures.
5. **Re-check the 1/3 rule after fills.** If you set a limit order at 1/3-of-width and it doesn't fill, walk the price up — but if you have to give up more than 10-15% of your target credit, the trade isn't there.
6. **Wider when DVOL is high in its range; narrower when DVOL is low.** Wide spreads only work when the credit is meaningful. In low-[[dvol|DVOL]] regimes, the wider structure pays so little extra credit that it's not worth the extra capital.

## Width and Settlement Risk

On Deribit, options are **European-style and cash-settled to an index**, so there is *no early assignment* and no physical delivery — the whole class of early-assignment and dividend-adjustment risk that shapes equity spread-width decisions simply does not apply. Width's only expiry effect is mechanical: if the short strike is breached and the trade is held to expiry, a wider spread means more dollars at risk between the strikes, settled in cash against the index print. There is no crypto analog to dividend-driven early assignment; the one settlement nuance to watch is **inverse (coin-margined)** contracts, where the P&L between strikes is denominated in the coin and interacts with the falling collateral value — prefer USDC-margined (linear) spreads for clean, width-defined USD risk.

## Width and the Gamma Trap

Per [[gamma-risk]], all short-premium structures concentrate risk near expiry (the equity rule of thumb is ~21 DTE). Width interacts with gamma in a subtle way: a *narrower* spread reaches max loss faster (it doesn't take a big move to blow through the long strike), but the absolute dollar damage is small. A *wider* spread takes longer to reach max loss but the dollar damage when it does is large. For traders who reliably manage on schedule, narrower-and-more-contracts is generally safer; for traders who tend to hold longer, wider-and-fewer-contracts gives more time/space to roll. **Crypto sharpens this trap**: 24/7 trading means the gap that blows through the long strike can arrive at any hour with no market close to pause it, so the "narrower spread reaches max loss faster" risk is realized more often than on equities — a reason to lean toward defined-risk, manageable widths rather than chasing the wide spread's fee efficiency into an overnight gap.

## Crypto Specifics

The width tradeoffs (max loss, R:R, cost drag, the 1/3-of-width rule) are identical in logic on crypto. What changes:

- **Notional scale forces the underlying choice.** A single BTC put spread carries ~$60k of notional per contract, so meaningful widths blow through a retail risk budget in one contract. ETH (and, for smaller accounts, the ability to size the vega rather than the contract count) is where retail width selection actually happens; BTC spreads suit larger books.
- **Costs are wider and premium-capped.** Deribit's taker fee is 0.03% of the underlying **capped at 12.5% of the option premium** — the cap dominates on cheap OTM wings, so the cost penalty for going *too narrow* (thin credit) is harsher than on penny-wide equity options. This pushes crypto width slightly wider than the equity default, liquidity permitting.
- **Cash settlement removes assignment from the width equation.** European-style, index-settled contracts mean width only governs dollars-at-risk between strikes, never early-assignment mechanics.
- **Width is only free to choose on BTC/ETH.** Alt option chains are too thin to support anything but the narrowest spreads (or none) — for most of the crypto universe, "what width?" reduces to "not tradeable."
- **24/7 gap risk.** With no market close, the narrow spread's "reaches max loss faster" downside and the wide spread's "large dollar damage" both land on overnight gaps that equities never see — favor defined, manageable widths and hard risk limits. See [[crypto-options-volatility-selling]] for the full short-vol risk framework.

## Getting the Data (CryptoDataAPI)

Per-strike premiums and vol-point bid-ask (which set the credit and cost drag at each width) come from [[deribit|Deribit]] / [[greeks-live|Greeks.live]]. [[cryptodataapi|CryptoDataAPI]] supplies the options positioning and vol-regime context for deciding *whether* the credit-per-width is worth it.

**Live data:**
- `GET /api/v1/market-intelligence/options` — BTC options OI, volume, and [[max-pain]] strike (where the liquidity is, to judge viable width)
- `GET /api/v1/volatility/regime` — per-asset vol regime (is DVOL high enough in its range to pay for a wider spread?)
- `GET /api/v1/liquidity/depth` — spot depth/spread, the hedge-side liquidity behind the structure

**Historical data:**
- `GET /api/v1/volatility/regime/{symbol}` — per-asset vol regime detail + 60-day history

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/market-intelligence/options"
```

Auth: `X-API-Key` header. Full catalog: [[cryptodataapi-market-intelligence]]; volatility-regime detail on [[cryptodataapi]].

## Related

- [[deribit]] — the venue whose fee cap and cash settlement shape crypto width choice
- [[crypto-options-volatility-selling]] — the defined-risk short-vol book width selection feeds
- [[dvol]] — the regime gauge for whether a wider spread's credit is worth it
- [[options]] — overview
- [[credit-spreads]] — the primary structure where width selection applies
- [[iron-condors]] — two-sided structure with width on each wing
- [[short-strangle]] — undefined-risk alternative when width-driven capital is too high
- [[probability-of-profit]] — the metric that barely changes with width
- [[delta]] — the strike-selection metric that drives PoP
- [[position-sizing]] — the master constraint width must respect
- [[bid-ask-spread]] — the cost that punishes narrow spreads
- [[liquidity]] — determines viable width on a given name
- [[buying-power]] — determines max contracts at a given width

## Sources

- (Source: [[2026-04-22-gap-finder-options-portfolios]])
- [[deribit]] / [[greeks-live]] — Deribit taker-fee schedule (0.03% of underlying, 12.5%-of-premium cap), European-style cash settlement, and BTC/ETH vs alt liquidity that bound viable width in crypto
- tastytrade research archive — the 1/3-of-width credit heuristic and R:R/breakeven arithmetic (ports directly to crypto)
