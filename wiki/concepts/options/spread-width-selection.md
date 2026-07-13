---
title: "Spread Width Selection"
type: concept
created: 2026-05-03
updated: 2026-06-11
status: good
tags: [options, derivatives, risk-management]
aliases: ["Wing Width", "Strike Width", "Spread Width"]
domain: [risk-management, options]
prerequisites: ["[[options]]", "[[credit-spreads]]", "[[iron-condors]]", "[[delta]]"]
difficulty: intermediate
related: ["[[options]]", "[[credit-spreads]]", "[[iron-condors]]", "[[short-strangle]]", "[[delta]]", "[[probability-of-profit]]", "[[position-sizing]]", "[[bid-ask-spread]]", "[[liquidity]]", "[[buying-power]]"]
---

Spread width — the dollar distance between the long and short strikes in a vertical or [[iron-condors|iron condor]] structure — is the single most important sizing decision after strike selection. Width determines max loss, capital required, reward-to-risk ratio, and how badly transaction costs eat into the trade. Picking the wrong width can turn a structurally good trade into a structurally bad one.

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
| **Commission drag** | Severe (per-contract fees a larger fraction of credit) | Mild |
| **Tail risk if assigned** | Capped tightly | Capped, but the cap is large |

The narrow spread is "safer" per trade in absolute dollars but bleeds capital through fill economics; the wide spread is more expensive per loss but more efficient when liquidity is good.

## Worked Example: 5-Wide vs. 10-Wide Put Credit Spread on SPY

SPY at $500, 45 DTE. Sell the 30-delta short put at strike $485. IV ~15%. Compare two long-strike choices:

### 5-wide: Short $485 Put / Long $480 Put

- Credit: ~$1.65
- Max profit: **$165** per contract
- Max loss: $5.00 − $1.65 = **$335** per contract
- Capital required: $335
- R:R: 1 : 2.03 (need to win 67% of the time to break even)
- PoP (broker-quoted): ~71%
- Credit / width: 33% (right at tastytrade's "1/3-of-width" target)

### 10-wide: Short $485 Put / Long $475 Put

- Credit: ~$2.85
- Max profit: **$285** per contract
- Max loss: $10.00 − $2.85 = **$715** per contract
- Capital required: $715
- R:R: 1 : 2.51 (need to win 71.5% to break even)
- PoP (broker-quoted): ~70% (barely changes — the short leg drives it)
- Credit / width: 28.5% (below tastytrade's 1/3 rule of thumb)

### Cost Overlay

Assume $1.30 round-trip commissions per spread plus $0.04 of bid-ask slippage on each leg ($0.08 round-trip total per spread):

- 5-wide net credit: $1.65 − $0.08 − $0.013 ≈ $1.56 → max profit drops to **$156** (5.5% drag)
- 10-wide net credit: $2.85 − $0.08 − $0.013 ≈ $2.76 → max profit drops to **$276** (3.2% drag)

The wide spread loses a smaller percentage to costs — this is the case for going wider when the underlying is liquid. On illiquid names with $0.10+ bid-ask, the narrow spread gets crushed.

### Sizing

A trader with a $50,000 account willing to risk 2% per trade ($1,000) can size:

- 5-wide: $1,000 / $335 = **3 contracts** → max profit $495, max loss $1,005
- 10-wide: $1,000 / $715 = **1 contract** (rounding down) → max profit $285, max loss $715

The 5-wide structure delivers more total credit at the same risk budget *and* fills three independent fills' worth of theta-decay/management opportunity. For risk-budget-bound retail traders, narrower-and-more-contracts is often the better answer when liquidity supports it.

## The "1/3-of-Width" Rule of Thumb

The tastytrade educational stack popularized a heuristic: only sell credit spreads that pay at least **one-third of the width as credit**. For a 5-wide spread, demand at least $1.65 credit; for a 10-wide, at least $3.30. The reasoning:

- 1/3 credit-to-width gives a R:R of 1:2 (max loss = 2× max profit), which sets the breakeven win-rate at ~67%.
- A 30-delta short strike has model-implied [[probability-of-profit|PoP]] near 70%, providing a thin theoretical edge over breakeven.
- If the trade only pays 1/4 of width, the breakeven win-rate jumps to 75%+ and the model-PoP is no longer enough to be edge-positive.

The rule is a fast filter: if a credit spread doesn't clear the 1/3 hurdle, either the strikes are too far OTM (move strikes closer in) or the IV is too low to bother (skip the trade or wait for higher IV).

For [[iron-condors]], the equivalent rule is "1/3 of one-side's width" since you're collecting credit on both sides. A 10-wide condor on each side should pay at least $3.30 total.

## Selection Heuristics

1. **Size by risk budget first.** Pick the contract count that keeps max loss below 1-2% of portfolio. Then choose the width that lets you hit that count. Don't pick the width first.
2. **Match width to liquidity.** On SPY, SPX, QQQ, IWM — wide spreads (10-20) fill cleanly. On a $40 small-cap with $0.20 bid-ask, stick to 1-2 wide and accept the worse R:R, or skip the name.
3. **Match width to expected hold time.** If you plan to close at 50% max profit in 5-15 days, a narrower spread is fine — you're not holding to expiry. If you plan to manage at 21 DTE, wider gives more buffer to the short strike.
4. **Don't let one spread blow more than X% of buying power.** A common rule is 5% of buying power per single trade for defined-risk structures, lower for [[short-strangle|undefined-risk]] structures.
5. **Re-check the 1/3 rule after fills.** If you set a limit order at 1/3-of-width and it doesn't fill, walk the price up — but if you have to give up more than 10-15% of your target credit, the trade isn't there.
6. **Wider on high-IV-rank names; narrower on low-IV-rank names.** Wide spreads only work when the credit is meaningful. In low-IV regimes, the wider structure pays so little extra credit that it's not worth the extra capital.

## Width and Assignment Risk

A wider spread does not increase per-trade [[assignment]] risk on the *short* leg — the short strike is the same. But if the short leg is breached and the trade is held into expiry, a wider spread means more dollars at risk between the strikes. For dividend-paying underlyings, see dividend-adjustments — wide spreads on dividend stocks compound the early-assignment risk because the long leg's protection is further away.

## Width and the Gamma Trap

Per [[gamma-risk]], all short-premium structures concentrate risk near 21 DTE. Width interacts with gamma in a subtle way: a *narrower* spread reaches max loss faster (it doesn't take a big move to blow through the long strike), but the absolute dollar damage is small. A *wider* spread takes longer to reach max loss but the dollar damage when it does is large. For traders who reliably manage at 21 DTE, narrower-and-more-contracts is generally safer. For traders who tend to hold past 21 DTE, wider-and-fewer-contracts gives more time/space to roll.

## Related

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
