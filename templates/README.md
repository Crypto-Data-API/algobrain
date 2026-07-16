# Page Templates

Skeletons for each AlgoBrain wiki page type. Copy the matching template when
creating a new page so frontmatter and section structure stay consistent with
the schema in [`../CLAUDE.md`](../CLAUDE.md) / [`../AGENTS.md`](../AGENTS.md).

| Template | Use for |
|----------|---------|
| `category-index.md` | Category overview / index pages (`<category>-overview.md`) |
| `concept-page.md` | `type: concept` — indicators, risk, microstructure, etc. |
| `strategy-page.md` | `type: strategy` — the full strategy structure (edge, null hypothesis, kill criteria…) |
| `entity-page.md` | `type: entity` — exchanges, protocols, funds, people, regulators |
| `market-page.md` | `type: market` — crypto assets and macro instruments |
| `comparison-page.md` | `type: comparison` — head-to-head pages |
| `news-event.md` | `type: news` — dated, verified market events |
| `source-summary.md` | `type: source` — ingested source summaries (`wiki/sources/<id>.md`) |

Every new page MUST carry complete YAML frontmatter (`title`, `type`, `created`,
`updated`, `status`, `tags`). See the Frontmatter Schema section of `CLAUDE.md`.
