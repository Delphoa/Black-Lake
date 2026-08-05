# Black Lake Arxiv DEP Log

- **Public run date:** 2026-08-06
- **Outcome:** Black Lake Arxiv DEP selected and reviewed one eligible arXiv archive paper.
- **Selected paper:** *Learning Natural Language Inference with LSTM* — arXiv:1512.08849v2; Shuohang Wang and Jing Jiang.
- **Sanitized source provenance:** Public arXiv metadata and PDF were inspected; the official full-paper HTML route returned 404, so the approved ar5iv full-paper fallback was repaired and verified in the private archive. Source files, extracted text, caches, and provenance records remain withheld locally.
- **Random selection:** rg --files -g "*.pdf" enumerated 75,960 PDF candidates and 75,957 unique parent-directory paper units. Uniform PowerShell Get-Random selected zero-based unit index 55,698 on the first draw.
- **Eligibility and deduplication:** Scanned .logs, .reports, .lake-data, .staging, automation memory, and live Black-Lake-Data search results for arXiv ID, title, DOI, and slug markers. The 24-hour cutoff was 2026-08-05. Excluded papers: 0. Duplicate re-selections: 0.
- **Source-integrity gate:** Repaired from partial to complete. The preserved PDF is valid; full-paper HTML passed the size, body, document-marker, heading, and structure checks. The source package was unavailable. No source files were uploaded.
- **Related DEP entries:** CFE2 Search Explain (.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/); Token Cooccurrence RAG (.lake-data/DEP-A/DEP-A-20260715-Token Cooccurrence RAG/); CompressKV Semantic Heads (.lake-data/DEP-A/DEP-A-20260714-CompressKV Semantic Heads/).
- **Outputs:** .reports/BL-Arxiv-NLI-mLSTM-20260806/Report-Mark.md; .lake-data/DEP-E/DEP-E-20260806-NLI mLSTM/README.md; .lake-data/DEP-E/DEP-E-20260806-NLI mLSTM/mlstm_nli_manuscript.md; .lake-data/DEP-E/.index/pubs-index.md.
- **Validation notes:** Manuscript schema headings, title identity, exact-three exercise paths, Report-Mark exact-three synthesis lists, DEP inventory, public-safety scan, source-file allowlist, and staged sanitization gate were required for submission. Source files were not staged.

## Questions for the Next Reviewer

1. Does mLSTM still improve when evaluated on cross-domain NLI rather than SNLI?
2. Which error types are reduced by the match-state gates under calibrated thresholds?
3. Can a modern implementation reproduce the reported 86.1% result with pinned data and preprocessing?

## Challenges for the Next Review Pass

1. Modernize the Torch7 implementation without changing the paper’s data and comparison protocol.
2. Separate useful mismatch memory from dataset-specific annotation or lexical shortcuts.
3. Compare match-state retention with current cross-attention and reranking baselines under equal compute.
