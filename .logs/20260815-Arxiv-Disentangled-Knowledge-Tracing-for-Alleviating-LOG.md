# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260815-A0637DE9`
- Deployment item ID: `BLAD-2200-20260815-A0637DE9-P06`
- Public-safe date: 2026-08-15
- Paper: *Disentangled Knowledge Tracing for Alleviating Cognitive Bias*
- Identifier: `arXiv:2503.02539`; DOI: `10.48550/arXiv.2503.02539`
- URL: https://arxiv.org/abs/2503.02539

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 38,443 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Disentangled-Knowledge-Tracing-for-Alleviating` slug; the 24-hour marker cutoff was 2026-08-14.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,233,203 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 438,527 bytes, 95,962 body characters, 76 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260815-Arxiv-Disentangled-Knowledge-Tracing-for-Alleviating-LOG.md`
- `.reports/BL-Arxiv-Disentangled-Knowledge-Tracing-for-Alleviating-20260815/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260815-Disentangled Knowledge/README.md`
- `.lake-data/DEP-E/DEP-E-20260815-Disentangled Knowledge/disentangled_knowledge_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Alleviating Inconsistency/alleviating_inconsistency_manuscript.md` - Alleviating Inconsistency Review - DEP-E; overlap: alleviating, bias.
2. `.lake-data/DEP-E/DEP-E-20260712-KDFlow LLM Distill/kdflow_llm_distill_manuscript.md` - KDFlow LLM Distill - DEP-E; overlap: knowledge, bias.
3. `.lake-data/DEP-E/DEP-E-20260716-CorrKD Missing Modal/corrkd_missing_modal_manuscript.md` - CorrKD Missing Modal - DEP-E; overlap: knowledge, bias.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
