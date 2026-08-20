# .lake-data

Canonical home for Black Lake DEP deposits.

## DEP classes and filing locations

Use exactly one DEP class per entry. The class is part of both the directory name and the filing location.

| Class | Purpose | Required location |
|---|---|---|
| `DEP-E` | Ongoing research, evaluations, literature reviews, and research artifacts expected to receive follow-up analysis. | `DEP-E/Series NNN/DEP-E-YYYYMMDD-Short Description/` |
| `DEP-A` | Long-term cold-storage artifacts whose contents and interpretation are intended to remain stable. | `DEP-A/Series NNN/DEP-A-YYYYMMDD-Short Description/` |
| `DEP-R` | Static records that are neither active research nor cold-storage artifacts. | `DEP-R/Series NNN/DEP-R-YYYYMMDD-Short Description/` |

Do not file a class-prefixed DEP entry directly under `.lake-data` or directly
under a class container. Every DEP object belongs in the Series assigned by the
class's `.index/series-map.json`.

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
2. Under the repository-wide deployment lock, validate the latest repository
   head and the selected class's `.index/series-map.json` with the shared
   [`automation-tools/dep_series.py`](../automation-tools/dep_series.py)
   helper.
3. Resolve an existing DEP by its stable identity or current/prior repository
   path. A repair retains its ordinal and Series. Never allocate by basename
   alone.
4. For a genuinely new DEP, supply an explicit stable object identity, allocate `next_ordinal`, and compute
   `series_number = ceil(ordinal / 1000)`. The helper, rather than a writer,
   chooses the `Series NNN` directory.
5. When allocating ordinal `1000k + 1`, create `Series (k+1)` in the same commit
   as its first DEP and seal the preceding Series in the map. Git does not track
   empty directories, so do not pre-create a Series or add placeholder files.
6. Add the required DEP contents and confirm every repository-relative or
   GitHub link uses the mapped Series path.
7. If the DEP reviews one or more arXiv papers or other research publications, update the matching publication index in the same change:
   - `DEP-E/.index/pubs-index.md` for a `DEP-E` entry;
   - `DEP-A/.index/pubs-index.md` for a `DEP-A` entry.
8. Append the Series-map assignment, advance `next_ordinal`, and stage the DEP,
   map, and applicable indexes atomically. A separately named correction or
   remediation DEP receives a new ordinal.
9. Add one index row for every publication actually reviewed. Record the canonical title, author attribution, canonical arXiv/DOI/publisher URL, and owning DEP entry. Do not index a paper that appears only as background reading or an unreviewed citation.
10. When a DEP is renamed, reclassified, corrected, or moved, update its map entry, index row, aliases, and all affected repository links in the same commit.
11. Revalidate the map/tree bijection and every changed link before committing.

Writers must fail closed on a stale repository head, duplicate identity or
alias, capacity drift, a full or premature Series, a missing map assignment,
or a map/tree mismatch. These layouts and behaviors are invalid:

- `.lake-data/DEP-X-*`;
- `.lake-data/DEP-X/DEP-X-*`;
- manual Series selection;
- basename-only lookup;
- allocation outside the deployment lock; and
- splitting one DEP and its map or required index update across commits.

For large collaborations, the index may use `First Author et al.` when the linked canonical record exposes the complete author list. Never infer or invent author names.

## Commit convention

The final commit completing a DEP must start with the DEP data subject title, for example:

```text
Semantically Enhanced PCFG for Password Analysis: add DEP-R-20260708-SEPCFG Paper
```
