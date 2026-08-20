# DEP-A-20260802-moBERTo Portuguese

#artificial-intelligence #Portuguese #encoder-models #continued-pretraining #long-context #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2606.22722v1, *moBERTo: A Modern Encoder for Portuguese via Continued Pretraining of ModernBERT*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2606.22722-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2606.22722-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records complete section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Continued pretraining on Portuguese yields average gains for all moBERTo variants over ModernBERT-base, but the benefit is not uniform across architectures: NeoBERT-PT shows only a marginal improvement over NeoBERT-base, and Qwen3-0.6B-PT, while improving on average, degrades on Robust04-PT relative to Qwen3-0.6B-base. As expected, continued pretraining on Portuguese degrades English performance: ModernBERT-base leads on GLUE (0.8301), while all moBERTo variants drop, with the SWM variants showing the largest decrease due to the new tokenizer. We introduce moBERTo, a Portuguese adaptation of ModernBERT obtained through continued pretraining of the ModernBERT-base checkpoint on 60 billion tokens (5 epochs over a 12-billion-token corpus curated from FineWeb2 and filtered with educational and STEM classifiers).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. For Black Lake, the most useful downstream implication is: Maintain a language-adapted encoder as a documented model lineage: bind corpus filters, tokenizer transfer, continued-pretraining checkpoints, long-context post-training, and task heads, while monitoring whether token-level gains trade off against retrieval or regional-language coverage.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2606.22722v1
  - Applies to: `2606.22722-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2606.22722v1
  - Applies to: `2606.22722-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2606.22722v1
  - Applies to: `2606.22722-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI: https://doi.org/10.48550/arXiv.2606.22722
  - Applies to: `2606.22722-whitepaper-review.md` and this README.
  - Notes: canonical arXiv DOI resolver.
- Official code, data, or project source: https://huggingface.co/Tropic-AI/moBERTo
  - Applies to: reproducibility context in `2606.22722-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Official code, data, or project source: https://huggingface.co/datasets/Tropic-AI/moberto-pretraining-dataset-c4-compatible
  - Applies to: reproducibility context in `2606.22722-whitepaper-review.md`.
  - Notes: author-linked primary source; availability does not establish independent reproduction.
- Author: Thiago Laitz
  - arXiv author search: https://arxiv.org/search/?query=Thiago%20Laitz&searchtype=author
  - Applies to: the reviewed paper and `2606.22722-whitepaper-review.md`.
- Author: Thales Sales Almeida
  - arXiv author search: https://arxiv.org/search/?query=Thales%20Sales%20Almeida&searchtype=author
  - Applies to: the reviewed paper and `2606.22722-whitepaper-review.md`.
- Author: João Guilherme Alves Santos
  - arXiv author search: https://arxiv.org/search/?query=Jo%C3%A3o%20Guilherme%20Alves%20Santos&searchtype=author
  - Applies to: the reviewed paper and `2606.22722-whitepaper-review.md`.
- Author: Giovana Kerche Bonás
  - arXiv author search: https://arxiv.org/search/?query=Giovana%20Kerche%20Bon%C3%A1s&searchtype=author
  - Applies to: the reviewed paper and `2606.22722-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
