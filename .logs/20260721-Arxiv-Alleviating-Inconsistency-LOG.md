# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260721-F7EDC854`
- Deployment item ID: `BLAD-2200-20260721-F7EDC854-P01`
- Public-safe date: 2026-07-21
- Paper: *Alleviating the Inconsistency Problem of Applying Graph Neural Network to Fraud Detection*
- Identifier: `arXiv:2005.00625`; DOI: `10.1145/3397271.3401253`
- URL: https://arxiv.org/abs/2005.00625

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,779 PDFs and 75,776 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 42,458 on the first draw.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Alleviating-Inconsistency` slug; the 24-hour marker cutoff was 2026-07-20.
- Duplicate exclusions: 0; source-gate exclusions for this accepted draw: 0; reselections: 0.

## Source Integrity

- Initial state: partial; the archive unit did not contain a verified full-paper HTML document or authoritative author metadata.
- One bounded, unauthenticated arXiv repair preserved the valid PDF, retrieved metadata, and used the approved ar5iv full-paper fallback.
- PDF: 964,626 bytes with a valid `%PDF-` header and trailing `%%EOF`.
- Full-paper HTML: 249,102 bytes, 29,379 body characters, 2 document markers, 33 headings, and 6 paper-structure terms.
- Final state: verified complete. All source and integrity files remain local.

## Public Outputs

- `.logs/20260721-Arxiv-Alleviating-Inconsistency-LOG.md`
- `.reports/BL-Arxiv-Alleviating-Inconsistency-20260721/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260721-Alleviating Inconsistency/README.md`
- `.lake-data/DEP-E/DEP-E-20260721-Alleviating Inconsistency/alleviating_inconsistency_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260709-SANE Embeddings/sane_embeddings_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260713-Dynamical Dictionary/dynamical_dictionary_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260710-Physical Data AI/physical_data_ai_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, personal data, production decisions, and model artifacts were withheld; zero source-document uploads.
