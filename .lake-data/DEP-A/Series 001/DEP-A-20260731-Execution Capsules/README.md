# DEP-A-20260731-Execution Capsules

#artificial-intelligence #coding-agents #checkpointing #execution-state #portability #systems

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.20537v1, *Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.20537-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.20537-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: By physical-AI serving we mean low-latency, small-batch (single- or few-stream) interactive inference loops whose outputs drive language, speech, or action in real time—latency-first LLMs (coding agents/assistants), voice/TTS front-ends, and vision-language-action (VLA)/robot policies—typically on one on-device or edge GPU. Unlike process checkpoint/restore [ 2 ] , a capsule is not a full process snapshot but the model-specific graph-bound continuation state needed for the next replay; and unlike shared-prefix mechanisms—Pensieve [ 14 ] caches multi-turn conversation state across requests, Hydragen [ 5 ] and Prompt Cache [ 3 ] reuse shared-prefix attention/KV state—the reused object is not KV-derived prefix state but the closed graph-bound buffer set (recurrent/conv included), and capsules add fork/rollback. Second , because that computation graph runs over a fixed, named buffer set, the complete state needed to continue the next replay at any committed token boundary is exactly that closed, named buffer set; freezing it—the execution-state capsule —is a checkpoint and restore of the graph-bound execution state , turning restore , fork , and rollback of a session into a single copy of that buffer set, and prefix reuse from a.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat execution-state capsules as portable but untrusted state: bind them to code and runtime versions, authenticate contents, validate resumability in an isolated environment, and fall back to replay when compatibility or integrity checks fail.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.20537v1
  - Applies to: `2606.20537-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.20537v1
  - Applies to: `2606.20537-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.20537v1
  - Applies to: `2606.20537-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.20537
  - Applies to: `2606.20537-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Liang Su
  - arXiv author search: https://arxiv.org/search/?query=Liang%20Su&searchtype=author
  - Applies to: the reviewed paper and `2606.20537-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
