---
title: "Phemex"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [exchange, crypto, derivatives]
aliases: ["Phemex"]
entity_type: exchange
founded: 2019
headquarters: "Singapore"
website: "https://phemex.com"
related: ["[[counterparty-risk]]", "[[defi-hacks-and-exploits]]", "[[perpetual-futures]]", "[[ethereum]]", "[[bybit]]", "[[nobitex]]"]
---

# Phemex

Phemex is a Singapore-based cryptocurrency exchange founded in 2019 by a team of former Morgan Stanley executives, including CEO Jack Tao. The exchange offers spot trading and cryptocurrency derivatives, including [[perpetual-futures|perpetual futures]] contracts. In January 2025, Phemex suffered a hot wallet private key compromise attributed to the Lazarus Group, resulting in estimated losses of $73-85 million — one of several major exchange security incidents in early 2025. Phemex covered all user losses, restored withdrawals within days, and remains operational as of June 2026.

## Key Facts

| Metric | Value |
|---|---|
| Founded | 2019 |
| Founders | Jack Tao and former Morgan Stanley team |
| Headquarters | Singapore |
| Products | Spot trading, perpetual futures, options, copy trading |
| January 2025 loss | $73-85M (hot wallet compromise) |
| Notable feature | Zero-fee spot trading (select pairs) |

## Exchange Overview

Phemex differentiated itself in the competitive crypto exchange market through several features:

- **Institutional pedigree** — founded by former Morgan Stanley executives with experience in traditional finance infrastructure
- **Derivatives focus** — competitive perpetual futures offering with up to 100x leverage
- **Zero-fee spot trading** — select trading pairs offered with no maker or taker fees (for premium members)
- **Copy trading** — social trading features allowing users to replicate experienced traders' positions

The exchange competed primarily against [[bybit]], [[binance]], and [[okx]] in the Asian derivatives market.

## January 2025 Hot Wallet Breach

On 23 January 2025 (11:30 UTC), Phemex detected unusual activity and suffered a significant security breach when attackers compromised the private keys controlling the exchange's hot wallets. The incident resulted in estimated losses between $73 million and $85 million, drained across **16 blockchains**. The attack has been attributed by multiple security researchers to North Korea's **Lazarus Group** — the same actor later blamed for the February 2025 [[bybit]] hack.

### Timeline

1. **23 Jan 2025, 11:30 UTC** — Phemex detects anomalous hot wallet outflows; on-chain monitoring services (Cyvers, ZachXBT) flag the drain in near real time; withdrawals suspended
2. **Fund extraction** — assets drained across 16 blockchain networks including [[ethereum]], BNB Chain, [[polygon|Polygon]], Optimism, Arbitrum, Base and others
3. **24 Jan 2025** — withdrawals resume (manual approval) for ETH, USDT, USDC on Ethereum
4. **25–26 Jan 2025** — BTC withdrawals resume, then Arbitrum, Optimism, BSC, Polygon, Base
5. **Feb 2025** — all withdrawal services fully restored; Phemex announced it covered all user losses from its own reserves

### Attack Details

- **Multi-chain extraction** — unlike single-chain breaches, the attacker drained hot wallets across 16 blockchains simultaneously, suggesting comprehensive key compromise rather than a smart contract exploit
- **Estimated loss** — $73-85M (estimates vary by source depending on token valuations at the time of the breach)
- **Type** — private key compromise (not a [[smart-contracts|smart contract]] vulnerability)
- **Attribution** — Lazarus Group (North Korea), per Merkle Science and other blockchain forensics analyses

### Recovery and Current Status (June 2026)

Phemex made users whole, rebuilt its custody architecture around **Fireblocks MPC** (multi-party computation) custody, and continued operating through 2025 into 2026. A February 2026 proof-of-reserves snapshot showed reserves exceeding liabilities by 13–49% across key assets. The exchange remains a mid-tier derivatives venue competing with [[bybit]], [[binance]] and [[okx]].

## Relevance to Trading

The Phemex breach has several implications for crypto traders:

1. **[[counterparty-risk]] at mid-tier exchanges** — even exchanges founded by traditional finance professionals are vulnerable to hot wallet compromises; institutional background does not guarantee institutional-grade security
2. **2025 exchange security pattern** — the Phemex breach was part of a broader pattern in early 2025 that included the [[bybit]] breach ($1.4B+) and later the [[nobitex]] breach ($90M), suggesting systemic vulnerabilities in exchange hot wallet infrastructure
3. **Multi-chain risk compounding** — exchanges supporting many blockchains must secure hot wallets on each chain, expanding the attack surface proportionally
4. **Derivatives position risk** — traders with open [[perpetual-futures|perpetual futures]] positions during the withdrawal freeze faced liquidation risk if they could not add margin or close positions

### Risk Mitigation

- Limit exchange balances to active trading capital only
- Prefer exchanges with proof-of-reserves and regular third-party security audits
- Maintain withdrawal addresses on allowlists with time-delayed changes
- Diversify exchange exposure across multiple platforms to limit single-point-of-failure risk

## Sources

- Phemex, "Hot Wallet Security Incident Update and Timeline" (official announcement) — https://phemex.com/announcements/phemex-hot-wallet-security-incident-update-and-timeline
- Merkle Science, "Hack Track: Phemex Flow of Funds Analysis" — https://www.merklescience.com/blog/hack-track-phemex-flow-of-funds-analysis
- U.Today, "Phemex Exchange Halts Withdrawals as Millions Feared Drained" (Jan 2025) — https://u.today/scam-alert-phemex-exchange-halts-withdrawals-as-millions-feared-drained
- FXEmpire, "Phemex Review 2026" — https://www.fxempire.com/exchanges/phemex
- Verified via Perplexity (sonar) and web search, 2026-06-10

## Related

- [[counterparty-risk]]
- [[defi-hacks-and-exploits]]
- [[perpetual-futures]]
- [[bybit]]
- [[nobitex]]
- [[ethereum]]
- [[binance]]
