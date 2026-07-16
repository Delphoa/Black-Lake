# Black Lake Arxiv DEP: Beyond XAI

- Public run date: 2026-07-16
- Actor/tool: Codex recurring automation, source-first arXiv review workflow.
- Action: selected, repaired, reviewed, and prepared one eligible paper for a Black Lake DEP-E deposit.
- Selected paper: *Beyond Explainable AI (XAI): An Overdue Paradigm Shift and Post-XAI Research Directions* (`arXiv:2602.24176v5`; arXiv-issued DOI `10.48550/arXiv.2602.24176`).
- Sanitized provenance: a verified local paper unit plus public arXiv records. All original source files, extracted content, caches, and local locations remain private and were not uploaded.
- Random method: `rg --files -g "*.pdf"` found 75,777 PDF candidates, collapsed to 75,776 unique parent-directory paper units. PowerShell `Get-Random` made a uniform zero-based draw over the raw units; rejection on used or identifier-incomplete units preserves a uniform eligible selection. The accepted raw index was 28,956.
- Dedup validation: scanned Black Lake `.logs`, `.reports`, `.lake-data`, `.staging`, the DEP-E and DEP-A publication indexes, automation memory, and live Black-Lake-Data `.lake-data`/`.reports` for arXiv ID, DOI, normalized title, and slug. The primary-record set contained 232 used arXiv IDs; 93 archive units matched a used primary ID and 185 lacked a derivable identifier, leaving 75,498 units eligible under those filters. The selected ID, DOI, normalized title, and slug were absent. Duplicate rejections/reselections: 0.
- 24-hour validation: the public-safe cutoff date was 2026-07-15; no same-paper or same-unit marker was found on or after the cutoff. Black-Lake-Data contained metadata-inventory rows only, not a prior DEP synthesis for this paper.
- Source integrity before repair: `partial`; the 1,976,924-byte PDF passed the size, `%PDF-` header, trailing `%%EOF`, and SHA-256 checks, but full-paper HTML was absent.
- Repair: preserved the valid PDF; fetched the arXiv metadata page, official full-paper HTML, and source package using bounded direct-HTTPS attempts; updated the archive-unit README, provenance JSON, machine-readable summary CSV, and verification report.
- Source integrity after repair: `complete`. The official full-paper HTML is 356,861 bytes with 140,055 body characters, a document marker, 71 heading/section markers, and seven paper-structure terms. The source package is 2,026,164 bytes with a readable archive inventory. Partial files: 0.
- Evidence reviewed: complete PDF, official full-paper HTML, metadata HTML, TeX source, 287-entry bibliography, arXiv version history, and the paper's seven figure assets. The paper is a cross-disciplinary position and literature-synthesis article; it does not report an original benchmark, released dataset, or official implementation.
- Related DEP entries: `.lake-data/DEP-E/DEP-E-20260712-VLM Probing/vlm_probing_manuscript.md`; `.lake-data/DEP-E/DEP-E-20260708-Agent State Review/agent_state_review.md`; `.lake-data/DEP-E/DEP-E-20260716-Medical Diff VQA/medical_diff_vqa_manuscript.md`.
- Report-Mark: `.reports/BL-Arxiv-Beyond-XAI-20260716/Report-Mark.md`.
- DEP-E: `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI`.
- Manuscript: `.lake-data/DEP-E/DEP-E-20260716-Beyond XAI/beyond_xai_manuscript.md`.
- Outcome target: source-grounded position-paper review with author claims separated from reviewer assessment, exact-three synthesis groups, publication-index maintenance, public-output leak scanning, and a Markdown-only staged allowlist.

## Questions for the Next Reviewer

1. Which empirical findings survive a preregistered systematic review that separates post-hoc proxy explanations, intrinsically interpretable models, human-centered explanation interfaces, and mechanistic analysis?
2. Can interactive verification improve calibrated reliance without simply moving opacity, bias, or authority into expert panels and certification institutions?
3. Which intervention-based tests can distinguish a useful model diagnostic from a faithful causal account of a model decision or real-world phenomenon?

## Challenges for the Next Review Pass

1. Audit the paper's 287 references with explicit search, inclusion, quality, and claim-to-citation criteria rather than relying on a narrative evidence synthesis.
2. Formalize and peer-test the proxy-model paradox against counterexamples, including approximate but useful explanations that make bounded claims without promising completeness.
3. Build a comparative benchmark that measures explanation, verification, user reliance, error detection, coverage, and institutional cost across the proposed post-XAI alternatives.
