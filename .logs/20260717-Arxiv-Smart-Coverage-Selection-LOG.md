# Black Lake Arxiv DEP: Smart Coverage Selection

- Public run date: 2026-07-17
- Actor/tool: Codex recurring automation, source-first arXiv review workflow.
- Action: selected, repaired, reviewed, and prepared one eligible paper for a Black Lake DEP-E deposit.
- Selected paper: *Selectively Combining Multiple Coverage Goals in Search-Based Unit Test Generation* (`arXiv:2208.04096v1`; DOI `10.1145/3551349.3556902`).
- Sanitized provenance: a verified local paper unit plus public arXiv, ASE, DOI, Zenodo, and author-publication records. All original source files, extracted text, and caches remain local and are not uploaded.
- Random method: `rg --files -g "*.pdf"` found 75,777 PDF candidates, collapsed to 75,776 unique parent-directory paper units. A used-paper index was built first; PowerShell `Get-Random` then made a uniform draw over 75,413 eligible identified units. The selected zero-based eligible index was 74,157.
- Dedup validation: scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, automation memory, and live Black-Lake-Data `.lake-data`/`.reports` for arXiv ID, DOI, normalized title, and slug. The scan observed 720 used arXiv IDs, excluded 178 units by used ID, and withheld 185 identifier-incomplete units from the draw. Exact-title, ID, and slug checks found no prior deposit. Duplicate rejections/reselections: 0.
- 24-hour validation: the public-safe cutoff date was 2026-07-16; no same-paper or same-unit completion, verification, report, status, or marker file was found on or after the cutoff.
- Source integrity before repair: `partial` because a valid PDF existed but full-paper HTML was absent.
- Repair: preserved the valid PDF; the official arXiv full-paper HTML endpoint returned 404, so the approved ar5iv full-paper fallback was fetched. Metadata HTML and the arXiv source package were also collected with two-attempt bounds and a 200 MiB cap. The paper-unit README, provenance JSON, machine-readable summary CSV, and verification report were updated.
- Source integrity after repair: `complete`. PDF: 1,208,175 bytes, `%PDF-` header, trailing `%%EOF`. Full-paper HTML: 560,847 bytes, 87,878 body characters, document marker present, 56 heading markers, and seven paper-structure terms. Source archive: 3,839,205 bytes with 66 entries. Partial files: 0.
- Evidence reviewed: complete PDF/full-paper HTML/TeX source, arXiv metadata, ASE research and artifact-evaluation pages, publisher DOI, artifact DOI records, and the corresponding author publication list. The artifact package and experiments were not downloaded or run.
- Related DEP entries: `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260714-Tech Intel 1106/daily_research_findings_2026-07-14_1106.md` (SCATE); `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260717-Tech Intel 0104/daily_research_findings_2026-07-17_0104.md` (SWE-Bench Pro audit); `Delphoa-Labs/Black-Lake-Data/.lake-data/DEP-20260716-Tech Intel 1303/daily_research_findings_2026-07-16_1303.md` (AgentCompass).
- Report-Mark: `.reports/BL-Arxiv-Smart-Coverage-Selection-20260717/Report-Mark.md`.
- DEP-E: `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals`.
- Manuscript: `.lake-data/DEP-E/DEP-E-20260717-Smart Coverage Goals/smart_coverage_goals_manuscript.md`.
- Outcome target: source-grounded research deposit with author claims separated from reviewer interpretation, exact-three synthesis groups, publication-index maintenance, a public-output leak scan, and a Markdown-only staged allowlist.

## Questions for the Next Reviewer

1. Does smart selection retain its advantage under equalized wall-clock, fitness-evaluation, and generated-suite-size budgets across current EvoSuite versions?
2. How stable are the criterion groups, representative goals, and `lineThreshold=8` choice across newer Java projects and non-Java test generators?
3. Can goal reduction be learned online without obscuring which test properties were intentionally represented or omitted?

## Challenges for the Next Review Pass

1. Reproduce the WS, MOSA, and DynaMOSA tables from the artifact at pinned versions with deterministic environment receipts.
2. Test criterion selection on recent projects and stratify by class complexity, infeasible goals, mutation operator, and build-system behavior.
3. Compare static correlation/subsumption rules against adaptive goal budgeting while preserving auditable property coverage.
