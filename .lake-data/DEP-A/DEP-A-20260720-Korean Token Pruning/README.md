# DEP-A-20260720-Korean Token Pruning

#artificial-intelligence #language-models #token-pruning #Korean-NLP #model-compression #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2604.16235v1, *Optimizing Korean-Centric LLMs via Token Pruning*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2604.16235-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2604.16235-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The study removes vocabulary entries and their embedding parameters for languages outside Korean-centric deployment, comparing original, English-Korean, and English-Korean-Chinese vocabularies across Qwen3, Gemma-3, Llama-3, and Aya. The intervention targets vocabulary and embedding storage, not sequence-length pruning inside attention layers.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat vocabulary pruning as a reversible deployment profile: retain an escape vocabulary, measure per-domain unknown and fragmentation rates, and route inputs to broader profiles when code-switching or rare-token coverage crosses a calibrated threshold.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct context-compression method context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2604.16235v1
  - Applies to: `2604.16235-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2604.16235v1
  - Applies to: `2604.16235-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2604.16235v1
  - Applies to: `2604.16235-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2604.16235
  - Applies to: `2604.16235-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Hoyeol Kim
  - arXiv author search: https://arxiv.org/search/?query=Hoyeol%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2604.16235-whitepaper-review.md`.
- Author: Hyeonwoo Kim
  - arXiv author search: https://arxiv.org/search/?query=Hyeonwoo%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2604.16235-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
