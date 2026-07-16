# Raw Sources

Raw source documents that feed the AlgoBrain ingest workflow. The LLM agent
**reads** these but does not treat them as wiki pages — it extracts claims from
them into `wiki/sources/<source-id>.md` summaries and the interlinked wiki pages
they contribute to (see the Ingest Workflow in [`../CLAUDE.md`](../CLAUDE.md)).

Organized by source type:

| Folder | Contents |
|--------|----------|
| `articles/` | Article / web-page captures, named `YYYY-MM-DD-slug.md` |
| `data/` | Structured data pulls and datasets used as inputs |
| `misc/` | Everything else (notes, transcripts, ad-hoc captures) |

Each ingested source should end up with a matching summary under
`wiki/sources/` and an entry in `wiki/log.md`.
