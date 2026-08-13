# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P01`
- Public-safe date: 2026-08-03
- Paper: *One-shot neural band selection for spectral recovery*
- Identifier: `arXiv:2305.09236`; DOI: `10.48550/arXiv.2305.09236`
- URL: https://arxiv.org/abs/2305.09236

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 75,793 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `One-shot-neural-band-selection-for-spectral` slug; the 24-hour marker cutoff was 2026-08-02.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,761,171 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 5; sampled text inspection: true.
- Full-paper HTML: 194,076 bytes, 24,999 body characters, 20 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260803-Arxiv-One-shot-neural-band-selection-for-spectral-LOG.md`
- `.reports/BL-Arxiv-One-shot-neural-band-selection-for-spectral-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-One-shot neural band/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-One-shot neural band/one_shot_neural_band_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260724-OE-BevSeg Perception/oe_bevseg_perception_manuscript.md` - OE-BevSeg Perception - DEP-E; overlap: one-shot, band, recovery, selection.
2. `.lake-data/DEP-E/DEP-E-20260719-CAP Rank Sparsity/cap_rank_sparsity_manuscript.md` - CAP Compression - DEP-E; overlap: one-shot, spectral, recovery, selection.
3. `.lake-data/DEP-E/DEP-E-20260717-Residual Gaussian/residual_gaussian_cbct_manuscript.md` - Residual Gaussian CBCT - DEP-E; overlap: band, spectral, neural, selection.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
