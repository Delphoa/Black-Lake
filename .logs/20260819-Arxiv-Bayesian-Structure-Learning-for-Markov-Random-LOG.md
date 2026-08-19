# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P83`
- Public-safe date: 2026-08-19
- Paper: *Bayesian Structure Learning for Markov Random Fields with a Spike and Slab Prior*
- Identifier: `arXiv:1206.1088`; DOI: `10.48550/arXiv.1206.1088`
- URL: https://arxiv.org/abs/1206.1088

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 13,705 on draw 9.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: learning, markov.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Bayesian-Structure-Learning-for-Markov-Random` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 6; source-gate exclusions: 0; reselections: 8.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 695,649 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 11; sampled text inspection: true.
- Full-paper HTML: 240,536 bytes, 55,753 body characters, 52 headings, and 6 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Bayesian-Structure-Learning-for-Markov-Random-LOG.md`
- `.reports/BL-Arxiv-Bayesian-Structure-Learning-for-Markov-Random-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Bayesian Structure/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Bayesian Structure/bayesian_structure_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260819-Automated Random/automated_random_manuscript.md` - Automated Random - DEP-E; overlap: bayesian, random, structure.
2. `.lake-data/DEP-E/DEP-E-20260728-Constrained Bayesian/constrained_bayesian_manuscript.md` - Constrained Bayesian - DEP-E; overlap: bayesian, random, structure.
3. `.lake-data/DEP-E/DEP-E-20260803-Latent-IMH Efficient/latent_imh_efficient_manuscript.md` - Latent-IMH Efficient - DEP-E; overlap: bayesian, structure.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
