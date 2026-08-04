# Black Lake Arxiv DEP Log

## Public-Safe Run Summary

- Paper: *DRMOT: A Dataset and Framework for RGBD Referring Multi-Object Tracking*
- arXiv ID: `2602.04692` (reviewed public revision: v2)
- DEP date: `2026-08-04`
- Job type: source-first random arXiv research deposit
- Result: complete; public submission and notification are handled as the final workflow phase.
- Public boundary: source files were inspected locally and withheld from the public repository; no `.source/` directory was created.

## Selection and Deduplication

- Enumeration method: `rg --files -g "*.pdf"` against the local arXiv archive root.
- PDF candidates: `75,960`.
- Unique PDF-parent paper units: `75,957`.
- Random method: uniform zero-based `Get-Random` index over sorted unique paper units.
- Draw: index `25,503`; first draw accepted.
- Duplicate exclusions: `0`.
- Other exclusions: `0`.
- Same-paper-within-24-hours markers: `0`.
- Reselections: `0`.
- Dedup keys checked: arXiv ID, arXiv DOI, normalized title, paper slug, prior Arxiv DEP paths, automation memory, and relevant Black-Lake-Data inventory/artifacts.

## Source Integrity Gate

- Initial state: partial; the selected unit had a valid PDF but no full-paper HTML.
- Repair: one bounded brokered single-paper archive repair; the existing valid PDF was preserved.
- Final PDF verification: `28,646,000` bytes, `%PDF-` header, trailing `%%EOF`.
- Final full-paper HTML verification: `180,925` bytes, `50,391` body characters, document marker, `65` heading/section markers, and `7` paper-structure terms.
- Metadata/provenance/summary/verification records: updated in the local archive unit.
- Source package: unavailable through the broker redirect policy; this did not block review after PDF and full-paper HTML verification.
- Partial files after repair: none observed.

## Output Paths

- `.logs/20260804-Arxiv-DRMOT-LOG.md`
- `.reports/BL-Arxiv-DRMOT-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-DRMOT Tracking/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-DRMOT Tracking/drmot_tracking_manuscript.md`
- `.lake-data/DEP-E/.index/pubs-index.md`

## Review and Validation Notes

The full arXiv paper was inspected through its verified local HTML and the live arXiv metadata/HTML pages. The review covers DRSet, DRTrack, depth-promoted grounding, geometric-aware GRPO, depth-enhanced OC-SORT association, quantitative results, ablations, limitations, the official repository state, and three related Black Lake DEP entries. The manuscript follows the `2026-07-07-expanded` schema, and the Report-Mark contains the required exact-three synthesis sets and three bounded Python mock-ups.

No PDF, HTML, metadata page, source archive, cache, extracted text, model, dataset, or local archive record was staged, committed, uploaded, or attached. Slack notification is sent only after the public commit is verified.

## Next-Review Questions

1. Does DRTrack retain its depth benefit under calibrated depth noise, missing depth, and cross-sensor shifts?
2. How much of the reported gain comes from depth input, GRPO fine-tuning, or the association rule when compute and prompts are matched?
3. Can a larger and more balanced set of depth-related language expressions improve rare-category and multi-target generalization?

## Challenges

1. The public repository states that the dataset, code, and weights will be released after acceptance, so exact implementation reproduction is not currently available from the inspected repository state.
2. The dataset is compact and structurally imbalanced, making broad claims about real-world tracking, rare categories, and long-tail spatial language premature.
3. Depth quality, annotation agreement, privacy/consent, and scene-level leakage need explicit audit evidence before any consequential deployment.

## Attribution Boundary

- Public source URLs are recorded in the Report-Mark, DEP README, and manuscript.
- Source files remain local only; no public artifact contains a local absolute path, machine identifier, username, timezone label, or exact local execution timestamp.
