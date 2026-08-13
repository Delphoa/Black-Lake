# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260801-A1ED7FC9`
- Deployment item ID: `BLAD-2200-20260801-A1ED7FC9-P06`
- Public-safe date: 2026-08-01
- Paper: *On Mechanism Underlying Algorithmic Collusion*
- Identifier: `arXiv:2409.01147`; DOI: `10.48550/arXiv.2409.01147`
- URL: https://arxiv.org/abs/2409.01147

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 63,706 on draw 1 for this slot.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `On-Mechanism-Underlying-Algorithmic-Collusion` slug; the 24-hour marker cutoff was 2026-07-31.
- Duplicate exclusions: 0; source-gate exclusions: 0; metadata exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,609,660 bytes with valid `%PDF-` header and trailing `%%EOF`; pages: 50; extracted text characters: 102,558.
- Full-paper HTML: 2,657,929 bytes, 258,868 body characters, 94 heading/section markers, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260801-Arxiv-On-Mechanism-Underlying-Algorithmic-Collusion-LOG.md`
- `.reports/BL-Arxiv-On-Mechanism-Underlying-Algorithmic-Collusion-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-On Mechanism Underlying/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-On Mechanism Underlying/on_mechanism_underlying_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/provably_faster_algorithm_manuscript.md` - Provably Faster Algorithms for B - DEP-E; concrete overlap: algorithms, design, learning, mechanism.
2. `.lake-data/DEP-E/DEP-E-20260728-Constrained Bayesian/constrained_bayesian_manuscript.md` - Constrained Bayesian - DEP-E; concrete overlap: algorithms, design, learning, mechanism.
3. `.lake-data/DEP-E/DEP-E-20260723-CausalStock Review/causalstock_review_manuscript.md` - CausalStock Review - DEP-E; concrete overlap: design, learning, mechanism, price.

Only generated Markdown and the required dedup JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
