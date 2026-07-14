# DEP-A-20260714-DepthWeave KV

#arxiv #kv-cache #long-context #low-rank-factorization #token-routing #language-model-inference #provenance #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression,” arXiv:2607.06523v1**. The review reconstructs the proposed token router, cross-layer residual factorization, training objectives, reported efficiency results, provenance defects, and independent tests required before the claims can be trusted. A complete PDF and full-paper HTML were verified from a local archive; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14  
Stable paper version: arXiv:2607.06523v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2607.06523-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, discloses the manuscript’s material provenance limitations, links verified same-paper records, and records complete attribution.

### `2607.06523-whitepaper-review.md`

Reconstructs the three-rank factorization and routing pipeline, audits the claimed calibration-free behavior against trained auxiliary components, cross-checks every table and figure, and documents missing model, hardware, optimization, code, and statistical details. The validator passed the canonical review at 3,693 words.

## Insights and Relevance

DepthWeave-KV describes a potentially useful adaptive rank-allocation mechanism, but its evidence is not presently assessable. The source includes a comment identifying a fixed synthetic byline, uses an accepted ICML 2024 template for a July 2026 paper, supplies synthetic institutional/contact details, omits the base model and experimental identity, and contains equation and ablation inconsistencies. These are provenance and reproducibility defects, not cosmetic formatting issues; the public record preserves them prominently.

## Associated DEP Records

- [DEP-E-20260710-Tech Intel 0101](../../DEP-E/DEP-E-20260710-Tech%20Intel%200101/README.md) — verified same-paper DEP-E context in this repository; it is related evidence, not a duplicate DEP-A review.
- [Delphoa-Labs same-paper context](https://github.com/Delphoa-Labs/Black-Lake-Data/tree/main/.lake-data/DEP-20260709-Tech%20Intel%200101) — verified same-paper source-context record in the related data repository.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.06523
- Canonical PDF: https://arxiv.org/pdf/2607.06523
- Canonical full-paper HTML: https://arxiv.org/html/2607.06523
- DOI: https://doi.org/10.48550/arXiv.2607.06523
- Authors from the canonical arXiv record:
  - Anna Cordoba — https://arxiv.org/search/cs?query=Cordoba%2C+A&searchtype=author
  - Adam Puente Tercero — https://arxiv.org/search/cs?query=Puente+Tercero%2C+A&searchtype=author
  - Nerea Angulo Hijo — https://arxiv.org/search/cs?query=Angulo+Hijo%2C+N&searchtype=author
  - Mar Linares Tercero — https://arxiv.org/search/cs?query=Linares+Tercero%2C+M&searchtype=author
  - Julia Barrientos — https://arxiv.org/search/cs?query=Barrientos%2C+J&searchtype=author
  - Ainhoa Miranda — https://arxiv.org/search/cs?query=Miranda%2C+A&searchtype=author
  - Jesus Olivera — https://arxiv.org/search/cs?query=Olivera%2C+J&searchtype=author
- Attribution qualification: the canonical record exposes these names, while the manuscript source itself labels the byline synthetic; the review does not independently authenticate author identities.
- Applies to: `README.md` and `2607.06523-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
