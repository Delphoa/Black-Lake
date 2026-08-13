# DEP-A-20260812-VarRate KV Compression

#artificial-intelligence #KV-cache #compression #variable-rate-coding #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.15498v1, *VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.15498-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.15498-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We present VarRate, a training-free codec that compresses the KV cache by giving each token a variable low-rank budget, allocated by query salience under a fixed memory budget. At 5 × 5\times compression VarRate lands within 0.3 0.3 points of the uncompressed ceiling on Llama and 0.8 0.8 on Qwen (Table 1 ), and it has the best two-model mean of any matched-memory compressor. First, KIVI (2- and 4-bit) is reproduced in-pipeline rather than taken from published numbers; before trusting its comparison, we validate the reproduction directly on uncompressed-equivalent passage retrieval, where KIVI-2 ( ≈ 19 % \approx 19\% memory) reaches 100.0 100.0 and KIVI-4 ( ≈ 31 % \approx 31\% memory) reaches 99.5 99.5 —both within noise of the uncompressed ceiling, confirming the quantization implementation is not silently degrading accuracy on its own before any compression-specific comparison is drawn.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Interpret variable-rate KV compression as reversible fidelity allocation rather than eviction: log each token's salience, rank floor, basis, and reconstruction error, then stress stale-query salience and compare against matched-overhead uniform and query-agnostic codecs.

## Associated DEP Records

- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct learned context and semantic-compression context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.15498v1
  - Applies to: `2607.15498-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.15498v1
  - Applies to: `2607.15498-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.15498v1
  - Applies to: `2607.15498-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.15498
  - Applies to: `2607.15498-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Shahrzad Esmat
  - arXiv author search: https://arxiv.org/search/?query=Shahrzad%20Esmat&searchtype=author
  - Applies to: the reviewed paper and `2607.15498-whitepaper-review.md`.
- Author: Dhawal Shah
  - arXiv author search: https://arxiv.org/search/?query=Dhawal%20Shah&searchtype=author
  - Applies to: the reviewed paper and `2607.15498-whitepaper-review.md`.
- Author: Ali Jannesari
  - arXiv author search: https://arxiv.org/search/?query=Ali%20Jannesari&searchtype=author
  - Applies to: the reviewed paper and `2607.15498-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
