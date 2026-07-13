---
title: "Neutrl USD"
type: entity
created: 2026-04-09
updated: 2026-06-23
status: excellent
tags: [crypto, stablecoins]
aliases: ["NUSD"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://neutrl.finance/"
related: ["[[crypto-markets]]", "[[ethereum]]", "[[stablecoin]]", "[[stablecoins]]", "[[ethena-usde]]", "[[synthetic-dollar]]"]
---

# Neutrl USD

**Neutrl USD** (ticker **NUSD**) is a market-neutral [[synthetic-dollar|synthetic dollar]] issued by the Neutrl protocol on [[ethereum|Ethereum]], targeting a soft peg of 1 NUSD ≈ US$1. Unlike a fiat-backed [[stablecoin]], NUSD is collateralized by a delta-neutral trading book — combining OTC arbitrage on locked/discounted altcoins, perpetual-futures funding-rate capture, and other hedged DeFi strategies — so the token aims to hold its dollar value while the backing positions generate yield distributable to a staked variant. Conceptually it sits in the same "yield-bearing synthetic dollar" family pioneered by [[ethena-usde|Ethena USDe]].

> **Subject note / disambiguation:** "nUSD" / "NUSD" has been used by several unrelated projects (e.g. Synthetix's legacy nUSD, Nexus Mutual contexts). *This* page is specifically **Neutrl USD** issued by the **Neutrl protocol** (neutrl.finance). Do not graft other nUSD histories onto it.

Neutrl's distinguishing angle within the synthetic-dollar category is its **OTC locked/discounted-token arbitrage** sleeve: rather than relying purely on perpetual-futures funding (the Ethena model), Neutrl also sources yield by buying tokens at a discount in OTC/locked deals and hedging the directional exposure, aiming to diversify the return engine away from a single funding-rate dependency.

---

## Market Data

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

| Field | Detail |
|---|---|
| **Ticker** | NUSD |
| **Market Cap Rank** | #283 |
| **Current Price** | $0.9989 |
| **Market Cap** | $91.3M |
| **24h Volume** | $6.78M |
| **24h Change** | -0.03% |
| **Circulating / Total Supply** | 91.45M / 91.45M NUSD |
| **All-Time High** | $1.031 |
| **All-Time Low** | $0.9754 |
| **Categories** | Stablecoins, Synthetic Asset, Ethereum Ecosystem |
| **Website** | [https://neutrl.finance/](https://neutrl.finance/) |

At the snapshot, NUSD traded at **$0.9989**, within ~11 bps of its dollar target — effectively at peg. Its lifetime range ($0.9754–$1.031) shows the typical modest band of a synthetic dollar that has never suffered a severe de-peg, though the sub-$1 ATL confirms it does drift below par under stress.

---

## Architecture — How NUSD Works

NUSD is a **synthetic dollar**: it holds no fiat reserves and no over-collateralized crypto vault. Instead, its dollar value is *manufactured* by a delta-neutral trading book whose mark-to-market is engineered to stay near $1 regardless of crypto direction, while the carry it throws off is paid out as yield.

### Collateral / reserve model
- **Backing:** a fully collateralized, **market-neutral (delta-hedged) portfolio** — OTC purchases of discounted/locked tokens hedged with offsetting short positions, plus funding-rate and basis capture. Value is meant to be insulated from the direction of crypto prices.
- **Three return sleeves:** (1) **OTC/locked-token discount capture** — buy tokens below spot in locked deals, hedge the price exposure; (2) **perpetual-futures funding** — collect funding while delta-hedged; (3) **basis/other hedged DeFi** carry. Diversifying across sleeves is the design's hedge against any single source (e.g. funding) flipping negative.

### Peg / stability mechanism
- **Peg target:** soft 1:1 to the US dollar, maintained through arbitrage and mint/redeem incentives rather than a hard fiat redemption guarantee.
- **Enforcement:** arbitrageurs mint NUSD when it trades above $1 and redeem/buy when below; the credibility of that loop depends on the neutral book actually being worth ~$1 per token. If the hedge breaks (delta-neutrality fails), the soft peg is what gives first.

### Yield source
- **Yield source:** trading profits from the neutral book (funding, basis, OTC discounts) accrue to a **staked version** of the token rather than to passive holders, mirroring the [[ethena-usde|Ethena]] USDe / sUSDe split. Holding plain NUSD is a stable-value position; staking captures the carry.

### Mint / redeem & gating
- **Redemption:** mint and redeem are run by the protocol against the collateral pool; like most synthetic dollars, instant redemption can be gated or queued during volatility, which is the main mechanism a holder relies on to enforce the peg. The OTC/locked sleeve in particular can be slow to unwind, so redemption liveness is a key risk to monitor.

---

## Comparison vs Peer Synthetic / Stablecoins

| Dimension | **NUSD** (Neutrl) | [[ethena-usde\|USDe]] (Ethena) | [[usdu\|USDU]] (Unitas) | [[nxusd\|NXUSD]] (Nereus) |
|---|---|---|---|---|
| **Peg model** | Soft $1, delta-neutral | Soft $1, delta-neutral | $1, fiat/RWA reserve | $1, crypto-collateral |
| **Backing** | OTC discounts + perp shorts + basis | Crypto + perp shorts | Cash + T-bills | Over-collateralized crypto |
| **Yield source** | Funding + basis + OTC discounts | Funding rate + staking | T-bill yield | Lending/borrow spread |
| **Yield to holder** | Via staked NUSD | Via sUSDe | Direct | Indirect (money market) |
| **Crypto correlation** | Low (hedged) | Low (hedged) | Low (rates) | High (collateral) |
| **Key failure mode** | Hedge/funding break | Funding flips negative | Custodian/banking | Collateral crash + oracle |

NUSD's nearest peer is Ethena's USDe (same delta-neutral synthetic-dollar template); its claimed edge is the additional OTC locked-token discount sleeve diversifying away from pure funding-rate dependence.

---

## How & Where It Trades / Is Used

- **Primary venue:** on-chain DEX liquidity on [[ethereum|Ethereum]] (Neutrl contract `0xe556aba6fe6036275ec1f87eda296be72c811bce`), plus mint/redeem directly with the protocol.
- **DeFi composability:** plain NUSD functions as a stable unit of account / collateral, while the staked variant is the yield-bearing instrument — the standard "two-token" synthetic-dollar pattern (hold for stability, stake for carry). Integration depth and the staked-token venues are the main composability levers.
- **Liquidity caveat:** ~$6.8M of 24h volume against a ~$91M cap is reasonable for a synthetic dollar of this size, but liquidity is concentrated in a few pools; large redemptions in a stressed market could push the secondary-market price below the protocol's NAV before arbitrage closes the gap.
- This is **not** a major-exchange listed asset; treat order-book depth as thin relative to fiat-backed majors like [[usdc]] or [[usdt]].

---

## Narrative / Category & Catalysts

NUSD sits in the **delta-neutral synthetic-dollar / "internet bond"** narrative that [[ethena-usde|Ethena]] defined — dollars whose yield comes from crypto-market structure (funding, basis) and, in Neutrl's case, OTC discount capture, rather than from T-bills or token emissions. Catalysts:

- **Funding-rate regime is the master variable.** Positive perpetual funding is the lifeblood of the model; a sustained negative-funding bear regime compresses or inverts the carry — directly relevant in the current bottoming/accumulation phase.
- **OTC locked-token deal flow:** Neutrl's differentiator scales with the availability of discounted/locked-token deals to arbitrage; a rich pipeline is a tailwind, a dry one a headwind.
- **Diversification pitch vs single-source rivals:** if NUSD can demonstrate yield resilience when funding turns negative (via the OTC sleeve), that is its key differentiation catalyst versus pure-funding synthetic dollars.
- **Regulatory scrutiny of synthetic dollars:** yield-bearing synthetic dollars face the same securities/stablecoin questions as Ethena — a sector-wide swing factor.

---

## History / Timeline

- **2026-04-09** — Captured in the wiki via the CoinGecko top-1000 snapshot (Source: [[coingecko-top-1000-2026-04-09]]); page created.
- **2026-06-21** — Market-data refresh: price $0.9989, cap ~$91.3M, rank #283, ~$6.78M 24h volume; lifetime range $0.9754–$1.031, never a severe de-peg.
- **2026-06-23** — Page expanded to `excellent`.

> Note: only wiki-verified dates are listed; dated protocol-launch, audit, and funding milestones are not yet ingested from a primary source.

---

## Risks

- **De-peg risk:** the peg depends on the neutral book staying neutral. A funding-rate regime flip, exchange counterparty failure, or inability to hedge OTC positions can break delta-neutrality and pressure the dollar value — the sub-$1 ATL ($0.9754) shows this drift is real.
- **Collateral / strategy risk:** OTC-locked-token positions and perp hedges carry liquidation, basis-blowout, and venue-risk that a simple T-bill-backed coin does not.
- **Issuer / custodial risk:** value depends on the Neutrl protocol's execution and the centralized venues where hedges and OTC trades sit.
- **Liquidity / redemption risk:** redemption may be queued or gated under stress, exactly when holders most want to exit.
- **Regulatory risk:** yield-bearing synthetic dollars face evolving scrutiny (securities and stablecoin-regime questions) similar to [[ethena-usde|Ethena]].
- **Macro backdrop:** as of 2026-06-21 the Crypto Fear & Greed Index read **23**; by the 2026-06-23 snapshot it sits at **21 (Extreme Fear)**, market-health 29/100, long-horizon regime **bottoming / accumulation** — a regime in which funding-rate yields compress (and can go negative) and de-peg stress on synthetic dollars historically rises, making the OTC-discount sleeve's diversification especially load-bearing.

---

## Trading / Usage Playbook

- **Hold NUSD for stability, stake for yield.** Plain NUSD is the stable-value leg; the carry accrues only to the staked variant. Decide which exposure you actually want before minting.
- **Watch funding like a hawk.** The peg and the yield both lean on a delta-neutral book; persistent negative perpetual funding is the classic synthetic-dollar stressor and the single most important live signal for NUSD.
- **OTC sleeve = redemption-liquidity risk.** Locked/discounted-token positions can be slow to unwind, so in a rush for the exits redemption may gate — size positions to survive a queue, and treat the sub-$1 ATL ($0.9754) as the realistic downside drift.
- **Benchmark against USDe/sUSDe.** If you are buying NUSD for yield, compare net staked yield and de-peg track record against the larger, more liquid Ethena complex; NUSD's case rests on the OTC-discount diversification holding up when funding does not.

> *Not financial advice. Synthetic dollars carry hedge-failure, counterparty, and redemption-gating risk and can de-peg under stress.*

---

## Tokenomics

| Metric | Value |
|---|---|
| **Circulating Supply** | 91.45M NUSD |
| **Total Supply** | 91.45M NUSD |
| **Max Supply** | Unlimited |
| **Market Cap / FDV Ratio** | ~1.00 |

---

## Platform & Chain Information

**Native Chain:** Ethereum

### Contract Addresses

| Chain | Address |
|---|---|
| Ethereum | `0xe556aba6fe6036275ec1f87eda296be72c811bce` |

---

## Exchange Listings

> *No major exchange listings found in CoinGecko data.*

---

## Social & Community

| Platform | Link / Metric |
|---|---|
| **Website** | [https://neutrl.finance/](https://neutrl.finance/) |
| **Twitter** | [@neutrl](https://twitter.com/neutrl) |
| **Telegram** | [NeutrlOfficial](https://t.me/NeutrlOfficial) (1,199 members) |
| **Discord** | [https://discord.gg/Neutrl](https://discord.gg/Neutrl) |
| **GitHub** | [https://github.com/neutrl-lab](https://github.com/neutrl-lab) |
| **Whitepaper** | [https://docs.neutrl.finance/](https://docs.neutrl.finance/) |

---

## Trading Characteristics

| Characteristic | Detail |
|---|---|
| **24h Volume** | $6.78M |
| **Market Cap Rank** | #283 |
| **Last Updated** | 2026-06-21 |

---

## Whale & Holder Information

> *On-chain holder distribution data requires blockchain analytics integration. This section will be populated from on-chain sources as they are ingested.*

---

## Major News & Events

> *Notable events and news will be added through the wiki's source ingestion workflow as relevant articles are processed.*

---

## Related

- [[stablecoin]] / [[stablecoins]]
- [[synthetic-dollar]]
- [[ethena-usde]] — the reference yield-bearing synthetic dollar
- [[crypto-markets]]
- [[ethereum]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data: cryptodataapi.com / CoinGecko snapshot, 2026-06-21.
- General market knowledge; no specific wiki source ingested yet.
