# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P53`
- Public-safe date: 2026-08-19
- Paper: *The performance of the amplitude-based model for complex phase retrieval*
- Identifier: `arXiv:2204.05492`; DOI: `10.48550/arXiv.2204.05492`
- URL: https://arxiv.org/abs/2204.05492

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 45,625 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: model, retrieval.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `The-performance-of-the-amplitude-based-model` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 5; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 351,755 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 34; sampled text inspection: true.
- Full-paper HTML: 1,000,787 bytes, 148,743 body characters, 74 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-The-performance-of-the-amplitude-based-model-LOG.md`
- `.reports/BL-Arxiv-The-performance-of-the-amplitude-based-model-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-The performance of the/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-The performance of the/the_performance_of_the_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Acoustic Phase Retrieval/acoustic_phase_retrieval_manuscript.md` - Acoustic Phase Retrieval - DEP-E; overlap: phase, retrieval, complex.
2. `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md` - SIM MARL Power - DEP-E; overlap: phase, performance.
3. `.lake-data/DEP-E/DEP-E-20260818-Aerial RIS-Enhanced/aerial_ris_enhanced_manuscript.md` - Aerial RIS-Enhanced - DEP-E; overlap: phase, performance.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
