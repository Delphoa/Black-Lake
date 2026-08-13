# DEP-A-20260804-Turn Averaged SAEs

#artificial-intelligence #sparse-autoencoders #mechanistic-interpretability #long-context #attribution #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.28548v1, *Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.28548-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.28548-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Turn-averaged SAEs capture high-level features but cannot reconstruct per-token detail — the averaging discards the high-frequency component of the signal. The separation of the two underlying models does not allow typical analysis techniques such as attribution — the two feature sets are causally disconnected because the per-token SAE’s input h t − x ¯ h_{t}-\bar{x} is invariant to the uniform shifts produced by ablating turn-averaged features. We build multi-layer attribution graphs using the circuit-tracer framework (Ameisen & Lindsey 2025) with SAEs trained on the same Qwen model at layers 6, 11, 16, and 21 — roughly 20%, 40%, 60%, and 80% depth.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260729-Causal Intervention Based](../DEP-A-20260729-Causal%20Intervention%20Based/README.md) - direct causal-intervention and inference context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.28548v1
  - Applies to: `2606.28548-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.28548v1
  - Applies to: `2606.28548-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.28548v1
  - Applies to: `2606.28548-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.28548
  - Applies to: `2606.28548-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Kevin Der
  - arXiv author search: https://arxiv.org/search/?query=Kevin%20Der&searchtype=author
  - Applies to: the reviewed paper and `2606.28548-whitepaper-review.md`.
- Author: Harish Kamath
  - arXiv author search: https://arxiv.org/search/?query=Harish%20Kamath&searchtype=author
  - Applies to: the reviewed paper and `2606.28548-whitepaper-review.md`.
- Author: Ben Thompson
  - arXiv author search: https://arxiv.org/search/?query=Ben%20Thompson&searchtype=author
  - Applies to: the reviewed paper and `2606.28548-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
