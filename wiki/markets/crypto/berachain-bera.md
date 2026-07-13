---
title: "Berachain"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto, defi]
aliases: ["BERA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://berachain.com/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[layer-1]]", "[[proof-of-stake]]", "[[hyperliquid]]", "[[fear-and-greed-index]]"]
---

# Berachain

**Berachain** (ticker **BERA**) is an EVM-compatible [[layer-1]] blockchain best known for its novel **Proof-of-Liquidity (PoL)** consensus and a three-token model. BERA is the network's native gas and staking token, paired with **BGT** (a non-transferable governance/reward token earned by providing liquidity) and **HONEY** (the ecosystem's native stablecoin).

Proof-of-Liquidity aligns network security with DeFi liquidity: instead of validators simply locking the gas token, the design directs emissions to liquidity providers, aiming to make the chain's economic activity and its security budget reinforce each other. Berachain has been backed by investors including Polychain Capital and Outlier Ventures, and launched mainnet in February 2025 after one of the more closely watched testnet ("Artio"/"bArtio") campaigns of the prior cycle.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | BERA |
| **Current Price** | $0.228967 |
| **Market Cap** | $63,514,146 (~$63.5M) |
| **Market Cap Rank** | #381 |
| **24h Volume** | $18,096,879 (~$18.1M) |
| **24h Change** | -0.41% |
| **7d Change** | -11.19% |
| **Fully Diluted Valuation** | ~$124.4M |
| **All-Time High** | $14.83 (2025-02-06) — now ~-98.5% |
| **All-Time Low** | $0.218198 (2026-06-20) — now ~+5.2% |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

BERA is one of the weaker performers in this cohort, down ~11% over 7 days and trading roughly 98% below its February 2025 all-time high. It sits barely above the all-time low it printed on 2026-06-20, the day before this snapshot — underscoring acute bear-market pressure. The decline is consistent with an extreme-fear market backdrop (crypto [[fear-and-greed-index|Fear & Greed Index]] 23, an "Established Bear Market" regime as of 2026-06-21). The ~$18M of daily turnover against a ~$64M cap (a ~0.28 volume/mcap ratio) shows BERA is still actively traded for its size.

---

## Technology & Consensus

Berachain runs an EVM-identical execution layer on top of **BeaconKit**, a modular consensus framework derived from the [[ethereum|Ethereum]] / CometBFT stack, so existing Solidity contracts and tooling (MetaMask, Foundry, Hardhat) work unchanged. What differs is the reward routing:

- **Proof-of-Liquidity (PoL):** validators are selected by BGT delegated to them, and block rewards are emitted as **BGT** rather than as the gas token. Validators in turn direct BGT emissions toward "reward vaults" — pools of approved DeFi liquidity (DEX LPs, lending markets, etc.). The intent is that the chain's security budget is spent buying *useful* liquidity rather than passive lockups.
- **Three-token separation:** **BERA** (transferable gas/staking token), **BGT** (non-transferable, earned by providing liquidity; can be "burned" 1:1 into BERA but not the reverse), and **HONEY** (the native overcollateralized stablecoin). This separates the speculative/liquid asset (BERA) from the governance-and-emissions asset (BGT).

This positions Berachain firmly in the [[proof-of-stake]] family (BGT-weighted validator selection) but with an opinionated twist that couples consensus rewards to on-chain liquidity provision.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~277.13M BERA |
| **Total Supply** | ~542.77M BERA |
| **Max Supply** | Uncapped (inflationary) |
| **Fully Diluted Valuation** | ~$124.4M |
| **Market Cap / FDV** | ~0.51 |

BERA is the gas and staking token within Berachain's three-token Proof-of-Liquidity system (BERA / BGT / HONEY). A market-cap/FDV ratio around **0.51** means roughly half of total supply is still locked, implying meaningful future unlock/emission pressure as team, investor, and ecosystem allocations vest. The uncapped max supply reflects ongoing PoL emissions (paid in BGT, convertible to BERA), so **dilution is structural** rather than a one-off cliff: as long as the chain emits rewards, BERA supply grows.

---

## Market Structure & Derivatives

### Spot venues (centralized)

| Exchange | Pair |
|---|---|
| Binance | BERA/USDT |
| Kraken | BERA/USD |
| Upbit | BERA/KRW |
| Bitget | BERA/USDT |
| KuCoin | BERA/USDT |
| Crypto.com Exchange | BERA/USD |

### Derivatives

| Venue | Instrument | Type |
|---|---|---|
| [[hyperliquid|Hyperliquid]] | BERA-PERP | Perpetual |
| Binance Futures / Bybit / OKX | BERA perps | Perpetual (CEX) |

BERA has broad centralized listing including Binance and Korean-won liquidity via Upbit, and trades as a perpetual on [[hyperliquid|Hyperliquid]] for leveraged exposure with on-chain [[funding-rate|funding]] and open-interest. On-chain, Berachain's native DeFi venues (the DEXs and lending markets wired into PoL reward vaults, built around the HONEY economy) provide spot liquidity. Specific funding/OI figures are not captured in this snapshot — verify live before sizing; in an extreme-fear regime, small-cap perp funding can swing sharply.

---

## Use Case, Narrative & Category

Berachain sits in the **DeFi-native Layer 1** category. CoinGecko tags include Smart Contract Platform, Decentralized Finance (DeFi), Layer 1 (L1), Berachain Ecosystem, Binance HODLer Airdrops, Outlier Ventures Portfolio, and Polychain Capital Portfolio.

The differentiating narrative is **Proof-of-Liquidity**: a consensus design that ties validator rewards to ecosystem liquidity rather than to passive staking of the gas token alone. The pitch is a self-reinforcing flywheel where DeFi activity deepens security and vice versa. This makes Berachain a bet on a specific, opinionated tokenomic experiment rather than on raw throughput — closer in spirit to a DeFi protocol with its own chain than to a generic high-TPS [[layer-1|L1]].

---

## Valuation Framing (qualitative)

BERA's ~$64M market cap against a ~$124M FDV embeds a ~0.51 MC/FDV ratio — i.e. the market is pricing roughly half the eventual supply. Because PoL is emissions-driven, the relevant question for valuation is whether emitted BGT/BERA reliably attracts *sticky* TVL that generates real fees, or merely rents mercenary liquidity that exits when emissions taper. With the token ~98% off ATH and sitting on fresh all-time lows, the market is currently pricing the latter, skeptical case. A re-rating would likely require demonstrable TVL retention and fee growth that outpaces emission dilution. This is framing, not a price target.

---

## Peer Comparison

| Token | Symbol | Category | Mkt Cap | Rank | MC/FDV | Notes |
|---|---|---|---|---|---|---|
| **Berachain** | BERA | DeFi-native L1 (PoL) | ~$63.5M | #381 | ~0.51 | Tri-token; emissions to LPs |
| [[sonic-3\|Sonic]] | S | High-TPS EVM L1 | ~$107.9M | #258 | ~0.97 | Ex-[[fantom\|Fantom]] rebrand; FeeM |
| [[ontology\|Ontology]] | ONT | DID / trust L1 | ~$45.8M | #487 | ~1.00 | Dual-token ONT/ONG |
| [[altlayer\|AltLayer]] | ALT | RaaS / [[restaking]] | ~$41.1M | #515 | ~0.64 | L2 infra, not an L1 |

*(Comparison figures from the same 2026-06-21 snapshot.)* Among these L1 peers BERA carries the heaviest *future* dilution risk (MC/FDV ~0.51) but a richer, more experimental consensus thesis.

---

## Notable History

- **All-time high:** $14.83 on 2025-02-06, around its high-profile mainnet launch and airdrop.
- **All-time low:** $0.218198 on 2026-06-20 — a fresh all-time low set the day before this snapshot, underscoring acute bear-market pressure.
- The ~98% drawdown from ATH is among the steepest in this cohort, reflecting a launch into peak hype followed by a severe de-rating.

---

## Risks

- **Tokenomic complexity:** the three-token PoL model (BERA/BGT/HONEY) is innovative but unproven at scale and harder for users to reason about, raising execution and adoption risk.
- **Emissions/dilution:** uncapped supply plus a ~0.51 MC/FDV ratio means continued emissions and unlocks can weigh on price; supply growth is structural.
- **Liquidity-incentive dependence:** PoL relies on emissions to attract liquidity; if rewards taper or mercenary capital exits, TVL and the security incentive can unwind together (a reflexive downside).
- **Bear-market beta:** with [[fear-and-greed-index|Fear & Greed]] at 23 (extreme fear) and an established bear-market regime, and BERA at fresh all-time lows, downside and liquidity risk are elevated.
- **Volatility / liquidity:** ~$64M market cap makes BERA a small-cap, high-volatility asset prone to sharp moves and slippage.

---

## Related

- [[crypto-markets]]
- [[ethereum]] — EVM/BeaconKit lineage
- [[layer-1]]
- [[proof-of-stake]] — BGT-weighted validator selection
- [[hyperliquid]] — venue for BERA perpetuals
- [[fear-and-greed-index]] — macro sentiment gauge
- [[sonic-3]], [[ontology]], [[altlayer]] — L1/infra peers

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data snapshot 2026-06-21 (cryptodataapi.com / CoinGecko; `raw/data/crypto-loop/coingecko-markets.json`).
- General market knowledge; no specific wiki source ingested yet.
