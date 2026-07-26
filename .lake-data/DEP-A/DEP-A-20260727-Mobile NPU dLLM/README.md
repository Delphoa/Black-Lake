# DEP-A-20260727-Mobile NPU dLLM

#artificial-intelligence #diffusion-language-models #mobile-NPU #on-device-inference #GPU-kernels #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.13740v1, *Efficient On-Device Diffusion LLM Inference with Mobile NPU*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.13740-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.13740-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The llada.cpp framework maps block-wise diffusion decoding onto mobile NPU constraints. Multi-block speculation fills the NPU as current-block uncertainty shrinks, dual-path progressive revision keeps committed tokens revisable through a CPU path, and a swap-optimized runtime compacts NPU-visible memory while overlapping staging with compute.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Expose the diffusion scheduler as a thermal-aware work-conservation controller that logs speculative tokens, revisions, transfers, and NPU occupancy. The mechanism is weakened if the advantage disappears after matching a strong GPU/NPU baseline and sustained thermal envelope.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.13740v1
  - Applies to: `2606.13740-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.13740v1
  - Applies to: `2606.13740-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.13740v1
  - Applies to: `2606.13740-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.13740
  - Applies to: `2606.13740-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Tuowei Wang
  - arXiv author search: https://arxiv.org/search/?query=Tuowei%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.13740-whitepaper-review.md`.
- Author: Yanfan Sun
  - arXiv author search: https://arxiv.org/search/?query=Yanfan%20Sun&searchtype=author
  - Applies to: the reviewed paper and `2606.13740-whitepaper-review.md`.
- Author: Ju Ren
  - arXiv author search: https://arxiv.org/search/?query=Ju%20Ren&searchtype=author
  - Applies to: the reviewed paper and `2606.13740-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
