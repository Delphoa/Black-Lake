# DEP-A-20260812-Soft NBCE Fusion

#artificial-intelligence #long-context #chunk-fusion #entropy #distillation #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.01101v1, *Soft-NBCE: Entropy-Weighted Chunk Fusion for Long-Context*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.01101-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.01101-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose Soft-NBCE, which treats each chunk as a probabilistic expert and computes a continuous confidence distribution via an entropy-scaled Softmax. First, we propose Soft-NBCE, a temperature-parameterized log-space chunk fusion that unifies hard selection ( τ → 0 \tau\to 0 ) and uniform averaging ( τ → ∞ \tau\to\infty ) as limiting cases; an ablation identifies τ = 0.1 \tau{=}0.1 as a robust default (Section 6.3 ). Soft-NBCE runs n n forward passes of length L / n L/n , reducing the attention-side cost per chunk from O ​ ( L 2 ) O(L^{2}) to O ​ ( L 2 / n ) O(L^{2}/n) and peak KV-cache memory to O ​ ( L / n ) O(L/n) per chunk.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Model entropy-weighted chunk fusion as an approximate product-of-evidence controller: calibrate chunk entropy, temperature, cross-chunk dependence, and teacher mismatch, then test adversarial cases where each chunk is individually uncertain but their joint evidence is decisive.

## Associated DEP Records

- [DEP-A-20260714-LCLM Context Compression](../../Series%20001/DEP-A-20260714-LCLM%20Context%20Compression/README.md) - direct learned context and semantic-compression context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260725-RAR Reranking Intake](../../Series%20001/DEP-A-20260725-RAR%20Reranking%20Intake/README.md) - direct retrieval representation, reranking, and evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.01101v1
  - Applies to: `2606.01101-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.01101v1
  - Applies to: `2606.01101-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.01101v1
  - Applies to: `2606.01101-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.01101
  - Applies to: `2606.01101-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Shihao Ji
  - arXiv author search: https://arxiv.org/search/?query=Shihao%20Ji&searchtype=author
  - Applies to: the reviewed paper and `2606.01101-whitepaper-review.md`.
- Author: Mingyu Li
  - arXiv author search: https://arxiv.org/search/?query=Mingyu%20Li&searchtype=author
  - Applies to: the reviewed paper and `2606.01101-whitepaper-review.md`.
- Author: Zihui Song
  - arXiv author search: https://arxiv.org/search/?query=Zihui%20Song&searchtype=author
  - Applies to: the reviewed paper and `2606.01101-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
