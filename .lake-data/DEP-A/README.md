# DEP-A - Cold-Storage Artifacts

This directory is the class container for Black Lake long-term cold-storage deposits.

## Entry layout

Every entry belongs in the Series assigned by [the authoritative Series
map](.index/series-map.json) and retains its full class-prefixed name:

```text
DEP-A/
|-- .index/
|   |-- pubs-index.md
|   `-- series-map.json
|-- README.md
`-- Series NNN/
    `-- DEP-A-YYYYMMDD-Short Description/
        |-- README.md
        `-- public-safe archival artifacts
```

Each Series contains at most 1,000 DEP objects. Writers must use the shared
[`dep_series.py`](../../automation-tools/dep_series.py) helper under the
repository deployment lock; they may not select a Series manually. A new
allocation requires an explicit stable object identity. A new Series appears
only when its first DEP is committed, with the preceding Series
sealed and the map plus publication index updated in that same commit. Existing
DEP repairs retain their ordinal and Series; a new correction/remediation
object receives a new ordinal. Flat DEP-A paths are invalid.

Use `DEP-A` only for intentionally stable artifacts retained for long-horizon retrieval. Active research, iterative paper reviews, and evolving technical analysis belong in [`DEP-E`](../DEP-E/README.md). Follow the repository-wide requirements in [`.lake-data/README.md`](../README.md).

## Publication index contract

[`pubs-index.md`](.index/pubs-index.md) is the authoritative class-level map from research publications preserved or substantively reviewed by `DEP-A` entries. Add or update the relevant row in the same commit that creates, renames, corrects, reclassifies, or removes an entry.

[`series-map.json`](.index/series-map.json) is the authoritative ordinal and
location ledger. A DEP-A commit is incomplete unless the object, Series map,
and applicable publication-index change agree and validate against the same
repository head.

Use canonical publication metadata and public URLs. Scholarly source files downloaded by arXiv or research-paper automations remain local. Any other original-source deposition requires separate task authorization, redistribution-rights review, and public-safety checks.
