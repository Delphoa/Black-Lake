# DEP-A-20260818-Price Anarchy Disaggregat

#artificial-intelligence #arXiv #paper-review #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.17081v1, *The Price of Anarchy in Disaggregated Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.17081-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.17081-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Dynamo is NVIDIA’s production framework for disaggregated LLM inference. The architecture winning at scale for high-throughput LLM serving is disaggregated inference : physically separating the compute-bound prefill phase (processing the full input prompt) from the memory-bandwidth-bound decode phase (generating output tokens autoregressively) onto distinct GPU pools [ 40 , 27 ] . Inference framework: Dynamo v0.9.0 ( nvcr.io/nvidia/ai-dynamo/vllm-runtime:0.9.0-cuda13 ) Runtime: vLLM backend with PagedAttention [ 20 ] KV transfer: NIXL over UCX/verbs on InfiniBand for the data path; IPoIB (10.0.0.{1,2,3}/24 on ibp14s0 ) used only for the NIXL metadata side channel ( VLLM_NIXL_SIDE_CHANNEL_HOST ), not for KV bulk transfer Coordination: etcd (service discovery), NATS JetStream (event plane) Monitoring: Prometheus + NATS event correlation Controller: Python 3.12, nats-py , scipy FP8 is applied at load time via vLLM’s --quantization fp8 flag, which resolves to FP8-E4M3 weights and activations with dynamic per-tensor activation scaling (no calibration set used).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat The Price of Anarchy in Disaggregated Inference as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.17081v1
  - Applies to: `2606.17081-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.17081v1
  - Applies to: `2606.17081-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.17081v1
  - Applies to: `2606.17081-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.17081
  - Applies to: `2606.17081-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Athos Georgiou
  - arXiv author search: https://arxiv.org/search/?query=Athos%20Georgiou&searchtype=author
  - Applies to: the reviewed paper and `2606.17081-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
