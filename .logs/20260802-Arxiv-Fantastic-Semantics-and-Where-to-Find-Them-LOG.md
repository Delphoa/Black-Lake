# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260802-0D11B2FA`
- Deployment item ID: `BLAD-2200-20260802-0D11B2FA-P08`
- Public-safe date: 2026-08-02
- Paper: *Fantastic Semantics and Where to Find Them: Investigating Which Layers of Generative LLMs Reflect Lexical Semantics*
- Identifier: `arXiv:2403.01509`; DOI: `10.48550/arXiv.2403.01509`
- URL: https://arxiv.org/abs/2403.01509

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 34,789 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Fantastic-Semantics-and-Where-to-Find-Them` slug; the 24-hour marker cutoff was 2026-08-01.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 329,646 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 8; sampled text inspection: true.
- Full-paper HTML: 106,014 bytes, 32,793 body characters, 49 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260802-Arxiv-Fantastic-Semantics-and-Where-to-Find-Them-LOG.md`
- `.reports/BL-Arxiv-Fantastic-Semantics-and-Where-to-Find-Them-20260802/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260802-Fantastic Semantics and/README.md`
- `.lake-data/DEP-E/DEP-E-20260802-Fantastic Semantics and/fantastic_semantics_and_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/cfe2_search_explanation_manuscript.md` - CFE2 Search Explanations - DEP-E; overlap: investigating, find, lexical, them.
2. `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` - VLM Probing - DEP-E; overlap: lexical, reflect, generative, layers, them.
3. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - Document Fraud LLM - DEP-E; overlap: reflect, llms, layers, semantics, them.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
