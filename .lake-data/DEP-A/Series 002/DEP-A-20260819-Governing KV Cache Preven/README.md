# DEP-A-20260819-Governing KV Cache Preven

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.09225v1, *Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.09225-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.09225-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: 2024 ) —cache the key-value (KV) attention states of previously computed token prefixes. Describe the issue below: Abstract 1 Introduction 2.1 KV Cache in Multi-Tenant LLM Serving 2.2 A Taxonomy of Inference Caches 2.3 Threat Model 3.1 PROMPTPEEK: Timing Fingerprint Attack 3.2 EarlyBird: Token Reconstruction via Timing 3.3 InputSnatch: Shared-Partition Enumeration 3.4 Structured Prompts Defeat Block-Size Protection 3.5 Synthesis: Oracles and Goals 4.1 HMAC-Keyed Namespace Isolation 4.2 Boundary Salting: Isolation Without Losing Reuse 4.3 ORIGAMI: Stackelberg Audit Scheduler 4.4 Evolutionary Stability Analysis 5.1 Experimental Setup 5.2 ASR Results 5.3 Ablation Study 5.4 ORIGAMI Audit Scheduler 5.5 Adversarial Load Benchmark 5.6 Evolutionary Stability 5.7 Real TTFT Measurement 5.8 Independent-Stack Replication 5.9 Performance Overhead KV cache timing attacks. 2024 demonstrated the first timing side-channel attack against shared KV caches in LLM serving, showing that vLLM’s prefix cache enables token reconstruction via TTFT timing.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat Governing the KV Cache: Preventing Timing Side-Channel Leakage in Multi-Tenant LLM Inference as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.09225v1
  - Applies to: `2608.09225-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.09225v1
  - Applies to: `2608.09225-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.09225v1
  - Applies to: `2608.09225-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.09225
  - Applies to: `2608.09225-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Author: Tejasvi C. Addagada
  - arXiv author search: https://arxiv.org/search/?query=Tejasvi%20C.%20Addagada&searchtype=author
  - Applies to: the reviewed paper and `2608.09225-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
