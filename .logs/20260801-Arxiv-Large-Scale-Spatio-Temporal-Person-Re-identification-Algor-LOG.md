# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260801-A1ED7FC9`
- Deployment item ID: `BLAD-2200-20260801-A1ED7FC9-P04`
- Public-safe date: 2026-08-01
- Paper: *Large-Scale Spatio-Temporal Person Re-identification: Algorithms and Benchmark*
- Identifier: `arXiv:2105.15076`; DOI: `10.48550/arXiv.2105.15076`
- URL: https://arxiv.org/abs/2105.15076

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 8,974 on draw 1 for this slot.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Large-Scale-Spatio-Temporal-Person-Re-identification-Algor` slug; the 24-hour marker cutoff was 2026-07-31.
- Duplicate exclusions: 0; source-gate exclusions: 0; metadata exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 3,268,209 bytes with valid `%PDF-` header and trailing `%%EOF`; pages: 14; extracted text characters: 61,624.
- Full-paper HTML: 491,014 bytes, 65,531 body characters, 87 heading/section markers, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260801-Arxiv-Large-Scale-Spatio-Temporal-Person-Re-identification-Algor-LOG.md`
- `.reports/BL-Arxiv-Large-Scale-Spatio-Temporal-Person-Re-identification-20260801/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260801-Large-Scale/README.md`
- `.lake-data/DEP-E/DEP-E-20260801-Large-Scale/large_scale_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260730-SLFE Redundancy Review/slfe_redundancy_manuscript.md` - SLFE Redundancy - DEP-E; concrete overlap: algorithms, benchmark, last.
2. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md` - Smart Coverage Goals - DEP-E; concrete overlap: algorithms, benchmark, last.
3. `.lake-data/DEP-E/DEP-E-20260728-MI-Motion Review/mi_motion_manuscript.md` - MI-Motion - DEP-E; concrete overlap: benchmark, person.

Only generated Markdown and the required dedup JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
