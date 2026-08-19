# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P130`
- Public-safe date: 2026-08-19
- Paper: *Regret Minimization Experience Replay in Off-Policy Reinforcement Learning*
- Identifier: `arXiv:2105.07253`; DOI: `10.48550/arXiv.2105.07253`
- URL: https://arxiv.org/abs/2105.07253

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 49,139 on draw 14.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: ML memory.
- Matched title/abstract terms or phrases: experience replay.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Regret-Minimization-Experience-Replay-in-Off` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 0; focus exclusions: 13; source-gate exclusions: 0; reselections: 13.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 7,583,505 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 0; sampled text inspection: true.
- Full-paper HTML: 711,408 bytes, 110,432 body characters, 115 headings, and 8 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Regret-Minimization-Experience-Replay-in-Off-LOG.md`
- `.reports/BL-Arxiv-Regret-Minimization-Experience-Replay-in-Off-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Regret Minimization/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Regret Minimization/regret_minimization_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-ARPO End-to-End Policy/arpo_end_to_end_policy_manuscript.md` - ARPO End-to-End Policy - DEP-E; overlap: experience, replay, minimization.
2. `.lake-data/DEP-E/DEP-E-20260819-ONER Online Experience/oner_online_experience_manuscript.md` - ONER Online Experience - DEP-E; overlap: experience, replay, minimization.
3. `.lake-data/DEP-E/DEP-E-20260731-CT-UCBVI Regret/ct_ucbvi_regret_manuscript.md` - CT-UCBVI Regret - DEP-E; overlap: regret, reinforcement.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
