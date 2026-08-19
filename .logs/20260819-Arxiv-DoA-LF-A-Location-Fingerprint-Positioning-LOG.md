# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P138`
- Public-safe date: 2026-08-19
- Paper: *DoA-LF: A Location Fingerprint Positioning Algorithm with Millimeter-Wave*
- Identifier: `arXiv:2102.13297`; DOI: `10.1109/ACCESS.2017.2753781`
- URL: https://arxiv.org/abs/2102.13297

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 20,329 on draw 5.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `DoA-LF-A-Location-Fingerprint-Positioning` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 4; source-gate exclusions: 0; reselections: 4.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 793,480 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 261,367 bytes, 55,988 body characters, 36 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-DoA-LF-A-Location-Fingerprint-Positioning-LOG.md`
- `.reports/BL-Arxiv-DoA-LF-A-Location-Fingerprint-Positioning-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-DoA-LF A Location/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-DoA-LF A Location/doa_lf_a_location_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260815-Hierarchical Perceptual/hierarchical_perceptual_manuscript.md` - Hierarchical Perceptual - DEP-E; overlap: fingerprint.
2. `.lake-data/DEP-E/DEP-E-20260811-RGB-T Semantic/rgb_t_semantic_manuscript.md` - RGB-T Semantic - DEP-E; overlap: location.
3. `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md` - High-Order Langevin - DEP-E; overlap: algorithm.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
