# DEP-A-20260804-ReQAT FP4 Reasoning

#artificial-intelligence #quantization-aware-training #FP4 #reasoning #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.15682v1, *ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.15682-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.15682-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: 3 that quantization-induced errors disproportionately affect low-entropy predictions, we propose ReQAT, a unified framework for training FP4 LRMs that explicitly addresses this failure mode. In this work, we propose ReQAT, a reasoning-centric training framework motivated by the novel insight that LRM quantization failures concentrate on low-entropy tokens. Based on this insight, we propose ReQAT, a reasoning-centric FP4 training framework with three components: (i) Trace-Aligned QAT (TAQ), which revisits identical reasoning traces to focus updates on critical low-entropy decisions; (ii) Selective Entropy Minimization (SEM), which reinforces confidence at low-entropy positions; and (iii) Q-FIT, a quantization-friendly initialization that jointly calibrates RoPE-consistent KV cache transformations to stabilize QAT.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat ReQAT: Achieving Full-Precision Reasoning Accuracy with 4-bit Floating-Point Quantization-Aware Training as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.15682v1
  - Applies to: `2606.15682-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.15682v1
  - Applies to: `2606.15682-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.15682v1
  - Applies to: `2606.15682-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.15682
  - Applies to: `2606.15682-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/aiha-lab/ReQAT
  - Applies to: reproducibility context in `2606.15682-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Janghwan Lee
  - arXiv author search: https://arxiv.org/search/?query=Janghwan%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Author: Sihwa Lee
  - arXiv author search: https://arxiv.org/search/?query=Sihwa%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Author: Jinseok Kim
  - arXiv author search: https://arxiv.org/search/?query=Jinseok%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Author: Yongjik Kim
  - arXiv author search: https://arxiv.org/search/?query=Yongjik%20Kim&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Author: Jieun Lim
  - arXiv author search: https://arxiv.org/search/?query=Jieun%20Lim&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Author: Jinwook Oh
  - arXiv author search: https://arxiv.org/search/?query=Jinwook%20Oh&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Author: Jungwook Choi
  - arXiv author search: https://arxiv.org/search/?query=Jungwook%20Choi&searchtype=author
  - Applies to: the reviewed paper and `2606.15682-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
