---
title: "Chia"
type: entity
created: 2026-04-09
updated: 2026-07-16
status: excellent
tags: [crypto]
aliases: ["XCH"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.chia.net/"
related: ["[[bitcoin]]", "[[crypto-markets]]", "[[depin]]", "[[layer-1]]", "[[proof-of-space]]", "[[proof-of-work]]"]
---

# Chia

**Chia** (ticker **XCH**) is a [[layer-1]] blockchain founded by Bram Cohen, inventor of the BitTorrent protocol. It pioneered **Proof of Space and Time (PoST)**, a consensus mechanism that secures the network using unused hard-disk storage ("farming") plus a verifiable-delay-function time component, instead of energy-intensive [[proof-of-work]] mining. XCH is the native coin used for fees, farming rewards, and on-chain smart transactions written in Chia's Chialisp language.

---

## Market Data

| Field | Value |
|---|---|
| **Ticker** | XCH |
| **Market Cap Rank** | #581 |
| **Market Cap** | $34.99M |
| **Current Price** | $1.88 |
| **24h Change** | -1.55% |
| **7d Change** | -8.27% |
| **24h Volume** | $2.53M |
| **Circulating Supply** | ~18.57M XCH |
| **Fully Diluted Valuation** | $65.85M |
| **Market Cap / FDV** | ~0.53 |
| **All-Time High** | $1,645.12 (2021-05-15) — ~99.9% below |
| **All-Time Low** | $1.88 (2026-06-20) — at/near ATL |

> *Market data as of 2026-06-21 (cryptodataapi.com / CoinGecko).*

XCH is down on both the 24h (-1.55%) and 7d (-8.27%) windows amid an "Established Bear Market" regime and extreme fear (Crypto [[crypto-fear-and-greed-index|Fear & Greed Index]] = 23). At ~$1.88, XCH trades ~99.9% below its May 2021 all-time high of $1,645.12 — one of the steepest peak-to-trough declines among surviving L1s, reflecting the collapse of the 2021 "farming" hype and a large early premine/reserve overhang. **Notably, the snapshot records a fresh all-time low of $1.88 on 2026-06-20** — XCH is making new lows, with no historical price floor offering support. The ~0.53 MC/FDV means roughly half of total supply is not yet circulating, so even at all-time-low spot the implied FDV (~$66M) carries latent dilution.

---

## Tokenomics & Supply

| Metric | Value |
|---|---|
| **Circulating Supply** | ~18.57M XCH |
| **Total Supply** | ~34.94M XCH |
| **Max Supply** | Uncapped (continuous farming emission) |
| **Fully Diluted Valuation** | $65.85M |
| **Market Cap / FDV** | ~0.53 |

Chia has no fixed max supply: new XCH is emitted continuously as farming rewards on a halving-style schedule. A significant feature of Chia's tokenomics is the **strategic reserve** held by Chia Network Inc. (a "pre-farm" of millions of XCH), intended to fund development, lending and ecosystem growth — a notable supply overhang and a frequent point of criticism. The roughly 0.53 market-cap-to-FDV ratio reflects coins not yet in circulation, including reserve and unmined supply.

---

## How & Where It Trades

**Spot venues:** XCH is listed on a limited set of centralized exchanges including KuCoin (XCH/USDT) and Crypto.com (XCH/USD), among others. Its exchange footprint is narrower than most similarly-ranked L1s.

**Derivatives:** There is **no significant XCH perpetual/derivatives market** on major venues; XCH is effectively a spot-only asset for most traders, with no reliable funding or open-interest data. Plan for spot execution and limited depth.

At ~$2.5M daily volume on a ~$35.0M cap (~7% turnover), XCH has modest turnover and limited absolute liquidity. There is no liquid [[hyperliquid|Hyperliquid]] perp; price discovery is spot-only on a thin set of venues.

---

## Technology / Consensus

Chia's **[[proof-of-space|Proof of Space and Time]] (PoST)** has farmers allocate disk space to store cryptographic "plots"; the network selects winners proportional to allocated space, with a verifiable delay function (VDF, the "time" component) preventing grinding attacks and enforcing block spacing. Chia bills this as "the first new Nakamoto-style consensus since Bitcoin," designed to be more energy-efficient and decentralized than [[proof-of-work]]. Smart transactions are written in **Chialisp**, a Lisp-based language built around the coin/UTXO model for auditable, secure on-chain logic. The same [[proof-of-space]] mechanism gives XCH a [[depin]] (storage-as-security) flavor, distinguishing its energy profile sharply from PoW chains like [[bitcoin]].

---

## Use Case / Narrative / Category

Chia's narrative blends **energy-efficient consensus** and **enterprise/institutional smart transactions** — positioning XCH as a greener, more auditable alternative to [[bitcoin]] for payments, lending and tokenized assets. Category tags include Smart Contract Platform, [[layer-1]], [[depin]] (decentralized physical infrastructure, via storage farming), and a16z Portfolio. The storage-as-security model also gives it a DePIN angle.

---

## Valuation Framing

Chia is best understood as a **once-hyped L1 now trading near liquidation value**, making fresh all-time lows in mid-2026. Two structural drags define the valuation: (1) the corporate **strategic reserve** held by Chia Network Inc., a large pre-farm representing a persistent supply overhang and ~0.47 of total supply not yet circulating; and (2) uncapped farming emissions that dilute over time. The qualitative bull case rests on the company's "TradFi-friendly" path — reported moves toward a public listing and a corporate XCH reserve strategy could give the token an institutional bid that pure-retail L1s lack. The bear case is that PoST and Chialisp never achieved the developer/user adoption of EVM ecosystems, leaving XCH as a technically interesting but economically stranded asset. With the spot price at/near its ATL and FDV ~2x the circulating cap, the market is pricing deep skepticism about future demand.

---

## Peer Comparison

| Token | Consensus | Mkt-cap rank | Supply | Niche |
|---|---|---|---|---|
| **Chia (XCH)** | [[proof-of-space|Proof of Space + Time]] | #581 | Uncapped farming, reserve overhang | Energy-efficient L1, Chialisp |
| **[[bitcoin]] (BTC)** | [[proof-of-work]] | #1 | Capped 21M | Store of value, security via energy |
| **[[siacoin|Siacoin]] (SC)** | PoW (storage utility) | #566 | Uncapped | Decentralized storage (different aim) |
| Filecoin (FIL) | Proof-of-replication | large-cap | Capped 2B | Storage market (DePIN peer) |

*Chia, Siacoin ranks reflect the 2026-06-21 snapshot; BTC/FIL shown qualitatively. Chia competes on consensus design and a green/enterprise narrative rather than on storage rental like Sia/Filecoin.*

---

## Notable History

- **2021** — Mainnet launch triggered a global hard-drive/SSD buying frenzy as farmers raced to allocate storage; XCH spiked to an all-time high of $1,645.12 (May 15, 2021).
- **2021-2026** — XCH declined ~99.9% from its ATH as farming hype faded and supply expanded.
- **2026-06-20** — XCH printed a **fresh all-time low of $1.88**, the price recorded in the latest snapshot — the token is making new lows in the Established Bear Market.
- Chia Network Inc. has pursued a more "TradFi-friendly" path, including reported moves toward a public listing and a corporate XCH strategic reserve.

---

## Risks

- **Severe long-term drawdown** — XCH is ~99.9% below ATH; momentum and sentiment have been deeply negative for years.
- **Uncapped emission + reserve overhang** — continuous farming issuance plus the corporate strategic reserve create persistent sell-pressure risk.
- **Limited liquidity and venue support** — modest volume, few major listings, no meaningful derivatives market.
- **Bear-market regime** — extreme fear (F&G = 23) and an "Established Bear Market" weigh on small-cap L1s; XCH is currently making fresh all-time lows with no historical price support beneath it.
- **Adoption risk** — Chialisp and the PoST model have not driven broad developer/user adoption versus EVM ecosystems.
- **Hardware/centralization concerns** — large "farms" can concentrate storage capacity.

---

## See Also

- [[crypto-markets]]
- [[bitcoin]]
- [[proof-of-work]]
- [[proof-of-space]]
- [[layer-1]]
- [[depin]]

---

## Sources

- (Source: [[coingecko-top-1000-2026-04-09]])
- Market data as of 2026-06-21 from cryptodataapi.com / CoinGecko bulk snapshot.

