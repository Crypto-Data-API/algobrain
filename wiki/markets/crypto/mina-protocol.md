---
title: "Mina Protocol"
type: entity
created: 2026-04-09
updated: 2026-06-21
status: excellent
tags: [crypto]
aliases: ["MINA"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://minaprotocol.com/"
related: ["[[crypto-markets]]", "[[layer-1]]", "[[zero-knowledge-proofs]]", "[[proof-of-stake]]", "[[ethereum]]"]
---

# Mina Protocol

**Mina Protocol** (ticker **MINA**) is a [[proof-of-stake]] [[layer-1]] that bills itself as "the world's lightest blockchain": instead of growing without bound, the entire chain is compressed to a constant-size **succinct [[zero-knowledge-proofs|zk-SNARK]] proof of roughly 22 KB**. This lets any participant — even on a phone — verify the full chain state without downloading its history, enabling a highly decentralized and verifiable network. Mina also exposes its zk machinery to developers through **zkApps** (zero-knowledge smart contracts written in TypeScript via the o1js library), positioning it as privacy- and verifiability-focused infrastructure.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | MINA |
| **Market Cap Rank** | #427 |
| **Market Cap** | $54.22M |
| **Current Price** | $0.04203 |
| **24h Change** | -0.67% |
| **7d Change** | -2.85% |
| **24h Volume** | $3.52M |
| **All-Time High** | $9.09 (June 2021) |
| **All-Time Low** | $0.03990 |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

The macro backdrop is risk-off: the crypto [[fear-and-greed-index|Fear & Greed Index]] reads **23 (extreme fear)** and the long-horizon regime is an **Established Bear Market** as of 2026-06-21. MINA trades roughly 5% above its all-time low (~$0.0399) and about 99.5% below its June-2021 all-time high of $9.09 — one of the deeper peak-to-trough declines among surviving [[layer-1|L1s]].

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~1.29B MINA |
| **Total Supply** | ~1.29B MINA |
| **Max Supply** | Uncapped (inflationary) |
| **Fully Diluted Valuation (FDV)** | ~$54.22M |
| **Market Cap / FDV** | ~1.00 |

MINA has **no fixed max supply**; new tokens are issued continuously as block rewards to fund [[proof-of-stake]] staking. Because circulating supply effectively equals total supply (MC/FDV ≈ 1.00), there is no large locked overhang from team/investor cliffs — but the trade-off is **persistent token inflation** that dilutes holders unless they stake. Mina uses **Ouroboros Samasika**, a succinct-blockchain-adapted variant of Cardano-style Ouroboros [[proof-of-stake]]; any holder can stake (or delegate to a block producer) to earn rewards and help secure the chain.

---

## How & Where It Trades

**Spot venues.** MINA is listed on [[binance]] (MINA/USDT), [[kraken]] (MINA/USD), Upbit (MINA/KRW), Bitget, KuCoin, and Crypto.com.

**Derivatives.** A MINA perpetual trades on [[hyperliquid]] (MINA-PERP), plus perp markets on major centralized derivatives venues. At a ~$54M market cap with ~$3.7M daily volume, derivatives depth is thin and funding/OI are volatile — confirm live before sizing leverage. Spot liquidity is concentrated in USDT pairs.

---

## Technology & Consensus

Mina's core innovation is **recursive zk-SNARKs**: each new block carries a proof that recursively attests to the validity of all prior blocks, so the proof of the entire chain stays a constant ~22 KB regardless of how long the chain runs. Consequences:

- **Succinct verification.** Light clients verify the whole chain by checking one small proof — no multi-hundred-gigabyte node sync, sharply lowering the hardware barrier to running a verifying node.
- **Ouroboros Samasika consensus.** A provably secure [[proof-of-stake]] protocol adapted to the succinct-blockchain setting, allowing nodes to bootstrap from genesis using only the SNARK.
- **zkApps.** Off-chain execution with on-chain proof verification, written in TypeScript (o1js), enabling private inputs and verifiable computation — a natural fit for identity, compliance, and oracle use cases.

---

## Use Case, Narrative & Category

Mina sits in the **zero-knowledge / privacy / succinct-blockchain L1** category, overlapping conceptually with [[zero-knowledge-proofs|ZK]] scaling projects but distinct in that the *base layer itself* is the SNARK, not a rollup atop [[ethereum]]. Its narrative centers on decentralization (a phone can verify the chain), privacy-preserving applications, and a "verifiable internet" / proof-of-everything thesis. Tagged categories include Smart Contract Platform, Layer 1 (L1), Zero Knowledge (ZK), Privacy Blockchain, Proof of Stake (PoS), Coinbase 50 Index, plus numerous VC-portfolio tags (Paradigm, Coinbase Ventures, Multicoin, Pantera, Polychain).

---

## Valuation Framing (qualitative)

At a ~$54M market cap, MINA is a deep small-cap whose price is ~99.5% below its 2021 peak. With MC/FDV ≈ 1.00 there is no locked-supply cliff, so the dilution risk is *flow* (continuous PoS emissions) rather than a discrete unlock event — holders must stake to avoid being inflated away. The bull case is technological optionality: a constant-size, phone-verifiable [[zero-knowledge-proofs|zk]] base layer is a genuinely differentiated design, and ZK/privacy is a recurring narrative. The bear case is the gap between that thesis and realized usage — zkApp adoption has lagged, and a token can stay "interesting tech, no flow" indefinitely. In an extreme-fear regime, thin liquidity (~$3.5M/day) amplifies both directions. Not investment advice.

---

## Peer Comparison

| Project | Ticker | Category | MC Rank | Market Cap | MC/FDV | ZK role |
|---|---|---|---|---|---|---|
| **Mina** | MINA | Succinct zk [[layer-1]] | #427 | $54.22M | ~1.00 | Base layer *is* the SNARK |
| [[linea]] | LINEA | zkEVM [[layer-2]] | #391 | $61.63M | ~0.34 | zk-rollup atop [[ethereum]] |
| [[zetachain]] | ZETA | Omnichain L1 | #426 | $54.23M | ~0.70 | TSS / cross-chain, not zk |
| [[astar]] | ASTR | Multi-chain L1/L2 | #475 | $47.34M | ~0.87 | zkEVM L2 (Polygon CDK) |

*Mina is the only project here where the entire base chain is compressed to a recursive SNARK; the others use zk as a scaling rollup or use non-zk cross-chain security.*

---

## Notable History

- Mina launched its mainnet in 2021 after a high-profile CoinList sale; MINA printed its all-time high of **$9.09 in June 2021**.
- The token has since declined ~99.5%, reaching an all-time low near $0.0399 around March 2026.
- It carries **FTX Holdings** and **Alameda/various-VC portfolio** tags, a legacy association from the 2021–22 cycle that surfaced overhang concerns during the FTX collapse.
- As of 2026-06-21 it trades at ~$0.042, about 5% off its low.

---

## Risks

- **Perpetual inflation.** Uncapped supply means non-stakers are continuously diluted; demand must keep pace with emissions to hold price.
- **zkApp adoption lag.** The succinct-chain thesis is technically elegant but on-chain application traction and developer adoption have been limited; the value case depends on usage that has not yet materialized at scale.
- **Prover performance / centralization.** Generating recursive SNARKs is computationally heavy, which can concentrate block production among well-resourced operators.
- **Legacy distribution overhang.** FTX/Alameda-era holdings and VC allocations add historical supply-disposition risk.
- **Severe drawdown / liquidity.** Down ~99.5% from ATH, ~$3.7M daily volume, and an extreme-fear macro regime amplify volatility and slippage.

---

## See Also

- [[crypto-markets]]
- [[layer-1]]
- [[zero-knowledge-proofs]]
- [[proof-of-stake]]
- [[hyperliquid]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market snapshot 2026-06-21 (cryptodataapi.com / CoinGecko bulk endpoint), `raw/data/crypto-loop/coingecko-markets.json`.
