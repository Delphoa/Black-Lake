# DEP-E-20260720-CFE2 Search Explain

`#information-retrieval` `#counterfactual-explanation` `#explainable-ai` `#query-reformulation` `#dense-retrieval` `#human-evaluation` `#research`

- **DEP class:** DEP-E research deposit
- **Deposit date:** 2026-07-20; exact execution timestamp withheld
- **Primary subject:** *CFE2: Counterfactual Editing for Search Result Explanation*
- **Identifiers:** arXiv `2301.10389v3`; https://doi.org/10.48550/arXiv.2301.10389; https://doi.org/10.1145/3664190.3672508
- **Context:** a source-first review of counterfactual query editing as a testable local search-ranking probe, with explicit limits on causal and global-faithfulness claims
- **Source handling:** the complete PDF, full-paper HTML, metadata HTML, source package, extracted evidence, and integrity records remain in the private archive. This public deposit contains derived Markdown only and has no `.source/` directory.

## Contents

| Item | Type | Description |
|---|---|---|
| `README.md` | DEP inventory | Public-safe context, contents, synthesis summary, and source-level attribution |
| `cfe2_search_explanation_manuscript.md` | Research manuscript | Schema-complete source review, evidence ledger, limitations, implementation analysis, exercise paths, and MVP specification |

## Summary of Items

The manuscript examines CFE2, a system that edits a query until a lower-ranked document overtakes a higher-ranked document. The paper combines a dense search model, a token-importance masker, a masked-language-model editor, beam search, and explicit pairwise flip verification. It reports `0.998-1.000` FlipRate across five datasets, generally strong semantic-closeness measures, and sub-second per-edit runtimes in its principal table.

The deposit also records the boundaries of that evidence. Several baselines already approach the FlipRate ceiling; the human study covers 50 SciFact triplets and reports only slight-to-fair agreement; experiments use one search model; and a successful boundary flip is not proof of the causal reason for the original ranking. The manuscript preserves an apparent source-table error, `CosSim 9.959`, without guessing a correction.

Source integrity was repaired before review: the pre-existing PDF passed validation, official full-paper HTML was missing, and a bounded repair added a verified official HTML representation plus provenance companions to the private archive. The final private gate confirmed a 1,014,492-byte PDF with valid opening and closing markers and 551,159-byte full-paper HTML with 98,103 body characters, a document marker, 47 headings, and seven paper-structure terms. No fallback was needed and no source file was uploaded.

## Insights and Relevance

- CFE2 is best presented as a **verified local counterfactual probe**: the edit and the rank reversal can be recomputed against a recorded model and index.
- The probe should not be labeled as a causal account of why the model ranked the documents. Its most defensible scope is one query, one document pair, and one versioned retrieval state.
- Near-ceiling FlipRate shifts evaluation toward semantic preservation, stability, usefulness, latency, safety, and human agreement.
- A production receipt should separate the observed query and documents, derived importance and scores, generated counterfactual, and reviewer judgment.
- Search queries can contain sensitive personal information. Safe deployment requires minimization, redaction, retention controls, policy filtering, and no raw-query logging by default.
- Three verified Black Lake entries anchor the synthesis: Beyond XAI constrains faithfulness language, OViP Preference motivates semantic-isolation and shortcut checks, and REAL Temporal Graph motivates explicit provenance for observed, derived, and counterfactual states.

## Attribution Block

- Xu, Zhichao; Lamba, Hemank; Ai, Qingyao; Tetreault, Joel; Jaimes, Alex. *CFE2: Counterfactual Editing for Search Result Explanation*. arXiv `2301.10389v3`, ICTIR 2024. Metadata: https://arxiv.org/abs/2301.10389. PDF: https://arxiv.org/pdf/2301.10389. Full-paper HTML: https://arxiv.org/html/2301.10389. Source endpoint: https://arxiv.org/e-print/2301.10389. arXiv DOI: https://doi.org/10.48550/arXiv.2301.10389. Published DOI: https://doi.org/10.1145/3664190.3672508.
- OpenReview public record: https://openreview.net/forum?id=G3a15oOyJQ&noteId=86yHStWtLa.
- ICTIR 2024 accepted-paper record: https://www.ictir2024.org/program/accepted-papers.
- University of Utah NLP publication record: https://nlp.cs.utah.edu/publications/.
- Related DEP, *Beyond XAI*: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260716-Beyond%20XAI/beyond_xai_manuscript.md. Its primary source is arXiv `2602.24176`.
- Related DEP, *OViP Preference*: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-E/DEP-E-20260714-OViP%20Preference/ovip_preference_manuscript.md. Its primary source is arXiv `2505.15963`.
- Related DEP, *REAL Temporal Graph*: https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/DEP-A/DEP-A-20260717-REAL%20Temporal%20Graph/2606.10694-whitepaper-review.md. Its primary source is arXiv `2606.10694`.
- Repository authority consulted: https://github.com/Delphoa/Black-Lake/blob/main/README.md and https://github.com/Delphoa/Black-Lake/blob/main/.lake-data/README.md.
- Related repository authority consulted: https://github.com/Delphoa-Labs/Black-Lake-Data/blob/main/README.md.
- Private source-integrity, repair, verification, and provenance records: paths withheld; processing evidence only; no original source file was uploaded.
