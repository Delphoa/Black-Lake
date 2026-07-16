# Black Lake Arxiv DEP: Medical Diff VQA

- Public run date: 2026-07-16
- Actor/tool: Codex recurring automation, source-first arXiv review workflow.
- Action: selected, repaired, reviewed, and prepared one eligible paper for a Black Lake DEP-E deposit.
- Selected paper: *Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering* (`arXiv:2307.11986v2`; DOI `10.1145/3580305.3599819`).
- Sanitized provenance: a verified local paper unit plus public arXiv, DOI, PhysioNet, and official GitHub records. All original source files, extracted text, and caches remain local and are not uploaded.
- Random method: `rg --files -g "*.pdf"` found 75,777 PDF candidates, collapsed to 75,776 unique parent-directory paper units. A used-paper index was built first; PowerShell `Get-Random` then made a uniform draw over 75,537 eligible units. The selected zero-based eligible index was 32,396.
- Dedup validation: scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data `.lake-data`/`.reports` for arXiv ID, DOI, normalized title, and slug. The scan observed 446 used arXiv IDs, excluded 54 units by used ID, and withheld 185 identifier-incomplete units from the draw. Exact-title, ID, and slug checks found no prior deposit. Duplicate rejections/reselections: 0.
- 24-hour validation: the public-safe cutoff date was 2026-07-15; no same-paper or same-unit marker was found on or after the cutoff.
- Source integrity before repair: `partial` because a valid PDF existed but full-paper HTML was absent.
- Repair: preserved the valid PDF; fetched official full-paper HTML, metadata HTML, and the arXiv source package with bounded direct-HTTPS attempts; updated the paper-unit README, provenance JSON, machine-readable summary CSV, and verification report.
- Source integrity after repair: `complete`. PDF: 10,107,164 bytes, `%PDF-` header, trailing `%%EOF`. Full-paper HTML: 204,036 bytes, 60,080 body characters, document marker present, 60 heading markers, and eight paper-structure terms. Source archive: 40,091,466 bytes with 51 entries. Partial files: 0.
- Evidence reviewed: complete PDF/HTML/TeX source, arXiv metadata, KDD DOI metadata, PhysioNet Medical-Diff-VQA v1.0.1, official dataset-generation repository, and official EKAID implementation repository at observed commit `1e5dd0de91554515d2acc83ad402e810ace0a5d7`. Code and experiments were not run.
- Related DEP entries: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260714-OViP Preference/ovip_preference_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260709-VideoWeave Geometry/videoweave_geometry_manuscript.md`.
- Report-Mark: `.reports/BL-Arxiv-Medical-Diff-VQA-20260716/Report-Mark.md`.
- DEP-E: `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA`.
- Manuscript: `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md`.
- Outcome target: source-grounded research deposit with author claims separated from reviewer interpretation, exact-three synthesis groups, publication-index maintenance, a public-output leak scan, and a Markdown-only staged allowlist.

## Questions for the Next Reviewer

1. How well does the model preserve temporal disease-change semantics when image alignment, projection, device, or acquisition protocol changes?
2. Does the rule-generated QA distribution contain patient, report-template, or lexical shortcuts that inflate answer metrics without improving image grounding?
3. Can clinical experts validate graph attention and generated answers prospectively without treating saliency as causal explanation?

## Challenges for the Next Review Pass

1. Reproduce the paper tables from the released dataset and code at pinned versions, including repeated seeds and confidence intervals.
2. Add patient-level leakage audits, subgroup analysis, calibration, abstention, and clinically meaningful error severity.
3. Test graph ablations under controlled spatial misregistration and knowledge-graph corruption rather than only aggregate caption metrics.
