# DEP-A-20260719-HEAL Reproducibility

#artificial-intelligence #numerical-stability #reproducibility #quantization #GPU-kernels #mission-critical-systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.21023v1, *Demystifying Numerical Instability in LLM Inference: Achieving Reproducible Inference for Mission-Critical Tasks with HEAL*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.21023-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.21023-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HEAL attributes cross-GPU greedy-decoding divergence to truncation at kernel boundaries and targets the implicated operations instead of converting the whole pipeline to FP32. It stores Q, K, and V through INT16 quantization and synthesizes higher-precision matrix products with error compensation executed on 16-bit Tensor Cores.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use sensitivity-guided precision: locate token and layer margins online, activate compensated kernels only where predicted numerical error can cross a decision boundary, and certify a hardware/kernel matrix with adversarial near-tie prompts and repeated cross-device trials.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.21023v1
  - Applies to: `2606.21023-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.21023v1
  - Applies to: `2606.21023-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.21023v1
  - Applies to: `2606.21023-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.21023
  - Applies to: `2606.21023-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Zhenting Zhu
  - arXiv author search: https://arxiv.org/search/?query=Zhenting%20Zhu&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Lucas Thai
  - arXiv author search: https://arxiv.org/search/?query=Lucas%20Thai&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Shan Yu
  - arXiv author search: https://arxiv.org/search/?query=Shan%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Yicheng Liu
  - arXiv author search: https://arxiv.org/search/?query=Yicheng%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Yifan Qiao
  - arXiv author search: https://arxiv.org/search/?query=Yifan%20Qiao&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Chenxi Wang
  - arXiv author search: https://arxiv.org/search/?query=Chenxi%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Harry Xu
  - arXiv author search: https://arxiv.org/search/?query=Harry%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Author: Junyi Shu
  - arXiv author search: https://arxiv.org/search/?query=Junyi%20Shu&searchtype=author
  - Applies to: the reviewed paper and `2606.21023-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
