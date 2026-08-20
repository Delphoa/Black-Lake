# DEP-A-20260714-H2MT Memory

#arxiv #long-context #hierarchical-memory #semantic-routing #memory-tokens #retrieval-augmented-generation #language-model-inference #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“H²MT: Semantic Hierarchy-Aware Hierarchical Memory Transformer,” arXiv:2605.24930v1**. The review reconstructs offline hierarchy construction, one-vector node memories, training objectives, top-down query routing, twelve tables, four figures, publication history, reproducibility gaps, and an independent multiresolution-index interpretation. A complete PDF and full-paper HTML were verified from a local archive; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14  
Stable paper version: arXiv:2605.24930v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2605.24930-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, explains the architecture and review boundary, records publication status, and provides complete public attribution.

### `2605.24930-whitepaper-review.md`

Reconstructs leaf and internal memory formation, routing and generation, training losses, complexity, public and private benchmark evidence, all tables and figures, missing artifacts, and falsifiable hybrid-routing proposals. The validator passed the canonical review at 5,502 words.

## Insights and Relevance

H²MT’s strongest idea is to treat a document hierarchy as an amortized multiresolution latent index: build it once, route queries through it, and prefill only selected node vectors. The paper reports large TTFT reductions against HMT, but code, checkpoints, exact configurations, seeds, hardware, raw predictions, and one private benchmark are unavailable. OpenReview also records an earlier withdrawn ICLR 2026 submission. The record therefore preserves a promising expanded preprint while clearly separating architecture from independently reproducible evidence.

## Associated DEP Records

No same-paper or directly corresponding DEP-A, DEP-E, or relevant Delphoa-Labs/Black-Lake-Data record was verified after checking class indexes, DEP READMEs, logs, reports, arXiv ID, DOI, normalized title, method, benchmark, and implementation. HMT and RAPTOR are verified predecessor/benchmark publications, not same-paper DEP records.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.24930
- Canonical PDF: https://arxiv.org/pdf/2605.24930
- Canonical full-paper HTML: https://arxiv.org/html/2605.24930
- DOI: https://doi.org/10.48550/arXiv.2605.24930
- OpenReview publication-history record: https://openreview.net/forum?id=X8EpTbI5ov
- HMT predecessor publication and code: https://aclanthology.org/2025.naacl-long.410/ and https://github.com/OswaldHe/HMT-pytorch
- RAPTOR benchmark publication and code: https://arxiv.org/abs/2401.18059 and https://github.com/parthsarthi03/raptor
- Authors from the canonical arXiv record:
  - Maryam Haghifam — https://arxiv.org/search/cs?query=Haghifam%2C+M&searchtype=author
  - Zifan He — https://arxiv.org/search/cs?query=He%2C+Z&searchtype=author
  - Jason Cong — https://arxiv.org/search/cs?query=Cong%2C+J&searchtype=author
  - Yizhou Sun — https://arxiv.org/search/cs?query=Sun%2C+Y&searchtype=author
- Applies to: `README.md` and `2605.24930-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
