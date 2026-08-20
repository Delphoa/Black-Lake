# DEP-A-20260727-Memory Experts Diffusion

#artificial-intelligence #world-models #diffusion #long-term-memory #video-generation #planning

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2605.18813v1, *Composition of Memory Experts for Diffusion World Models*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2605.18813-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2605.18813-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Composition of Memory Experts augments a diffusion world model with specialized short-term, long-term episodic, and spatial long-term experts. The short-term expert follows local dynamics, the long-term expert stores past observations through lightweight test-time adaptation, and the spatial expert enforces geometry; their denoising scores are combined through a contrastive product-of-experts designed to suppress inconsistent modes.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Attach uncertainty and conflict diagnostics to each expert score, then adapt composition weights when memories disagree instead of multiplying them blindly. Falsification would be a single memory adapter with equal test-time compute matching the compositional model on recall, planning, and long-rollout consistency.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2605.18813v1
  - Applies to: `2605.18813-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2605.18813v1
  - Applies to: `2605.18813-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2605.18813v1
  - Applies to: `2605.18813-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2605.18813
  - Applies to: `2605.18813-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://openreview.net/forum?id=yDo1ynArjj
  - Applies to: reproducibility context in `2605.18813-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Sebastian Stapf
  - arXiv author search: https://arxiv.org/search/?query=Sebastian%20Stapf&searchtype=author
  - Applies to: the reviewed paper and `2605.18813-whitepaper-review.md`.
- Author: Pablo Acuaviva Huertos
  - arXiv author search: https://arxiv.org/search/?query=Pablo%20Acuaviva%20Huertos&searchtype=author
  - Applies to: the reviewed paper and `2605.18813-whitepaper-review.md`.
- Author: Aram Davtyan
  - arXiv author search: https://arxiv.org/search/?query=Aram%20Davtyan&searchtype=author
  - Applies to: the reviewed paper and `2605.18813-whitepaper-review.md`.
- Author: Paolo Favaro
  - arXiv author search: https://arxiv.org/search/?query=Paolo%20Favaro&searchtype=author
  - Applies to: the reviewed paper and `2605.18813-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
