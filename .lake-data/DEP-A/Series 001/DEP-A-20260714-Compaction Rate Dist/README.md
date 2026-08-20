# DEP-A-20260714-Compaction Rate Dist

#arxiv #large-language-models #agent-memory #context-compression #rate-distortion #information-theory #long-context #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“What to Keep, What to Forget: A Rate–Distortion View of Memory Compaction in LLMs and Agents,” arXiv:2607.08032v1**. The review reconstructs the paper’s cross-layer memory vocabulary, rate–distortion framing, benchmark, repeated-compaction analysis, limitations, and independent re-conceptualization. A complete PDF and full-paper HTML were verified from a local archive; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14  
Stable paper version: arXiv:2607.08032v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2607.08032-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, explains the review’s significance, identifies verified related repository context, and records complete public attribution.

### `2607.08032-whitepaper-review.md`

Audits the paper’s memory-layer taxonomy and information-theoretic claims, separates information capacity from physical or token budgets, reconstructs the reported repeated-compaction benchmark, and proposes a falsifiable evaluation framework. The validator passed the canonical review at 4,220 words.

## Insights and Relevance

The paper’s strongest contribution is a shared vocabulary for comparing compression at token, KV, latent-memory, summary, and archive layers. Its formalism is less complete than its presentation suggests: the query penalty is posited rather than derived, the Fano-style capacity bound does not directly cover arbitrary storage budgets, and the reversible-retrieval experiment excludes archive and index costs. The review preserves that distinction between a useful conceptual framework and an established quantitative law.

## Associated DEP Records

- [Delphoa-Labs raw same-paper context](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260711-Tech%20Intel%201311) — a verified same-paper source-context record in the related data repository; it is not a substitute for this substantive DEP-A review.

No same-paper DEP-A or DEP-E record was verified after checking class indexes, DEP READMEs, logs, reports, arXiv ID, DOI, normalized title, method, benchmark, and implementation.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.08032
- Canonical PDF: https://arxiv.org/pdf/2607.08032
- Canonical full-paper HTML: https://arxiv.org/html/2607.08032
- DOI: https://doi.org/10.48550/arXiv.2607.08032
- Authors from the canonical arXiv record:
  - Ashwin Gerard Colaco — https://arxiv.org/search/cs?query=Colaco%2C+A+G&searchtype=author
  - Nada Lahjouji — https://arxiv.org/search/cs?query=Lahjouji%2C+N&searchtype=author
- Applies to: `README.md` and `2607.08032-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
