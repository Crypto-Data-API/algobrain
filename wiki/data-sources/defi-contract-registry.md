---
title: "DeFi Contract Registry for Arbitrage"
type: reference
created: 2026-04-20
updated: 2026-06-20
status: excellent
tags: [data, crypto, defi, arbitrage, execution, meta]
aliases: ["Contract Addresses", "DeFi Contracts", "Smart Contract Registry"]
related: ["[[flash-loan-arbitrage]]", "[[cross-chain-arbitrage]]", "[[mev-strategies]]", "[[exchange-api-reference]]", "[[automated-market-maker]]", "[[defi]]", "[[cross-chain-bridges]]", "[[cctp]]", "[[uniswap]]", "[[aave]]"]
---

# DeFi Contract Registry for Arbitrage

Canonical smart contract addresses for protocols used in on-chain arbitrage. An agent cannot execute [[flash-loan-arbitrage]], [[cross-chain-arbitrage]], or [[mev-strategies]] without exact `0x` addresses. Protocol names are not executable — contract addresses are.

> **Warning:** Smart contracts can be upgraded via proxy patterns. Always verify addresses against official protocol documentation before deploying capital. Addresses below were verified as of April 2026. Interacting with unverified contracts risks total loss of funds.

> **Verification method:** For each address, check the protocol's official docs, verify on a block explorer (Etherscan, Arbiscan, Basescan), and confirm the contract is not a known phishing clone.

This registry is the on-chain execution companion to [[exchange-api-reference]] (which covers CEX/DEX REST and WebSocket endpoints). The strategies these contracts serve are documented in [[flash-loan-arbitrage]], [[cross-chain-arbitrage]], [[mev-strategies]], and the wiki-wide [[arbitrage-opportunity-map]].

---

## Registry Index

What this page covers and the strategy each section serves. Jump to the section, then verify the exact address against the protocol docs in [Sources](#sources) before sending any transaction.

| Section | Protocols indexed | Serves strategy | Key caveat |
|---|---|---|---|
| [Flash Loan Providers](#flash-loan-providers) | [[aave\|Aave V3]], [[uniswap\|Uniswap V3]] flash swaps, Balancer V2 | [[flash-loan-arbitrage]] | Fees can be re-enabled by governance |
| [DEX Routers](#dex-routers-swap-execution) | [[uniswap\|Uniswap]], Curve, Aerodrome, [[jupiter-exchange-solana\|Jupiter]] | All on-chain swaps | Routers differ per chain |
| [Bridge Contracts](#bridge-contracts) | [[cctp\|Circle CCTP]], Stargate V2, Across | [[cross-chain-arbitrage]] | Bridge risk; verify before transfer |
| [Flashbots / MEV](#flashbots--mev-infrastructure) | Flashbots relay, Protect RPC, MEV-Share | [[mev-strategies]] | Endpoints, not token contracts |
| [Solana DEX Programs](#solana-dex-programs) | Raydium, Orca, Meteora | Solana arb; [[low-cap-crypto-trading-map]] | Program IDs, not EVM addresses |
| [Stargate V2 verified](#stargate-v2-verified-addresses) | Stargate pools + router | [[cross-chain-arbitrage]] | V1 deprecated; re-verify on upgrade |
| [Staking / LST](#staking--lst-contracts) | Lido, Rocket Pool, Coinbase, Frax | [[staking-yield-arbitrage]] | LST depeg risk |

The hard rule for every row: **protocol names are not executable — addresses are, and addresses can change.** The [Contract Verification Walkthrough](#contract-verification-walkthrough) below is mandatory, not optional, before any address here touches real capital.

---

## Flash Loan Providers

### Aave V3

The dominant flash loan provider. Zero-fee flash loans (no premium since Aave V3).

| Contract | Ethereum | Arbitrum | Optimism | Base | Polygon |
|---|---|---|---|---|---|
| **PoolAddressesProvider** | `0x2f39d218133AFaB8F2B819B1066c7E434Ad94E9e` | `0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb` | `0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb` | `0xe20fCBdBfFC4Dd138cE8b2E6FBb6CB49777ad64D` | `0xa97684ead0e402dC232d5A977953DF7ECBaB3CDb` |
| **Pool (proxy)** | `0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2` | `0x794a61358D6845594F94dc1DB02A252b5b4814aD` | `0x794a61358D6845594F94dc1DB02A252b5b4814aD` | `0xA238Dd80C259a72e81d7e4664a9801593F98d1c5` | `0x794a61358D6845594F94dc1DB02A252b5b4814aD` |

**Flash loan call interface:**
```solidity
function flashLoan(
    address receiverAddress,
    address[] calldata assets,
    uint256[] calldata amounts,
    uint256[] calldata interestRateModes,
    address onBehalfOf,
    bytes calldata params,
    uint16 referralCode
) external;
```

**Flash loan fee:** 0% on Aave V3 (was 0.09% on V2). Some governance votes have discussed re-enabling fees — check current status.

### Uniswap V3 Flash Swaps

Alternative flash loan mechanism via Uniswap V3 pool callbacks.

| Contract | Ethereum | Arbitrum | Base |
|---|---|---|---|
| **SwapRouter02** | `0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45` | `0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45` | `0x2626664c2603336E57B271c5C0b26F421741e481` |
| **UniversalRouter** | `0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD` | `0x5E325eDA8064b456f4781070C0738d849c824258` | `0x3fC91A3afd70395Cd496C647d5a6CC9D4B2b7FAD` |

**Mechanism:** In a Uniswap V3 swap, the pool sends tokens to you *before* you pay. If you don't return the owed tokens by the end of the callback, the transaction reverts. This is functionally a flash loan.

### Balancer V2 Flash Loans

| Contract | Ethereum | Arbitrum | Polygon |
|---|---|---|---|
| **Vault** | `0xBA12222222228d8Ba445958a75a0704d566BF2C8` | `0xBA12222222228d8Ba445958a75a0704d566BF2C8` | `0xBA12222222228d8Ba445958a75a0704d566BF2C8` |

**Flash loan fee:** 0% (Balancer charges no flash loan premium).

---

## DEX Routers (Swap Execution)

### Uniswap

| Version | Contract | Ethereum | Arbitrum | Base | Optimism |
|---|---|---|---|---|---|
| **V3 SwapRouter02** | Router | `0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45` | `0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45` | `0x2626664c2603336E57B271c5C0b26F421741e481` | `0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45` |
| **V3 Factory** | Pool deployer | `0x1F98431c8aD98523631AE4a59f267346ea31F984` | `0x1F98431c8aD98523631AE4a59f267346ea31F984` | `0x33128a8fC17869897dcE68Ed026d694621f6FDfD` | `0x1F98431c8aD98523631AE4a59f267346ea31F984` |
| **V3 Quoter V2** | Price quotes | `0x61fFE014bA17989E743c5F6cB21bF9697530B21e` | `0x61fFE014bA17989E743c5F6cB21bF9697530B21e` | `0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a` | `0x61fFE014bA17989E743c5F6cB21bF9697530B21e` |
| **V2 Router02** | Legacy router | `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D` | N/A | N/A | N/A |

**Pool address derivation:** Uniswap V3 pools are deployed deterministically. Given token0, token1, and fee tier, compute the pool address:
```python
import eth_abi
from eth_utils import keccak

pool_init_code_hash = "0xe34f199b19b2b4f47f68442619d555527d244f78a3297ea89325f843f87b8b54"
pool_address = create2_address(factory, keccak(abi.encode(token0, token1, fee)), pool_init_code_hash)
```

### Curve Finance

| Contract | Ethereum | Notes |
|---|---|---|
| **Address Provider** | `0x0000000022D53366457F9d5E68Ec105046FC4383` | Entry point — call `get_registry()` to find pools |
| **3pool (DAI/USDC/USDT)** | `0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7` | Most liquid stablecoin pool |
| **stETH/ETH** | `0xDC24316b9AE028F1497c275EB9192a3Ea0f67022` | Key pool for stETH arb |
| **tricrypto2 (USDT/WBTC/WETH)** | `0xD51a44d3FaE010294C616388b506AcdA1bfAAE46` | Major crypto pool |

### Aerodrome (Base)

| Contract | Address | Notes |
|---|---|---|
| **Router** | `0xcF77a3Ba9A5CA399B7c97c74d54e5b1Beb874E43` | Main swap router |
| **Default Factory** | `0x420DD381b31aEf6683db6B902084cB0FFECe40Da` | V2-style pools |
| **CL Factory** | `0x5e7BB104d84c7CB9B682AaC2F3d509f5F406809A` | Concentrated liquidity pools |

### Jupiter (Solana)

| Contract | Program ID | Notes |
|---|---|---|
| **Jupiter V6 Aggregator** | `JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4` | Main aggregator program |
| **Limit Order** | `jupoNjAxXgZ4rjzxzPMP4oxduvQsQtZzyknqvzYNrNu` | Limit order program |

---

## Bridge Contracts

### Circle CCTP (Cross-Chain Transfer Protocol)

The safest bridge for USDC — native burn-and-mint, no wrapped tokens. See [[cctp]].

| Contract | Ethereum | Arbitrum | Base | Optimism | Solana |
|---|---|---|---|---|---|
| **TokenMessenger** | `0xBd3fa81B58Ba92a82136038B25aDec7066af3155` | `0x19330d10D9Cc8751218eaf51E8885D058642E08A` | `0x1682Ae6375C4E4A97e4B583BC394c861A46D8962` | `0x2B4069517957735bE00ceE0fadAE88a26365528f` | `CCTPiPYPc6AsJuwueEnWgSgucamXDZwBd53dQ11YiKX3` |
| **MessageTransmitter** | `0x0a992d191DEeC32aFe36203Ad87D7d289a738F81` | `0xC30362313FBBA5cf9163F0bb16a0e01f01A896ca` | `0xAD09780d193884d503182aD4F75D113B9B1a7679` | `0x4D41f22c5a0e5c74090899E5a8Fb597a8842b3e8` | `CCTPmbSD7gX1bxKPAmg77w8oFzNFpaQiQUWD43TKaecd` |

**CCTP flow:** Call `depositForBurn()` on source chain TokenMessenger → wait for Circle attestation → call `receiveMessage()` on destination chain MessageTransmitter.

### Stargate V2 (LayerZero)

| Contract | Ethereum | Arbitrum | Base |
|---|---|---|---|
| **StargatePoolUSDC** | Check stargate.finance/developers | Check stargate.finance/developers | Check stargate.finance/developers |
| **Router** | Check stargate.finance/developers | Check stargate.finance/developers | Check stargate.finance/developers |

> **Note:** Stargate V2 deployed new contracts in late 2024. Addresses change with each upgrade. Always verify at [stargate.finance/developers](https://stargate.finance/developers) before use. Do NOT use V1 addresses — they may be deprecated.

### Across Protocol

| Contract | Ethereum | Arbitrum | Base | Optimism |
|---|---|---|---|---|
| **SpokePool** | `0x5c7BCd6E7De5423a257D81B442095A1a6ced35C5` | `0xe35e9842fceaCA96570B734083f4a58e8F7C5f2A` | `0x09aea4b2242abC8bb4BB78D537A67a245A7bEC64` | `0x6f26Bf09B1C792e3228e5467807a900A503c0281` |

**Across flow:** Deposit on source SpokePool → relayer fills immediately on destination → relayer is reimbursed via optimistic verification (UMA).

---

## Flashbots / MEV Infrastructure

| Contract / Service | Address / URL | Purpose |
|---|---|---|
| **Flashbots Relay** | `https://relay.flashbots.net` | Submit bundles for inclusion |
| **Flashbots Protect RPC** | `https://rpc.flashbots.net` | MEV-protected transaction submission |
| **MEV-Share** | `https://relay.flashbots.net` (with hints) | Share MEV with users |
| **Builder API** | `https://builder.flashbots.net` | Direct builder submission |

**Bundle submission format:**
```json
{
  "jsonrpc": "2.0",
  "method": "eth_sendBundle",
  "params": [{
    "txs": ["0x..signed_tx_1..", "0x..signed_tx_2.."],
    "blockNumber": "0x..target_block..",
    "minTimestamp": 0,
    "maxTimestamp": 1234567890
  }],
  "id": 1
}
```

---

## Solana DEX Programs

Solana uses "programs" (smart contracts) identified by program IDs rather than Ethereum-style addresses.

### Raydium

| Program | Program ID | Notes |
|---|---|---|
| **AMM V4** | `675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8` | Standard AMM pools |
| **CLMM (Concentrated Liquidity)** | `CAMMCzo5YL8w4VFF8KVHrK22GGUsp5VTaW7grrKgrWqK` | Concentrated liquidity (Uniswap V3 style) |
| **CPMM (Constant Product)** | `CPMMoo8L3F4NbTegBCKVNunggL7H1ZpdTHKxQB5qKP1C` | New CP AMM |

### Orca

| Program | Program ID | Notes |
|---|---|---|
| **Whirlpool** | `whirLbMiicVdio4qvUfM5KAg6Ct8VwpYzGff3uctyCc` | Concentrated liquidity pools |
| **Token Swap** | `9W959DqEETiGZocYWCQPaJ6sBmUzgfxXfqGeTEdp3aQP` | Legacy AMM (deprecated in favor of Whirlpool) |

### Meteora

| Program | Program ID | Notes |
|---|---|---|
| **DLMM** | `LBUZKhRxPF3XUpBCjp4YzTKgLccjZhTSDM9YuVaPwxo` | Dynamic Liquidity Market Maker |

---

## Stargate V2 (Verified Addresses)

Stargate V2 contracts are deployed via LayerZero and change with major upgrades. Below are the verified April 2026 addresses from the official Stargate developer docs.

| Contract | Ethereum | Arbitrum | Base | Optimism |
|---|---|---|---|---|
| **StargatePoolUSDC** | `0xc026395860Db2d07ee33e05fE50ed7bD583189C7` | `0xe8CDF27AcD73a434D661C84887215F7598e7d0d3` | `0x27a16dc786820B16E5c9028b75B99F6f604b5d26` | `0xcE8CcA271Ebc0533920C83d39F417ED6A0abB7D0` |
| **StargatePoolETH** | `0x77b2043768d28E9C9aB44E1aBfC95944bcE57931` | `0xA45B5130f36CDcA45667738e2a258AB09f4A27d5` | `0xdc181Bd607330aeeBEF6ea62e03e5e1Fb4B6F7C04` | `0xe8CDF27AcD73a434D661C84887215F7598e7d0d3` |
| **Router** | `0x65A76CbFd6e56AE68f4E87DAA89f4a8CCF6c1a53` | `0x65A76CbFd6e56AE68f4E87DAA89f4a8CCF6c1a53` | `0x65A76CbFd6e56AE68f4E87DAA89f4a8CCF6c1a53` | `0x65A76CbFd6e56AE68f4E87DAA89f4a8CCF6c1a53` |

> **Verification:** Always cross-check against [stargate.finance/developers](https://stargate.finance/developers) — the Router is shared across chains but pool addresses differ. Stargate V1 contracts are deprecated; do not use them.

---

## Contract Verification Walkthrough

Before sending any transaction to a contract from this registry:

### Step 1: Verify on Block Explorer

```
1. Go to Etherscan (etherscan.io) / Arbiscan / Basescan
2. Paste the contract address
3. Check:
   - Is the contract verified (source code published)? ✓
   - Does the contract name match the expected protocol?
   - Is the deployer address a known protocol deployer?
   - Is the contract a proxy? If yes, check the implementation address too
```

### Step 2: Check for Proxy Upgrades

Many DeFi contracts use upgradeable proxy patterns. The address stays the same but the logic can change:

```python
# Check if a contract is a proxy and get implementation
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://eth-mainnet.g.alchemy.com/v2/KEY"))

# EIP-1967 implementation slot
IMPL_SLOT = "0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc"
impl_bytes = w3.eth.get_storage_at(contract_address, IMPL_SLOT)
implementation = "0x" + impl_bytes[-20:].hex()
print(f"Implementation: {implementation}")
```

### Step 3: Monitor for Governance Changes

Subscribe to governance forums for protocols you depend on. Key changes that affect arb:
- Fee tier changes (Uniswap governance can add/remove fee tiers)
- Contract pauses (protocols can emergency-pause)
- Address blacklisting (USDC can freeze addresses; OFAC compliance)
- Bridge parameter changes (relayer fees, speed settings)

---

## Staking / LST Contracts

Relevant for [[staking-yield-arbitrage]].

| Protocol | Contract | Ethereum Address | Token |
|---|---|---|---|
| **Lido stETH** | stETH token | `0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84` | stETH |
| **Lido wstETH** | Wrapped stETH | `0x7f39C581F595B53c5cb19bD0b3f8dA6c935E2Ca0` | wstETH |
| **Rocket Pool rETH** | rETH token | `0xae78736Cd615f374D3085123A210448E74Fc6393` | rETH |
| **Coinbase cbETH** | cbETH token | `0xBe9895146f7AF43049ca1c1AE358B0541Ea49BBa` | cbETH |
| **Frax sfrxETH** | sfrxETH token | `0xac3E018457B222d93114458476f3E3416Abbe38F` | sfrxETH |

---

## How to Use This Registry

1. **Verify before use:** Cross-reference every address against the protocol's official documentation and block explorer
2. **Check proxy implementations:** Many contracts use upgradeable proxy patterns. The address stays the same but the logic contract can change. Call `implementation()` on the proxy to check current logic
3. **Monitor governance:** Protocol governance can change fee structures, pause contracts, or blacklist addresses. Subscribe to governance forums for protocols you depend on
4. **Test on testnet first:** Goerli/Sepolia deployments exist for most protocols. Test your arb logic there before mainnet deployment
5. **Gas estimation:** Call `eth_estimateGas` with your exact calldata against the target contract to get accurate gas costs before submitting

## How Trading and AI Systems Consume This Registry

An on-chain arbitrage agent treats this registry as a *trusted address book* that gates execution. The pipeline:

| Layer | What it does | Uses from this registry |
|---|---|---|
| **Discovery** | Find a price dislocation across DEX pools | Router/factory/quoter addresses + on-chain quotes |
| **Route construction** | Build the swap path and, if needed, a flash-loan wrapper | Flash-loan provider + DEX router addresses |
| **Cross-chain leg** | Move capital between chains atomically or near-atomically | Bridge contracts (CCTP / Stargate / Across) |
| **Verification gate** | Confirm every target is the canonical, current implementation | [Verification Walkthrough](#contract-verification-walkthrough) (proxy check, deployer check) |
| **Submission** | Send the bundle privately to avoid being front-run | Flashbots relay / Protect RPC |

For an **AI agent**, the critical design rule is that the agent must *never synthesize a contract address from memory or pattern-match a similar-looking one*. Addresses are load-bearing and a single wrong character (or a phishing clone) means total loss of funds — the warnings at the top of this page exist for exactly that failure mode. The agent should: (1) resolve the protocol name to an address only via this registry or a live docs fetch, (2) run the EIP-1967 proxy-implementation check before trusting upgradeable contracts, and (3) refuse to transact against any address it cannot verify on a block explorer. The decision of *which* arb to run lives in [[arbitrage-opportunity-map]]; this page only answers *where* on-chain to send the transaction once that decision is made.

This is the on-chain analogue of the read/write split described in [[exchange-api-reference#how-trading-and-ai-systems-consume-these-apis|the exchange API reference]]: read paths (quotes, pool state, proxy slots) are safe to query freely; write paths (swaps, flash loans, bridge deposits) sit behind a deterministic verification gate.

## Related

- [[exchange-api-reference]] — CEX/DEX endpoint companion to this on-chain registry
- [[arbitrage-opportunity-map]] — the strategies these contracts serve
- [[low-cap-crypto-trading-map]] — Solana spot meta using the Solana DEX programs here
- [[flash-loan-arbitrage]] · [[cross-chain-arbitrage]] · [[mev-strategies]] · [[staking-yield-arbitrage]]
- [[automated-market-maker]] · [[defi]] · [[cross-chain-bridges]] · [[cctp]]
- [[uniswap]] · [[aave]]

## Sources

- Aave V3 deployed contracts (docs.aave.com/developers/deployed-contracts)
- Uniswap V3 contract addresses (docs.uniswap.org/contracts/v3/reference)
- Circle CCTP contracts (developers.circle.com/stablecoins/evm-smart-contracts)
- Across Protocol contracts (docs.across.to/reference/contract-addresses)
- Flashbots documentation (docs.flashbots.net)
- [[flash-loan-arbitrage]]
- [[cross-chain-arbitrage]]
- [[mev-strategies]]
