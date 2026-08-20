# DEP-A-20260818-ORFuzz Intake

#llm-safety #over-refusal #fuzz-testing #human-evaluation #benchmarking #model-judges #archival-intake #whitepaper-review

Public deposition date: 2026-08-18. This DEP-A is a new, public-safe archival intake derived by reviewing `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other` at source commit `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`. The paired task indicator is `BL-DEPPAIR-20260818-4022BD63`.

## Contents

- `README.md`
  - Classification, item inventory, summary, relevance, one-way provenance, associated records, and attribution.
- `whitepaper-intake-review.md`
  - Whitepaper-grade review covering source integrity, technical and evidentiary reconstruction, claim vetting, quantitative boundaries, independent re-conceptualization, failure modes, hypotheses, replication, and complete coverage.

## Summary of Items

The review treats the complete DEP-E repository record as its primary object. It distinguishes source reporting, directly inspected primary evidence, reviewer inference, and hypothesis. It does not copy the source record or claim independent reproduction.

The central durable finding is: ORFuzz turns over-refusal testing into adaptive boundary search: category-aware seed exploration and mutator selection seek benign prompts near safety-sensitive regions, while OR-Judge supplies a learned oracle calibrated against human judgments. The framework finds transferable failures, but its strongest numbers remain conditioned on the judge, category taxonomy, sampled human study, target-model versions, and the difficult normative boundary between caution and erroneous refusal.

## Insights and Relevance

This package converts a complete research record into an archival evidence object whose claims stay attached to source identity, evaluation coordinates, limitations, and falsifiers. It is intended for future research planning, implementation gating, and provenance-aware comparison.

Passing the included review methodology supports auditability, observability, and traceable lineage. It does not certify correctness, security, clinical readiness, legal compliance, privacy, fairness, or production safety.

## Provenance Pair

- Paired task indicator: `BL-DEPPAIR-20260818-4022BD63`
- Direction: `DEP-E -> DEP-A`
- Source DEP-E: `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other`
- Source commit: `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`
- Source action: review-only
- Source DEP modified: no
- Files moved: no
- Existing files copied into DEP-A: no
- New derived data generated: yes
- DEP-A intake status: complete only after validation and repository submission
- DEP-A deposition status: complete only after validation and repository submission
- This one-way pair does not reclassify, transfer, supersede, or mutate the DEP-E.

## Attribution Block

- Source DEP-E repository URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260817-ORFuzz%20Fuzzing%20the%20Other
  - Item: complete source record `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other` at `904c1bac689ba83c4ee1117d41a7cd5fbcdc8fff`
  - Notes: repository data was reviewed in place; no source DEP file was modified, moved, copied, renamed, deleted, or reclassified.
- Source URL: https://arxiv.org/abs/2508.11222
  - Item: Canonical arXiv identity and version record.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Source URL: https://arxiv.org/pdf/2508.11222
  - Item: Complete canonical paper inspected page by page; no source document uploaded.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Source URL: https://doi.org/10.1109/ASE63991.2025.00156
  - Item: Persistent primary-source identifier.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Generated review: `whitepaper-intake-review.md`
  - Item: new public-safe whitepaper-grade archival intake review
  - Notes: original derived prose; validated before submission; source documents and private processing evidence were not uploaded.
