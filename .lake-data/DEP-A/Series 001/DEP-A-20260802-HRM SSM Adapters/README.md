# DEP-A-20260802-HRM SSM Adapters

#artificial-intelligence #state-space-models #adapters #long-context #parameter-efficient-tuning #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.26290v1, *SSM Adapters via Hankel Reduced-order Modeling: Injection Site Determines Task Suitability in Long-Context Fine-Tuning*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.26290-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.26290-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: HRM is the first method that adds SSM-style temporal memory in the PEFT setting; therefore, the backbone is frozen, the adapter has ∼ 0.1 % \sim 0.1\% parameters, and no pre-training data beyond the fine-tuning task is required. MLP injection site, and more importantly, finding out task signatures suitable for each injection site for the adapter, and examine if simultaneous injection would benefit retrieval + integration tasks. We examine if PEFT for such tasks can benefit from state space model (SSMs) adapters, and if MLP blocks are better injection sites.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Deploy recurrent adapters as injection-site-specific state modules: version the Hankel construction, retained order, gates, and placement, compare against iso-parameter static adapters, and fall back to LoRA when recurrence adds instability or no task-relevant state accumulation.

## Associated DEP Records

- [DEP-A-20260731-Spectral Adapter Intake](../DEP-A-20260731-Spectral%20Adapter%20Intake/README.md) - direct adapter architecture and spectral state-compression context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.26290v1
  - Applies to: `2606.26290-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.26290v1
  - Applies to: `2606.26290-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.26290v1
  - Applies to: `2606.26290-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.26290
  - Applies to: `2606.26290-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://openreview.net/forum?id=rGFtmR5Udg
  - Applies to: reproducibility context in `2606.26290-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Omanshu Thapliyal
  - arXiv author search: https://arxiv.org/search/?query=Omanshu%20Thapliyal&searchtype=author
  - Applies to: the reviewed paper and `2606.26290-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
