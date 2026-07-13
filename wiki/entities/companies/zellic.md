---
title: "Zellic"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [crypto, defi]
entity_type: company
founded: 2022
headquarters: "Austin, Texas, USA"
website: "https://zellic.io"
aliases: ["Zellic Security", "Zellic Inc"]
related: ["[[hyperliquid]]", "[[openzeppelin]]", "[[halborn]]", "[[smart-contracts]]", "[[defi-hacks-and-exploits]]", "[[counterparty-risk]]", "[[solana]]", "[[trail-of-bits]]"]
---

Zellic is a blockchain security auditing firm founded in 2022 by Stephen Tong and Jasraj Bedi, both formerly of [[trail-of-bits|Trail of Bits]], a leading cybersecurity research firm. Zellic specializes in smart contract audits, protocol security assessments, and vulnerability research across multiple blockchain ecosystems. The firm has established a reputation for uncovering critical vulnerabilities in high-value DeFi protocols and Layer 1 infrastructure.

Zellic is privately held and notably **bootstrapped** — it has not raised institutional venture funding, which is unusual among top-tier crypto-security firms and is part of its founder-led, research-driven brand. Its team also founded the world's #1 CTF (capture-the-flag competitive-hacking) team and is a founding member of the **Security Alliance (SEAL)**, the whitehat coordination group led by samczsun.

## Overview

Zellic provides security auditing services for blockchain protocols, focusing on [[smart-contracts|smart contract]] code review, formal verification, and adversarial testing. The firm's co-founders bring deep expertise from [[trail-of-bits|Trail of Bits]], one of the most respected names in software security research, which gives Zellic credibility in an industry where audit quality varies enormously.

## Corporate Developments

- **Code4rena acquisition (August 2024):** Zellic acquired Paradigm-backed competitive-audit platform **Code4rena** — its first acquisition — and launched **Audits+**, combining Zellic's expert review with Code4rena's crowdsourced competitive-audit model. Code4rena continues to operate independently. This positions Zellic to offer both expert and crowd-sourced assurance under one roof.
- **Funding:** as of mid-2026, Zellic remained bootstrapped with no disclosed external funding round.

## Notable Audits

| Client | Scope | Significance |
|--------|-------|-------------|
| **[[hyperliquid]]** — HyperBVM | L1 blockchain (HyperCore + HyperEVM) | Security foundation for the largest [[perpetual-futures]] DEX by volume |
| **Solana Foundation** | Core [[solana]] protocol | One of the highest-TVL Layer 1 blockchains |
| **LayerZero** | Cross-chain messaging protocol | Critical infrastructure for [[cross-chain-bridges]] |
| Various DeFi protocols | Smart contracts, bridges, AMMs | Across [[ethereum]], [[solana]], and other chains |

## Hyperliquid Audit Significance

Zellic's audit of [[hyperliquid|Hyperliquid's]] HyperBVM is particularly relevant for traders because:

1. **Counterparty risk assessment**: [[hyperliquid]] processes billions in daily [[perpetual-futures|perp]] volume. The security of its L1 directly determines whether user funds are safe. A Zellic audit provides a baseline assurance, though no audit eliminates all risk.
2. **Bug bounty complement**: Hyperliquid maintains a **$1M bug bounty** program alongside the Zellic audit, creating a two-layer defense (professional audit + crowdsourced research).
3. **DEX trust hierarchy**: For traders choosing between centralized exchanges ([[binance]], [[bybit]]) and decentralized alternatives ([[hyperliquid]], [[gmx]]), audit provenance is a key factor in platform selection. Zellic's reputation strengthens Hyperliquid's security narrative.

## Trading Relevance

Audit quality directly impacts [[counterparty-risk]] assessment for DeFi protocols. Traders should evaluate:

- **Has the protocol been audited?** Unaudited protocols carry significantly higher exploit risk (see [[defi-hacks-and-exploits]])
- **Who performed the audit?** Zellic, [[openzeppelin]], [[halborn]], and Trail of Bits are considered top-tier; lesser-known firms may provide weaker assurance
- **When was the audit?** Code changes after the audit may introduce new vulnerabilities
- **Scope coverage**: Did the audit cover the full codebase or only specific components?
- **Bug bounty size**: Larger bounties ($1M+) attract skilled researchers and complement audits

Protocols that have suffered exploits despite being audited (e.g., Euler Finance, Beanstalk) demonstrate that audits reduce but do not eliminate risk. Position sizing on DeFi platforms should always account for residual smart contract risk.

## Founders

- **Stephen Tong** — Co-founder, previously at Trail of Bits. Background in vulnerability research and exploit development.
- **Jasraj Bedi** — Co-founder, previously at Trail of Bits. Security engineering and formal verification expertise.

## Related

- [[hyperliquid]] — Largest perp DEX, audited by Zellic
- [[openzeppelin]] — Competing blockchain security firm and open-source smart contract library
- [[halborn]] — Competing blockchain security firm
- [[trail-of-bits]] — Where Zellic's founders came from
- [[smart-contracts]] — The code that Zellic audits
- [[defi-hacks-and-exploits]] — What happens when audits miss vulnerabilities
- [[counterparty-risk]] — Audit quality as a component of platform risk assessment

## Sources

- Zellic acquisition of Code4rena (Aug 2024) — [The Block](https://www.theblock.co/post/312583/zellic-code4rena)
- Zellic company profile and funding status — [Tracxn](https://tracxn.com/d/companies/zellic/__w9LSbXn-MKY7ua-lqFPiUQBD520UQZgJ1c3pNjTZ6Tg); [Zellic](https://www.zellic.io/)
- Content based on Zellic public disclosures, Hyperliquid documentation, and blockchain-security industry analysis as of June 2026.
