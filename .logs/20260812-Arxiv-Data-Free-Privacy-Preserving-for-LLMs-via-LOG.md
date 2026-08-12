# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260812-9483C5E4`
- Deployment item ID: `BLAD-2200-20260812-9483C5E4-P01`
- Public-safe date: 2026-08-12
- Paper: *Data-Free Privacy-Preserving for LLMs via Model Inversion and Selective Unlearning*
- Identifier: `arXiv:2601.15595`; DOI: `10.48550/arXiv.2601.15595`
- URL: https://arxiv.org/abs/2601.15595

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 28,123 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Data-Free-Privacy-Preserving-for-LLMs-via` slug; the 24-hour marker cutoff was 2026-08-11.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,008,991 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 225,162 bytes, 52,572 body characters, 59 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260812-Arxiv-Data-Free-Privacy-Preserving-for-LLMs-via-LOG.md`
- `.reports/BL-Arxiv-Data-Free-Privacy-Preserving-for-LLMs-via-20260812/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260812-Data-Free/README.md`
- `.lake-data/DEP-E/DEP-E-20260812-Data-Free/data_free_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260802-Separate the Wheat from/separate_the_wheat_from_manuscript.md` - Separate the Wheat from - DEP-E; overlap: unlearning, llms.
2. `.lake-data/DEP-E/DEP-E-20260804-Forget FOLTR/forget_foltr_manuscript.md` - FOLTR Unlearning - DEP-E; overlap: unlearning.
3. `.lake-data/DEP-E/DEP-E-20260809-ECHO Prune to act trace/echo_prune_to_act_trace_manuscript.md` - ECHO Prune to act trace - DEP-E; overlap: selective.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
