# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260817-2C1A830E`
- Deployment item ID: `BLAD-2200-20260817-2C1A830E-P04`
- Public-safe date: 2026-08-17
- Paper: *An Item is Worth a Prompt: Versatile Image Editing with Disentangled Control*
- Identifier: `arXiv:2403.04880`; DOI: `10.48550/arXiv.2403.04880`
- URL: https://arxiv.org/abs/2403.04880

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 1,930 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `An-Item-is-Worth-a-Prompt-Versatile` slug; the 24-hour marker cutoff was 2026-08-16.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 46,276,116 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 131,715 bytes, 44,342 body characters, 50 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260817-Arxiv-An-Item-is-Worth-a-Prompt-Versatile-LOG.md`
- `.reports/BL-Arxiv-An-Item-is-Worth-a-Prompt-Versatile-20260817/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260817-An Item is Worth a Prompt/README.md`
- `.lake-data/DEP-E/DEP-E-20260817-An Item is Worth a Prompt/an_item_is_worth_a_prompt_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260815-Disentangled Knowledge/disentangled_knowledge_manuscript.md` - Disentangled Knowledge - DEP-E; overlap: disentangled, item, control.
2. `.lake-data/DEP-E/DEP-E-20260815-Rethinking Residual/rethinking_residual_manuscript.md` - Rethinking Residual - DEP-E; overlap: editing, item, control.
3. `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/cfe2_search_explanation_manuscript.md` - CFE2 Search Explanations - DEP-E; overlap: editing.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
