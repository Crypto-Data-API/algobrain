---
title: "Hyperliquid Margining Modes"
type: concept
created: 2026-06-20
updated: 2026-06-20
status: draft
tags: [crypto, market-microstructure, derivatives, leverage, margin]
aliases: ["Hyperliquid Margin Modes", "HL Cross vs Isolated", "Hyperliquid No-Cross Margin", "Hyperliquid Maintenance Margin"]
related: ["[[hyperliquid]]", "[[hypercore]]", "[[hip-3-builder-deployed-perps]]", "[[hlp]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-fee-tiers-and-maker-rebates]]", "[[hyperliquid-funding-rate-microstructure]]", "[[funding-rate]]", "[[clob]]", "[[order-book]]", "[[market-microstructure]]", "[[slippage]]", "[[market-impact]]", "[[liquidation]]", "[[perpetual-futures]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[perpetual-futures]]", "[[liquidation]]"]
difficulty: advanced
---

# Hyperliquid Margining Modes

**Hyperliquid margining modes** govern how collateral is allocated to [[perpetual-futures]] positions on [[hypercore|HyperCore]] and therefore determine when the [[hyperliquid-liquidation-engine|liquidation engine]] fires. Hyperliquid supports **cross** margin and **isolated** margin on core markets, and [[hip-3-builder-deployed-perps|HIP-3]] builder-deployed markets add a **"no-cross"** mode that enables isolated margin with margin removal but without cross-margining across positions. Across all modes, a position is liquidated when **account equity falls below maintenance margin**, where maintenance margin is defined as **half the initial margin at maximum leverage**; with max leverage ranging roughly **3x–40x**, this implies maintenance-margin ratios from about **16.7% down to ~1.25%** by market (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

> **Where this page sits.** This is the margin-allocation reference. For what happens *after* the trigger — the tiered Tier-1/Tier-2/ADL cascade, HLP backstop absorption, mark-price construction, and cascade dynamics — see the dedicated [[hyperliquid-liquidation-engine]] page. This page deliberately does **not** duplicate that engine detail; it links to it.

## The Three Modes

| Mode | Collateral sharing | Where available | Key property |
|---|---|---|---|
| **Cross** | One shared collateral pool backs all positions | Core markets | Most capital-efficient; a loss on one position draws on the equity backing every other position — a single bad position can cascade into the whole account. |
| **Isolated** | Collateral is ring-fenced per position | Core markets | Localizes failure: a liquidation closes only that position and consumes only its allocated margin, leaving the rest of the account untouched. |
| **No-cross** (HIP-3) | Isolated, with margin removal allowed, no cross-margin across positions | [[hip-3-builder-deployed-perps|HIP-3]] markets | HIP-3 DEXs support this mode so positions on a builder-deployed market are not cross-margined against the rest of the account. |

The practical consequence is that the **same account** can be subject to different margining rules depending on whether it is trading a core perp or a HIP-3 perp — the trader must reason about each market's mode independently rather than assuming uniform account-level risk (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Initial vs Maintenance Margin

Hyperliquid defines the two margin levels relative to each market's maximum leverage:

- **Initial margin (IM)** is the collateral required to open a position. At maximum leverage, IM is the reciprocal of the leverage cap (e.g., a 40x market requires IM ≈ 1/40 = 2.5% to open at the cap).
- **Maintenance margin (MM)** is **half the initial margin at maximum leverage**. A position is liquidated once account equity falls below this level.

Because MM is anchored to half the max-leverage IM, the maintenance-margin *ratio* is determined by the market's leverage cap:

| Max leverage | Approx. IM at cap | Maintenance margin ratio (≈ half IM at max lev) |
|---|---|---|
| ~3x | ~33.3% | ~16.7% |
| ~10x | ~10% | ~5% |
| ~20x | ~5% | ~2.5% |
| ~40x | ~2.5% | ~1.25% |

So a high-leverage major (e.g., a 40x BTC market) tolerates equity falling to ~1.25% of notional before liquidating, while a low-leverage long-tail market (e.g., 3x) requires far more equity headroom (~16.7%). Lower max leverage is the protocol's first line of defense on thinner, more manipulable markets (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

> The figures above are the *structural* relationship the research states (MM = half IM at max leverage; max leverage ~3–40x → MM ratio ~16.7%→~1.25%). Per-asset leverage caps and any notional-tiered maintenance schedule come from the live Hyperliquid documentation; see [[hyperliquid-liquidation-engine#Maintenance Margin Tiers]] for the notional-tiered view of the same parameters.

## The Liquidation Trigger

The trigger condition is uniform across modes:

```
liquidate when:  account_equity < maintenance_margin
where:           maintenance_margin = 0.5 * initial_margin_at_max_leverage * notional
```

When the condition is met, the protocol **closes positions via market orders into existing [[order-book|book depth]]** on the [[hypercore|HyperCore]] [[clob|CLOB]]. This is the critical link between margining and microstructure: the realized liquidation price is whatever the resting bids/asks offer, so **available book depth directly determines liquidation slippage**. In a deep book, the closeout is near mark; in a thin book, [[slippage]] and [[market-impact]] widen the realized loss, and — on Hyperliquid — the residual flow falls to the [[hlp|HLP]] backstop. The full tiered execution path (public book → HLP absorption → ADL) is documented in [[hyperliquid-liquidation-engine]] (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Core Markets vs HIP-3 Markets

[[hip-3-builder-deployed-perps|HIP-3]] markets inherit HyperCore's margining and order books but differ from core markets in ways that change the margin/liquidation risk profile:

| Dimension | Core markets | HIP-3 markets |
|---|---|---|
| Margin modes | Cross, isolated | Isolated / **no-cross** (no cross-margin across positions) |
| Leverage limits | Set by protocol | Set by the **deployer** |
| Oracle | Protocol/crypto cross-venue feeds | **Builder-configured** oracle (weaker manipulation-resistance possible) |
| Liquidation backstop | HLP vault | Each HIP-3 DEX has its **own on-chain backstop liquidation strategy contract** |
| Settlement rules | Protocol-defined | Deployer-defined |

The combination matters: a HIP-3 market can pair aggressive leverage limits with a thinner book and a builder-configured oracle, so the same nominal leverage carries more liquidation risk than on a core major. Per the research and the [[hyperliquid-liquidation-engine|JELLYJELLY post-mortem]], long-tail HIP-3 listings are precisely where margining headroom is thinnest and mark integrity is most fragile (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

## Practical Implications for Traders

- **Prefer isolated / no-cross for uncorrelated bets.** Cross margin is more capital-efficient but cascades one bad position into the whole account; isolated and no-cross localize the failure.
- **Treat the leverage cap as a maintenance-margin signal.** A market's max leverage *is* its maintenance-margin ratio (MM ≈ half IM at the cap). Trading near the cap leaves almost no equity buffer (as little as ~1.25% on 40x markets).
- **Account for funding in the equity calculation.** Hourly [[hyperliquid-funding-rate-microstructure|funding]] payments debit/credit equity and can push a marginal position into liquidation independent of price; high positive [[funding-rate]] also signals a heavy leveraged-long book and elevated cascade risk.
- **Re-underwrite each HIP-3 market.** Deployer-set leverage, a builder oracle, and a separate backstop contract mean HIP-3 margin risk is *not* comparable to core markets even at identical leverage.
- **Liquidation cost is a book-depth question.** Because closeouts are market orders into the live book, position sizing should account for the [[slippage]] / [[market-impact]] your own forced exit would create in that market's depth.

## Related

- [[hyperliquid-liquidation-engine]] — what happens after the trigger: tiered cascade, HLP backstop, ADL, mark price, cascade dynamics (do not duplicate here)
- [[hyperliquid]] — the venue overview
- [[hypercore]] — the L1 engine hosting margining and the order books
- [[hip-3-builder-deployed-perps]] — builder-deployed markets and the no-cross mode
- [[hlp]] — the depositor-capitalized backstop that absorbs liquidation residuals
- [[hyperliquid-fee-tiers-and-maker-rebates]] — companion page on the fee schedule
- [[hyperliquid-funding-rate-microstructure]] — funding's effect on equity and cascade risk
- [[funding-rate]] — general funding background
- [[clob]], [[order-book]] — the book liquidations execute into
- [[slippage]], [[market-impact]] — drivers of realized liquidation cost
- [[liquidation]], [[perpetual-futures]] — underlying concepts
- [[market-microstructure]] — domain parent

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) — gap-finder deep research synthesizing Hyperliquid's official margining and liquidation documentation.
- **Hyperliquid Docs — Liquidations.** https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations — liquidation when equity < maintenance margin; MM = half IM at max leverage; max leverage ~3–40x → MM ratio ~16.7%→~1.25%; positions closed via market orders into book depth.
- **Hyperliquid Docs — Margining.** https://hyperliquid.gitbook.io/hyperliquid-docs/trading/margining — cross vs isolated margin; HIP-3 "no-cross" mode (isolated with margin removal, no cross-margin across positions).
- **Hyperliquid Docs — HIP-3 Builder-Deployed Perpetuals.** https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals — deployer-set leverage limits, builder oracles, per-DEX backstop liquidation strategy contracts.
