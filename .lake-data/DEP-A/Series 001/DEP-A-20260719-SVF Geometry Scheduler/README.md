# DEP-A-20260719-SVF Geometry Scheduler

#artificial-intelligence #LLM-serving #online-scheduling #KV-cache #competitive-analysis #vLLM

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.22327v2, *Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.22327-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.22327-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Smallest Volume First schedules requests by their two-dimensional memory-time volume rather than predicted duration alone; 1-bit SVF replaces an exact length estimate with a short-versus-long signal. The implementation inserts this decision layer into vLLM without changing the model computation.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Augment SVF with an online uncertainty interval for request volume and use robust priority bands: deterministic SVF when bounds are tight, randomized or age-corrected ordering when estimates overlap, and explicit protection for α-heavy requests.

## Associated DEP Records

- [DEP-A-20260716-Metronome Bound the Cache](../DEP-A-20260716-Metronome%20Bound%20the%20Cache/README.md) - direct long-context cache and attention systems context; not the same paper. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.22327v2
  - Applies to: `2606.22327-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.22327v2
  - Applies to: `2606.22327-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.22327v2
  - Applies to: `2606.22327-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.22327
  - Applies to: `2606.22327-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/Li-Beverly-Kong/Geometry-Aware-Online-Scheduling
  - Applies to: reproducibility context in `2606.22327-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://github.com/vllm-project/vllm
  - Applies to: reproducibility context in `2606.22327-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Li Kong
  - arXiv author search: https://arxiv.org/search/?query=Li%20Kong&searchtype=author
  - Applies to: the reviewed paper and `2606.22327-whitepaper-review.md`.
- Author: Qi Qi
  - arXiv author search: https://arxiv.org/search/?query=Qi%20Qi&searchtype=author
  - Applies to: the reviewed paper and `2606.22327-whitepaper-review.md`.
- Author: Yinyu Ye
  - arXiv author search: https://arxiv.org/search/?query=Yinyu%20Ye&searchtype=author
  - Applies to: the reviewed paper and `2606.22327-whitepaper-review.md`.
- Author: Zijie Zhou
  - arXiv author search: https://arxiv.org/search/?query=Zijie%20Zhou&searchtype=author
  - Applies to: the reviewed paper and `2606.22327-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
