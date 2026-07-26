# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260726-1DBD5211`
- Deployment item ID: `BLAD-2200-20260726-1DBD5211-P06`
- Public-safe date: 2026-07-26
- Paper: *WebUIBench: A Comprehensive Benchmark for Evaluating Multimodal Large Language Models in WebUI-to-Code*
- Identifier: `arXiv:2506.07818`; DOI: `10.48550/arXiv.2506.07818`
- URL: https://arxiv.org/abs/2506.07818

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,781 PDFs and 75,778 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 28,423 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `WebUIBench-A-Comprehensive-Benchmark-for` slug; the 24-hour marker cutoff was 2026-07-25.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 8,311,372 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 18; sampled text inspection: true.
- Full-paper HTML: 326,727 bytes, 60,588 body characters, 81 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260726-Arxiv-WebUIBench-A-Comprehensive-Benchmark-for-LOG.md`
- `.reports/BL-Arxiv-WebUIBench-A-Comprehensive-Benchmark-for-20260726/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260726-WebUIBench A/README.md`
- `.lake-data/DEP-E/DEP-E-20260726-WebUIBench A/webuibench_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Rethinking Facial Express/rethinking_facial_express_manuscript.md` - Rethinking Facial Expression Rec - DEP-E; overlap: language, multimodal, benchmark.
2. `.lake-data/DEP-E/DEP-E-20260718-Efficient FM Survey/efficient_fm_survey_manuscript.md` - Efficient FM Survey - DEP-E; overlap: language, multimodal.
3. `.lake-data/DEP-E/DEP-E-20260724-OmniSQL Synthesizing/omnisql_synthesizing_manuscript.md` - OmniSQL Synthesizing - DEP-E; overlap: high-quality, text-to-sql.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
