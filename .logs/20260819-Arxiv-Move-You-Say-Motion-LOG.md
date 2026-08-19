# Black Lake Arxiv DEP Log

## Run Summary

- Automation: Black Lake Arxiv DEP 1500
- Run date: 2026-08-19
- Selected paper: Move as You Say, Interact as You Can: Language-guided Human Motion Generation with Scene Affordance
- arXiv: [2403.18036v1](https://arxiv.org/abs/2403.18036)
- DOI: [10.48550/arXiv.2403.18036](https://doi.org/10.48550/arXiv.2403.18036)
- Selection method: enumerate PDF files with rg --files -g "*.pdf", collapse each PDF parent directory to one paper unit, and draw one uniform index with PowerShell Get-Random.
- Candidate counts: 75,967 PDF files and 75,964 distinct parent-paper units.
- Draw: index 6,095; first draw accepted.
- Duplicate exclusions: 0.
- Reselections: 0.
- Same-paper markers within the prior 24-hour window: none found.

## Source Integrity and Locality

The initial archive unit was partial because it had a valid PDF but no full-paper HTML. A bounded repair fetched the public arXiv full-paper HTML and refreshed local archive metadata and verification records. The PDF and full-paper HTML then passed the mandatory validation checks. Source files, extracted text, caches, and acquisition records remain local and were not uploaded, staged, committed, attached, or sent to Slack.

## Review and Extraction

The source-first review used the local PDF and full-paper HTML, refreshed local metadata, the public arXiv abstract and HTML, the official project page, and the official implementation repository. The missing-only cache pass completed with HTML extraction through html-regex and PDF extraction through pypdf because pdftotext was unavailable. No local source package was available, so no source text was extracted. No experiments were rerun.

The paper presents a two-stage scene-affordance pipeline: an Affordance Map Diffusion Model grounds language and human motion in a 3D scene, and an Affordance-aware Motion Diffusion Model generates motion conditioned on that representation. Evaluation covers HumanML3D, HUMANISE, and a novel-scene evaluation set; failure cases include unseen interactions and complex descriptions.

## Output Paths

- .logs/20260819-Arxiv-Move-You-Say-Motion-LOG.md
- .logs/20260819-Arxiv-Move-You-Say-Motion-PHASE-LOG.md
- .reports/BL-Arxiv-Move-You-Say-Motion-20260819/Report-Mark.md
- .lake-data/DEP-E-20260819-Move You Say/README.md
- .lake-data/DEP-E-20260819-Move You Say/move_you_say_motion_manuscript.md
- .staging/arxiv-dep-dedup-index.json

## Related DEP Entries

1. .lake-data/DEP-E/DEP-E-20260720-AR-Drag Motion/ar_drag_motion_manuscript.md — motion generation and controllable sequence behavior; useful for comparing semantic control with interactive responsiveness.
2. .lake-data/DEP-E/DEP-E-20260724-Habitat Synthetic Scenes/habitat_synthetic_scenes_manuscript.md — 3D scene coverage and realism; useful for assessing how environment diversity constrains affordance learning.
3. .lake-data/DEP-E/DEP-E-20260809-NaLA A 3D Native LLM/nala_a_3d_native_llm_manuscript.md — language-conditioned spatial representation; useful for the language-to-scene grounding interface.

## Questions for Next Review

1. Can the official implementation reproduce the reported grounding and motion metrics under a pinned, publicly documented environment and data manifest?
2. How does the affordance representation behave for unseen interaction categories, longer instructions, occluded geometry, and multiple people?
3. Which independent metrics best separate semantic faithfulness from a plausible motion grounded at the wrong scene location?

## Challenges for Next Review

1. Establish a legally redistributable public or synthetic evaluation slice without exposing restricted source data.
2. Audit contact, collision, average pairwise distance, and diversity trade-offs with matched seeds and uncertainty intervals.
3. Measure diffusion latency, failure recovery, and human correction cost in an authorized interactive prototype.

## Status

Research artifacts were drafted from verified local source material and public references, then committed and pushed to [Delphoa/Black-Lake](https://github.com/Delphoa/Black-Lake/commit/d82a3ab6). The phase log records cache and integrity metrics. The completion notice was sent to [#black-lake-artifacts](https://delphoalabs.slack.com/archives/C0BFP2E4ZNJ/p1787121173070219).
