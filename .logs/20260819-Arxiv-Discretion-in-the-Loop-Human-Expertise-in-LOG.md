# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P117`
- Public-safe date: 2026-08-19
- Paper: *Discretion in the Loop: Human Expertise in Algorithm-Assisted College Advising*
- Identifier: `arXiv:2505.13325`; DOI: `10.48550/arXiv.2505.13325`
- URL: https://arxiv.org/abs/2505.13325

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 72,402 on draw 6.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: algorithmic research.
- Matched title/abstract terms or phrases: algorithm.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Discretion-in-the-Loop-Human-Expertise-in` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 3; source-gate exclusions: 0; reselections: 5.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,180,444 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 62; sampled text inspection: true.
- Full-paper HTML: 816,580 bytes, 197,537 body characters, 217 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Discretion-in-the-Loop-Human-Expertise-in-LOG.md`
- `.reports/BL-Arxiv-Discretion-in-the-Loop-Human-Expertise-in-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Discretion in the Loop/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Discretion in the Loop/discretion_in_the_loop_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260725-Willmore Loop Groups/willmore_loop_groups_manuscript.md` - Willmore Loop Groups - DEP-E; overlap: loop.
2. `.lake-data/DEP-E/DEP-E-20260730-RLHF-V Towards/rlhf_v_towards_manuscript.md` - RLHF-V Towards - DEP-E; overlap: human, loop.
3. `.lake-data/DEP-E/DEP-E-20260805-AVGCN Trajectory/avgcn_trajectory_manuscript.md` - AVGCN Trajectory - DEP-E; overlap: human, loop.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
