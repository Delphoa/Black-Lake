# DEP-A-20260814-Controllable Intake

#neural-rendering #NeRF #3D-portraits #illumination #facial-reanimation #archival-intake #whitepaper-review

Public deposition date: 2026-08-14. This DEP-A is a new, public-safe archival intake derived by reviewing `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic` at source commit `ef1ada6c114897ab17a91db92882139989f414e6`. The paired task indicator is `BL-DEPPAIR-20260814-37150705`.

## Contents

- `README.md`
  - Classification, item inventory, summary, relevance, one-way provenance, associated records, and attribution.
- `whitepaper-intake-review.md`
  - Whitepaper-grade review covering source integrity, technical and evidentiary reconstruction, claim vetting, quantitative boundaries, independent re-conceptualization, failure modes, hypotheses, replication, and complete coverage.

## Summary of Items

The review treats the complete DEP-E repository record as its primary object. It distinguishes source reporting, directly inspected primary evidence, reviewer inference, and hypothesis. It does not copy the source record or claim independent reproduction.

The central durable finding is: CoDyNeRF's core contribution is a conditional appearance factorization: deform portrait geometry into canonical space, infer dynamic surface normals with a 3D morphable-model prior, and condition appearance on normals, pose, expression, and view so cast shadows and specularities need not be baked into expression. Four-subject and synthetic evidence supports the factorization under captured lighting, while subject-specific training, no novel relighting, and misuse risk remain central.

## Insights and Relevance

This package converts a complete research record into an archival evidence object whose claims stay attached to source identity, evaluation coordinates, limitations, and falsifiers. It is intended for future research planning, implementation gating, and provenance-aware comparison.

Passing the included review methodology supports auditability, observability, and traceable lineage. It does not certify correctness, security, clinical readiness, legal compliance, privacy, fairness, or production safety.

## Provenance Pair

- Paired task indicator: `BL-DEPPAIR-20260814-37150705`
- Direction: `DEP-E -> DEP-A`
- Source DEP-E: `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic`
- Source commit: `ef1ada6c114897ab17a91db92882139989f414e6`
- Source action: review-only
- Source DEP modified: no
- Files moved: no
- Existing files copied into DEP-A: no
- New derived data generated: yes
- DEP-A intake status: complete only after validation and repository submission
- DEP-A deposition status: complete only after validation and repository submission
- This one-way pair does not reclassify, transfer, supersede, or mutate the DEP-E.

## Attribution Block

- Source DEP-E repository URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/Series%20001/DEP-E-20260813-Controllable%20Dynamic
  - Item: complete source record `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic` at `ef1ada6c114897ab17a91db92882139989f414e6`
  - Notes: repository data was reviewed in place; no source DEP file was modified, moved, copied, renamed, deleted, or reclassified.
- Source URL: https://arxiv.org/abs/2309.11009
  - Item: Canonical arXiv identity and version record.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Source URL: https://arxiv.org/html/2309.11009
  - Item: Complete primary paper inspected, including canonical deformation, normal and appearance models, four-subject results, synthetic controls, ablations, compute, and limitations.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Source URL: https://philgras.github.io/codynerf/
  - Item: Official project locator; model and media artifacts were not executed or reproduced.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Source URL: https://arxiv.org/pdf/2309.11009
  - Item: Canonical PDF locator; no source document uploaded.
  - Notes: Reviewed as primary or canonical evidence; no source document was uploaded.
- Generated review: `whitepaper-intake-review.md`
  - Item: new public-safe whitepaper-grade archival intake review
  - Notes: original derived prose; validated before submission; source documents and private processing evidence were not uploaded.
