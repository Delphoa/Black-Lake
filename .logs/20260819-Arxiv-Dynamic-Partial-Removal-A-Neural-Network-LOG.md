# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P292`
- Public-safe date: 2026-08-19
- Paper: *Dynamic Partial Removal: A Neural Network Heuristic for Large Neighborhood Search*
- Identifier: `arXiv:2005.09330`; DOI: `10.48550/arXiv.2005.09330`
- URL: https://arxiv.org/abs/2005.09330

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 13,211 on draw 53.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Dynamic-Partial-Removal-A-Neural-Network` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 4; focus exclusions: 48; source-gate exclusions: 0; reselections: 52.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,546,530 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 10; sampled text inspection: true.
- Full-paper HTML: 153,886 bytes, 36,305 body characters, 38 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Dynamic-Partial-Removal-A-Neural-Network-LOG.md`
- `.reports/BL-Arxiv-Dynamic-Partial-Removal-A-Neural-Network-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Dynamic Partial Removal A/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Dynamic Partial Removal A/dynamic_partial_removal_a_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Stacked BNAS Rethinking/stacked_bnas_rethinking_manuscript.md` - Stacked BNAS Rethinking - DEP-E; overlap: neural, network, search.
2. `.lake-data/DEP-E/DEP-E-20260819-M-FasterSeg An Efficient/m_fasterseg_an_efficient_manuscript.md` - M-FasterSeg An Efficient - DEP-E; overlap: neural, network, search.
3. `.lake-data/DEP-E/DEP-E-20260813-Controllable Dynamic/controllable_dynamic_manuscript.md` - Controllable Dynamic - DEP-E; overlap: dynamic, neural.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
