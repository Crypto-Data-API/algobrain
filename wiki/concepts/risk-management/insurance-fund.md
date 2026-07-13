---
title: Insurance Fund
type: concept
created: 2026-04-06
updated: 2026-06-11
status: good
tags: [risk-management, crypto, exchange, leverage]
aliases: ["insurance-fund", "exchange insurance fund", "liquidation fund", "socialized loss fund"]
domain: [risk-management]
prerequisites: ["[[liquidation]]", "[[margin]]"]
difficulty: intermediate
related:
  - "[[liquidation]]"
  - "[[auto-deleveraging]]"
  - "[[counterparty-risk]]"
  - "[[liquidity-risk]]"
  - "[[systemic-risk]]"
  - "[[tail-risk]]"
  - "[[hyperliquid]]"
---

# Insurance Fund

An insurance fund is a reserve maintained by a derivatives exchange (primarily in crypto) to cover losses when a trader's position is liquidated at a price worse than their **bankruptcy price**, preventing those losses from being socialized to profitable traders. It is the first line of defense in an exchange's loss-absorption waterfall, sitting between an individual liquidation shortfall and system-wide [[auto-deleveraging|ADL]] or clawbacks.

## How It Works

1. A leveraged trader's position hits the liquidation price ([[liquidation]] engine takes over)
2. The engine attempts to close the position in the market
3. If it closes at a **better** price than the trader's bankruptcy price (the point where margin = 0), the residual margin surplus is paid **into** the insurance fund
4. If it closes at a **worse** price (e.g., during a flash crash or [[slippage|slippage]]-heavy cascade), the insurance fund pays **out** to cover the shortfall, leaving the trader at -100% of margin but no worse
5. If the insurance fund is depleted, the exchange escalates to [[auto-deleveraging|auto-deleveraging (ADL)]] — forcibly reducing the most profitable, highest-leveraged positions on the opposite side — and, as a final fallback in some designs, socialized loss / clawback across winners (Source: verified via Perplexity sonar, 2026-06-11)

So the fund is largely self-funding: it accumulates the small surpluses from well-executed liquidations during calm markets and spends them down during volatile cascades when liquidations fill below bankruptcy price.

## The Loss-Absorption Waterfall

```
Position underwater (fill worse than bankruptcy price)
        │
        ▼
  1. Insurance Fund absorbs the deficit
        │  (if depleted)
        ▼
  2. Auto-Deleveraging (ADL) — reduce opposing winning positions
        │  (if insufficient / by protocol design)
        ▼
  3. Socialized loss / clawback across profitable traders
```

Step 3 is mostly associated with older or decentralized perp designs; mainstream centralized exchanges (CEXs) rely on steps 1–2 and, in extremis, exchange capital support.

## CEX vs. On-Chain Designs

- **Binance** maintains a per-contract insurance fund plus the separate **SAFU** user-protection reserve, publicly disclosed above ~$2B in early 2024 (BTC, BNB, USDT, TUSD).
- **OKX** runs a "Risk Shield" user-protection program reported around ~$700M.
- **Bybit / OKX / others** fund standard per-contract insurance funds from liquidation fees and surplus collateral.
- **[[hyperliquid]]** has no conventional exchange-owned reserve; the community-owned **HLP vault** acts as market-maker and backstop, so liquidation inventory/execution losses are borne by the vault's LPs (publicly supplied capital deployed in-market) rather than an exchange reserve.
- **dYdX** uses a protocol-level insurance fund plus leverage-risk reduction — closer to a mutualized risk pool than a centralized reserve.

Major CEX insurance funds are rarely fully depleted; through 2022–2025 the prominent public disclosures were of fund **growth**, not depletion, with extreme volatility handled via ADL or exchange capital support rather than total exhaustion.

## Why It Matters

Without an insurance fund, every liquidation shortfall would be socialized across profitable traders through clawbacks (as happened on early crypto venues like BitMEX during sharp moves). The fund decouples individual liquidations from system-wide losses, reducing [[counterparty-risk]] for the average trader.

## Trading Relevance

Traders on leveraged crypto exchanges should monitor the insurance fund balance relative to open interest. A rapidly declining fund during volatile markets signals elevated [[counterparty-risk]] and a rising probability of [[auto-deleveraging|ADL]] — meaning a *winning* position could be force-closed without consent precisely when it is most profitable. Conversely, a large and growing fund is a (weak) proxy for exchange solvency and orderly liquidation behavior. For traders who cannot tolerate ADL on hedges, this is a reason to prefer venues with deep insurance funds, to avoid extreme leverage, and to size so that they are never the most-profitable opposing position the engine would target.

## Sources

- Cointelegraph, "Crypto exchange insurance funds surge more than $1B amid bull market" (2024) — Binance SAFU >$2B, OKX Risk Shield ~$700M disclosures
- Greeks.live / Lytera research notes on crypto-exchange insurance funds and the liquidation waterfall
- (Source: verified via Perplexity sonar, 2026-06-11) — funding mechanics, waterfall ordering, and Hyperliquid HLP vs. dYdX vs. CEX structural differences
