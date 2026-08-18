# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-BBEE0F31`
- Deployment item ID: `BLAD-2200-20260818-BBEE0F31-P31`
- Public-safe date: 2026-08-18
- Paper: *A Framework for Evaluating Snippet Generation for Dataset Search*
- Identifier: `arXiv:1907.01183`; DOI: `10.48550/arXiv.1907.01183`
- URL: https://arxiv.org/abs/1907.01183

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 24,383 on draw 12.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: search.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `A-Framework-for-Evaluating-Snippet-Generation` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 11; source-gate exclusions: 0; reselections: 11.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 384,706 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 17; sampled text inspection: true.
- Full-paper HTML: 225,551 bytes, 56,870 body characters, 76 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-A-Framework-for-Evaluating-Snippet-Generation-LOG.md`
- `.reports/BL-Arxiv-A-Framework-for-Evaluating-Snippet-Generation-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-A Framework for/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-A Framework for/a_framework_for_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260726-WebUIBench A/webuibench_a_manuscript.md` - WebUIBench A - DEP-E; overlap: evaluating.
2. `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - VideoWeave - DEP-E; overlap: generation, search.
3. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: generation, search.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
