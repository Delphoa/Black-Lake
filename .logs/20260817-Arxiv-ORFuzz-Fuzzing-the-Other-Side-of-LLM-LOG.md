# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P05`
- Public-safe date: 2026-08-17
- Paper: *ORFuzz: Fuzzing the "Other Side" of LLM Safety -- Testing Over-Refusal*
- Identifier: `arXiv:2508.11222`; DOI: `10.1109/ASE63991.2025.00156`
- URL: https://arxiv.org/abs/2508.11222

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 61,904 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ORFuzz-Fuzzing-the-Other-Side-of-LLM` slug; the 24-hour marker cutoff was 2026-08-16.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,157,522 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 309,301 bytes, 70,105 body characters, 95 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260817-Arxiv-ORFuzz-Fuzzing-the-Other-Side-of-LLM-LOG.md`
- `.reports/BL-Arxiv-ORFuzz-Fuzzing-the-Other-Side-of-LLM-20260817/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other/README.md`
- `.lake-data/DEP-E/DEP-E-20260817-ORFuzz Fuzzing the Other/orfuzz_fuzzing_the_other_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - KDFlow LLM Distill - DEP-E; overlap: llm, side, other, testing, safety.
2. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: llm, other, testing, safety.
3. `.lake-data/DEP-E/DEP-E-20260715-Document Fraud LLM/document_fraud_llm_manuscript.md` - Document Fraud LLM - DEP-E; overlap: llm, other, safety.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
