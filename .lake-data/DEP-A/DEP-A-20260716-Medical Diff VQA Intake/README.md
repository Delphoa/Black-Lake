# DEP-A-20260716-Medical Diff VQA Intake

#medical-ai #visual-question-answering #chest-radiography #graph-learning #longitudinal-imaging #mimic-cxr #archival-intake #whitepaper-review

Public deposition date: 2026-07-16. This DEP-A is a new, public-safe archival intake derived by reviewing `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA` at source commit `b5ad2459a6ee3d649feb8209d9390d86d475502c`. The paired task indicator is `BL-DEPPAIR-20260716-672AC475`.

## Contents

- `README.md`
  - Classification, item inventory, summary, relevance, one-way provenance, associated records, and attribution.
- `medical-diff-vqa-intake-review.md`
  - Whitepaper-grade intake review covering dataset construction, expert-graph architecture, quantitative and ablation audit, shortcut and clinical boundaries, claim vetting, re-conceptualization, falsifiable hypotheses, and complete DEP-E coverage.

## Summary of Items

The review treats the complete two-file DEP-E repository record as its primary object. It directly checks the canonical arXiv identity and abstract, while attributing table-level results, dataset details, code and data status, and clinical caveats to the DEP-E report that records complete paper and public-resource inspection. The current intake did not independently rerun the code, download restricted data, or re-read the external full paper.

The durable finding is that longitudinal medical VQA is best decomposed into alignment, structured change representation, and answer generation. The reported graph model improves total and closed-question accuracy, yet open-question performance remains weak and some ablations outperform the full graph on individual metrics. Benchmark success therefore demonstrates a useful representation signal, not clinical readiness or causal faithfulness.

## Insights and Relevance

The artifact converts a large synthetic QA benchmark into a provenance-aware evaluation framework. It isolates question generation, detector quality, image-pair alignment, graph relations, answer type, and clinical validity as distinct error sources. This is relevant to medical multimodal systems because aggregate accuracy can hide clinically asymmetric errors and language shortcuts.

Passing the included review methodology supports auditability and traceable lineage. It does not certify patient safety, diagnostic performance, fairness, privacy, calibration, external validity, or clinical utility.

## Provenance Pair

- Paired task indicator: `BL-DEPPAIR-20260716-672AC475`
- Direction: `DEP-E -> DEP-A`
- Source DEP-E: `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA`
- Source commit: `b5ad2459a6ee3d649feb8209d9390d86d475502c`
- Source action: review-only
- Source DEP modified: no
- Files moved: no
- Existing files copied into DEP-A: no
- New derived data generated: yes
- DEP-A intake status: complete only after validation and repository submission
- DEP-A deposition status: complete only after validation and repository submission
- This one-way pair does not reclassify, transfer, supersede, or mutate the DEP-E.

## Associated DEP Records

- [`.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA`](https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA) — verified source record for this intake.

## Attribution Block

- Source DEP-E repository URL: https://github.com/Delphoa/Black-Lake/tree/main/.lake-data/DEP-E/DEP-E-20260716-Medical%20Diff%20VQA
  - Item: complete source record at source commit `b5ad2459a6ee3d649feb8209d9390d86d475502c`.
  - Notes: repository data was reviewed in place; no source DEP file was modified, moved, copied, renamed, deleted, or reclassified.
- Source URL: https://arxiv.org/abs/2307.11986v2
  - Item: canonical identity, abstract, authorship, version, and access record for “Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering.”
  - Notes: canonical metadata was directly inspected; the external full paper was not independently re-read in this intake, and no source document was uploaded.
- Source URL: https://doi.org/10.1145/3580305.3599819
  - Item: KDD publication DOI reported by the DEP-E.
  - Notes: used for publication provenance.
- Source URL: https://physionet.org/content/medical-diff-vqa/1.0.1/
  - Item: official Medical-Diff-VQA dataset record reported by the DEP-E.
  - Notes: access context only; no data or patient-derived source material was downloaded or uploaded.
- Source URL: https://github.com/Holipori/MIMIC-Diff-VQA
  - Item: public dataset/code repository reported by the DEP-E.
  - Notes: not executed, copied, or deposited in this intake.
- Source URL: https://github.com/Holipori/Medical_Diff_VQA
  - Item: public model repository reported by the DEP-E.
  - Notes: not executed, copied, or deposited in this intake.
- Generated review: `medical-diff-vqa-intake-review.md`
  - Item: new public-safe whitepaper-grade archival intake review.
  - Notes: original derived prose validated before submission; repository data was reviewed in place, and source documents, data, code, private coverage notes, and validator output were not uploaded.
