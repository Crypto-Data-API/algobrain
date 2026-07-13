---
title: "Reentrancy Attacks"
type: concept
created: 2026-04-14
updated: 2026-06-21
status: excellent
tags: [crypto, defi, risk-management, security, smart-contracts, exploits]
aliases: ["reentrancy", "reentrancy attack", "reentrancy exploit", "re-entrancy"]
domain: [risk-management, crypto]
difficulty: intermediate
prerequisites: ["[[smart-contracts]]", "[[defi]]"]
related: ["[[smart-contract-risk]]", "[[2016-06-the-dao-hack]]", "[[2023-07-curve-finance-exploit]]", "[[2021-10-cream-finance-exploits]]", "[[flash-loan-attacks]]", "[[defi-hacks-and-exploits]]", "[[smart-contract-vulnerability-taxonomy]]", "[[ai-vulnerability-discovery]]", "[[ai-amplified-exploit-arbitrage]]"]
---

A reentrancy attack exploits the order of operations in a smart contract by re-entering a function before the previous invocation has finished updating state. The canonical pattern: a contract sends ETH (or calls an external contract), the recipient's fallback function calls back into the original contract, and because the state (e.g., balance) hasn't been updated yet, the contract sends funds again. This loop drains the contract. Reentrancy is the oldest and most historically costly class of smart contract vulnerability, responsible for [[2016-06-the-dao-hack|The DAO hack]] ($60M, 2016) and the [[2023-07-curve-finance-exploit|Curve Finance exploit]] ($73M, 2023).

## How Reentrancy Works

### The Vulnerable Pattern

```solidity
// VULNERABLE — do not use
function withdraw() public {
    uint balance = balances[msg.sender];
    require(balance > 0);
    
    // Step 1: Send ETH to caller
    (bool success, ) = msg.sender.call{value: balance}("");
    require(success);
    
    // Step 2: Update state AFTER sending
    balances[msg.sender] = 0;  // ← never reached during attack
}
```

The problem: `msg.sender.call{value: balance}("")` transfers control to the caller. If the caller is a malicious contract, its `receive()` function can call `withdraw()` again *before* `balances[msg.sender]` is set to zero. The balance check passes again (it's still the original value), and ETH is sent again. This repeats until the contract is drained or gas runs out.

### The Attack Contract

```solidity
contract Attacker {
    VulnerableContract target;
    
    function attack() external payable {
        target.deposit{value: 1 ether}();
        target.withdraw();
    }
    
    receive() external payable {
        if (address(target).balance >= 1 ether) {
            target.withdraw();  // re-enter!
        }
    }
}
```

### Step-by-Step Attack Flow

Tracing the vulnerable `withdraw()` against the attacker contract above:

| Step | Actor | Action | State after |
|------|-------|--------|-------------|
| 1 | Attacker | `deposit{value: 1 ether}()` | `balances[attacker] = 1` |
| 2 | Attacker | `withdraw()` — reads balance = 1, passes `require` | balance still 1 |
| 3 | Victim | `call{value: 1 ether}` sends 1 ETH to attacker | balance still 1 (not yet zeroed) |
| 4 | Attacker `receive()` | re-enters `withdraw()` — reads balance = **still 1** | balance still 1 |
| 5 | Victim | sends another 1 ETH | balance still 1 |
| 6 | — | steps 4–5 loop until contract drained or gas exhausted | drained |
| 7 | Victim | finally sets `balances[attacker] = 0` (too late) | 0, but funds gone |

The vulnerability is entirely about **ordering**: the external call (interaction) happens before the state update (effect). The DAO hack exploited exactly this sequence.

## The DAO Hack (June 2016) — In Depth

[[2016-06-the-dao-hack|The DAO]] was a decentralized venture-capital fund on Ethereum that raised ~$150M in ETH from thousands of contributors. Its `splitDAO` / withdraw-reward logic sent ETH to the caller **before** updating the caller's internal token balance — the classic checks-effects-interactions violation. An attacker:

1. Funded a malicious contract with DAO tokens.
2. Requested a split/withdrawal, triggering an ETH transfer to the contract.
3. The contract's fallback re-entered the withdrawal function before the DAO zeroed the balance.
4. The recursion drained ~3.6M ETH (~$60M at the time) into a "child DAO."

The fallout was historic: the Ethereum community executed a contentious **hard fork** to claw back the funds, splitting the chain into **Ethereum (ETH)** — the forked chain that reversed the hack — and **Ethereum Classic (ETC)** — the original chain preserving the "code is law" outcome. The DAO hack remains the single most consequential smart-contract exploit, both financially and for chain governance. See [[defi-hacks-and-exploits]] for the broader timeline.

## Variants

### Single-Function Reentrancy
The classic form — re-entering the same function that made the external call. The DAO hack used this pattern.

### Cross-Function Reentrancy
Re-entering a *different* function that shares the same state variables. For example, re-entering a `transfer()` function while a `withdraw()` is in progress, if both read from the same `balances` mapping.

### Cross-Contract Reentrancy
Re-entering a different contract that shares state with the vulnerable contract. Common in protocols with multiple interacting contracts (lending pools, DEXs).

### Read-Only Reentrancy
The attacker re-enters a view function to read stale state (e.g., a price or balance that hasn't been updated yet). This stale read is then used by another protocol that queries the vulnerable contract for pricing. The Curve Finance exploit's impact on protocols using Curve pool prices as oracles was a form of this.

### ERC-777 / Callback Reentrancy
Tokens that implement transfer hooks (ERC-777, ERC-1155) can trigger reentrancy during token transfers. [[2021-10-cream-finance-exploits|Cream Finance's August 2021 exploit]] ($18.8M) used the AMP token's ERC-777 callback to re-enter during a liquidation.

### Variants at a Glance

| Variant | Re-enters | Hardest part to detect | Defeated by |
|---------|-----------|------------------------|-------------|
| Single-function | Same function | Easy (classic pattern) | CEI, mutex |
| Cross-function | Different function, shared state | Medium — must track shared state | Mutex covering all functions touching the state |
| Cross-contract | Different contract, shared state | Hard — spans audit scopes | Global locks, careful composability review |
| Read-only | View function returning stale state | Hard — no state change in the view | Don't expose mid-update views; check `nonReentrant` reads |
| ERC-777 / callback | Via token transfer hook | Medium — hidden in token standard | CEI + mutex; restrict to plain ERC-20 |

## Historical Losses

| Date | Protocol | Amount | Variant |
|------|----------|--------|---------|
| 2016-06 | [[2016-06-the-dao-hack|The DAO]] | $60M | Single-function |
| 2020-04 | Uniswap + Lendf.me | $25M | ERC-777 callback |
| 2021-08 | [[2021-10-cream-finance-exploits|Cream Finance]] | $18.8M | ERC-777 callback |
| 2022-03 | Paraluni | $1.7M | Cross-function |
| 2023-07 | [[2023-07-curve-finance-exploit|Curve Finance]] | $73M | Compiler-broken reentrancy lock |
| | **Cumulative** | **$180M+** | |

## Defenses

### 1. Checks-Effects-Interactions (CEI) Pattern

The primary defense — reorder operations so state is updated *before* any external call:

```solidity
// SAFE — CEI pattern
function withdraw() public {
    uint balance = balances[msg.sender];
    require(balance > 0);
    
    // Step 1: Update state FIRST
    balances[msg.sender] = 0;
    
    // Step 2: Then send ETH
    (bool success, ) = msg.sender.call{value: balance}("");
    require(success);
}
```

Now, if the caller re-enters `withdraw()`, the balance is already zero and the `require` fails.

### 2. Reentrancy Guards (Mutex)

A modifier that prevents re-entering any guarded function:

```solidity
bool private locked;

modifier nonReentrant() {
    require(!locked, "Reentrancy");
    locked = true;
    _;
    locked = false;
}

function withdraw() public nonReentrant {
    // safe from reentrancy
}
```

OpenZeppelin's `ReentrancyGuard` is the standard implementation. Note: the [[2023-07-curve-finance-exploit|Curve exploit]] showed that this only works if the compiler correctly compiles the guard — Vyper's compiler silently broke it.

### 3. Pull Over Push

Instead of sending ETH to users, let them withdraw:

```solidity
// Instead of: msg.sender.call{value: amount}("")
// Do: pendingWithdrawals[msg.sender] += amount;
// User calls: claimWithdrawals() separately
```

This eliminates the external call entirely during state-changing operations.

### 4. Avoid ERC-777 / Callback Tokens

If a protocol doesn't explicitly need transfer hooks, restricting to standard ERC-20 tokens eliminates callback-based reentrancy.

### Defenses Compared

| Defense | What it stops | Limitations |
|---------|---------------|-------------|
| **Checks-Effects-Interactions** | Same- and cross-function reentrancy on the updated state | Requires discipline; doesn't help if a *different* contract holds the stale state |
| **Reentrancy guard (mutex)** | Re-entry into any guarded function | Only as good as the compiler (see Curve/Vyper); per-contract scope; can miss cross-contract paths |
| **Pull over push** | Reentrancy during state-changing transfers | Adds a second user transaction; doesn't cover all flows |
| **Avoid callback tokens** | ERC-777/1155 hook reentrancy | Limits token compatibility; not always possible |
| **Gas stipend (`transfer`/`send`)** | Historically capped gas to 2300, blocking re-entry | **No longer reliable** — gas costs change across hard forks (EIP-1884); not a real defense |

The modern consensus: **use CEI as the default, add a reentrancy guard as defense-in-depth, and never rely on gas stipends.**

## Detection and Auditing

Reentrancy is well-covered by tooling, yet still ships to production:

- **Static analysis** — Slither, Mythril, and Securify flag the external-call-before-state-update pattern (mapped to **SWC-107** in the SWC Registry).
- **Fuzzing / invariant testing** — Echidna and Foundry invariant tests can catch state inconsistencies a reentrant call would cause.
- **Manual review** — auditors trace every external call and ask "what reentrant path exists here?"; cross-contract and read-only variants typically require human reasoning, not just tooling.
- **Formal verification** — proves the absence of certain reentrant state violations for critical contracts.

These map into the broader [[smart-contract-vulnerability-taxonomy]] and the practices in [[smart-contract-risk]]. AI-assisted scanning is an emerging layer — see [[ai-vulnerability-discovery]].

## Why Reentrancy Persists

Despite being known since 2016, reentrancy attacks continue because:

1. **New developers** learn Solidity without internalizing CEI as a default
2. **Cross-contract reentrancy** is harder to detect — it spans multiple contracts and audit scopes
3. **Read-only reentrancy** is a newer variant that doesn't fit the classic mental model
4. **Compiler bugs** (Curve/Vyper) can silently break reentrancy guards
5. **Protocol composability** means a reentrancy-safe contract can become unsafe when composed with another contract that doesn't enforce the same guards

## Related

- [[smart-contract-risk]] — reentrancy is the most historically costly smart contract vulnerability
- [[2016-06-the-dao-hack]] — the canonical reentrancy exploit
- [[2023-07-curve-finance-exploit]] — compiler-broken reentrancy locks
- [[2021-10-cream-finance-exploits]] — ERC-777 callback reentrancy
- [[flash-loan-attacks]] — often combined with reentrancy
- [[defi-hacks-and-exploits]] — master timeline
- [[smart-contract-vulnerability-taxonomy]] — full classification (SWC-107 and beyond)
- [[ai-vulnerability-discovery]] — automated/AI-assisted detection
- [[ai-amplified-exploit-arbitrage]] — exploit-driven trading dynamics

## Sources

_Content based on The DAO post-mortem, OpenZeppelin documentation, SWC Registry (SWC-107), Vyper compiler bug disclosure, and public exploit analysis. No raw sources ingested._
