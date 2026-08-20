# DEP-A-20260717-HyperQuant Pipeline

#machine-learning #quantization #rate-distortion #llm-serving #diffusion-models #kv-cache

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.23406v1, *HyperQuant: A Rate-Distortion-Optimal Quantization Pipeline for Large Language and Diffusion Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.23406-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.23406-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HyperQuant combines randomized Hadamard transforms, optimal low-dimensional lattices, lossless bit stripping with Rice coding, and KV bias correction. It integrates decoded values with several Tensor Core arithmetic paths for language and diffusion transformers.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Publish a true-rate ledger including headers, decoder workspace, kernel occupancy, and error tails, then test whether the chosen lattice remains optimal after random-access and serving constraints are priced.

## Associated DEP Records

- [DEP-A-20260716-KV Memory Hierarchy](../DEP-A-20260716-KV%20Memory%20Hierarchy/README.md) - direct method context: reviewed survey of KV-cache representation, movement, reuse, and memory hierarchy. This is method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.23406v1
  - Applies to: `2606.23406-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.23406v1
  - Applies to: `2606.23406-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.23406v1
  - Applies to: `2606.23406-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.23406
  - Applies to: `2606.23406-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://moonmath.ai/hyperquant/
  - Applies to: reproducibility context in `2606.23406-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Yuval Domb
  - arXiv author search: https://arxiv.org/search/?query=Yuval%20Domb&searchtype=author
  - Applies to: the reviewed paper and `2606.23406-whitepaper-review.md`.
- Author: Hadar Sackstein
  - arXiv author search: https://arxiv.org/search/?query=Hadar%20Sackstein&searchtype=author
  - Applies to: the reviewed paper and `2606.23406-whitepaper-review.md`.
- Author: Tomer Solberg
  - arXiv author search: https://arxiv.org/search/?query=Tomer%20Solberg&searchtype=author
  - Applies to: the reviewed paper and `2606.23406-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
