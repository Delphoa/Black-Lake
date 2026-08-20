# DEP-A-20260812-SPEED KV Visibility

#artificial-intelligence #long-context #KV-cache #prefill #inference-efficiency #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.06105v1, *Shallow Prefill, Deep Decoding: Efficient Long-Context Inference via Layer-Asymmetric KV Visibility*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.06105-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.06105-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We propose Shallow Prefill, dEEp Decode (SPEED), a phase-asymmetric KV-visibility policy that makes prefill tokens shallow while keeping decode tokens deep. Han (2024) Duoattention: efficient long-context llm inference with retrieval and streaming heads . Thus, the stage-aware comparison separates Prefill-side acceleration from Decode-time memory-interface changes: SPEED reduces repeated upper-layer prefill-token attention and active KV memory by removing the long prefill sequence from upper-layer Decode visibility.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat layer-asymmetric KV visibility as a phase-specific retention contract: preserve a small full-depth anchor, log each layer cutoff and realized memory saving, and fall back to full-depth prompt visibility when retrieval or generation quality departs from a calibrated envelope.

## Associated DEP Records

- [DEP-A-20260810-UniPrefill](../DEP-A-20260810-UniPrefill/README.md) - direct sparse long-context prefill and acceleration context. This is direct method context, not a same-paper duplicate.
- [DEP-A-20260810-MomentKV](../DEP-A-20260810-MomentKV/README.md) - direct long-context KV-cache eviction and retention context. This is direct method context, not a same-paper duplicate.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.06105v1
  - Applies to: `2605.06105-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.06105v1
  - Applies to: `2605.06105-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.06105v1
  - Applies to: `2605.06105-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.06105
  - Applies to: `2605.06105-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://zenodo.org/records/20057920
  - Applies to: reproducibility context in `2605.06105-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Jungsuk Oh
  - arXiv author search: https://arxiv.org/search/?query=Jungsuk%20Oh&searchtype=author
  - Applies to: the reviewed paper and `2605.06105-whitepaper-review.md`.
- Author: Hyeseo Jeon
  - arXiv author search: https://arxiv.org/search/?query=Hyeseo%20Jeon&searchtype=author
  - Applies to: the reviewed paper and `2605.06105-whitepaper-review.md`.
- Author: Hyunjune Ji
  - arXiv author search: https://arxiv.org/search/?query=Hyunjune%20Ji&searchtype=author
  - Applies to: the reviewed paper and `2605.06105-whitepaper-review.md`.
- Author: Kyongmin Kong
  - arXiv author search: https://arxiv.org/search/?query=Kyongmin%20Kong&searchtype=author
  - Applies to: the reviewed paper and `2605.06105-whitepaper-review.md`.
- Author: Jay-Yoon Lee
  - arXiv author search: https://arxiv.org/search/?query=Jay-Yoon%20Lee&searchtype=author
  - Applies to: the reviewed paper and `2605.06105-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
