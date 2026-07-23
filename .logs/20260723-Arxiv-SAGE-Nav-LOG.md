# Arxiv DEP Job Log: SAGE-Nav

- Public run marker: 2026-07-23 (date only)
- Outcome: Complete after bounded local source repair
- Selected paper: *SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation*
- Stable identifier: arXiv:2606.25497v1
- Public record: https://arxiv.org/abs/2606.25497
- arXiv DOI: https://doi.org/10.48550/arXiv.2606.25497

## Selection and Deduplication

- Candidate enumeration used `rg --files -g "*.pdf"` against the private source archive.
- Enumeration produced 75,780 PDF files and 75,777 unique PDF-parent paper units.
- Unique units were sorted, then PowerShell `Get-Random` selected zero-based index 43,405 uniformly from `[0, 75,777)`.
- The first draw was accepted: 0 duplicate exclusions, 0 other exclusions, and 0 reselections.
- Dedup checked arXiv ID, DOI, normalized title, slug family, and same-paper markers across live `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data records.
- The only match was a metadata-only arXiv author-inventory row. It is not a processed DEP artifact and did not trigger exclusion.
- No matching Arxiv DEP artifact or same-paper marker within the preceding 24 hours was found.

## Local Source Integrity

- Initial classification: Partial. The existing 16,110,369-byte PDF passed the 10 KB minimum, `%PDF-` header, trailing `%%EOF`, and SHA-256 preservation checks, but full-paper HTML and companion verification records were absent.
- Repair: One bounded direct-HTTPS companion repair preserved the valid PDF, collected official arXiv metadata HTML and the source archive, and used the approved ar5iv fallback when official full-paper HTML was unavailable.
- Transfer controls: one active strategy, no credentials, a 200 MB target ceiling, a 50 MB partial ceiling, a 500 MB free-space floor, and one bounded attempt per artifact candidate.
- Final classification: Complete. Full-paper HTML is 179,235 bytes with 47,690 body characters, three document markers, 61 heading/section markers, at least five paper-structure term classes, and no abstract-only, error, or conversion marker.
- The local README, attribution/provenance record, machine-readable CSV summary, preflight manifest, and verification report were updated before review.
- All eight PDF pages were rendered and visually inspected in the private archive; extracted text and renderings remained local.
- No partial files remained after verification.

## Review Summary

- SAGE-Nav separates asynchronous LLM-based semantic waypoint planning from a high-frequency reactive navigation policy.
- A hierarchical scene graph is encoded by a three-layer relational graph network, conditioned on the active waypoint, and fused with egocentric visual features through cross-attention and an alignment-aware gate.
- The reported iTHOR result is 82.47% success overall and 77.22% for paths of at least five meters. RoboTHOR results are 52.35% and 40.82%, respectively.
- Six held-out object categories yield 75.05% zero-shot success, 34.05% SPL, and 0.38 m distance to success.
- The efficiency table reports 0.42 seconds average latency and 9.1 LLM calls per episode, with higher SPL than CogNav and SG-Nav but lower success than CogNav.
- Evidence limitations include simulator-only evaluation, unclear RoboTHOR split accounting, cross-publication baseline parity, best-validation-checkpoint selection without repeated-seed uncertainty, under-specified asynchronous latency accounting, no located official implementation, and no real-robot validation.

## Output Paths

- `.logs/20260723-Arxiv-SAGE-Nav-LOG.md`
- `.reports/BL-Arxiv-SAGE-Nav-20260723/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/README.md`
- `.lake-data/DEP-E/DEP-E-20260723-SAGE-Nav Review/sage_nav_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260720-VG Navigable Space/vg_navigable_space_manuscript.md`
2. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md`
3. `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`

## Next-Review Questions

1. Does SAGE-Nav retain its reported success and latency gains when all baselines are rerun with identical splits, sensors, compute, seeds, and LLM accounting?
2. How much of zero-shot performance comes from LLM priors versus scene-graph hierarchy, cross-attention, and the explicit gate under a factorial matched-compute study?
3. Can the planner-policy interface remain calibrated under detector errors, stale graph state, deadlocks, and real-robot perception and actuation delays?

## Challenges

1. Reproduce the online graph builder, prompts, waypoint parser, replanning triggers, cache behavior, and latency accounting without an author-identified code release.
2. Resolve the dataset-split and baseline-parity ambiguities while adding repeated seeds, confidence intervals, tail latency, LLM cost, and failure denominators.
3. Place semantic waypoint proposals behind independent traversability, collision, freshness, and safe-stop controls before any physical deployment claim.

## Submission Boundary

- Public allowlist: the five generated Markdown paths listed above.
- Excluded: PDF, full-paper HTML, metadata HTML, source archive, extracted text, renderings, caches, provenance records, verification files, and private archive locators.
- Source files were withheld locally. No `.source/` directory was created, and no source file may be staged, committed, uploaded, or attached.
