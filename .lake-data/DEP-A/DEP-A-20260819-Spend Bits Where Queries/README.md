# DEP-A-20260819-Spend Bits Where Queries

#artificial-intelligence #arXiv #paper-review #KV-cache #model-compression #attention #evaluation

This DEP-A archives a public-safe, whitepaper-grade review of arXiv:2608.04074v1, *Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms*. The complete PDF and full-paper HTML were verified locally. Source documents, private coverage matrices, cache indexes, validator receipts, and deployment audits remain outside the repository.

## Contents

- `README.md` - classification, deposition context, complete inventory, associations, and source attribution.
- `2608.04074-whitepaper-review.md` - validated full-paper technical reconstruction, experimental and claim audit, independent re-conceptualization, coverage ledger, limitations, and replication agenda.

## Summary of Items

### `README.md`

Defines the archival boundary and gives canonical public provenance without exposing private machine context.

### `2608.04074-whitepaper-review.md`

Reconstructs the paper's mechanism and formal objective, audits the evaluation and reported results, separates paper report from reviewer inference, and records section, table, figure, equation, appendix, disclosure, and reproducibility coverage. Its central technical focus is: Describe the issue below: Abstract 1 Introduction 2.1 Attention and the KV Cache 2.2 Transform coding 2.3 Related work 3.1 Key transform 3.2 Value transform 4 KV cache vector quantization Transform analysis. 6 Conclusion A.1 Conventions A.2 Attention and the cache A.3 Calibration statistics A.4 Transforms, quantization, and grouping A.5 Symbol table A.6 High-level algorithm Bits per element (BPE). KV cache reduction can be achieved by combining several complementary approaches: (i) token eviction, where cached tokens are dropped based on their estimated importance to future attention ( 55 ; 26 ; 49 ; 10 ) ; (ii) low-rank designs, which shrink the head dimension ( 30 ) ; and (iii) quantization (our approach).

## Insights and Relevance

The paper matters because it makes a consequential state, resource, or integrity decision explicit and testable. The review preserves the reported result while retaining its model, workload, metric, and systems boundaries. The most useful downstream implication is: Treat Spend Bits Where Queries Look: KV Cache Vector Quantization with Attention-Preserving Transforms as an evidence-linked control mechanism: preserve the exact input identity, intermediate decisions, realized resource use, fallback behavior, and downstream outcome; then test the paper's proposed mechanism against matched-budget alternatives and distribution shifts that could falsify the claimed causal account.

## Associated DEP Records

- No same-paper DEP or sufficiently direct repository association was verified.

## Attribution Block

- Canonical arXiv record: https://arxiv.org/abs/2608.04074v1
  - Applies to: `2608.04074-whitepaper-review.md` and this README.
  - Notes: stable canonical identity and reviewed version.
- Canonical PDF: https://arxiv.org/pdf/2608.04074v1
  - Applies to: `2608.04074-whitepaper-review.md`.
  - Notes: the complete source document was verified locally and withheld from this repository.
- Canonical full-paper HTML: https://arxiv.org/html/2608.04074v1
  - Applies to: `2608.04074-whitepaper-review.md`.
  - Notes: the complete full-paper rendering was verified locally and withheld from this repository.
- DOI or canonical resolver: https://doi.org/10.48550/arXiv.2608.04074
  - Applies to: `2608.04074-whitepaper-review.md` and this README.
  - Notes: canonical DOI or arXiv DOI resolver.
- Official code, data, project, or publisher source: https://amir-zsh.github.io/nova-kv
  - Applies to: reproducibility context in `2608.04074-whitepaper-review.md`.
  - Notes: primary-source availability does not establish independent reproduction.
- Official code, data, project, or publisher source: https://github.com/Amir-zsh/nova-kv
  - Applies to: reproducibility context in `2608.04074-whitepaper-review.md`.
  - Notes: primary-source availability does not establish independent reproduction.
- Author: Samuel Fernández-Menduiña
  - arXiv author search: https://arxiv.org/search/?query=Samuel%20Fern%C3%A1ndez-Mendui%C3%B1a&searchtype=author
  - Applies to: the reviewed paper and `2608.04074-whitepaper-review.md`.
- Author: Amir Ziashahabi
  - arXiv author search: https://arxiv.org/search/?query=Amir%20Ziashahabi&searchtype=author
  - Applies to: the reviewed paper and `2608.04074-whitepaper-review.md`.
- Author: Eduardo Pavez
  - arXiv author search: https://arxiv.org/search/?query=Eduardo%20Pavez&searchtype=author
  - Applies to: the reviewed paper and `2608.04074-whitepaper-review.md`.
- Author: Antonio Ortega
  - arXiv author search: https://arxiv.org/search/?query=Antonio%20Ortega&searchtype=author
  - Applies to: the reviewed paper and `2608.04074-whitepaper-review.md`.
- Author: Salman Avestimehr
  - arXiv author search: https://arxiv.org/search/?query=Salman%20Avestimehr&searchtype=author
  - Applies to: the reviewed paper and `2608.04074-whitepaper-review.md`.
- Source boundary: all source documents, private indexes, validators, manifests, and machine context remained local and were not uploaded.
