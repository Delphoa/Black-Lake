# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P189`
- Public-safe date: 2026-08-19
- Paper: *Calibrated Dataset Condensation for Faster Hyperparameter Search*
- Identifier: `arXiv:2405.17535`; DOI: `10.48550/arXiv.2405.17535`
- URL: https://arxiv.org/abs/2405.17535

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 71,568 on draw 65.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Calibrated-Dataset-Condensation-for-Faster` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 60; source-gate exclusions: 1; reselections: 64.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 2,649,913 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 37; sampled text inspection: true.
- Full-paper HTML: 777,422 bytes, 144,394 body characters, 99 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Calibrated-Dataset-Condensation-for-Faster-LOG.md`
- `.reports/BL-Arxiv-Calibrated-Dataset-Condensation-for-Faster-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Calibrated Dataset/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Calibrated Dataset/calibrated_dataset_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/provably_faster_algorithm_manuscript.md` - Provably Faster Algorithms for B - DEP-E; overlap: faster, calibrated.
2. `.lake-data/DEP-E/DEP-E-20260816-Train Faster Perform/train_faster_perform_manuscript.md` - Train Faster Perform - DEP-E; overlap: faster, calibrated.
3. `.lake-data/DEP-E/DEP-E-20260818-A Better and Faster/a_better_and_faster_manuscript.md` - A Better and Faster - DEP-E; overlap: faster, calibrated.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
