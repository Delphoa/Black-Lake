# DEP-R - Static Records

This directory is the class container for Black Lake static-record deposits.

## Entry Layout

Every entry belongs in the Series assigned by [the authoritative Series
map](.index/series-map.json) and retains its full class-prefixed name:

```text
DEP-R/
|-- .index/
|   `-- series-map.json
|-- README.md
`-- Series NNN/
    `-- DEP-R-YYYYMMDD-Short Description/
        |-- README.md
        `-- public-safe static records
```

Each Series contains at most 1,000 DEP objects. Writers must use the shared
[`dep_series.py`](../../automation-tools/dep_series.py) helper under the
repository deployment lock; they may not select a Series manually. A new
allocation requires an explicit stable object identity. A new Series appears
only when its first DEP is committed, with the preceding Series
sealed and the map updated in that same commit. Existing DEP repairs retain
their ordinal and Series; a new correction or supersession object receives a
new ordinal. Flat DEP-R paths are invalid.

Use `DEP-R` for stable records preserved for posterity that are neither evolving research nor cold-storage artifacts. Active research belongs in [`DEP-E`](../DEP-E/README.md); deliberately frozen long-term artifacts belong in [`DEP-A`](../DEP-A/README.md). Follow the repository-wide requirements in [`.lake-data/README.md`](../README.md).

## Discovery and Correction Contract

DEP-R currently has no class publication index. Each entry must preserve public-safe source locators in its README and expose any cross-class relationships through repository-relative links. If a static record needs correction or supersession, retain the prior provenance and add a clearly named correction/supersession record or a new linked DEP entry.

[`series-map.json`](.index/series-map.json) is the authoritative ordinal and
location ledger. A DEP-R commit is incomplete unless the object and map update
agree and validate against the same repository head.
