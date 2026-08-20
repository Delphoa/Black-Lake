# DEP-E - Ongoing Research

This directory is the class container for Black Lake exploratory and evolving research deposits.

## Entry layout

Every entry belongs in the Series assigned by [the authoritative Series
map](.index/series-map.json) and retains its full class-prefixed name:

```text
DEP-E/
|-- .index/
|   |-- pubs-index.md
|   `-- series-map.json
|-- README.md
`-- Series NNN/
    `-- DEP-E-YYYYMMDD-Short Description/
        |-- README.md
        `-- derived research artifacts
```

Each Series contains at most 1,000 DEP objects. Writers must use the shared
[`dep_series.py`](../../automation-tools/dep_series.py) helper under the
repository deployment lock; they may not select a Series manually. A new
allocation requires an explicit stable object identity. A new Series appears
only when its first DEP is committed, with the preceding Series
sealed and the map plus publication index updated in that same commit. Existing
DEP repairs retain their ordinal and Series; a new correction/remediation
object receives a new ordinal. Flat DEP-E paths are invalid.

Use `DEP-E` for source-grounded reviews, literature syntheses, evaluations, technical investigations, and other research records that can receive later expansion or correction. Follow the repository-wide requirements in [`.lake-data/README.md`](../README.md).

## Publication index contract

[`pubs-index.md`](.index/pubs-index.md) is the authoritative class-level map from reviewed publications to their owning `DEP-E` entries. A submission that adds, removes, renames, or reclassifies a reviewed paper is incomplete until the index is updated in the same commit.

[`series-map.json`](.index/series-map.json) is the authoritative ordinal and
location ledger. A DEP-E commit is incomplete unless the object, Series map,
and applicable publication-index change agree and validate against the same
repository head.

Index publications that the DEP actually analyzes. Do not promote related-reading references into the index unless the DEP contains a substantive review of them. Use a canonical arXiv abstract record, DOI, or publisher page and preserve author attribution from that source.

Locally archived source papers remain local and must not be committed to this public repository.
