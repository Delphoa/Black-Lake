# Arxiv DEP Log: SIM MARL Power

- Date marker: 2026-07-22
- Actor/tool: Codex recurring Arxiv DEP automation
- Selected paper: *Joint Power Allocation and Phase Shift Design for Stacked Intelligent Metasurfaces-aided Cell-Free Massive MIMO Systems with MARL*
- Stable identifier: arXiv:2502.19675v1; DOI 10.48550/arXiv.2502.19675
- Canonical URL: https://arxiv.org/abs/2502.19675v1
- Outcome: reviewed, validated, and deposited as generated public-safe Markdown.

## Selection Method

`rg --files -g "*.pdf"` enumerated 75,780 PDFs. Treating each PDF parent directory as one paper unit produced 75,777 units. Dedup reconciliation matched 266 units against 1,100 normalized used identifiers, leaving 75,511 eligible units. PowerShell `Get-Random` selected the first accepted rejection-sampling draw: zero-based all-unit index 38,440 and final eligible index 38,300. Reselections: 0.

## Dedup and Recent-Marker Validation

Black-Lake `.logs`, `.reports`, `.lake-data`, the public dedup index, automation memory, and relevant live Black-Lake-Data entries were scanned for the arXiv ID, DOI, normalized title, slug family, owning artifacts, and recent same-paper markers. No prior Arxiv DEP log, report, DEP-E deposit, or recent owning marker matched the paper.

## Source Integrity and Repair

The initial source state was `partial`: a 2,290,516-byte PDF passed the minimum-size, `%PDF-` header, trailing `%%EOF`, and parse checks, but full-paper HTML was absent. Review paused for one bounded local-only repair. The valid PDF was preserved; full-paper HTML, metadata HTML, and the source package were collected; the local README, attribution record, machine-readable summary, and verification report were updated.

Final verification was `complete`: six PDF pages; 459,959-byte full-paper HTML with 55,804 body characters, a document marker, 44 section/heading markers, and six structure terms; 42,116-byte metadata HTML; 3,167,313-byte source package with 15 readable entries; zero partial files. All source files and processing material remain local. No source file was uploaded, staged, attached, or placed in `.source/`.

## Outputs

- `.logs/20260722-Arxiv-SIM-MARL-Power-LOG.md`
- `.reports/BL-Arxiv-SIM-MARL-Power-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-SIM MARL Power/sim_marl_power_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260716-Multi-Point ISAC/multi_point_isac_manuscript.md` - direct distributed wireless allocation and coordination overlap.
2. `.lake-data/DEP-E/DEP-E-20260711-Telecom AI Roadmap/telecom_ai_roadmap_manuscript.md` - guarded telecom AI execution, digital-twin, monitoring, and rollback overlap.
3. `.lake-data/DEP-E/DEP-E-20260716-GPMD Regularized RL/gpmd_regularized_rl_manuscript.md` - policy regularization, convergence, and approximation-error overlap.

## Next-Review Questions

1. Does a corrected, fully specified NVR-MAPPO implementation reproduce the early-convergence claim over multiple seeds?
2. How much of the reported gain remains against strong alternating-optimization and small-instance oracle baselines?
3. Do discrete phase control, stale CSI, calibration drift, communication cost, and fairness constraints change the method ranking?

## Challenges

1. The source bundle has no official code, raw curves, seed schedule, or complete configuration manifest.
2. The actor-loss source expression and approximately 18% convergence claim are not specified precisely enough for direct reproduction.
3. Simulation omits hardware nonidealities, uncertainty, energy measurement, fairness, and operational communication cost.

## Blockers

None for source-grounded deposition. Independent reproduction and authorized hardware validation remain future work, not completion blockers.
