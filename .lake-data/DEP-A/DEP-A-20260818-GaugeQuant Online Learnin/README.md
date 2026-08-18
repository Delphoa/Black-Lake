# DEP-A-20260818-GaugeQuant Online Learnin

#artificial-intelligence #arXiv #paper-review #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.20757v2, *GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.20757-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.20757-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: In this paper, we propose GaugeQuant: an in-training quantization mechanism that mitigates PTQ’s drawbacks by learning a preferred basis across different boundaries of the LLM architecture during training. ( 2025 ) , which proposes an outlier-safe in-training framework that, like GaugeQuant, targets quantization robustness during training, though via architectural modifications (optimizer and normalization changes) rather than learned rotations. On LLaMA-2 7B, GaugeQuant achieves 5.45 PPL under 4-bit weight quantization, a 51% reduction in quantization-induced degradation compared to the baseline (11.16), approaching the ∼ 6.2 {\sim}6.2 reported by SpinQuant under comparable evaluation conditions.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat GaugeQuant: Online Learning of Quantization-Optimal Bases from LLM Symmetries as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.20757v2
  - Applies to: `2607.20757-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.20757v2
  - Applies to: `2607.20757-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.20757v2
  - Applies to: `2607.20757-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.20757
  - Applies to: `2607.20757-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/MPedraBento/gauge-quant
  - Applies to: reproducibility context in `2607.20757-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Miguel P. Bento
  - arXiv author search: https://arxiv.org/search/?query=Miguel%20P.%20Bento&searchtype=author
  - Applies to: the reviewed paper and `2607.20757-whitepaper-review.md`.
- Author: João F. Seabra
  - arXiv author search: https://arxiv.org/search/?query=Jo%C3%A3o%20F.%20Seabra&searchtype=author
  - Applies to: the reviewed paper and `2607.20757-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
