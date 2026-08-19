# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P173`
- Public-safe date: 2026-08-19
- Paper: *TIPCB: A Simple but Effective Part-based Convolutional Baseline for Text-based Person Search*
- Identifier: `arXiv:2105.11628`; DOI: `10.48550/arXiv.2105.11628`
- URL: https://arxiv.org/abs/2105.11628

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 60,045 on draw 8.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `TIPCB-A-Simple-but-Effective-Part-based` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 7; source-gate exclusions: 0; reselections: 7.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 12,600,222 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 27; sampled text inspection: true.
- Full-paper HTML: 160,868 bytes, 52,987 body characters, 41 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-TIPCB-A-Simple-but-Effective-Part-based-LOG.md`
- `.reports/BL-Arxiv-TIPCB-A-Simple-but-Effective-Part-based-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-TIPCB A Simple but/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-TIPCB A Simple but/tipcb_a_simple_but_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Stacked BNAS Rethinking/stacked_bnas_rethinking_manuscript.md` - Stacked BNAS Rethinking - DEP-E; overlap: convolutional, search, simple, baseline, but.
2. `.lake-data/DEP-E/DEP-E-20260801-Large-Scale/large_scale_manuscript.md` - Large-Scale - DEP-E; overlap: person, effective, simple, baseline, but.
3. `.lake-data/DEP-E/DEP-E-20260811-Constrained Deep Metric/constrained_deep_metric_manuscript.md` - Constrained Deep Metric - DEP-E; overlap: person, simple, baseline, but.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
