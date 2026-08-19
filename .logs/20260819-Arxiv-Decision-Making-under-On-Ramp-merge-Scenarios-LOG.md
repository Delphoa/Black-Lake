# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P06`
- Public-safe date: 2026-08-19
- Paper: *Decision-Making under On-Ramp merge Scenarios by Distributional Soft Actor-Critic Algorithm*
- Identifier: `arXiv:2103.04535`; DOI: `10.48550/arXiv.2103.04535`
- URL: https://arxiv.org/abs/2103.04535

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 13,751 on draw 13.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Decision-Making-under-On-Ramp-merge-Scenarios` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 1; focus exclusions: 11; source-gate exclusions: 0; reselections: 12.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,154,062 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 13; sampled text inspection: true.
- Full-paper HTML: 223,231 bytes, 49,429 body characters, 47 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Decision-Making-under-On-Ramp-merge-Scenarios-LOG.md`
- `.reports/BL-Arxiv-Decision-Making-under-On-Ramp-merge-Scenarios-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Decision-Making under/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Decision-Making under/decision_making_under_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-OpenHalDet A Unified/openhaldet_a_unified_manuscript.md` - OpenHalDet A Unified - DEP-E; overlap: scenarios, under.
2. `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md` - High-Order Langevin - DEP-E; overlap: algorithm, under.
3. `.lake-data/DEP-E/DEP-E-20260804-A GNSS Aided Initial/a_gnss_aided_initial_manuscript.md` - A GNSS Aided Initial - DEP-E; overlap: algorithm, under.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
