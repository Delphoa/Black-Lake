# DEP-R - Static Records

This directory is the class container for Black Lake static-record deposits.

## Entry Layout

Every entry belongs directly under this directory and retains its full class-prefixed name:

```text
DEP-R/
|-- README.md
`-- DEP-R-YYYYMMDD-Short Description/
    |-- README.md
    `-- public-safe static records
```

Use `DEP-R` for stable records preserved for posterity that are neither evolving research nor cold-storage artifacts. Active research belongs in [`DEP-E`](../DEP-E/README.md); deliberately frozen long-term artifacts belong in [`DEP-A`](../DEP-A/README.md). Follow the repository-wide requirements in [`.lake-data/README.md`](../README.md).

## Discovery and Correction Contract

DEP-R currently has no class publication index. Each entry must preserve public-safe source locators in its README and expose any cross-class relationships through repository-relative links. If a static record needs correction or supersession, retain the prior provenance and add a clearly named correction/supersession record or a new linked DEP entry.
