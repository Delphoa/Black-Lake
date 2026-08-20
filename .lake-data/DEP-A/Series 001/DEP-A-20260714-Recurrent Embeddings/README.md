# DEP-A-20260714-Recurrent Embeddings

#arxiv #text-embeddings #recurrent-models #mamba #long-documents #constant-memory #retrieval #representation-learning #machine-learning

This DEP-A entry preserves a public-safe, whitepaper-grade full-paper review of **“Linear-Time and Constant-Memory Text Embeddings Based on Recurrent Language Models,” arXiv:2604.18199v1**. The review reconstructs the recurrent embedding pipeline, chunkable state handling, training and evaluation, MTEB and LongEmbed results, ablations, resource semantics, external release checks, limitations, and an independent re-conceptualization. A complete PDF and full-paper HTML were verified from a local archive; source documents remain local and are withheld from this repository.

Deposition date: 2026-07-14  
Stable paper version: arXiv:2604.18199v1

## Contents

- `README.md` — deposition context, complete inventory, relationships, and attribution.
- `2604.18199-whitepaper-review.md` — validated public-safe full-paper review and independent re-conceptualization.

## Summary of Items

### `README.md`

Defines the stable record, inventories both files, explains the long-document embedding relevance, and attributes the paper, benchmarks, and released checkpoints.

### `2604.18199-whitepaper-review.md`

Reconstructs recurrent state aggregation and chunkable execution, audits claimed linear-time and constant-input-length-memory behavior, covers benchmark tables and ablations, verifies the public model collection, and proposes replication and streaming tests. The validator passed the canonical review at 5,410 words.

## Insights and Relevance

The durable contribution is a text-embedding interface whose working memory can stop growing with document length after fixed chunk dimensions are chosen. That is valuable for streaming and long-corpus retrieval, while the review preserves the boundary that “constant memory” still depends on model depth, recurrent state, batch, precision, and selected chunk configuration.

## Associated DEP Records

No same-paper or directly corresponding DEP record was verified after checking the live class indexes, DEP READMEs, logs, reports, and relevant Delphoa-Labs/Black-Lake-Data entries by arXiv ID, DOI, normalized title, architecture, benchmark, and official model collection.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.18199
- Canonical PDF: https://arxiv.org/pdf/2604.18199
- Canonical full-paper HTML: https://arxiv.org/html/2604.18199
- DOI: https://doi.org/10.48550/arXiv.2604.18199
- Official release collection: https://huggingface.co/collections/dynatrace-oss/embed-mamba2
- MTEB sources: https://arxiv.org/abs/2210.07316 and https://docs.mteb.org/
- MMTEB source: https://arxiv.org/abs/2502.13595
- LongEmbed source: https://arxiv.org/abs/2404.12096
- Authors from the canonical arXiv record:
  - Tobias Grantner — https://arxiv.org/search/cs?query=Grantner%2C+T&searchtype=author
  - Emanuel Sallinger — https://arxiv.org/search/cs?query=Sallinger%2C+E&searchtype=author
  - Martin Flechl — https://arxiv.org/search/cs?query=Flechl%2C+M&searchtype=author
- Applies to: `README.md` and `2604.18199-whitepaper-review.md`.
- Verification note: complete source documents were verified locally and withheld from this repository.
