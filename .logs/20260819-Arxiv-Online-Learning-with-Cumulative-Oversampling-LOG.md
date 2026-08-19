# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-9951C2C3`
- Deployment item ID: `BLAD-2200-20260819-9951C2C3-P132`
- Public-safe date: 2026-08-19
- Paper: *Online Learning with Cumulative Oversampling: Application to Budgeted Influence Maximization*
- Identifier: `arXiv:2004.11963`; DOI: `10.48550/arXiv.2004.11963`
- URL: https://arxiv.org/abs/2004.11963

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 20,203 on draw 5.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: online learning.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Online-Learning-with-Cumulative-Oversampling` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 4; source-gate exclusions: 0; reselections: 4.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 708,321 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 20; sampled text inspection: true.
- Full-paper HTML: 904,439 bytes, 136,421 body characters, 86 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Online-Learning-with-Cumulative-Oversampling-LOG.md`
- `.reports/BL-Arxiv-Online-Learning-with-Cumulative-Oversampling-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Online Learning with/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Online Learning with/online_learning_with_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260711-CausalTAD Trajectory/causaltad_trajectory_manuscript.md` - CausalTAD Trajectory - DEP-E; overlap: online, influence.
2. `.lake-data/DEP-E/DEP-E-20260812-Multi-Step Alignment as/multi_step_alignment_as_manuscript.md` - Multi-Step Alignment as - DEP-E; overlap: online, influence.
3. `.lake-data/DEP-E/DEP-E-20260813-Adapt as You Say Online/adapt_as_you_say_online_manuscript.md` - Adapt as You Say Online - DEP-E; overlap: online, influence.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
