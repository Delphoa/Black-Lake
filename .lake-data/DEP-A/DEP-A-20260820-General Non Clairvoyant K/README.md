# DEP-A-20260820-General Non Clairvoyant K

#artificial-intelligence #arXiv #paper-review #KV-cache #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.09248v1, *General Non-Clairvoyant KV-Cache Scheduling via Regime-Aware Routing*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.09248-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.09248-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: ( 2025 ) initiate the theoretical study of KV-cache scheduling for LLM inference by formulating the scheduling model, proving an Ω ​ ( n ) \Omega(\sqrt{n}) lower bound for deterministic algorithms under adversarial online arrivals, and giving the Memory-Constrained Shortest-First rule which achieves a 9216 9216 -approximation in the offline identical-prompt clairvoyant setting. For every feasible batch KV-cache scheduling instance with arbitrary prompt lengths and arbitrary response lengths, there is a fully non-clairvoyant scheduling algorithm whose makespan is within a constant factor of the optimal clairvoyant makespan: Set Λ = M / 4 \Lambda=M/4 and α = 2 \alpha=2 , and run the routing meta-scheduler Route in Algorithm 4 . For every feasible online-arrival KV-cache scheduling instance with arbitrary prompt lengths, arbitrary response lengths, and arbitrary arrival times, there is an online non-clairvoyant scheduling algorithm whose total completion time is within a constant factor of the optimal clairvoyant total completion time among schedules that process each job only after its arrival: Set Λ = M / 4 \Lambda=M/4 and α = 2 \alpha=2 , and run the online-arrival routing meta-scheduler in Algorithm 9 .

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat General Non-Clairvoyant KV-Cache Scheduling via Regime-Aware Routing as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- [DEP-A-20260812-KVBuffer Serving](../DEP-A-20260812-KVBuffer%20Serving/README.md) - direct decode-time KV-cache serving context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.09248v1
  - Applies to: `2607.09248-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.09248v1
  - Applies to: `2607.09248-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.09248v1
  - Applies to: `2607.09248-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.09248
  - Applies to: `2607.09248-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Author: Yiding Feng
  - arXiv author search: https://arxiv.org/search/?query=Yiding%20Feng&searchtype=author
  - Applies to: the reviewed paper and `2607.09248-whitepaper-review.md`.
- Author: Siyu Liu
  - arXiv author search: https://arxiv.org/search/?query=Siyu%20Liu&searchtype=author
  - Applies to: the reviewed paper and `2607.09248-whitepaper-review.md`.
- Author: Zonghan Yang
  - arXiv author search: https://arxiv.org/search/?query=Zonghan%20Yang&searchtype=author
  - Applies to: the reviewed paper and `2607.09248-whitepaper-review.md`.
- Author: Yuhao Zhang
  - arXiv author search: https://arxiv.org/search/?query=Yuhao%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.09248-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
