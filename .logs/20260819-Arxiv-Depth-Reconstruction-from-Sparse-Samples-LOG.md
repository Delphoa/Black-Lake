# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P355`
- Public-safe date: 2026-08-19
- Paper: *Depth Reconstruction from Sparse Samples: Representation, Algorithm, and Sampling*
- Identifier: `arXiv:1407.3840`; DOI: `10.48550/arXiv.1407.3840`
- URL: https://arxiv.org/abs/1407.3840

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 55,489 on draw 76.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Depth-Reconstruction-from-Sparse-Samples` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 13; focus exclusions: 62; source-gate exclusions: 0; reselections: 75.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,493,887 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 19; sampled text inspection: true.
- Full-paper HTML: 511,568 bytes, 87,851 body characters, 89 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Depth-Reconstruction-from-Sparse-Samples-LOG.md`
- `.reports/BL-Arxiv-Depth-Reconstruction-from-Sparse-Samples-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Depth Reconstruction from/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Depth Reconstruction from/depth_reconstruction_from_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260728-FLASH Efficient/flash_efficient_manuscript.md` - FLASH Efficient - DEP-E; overlap: sampling, sparse, representation.
2. `.lake-data/DEP-E/DEP-E-20260730-Sat3R Satellite DSM/sat3r_satellite_dsm_manuscript.md` - Sat3R Satellite DSM - DEP-E; overlap: depth, reconstruction, representation.
3. `.lake-data/DEP-E/DEP-E-20260819-A density peaks/a_density_peaks_manuscript.md` - A density peaks - DEP-E; overlap: sparse, algorithm, representation.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
