# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P347`
- Public-safe date: 2026-08-19
- Paper: *FARM: Frequency-Aware Model for Cross-Domain Live-Streaming Recommendation*
- Identifier: `arXiv:2502.09375`; DOI: `10.48550/arXiv.2502.09375`
- URL: https://arxiv.org/abs/2502.09375

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 57,612 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: model, streaming.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `FARM-Frequency-Aware-Model-for-Cross-Domain` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 3; focus exclusions: 4; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,920,109 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 9; sampled text inspection: true.
- Full-paper HTML: 297,671 bytes, 63,650 body characters, 59 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-FARM-Frequency-Aware-Model-for-Cross-Domain-LOG.md`
- `.reports/BL-Arxiv-FARM-Frequency-Aware-Model-for-Cross-Domain-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-FARM Frequency-Aware/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-FARM Frequency-Aware/farm_frequency_aware_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-MiNet CTR Transfer/minet_ctr_manuscript.md` - Mixed-Interest CTR Transfer; overlap: cross-domain.
2. `.lake-data/DEP-E/DEP-E-20260801-CrossNER Adapt/crossner_domain_adaptation_manuscript.md` - CrossNER - DEP-E; overlap: cross-domain.
3. `.lake-data/DEP-E/DEP-E-20260818-AcroFOD An Adaptive/acrofod_an_adaptive_manuscript.md` - AcroFOD An Adaptive - DEP-E; overlap: cross-domain.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
