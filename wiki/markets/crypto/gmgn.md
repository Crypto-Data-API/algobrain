---
title: "GMGN.ai"
type: entity
created: 2026-05-04
updated: 2026-06-12
status: draft
tags: [crypto, solana, sniping, trading-bots]
aliases: ["GMGN", "gmgn.ai", "GMGN AI"]
entity_type: company
website: "https://gmgn.ai"
related:
  - "[[solana]]"
  - "[[pump-fun]]"
  - "[[memecoin-sniping]]"
  - "[[photon-sol]]"
  - "[[bullx]]"
  - "[[axiom-pro]]"
  - "[[banana-gun]]"
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# GMGN.ai

**GMGN** (gmgn.ai) is a memecoin discovery and trading terminal centred on [[solana|Solana]] but with multi-chain coverage, best known for its smart-money wallet tracking and one-click copy-trading of profitable memecoin traders. It combines a [[dex-screener|DEX-Screener]]-style new-pair feed with an integrated sniper that competes with [[photon-sol|Photon]], [[bullx|BullX]], and [[axiom-pro|Axiom Pro]].

---

## Overview

GMGN's pitch is "follow the smart money." The site indexes wallets by realized PnL on [[pump-fun|Pump.fun]] and other Solana launchpads, ranks them, and lets users mirror their trades automatically. For traders who do not want to hand-pick from the firehose of new tokens, copy-trading a curated list of profitable wallets is an alternative entry strategy to manual [[memecoin-sniping|memecoin sniping]].

Beyond copy trading, GMGN functions as a full terminal: live new-pair feed, token safety panels, holder analytics, charts, and integrated swap execution through a custodial hot wallet.

---

## Features

- **Smart-money tracking** — leaderboards of wallets ranked by PnL, win rate, and average hold time on Solana memecoins.
- **One-click copy trading** — automatically mirror trades from selected wallets with configurable size, slippage, and TP/SL rules.
- **New-pair feed** — real-time scanner across [[pump-fun|Pump.fun]], [[raydium|Raydium]], [[pumpswap|PumpSwap]], and other Solana launchpads.
- **Token safety panel** — bundles common [[rug-detection-checklist|rug-detection]] checks (LP locked, mint/freeze authority, top-holder concentration, dev holdings).
- **Multi-chain coverage** — primary focus is Solana, with support for additional EVM chains for cross-chain discovery.
- **In-browser swap** — trades execute against a custodial hot wallet without per-trade external wallet popups.
- **Limit orders, TP/SL, trailing stops** — automated exit management per position.
- **Wallet PnL viewer** — paste any wallet address to inspect its memecoin PnL history, useful for vetting copy-trade targets.
- **Telegram bot integration** — alerts and execution from mobile.

---

## Fees

GMGN charges a per-trade percentage fee on swaps routed through the platform, in addition to underlying DEX fees ([[raydium|Raydium]], [[pump-fun|Pump.fun]] bonding curve, [[jupiter-exchange-solana|Jupiter]] routing) and Solana network fees. Optional [[jito-bundle-sniping|Jito]] tips can be added for bundle inclusion. Check current fee schedule on gmgn.ai before sizing trades, since rates change.

Cost stack to model:

- GMGN platform fee.
- DEX / AMM fee.
- Solana priority fee.
- Optional Jito tip.

---

## How it works

1. **Onboarding** — user creates an account on gmgn.ai; a custodial Solana hot wallet is generated in-app. User funds it from [[phantom-wallet|Phantom]] or a CEX.
2. **Discovery path A — manual** — user browses the new-pair feed, applies filters (market cap, holders, age, bonding progress), and reviews safety panel before buying.
3. **Discovery path B — copy trading** — user opens the smart-money leaderboard, vets candidate wallets via PnL history, and configures a copy-trade rule (max size per trade, slippage cap, auto-sell rules).
4. **Execution** — copy trades fire automatically when the followed wallet transacts; manual trades execute via the in-browser swap.
5. **Management** — TP/SL and trailing stops handle exits; per-position and aggregate PnL update live.

---

## Risks

- **Copy-trading lag and adverse selection** — by the time a smart-money wallet's trade is detected and copied, price has often moved. Followed wallets may also intentionally exit into copier flow.
- **Survivorship bias in leaderboards** — top-ranked wallets are visible because they recently won; their forward edge may be much weaker than their backward PnL implies.
- **Custodial hot-wallet risk** — keys are held by the platform. Compromise or malicious update can drain balances. Keep working capital small.
- **Phishing surface** — verify the URL `gmgn.ai` directly; sniper sites are routinely cloned in ads and Telegram messages.
- **Memecoin base rate** — most [[pump-fun|Pump.fun]] tokens fail. Better tooling does not fix a poor underlying strategy (see [[memecoin-sniping]]).
- **Fee drag** — platform fee plus Jito tip plus DEX fee compounds heavily on small, frequent flips typical of memecoin trading.
- **Wash trading and farming** — some "smart-money" wallets may be wash-trading to inflate PnL and attract copy flow.

---

## Comparison to competitors

| Tool | Differentiator | Interface | Chains |
|---|---|---|---|
| **GMGN** | Smart-money tracking + copy trading | Web + Telegram | Solana primary, multi-chain |
| [[photon-sol]] | Low-latency Solana sniping UI | Web | Solana |
| [[bullx]] | Multi-chain sniper terminal | Web | Multi-chain |
| [[axiom-pro]] | Pro Solana sniping, low latency | Web | Solana |
| [[banana-gun]] | Telegram-first sniping | Telegram | Ethereum, multi-chain |
| [[maestro-bot]] | Multi-chain Telegram sniping | Telegram | Multi-chain |
| [[dex-screener]] | Pure analytics, no execution | Web | Multi-chain |
| [[birdeye]] | Solana analytics, charts | Web | Solana |

Where [[photon-sol|Photon]] and [[axiom-pro|Axiom Pro]] compete on raw execution speed, GMGN competes on discovery and follower-style trading. Many traders use GMGN for wallet research and another terminal for execution.

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]) — gap-finder research on low-cap Solana memecoin tooling
- GMGN application: https://gmgn.ai
- Pump.fun ecosystem context: https://coinmarketcap.com/view/pump-fun-ecosystem/ and https://pump.fun

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
- [[photon-sol]]
- [[bullx]]
- [[axiom-pro]]
- [[banana-gun]]
- [[maestro-bot]]
- [[dex-screener]]
- [[birdeye]]
- [[copy-trading]]
- [[smart-money-tracking]]
