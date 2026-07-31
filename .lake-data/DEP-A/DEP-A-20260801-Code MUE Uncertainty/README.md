# DEP-A-20260801-Code MUE Uncertainty

#artificial-intelligence #software-engineering #uncertainty-estimation #code-generation #semantic-graphs #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.12273v1, *Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.12273-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.12273-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: In this paper, we propose Code-MUE , a purely black-box, execution-based framework for quantifying uncertainty in Code LLMs. Our results demonstrate that Code-MUE achieves a strong negative correlation with functional correctness (Spearman’s ρ \rho up to -0.98), significantly outperforming traditional lexical and embedding-based uncertainty baselines. As illustrated in Figure 2 , Code-MUE performs semantic uncertainty estimation through a three-stage pipeline: Probabilistic Sampling and Test Input Synthesis.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat execution-derived semantic disagreement as a risk sensor rather than a correctness oracle: retain the sampled programs, test inputs, behavioral edges, entropy computation, and observed failures, then calibrate abstention thresholds separately for each task family and model revision.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.12273v1
  - Applies to: `2607.12273-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.12273v1
  - Applies to: `2607.12273-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.12273v1
  - Applies to: `2607.12273-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.12273
  - Applies to: `2607.12273-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/hnurxn/Code-Uncertainty
  - Applies to: reproducibility context in `2607.12273-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Xiaoning Ren
  - arXiv author search: https://arxiv.org/search/?query=Xiaoning%20Ren&searchtype=author
  - Applies to: the reviewed paper and `2607.12273-whitepaper-review.md`.
- Author: Yinxing Xue
  - arXiv author search: https://arxiv.org/search/?query=Yinxing%20Xue&searchtype=author
  - Applies to: the reviewed paper and `2607.12273-whitepaper-review.md`.
- Author: Lei Ma
  - arXiv author search: https://arxiv.org/search/?query=Lei%20Ma&searchtype=author
  - Applies to: the reviewed paper and `2607.12273-whitepaper-review.md`.
- Author: Yuheng Huang
  - arXiv author search: https://arxiv.org/search/?query=Yuheng%20Huang&searchtype=author
  - Applies to: the reviewed paper and `2607.12273-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
