# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260821-909CA89B`
- Deployment item ID: `BLAD-2200-20260821-909CA89B-P01`
- Public-safe date: 2026-08-21
- Paper: *Is it Still Fair? A Comparative Evaluation of Fairness Algorithms through the Lens of Covariate Drift*
- Identifier: `arXiv:2409.12428`; DOI: `10.48550/arXiv.2409.12428`
- URL: https://arxiv.org/abs/2409.12428

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 38,830 on draw 1.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Is-it-Still-Fair-A-Comparative-Evaluation` slug; the 24-hour marker cutoff was 2026-08-20.
- Duplicate exclusions: 13958; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,860,320 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 195,212 bytes, 55,392 body characters, 61 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260821-Arxiv-Is-it-Still-Fair-A-Comparative-Evaluation-LOG.md`
- `.reports/BL-Arxiv-Is-it-Still-Fair-A-Comparative-Evaluation-20260821/Report-Mark.md`
- `.lake-data/DEP-E/Series 002/DEP-E-20260821-Is it Still Fair A 2428/README.md`
- `.lake-data/DEP-E/Series 002/DEP-E-20260821-Is it Still Fair A 2428/is_it_still_fair_a_2428_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/Series 002/DEP-E-20260820-Spectrum Occupancy/spectrum_occupancy_ml_manuscript.md` - Spectrum ML - DEP-E; overlap: algorithms, machine, synthesize, priority, patterns.
2. `.lake-data/DEP-E/Series 001/DEP-E-20260819-Fast ML Science/fast_ml_science_manuscript.md` - Fast ML Science - DEP-E; overlap: applications, machine, breadth, literature, choice.
3. `.lake-data/DEP-E/Series 001/DEP-E-20260819-Distributional Successor/distributional_successor_manuscript.md` - Distributional Successor - DEP-E; overlap: distributional, policy, cover, show, implications.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
