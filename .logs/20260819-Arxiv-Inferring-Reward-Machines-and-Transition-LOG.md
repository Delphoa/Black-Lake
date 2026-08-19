# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260819-8DFEF0DE`
- Deployment item ID: `BLAD-2200-20260819-8DFEF0DE-P105`
- Public-safe date: 2026-08-19
- Paper: *Inferring Reward Machines and Transition Machines from Partially Observable Markov Decision Processes*
- Identifier: `arXiv:2508.01947`; DOI: `10.48550/arXiv.2508.01947`
- URL: https://arxiv.org/abs/2508.01947

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,967 PDFs and 75,964 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 40,753 on draw 32.

## Research Focus Eligibility

- One-time focus: ML memory, stateful systems, and algorithmic research.
- Matched categories: stateful systems.
- Matched title/abstract terms or phrases: markov decision process, partially observable.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `Inferring-Reward-Machines-and-Transition` slug; the 24-hour marker cutoff was 2026-08-18.
- Duplicate exclusions: 2; focus exclusions: 29; source-gate exclusions: 0; reselections: 31.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 393,728 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 309,681 bytes, 67,532 body characters, 142 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260819-Arxiv-Inferring-Reward-Machines-and-Transition-LOG.md`
- `.reports/BL-Arxiv-Inferring-Reward-Machines-and-Transition-20260819/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260819-Inferring Reward Machines/README.md`
- `.lake-data/DEP-E/DEP-E-20260819-Inferring Reward Machines/inferring_reward_machines_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260818-Learning Adversarial/learning_adversarial_manuscript.md` - Learning Adversarial - DEP-E; overlap: markov, processes, transition, decision.
2. `.lake-data/DEP-E/DEP-E-20260731-CT-UCBVI Regret/ct_ucbvi_regret_manuscript.md` - CT-UCBVI Regret - DEP-E; overlap: markov, processes, decision, transition, reward.
3. `.lake-data/DEP-E/DEP-E-20260819-Kernel Taylor-Based Value/kernel_taylor_based_value_manuscript.md` - Kernel Taylor-Based Value - DEP-E; overlap: markov, processes, decision.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
