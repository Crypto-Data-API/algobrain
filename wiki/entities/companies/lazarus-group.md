---
title: "Lazarus Group"
type: entity
created: 2026-04-22
updated: 2026-06-11
status: good
tags: [crypto, defi, risk-management, history]
aliases: ["Lazarus Group", "APT38", "Hidden Cobra", "TEMP.Hermit", "BlueNoroff"]
entity_type: threat-actor
founded: 2007
headquarters: "Pyongyang, North Korea"
website: ""
related: ["[[defi-hacks-and-exploits]]", "[[counterparty-risk]]", "[[cross-chain-bridges]]", "[[ethereum]]", "[[smart-contracts]]", "[[bybit]]", "[[binance]]", "[[2026-04-01-drift-protocol-exploit]]", "[[solana-durable-nonce-governance-attacks]]", "[[2026-exploit-target-watchlist]]"]
---

Lazarus Group is a North Korean state-sponsored hacking organization, also tracked under the designations APT38, Hidden Cobra, TEMP.Hermit, and BlueNoroff. It is responsible for billions of dollars in cryptocurrency theft and is widely considered the most significant external threat actor in the crypto ecosystem. Stolen funds are believed to finance North Korea's weapons programs, making Lazarus-linked exploits a national security concern beyond the financial losses themselves.

## Key Facts

| Metric | Value |
|---|---|
| Attribution | North Korea (DPRK) Reconnaissance General Bureau |
| Active since | ~2007 (crypto-focused operations from ~2017) |
| Estimated crypto theft | ≥$6.75B cumulative through 2025 (Chainalysis lower-bound estimate) |
| Also known as | APT38, Hidden Cobra, TEMP.Hermit, BlueNoroff |
| Primary targets | [[cross-chain-bridges]], exchanges, [[defi]] protocols |
| Sanctioned by | US Treasury (OFAC), UN Security Council |

## Major Cryptocurrency Hacks

### Ronin Bridge — $625M (March 2022)

The largest crypto hack attributed to Lazarus Group targeted the Ronin Bridge, a [[cross-chain-bridges|cross-chain bridge]] connecting the Axie Infinity sidechain to [[ethereum]]. Attackers compromised 5 of 9 validator private keys through a social engineering campaign targeting Sky Mavis employees. The breach went undetected for six days. The FBI formally attributed the attack to Lazarus Group in April 2022.

### Horizon Bridge — $100M (June 2022)

Lazarus Group compromised the Harmony Horizon Bridge by obtaining 2 of 5 multi-sig keys needed to authorize transactions. The bridge's low multi-sig threshold (2-of-5) made it an attractive target. Funds were laundered through [[ethereum]] mixers including Tornado Cash.

### Bybit Exchange — ~$1.5B (February 2025)

In what became the largest single cryptocurrency theft in history, Lazarus Group exploited [[bybit|Bybit's]] multi-signature wallet infrastructure. The attack targeted the cold-to-hot wallet transfer process, manipulating the signing interface to redirect funds. Approximately $1.4-1.5 billion in [[ethereum]] and related tokens were stolen (Chainalysis attributes ~$1.5B of 2025 DPRK theft to this single incident; the FBI attributed the attack to DPRK "TraderTraitor" activity).

### Other Notable Operations

- **Atomic Wallet** (June 2023) — $100M+ stolen from individual user wallets
- **CoinEx** (September 2023) — $55M exchange hot wallet compromise
- **Stake.com** (September 2023) — $41M from the crypto gambling platform
- **Numerous DeFi exploits** across 2024-2025, comprising a significant portion of total crypto losses
- **Upbit** (November 2025) — ~$30M suspected theft from South Korea's largest crypto exchange
- **[[2026-04-01-drift-protocol-exploit|Drift Protocol]]** (April 2026) — $285-286M drained via 6-month UNC1069 social-engineering campaign + [[solana-durable-nonce-governance-attacks|Solana durable-nonce abuse]]; first major DeFi exploit attributed to UNC1069 cluster within Lazarus operations

## 2025: Record Year

Per Chainalysis, DPRK-linked hackers stole at least **$2.02 billion** in cryptocurrency in 2025 — a 51% increase year-over-year and the most severe year on record — out of ~$3.4B total crypto stolen industry-wide that year. DPRK attacks accounted for a record **76% of all service (exchange/custodian) compromises**, and the Bybit heist alone contributed ~$1.5B. The 2025 numbers brought Chainalysis's lower-bound cumulative estimate of DPRK crypto theft to **$6.75 billion**. A growing share of compromises was enabled by North Korean IT workers fraudulently embedded inside crypto companies to gain privileged access — shifting the dominant vector from pure malware toward insider/social infiltration. (Sources: [Chainalysis 2026 crypto crime update](https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/), [The Hacker News](https://thehackernews.com/2025/12/north-korea-linked-hackers-steal-202.html), [The Block](https://www.theblock.co/post/381841/north-korean-crypto-hacks-escalate-2025))

## Tactics, Techniques, and Procedures

### Social Engineering

Lazarus Group frequently uses targeted social engineering, including:

- Fake job offers sent to developers and employees at crypto companies
- Compromised or impersonated LinkedIn profiles
- Malicious npm packages and GitHub repositories
- Trojanized trading applications and DeFi tools

### Technical Exploitation

- **Private key compromise** — the most common vector, achieved through malware, social engineering, or supply chain attacks
- **Bridge targeting** — [[cross-chain-bridges]] are favored targets due to large TVL and complex multi-sig setups
- **Supply chain attacks** — compromising development tools, libraries, and CI/CD pipelines

### Money Laundering

- Chain-hopping across multiple blockchains
- Use of privacy protocols (Tornado Cash, Sinbad)
- Conversion through over-the-counter (OTC) desks
- Extended holding periods before laundering (sometimes months or years)
- Peer-to-peer exchanges and decentralized swap protocols

## Relevance to Trading

Lazarus Group activity has direct implications for crypto traders and risk management:

1. **Exchange [[counterparty-risk]]** — the group's ability to compromise major exchanges means holding funds on any centralized platform carries non-trivial tail risk
2. **Bridge risk** — [[cross-chain-bridges]] remain high-value targets; traders using bridges for arbitrage or multi-chain strategies must account for bridge exploit risk
3. **Market impact** — large-scale hacks cause immediate price drops in affected tokens and broader market contagion; the Ronin hack depressed AXS/RON prices for months
4. **Regulatory response** — Lazarus-linked hacks have accelerated sanctions on mixing services (Tornado Cash) and prompted stricter KYC requirements, affecting DeFi accessibility
5. **Fund recovery** — stolen funds are rarely recovered; unlike traditional finance, blockchain transactions are irreversible (see [[counterparty-risk]])

## Sources

No raw sources ingested for this page. External references:

- Chainalysis — "2025 Crypto Theft Reaches $3.4 Billion" (2026 crypto crime update): https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/
- The Hacker News — "North Korea-Linked Hackers Steal $2.02 Billion in 2025": https://thehackernews.com/2025/12/north-korea-linked-hackers-steal-202.html
- The Block — "North Korean crypto hacks escalate in record year of theft and laundering": https://www.theblock.co/post/381841/north-korean-crypto-hacks-escalate-2025
- Verified via WebSearch, 2026-06-10

## Related

- [[defi-hacks-and-exploits]]
- [[counterparty-risk]]
- [[cross-chain-bridges]]
- [[bybit]]
- [[ethereum]]
- [[smart-contracts]]
- [[binance]]
