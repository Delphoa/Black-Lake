# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260815-A0637DE9`
- Deployment item ID: `BLAD-2200-20260815-A0637DE9-P08`
- Public-safe date: 2026-08-15
- Paper: *Rethinking Residual Distribution in Locate-then-Edit Model Editing*
- Identifier: `arXiv:2502.03748`; DOI: `10.48550/arXiv.2502.03748`
- URL: https://arxiv.org/abs/2502.03748

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 28,052 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Rethinking-Residual-Distribution-in-Locate-then` slug; the 24-hour marker cutoff was 2026-08-14.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,342,179 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 27; sampled text inspection: true.
- Full-paper HTML: 686,866 bytes, 99,351 body characters, 90 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260815-Arxiv-Rethinking-Residual-Distribution-in-Locate-then-LOG.md`
- `.reports/BL-Arxiv-Rethinking-Residual-Distribution-in-Locate-then-20260815/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260815-Rethinking Residual/README.md`
- `.lake-data/DEP-E/DEP-E-20260815-Rethinking Residual/rethinking_residual_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-CFE2 Search Explain/cfe2_search_explanation_manuscript.md` - CFE2 Search Explanations - DEP-E; overlap: editing, distribution.
2. `.lake-data/DEP-E/DEP-E-20260723-Rethinking Facial Express/rethinking_facial_express_manuscript.md` - Rethinking Facial Expression Rec - DEP-E; overlap: rethinking, distribution.
3. `.lake-data/DEP-E/DEP-E-20260729-Decentralized Attention/decentralized_attention_manuscript.md` - Decentralized Attention - DEP-E; overlap: rethinking, distribution.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
