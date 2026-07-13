---
title: "Trojan Bot"
type: entity
created: 2026-05-04
updated: 2026-06-12
status: draft
tags: [crypto, solana, sniping, trading-bots, telegram]
aliases: ["Trojan", "Trojan on Solana", "@TrojanOnSolana"]
entity_type: protocol
website: "https://trojan.app"
related: ["[[pump-fun]]", "[[solana]]", "[[memecoin-sniping]]", "[[telegram-bot-trading]]", "[[bonkbot]]", "[[maestro-bot]]", "[[axiom-pro]]", "[[banana-gun]]", "[[jupiter-exchange-solana]]", "[[raydium]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Trojan Bot

**Trojan** is a [[solana]]-focused [[telegram-bot-trading|Telegram trading bot]] for sniping memecoins, with a feature set and target audience that overlap heavily with [[bonkbot]]. The two are typically named in the same breath as the dominant retail Solana TG sniper bots in the [[pump-fun]] era (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]).

---

## Overview

Trojan provides one-click sniping and trading for Solana DEXes from inside Telegram, including [[pump-fun]] launches, [[raydium]] pools, and post-migration tokens routed via [[jupiter-exchange-solana|Jupiter]]. It serves traders who want a mobile-first execution surface and is part of the broader Telegram-bot category that handles a large share of Solana memecoin volume.

Functionally, Trojan and [[bonkbot]] are close substitutes. Many active traders keep accounts on both so they have a fallback when one bot's RPC or transaction queue is congested during a hot launch.

---

## Features

- **Solana-native** Telegram bot.
- **One-click buys / sells** on Solana DEXes including [[pump-fun]] and [[raydium]].
- **Routing via [[jupiter-exchange-solana|Jupiter]]** for graduated tokens.
- **Limit orders**, configurable slippage, anti-MEV options.
- **Pump.fun scanner** for new launches, [[bonding-curve-analysis|bonding-curve]] tracking.
- **Copy trading** of specified wallets.
- **Multi-wallet** management inside the bot.
- **Referral / fee-sharing** structure.

---

## Fees

Trojan charges a per-trade fee in addition to Solana network priority fees. The exact percentage and any referral-based discount vary; verify against the live bot before committing size.

---

## How it works

1. User starts the official Trojan Telegram bot and generates an in-bot Solana wallet.
2. SOL is deposited to that wallet (custodial — Trojan holds the keys).
3. Buys are initiated by pasting a token mint or selecting a scanned [[pump-fun]] launch; the bot submits the swap, optionally bundled via Jito to reduce sandwich risk (see [[jito-bundle-sniping]]).
4. Position view shows live PnL and supports fractional sells; limit and stop orders run server-side.
5. Withdrawals to external wallets are user-initiated.

---

## Risks

- **Custodial wallet** — Trojan holds the keys to the in-bot wallet; platform compromise affects user balances.
- **Phishing clones** — impostor "Trojan" bots on Telegram are common; verify the canonical handle every time before depositing.
- **Pump.fun base rate** — the underlying memecoin market is dominated by rugs and dumps; see [[rug-detection-checklist]] and [[holder-concentration-analysis]].
- **Public-bot crowding** — every Trojan user sees the same launches; no edge over other Trojan/BonkBot users without faster custom infra.
- **Fee drag** — combined bot fee, priority tip, and slippage compound rapidly across many micro-trades.

---

## Comparison to competitors

| Bot | Chains | Position vs. Trojan |
|---|---|---|
| [[bonkbot]] | Solana | Closest direct competitor; near-identical product |
| [[maestro-bot]] | Multi-chain | Stronger copy-trade and limit-order story; broader chain coverage |
| [[banana-gun]] | Ethereum (+ expansions) | EVM-first analogue |
| [[axiom-pro]] | Solana | Web terminal rather than Telegram; richer charts and holder views |

Trojan vs. [[bonkbot]] is largely a matter of UI preference and which bot a trader's referral chain points to. Both sit in the same execution-layer slot in a typical Solana memecoin stack: scanners ([[dex-screener]] / [[birdeye]]) for discovery, Trojan or BonkBot for execution, and a [[rug-detection-checklist]] for survival.

---

## Sources

- (Source: [[2026-04-22-gap-finder-low-cap-crypto-trading-microcaps-memecoi]]) — Perplexity gap-finder research on low-cap Solana memecoin trading, naming Trojan alongside BonkBot as the leading Solana Telegram sniper bots.
- Official Trojan Telegram (verify canonical handle in-app before depositing).

---

## Related

- [[pump-fun]]
- [[solana]]
- [[memecoin-sniping]]
- [[telegram-bot-trading]]
- [[bonkbot]]
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
