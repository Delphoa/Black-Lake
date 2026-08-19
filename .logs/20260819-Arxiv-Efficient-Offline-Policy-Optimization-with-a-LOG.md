# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P32`
- Public-safe date: 2026-08-19
- Paper: *Efficient Offline Policy Optimization with a Learned Model*
- Identifier: `arXiv:2210.05980`; DOI: `10.48550/arXiv.2210.05980`
- URL: https://arxiv.org/abs/2210.05980

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 31,120 on draw 23.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: optimization.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Efficient-Offline-Policy-Optimization-with-a` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 22; source-gate exclusions: 0; reselections: 22.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,382,681 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 22; sampled text inspection: true.
- Full-paper HTML: 450,261 bytes, 119,480 body characters, 85 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Efficient-Offline-Policy-Optimization-with-a-LOG.md`
- `.reports/BL-Arxiv-Efficient-Offline-Policy-Optimization-with-a-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Efficient Offline Policy/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Efficient Offline Policy/efficient_offline_policy_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-A Policy Optimization/a_policy_optimization_manuscript.md` - A Policy Optimization - DEP-E; overlap: optimization, policy, offline.
2. `.lake-data/DEP-E/DEP-E-20260818-Learning adaptive/learning_adaptive_manuscript.md` - Learning adaptive - DEP-E; overlap: optimization, policy, offline.
3. `.lake-data/DEP-E/DEP-E-20260818-RePO Replay-Enhanced/repo_replay_enhanced_manuscript.md` - RePO Replay-Enhanced - DEP-E; overlap: optimization, policy, offline.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
