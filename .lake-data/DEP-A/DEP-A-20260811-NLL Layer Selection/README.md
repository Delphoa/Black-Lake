# DEP-A-20260811-NLL Layer Selection

#artificial-intelligence #long-context #hybrid-attention #layer-selection #NLL #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.27791v1, *NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.27791-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.27791-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose NLL-guided layer selection for training-free sliding-window attention adaptation. Our contributions are: We introduce NLL-guided layer selection, a training-free method for identifying which layers should retain full attention in hybrid sliding-window models. We propose NLL-guided layer selection, a training-free method that directly measures each layer’s importance by computing the negative log-likelihood degradation on answer tokens when that layer uses sliding-window instead of full attention.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat NLL-guided full-attention placement as a calibrated deployment configuration: bind layer choices to model, tokenizer, calibration set, window, and answer-token definition, monitor OOD NLL drift, and restore full attention when the selected pattern no longer preserves task accuracy.

## Associated DEP Records

- [DEP-A-20260810-AB Sparse Attention](../DEP-A-20260810-AB%20Sparse%20Attention/README.md) - direct adaptive sparse-attention and long-context evaluation context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-UniPrefill](../DEP-A-20260810-UniPrefill/README.md) - direct sparse long-context prefill and acceleration context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.27791v1
  - Applies to: `2606.27791-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.27791v1
  - Applies to: `2606.27791-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.27791v1
  - Applies to: `2606.27791-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.27791
  - Applies to: `2606.27791-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Qiong Tang
  - arXiv author search: https://arxiv.org/search/?query=Qiong%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2606.27791-whitepaper-review.md`.
- Author: Xiangkun Hu
  - arXiv author search: https://arxiv.org/search/?query=Xiangkun%20Hu&searchtype=author
  - Applies to: the reviewed paper and `2606.27791-whitepaper-review.md`.
- Author: Xiangyang Liu
  - arXiv author search: https://arxiv.org/search/?query=Xiangyang%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.27791-whitepaper-review.md`.
- Author: Yiran Chen
  - arXiv author search: https://arxiv.org/search/?query=Yiran%20Chen&searchtype=author
  - Applies to: the reviewed paper and `2606.27791-whitepaper-review.md`.
- Author: Yunfan Shao
  - arXiv author search: https://arxiv.org/search/?query=Yunfan%20Shao&searchtype=author
  - Applies to: the reviewed paper and `2606.27791-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
