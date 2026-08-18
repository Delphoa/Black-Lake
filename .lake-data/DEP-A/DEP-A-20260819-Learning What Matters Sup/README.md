# DEP-A-20260819-Learning What Matters Sup

#artificial-intelligence #arXiv #paper-review #attention #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.21692v1, *Learning What Matters: Supervising Sparse Attention Routing with Causal Evidence Sets*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.21692-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.21692-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: The result of Section 5 holds across three model families and three orders of magnitude of teacher scale: supervision copied from attention inherits these stale-evidence failures, and supervision from causal evidence sets avoids them in these tests. Causal evidence sets, recovered by the same interventions, agree across seeds far more than attention does (Jaccard 0.79 to 0.90, against 0.38 to 0.46 for size-matched attention sets). Describe the issue below: Abstract 1 Introduction 2.1 Tasks 2.2 Teachers, interventions, and sanity checks 2.3 Labels 3 Attention includes evidence that does not matter 4 Causal evidence sets are stable 5 Causal supervision improves routing 6 The labels can be recovered without annotations 7 The measurements transfer to frozen pretrained models 8 Limits of sparse routing 9 Related work 10 Limitations 11 Conclusion References A Reproduction B Task and protocol details C Hyperparameters D Minimality of behaviorally sufficient sets E Recovery estimator ablation F Budget curves G Per-seed results H Operator robustness and record-count scaling Every example is a sequence of n n blocks of w w tokens followed by a short query, with n = 32 n{=}32 and w = 8 w{=}8 unless stated.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Learning What Matters: Supervising Sparse Attention Routing with Causal Evidence Sets as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.21692v1
  - Applies to: `2607.21692-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.21692v1
  - Applies to: `2607.21692-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.21692v1
  - Applies to: `2607.21692-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.21692
  - Applies to: `2607.21692-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Jim Allchin
  - arXiv author search: https://arxiv.org/search/?query=Jim%20Allchin&searchtype=author
  - Applies to: the reviewed paper and `2607.21692-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
