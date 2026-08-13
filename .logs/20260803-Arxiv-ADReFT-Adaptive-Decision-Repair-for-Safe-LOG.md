# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260803-11C1283E`
- Deployment item ID: `BLAD-2200-20260803-11C1283E-P10`
- Public-safe date: 2026-08-03
- Paper: *ADReFT: Adaptive Decision Repair for Safe Autonomous Driving via Reinforcement Fine-Tuning*
- Identifier: `arXiv:2506.23960`; DOI: `10.48550/arXiv.2506.23960`
- URL: https://arxiv.org/abs/2506.23960

## Random Selection

- `rg --files -g "*.pdf"` enumerated 75,960 PDFs and 75,957 unique parent units.
- A uniform cryptographic random index, without a derived seed, selected one-based index 40,072 on draw 1.

## Deduplication and Reselection

- Scanned `.logs`, `.reports`, `.lake-data`, `.staging/arxiv-dep-dedup-index.json`, automation memory, relevant `Delphoa-Labs/Black-Lake-Data` deposits, and the current-job selected set.
- Keys included arXiv ID, DOI, normalized title, and `ADReFT-Adaptive-Decision-Repair-for-Safe` slug; the 24-hour marker cutoff was 2026-08-02.
- Duplicate exclusions: 0; source-gate exclusions: 0; reselections: 0.

## Source Integrity

- Final state: verified complete after one bounded local archive repair.
- PDF: 1,094,631 bytes with a valid `%PDF-` header and trailing `%%EOF`; page markers: 12; sampled text inspection: true.
- Full-paper HTML: 687,380 bytes, 112,722 body characters, 62 headings, and 7 paper-structure terms.
- Unexpected partials: 0. All source and integrity files remain local.

## Public Outputs

- `.logs/20260803-Arxiv-ADReFT-Adaptive-Decision-Repair-for-Safe-LOG.md`
- `.reports/BL-Arxiv-ADReFT-Adaptive-Decision-Repair-for-Safe-20260803/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision/README.md`
- `.lake-data/DEP-E/DEP-E-20260803-ADReFT Adaptive Decision/adreft_adaptive_decision_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260721-Stealth Memory Injection/stealth_memory_trust_manuscript.md` - Stealth Memory Trust - DEP-E; overlap: reinforcement, fine-tuning, adaptive, decision.
2. `.lake-data/DEP-E/DEP-E-20260729-Decoupled Training with/decoupled_training_with_manuscript.md` - Decoupled Training with - DEP-E; overlap: reinforcement, fine-tuning, autonomous, decision, safe.
3. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - LA-Pose Latent Action - DEP-E; overlap: driving, fine-tuning, decision, safe.

Only generated Markdown and required index JSON may be staged. PDF, HTML, source archives, extracted source text, caches, datasets, credentials, and executable research artifacts were withheld; zero source-document uploads.
