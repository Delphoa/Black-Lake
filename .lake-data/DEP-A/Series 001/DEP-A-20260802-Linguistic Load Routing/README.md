# DEP-A-20260802-Linguistic Load Routing

#artificial-intelligence #LLM-serving #workload-prediction #routing #edge-computing #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.04951v1, *When Words Predict Workload*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.04951-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.04951-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: When a patent claim arrives, the gateway executes the following pipeline on a single CPU thread, with a target budget of < 5 ms <$5\text{\,}\mathrm{ms}$ end-to-end: Pre-allocation safety check (Mechanism B § IV-G ) : A closed-form KV-cache size estimate confirms that the projected peak VRAM usage stays under 7.5 GB 7.5\text{\,}\mathrm{GB} . This creates a sudden, unpredictable demand on memory and latency that saturates the consumer-grade edge accelerators (e.g., NVIDIA GeForce GTX 1080), triggers out of memory aborts, stalls the head-of-line queue, and forces a serial fallback to the cloud, where the system pays the full latency penalty of CUDA memory cleanup, state serialization, and remote re-transmission. To close this gap, we present Linguistic Resource Forecasting (LRF) , a sub- 5 ms 5\text{\,}\mathrm{ms} CPU pipeline that predicts hardware escalation probability P escalate P_{\mathrm{escalate}} using a sixteen-dimensional vector of likelihood-orthogonal features.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat When Words Predict Workload as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260802-AgentServeSim](../DEP-A-20260802-AgentServeSim/README.md) - direct LLM-serving workload and systems-evaluation context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.04951v1
  - Applies to: `2607.04951-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.04951v1
  - Applies to: `2607.04951-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.04951v1
  - Applies to: `2607.04951-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.04951
  - Applies to: `2607.04951-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Anubhab Banerjee
  - arXiv author search: https://arxiv.org/search/?query=Anubhab%20Banerjee&searchtype=author
  - Applies to: the reviewed paper and `2607.04951-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
