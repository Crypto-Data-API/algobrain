---
title: "Nobitex"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [exchange, crypto]
aliases: ["Nobitex"]
entity_type: exchange
founded: 2017
headquarters: "Tehran, Iran"
website: "https://nobitex.ir"
related: ["[[counterparty-risk]]", "[[defi-hacks-and-exploits]]", "[[binance]]", "[[ethereum]]"]
---

# Nobitex

Nobitex is Iran's largest cryptocurrency exchange by trading volume, providing fiat-to-crypto on-ramps for Iranian users in a market largely isolated from global financial infrastructure due to international sanctions. In June 2025, the exchange suffered a catastrophic hot wallet breach resulting in approximately $90 million in losses, highlighting persistent security vulnerabilities at exchanges operating in sanctioned or underregulated jurisdictions.

## Key Facts

| Metric | Value |
|---|---|
| Founded | ~2017 |
| Headquarters | Tehran, Iran |
| Market position | Largest crypto exchange in Iran |
| Primary pairs | BTC/IRR, ETH/IRR, USDT/IRR |
| June 2025 loss | ~$90M (hot wallet compromise) |
| Regulatory environment | Iranian jurisdiction; subject to US/EU sanctions |

## Exchange Overview

Nobitex operates as the dominant cryptocurrency exchange within Iran, a market with significant demand for crypto due to:

- **Sanctions evasion** — Iranian individuals and businesses use crypto to circumvent SWIFT disconnection and international banking restrictions
- **Currency depreciation** — the Iranian rial has experienced severe inflation, driving demand for dollar-denominated stablecoins (particularly USDT)
- **Capital controls** — domestic financial restrictions push capital into crypto as an alternative store of value

The exchange supports trading in major cryptocurrencies including [[bitcoin|Bitcoin]], [[ethereum|Ethereum]], and various stablecoins against the Iranian rial (IRR).

## June 2025 Hot Wallet Breach

On **June 18, 2025** — during the Israel–Iran war of June 2025 — Nobitex lost approximately $90 million (estimates range from $81M to $100M) when its hot wallet infrastructure was compromised. Key details:

- **Attribution** — the pro-Israel hacking group **Predatory Sparrow (Gonjeshke Darande)** claimed responsibility, framing the attack as retaliation for Nobitex's alleged role in IRGC-linked sanctions evasion and terror finance
- **Attack vector** — compromise of the exchange's hot wallet infrastructure and private keys
- **Funds burned, not stolen** — the attackers sent the assets to vanity addresses containing anti-IRGC slogans (e.g., "F***iRGCTerrorists") for which no private keys can exist, deliberately **destroying ~$90M** as a political statement rather than profiting
- **Source code leak** — two days later (June 20, 2025) the group published Nobitex's entire source code, infrastructure documentation, and internal privacy R&D, exposing operational details of Iran's largest crypto platform
- **Detection** — on-chain analysts identified abnormal outflows before the exchange publicly confirmed the breach
- **Impact on users** — withdrawals were suspended and a wallet-system migration was forced; user balances were honored from reserves

### Aftermath and Recovery (2025–2026)

- Withdrawals resumed for verified users from **June 30, 2025**; spot trading resumed **July 9, 2025**, and Nobitex announced full restoration of operations in July after rebuilding its technical infrastructure, drawing partly on bitcoin reserves including consolidated dormant mining-linked wallets
- Confidence damage was severe: incoming transaction volumes fell **more than 70% year-over-year** in the aftermath
- In **January 2026**, US OFAC sanctioned two UK-based platforms linked to the IRGC — the first direct designations of digital-asset exchanges tied to Iran's military apparatus; Nobitex was referenced in connection with those designations but was not itself designated
- As of mid-2026 Nobitex continues to operate as Iran's dominant exchange, with its leaked source code remaining a standing security liability

### Significance

The Nobitex breach was notable for several reasons:

1. **Emerging market vulnerability** — exchanges operating in sanctioned or underregulated jurisdictions often lack the security infrastructure, insurance, and regulatory oversight common at major global exchanges like [[binance|Binance]] or [[coinbase|Coinbase]]
2. **Hot wallet risk** — the breach reinforced that hot wallet private key management remains the single largest point of failure for centralized exchanges (see also [[bybit]] and [[phemex]] breaches in 2025)
3. **Limited recourse** — Iranian sanctions complicate law enforcement cooperation and fund recovery efforts, making stolen assets effectively unrecoverable
4. **Concentration risk** — as Iran's dominant exchange, Nobitex's breach affected a disproportionate share of Iranian crypto holders

## Relevance to Trading

Nobitex's breach provides several risk management lessons:

1. **[[counterparty-risk]] in emerging markets** — exchanges in sanctioned or underregulated jurisdictions carry elevated custodial risk due to weaker security standards and limited legal recourse
2. **Hot wallet exposure** — traders should assess what percentage of an exchange's assets are held in hot wallets versus cold storage; Nobitex's losses suggest inadequate cold storage practices
3. **Geographic risk premium** — exchanges operating under sanctions face additional operational constraints that can compromise security (difficulty hiring top security talent, limited access to institutional custody solutions)
4. **Self-custody imperative** — the breach reinforces the case for minimizing exchange-held balances, particularly on smaller or regionally isolated platforms

## Sources

No raw sources ingested for this page. External references:

- Fortune, "Israel hacks Iranian crypto exchange for $90 million" (Jun 18, 2025) — https://fortune.com/crypto/2025/06/18/nobitex-gonjeshke-darande-predatory-sparrow-iran-israel-hack/
- Halborn, "Explained: The Nobitex Hack (June 2025)" — https://www.halborn.com/blog/post/explained-the-nobitex-hack-june-2025
- TRM Labs, "Inside the Nobitex Breach: What the Leaked Source Code Reveals" — https://www.trmlabs.com/resources/blog/inside-the-nobitex-breach-what-the-leaked-source-code-reveals-about-irans-crypto-infrastructure
- CyberScoop, "Iran's financial sector takes another hit as largest crypto exchange is targeted" — https://cyberscoop.com/iran-nobitex-cyberattack-predatory-sparrow/
- AMLBot, "Breaking Down the Nobitex Hack: Timeline, Impact, and Key Takeaways" — https://blog.amlbot.com/breaking-down-the-nobitex-hack-timeline-impact-and-key-takeaways/
- GetBlock Research, "12 days of war: how the Iranian Nobitex exchange recovered after the hack" — https://getblock.net/en/research/12-days-of-war-how-the-iranian-nobitex-exchange-recovered-after-the-hack
- Verified via web search, 2026-06-10

## Related

- [[counterparty-risk]]
- [[defi-hacks-and-exploits]]
- [[bybit]]
- [[phemex]]
- [[binance]]
- [[ethereum]]
