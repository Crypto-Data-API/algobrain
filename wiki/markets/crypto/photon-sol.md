---
title: "Photon (Solana)"
type: entity
created: 2026-05-04
updated: 2026-06-12
status: draft
tags: [crypto, solana, sniping, trading-bots]
aliases: ["Photon", "Photon SOL", "photon-sol.tinyastro.io"]
entity_type: protocol
website: "https://photon-sol.tinyastro.io"
related:
  - "[[solana]]"
  - "[[pump-fun]]"
  - "[[memecoin-sniping]]"
  - "[[gmgn]]"
  - "[[bullx]]"
  - "[[axiom-pro]]"
  - "[[banana-gun]]"
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Photon (Solana)

**Photon** (photon-sol.tinyastro.io) is a web-based [[solana|Solana]] trading terminal designed for fast [[memecoin-sniping|memecoin sniping]] and short-horizon execution on [[pump-fun|Pump.fun]] launches and freshly migrated tokens. Unlike Telegram-bot-style snipers such as [[banana-gun|Banana Gun]] or [[maestro-bot|Maestro]], Photon ships a full browser UI with multi-pane charts, live new-pair feeds, and one-click buy/sell tied to a custodial in-app wallet.

---

## Overview

Photon is one of the dominant Solana sniper front-ends used by retail memecoin traders alongside [[gmgn|GMGN]], [[bullx|BullX]], and [[axiom-pro|Axiom Pro]]. Its core appeal is latency: orders are signed in-browser against a hot wallet held inside the app, removing the round-trip of approving each transaction in an external wallet like Phantom. This makes it competitive for sniping new [[pump-fun|Pump.fun]] tokens and post-bond [[raydium|Raydium]] migrations, where seconds determine entry price along the bonding curve.

The product targets traders who:

- Hunt [[pump-fun|Pump.fun]] launches before bonding completion (~$69k market cap migration to Raydium / [[pumpswap|PumpSwap]]).
- Want a desktop-class UI rather than a Telegram chat interface.
- Need fast manual execution combined with [[holder-concentration-analysis|holder]] and [[rug-detection-checklist|rug-detection]] filters.

---

## Features

- **Web-based UI** — full browser terminal, no desktop app or Telegram bot required.
- **Custodial in-app wallet** — pre-signed hot wallet enables one-click buys without per-trade signature prompts.
- **New-pair feed** — live stream of newly created Solana pairs from [[pump-fun|Pump.fun]], [[raydium|Raydium]], and other launchpads.
- **Token safety panel** — surfaces holder distribution, top-holder concentration, dev wallet, mint/freeze authority status (see [[rug-detection-checklist]]).
- **Limit orders and take-profit / stop-loss** — automated exits at price or market-cap thresholds.
- **Copy trading and wallet tracking** — follow specific wallets and mirror their trades, similar to [[gmgn|GMGN]] smart-money tracking.
- **Multi-wallet support** — manage several hot wallets within one session.
- **PnL tracking** — per-token and aggregate realized/unrealized PnL inside the UI.

---

## Fees

Photon charges a per-trade fee on swaps routed through its interface. The exact rate is set by the platform and applied in addition to standard Solana network fees and any [[jito-bundle-sniping|Jito]] tips users opt to add for priority inclusion. Refer to the live Photon documentation for the current rate before sizing trades, since sniper-terminal fees are repriced periodically.

Costs to budget per trade:

- Photon platform fee (percentage of swap notional).
- Solana base transaction fee (priority fee + base lamports).
- Optional [[jito-bundle-sniping|Jito tip]] for bundle inclusion.
- DEX/AMM fees (e.g., [[raydium|Raydium]], [[pump-fun|Pump.fun]] bonding curve, [[jupiter-exchange-solana|Jupiter]] routing).

---

## How it works

1. **Onboarding** — user visits photon-sol.tinyastro.io, signs in, and Photon generates an in-app Solana hot wallet. The user funds it from an external wallet ([[phantom-wallet|Phantom]], [[solflare|Solflare]], CEX withdrawal).
2. **Discovery** — the new-pair feed surfaces tokens as they launch on [[pump-fun|Pump.fun]] or migrate to [[raydium|Raydium]] / [[pumpswap|PumpSwap]]. Filters narrow by market cap, age, holder count, dev holdings, and bonding-curve progress.
3. **Pre-trade checks** — token detail panel exposes [[holder-concentration-analysis|holder concentration]], LP status, and authority renouncement to support a fast [[rug-detection-checklist|rug-detection]] pass.
4. **Execution** — buy is signed by the in-app wallet without an external popup, optionally bundled via [[jito-bundle-sniping|Jito]] to avoid sandwich MEV.
5. **Management** — limit orders, TP/SL, and trailing exits are configured per position; PnL updates live.

---

## Risks

- **Custodial hot-wallet risk** — funds sit in a wallet whose key is held by the Photon front-end. A site compromise or malicious update could drain balances. Standard mitigation: keep only sniping-size capital in the hot wallet.
- **Phishing surface** — sniper terminals are heavily impersonated. Confirm the URL `photon-sol.tinyastro.io` directly; do not click ads.
- **Memecoin base rate** — the underlying activity is sniping [[pump-fun|Pump.fun]] launches where the vast majority of tokens fail or rug. Tooling speed does not change the underlying win rate (see [[memecoin-sniping]]).
- **Fee drag** — platform fee plus Jito tip plus DEX fee compounds quickly on small notional and frequent flips.
- **MEV and failed transactions** — without a [[jito-bundle-sniping|Jito bundle]], snipes can be front-run or land too late on the bonding curve, paying a worse price.
- **Regulatory ambiguity** — custodial sniper terminals operate in a grey zone in many jurisdictions.

---

## Comparison to competitors

| Tool | Interface | Wallet model | Primary niche |
|---|---|---|---|
| **Photon** | Web UI | Custodial in-app hot wallet | Solana sniping, [[pump-fun|Pump.fun]] launches |
| [[gmgn]] | Web + Telegram | Custodial hot wallet | Smart-money tracking + memecoin discovery |
| [[bullx]] | Web UI | Custodial hot wallet | Multi-chain sniper terminal |
| [[axiom-pro]] | Web UI | Custodial hot wallet | Pro Solana sniping, low-latency execution |
| [[banana-gun]] | Telegram bot | Custodial | Ethereum-first sniping, multi-chain expansion |
| [[maestro-bot]] | Telegram bot | Custodial | Multi-chain sniping + copy trading |

Photon competes most directly with [[axiom-pro|Axiom Pro]] as a web-based Solana terminal, while [[gmgn|GMGN]] differentiates on smart-money copy trading and [[bullx|BullX]] on multi-chain coverage.

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]) — gap-finder research on low-cap Solana memecoin tooling
- Photon application: https://photon-sol.tinyastro.io
- Related context on Pump.fun bonding curve mechanics: https://pump.fun and https://docs.bitquery.io/docs/blockchain/Solana/Pumpfun/Pump-Fun-API/

---

## Related

- [[solana]]
- [[pump-fun]]
- [[pumpswap]]
- [[raydium]]
- [[jupiter-exchange-solana]]
- [[memecoin-sniping]]
- [[jito-bundle-sniping]]
- [[holder-concentration-analysis]]
- [[rug-detection-checklist]]
- [[gmgn]]
- [[bullx]]
- [[axiom-pro]]
- [[banana-gun]]
- [[dex-screener]]
- [[birdeye]]
