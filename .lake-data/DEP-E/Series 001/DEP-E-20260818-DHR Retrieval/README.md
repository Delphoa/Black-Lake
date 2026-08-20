# DEP-E-20260818-DHR Retrieval

#arxiv #information-retrieval #dense-retrieval #open-domain-qa #RAG #evidence-governance

This DEP-E contains a public-safe source-grounded review of *Dense Hierarchical Retrieval for Open-Domain Question Answering* (arXiv:2110.15439v1; Findings of EMNLP 2021). The local source unit was repaired and verified before review. Original PDF, full-paper HTML, metadata, cache, provenance, and source-package evidence remain local and are not included here.

## Contents

- `README.md` — public-safe inventory, summary, relevance, and attribution.
- `dhr_retrieval_manuscript.md` — schema-complete manuscript research artifact covering source metadata, evidence ledger, method, results, limitations, implementation paths, exercises, and replication checklist.

## Summary of Items

### `dhr_retrieval_manuscript.md`

The manuscript reviews DHR’s structural document title tree, document-level and passage-level dual encoders, section-consistent passage splitting, title-path augmentation, hard negatives, iterative training, score fusion, benchmark evidence, timing boundary, code context, and reproducibility limits. It records the random-selection and deduplication methodology, the repaired complete-source result, exactly three safe exercise paths, and public source references.

## Insights and Relevance

DHR makes document-to-section lineage an active retrieval signal rather than discarding it during passage construction. Its reported gains connect structure-aware representation, staged search-space reduction, hard-negative training, and score calibration, while its limitations show why index-search speed is not equivalent to end-to-end serving efficiency. The artifact is relevant to RAG chunking, query planning, typed retrieval, provenance, freshness, authorization, and abstention design; it should be used as research context and implementation input, not as proof of current production readiness.

## Attribution Block

- Source URL: https://arxiv.org/abs/2110.15439
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Canonical arXiv metadata, title, authors, version, abstract, and public source links.
- Source URL: https://arxiv.org/html/2110.15439
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Full-paper method, experiments, tables, appendices, and conclusion; local copy withheld.
- Source URL: https://arxiv.org/pdf/2110.15439
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Primary PDF cross-check; local copy withheld.
- Source URL: https://doi.org/10.48550/arXiv.2110.15439
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: ArXiv-issued DOI record.
- Source URL: https://aclanthology.org/2021.findings-emnlp.19/
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Findings of EMNLP 2021 publication record, pages 188–200, DOI, and software locator.
- Source URL: https://doi.org/10.18653/v1/2021.findings-emnlp.19
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Publication DOI.
- Source URL: https://github.com/yeliu918/DHR
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Author-linked implementation context; code, data, and checkpoints were not executed or redistributed.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-RAG%20Chunking%20Study/2607.01852-whitepaper-review.md
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Related DEP evidence about RAG chunking and evidence-unit boundaries.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260717-PlanRAG%20Query%20Trees/2607.00508-whitepaper-review.md
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Related DEP evidence about hierarchical planning, staged retrieval, and cost/latency control.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/Series%20001/DEP-A-20260725-SchemaFirst%20Retrieval/2606.28387-whitepaper-review.md
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Related DEP evidence about typed retrieval, reranking, provenance, and access control.
- Source files: local-only verified PDF, full-paper HTML, metadata HTML, provenance, verification, receipts, and optional-source failure record.
  - Applies to: `dhr_retrieval_manuscript.md`
  - Notes: Withheld from the public repository and Slack; no `.source/` directory was created.
