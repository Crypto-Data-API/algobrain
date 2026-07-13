---
title: "Jump Trading"
type: entity
created: 2026-04-22
updated: 2026-06-10
status: good
tags: [company, crypto, futures, algorithmic, market-microstructure]
entity_type: company
aliases: ["Jump Trading LLC", "Jump Crypto"]
founded: 1999
headquarters: "Chicago, Illinois, USA"
website: "https://www.jumptrading.com"
related: ["[[high-frequency-trading]]", "[[market-maker]]", "[[futures]]", "[[co-location]]", "[[low-latency-trading]]", "[[citadel-securities]]", "[[jane-street]]", "[[cme-group]]", "[[defi]]", "[[solana]]"]
---

Jump Trading is a [[high-frequency-trading|high-frequency]] and proprietary trading firm specializing in [[futures]], equities, crypto, and DeFi. Founded in 1999 in Chicago, the firm is known for latency-sensitive strategies, extensive infrastructure investment, and early aggressive entry into cryptocurrency markets through its Jump Crypto division.

## Overview

Jump Trading was founded by Bill DiSomma and Paul Gurinas, both former floor traders at the [[cme-group|Chicago Board of Trade]]. The firm evolved from pit trading to electronic trading and became one of the most technologically sophisticated HFT firms globally. Jump operates across multiple asset classes and geographies, with offices in Chicago, New York, London, Singapore, and Shanghai.

The firm's name reportedly comes from the "jump ball" concept — competing for opportunities in fast-moving markets. Jump is privately held and notoriously secretive about its strategies and performance.

## Trading Activities

### Futures and Equities HFT

Jump Trading is a major participant on the [[cme-group|CME]], CBOE, and other futures exchanges, specializing in latency [[arbitrage]] and market making. Their strategies exploit microsecond-level speed advantages through:

- **[[co-location]]** — servers physically adjacent to exchange matching engines
- **Microwave/millimeter-wave towers** — Jump famously purchased a former military radio tower in Belgium and invested in microwave transmission networks between Chicago and New York/New Jersey to shave milliseconds off data transmission times
- **[[fpga]]** — hardware-based order processing for sub-microsecond decision making

### Jump Crypto

Jump Crypto was established as a dedicated cryptocurrency and [[defi|DeFi]] division. Key activities included:

- **Wormhole bridge** — Jump built and maintained the Wormhole cross-chain bridge, which suffered a $320 million exploit in February 2022. Jump Crypto covered the losses to maintain confidence
- **[[solana]] ecosystem** — significant investment in and market making for the Solana blockchain ecosystem
- **DeFi market making** — providing liquidity on decentralized exchanges and engaging in MEV (maximal extractable value) strategies
- **FTX exposure** — Jump Crypto had substantial exposure to the FTX exchange and suffered significant losses during FTX's collapse in November 2022, leading to a scaling back of crypto operations

### Losses and Restructuring

The 2022 crypto downturn hit Jump Crypto particularly hard. Between the Wormhole exploit ($320M), FTX collapse losses, and broader market declines, Jump Crypto's operations were significantly curtailed. By 2023-2024, the crypto division reduced headcount substantially (president Kanav Kariya departed in June 2024 amid a CFTC investigation), though the parent Jump Trading firm continued operating profitably in traditional markets.

## 2024–2026 Developments

- **SEC settlement (2024-12-20)** — Jump's Cayman subsidiary **Tai Mo Shan Limited agreed to pay ~$123M** to settle SEC charges over its role in the May 2021 TerraUSD (UST) depeg episode: the SEC found its ~$20M of stabilizing purchases (under an undisclosed Terraform arrangement with discounted LUNA incentives) created a false impression of UST's algorithmic stability. Breakdown: $73.45M disgorgement + $12.92M prejudgment interest + $36.73M civil penalty. Settled without admitting or denying.
- **Jump Crypto re-emergence (2025)** — after years of keeping a low profile, Jump Crypto publicly "re-introduced" itself as a **crypto infrastructure builder**, leaning on the friendlier US regulatory regime; it disclosed participation in US crypto-policy lobbying and continued flagship engineering work such as **Firedancer**, the high-performance [[solana]] validator client.
- **Renewed investing (2025)** — Jump Crypto resumed venture activity, e.g. co-leading (with General Catalyst) the **$20M Series A for Ostium**, an on-chain TradFi-perpetuals protocol (December 2025), alongside renewed market-making and infrastructure commitments.
- The parent firm remains one of the largest futures/equities HFT participants globally; no public P&L is disclosed (private partnership).

## Trading Relevance

Jump Trading's activities affect other traders in several ways:

- **Futures latency dynamics**: Jump's HFT activity in E-mini S&P ([[cme-group|ES]]) and other futures contracts creates the latency environment that scalpers and day traders operate within. Their presence means retail traders cannot compete on speed and must find edge elsewhere
- **Crypto market making**: Jump's crypto activities influenced [[bid-ask-spread|spreads]] and [[liquidity]] on major exchanges. Their partial withdrawal from crypto post-2022 contributed to thinner order books
- **Infrastructure arms race**: Jump's investments in microwave towers and [[co-location]] illustrate the barriers to entry in true HFT — relevant for anyone considering latency-based strategies

## Related

- [[high-frequency-trading]] — Jump's core competency in traditional markets
- [[co-location]] — infrastructure Jump uses for latency advantage
- [[low-latency-trading]] — the broader category of speed-sensitive trading
- [[cme-group]] — primary futures exchange where Jump trades
- [[citadel-securities]] — peer market maker and HFT firm
- [[jane-street]] — peer quantitative trading firm
- [[defi]] — DeFi ecosystem where Jump Crypto operated
- [[solana]] — blockchain ecosystem Jump invested in heavily
- [[fpga]] — hardware acceleration technology Jump employs

## Sources

*No raw sources ingested yet. This page is based on public information about Jump Trading's operations and crypto activities.*

- [SEC — In the Matter of Tai Mo Shan Limited (settlement and distribution)](https://www.sec.gov/enforcement-litigation/distributions-harmed-investors/tai-mo-shan-limited)
- [SEC fines Jump Trading subsidiary $123 million over TerraUSD — The Block, 2024-12-20](https://www.theblock.co/post/332096/sec-fines-jump-trading-subsidiary-123-million-for-propping-up-terrausd-stablecoin-during-depeg)
- [(re)Introducing Jump Crypto — Jump Crypto, 2025](https://jumpcrypto.com/reintroducing-jump-crypto/)
- [Jump Crypto, General Catalyst lead $20M Series A for Ostium — CoinDesk, 2025-12-03](https://www.coindesk.com/business/2025/12/03/ostium-raises-usd20m-series-a-led-by-general-catalyst-jump-crypto-to-put-tradfi-perps-onchain)
- Verified via Perplexity (sonar) and web search, 2026-06-10
