---
title: "BonkBot"
type: entity
created: 2026-05-04
updated: 2026-06-12
status: draft
tags: [crypto, solana, sniping, trading-bots, telegram]
aliases: ["Bonk Bot", "BONKbot", "@bonkbot"]
entity_type: protocol
website: "https://bonkbot.io"
related: ["[[pump-fun]]", "[[solana]]", "[[memecoin-sniping]]", "[[telegram-bot-trading]]", "[[trojan-bot]]", "[[maestro-bot]]", "[[axiom-pro]]", "[[banana-gun]]", "[[jupiter-exchange-solana]]", "[[raydium]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# BonkBot

**BonkBot** is a [[telegram-bot-trading|Telegram trading bot]] for [[solana]] that became one of the leading mobile sniping tools during the [[pump-fun]] memecoin cycle. Branded around the BONK memecoin community, it offers fast one-click buys/sells on Solana DEXes including [[pump-fun]] launches and [[raydium]] pools (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]).

---

## Overview

BonkBot is a Solana-only Telegram bot designed for retail traders who want to snipe and trade memecoins from a phone without a desktop terminal. It rose to prominence as one of the highest-volume Telegram bots on Solana during 2024-2025, alongside [[trojan-bot]], driven by the [[pump-fun]] launch boom.

The product surface is intentionally narrow: scan a contract, tap to buy, tap to sell. Most of the heavier analytics live elsewhere (e.g. [[dex-screener]], [[birdeye]]) and BonkBot is the execution layer.

---

## Features

- **Solana-native** Telegram bot (no app install).
- **One-click buys/sells** on Solana DEXes including [[pump-fun]] and [[raydium]].
- **Routing via [[jupiter-exchange-solana|Jupiter]]** for post-migration tokens.
- **Limit orders** and configurable slippage.
- **Multi-wallet** support inside the bot.
- **Copy trading** of selected wallets.
- **Pump.fun scanner** — surfaces new launches and tracks [[bonding-curve-analysis|bonding-curve]] progress.

---

## Fees

BonkBot charges a per-trade fee on top of Solana priority fees. Exact percentage and any referral discounts vary over time; check the official bot for current schedule.

---

## How it works

1. User starts the bot in Telegram (`@bonkbot_bot` or current official handle) and creates an in-bot Solana wallet.
2. SOL is deposited to that wallet (custodial — keys are held by BonkBot infrastructure).
3. To buy, the user pastes a Solana token mint or taps a scanned [[pump-fun]] launch; the bot builds and submits the swap, optionally with [[jito-bundle-sniping|Jito bundle]] tips.
4. Position view shows PnL and supports tap-to-sell at fractional sizes (25/50/100%).
5. Withdrawals to external wallets are user-initiated.

---

## Risks

- **Custodial wallet** — BonkBot holds the keys to the in-bot wallet; bot compromise or insider risk affects user balances.
- **Telegram phishing** — fake "BonkBot" clones are extremely common; always verify the official handle. A wrong-handle DM that looks identical can drain a wallet on first deposit.
- **Pump.fun base rate** — the underlying market is overwhelmingly rugs; see [[rug-detection-checklist]] and [[holder-concentration-analysis]].
- **Sniper crowding** — public Telegram bots all see the same launches; edge over other public-bot users is near zero without faster infra.
- **Fee drag** — per-trade fees compound across the dozens of micro-trades a typical memecoin session generates.

---

## Comparison to competitors

| Bot | Chains | Position vs. BonkBot |
|---|---|---|
| [[trojan-bot]] | Solana | Direct head-to-head; very similar UX, often cited together |
| [[maestro-bot]] | Multi-chain | More automation (copy-trade, limits) but less Solana-focused |
| [[banana-gun]] | Ethereum (+ expansions) | EVM-first equivalent of BonkBot |
| [[axiom-pro]] | Solana | Web terminal instead of Telegram; richer visuals, less mobile |

BonkBot and [[trojan-bot]] are typically the two reference Solana TG sniper bots; many traders run **both** so they can pivot if one bot has a stuck transaction queue or RPC issue during a hot launch.

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]) — Perplexity gap-finder research on low-cap Solana memecoin trading, identifying BonkBot and Trojan as the leading Solana Telegram sniper bots.
- https://bonkbot.io — official site (verify current canonical URL inside Telegram before depositing).

---

## Related

- [[pump-fun]]
- [[solana]]
- [[memecoin-sniping]]
- [[telegram-bot-trading]]
- [[trojan-bot]]
- [[maestro-bot]]
- [[banana-gun]]
- [[axiom-pro]]
- [[jupiter-exchange-solana]]
- [[raydium]]
- [[dex-screener]]
- [[birdeye]]
- [[bonding-curve-analysis]]
- [[holder-concentration-analysis]]
- [[rug-detection-checklist]]
- [[jito-bundle-sniping]]
