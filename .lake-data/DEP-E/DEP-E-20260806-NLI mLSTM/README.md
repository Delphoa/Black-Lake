# DEP-E-20260806-NLI mLSTM

#nlp #natural-language-inference #match-lstm #lstm #attention #semantic-matching #snli #research

- **DEP class:** DEP-E research deposit
- **Public deposition date:** 2026-08-06; exact execution timestamp withheld
- **Primary subject:** *Learning Natural Language Inference with LSTM* by Shuohang Wang and Jing Jiang
- **Identifier:** arXiv:1512.08849v2; https://doi.org/10.48550/arXiv.1512.08849
- **Source handling:** The complete PDF and full-paper HTML were verified in the private archive. The official HTML route returned 404 and the approved ar5iv fallback was used. Source files, extracted text, caches, and private provenance records remain local and are not included here.

## Contents

- README.md — public-safe DEP inventory, context, insights, and attribution.
- mlstm_nli_manuscript.md — schema-complete source-grounded manuscript with evidence ledger, paper review, implementation translation, and synthesis with three related DEP entries.

## Summary of Items

### README.md

This file identifies the DEP class and research subject, inventories the two public files, explains source withholding and integrity status, and preserves the public source locators needed to review the deposit.

### mlstm_nli_manuscript.md

The manuscript reconstructs the mLSTM problem, attention and gated match-state mechanism, SNLI experiment design, reported accuracy and gate analyses, implementation constraints, limitations, safe exercise paths, and a bounded MVP concept. It also connects mLSTM to CFE2 Search Explain, Token Cooccurrence RAG, and CompressKV Semantic Heads.

## Insights and Relevance

The deposit preserves a useful mechanism for evidence-sensitive sequence matching: local alignments are scored in context, important mismatches can persist, and the final decision is made from a compact state. The synthesis connects that mechanism to counterfactual ranking probes, proposal-corrector retrieval, and attention-guided memory retention. The .logs/20260806-Arxiv-NLI-mLSTM-LOG.md file records the operational selection and validation trail, while .reports/BL-Arxiv-NLI-mLSTM-20260806/Report-Mark.md contains the detailed review and exactly three implementation mock-ups. The source files were withheld locally, so downstream users should treat the public manuscript as a traceable research artifact rather than a reproduction bundle.

## Attribution Block

- Source URL: https://arxiv.org/abs/1512.08849
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Canonical paper identity, authors, abstract, version history, and arXiv-issued DOI.
- Source URL: https://arxiv.org/pdf/1512.08849
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Primary PDF inspected locally; source file withheld and not uploaded.
- Source URL: https://ar5iv.labs.arxiv.org/html/1512.08849
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Full-paper HTML fallback inspected locally after the official HTML route returned 404; source file withheld.
- Source URL: https://github.com/shuohangwang/SeqMatchSeq
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Official author implementation README used to verify code availability and historical dependencies.
- Source URL: https://nlp.stanford.edu/projects/snli/
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Official SNLI benchmark and license context.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E-20260720-CFE2%20Search%20Explain/cfe2_search_explanation_manuscript.md
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Related DEP used for counterfactual ranking and token-importance synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260715-Token%20Cooccurrence%20RAG/2606.30093-whitepaper-review.md
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Related DEP used for proposal-corrector retrieval and provenance synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A-20260714-CompressKV%20Semantic%20Heads/2606.24467-whitepaper-review.md
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Related DEP used for attention-selected evidence retention and memory-budget synthesis.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/README.md
  - Applies to: README.md and mlstm_nli_manuscript.md
  - Notes: Live repository authority consulted before writing.
- Source URL: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md
  - Applies to: README.md and mlstm_nli_manuscript.md
  - Notes: Live DEP filing and public-source rules consulted before writing.
- Source files: private local archive unit, PDF/full-paper HTML/metadata/verification records
  - Applies to: mlstm_nli_manuscript.md
  - Notes: Source files were inspected for integrity and review, remain local, and were not uploaded.
