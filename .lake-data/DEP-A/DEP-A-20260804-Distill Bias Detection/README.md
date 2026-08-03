# DEP-A-20260804-Distill Bias Detection

#artificial-intelligence #model-auditing #hidden-bias #knowledge-distillation #interpretability #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.01208v1, *Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.01208-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.01208-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Even with no lexical overlap between the injection prompt and the target, the cartridge again surfaces the bias at 100% Petri detection for both biases, while LoRA and full-model distillation stay near the teacher (Table 2 , Appendix C.1 ). The cartridge amplifies Petri detection to 100% for both biases, while LoRA and full-model distillation stay near the teacher baseline. D2D addresses this gap by first amplifying the distributional shift into the model’s generated behavior through cartridge distillation, making it accessible to any existing detection method.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Distill to Detect: Exposing Stealth Biases in LLMs through Cartridge Distillation as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260717-Judge Conformal Intake](../DEP-A-20260717-Judge%20Conformal%20Intake/README.md) - direct LLM-judge calibration and uncertainty context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.01208v1
  - Applies to: `2607.01208-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.01208v1
  - Applies to: `2607.01208-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.01208v1
  - Applies to: `2607.01208-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.01208
  - Applies to: `2607.01208-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://distill2detect.github.io/
  - Applies to: reproducibility context in `2607.01208-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Shayan Talaei
  - arXiv author search: https://arxiv.org/search/?query=Shayan%20Talaei&searchtype=author
  - Applies to: the reviewed paper and `2607.01208-whitepaper-review.md`.
- Author: Abhinav Chinta
  - arXiv author search: https://arxiv.org/search/?query=Abhinav%20Chinta&searchtype=author
  - Applies to: the reviewed paper and `2607.01208-whitepaper-review.md`.
- Author: Devvrit Khatri
  - arXiv author search: https://arxiv.org/search/?query=Devvrit%20Khatri&searchtype=author
  - Applies to: the reviewed paper and `2607.01208-whitepaper-review.md`.
- Author: Amin Karbasi
  - arXiv author search: https://arxiv.org/search/?query=Amin%20Karbasi&searchtype=author
  - Applies to: the reviewed paper and `2607.01208-whitepaper-review.md`.
- Author: Azalia Mirhoseini
  - arXiv author search: https://arxiv.org/search/?query=Azalia%20Mirhoseini&searchtype=author
  - Applies to: the reviewed paper and `2607.01208-whitepaper-review.md`.
- Author: Amin Saberi
  - arXiv author search: https://arxiv.org/search/?query=Amin%20Saberi&searchtype=author
  - Applies to: the reviewed paper and `2607.01208-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
