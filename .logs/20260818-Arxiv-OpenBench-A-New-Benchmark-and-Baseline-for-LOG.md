# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-D85F5742`
- Deployment item ID: `BLAD-2200-20260818-D85F5742-P36`
- Public-safe date: 2026-08-18
- Paper: *OpenBench: A New Benchmark and Baseline for Semantic Navigation in Smart Logistics*
- Identifier: `arXiv:2502.09238`; DOI: `10.48550/arXiv.2502.09238`
- URL: https://arxiv.org/abs/2502.09238

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 12,753 on draw 1.

## Research Focus Eligibility

- One-time focus: No one-time topic focus was requested..
- Matched categories: unrestricted.
- Matched title/abstract terms or phrases: not applicable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `OpenBench-A-New-Benchmark-and-Baseline-for` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; focus exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,213,651 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 7; sampled text inspection: true.
- Full-paper HTML: 128,736 bytes, 38,494 body characters, 76 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-OpenBench-A-New-Benchmark-and-Baseline-for-LOG.md`
- `.reports/BL-Arxiv-OpenBench-A-New-Benchmark-and-Baseline-for-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-OpenBench A New Benchmark/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-OpenBench A New Benchmark/openbench_a_new_benchmark_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; overlap: smart, semantic, benchmark.
2. `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md` - SAGE-Nav Review - DEP-E; overlap: navigation, semantic, benchmark, baseline.
3. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md` - VG Navigable Space Review - DEP-E; overlap: navigation, semantic, benchmark.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
