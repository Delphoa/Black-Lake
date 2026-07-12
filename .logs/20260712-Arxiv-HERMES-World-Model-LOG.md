# Arxiv DEP Log: HERMES World Model

## Public-Safe Run Summary

- Date: 2026-07-12
- Actor/tool: Codex recurring `Black Lake Arxiv DEP 1100` workflow
- Action: Randomly select one eligible local arXiv paper, review it source-first, connect it to exactly three related DEP entries, and deposit a log, Report-Mark, and DEP-E manuscript.
- Outcome: Selected arXiv:2501.14729, *HERMES: A Unified Self-Driving World Model for Simultaneous 3D Scene Understanding and Generation*. Duplicate checks passed on the first draw.
- Affected DEP: `.lake-data/DEP-E-20260712-HERMES World Model`
- Blockers: None.

## Random Selection Method

- Enumeration command: `rg --files -g "*.pdf"` against the local arXiv archive.
- Paper unit: Each unique PDF parent directory; adjacent readme and metadata files were treated as metadata for that unit.
- PDF files enumerated: 75,761.
- Candidate paper units: 75,761.
- Draw method: PowerShell `Get-Random` over the zero-based unit index range.
- Selected zero-based index: 69,210.
- Selected arXiv ID: 2501.14729.
- Selected DOI marker: 10.48550/arXiv.2501.14729.
- Duplicate rejections: 0.
- Reselections: 0.

## Deduplication and Eligibility

- Locations scanned: `Black-Lake/.logs`, `Black-Lake/.reports`, `Black-Lake/.lake-data`, automation memory, `Black-Lake-Data/.lake-data`, and `Black-Lake-Data/.reports`.
- Matching keys: Versionless arXiv ID, arXiv DOI marker, normalized title, and slug variants.
- Unique arXiv IDs observed in dedup context: 363.
- Candidate units matching a previously observed arXiv ID: 67.
- Exact selected-paper matches: 0.
- Same-paper markers in the preceding 24 hours: 0.
- Eligibility result: Accepted on the first uniform draw.

## Source Review

- Local evidence: The paper PDF and adjacent provenance readme were inspected; location details are withheld.
- Extraction: `pypdf` produced a 76,272-byte text cache. Local HTML and source-package text were unavailable.
- Primary public evidence: arXiv abstract/HTML, the ICCV 2025 open-access paper, and the official HERMES repository were inspected.
- Publication status: The public paper is the ICCV 2025 accepted work. No separate publisher DOI was found in inspected sources; the arXiv DOI marker is retained.
- Code status: The official Apache-2.0 repository contains setup, data/weights, usage, code, and model-release material; no reproduction was attempted.
- Source files collected into the DEP: None. The original PDF remains outside the public deposit and is not redistributed.

## Related DEP Entries

1. `.lake-data/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` — geometry-aware generation and spatial-consistency evaluation overlap with HERMES's BEV-to-point-cloud world modeling.
2. `.lake-data/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md` — attention and representation probes provide a review pattern for HERMES's cross-modal world-query pathway.
3. `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260628-Tech Intel 0102/daily_research_findings_2026-06-28_0102.md` — item 6 describes coverage-aware hallucination detection for visual world models, directly relevant to HERMES failure evaluation.

## Output Inventory

- `.logs/20260712-Arxiv-HERMES-World-Model-LOG.md`
- `.reports/BL-Arxiv-HERMES-World-Model-20260712/Report-Mark.md`
- `.lake-data/DEP-E-20260712-HERMES World Model/README.md`
- `.lake-data/DEP-E-20260712-HERMES World Model/hermes_world_model_manuscript.md`

## Validation Notes

- Live `Delphoa/Black-Lake` and `Delphoa-Labs/Black-Lake-Data` README authorities were read before drafting.
- Public content uses repository-relative paths, public URLs, and date-only markers.
- No `.source/` directory was created because redistribution was unnecessary and the source PDF was not collected for this public deposit.
- The manuscript title and H1 are identical and within 40 characters.
- Exactly three related DEP entries are used across the artifacts.

## Next-Review Questions

1. Do HERMES's gains persist under long-tail weather, rare agents, sensor degradation, and distribution shifts beyond nuScenes-derived data?
2. Which causal interventions can establish whether LLM-enriched world queries genuinely drive better geometry rather than correlate with stronger shared features?
3. Can future image generation and perception tasks be added without degrading the compact BEV interface or destabilizing joint optimization?

## Challenges

1. The paper reports strong benchmarks, but this run did not reproduce training or inference on the released code and checkpoints.
2. Caption and VQA metrics do not establish safety-critical scene understanding, calibration, or planning reliability.
3. Point-cloud Chamfer distance can hide object-level, semantic, and rare-event failures that matter in autonomous-driving simulation.

## Attribution Block

- Source URL: https://arxiv.org/abs/2501.14729
  - Applies to: paper identity, authors, submission date, abstract, and primary claims.
- Source URL: https://arxiv.org/html/2501.14729
  - Applies to: method, experiments, ablations, results, limitations, and supplementary details.
- Source URL: https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_HERMES_A_Unified_Self-Driving_World_Model_for_Simultaneous_3D_Scene_ICCV_2025_paper.html
  - Applies to: ICCV 2025 publication context and accepted-paper evidence.
- Source URL: https://github.com/LMD0311/HERMES
  - Applies to: official implementation, release, and license status.
