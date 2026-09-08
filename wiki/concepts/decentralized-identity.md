---
title: "Decentralized Identity"
type: concept
created: 2026-07-19
updated: 2026-09-09
status: good
tags: [crypto, on-chain, privacy, security, narrative-impact]
aliases: ["DID", "Decentralized Identifiers", "On-Chain Identity", "Proof of Personhood"]
domain: [crypto, market-microstructure]
prerequisites: ["[[defi]]", "[[proof-of-humanity]]"]
difficulty: intermediate
related: ["[[worldcoin-wld]]", "[[ethereum-name-service]]", "[[proof-of-humanity]]", "[[civic]]", "[[gitcoin]]", "[[humanity]]", "[[narrative-trading]]", "[[token-unlocks]]", "[[nft]]"]
---

# Decentralized Identity

**Decentralized identity (DID)** is the set of standards and protocols that let a person or entity control a portable, cryptographically verifiable identity that no single company or government issues or can revoke — as opposed to identity today, which is fragmented across siloed logins (Google, a bank's KYC file, a government ID database) that a user does not own and cannot port. In crypto, the term covers three distinct but related primitives: **DIDs** as a technical identifier standard, **verifiable credentials** as portable attestations built on top of a DID, and **proof-of-personhood** as the specific, commercially important sub-problem of proving a DID belongs to one unique living human rather than a bot or a duplicate. It is also a recurring crypto narrative sector — DID/identity tokens rotate in and out of favor with the broader altcoin cycle the same way DeFi or gaming tokens do.

## The Core Primitives

### DIDs (Decentralized Identifiers)

A **DID** is a globally unique identifier — typically a string like `did:method:12345` — that a person or entity controls via a private key, without registering it with a central authority. The **DID method** (the part after the first colon) defines how the identifier is created, resolved, and updated; different blockchains and protocols implement their own methods. DIDs are standardized by the **W3C** (World Wide Web Consortium), the same standards body behind HTML and CSS, which gives the format a level of vendor-neutral legitimacy that most crypto-native standards lack. A DID by itself is just an address a public key can sign for — the useful part is what gets attached to it.

### Verifiable Credentials

A **verifiable credential (VC)** is a signed, tamper-evident claim about a DID — "this DID passed KYC," "this DID graduated from X," "this DID is a unique human" — issued by some party (a government, a university, a protocol) and cryptographically verifiable by anyone without contacting the issuer. VCs are the mechanism that lets a DID accumulate a portable reputation: a user proves an attribute once, receives a credential, and can present that credential (or a zero-knowledge proof derived from it, revealing only what's needed) to any number of relying parties afterward, rather than re-verifying with each one. [[civic|Civic]] and Polygon ID are examples of infrastructure built specifically around issuing and verifying VCs.

### Soulbound and Non-Transferable Tokens as an Identity Primitive

A **soulbound token (SBT)** — a term popularized by Ethereum co-founder Vitalik Buterin's 2022 "Decentralized Society" paper — is a token, usually an NFT, that is permanently bound to one wallet and cannot be sold or transferred. The idea is to use non-transferability itself as the identity signal: a credential that *can* be sold (a normal NFT badge, a purchased "verified" flair) proves nothing about the holder, but a credential that structurally *cannot* be sold is evidence the holder actually earned it. In practice, most identity systems that reference "soulbound" credentials implement the same idea with an ordinary [[nft|NFT]] or attestation whose smart contract simply blocks transfer — [[ethereum-name-service|ENS]] names are transferable NFTs and so are not soulbound in this strict sense, but the identity-adjacent SBT concept they popularized (a name as a persistent on-chain handle) is what most "on-chain reputation" projects build toward. Soulbound design is still mostly at the "proposal and small pilot" stage rather than a dominant standard — no soulbound-token system has reached anything like ENS's or Worldcoin's adoption as of this writing.

## Proof of Personhood: Why It Matters for Trading

**Proof of personhood** (also called proof-of-humanity or Sybil resistance) is the specific problem of proving a DID maps to one, and only one, unique human. This sub-problem carries outsized trading and market-structure relevance because so much of crypto's value distribution is **per-account**: airdrops, quadratic-funding grants, DAO votes, and fair-launch token allocations all implicitly assume one account roughly equals one person. That assumption breaks down the moment an attacker can cheaply spin up thousands of wallets (a **Sybil attack**) and claim thousands of shares of a distribution meant for thousands of distinct people. The wiki's dedicated [[proof-of-humanity]] page covers this problem — and the AI-era threats to it (cheap LLM-driven bot farms, deepfake KYC evasion) — in depth; this page focuses on the identity layer it sits inside.

Three competing approaches have emerged, each trading off differently between uniqueness guarantees, privacy, and hardware dependence:

| Approach | Mechanism | Strength | Weakness | Example |
|---|---|---|---|---|
| **Biometric attestation** | Scan a unique biological signal (iris), hash it, issue a credential | Strongest uniqueness guarantee; scales globally without a bootstrap problem | Requires trusting purpose-built hardware; the deepest privacy and regulatory friction of the three | [[worldcoin-wld\|Worldcoin]]'s Orb |
| **Social-graph attestation** | A person is verified if enough already-verified humans vouch for them | No hardware; pseudonymous | Bootstrap problem (who verifies the first humans?); vulnerable to collusion at the graph's edges; does not scale to billions | [[humanity\|Humanity Protocol]], the original Kleros Proof-of-Humanity |
| **Credential aggregation** | Score an address by combining many weaker, independent signals (KYC'd exchange history, GitHub activity, existing on-chain reputation, biometric partners) into a composite "humanity score" | No single point of failure; usable immediately with existing Web2/Web3 data | The score is probabilistic, not a hard uniqueness guarantee — a well-resourced Sybil can accumulate enough weak signals to pass | Gitcoin Passport |

**Worldcoin's iris-scanning approach** (see [[worldcoin-wld]] for the full entity page) is the most capital-intensive and highest-uniqueness-guarantee of the three: a physical "Orb" device captures an iris code, and the resulting World ID is close to un-fakeable at scale, at the cost of requiring users to physically visit hardware and hand over a scan of one of the most sensitive biometric identifiers available. **ENS** (see [[ethereum-name-service]]) is not a proof-of-personhood system at all — a `.eth` name is a naming/handle primitive, not a uniqueness guarantee, since one person can own many names — but it functions as crypto's most widely adopted *identity* primitive in the looser sense of a persistent, human-readable, portable handle, and it is frequently used as one input signal inside aggregated reputation scores. **Gitcoin Passport**-style aggregation sits in between: rather than betting everything on one hard biometric guarantee, it stacks many independently-weak signals (has this address been active for years, does it hold a BrightID or Worldcoin credential, does it have exchange KYC) into a single Sybil-resistance score that grant programs and quadratic-funding rounds can threshold against.

## The Privacy/Surveillance Tension

Every proof-of-personhood system faces the same structural trade-off: **the stronger the uniqueness guarantee, the more it looks like a surveillance system.** A permanent, publicly linkable identity is exactly what Sybil resistance requires — if a credential can be forgotten, refreshed, or held under a new pseudonym, an attacker just re-verifies under a new identity and the Sybil resistance evaporates. But a permanent, linkable, biometrically-rooted identity is also the precise thing privacy advocates and regulators worry about: an iris scan tied to a public wallet address, once compromised or subpoenaed, cannot be reissued the way a password can. Worldcoin's design attempts to resolve this with zero-knowledge proofs — a user proves "I hold a unique, valid World ID" without revealing which World ID, so the *verification* is unlinkable across services even though the *underlying* biometric identity is fixed and permanent for that person. Whether this genuinely delivers unlinkability in practice, versus merely making correlation harder rather than impossible, remains a live technical and regulatory debate; Worldcoin has already faced biometric-data suspensions or bans in Spain, Portugal, Brazil, Indonesia, and Kenya (see [[worldcoin-wld]] for dates), each one a direct expression of this tension playing out as enforcement action. Social-graph and credential-aggregation approaches trade away some of the uniqueness guarantee specifically to reduce this surveillance surface — a BrightID or Gitcoin Passport score reveals less about any single biometric trait, at the cost of being a softer, gameable signal.

## Trading Relevance: Identity-Gated Distributions

The recurring, tradable pattern this concept produces is the **identity-gated airdrop or token distribution**: a protocol that wants to reward real, distinct users rather than farmed wallets requires proof-of-personhood or a minimum reputation score as an eligibility condition before a token generation event or grant round. This has become a standard mitigation against the airdrop-farming industry that emerged once "qualify for an airdrop by using the protocol" became a well-known playbook — see [[token-unlocks]] for the supply-side mechanics of what happens once those tokens unlock. Traders watching a project's pre-launch phase should treat "does this distribution use a PoH/reputation gate" as a real signal about post-launch sell pressure: an ungated airdrop concentrates in professional farmers who tend to sell immediately on listing, while a gated one distributes more evenly to users with less coordinated, lower-velocity selling behavior — though a gate is never a perfect filter, since aggregated-reputation scores in particular can still be gamed by well-capitalized farming operations that accumulate the underlying weak signals at scale.

DID/identity tokens ([[ethereum-name-service|ENS]], [[worldcoin-wld|WLD]], [[civic|CVC]], and smaller aggregation and PoP projects) also trade as a loose narrative basket: they tend to catch a bid together around AI-agent and Sybil-resistance news cycles (autonomous AI agents transacting on-chain reignite the "how do you tell a human from a bot" question) and fade together when the narrative cools, independent of any individual project's fundamentals. See [[narrative-trading]] for the general framework.

## Getting the Data (CryptoDataAPI)

[[cryptodataapi|CryptoDataAPI]] has no identity-specific or Sybil-scoring endpoints — DID reputation, World ID verification counts, and airdrop-eligibility data are not part of its schema as of this writing. Its genuinely relevant surface here is standard perpetual-futures market data for the sector's two most liquid, listed identity tokens, both of which already carry their own verified endpoint documentation on their entity pages: [[worldcoin-wld|Worldcoin (WLD)]] and [[ethereum-name-service|ENS]] each trade WLD-PERP / ENS-PERP on Hyperliquid — see the `Getting the Data (CryptoDataAPI)` section on those pages for the live and historical endpoint list rather than duplicating it here.

## Related

- [[worldcoin-wld]] — biometric proof-of-personhood reference implementation (Orb, World ID, WLD token)
- [[ethereum-name-service]] — the dominant naming/handle identity primitive
- [[proof-of-humanity]] — the dedicated page on the Sybil-resistance problem and its AI-era threats
- [[civic]] — reusable verifiable-credential infrastructure (Civic Pass)
- [[gitcoin]] — the entity behind Gitcoin Passport-style credential aggregation
- [[humanity]] — social-graph proof-of-personhood
- [[narrative-trading]] — how identity tokens trade as a sector basket
- [[token-unlocks]] — supply-side consequence of airdrop distributions this page's Sybil-resistance mechanisms try to clean up
- [[nft]] — the token standard soulbound/non-transferable credentials are usually built on

## Sources

- [[worldcoin-wld]], [[ethereum-name-service]], [[civic]], [[proof-of-humanity]] — wiki pages cross-checked for the biometric, naming, credential-issuance, and Sybil-resistance facts and dates cited above
- W3C Decentralized Identifiers (DID) and Verifiable Credentials specifications — the standards referenced for the DID/VC primitives
- Vitalik Buterin, Puja Ohlhaver, Glen Weyl, "Decentralized Society: Finding Web3's Soul" (2022) — origin of the soulbound-token concept
- General knowledge of proof-of-personhood approaches (biometric, social-graph, credential-aggregation) and the identity-gated-airdrop pattern, cross-checked against the cited wiki pages; treat specific adoption-scale and regulatory-status claims as of-writing snapshots and verify against current project/regulator disclosures before relying on them
