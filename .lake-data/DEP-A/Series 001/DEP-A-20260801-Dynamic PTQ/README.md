# DEP-A-20260801-Dynamic PTQ

#artificial-intelligence #quantization #post-training-quantization #activation-dynamics #model-compression #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.12487v1, *DynamicPTQ: Mitigating Activation Quantization Collapse via Residual-Stream Dynamics*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.12487-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.12487-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Residual-stream dynamics of DeepSeek-V2-Lite and LLaMA-3-8B under 4-bit activation quantization, measured by Jump Ratio and Historical SNR. Motivated by this observation, we propose DynamicPTQ , a phase-aware mixed-precision quantization strategy that adapts activation precision to the residual-stream dynamics of each phase. We evaluate the phase-wise residual-stream dynamics across dense LLMs of different parameter scales and model families under 4-bit activation-only quantization, using sequences constructed from WikiText-2 (20 samples, sequence length 512) and applying a FlatQuant activation-only quantization pipeline.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Use residual-stream dynamics as a quantization control signal: preserve layerwise activation statistics, selected precision, calibration domain, saturation events, and fallback decisions, and test whether the dynamic rule remains stable across model families and long-tail prompts rather than only averting collapse in calibration settings.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.12487v1
  - Applies to: `2606.12487-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.12487v1
  - Applies to: `2606.12487-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.12487v1
  - Applies to: `2606.12487-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.12487
  - Applies to: `2606.12487-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Zimo Zhao
  - arXiv author search: https://arxiv.org/search/?query=Zimo%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2606.12487-whitepaper-review.md`.
- Author: Maolin Wang
  - arXiv author search: https://arxiv.org/search/?query=Maolin%20Wang&searchtype=author
  - Applies to: the reviewed paper and `2606.12487-whitepaper-review.md`.
- Author: Bowen Yu
  - arXiv author search: https://arxiv.org/search/?query=Bowen%20Yu&searchtype=author
  - Applies to: the reviewed paper and `2606.12487-whitepaper-review.md`.
- Author: Bowen Liu
  - arXiv author search: https://arxiv.org/search/?query=Bowen%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2606.12487-whitepaper-review.md`.
- Author: Xiao Han
  - arXiv author search: https://arxiv.org/search/?query=Xiao%20Han&searchtype=author
  - Applies to: the reviewed paper and `2606.12487-whitepaper-review.md`.
- Author: Xiangyu Zhao
  - arXiv author search: https://arxiv.org/search/?query=Xiangyu%20Zhao&searchtype=author
  - Applies to: the reviewed paper and `2606.12487-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
