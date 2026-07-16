---
title: "Data Universe (SN13)"
type: entity
created: 2026-04-19
updated: 2026-07-16
status: draft
tags: [alternative-data, bittensor, crypto, social-media]
aliases: ["Data Universe", "SN13"]
entity_type: protocol
headquarters: "Decentralized"
website: "https://www.macrocosmos.ai/sn13"
related: ["[[alternative-data-providers]]", "[[bittensor-subnets]]", "[[bittensor]]", "[[crypto-markets]]", "[[dtao]]", "[[masa-subnet]]", "[[sentiment-trading]]", "[[social-arbitrage]]"]
---

> *As of 2026-06-12 this asset is outside the CoinGecko top 1000; figures below are the last cached snapshot and should be treated as stale.*

# Data Universe (SN13)

**Data Universe** (SN13) is a Bittensor subnet run by Macrocosmos that incentivizes decentralized scraping of social platforms -- primarily X (Twitter) and Reddit -- into a public, queryable dataset. Miners run scrapers and submit data shards; validators verify coverage, freshness, and deduplication. The result is a continuously-updated, decentralized alternative-data feed for the Bittensor ecosystem.

## How It Works

Miners are assigned target keywords, handles, subreddits, or time windows. They submit scraped rows to a decentralized store. Validators sample-check coverage and quality against known-good references. The dataset is queryable by other subnets and by external consumers (though the external consumption model is still maturing as of April 2026).

## Trading Relevance

SN13 is directly useful for [[sentiment-trading]] and [[social-arbitrage]] strategies -- it is effectively a decentralized, cheap alternative to Twitter/X API access (which became expensive in 2023) and Reddit API access (same). As Twitter/X API pricing has squeezed out smaller alternative-data vendors, SN13 has picked up share as an alt-data source for decentralized applications.

## Related

- [[bittensor]], [[bittensor-subnets]], [[dtao]] -- protocol context
- [[masa-subnet]] (SN42) -- parallel data-scraping subnet with different focus
- [[alternative-data-providers]] -- broader alt-data ecosystem
- [[sentiment-trading]], [[social-arbitrage]] -- strategies that consume this data
- [[chris-camillo]] -- retail exemplar of the social-arbitrage methodology

## Sources

- (Source: [[coingecko-top-1000-2026-07-16]])

## See Also

- [[crypto-markets]]

---
