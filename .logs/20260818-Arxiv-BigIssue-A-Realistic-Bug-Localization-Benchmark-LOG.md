# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260818-50A35360`
- Deployment item ID: `BLAD-2200-20260818-50A35360-P05`
- Public-safe date: 2026-08-18
- Paper: *BigIssue: A Realistic Bug Localization Benchmark*
- Identifier: `arXiv:2207.10739`; DOI: `10.48550/arXiv.2207.10739`
- URL: https://arxiv.org/abs/2207.10739

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 15,679 on draw 2.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `BigIssue-A-Realistic-Bug-Localization-Benchmark` slug; the 24-hour marker cutoff was 2026-08-17.
- Duplicate exclusions: 0; source-gate exclusions: 1; reselections: 1.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 322,142 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 340,416 bytes, 78,790 body characters, 78 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260818-Arxiv-BigIssue-A-Realistic-Bug-Localization-Benchmark-LOG.md`
- `.reports/BL-Arxiv-BigIssue-A-Realistic-Bug-Localization-Benchmark-20260818/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260818-BigIssue A Realistic Bug/README.md`
- `.lake-data/DEP-E/DEP-E-20260818-BigIssue A Realistic Bug/bigissue_a_realistic_bug_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260710-BEAGLE Learner/beagle_learner_manuscript.md` - BEAGLE Learner - DEP-E; overlap: realistic, benchmark.
2. `.lake-data/DEP-E/DEP-E-20260723-InterDance Reactive 3D Da/interdance_reactive_3d_da_manuscript.md` - InterDance Reactive 3D Dance Gen - DEP-E; overlap: realistic.
3. `.lake-data/DEP-E/DEP-E-20260716-UAV Visual Localization/uav_visual_localization_manuscript.md` - UAV Visual Localization - DEP-E; overlap: localization, benchmark.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
