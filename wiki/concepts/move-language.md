---
title: "Move Language"
type: concept
created: 2026-07-19
updated: 2026-09-09
status: good
tags: [crypto, smart-contracts, layer-2, security]
aliases: ["Move", "Aptos Move", "Sui Move"]
domain: [crypto, smart-contracts]
prerequisites: ["[[smart-contracts]]"]
difficulty: advanced
related: ["[[aptos]]", "[[sui]]", "[[movement]]", "[[ethereum]]", "[[oracle-manipulation]]"]
---

# Move Language

**Move** is a resource-oriented smart-contract programming language originally developed inside Meta (Facebook) for the **Diem** stablecoin project (formerly Libra), which was shut down in 2022 before shipping. Rather than dying with Diem, Move survived as an open-source language and became the foundation for two major, independent Layer 1 blockchains built by ex-Diem engineers — **[[aptos|Aptos]]** and **[[sui|Sui]]** — each of which forked the language into its own divergent dialect, plus smaller networks such as **[[movement|Movement]]**, which brings a Move execution environment to Ethereum settlement as a modular network. Move's core design idea is to treat digital assets as a distinct, first-class type the language itself protects — structurally, at compile time — from the class of bugs that has produced some of the most expensive exploits in Ethereum's Solidity-based ecosystem.

## The Core Idea: Resources as a First-Class Type

In Move, a **resource** is a special kind of type with two rules baked directly into the language's type system, not merely enforced by convention or a library:

1. **A resource cannot be copied.** Ordinary data (an integer, a string) can be freely duplicated by assignment; a resource type explicitly cannot be. If a resource represents 100 tokens, the compiler will not let a program accidentally produce two references that each claim to own that same 100 tokens.
2. **A resource cannot be implicitly discarded.** A resource must be explicitly *moved* — transferred to a new owner, stored, or destroyed through a sanctioned function — and the compiler rejects any code path where a resource value goes out of scope without being accounted for. There is no way to "drop" a resource on the floor by accident the way an unhandled reference or an unreachable code path can silently lose track of value in other languages.

Together, these two rules give the language its name: value in Move does not get copied or deleted, it only ever gets **moved** from one place to another, and the compiler enforces this globally, across an entire program, before the code ever runs. This is what "resource-oriented" means in practice — a token, an NFT, or any other asset is represented as a resource, and the language makes it structurally impossible to write a program that duplicates that asset out of thin air or silently loses track of it, because the type checker refuses to compile code that would do either.

## What This Prevents

The classes of bugs this design targets are exactly the ones that have produced some of the largest and most embarrassing losses in Solidity-based DeFi:

- **Double-spending a token object.** In an account/balance-mapping model, "the same token spent twice" is prevented only by careful bookkeeping in the contract's logic — a mistake in how a balance mapping is updated (a classic pattern behind several reentrancy exploits) can let an attacker spend value that should have already been deducted. In Move, a resource representing a token can only exist in one place at a time by construction; there is no code path that produces two live copies of the same resource for the type checker to allow.
- **Accidentally leaving an asset unaccounted for.** A common source of value-destroying bugs in other languages is a code path that receives or creates an asset and then, through an unhandled branch or an early return, simply fails to store, transfer, or return it — the asset is not technically "gone" from storage, but the contract's own logic loses track of it, effectively burning it by accident. Move's mandatory-move rule makes this a compile-time error rather than a runtime bug: the compiler will not accept a function that lets a resource value fall out of scope unaccounted for.

## Contrast with Solidity's Account/Balance-Mapping Model

Solidity, Ethereum's dominant smart-contract language, represents a token balance the ordinary way any general-purpose language represents a number: as an entry in a **mapping** from an address to an integer (`mapping(address => uint256) balances`). Nothing in Solidity's type system understands that this integer represents an asset that should never be duplicated or silently lost — that guarantee exists only insofar as the contract's own logic correctly increments and decrements the mapping on every transfer, and correctly rejects every code path that could double-count or misplace a balance. This is a **convention enforced by code review and testing**, not a property the compiler can check, which is precisely why asset-accounting bugs — reentrancy attacks that drain a balance before it is decremented, integer overflow/underflow miscounting a balance, access-control gaps that let an unauthorized caller modify a mapping directly — have been recurring, costly categories of Solidity exploit for years. Move does not eliminate the need for careful contract logic in general, but it does remove an entire category of *asset-accounting* bugs specifically from the set of mistakes a Move contract's logic can make, by making the token itself a typed value the compiler tracks rather than a bare integer a programmer must remember to manage correctly.

**The honest limit of this guarantee** is important to state plainly: Move's resource safety prevents *asset-accounting* bugs specifically — it does not make a contract bug-free in general. Arithmetic errors, flawed pricing math, access-control mistakes, and business-logic flaws are all still possible in Move, because none of those bug classes involve a resource being copied or dropped incorrectly — they involve a *correctly-accounted-for* resource being valued or authorized incorrectly. The **Cetus exploit on Sui** (May 2025, roughly $223M drained from the network's largest DEX) is the clearest real-world illustration of this limit: the vulnerability was a u256 integer-overflow bug in the protocol's concentrated-liquidity math, not a failure of Move's resource-safety guarantees — the resources involved were tracked correctly by the language the entire time, while the flawed math around them mispriced a swap. See [[sui]] for the full incident history. Move narrows the attack surface; it does not close it.

## Aptos Move vs. Sui Move: A Diverged Fork

Aptos and Sui both started from the same Move lineage but have since diverged into genuinely different dialects with different underlying data models, and neither should be assumed to behave identically to the other:

| | **Aptos Move** | **Sui Move** |
|---|---|---|
| **Data model** | Account-centric — assets are held under global accounts, closer in spirit to how most other chains organize state | Object-centric — every on-chain asset is an independently addressed object with a unique ID and explicit ownership, not an entry under a shared account ledger |
| **Parallel execution** | Block-STM — transactions execute optimistically and in parallel across CPU cores, then are validated for read/write conflicts and re-executed if they conflict | Owned-object fast path plus Mysticeti consensus for shared objects — transactions touching only independent, owned objects skip full consensus entirely; only transactions over objects multiple parties can write to need the consensus layer |
| **Why it matters** | Parallelism is discovered *at runtime* via conflict detection, which works well for arbitrary account-touching workloads | Parallelism is *structural* — the object model makes data dependencies explicit before execution starts, letting genuinely independent transactions (like a simple transfer) finalize in well under a second without touching consensus at all |

Both approaches pursue the same underlying goal — escaping the fully sequential execution that constrains account-based chains like unmodified [[ethereum|Ethereum]] — but they get there through different architectural bets, and Move code written against one dialect's object/account model is not directly portable to the other without adaptation. See [[aptos]] and [[sui]] for each chain's full protocol detail, including how each markets its execution-model choice as its competitive edge within the shared "Move L1" narrative basket the two are frequently traded against each other in.

## Beyond Aptos and Sui

Move's reach now extends past the two chains that inherited it directly from the Diem team. **[[movement|Movement]]** is a smaller network that brings a Move-based execution environment to an Ethereum-settled, modular Layer-2-style architecture, explicitly pitching Move's resource-oriented safety model as a value proposition for teams building on Ethereum's security and liquidity base rather than a standalone Move L1. This makes Move, as of this writing, a language whose adoption spans at least three genuinely independent execution environments with different trust and settlement assumptions, rather than a single chain's proprietary toolchain — closer in spirit to how Solidity runs across many separate EVM chains than to a language tied permanently to one network.

## Trading Relevance

Move itself is not a directly tradable asset — the trading relevance runs through the chains built on it. [[aptos|Aptos]] (APT) and [[sui|Sui]] (SUI) are routinely traded as a relative-value pair specifically *because* they share the Move lineage and compete for the same "high-performance Move L1" narrative and developer mindshare, even though their underlying object models differ; see each token's own page for its current pair-trade framing, funding, and liquidity profile. A disclosed Move-language-level vulnerability (as opposed to an application-level bug like Cetus's) would be a genuine, correlated negative catalyst across every Move chain simultaneously, since it would call the shared safety claim into question network-wide rather than implicating a single protocol — no such language-level vulnerability has been publicly disclosed as of this writing, and the Cetus incident specifically was confirmed by both Sui's own postmortem coverage and independent security-firm analysis to be an application-math bug rather than a Move-language flaw.

## Related

- [[aptos]] — Aptos Move (account-centric model), Block-STM parallel execution, and APT trading profile
- [[sui]] — Sui Move (object-centric model), Mysticeti consensus, and the Cetus exploit case study
- [[movement]] — a third, Ethereum-settled Move execution environment beyond the two Move L1s
- [[ethereum]] — the account/balance-mapping (Solidity/EVM) model Move's resource-oriented design is most directly contrasted against
- [[oracle-manipulation]] — a related but distinct DeFi bug class (price-feed manipulation) that Move's resource safety does not address, illustrating the boundary of what "asset safety" does and doesn't cover

## Sources

- [[aptos]], [[sui]], [[movement]] — wiki entity pages cross-checked for the Aptos-vs-Sui data-model contrast, Block-STM and Mysticeti descriptions, the Cetus exploit's root cause, and Movement's Ethereum-settled positioning
- General knowledge of Move's origin at Meta/Diem, its resource-oriented type-system design, and the general contrast between resource-typed and account/balance-mapping asset representation, cross-checked against the cited wiki pages
