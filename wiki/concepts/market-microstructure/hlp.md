---
title: "HLP (Hyperliquidity Provider)"
type: concept
created: 2026-06-20
updated: 2026-07-13
status: draft
tags: [crypto, market-microstructure, liquidity, derivatives, defi]
aliases: ["Hyperliquidity Provider", "HLP Vault", "HLP"]
related: ["[[hyperliquid]]", "[[hyperliquid-vault-architecture]]", "[[hlp-withdrawal-mechanics]]", "[[hyperliquid-hlp-basis-arbitrage]]", "[[hyperliquid-liquidation-engine]]", "[[hyperliquid-funding-rate-microstructure]]", "[[hyperliquid-order-book-microstructure]]", "[[latency-and-mev-on-chain-clob]]", "[[clob]]", "[[market-microstructure]]", "[[funding-rate]]", "[[hypercore]]", "[[hip-3-builder-deployed-perps]]", "[[cryptodataapi]]"]
domain: [market-microstructure, crypto]
prerequisites: ["[[clob]]", "[[market-making]]"]
difficulty: intermediate
---

# HLP (Hyperliquidity Provider)

The **Hyperliquidity Provider (HLP)** is [[hyperliquid|Hyperliquid]]'s protocol-native, community-owned vault that performs the venue's core liquidity and backstop functions: it quotes two-sided markets, stands as counterparty of last resort in liquidations, and warehouses the residual risk those activities leave behind. Depositors supply USDC, receive pro-rata vault shares, and earn a share of the strategies' net P&L — making HLP simultaneously a yield product for retail and the protocol's risk-warehousing layer. This page is the canonical entry point for the `[[hlp]]` link; for the internal three-strategy decomposition see [[hyperliquid-vault-architecture]], and for the lock-up/exit mechanics see [[hlp-withdrawal-mechanics]].

HLP is not a static reserve like a traditional [[insurance-fund|insurance fund]]. It is an active book embedded in [[hypercore|HyperCore]], the part of Hyperliquid's L1 that runs the on-chain perpetual and spot [[clob|order books]]. Because fees on Hyperliquid are directed to the community rather than to a corporate operator, HLP is one of the primary recipients of protocol revenue — which ties its returns directly to platform volume, liquidations, and funding flow.

---

## What HLP Does

HLP bundles three protocol functions into a single balance sheet. They are summarized below and decomposed in detail in [[hyperliquid-vault-architecture]].

| Function | Role | How HLP earns from it |
|---|---|---|
| **Market making** | Posts resting bids/asks across markets, including the long tail | Spread on round-trips plus continuous **maker rebates** |
| **Liquidation backstop** | Takes over positions that breach [[maintenance-margin]] and unwinds them on the book | Liquidation bonus plus any favorable unwind differential |
| **Residual risk warehousing** | Holds the net delta left after MM and liquidation activity | Harvests the [[funding-rate]] on the residual position |

The first two functions are what make HLP "the protocol's liquidity provider"; the third is the carry that emerges from running the first two.

---

## HLP as Counterparty and Backstop in Liquidations

When a leveraged position falls below maintenance margin, Hyperliquid's [[hyperliquid-liquidation-engine|liquidation engine]] forcibly closes it. HLP is the standing counterparty: it can take over the liquidatable position and unwind it through the order book via market orders, into whatever depth exists at that moment (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). This is the mechanical reason order-book depth matters not just for ordinary execution but for the *severity* of liquidation cascades — thin books mean worse unwind prices, and any gap between the maintenance-margin takeover price and the realized unwind price is absorbed by HLP.

This backstop role is what makes HLP partially an insurance layer. In normal conditions the liquidation bonus is a profit center; in extreme dislocations on thin markets HLP can take losses when the unwind gap exceeds the position's remaining collateral. See [[hyperliquid-vault-architecture#JELLYJELLY-Class Vulnerability]] for the failure boundary.

Note that under [[hip-3-builder-deployed-perps|HIP-3]] builder-deployed markets, each independently deployed DEX has its **own** on-chain backstop liquidation strategy contract rather than relying on the core HLP, so HLP's backstop role applies to the core protocol markets (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]).

---

## Depositor P&L and Revenue Share

HLP runs on a **pro-rata vault-token** model: a depositor's USDC mints shares at the current net asset value (NAV), and those shares represent a fixed fractional claim on the vault's mark-to-market value rather than on any specific position. There is no separately charged performance fee in the conventional sense — depositors simply receive their pro-rata share of whatever the strategies book, net of the trading costs the strategies themselves incur. Because HLP is predominantly a *maker*, much of its fee interaction is rebate income flowing into the vault rather than cost flowing out.

Two structural features govern depositor economics:

- **Lock-up.** Deposits are subject to a multi-day lock before withdrawal, which stabilizes HLP's capital base so it can quote and backstop without bank-run fragility. The exact timing rule (per-deposit cooldown vs. notice period) and the pro-rata stress-queue behavior are covered in full in [[hlp-withdrawal-mechanics]].
- **Regime-rotating yield.** No single function dominates returns: the market-making leg pays in calm markets, the liquidation leg pays during volatility, and funding carry pays in trending markets. This is why HLP's APR is best read as a *range* that rotates with the regime, not a fixed rate. The detailed P&L attribution lives in [[hyperliquid-vault-architecture#P&L Attribution]].

---

## How Protocol Fees Flow to HLP

Hyperliquid's fee design routes trading fees back to the community rather than to middlemen. Per the fee documentation, fees are directed to **HLP, an assistance fund, and deployers** (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]). The relevant mechanics for HLP:

| Fee mechanic | Detail | Relevance to HLP |
|---|---|---|
| **Fee tiers** | Based on rolling 14-day trading volume; spot volume counts double; a single tier spans perps, HIP-3 perps, and spot | Determines the taker fees that ultimately feed community recipients including HLP |
| **Maker rebates** | Paid continuously on each fill | HLP, as a high-volume maker, is a primary rebate recipient — this is a direct revenue stream into the vault |
| **Community direction** | Fees flow to HLP, assistance fund, and deployers (no fees to a corporate operator) | Makes HLP returns a function of platform fee volume |
| **HIP-3 fee shares** | Deployers of HIP-3 markets can configure their own fee shares | HIP-3 markets have separate fee economics from the core protocol that funds HLP |

Because HLP captures both maker rebates on its own fills and a community share of protocol fees, its return profile scales with Hyperliquid's overall volume and liquidation activity. See [[hyperliquid-funding-rate-microstructure]] for how funding — the third revenue leg — is computed from order-book impact prices.

---

## How HLP Relates to the Other Hyperliquid Pages

- **[[hyperliquid-vault-architecture]]** — the deep internals: the three-strategy decomposition (liquidator / market-maker / funding harvester), P&L attribution, capacity limits, and how HLP differs from [[gmx|GLP]] / [[jupiter|JLP]] / [[dydx|dYdX]] insurance funds. Read this for *how HLP works inside*.
- **[[hlp-withdrawal-mechanics]]** — the lock-up window, withdrawal-queue/stress dynamics, and the illiquidity premium. Read this for *how depositors get in and out*.
- **[[hyperliquid-hlp-basis-arbitrage]]** — the trader's side: strategies that run *alongside* HLP, depositing for carry while hedging the tail elsewhere. Read this for *how to trade around HLP*.

This page (HLP) is the orientation hub that links the three; it deliberately summarizes rather than duplicates them.

---

## Getting the Data (CryptoDataAPI)

**Live data:**
- `GET /api/v1/hyperliquid/prices` — all mid prices
- `GET /api/v1/hyperliquid/l2-book?coin=BTC` — L2 order book snapshot
- `GET /api/v1/hyperliquid/open-interest` — all-asset open interest
- `GET /api/v1/hyperliquid/summary?coin=BTC` — all-in-one perp data

**Historical data:**
- `GET /api/v1/hyperliquid/candles?coin=BTC&interval=1h&limit=1000` — OHLCV candles
- `GET /api/v1/hyperliquid/funding-rates?coin=BTC&limit=100` — current + historical funding
- `GET /api/v1/daily/hyperliquid` — daily bulk snapshot of ~230 HL perps

```bash
curl -H "X-API-Key: $CDA_KEY" "https://cryptodataapi.com/api/v1/hyperliquid/summary?coin=BTC"
```

Auth: `X-API-Key` header. Full endpoint catalog: [[cryptodataapi-hyperliquid]].

## Related

[[hyperliquid]] · [[hyperliquid-vault-architecture]] · [[hlp-withdrawal-mechanics]] · [[hyperliquid-hlp-basis-arbitrage]] · [[hyperliquid-liquidation-engine]] · [[hyperliquid-funding-rate-microstructure]] · [[hyperliquid-order-book-microstructure]] · [[latency-and-mev-on-chain-clob]] · [[hypercore]] · [[hip-3-builder-deployed-perps]] · [[clob]] · [[market-microstructure]] · [[funding-rate]] · [[market-making]] · [[insurance-fund]] · [[maintenance-margin]]

## Sources

- (Source: [[2026-04-22-gap-finder-hyperliquid-order-books]]) — gap-finder research synthesis on Hyperliquid order books and on-chain CLOB trading.
- Hyperliquid Docs — Fees: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees
- Hyperliquid Docs — Liquidations: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/liquidations
- Hyperliquid Docs — overview (HyperCore / HyperEVM split): https://hyperliquid.gitbook.io/hyperliquid-docs
- Hyperliquid Docs — HIP-3 Builder-Deployed Perpetuals: https://hyperliquid.gitbook.io/hyperliquid-docs/hyperliquid-improvement-proposals-hips/hip-3-builder-deployed-perpetuals
