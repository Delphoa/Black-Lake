# DEP-E - Ongoing Research

This directory is the class container for Black Lake exploratory and evolving research deposits.

## Entry layout

Every entry belongs directly under this directory and retains its full class-prefixed name:

```text
DEP-E/
|-- .index/
|   `-- pubs-index.md
|-- README.md
`-- DEP-E-YYYYMMDD-Short Description/
    |-- README.md
    `-- derived research artifacts
```

Use `DEP-E` for source-grounded reviews, literature syntheses, evaluations, technical investigations, and other research records that can receive later expansion or correction. Follow the repository-wide requirements in [`.lake-data/README.md`](../README.md).

## Publication index contract

[`pubs-index.md`](.index/pubs-index.md) is the authoritative class-level map from reviewed publications to their owning `DEP-E` entries. A submission that adds, removes, renames, or reclassifies a reviewed paper is incomplete until the index is updated in the same commit.

Index publications that the DEP actually analyzes. Do not promote related-reading references into the index unless the DEP contains a substantive review of them. Use a canonical arXiv abstract record, DOI, or publisher page and preserve author attribution from that source.

Locally archived source papers remain local and must not be committed to this public repository.
