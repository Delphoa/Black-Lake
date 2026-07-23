# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260723-FCF6DE3F`
- Deployment item ID: `BLAD-2200-20260723-FCF6DE3F-P08`
- Public-safe date: 2026-07-23
- Paper: *Provably Faster Algorithms for Bilevel Optimization via Without-Replacement Sampling*
- Identifier: `arXiv:2411.05868`; DOI: `10.48550/arXiv.2411.05868`
- URL: https://arxiv.org/abs/2411.05868

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,780 PDFs and 75,777 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 8,943 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` records, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Provably-Faster-Algorithms-for-Bilevel` slug; the 24-hour marker cutoff was 2026-07-22.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 7,324,412 bytes with a valid `%PDF-` header and trailing `%%EOF`; page count: 30; sampled text inspection: true.
- Full-paper HTML: 6,752,897 bytes, 544,891 body characters, 92 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260723-Arxiv-Provably-Faster-Algorithms-for-Bilevel-LOG.md`
- `.reports/BL-Arxiv-Provably-Faster-Algorithms-for-Bilevel-20260723/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/README.md`
- `.lake-data/DEP-E/DEP-E-20260723-Provably Faster Algorithm/provably_faster_algorithm_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260715-Joint Sensing MEC/joint_sensing_mec_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md`

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
