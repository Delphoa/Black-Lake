# DEP-A-20260724-EntropyInfer KV

#artificial-intelligence #long-context #attention-entropy #KV-cache #sparse-attention #efficient-inference

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.09508v1, *From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.09508-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.09508-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: EntropyInfer uses per-head, per-segment attention entropy to choose sparse prefill blocks and then applies latent KV compression during decoding. The core claim is that head sparsity and its context-dependent shifts are heterogeneous enough that fixed geometric or globally uniform sparsity wastes compute or quality.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use entropy as a calibrated routing signal with per-head drift monitoring, a short-context bypass, task-level quality sentinels, and reversible restoration when latent decode evidence diverges from prefill evidence.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct cache-budget and efficient-attention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.09508v1
  - Applies to: `2606.09508-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.09508v1
  - Applies to: `2606.09508-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.09508v1
  - Applies to: `2606.09508-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.09508
  - Applies to: `2606.09508-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/SHA-4096/EntropyInfer
  - Applies to: reproducibility context in `2606.09508-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Zhanchao Xu
  - arXiv author search: https://arxiv.org/search/?query=Zhanchao%20Xu&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Author: Haoyang Li
  - arXiv author search: https://arxiv.org/search/?query=Haoyang%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Author: Qingfa Xiao
  - arXiv author search: https://arxiv.org/search/?query=Qingfa%20Xiao&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Author: Fei Teng
  - arXiv author search: https://arxiv.org/search/?query=Fei%20Teng&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Author: Chen Jason Zhang
  - arXiv author search: https://arxiv.org/search/?query=Chen%20Jason%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Author: Lei Chen
  - arXiv author search: https://arxiv.org/search/?query=Lei%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Author: Qing Li
  - arXiv author search: https://arxiv.org/search/?query=Qing%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.09508-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
