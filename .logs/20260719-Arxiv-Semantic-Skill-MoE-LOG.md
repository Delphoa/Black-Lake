# Black Lake Arxiv DEP Log

- Automation: `Black Lake Arxiv DEP 2200 x10`
- Deployment job ID: `BLAD-2200-20260719-7D93E819`
- Deployment item ID: `BLAD-2200-20260719-7D93E819-P08`
- Public-safe run date: 2026-07-19
- Outcome: reviewed, validated, and prepared for submission
- Selected paper: *Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation*
- Stable identifier: `arXiv:2605.23477v1`
- Canonical URL: https://arxiv.org/abs/2605.23477

## Random Selection

- Method: `rg --files -g "*.pdf"`, unique PDF-parent units, uniform PowerShell `Get-Random` index.
- Refreshed pool: 75,790 PDFs across 75,777 paper units; selected one-based index: 35,828.
- First draw accepted; no machine-, user-, path-, timezone-, or timestamp-derived seed.

## Deduplication and Reselection

- Scanned Black Lake logs, reports, DEP-E artifacts/indexes, this automation memory, relevant Black-Lake-Data records, the current-job set, and the P07 rejected-unit exclusion.
- Keys: arXiv ID, DOI, normalized title, `Semantic-Skill-MoE` slug, prior cron markers, and markers on or after cutoff date 2026-07-18.
- Duplicate exclusions: 0; source-gate rejections: 0; reselections: 0.

## Source Integrity

- Initial state: partial; valid PDF present, full-paper HTML absent.
- One bounded repair retrieved official full-paper HTML and metadata while preserving the PDF.
- PDF: 3,013,189 bytes; `%PDF-` and trailing `%%EOF` passed.
- HTML: 319,510 bytes; 83,999 body characters; document marker; 43 headings; six structure terms; no rejected payload pattern.
- Cache: `cached`; PDF and HTML extraction succeeded; unexpected partials: 0.
- Final state: complete. Source files and caches remain local.

## Public Outputs

- `.logs/20260719-Arxiv-Semantic-Skill-MoE-LOG.md`
- `.reports/BL-Arxiv-Semantic-Skill-MoE-20260719/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/README.md`
- `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-DMNN Conditional Paths/dmnn_conditional_paths_manuscript.md` - conditional routing, expert utilization, and runtime evidence.
2. `.lake-data/DEP-E/DEP-E-20260713-LA-Pose Latent Action/la_pose_latent_action_manuscript.md` - latent action structure, transfer, and rare-motion limits.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - explicit admissibility, constrained motion, and safety fallback.

## Submission Gate

- Allowlist: generated Markdown plus required publication-index Markdown and dedup JSON.
- `.source/`: not created; source-document upload: none.
- Implementation discussion is simulation-first and safety-gated; no hardware control command or executable policy is published.
- Local paths, exact timestamps, timezone labels, and user/machine context are withheld.
