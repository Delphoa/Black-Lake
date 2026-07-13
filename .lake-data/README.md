# .lake-data

Canonical home for Black Lake DEP deposits.

## DEP classes and filing locations

Use exactly one DEP class per entry. The class is part of both the directory name and the filing location.

| Class | Purpose | Required location |
|---|---|---|
| `DEP-E` | Ongoing research, evaluations, literature reviews, and research artifacts expected to receive follow-up analysis. | `DEP-E/DEP-E-YYYYMMDD-Short Description/` |
| `DEP-A` | Long-term cold-storage artifacts whose contents and interpretation are intended to remain stable. | `DEP-A/DEP-A-YYYYMMDD-Short Description/` |
| `DEP-R` | Static records that are neither active research nor cold-storage artifacts. | `.lake-data/DEP-R-YYYYMMDD-Short Description/` until a separate `DEP-R` container is adopted. |

Do not file a `DEP-E-*` or `DEP-A-*` directory directly under `.lake-data`. Do not place `DEP-R` records inside either class container.

Choose `DEP-E` when the entry analyzes research, compares evidence, tracks an evolving technical question, or is expected to be expanded. Choose `DEP-A` only when the artifact is intentionally frozen for durable retention and future retrieval rather than active research. If neither description fits, use the existing `DEP-R` static-record class.

## Required DEP contents

Each DEP entry must include:

- a `README.md`;
- classification tags;
- an itemized inventory;
- an explanation of each item's purpose;
- insights and relevance notes; and
- a final Attribution Block with public-safe source locators.

Source documents downloaded by arXiv or research-paper automations must remain local and must not be committed. Publish allowed derived artifacts, public URLs, and public-safe provenance instead. Any other original-source deposition requires separate task authorization, redistribution-rights review, and removal of private filesystem paths, machine identifiers, credentials, and other private material.

## Filing workflow

1. Select exactly one class before creating the entry.
2. Create the entry inside the matching class container using the required class prefix and date: `DEP-E/DEP-E-YYYYMMDD-Short Description/` or `DEP-A/DEP-A-YYYYMMDD-Short Description/`.
3. Add the required DEP contents and confirm every repository-relative or GitHub link uses the containerized path.
4. If the DEP reviews one or more arXiv papers or other research publications, update the matching publication index in the same change:
   - `DEP-E/.index/pubs-index.md` for a `DEP-E` entry;
   - `DEP-A/.index/pubs-index.md` for a `DEP-A` entry.
5. Add one index row for every publication actually reviewed. Record the canonical title, author attribution, canonical arXiv/DOI/publisher URL, and owning DEP entry. Do not index a paper that appears only as background reading or an unreviewed citation.
6. When a DEP is renamed, reclassified, corrected, or moved, update its index row and all affected repository links in the same commit.
7. Verify that the entry path exists, each publication row resolves to an owning DEP, and no root-level `DEP-E-*` or `DEP-A-*` directory remains.

For large collaborations, the index may use `First Author et al.` when the linked canonical record exposes the complete author list. Never infer or invent author names.

## Commit convention

The final commit completing a DEP must start with the DEP data subject title, for example:

```text
Semantically Enhanced PCFG for Password Analysis: add DEP-R-20260708-SEPCFG Paper
```
