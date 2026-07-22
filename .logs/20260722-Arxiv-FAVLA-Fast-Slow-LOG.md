# Arxiv DEP Job Log: FAVLA Fast-Slow

- Public run marker: 2026-07-22 (date only)
- Outcome: Complete after bounded local source repair
- Selected paper: *FAVLA: A Force-Adaptive Fast-Slow VLA model for Contact-Rich Robotic Manipulation*
- Stable identifier: arXiv:2602.23648v1
- Public record: https://arxiv.org/abs/2602.23648
- arXiv DOI: https://doi.org/10.48550/arXiv.2602.23648

## Selection and Deduplication

- Candidate enumeration used `rg --files -g "*.pdf"` against the private source archive.
- Enumeration produced 75,780 PDF files and 75,777 unique PDF-parent paper units.
- Unique units were sorted, then PowerShell `Get-Random` selected zero-based index 47,262 uniformly from `[0, 75,777)`.
- The first draw was accepted: 0 duplicate exclusions, 0 other exclusions, and 0 reselections.
- Dedup checked arXiv ID, DOI, normalized title, slug family, and same-paper markers across live `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and relevant Black-Lake-Data records.
- The only match was one metadata-only author-inventory row; it is not a processed DEP artifact and did not trigger exclusion.
- No matching Arxiv DEP artifact or same-paper marker within the prior 24 hours was found.

## Local Source Integrity

- Initial classification: Partial. The existing 22,218,424-byte PDF passed minimum size, `%PDF-`, trailing `%%EOF`, and hash-preservation checks, but full-paper HTML and companion verification files were absent.
- Repair: One bounded direct-HTTPS companion repair preserved the PDF and collected official metadata HTML, official full-paper HTML, and the arXiv source archive. The transfer used a 200 MB target ceiling, a 50 MB partial ceiling, a 500 MB free-space floor, no credentials, and bounded source candidates.
- Final classification: Complete. Full-paper HTML is 212,377 bytes with 56,054 body characters, a full-document marker, 54 heading/section markers, seven paper-structure term classes, no abstract/error/conversion marker, and zero partial files.
- The local README, attribution/provenance, CSV summary, preflight manifest, and verification report were updated before review.
- All 16 PDF pages were visually inspected inside the private archive; temporary renderings were removed afterward.
- Source locality: PDF, full-paper HTML, metadata HTML, source archive, extraction material, verification records, and renderings remained private. No source file was uploaded and no public `.source/` directory was created.

## Review Outcome

FAVLA combines a slow PaliGemma-based semantic backbone with a force-injected action expert that can execute repeatedly inside one visual cycle. A predicted near-future force-variance signal schedules those calls, while fixed noise and temporal ensembling stabilize overlapping action chunks. The paper reports 80.8% unweighted mean success across four real-robot tasks, 13.8 points over the strongest mean baseline, plus lower average peak forces on Gear Assembly and Box Flipping.

The evidence is promising but bounded. Box Flipping is a three-way 80% tie rather than a unique FAVLA win. Training streams are downsampled to 30 Hz even though force was recorded at 200 Hz and the motivation emphasizes 100-1000 Hz contact cues. Trial counts total 85 per method, with no repeated training seeds, intervals, matched-average-compute scheduling control, official code, dataset, or complete wall-clock timing contract.

## Generated Outputs

- `.logs/20260722-Arxiv-FAVLA-Fast-Slow-LOG.md`
- `.reports/BL-Arxiv-FAVLA-Fast-Slow-20260722/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/README.md`
- `.lake-data/DEP-E/DEP-E-20260722-FAVLA Fast-Slow/favla_fast_slow_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Related DEP Entries

1. `.lake-data/DEP-E/DEP-E-20260719-Semantic Skill MoE/semantic_skill_moe_manuscript.md` - semantic action routing, chunk consistency, route auditing, and rare-skill coverage.
2. `.lake-data/DEP-E/DEP-E-20260714-iKalibr Calibration/ikalibr_calibration_manuscript.md` - spatiotemporal sensor calibration, timing provenance, observability, and drift gates.
3. `.lake-data/DEP-E/DEP-E-20260711-RRT-CBF Motion/rrt_cbf_motion_manuscript.md` - independent motion constraints, state/solver validity, trajectory tracking, and fallback.

## Next-Review Questions

1. Does adaptive scheduling outperform static policies when average and maximum action-expert calls, sensor age, and end-to-end latency are matched?
2. How do native 200 Hz force input and downsampled 30 Hz input change success, force impulse, slip, safety stops, and response delay?
3. Do the gains persist across new robots, objects, friction/compliance regimes, calibration drift, sensor faults, and repeated training/evaluation seeds?

## Challenges

1. The paper's high-frequency-force motivation is under-specified operationally because training data are downsampled to 30 Hz and actual evaluation control rates and latencies are not fully reported.
2. Small unequal trial counts, no intervals, cumulative ablations, and an unmatched compute schedule limit causal and statistical interpretation.
3. No official code, weights, dataset, evaluation scripts, or calibration/timing traces were identified, preventing exact reproduction and baseline-parity audit.

## Attribution Block

- Source URL: https://arxiv.org/abs/2602.23648
  - Applies to: selection identity, authors, metadata, version, DOI, license, and public paper links.
- Source URL: https://arxiv.org/pdf/2602.23648
  - Applies to: full method, experiments, figures, tables, appendix, and failure analysis; inspected locally and withheld.
- Source URL: https://arxiv.org/html/2602.23648
  - Applies to: verified full-paper cross-check; inspected locally and withheld.
- Source URL: https://arxiv.org/e-print/2602.23648
  - Applies to: equations, tables, captions, training/data details, and appendix; source archive withheld.
- Source files: Withheld locally; none were uploaded, staged, copied, or attached.
