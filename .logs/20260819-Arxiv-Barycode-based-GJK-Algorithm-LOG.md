# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P199`
- Public-safe date: 2026-08-19
- Paper: *Barycode-based GJK Algorithm*
- Identifier: `arXiv:2011.09117`; DOI: `10.48550/arXiv.2011.09117`
- URL: https://arxiv.org/abs/2011.09117

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 7,590 on draw 27.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Barycode-based-GJK-Algorithm` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 4; focus exclusions: 22; source-gate exclusions: 0; reselections: 26.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,085,807 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 8; sampled text inspection: true.
- Full-paper HTML: 286,585 bytes, 54,687 body characters, 30 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Barycode-based-GJK-Algorithm-LOG.md`
- `.reports/BL-Arxiv-Barycode-based-GJK-Algorithm-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Barycode-based GJK/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Barycode-based GJK/barycode_based_gjk_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260801-High-Order Langevin/high_order_langevin_manuscript.md` - High-Order Langevin - DEP-E; overlap: algorithm.
2. `.lake-data/DEP-E/DEP-E-20260804-A GNSS Aided Initial/a_gnss_aided_initial_manuscript.md` - A GNSS Aided Initial - DEP-E; overlap: algorithm.
3. `.lake-data/DEP-E/DEP-E-20260818-A Distributed Clustering/a_distributed_clustering_manuscript.md` - A Distributed Clustering - DEP-E; overlap: algorithm.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
