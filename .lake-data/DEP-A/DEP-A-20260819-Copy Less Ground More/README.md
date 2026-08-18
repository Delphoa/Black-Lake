# DEP-A-20260819-Copy Less Ground More

#artificial-intelligence #arXiv #paper-review #reinforcement-learning #reasoning #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.19345v1, *Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.19345-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.19345-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Describe the issue below: Abstract 1 Introduction 2 Related Work 3.1 Experimental Setup 3.2 Repetitive Copying is Prevalent among LLMs 3.3 Repetitive Copying Harms Task Performance 3.4 Repetitive Copying Reflects Insufficient Grounding 4.1 Reward Design 4.2 Evidence-Annotated Data Construction 4.3 Training Setup 5.1 Main Results 5.2 Effect on Repetitive Copying and Grounding 5.3 Ablation Study 6 Conclusion References A.1 Repetitive Copying across Models A.2 Grounding Ratio across Models A.3.1 Case 1: Frequent Word Extraction (Ruler, 32k) A.3.2 Case 2: Multi-Document Academic QA (LongBench-v2, 32k) A.4 Detailed Results for Section 3.3 Reinforcement learning for reasoning. Our work connects these threads by showing that in long-context settings, the dominant form of excessive reasoning is not aimless elaboration but direct copying from the prompt , and that this behavior is directly linked to insufficient evidence grounding. This reveals a failure mode: without a penalty for distractor copying, the grounding reward incentivizes the model to copy more from all parts of the input, including irrelevant context, resulting in longer and more repetitive reasoning that ultimately hurts task accuracy (Table 1 ).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.19345v1
  - Applies to: `2607.19345-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.19345v1
  - Applies to: `2607.19345-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.19345v1
  - Applies to: `2607.19345-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.19345
  - Applies to: `2607.19345-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Lizhe Fang
  - arXiv author search: https://arxiv.org/search/?query=Lizhe%20Fang&searchtype=author
  - Applies to: the reviewed paper and `2607.19345-whitepaper-review.md`.
- Author: Weizhou Shen
  - arXiv author search: https://arxiv.org/search/?query=Weizhou%20Shen&searchtype=author
  - Applies to: the reviewed paper and `2607.19345-whitepaper-review.md`.
- Author: Tianyi Tang
  - arXiv author search: https://arxiv.org/search/?query=Tianyi%20Tang&searchtype=author
  - Applies to: the reviewed paper and `2607.19345-whitepaper-review.md`.
- Author: Yisen Wang
  - arXiv author search: https://arxiv.org/search/?query=Yisen%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2607.19345-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
