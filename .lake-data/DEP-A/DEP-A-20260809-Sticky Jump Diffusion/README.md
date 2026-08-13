# DEP-A-20260809-Sticky Jump Diffusion

#artificial-intelligence #diffusion-models #jump-processes #masked-generation #hybrid-state-spaces #theory

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2607.10951v1, *Sticky Jump Diffusions: A Unifying View of Masked, Continuous, and Hybrid Diffusion*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2607.10951-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2607.10951-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: We define Sticky Jump Diffusions (SJDs), a class of continuous-time Markov processes on a continuous state space 𝖷 = ℝ d \mathsf{X}=\mathbb{R}^{d} with a finite or countable set of anchors 𝒜 ⊂ ℝ d \mathcal{A}\subset\mathbb{R}^{d} identified with token embeddings. A unifying view of masked, continuous, and hybrid diffusion. Its reversal explains features that each family treats as given: the mask of masked diffusion carries no evidence about the source token because the unsticking kernel of every anchor collapses to the same absorbing point; the terminal projection of continuous diffusion is required due to the absence of atoms in its forward marginal, without which flux balance yields no reverse jumps; and the update rules of hybrid diffusion (commit rate, destination, and drift) all follow from flux balance rather than from separate design.

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Treat Sticky Jump Diffusions: A Unifying View of Masked, Continuous, and Hybrid Diffusion as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2607.10951v1
  - Applies to: `2607.10951-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2607.10951v1
  - Applies to: `2607.10951-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2607.10951v1
  - Applies to: `2607.10951-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2607.10951
  - Applies to: `2607.10951-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://github.com/PascalJD/sticky-jump-diffusions
  - Applies to: reproducibility context in `2607.10951-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Pascal Jutras-Dubé
  - arXiv author search: https://arxiv.org/search/?query=Pascal%20Jutras-Dub%C3%A9&searchtype=author
  - Applies to: the reviewed paper and `2607.10951-whitepaper-review.md`.
- Author: Patrick Pynadath
  - arXiv author search: https://arxiv.org/search/?query=Patrick%20Pynadath&searchtype=author
  - Applies to: the reviewed paper and `2607.10951-whitepaper-review.md`.
- Author: Jeremy Lu
  - arXiv author search: https://arxiv.org/search/?query=Jeremy%20Lu&searchtype=author
  - Applies to: the reviewed paper and `2607.10951-whitepaper-review.md`.
- Author: Yuan Gao
  - arXiv author search: https://arxiv.org/search/?query=Yuan%20Gao&searchtype=author
  - Applies to: the reviewed paper and `2607.10951-whitepaper-review.md`.
- Author: Ruqi Zhang
  - arXiv author search: https://arxiv.org/search/?query=Ruqi%20Zhang&searchtype=author
  - Applies to: the reviewed paper and `2607.10951-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
