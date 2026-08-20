# DEP-A-20260722-PersistentKV Scheduling

#artificial-intelligence #LLM-serving #KV-cache #GPU-kernels #decode-scheduling #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.26666v2, *PersistentKV: Page-Aware Decode Scheduling for Long-Context LLM Serving on Commodity GPUs*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.26666-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.26666-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: PersistentKV executes native block-table decode attention by KV-head group, reuses K/V tiles across grouped-query heads, splits long sequences, and schedules only non-empty row-head-sequence tasks through a compact work queue. A calibrated policy routes each trace to FlashInfer or a PersistentKV mode.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Deploy the scheduler as a continuously validated route table with conservative fallback, per-shape confidence, drift detection, and trace-level goodput/tail-latency receipts; recalibrate only on versioned hardware/software changes.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.26666v2
  - Applies to: `2606.26666-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.26666v2
  - Applies to: `2606.26666-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.26666v2
  - Applies to: `2606.26666-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.26666
  - Applies to: `2606.26666-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Muhammad Ahmed
  - arXiv author search: https://arxiv.org/search/?query=Muhammad%20Ahmed&searchtype=author
  - Applies to: the reviewed paper and `2606.26666-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
