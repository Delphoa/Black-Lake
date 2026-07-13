# DEP-A - Cold-Storage Artifacts

This directory is the class container for Black Lake long-term cold-storage deposits.

## Entry layout

Every entry belongs directly under this directory and retains its full class-prefixed name:

```text
DEP-A/
|-- .index/
|   `-- pubs-index.md
|-- README.md
`-- DEP-A-YYYYMMDD-Short Description/
    |-- README.md
    `-- public-safe archival artifacts
```

Use `DEP-A` only for intentionally stable artifacts retained for long-horizon retrieval. Active research, iterative paper reviews, and evolving technical analysis belong in [`DEP-E`](../DEP-E/README.md). Follow the repository-wide requirements in [`.lake-data/README.md`](../README.md).

## Publication index contract

[`pubs-index.md`](.index/pubs-index.md) is the authoritative class-level map from research publications preserved or substantively reviewed by `DEP-A` entries. Add or update the relevant row in the same commit that creates, renames, corrects, reclassifies, or removes an entry.

Use canonical publication metadata and public URLs. Scholarly source files downloaded by arXiv or research-paper automations remain local. Any other original-source deposition requires separate task authorization, redistribution-rights review, and public-safety checks.
