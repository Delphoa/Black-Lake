# Arxiv DEP Job Log

## Selection

- Selected paper: CogPortrait: Fine-Grained Eye-Region Control in Portrait Animation via Hierarchical Agent Planning.
- arXiv: `2605.28056v1`.
- Authors: He Feng, Yongjia Ma, Donglin Di, Lei Fan, and Tonghua Su.
- Selection method: `rg --files -g "*.pdf"` enumeration, unique PDF-parent paper units, sorted list, and uniform PowerShell `Get-Random` index selection.
- Candidate inventory: 75,960 PDFs collapsed to 75,957 parent-paper units.
- Draw: zero-based index 43,688; first draw accepted.
- Exclusions: duplicate/dedup exclusions 0; source-gate exclusions 0; reselections 0; same-paper recent-marker exclusions 0.
- Dedup markers checked: arXiv ID, arXiv DOI, normalized title, slug, repository artifact surfaces, automation memory, and relevant Black-Lake-Data search results.

## Source Integrity

- Initial source state: partial; the valid PDF existed but full-paper HTML was missing.
- Repair: one bounded single-paper archive repair obtained official arXiv full-paper HTML and refreshed the local README, provenance record, machine-readable summary, acquisition receipt, and verification report.
- Final verification: complete. The PDF passed the minimum size, `%PDF-` header, and trailing `%%EOF` checks. The full-paper HTML passed the minimum size, body-text, document-marker, heading, and paper-structure checks.
- Source package: unavailable from the e-print endpoint; no TeX/source archive was collected.
- Source policy: PDF, full-paper HTML, metadata HTML, extracted text, cache, and integrity records remain local. No source files were uploaded, staged, committed, or attached.

## Outputs

- `.logs/20260804-Arxiv-CogPortrait-Eye-Control-LOG.md`
- `.logs/20260804-Arxiv-CogPortrait-Eye-Control-PHASE-LOG.md`
- `.reports/BL-Arxiv-CogPortrait-Eye-Control-20260804/Report-Mark.md`
- `.lake-data/DEP-E/DEP-E-20260804-CogPortrait Control/README.md`
- `.lake-data/DEP-E/DEP-E-20260804-CogPortrait Control/cogportrait_eye_control_manuscript.md`
- `.staging/arxiv-dep-dedup-index.json`

## Related DEP Entries

- `.lake-data/DEP-E/DEP-E-20260721-Hallo4 Portrait Motion/hallo4_portrait_motion_manuscript.md` - portrait animation, preference alignment, and temporal motion conditioning.
- `.lake-data/DEP-E/DEP-E-20260726-MoGIC Boosting Motion/mogic_boosting_motion_manuscript.md` - intention understanding and motion-generation planning.
- `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md` - latent video consistency and evaluation beyond surface appearance.

## Next-Review Questions

1. Can the EMH benchmark and its manual eye-region annotations be released with sufficient licensing, consent, and split documentation for independent evaluation?
2. How much of the reported gain comes from the hierarchical agents, the prototype library, dynamic CFG, or KTO when each component is evaluated under matched compute and repeated seeds?
3. Do AU-F1, AU-Temp, Eye-LMD, identity similarity, and human judgments agree on failure cases such as gaze aversion, asymmetric blinks, and large-angle head motion?

## Challenges

1. No official code, checkpoint, configuration manifest, or reproducible environment was identified in the inspected paper sources.
2. The user-study protocol, annotator details, uncertainty, and statistical tests are not exposed in the main paper text inspected.
3. The source package was unavailable, and PDF text contains some encoding noise; no experiment or video generation was reproduced.

## Attribution and Public-Safety Note

Public artifacts cite the canonical arXiv URLs and arXiv-issued DOI. The complete paper source files were withheld locally, and no public artifact discloses local paths, machine data, usernames, timezone labels, or exact local execution timestamps.
